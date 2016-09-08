
#!/usr/bin/python
# call using
# > py.test -s -k test_html_generator.py

# enable imports from web directory
from testlib import cmk_path
import sys
sys.path.insert(0, "%s/web/htdocs" % cmk_path())

# external imports
import re
from bs4 import BeautifulSoup as bs

# internal imports
from classes import HTMLOrigTester, HTMLCheck_MKTester
from tools import compare_html, gentest, compare_and_empty, prettify
from table import Table


from collections import defaultdict

info = defaultdict(str)
info["time"] = 12.4456
details=defaultdict(str)
title = "TEST"
content = "<tag> LOL </tag>"
format_bool = id
format_params = id
import time
version_title = "1.2.3.4.5."
joined_paths = ["one", "two"]

for key in ["crash_type", "os", "crash_type", "crash_type", "os", "crash_type", "version", "exc_type", "exc_value", "exc_traceback", "version", "exc_type", "exc_value", "exc_traceback", "local_vars", "local_vars", "python_paths", "Unknown", "details", "host", "check_type", "host", "check_type", "item", "description", "params", "item", "description", "params", "details", "page", "page", "vars", "username", "user_agent", "is_mobile", "is_ssl_request", "language", "username", "user_agent", "is_mobile", "is_ssl_request", "language"]:
    info[key] = key
    details[key] = key




def test_0():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<p>%s</p>" %
                    _("An internal error occured while processing your request. "
                     "You can report this issue to the Check_MK team to help "
                     "fixing this issue. Please use the form below for reporting."))
    new.p(_("An internal error occured while processing your request. "
                 "You can report this issue to the Check_MK team to help "
                 "fixing this issue. Please use the form below for reporting."))

    compare_and_empty(old, new)


def test_1():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<h3>%s</h3>' % title)
    old.write('<div class=log_output>%s</div>'
               % (content).replace("\n", "<br>").replace(' ', '&nbsp;'))
    new.h3(title)
    new.open_div(class_="log_output")
    new.write((content).replace("\n", "<br>").replace(' ', '&nbsp;'))
    new.close_div()


    compare_and_empty(old, new)


def test_2():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<div id=\"pending_msg\" style=\"display:none\">")
    new.open_div(id_="pending_msg", style="display:none")
    old.write("</div>")
    old.write("<div id=\"success_msg\" style=\"display:none\">")
    new.close_div()
    new.open_div(id_="success_msg", style="display:none")


    compare_and_empty(old, new)


def test_3():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>")
    old.write("<div id=\"fail_msg\" style=\"display:none\">")
    new.close_div()
    new.open_div(id_="fail_msg", style="display:none")
    old.write("</div>")
    new.close_div()


    compare_and_empty(old, new)


def _crash_row(old, new, title, infotext, odd=True, legend=False, pre=False):
    trclass = "data odd0" if odd else "data even0"
    tdclass = "left legend" if legend else "left"
    new.open_tr(class_=trclass)
    new.td(title, class_=tdclass)
    if pre:
        new.td( new.render_pre(infotext) )
    else:
        new.td(infotext)
    new.close_tr()


def test_4():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write("<h2>%s</h2>" % _("Crash Report"))
    old.write("<table class=\"data\">")
    new.h2(_("Crash Report"))
    new.open_table(class_="data")

    old.write("<tr class=\"data even0\"><td class=\"left legend\">%s</td>" % _("Crash Type"))
    old.write("<td>%s</td></tr>" % (info["crash_type"]))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Time"))
    old.write("<td>%s</td></tr>" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["time"])))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Operating System"))
    old.write("<td>%s</td></tr>" % (info["os"]))
    _crash_row(old, new, _("Crash Type"), info["crash_type"], odd=False,  legend=True)
    _crash_row(old, new, _("Time"), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["time"])), odd=True)
    _crash_row(old, new, _("Operating System"), info["os"], False)

    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % version_title)
    old.write("<td>%s</td></tr>" % (info["version"]))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Python Version"))
    old.write("<td>%s</td></tr>" % (info.get("python_version", _("Unknown"))))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Exception"))
    old.write("<td><pre>%s (%s)</pre></td></tr>" % ((info["exc_type"]), old.attrencode(info["exc_value"])))

    _crash_row(old, new, version_title, info["version"], True)
    _crash_row(old, new, _("Python Version"), info.get("python_version", _("Unknown")), False)
    _crash_row(old, new, _("Exception"), "%s (%s)" % (info["exc_type"], info["exc_value"]), odd=True, pre=True)

    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Traceback"))
    old.write("<td><pre>%s</pre></td></tr>" % ((info["exc_traceback"])))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Local Variables"))
    old.write("<td><pre>%s</pre></td></tr>" % ((info["local_vars"])))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Python Module Paths"))

    _crash_row(old, new, _("Traceback"), (info["exc_traceback"]), odd=False, pre=True)
    _crash_row(old, new, _("Local Variables"), (info["local_vars"]), odd=True, pre=True)
    _crash_row(old, new, _("Python Module Paths"), joined_paths, odd=False)
    old.write("<td>%s</td></tr>" % joined_paths)

    old.write("</table>")
    new.close_table()

#    print '%s\n%s' % (prettify(old.plugged_text), new.plugged_text)

    compare_and_empty(old, new)


def test_5():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<h2>%s</h2>" % _("Details"))
    old.write("<table class=\"data\">")
    old.write("<tr class=\"data even0\"><td class=\"left legend\">%s</td>" % _("Host"))
    old.write("<td>%s</td></tr>" % (details["host"]))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Is Cluster Host"))
    old.write("<td>%s</td></tr>" % format_bool(details.get("is_cluster")))
    new.h2(_("Details"))
    new.open_table(class_="data")
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Check Type"))
    old.write("<td>%s</td></tr>" % (details["check_type"]))
    _crash_row(old, new, _("Host"), details["host"], odd=False, legend=True)
    _crash_row(old, new, _("Is Cluster Host"), format_bool(details.get("is_cluster")), odd=True)
    _crash_row(old, new, _("Check Type"), details["check_type"], odd=False)
    _crash_row(old, new, _("Manual Check"), format_bool(details.get("manual_check")), odd=True, pre=True)
    _crash_row(old, new, _("Uses SNMP"), format_bool(details.get("uses_snmp")), odd=False, pre=True)
    _crash_row(old, new, _("Inline-SNMP"), format_bool(details.get("inline_snmp")), odd=True, pre=True)
    _crash_row(old, new, _("Check Item"), details["item"], odd=False)
    _crash_row(old, new, _("Description"), details["description"], odd=True)
    _crash_row(old, new, _("Parameters"), format_params(details["params"]), odd=False, pre=True)
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Manual Check"))
    old.write("<td><pre>%s</pre></td></tr>" % format_bool(details.get("manual_check")))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Uses SNMP"))
    old.write("<td><pre>%s</pre></td></tr>" % format_bool(details.get("uses_snmp")))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Inline-SNMP"))
    old.write("<td><pre>%s</pre></td></tr>" % format_bool(details.get("inline_snmp")))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Check Item"))
    old.write("<td>%s</td></tr>" % (details["item"]))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Description"))
    old.write("<td>%s</td></tr>" % (details["description"]))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Parameters"))
    old.write("<td><pre>%s</pre></td></tr>" % (format_params(details["params"])))
    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_6():

    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<h2>%s</h2>" % _("Details"))
    old.write("<table class=\"data\">")
    old.write("<tr class=\"data even0\"><td class=\"left legend\">%s</td>" % _("Page"))
    old.write("<td>%s</td></tr>" % (details["page"]))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Request Method"))
    old.write("<td>%s</td></tr>" % (details.get("request_method", _("Unknown"))))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("HTTP Parameters"))
    old.write("<td>")
    new.h2(_("Details"))
    new.open_table(class_="data")
    _crash_row(old, new, _("Page"), details["page"], odd=False, legend=True)
    _crash_row(old, new, _("Request Method"), details.get("request_method", _("Unknown")))
    new.open_tr(class_="data even0")
    new.td(_("HTTP Parameters"), class_="left")
    new.open_td()
    old.write("</td></tr>")
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("Referer"))
    old.write("<td>%s</td></tr>" % (details.get("referer", _("Unknown"))))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Username"))
    old.write("<td>%s</td></tr>" % (details["username"]))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("User Agent"))
    old.write("<td>%s</td></tr>" % (details["user_agent"]))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Mobile GUI"))
    old.write("<td>%s</td></tr>" % (details["is_mobile"]))
    old.write("<tr class=\"data odd0\"><td class=\"left\">%s</td>" % _("SSL"))
    old.write("<td>%s</td></tr>" % (details["is_ssl_request"]))
    old.write("<tr class=\"data even0\"><td class=\"left\">%s</td>" % _("Language"))
    old.write("<td>%s</td></tr>" % (details["language"]))
    old.write("</table>")
    new.close_td()
    new.close_tr()
    _crash_row(old, new, _("Referer"), details.get("referer", _("Unknown")))
    _crash_row(old, new, _("Username"), details["username"], odd=False)
    _crash_row(old, new, _("User Agent"), details["user_agent"])
    _crash_row(old, new, _("Mobile GUI"), details["is_mobile"], odd=False)
    _crash_row(old, new, _("SSL"), details["is_ssl_request"])
    _crash_row(old, new, _("Language"), details["language"], odd=False)
    new.close_table()

    compare_and_empty(old, new)

