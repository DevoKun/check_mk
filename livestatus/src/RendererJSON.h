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

#ifndef RendererJSON_h
#define RendererJSON_h

#include "config.h"  // IWYU pragma: keep
#include <string>
#include <vector>
#include "OutputBuffer.h"
#include "Renderer.h"

class RendererJSON : public Renderer {
public:
    RendererJSON(OutputBuffer *output,
                 OutputBuffer::ResponseHeader response_header,
                 bool do_keep_alive, std::string invalid_header_message,
                 int timezone_offset);

private:
    void outputNull() override;
    void outputBlob(const std::vector<char> &value) override;
    void outputString(const std::string &value) override;

    void startQuery() override;
    void separateQueryElements() override;
    void endQuery() override;

    void startRow() override;
    void separateRowElements() override;
    void endRow() override;

    void startList() override;
    void separateListElements() override;
    void endList() override;

    void startSublist() override;
    void separateSublistElements() override;
    void endSublist() override;

    void startDict() override;
    void separateDictElements() override;
    void separateDictKeyValue() override;
    void endDict() override;
};

#endif  // RendererJSON_h