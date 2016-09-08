#!/usr/bin/env python
# encoding: utf-8

import pytest
import cProfile
from testlib import web
import json
import time


def timeit(method):
    # https://www.andreas-jung.com/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print '%r %2.2f sec' % \
              (method.__name__, te-ts)
        return result
    return timed


@timeit
def timetest(site, web, test_nr, load_5k=False, printout = False):

    try:
        if not load_5k:
            r = web.get("view.py?view_name=allservices_test_%d" %test_nr)
        else:
            r = web.get("view.py?check_command=&host_regex=&is_host_in_notification_period=-1&is_in_downtime=-1&is_service_acknowledged=-1&is_service_active_checks_enabled=-1&is_service_in_notification_period=-1&is_service_in_service_period=-1&is_service_is_flapping=-1&is_service_notifications_enabled=-1&is_service_scheduled_downtime_depth=-1&limit=hard&neg_host_regex=&neg_opthost_group=&neg_optservice_group=&neg_service_output=&neg_service_regex=&opthost_group=&optservice_group=&selection=1c0643ed-ec85-43ff-8c38-833b1cd8d763&service_output=&service_regex=&site=&st0=on&st1=on&st2=on&st3=on&stp=on&view_name=allservices_test_%d" %test_nr)
        if printout:
            with open('allservices_test.html', 'w') as outfile:
                outfile.write(r.text.encode('utf8'))
    except Exception as e:
        print e.message()


def test_tables(site, web):


    load_5k = not True
    do_profile = False

    try:
        web.add_host("test-host", attributes={
            "ipaddress": "127.0.0.1",
        })
        hosts = web.get_all_hosts()
        web.discover_services("test-host")

        for test in [1,2,3,4]:
            if do_profile:
                profile = cProfile.Profile()
                profile.runctx("ttf(site, web, test_nr, load_5k=lfk)", \
                                        {'ttf': timetest}, \
                                        {'site': site, 'web': web, 'test_nr': test, 'lfk': load_5k})
                profile.dump_stats("speedtest_table_test_%d%s.cprof"%(test, "_5k"*load_5k))
            else:
                timetest(site, web, test, load_5k=load_5k)

    finally:
        web.delete_host("test-host")






