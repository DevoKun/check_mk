// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// tails. You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

// Needed for localtime_r
#define _XOPEN_SOURCE 500

#include "Logger.h"

#ifdef CMC

#include <sys/time.h>
#include <syslog.h>
#include <cerrno>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <mutex>
#include <string>

using std::lock_guard;
using std::mutex;
using std::string;

namespace {
FILE *g_logfile = nullptr;
std::mutex g_logfile_mutex;
int g_log_level = 5;
bool g_log_microtime = false;
}  // namespace

void set_log_config(int log_level, bool log_microtime) {
    g_log_level = log_level;
    g_log_microtime = log_microtime;
}

void open_logfile(const string &path) {
    g_logfile = fopen(path.c_str(), "a");
    if (g_logfile == nullptr) {
        logger(LOG_WARNING,
               "Cannot open logfile " + path + ": " + strerror(errno));
    }
}

void close_logfile() {
    if (g_logfile != nullptr) {
        fclose(g_logfile);
        g_logfile = nullptr;
    }
}

// Called during a logfile rotation, triggered by an external command.
// This should only do somehting in case the logfile is really open.
void reopen_logfile(const string &path) {
    if (g_logfile != nullptr) {
        close_logfile();
        open_logfile(path);
        logger(LOG_NOTICE, "Reopened logfile.");
    }
}

bool should_log(int priority) { return priority <= g_log_level; }

void logger(int priority, const string &message) {
    if (!should_log(priority)) {
        return;  // msg not important enough
    }

    FILE *logfile = get_logfile();

    // Make sure that loglines are not garbled up, Livestatus threads also
    // log...
    lock_guard<mutex> lg(g_logfile_mutex);
    struct timeval tv;
    gettimeofday(&tv, nullptr);
    time_t t = tv.tv_sec;
    struct tm lt;
    localtime_r(&t, &lt);
    char datestring[32];
    strftime(datestring, sizeof(datestring), "%Y-%m-%d %H:%M:%S ", &lt);
    fputs(datestring, logfile);
    if (g_log_microtime) {
        fprintf(logfile, "%03ld.%03ld ", tv.tv_usec / 1000, tv.tv_usec % 1000);
    }
    fprintf(logfile, "[%d] ", priority);
    fputs(message.c_str(), logfile);
    fputc('\n', logfile);
    fflush(logfile);
}

FILE *get_logfile() { return g_logfile != nullptr ? g_logfile : stdout; }

#else

#include <pthread.h>
#include <cstdio>
#include <syslog.h>
#include <cerrno>
#include <cstring>
#include <ctime>
#include <string>
#include "nagios.h"

using std::string;

pthread_t g_mainthread_id;
static FILE *fl_logfile = nullptr;

void open_logfile(const string &path) {
    // needed to determine main thread later
    g_mainthread_id = pthread_self();

    fl_logfile = fopen(path.c_str(), "a");
    if (fl_logfile == nullptr) {
        logger(LOG_WARNING,
               "Cannot open logfile " + path + ": " + strerror(errno));
    }
}

void close_logfile() {
    if (fl_logfile != nullptr) {
        fclose(fl_logfile);
        fl_logfile = nullptr;
    }
}

void logger(int /*priority*/, const string &message) {
    // Only the main process may use the Nagios log methods
    if (fl_logfile == nullptr || g_mainthread_id == pthread_self()) {
        // TODO(sp) The Nagios headers are (once again) not const-correct...
        write_to_all_logs(
            const_cast<char *>(("livestatus: " + message).c_str()),
            NSLOG_INFO_MESSAGE);
    } else if (fl_logfile != nullptr) {
        char timestring[64];
        time_t now_t = time(nullptr);
        struct tm now;
        localtime_r(&now_t, &now);
        strftime(timestring, 64, "%F %T ", &now);
        fputs((timestring + message + "\n").c_str(), fl_logfile);
        fflush(fl_logfile);
    }
}

#endif