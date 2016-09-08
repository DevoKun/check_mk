
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
from tools import compare_html , gentest, compare_and_empty
from table import Table


warn, crit = 0.61245, 3.3461213
def object_title(what, av_entry):
    return "TRUE (THIS IS A TEST)"
timeline_url = "www.timeline.de"

import time
from_time = 1222.090
until_time = 1244.090

format = "%a, %d %b %Y %H:%M:%S +0000"
def render_date(ts):
    return time.strftime(format, time.localtime(ts))

title = "TEST TITLE"
pixel = 10
row_nr = 4
width = height = 100
css = "test"

def test_0():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<div class="avlegend levels">')
    old.write('<h3>%s</h3>' % _("Availability levels"))
    old.write('<div class="state state0">%s</div><div class=level>&ge; %.3f%%</div>' % (_("OK"), warn))
    old.write('<div class="state state1">%s</div><div class=level>&ge; %.3f%%</div>' % (_("WARN"), crit))
    old.write('<div class="state state2">%s</div><div class=level>&lt; %.3f%%</div>' % (_("CRIT"), crit))
    old.write('</div>')
    new.open_div(class_="avlegend levels")
    new.h3(_("Availability levels"))
    new.div(_("OK"), class_="state state0")
    new.div("&ge; %.3f%%" % warn, class_="level")
    new.div(_("WARN"), class_="state state1")
    new.div("&ge; %.3f%%" % crit, class_="level")
    new.div(_("CRIT"), class_="state state2")
    new.div("&lt; %.3f%%" % crit, class_="level")
    new.close_div()

    compare_and_empty(old, new)


def test_1():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    what = "host"
    av_entry = "4"

    old.write("<h3>%s %s</h3>" % (_("Timeline of"), object_title(what, av_entry) ))
    new.open_h3()
    new.write("%s %s" % (_("Timeline of"), object_title(what, av_entry)))
    new.close_h3()
    old.write('<div class=info>%s</div>' % _("No information available"))
    new.div(_("No information available"), class_="info")

    compare_and_empty(old, new)


def test_2a():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    what = "host"

    old.write('<div class="avlegend timeline">')
    old.write('<h3>%s</h3>' % _('Timeline colors'))
    old.write('<div class="state state0">%s</div>' % (what == "host" and _("UP") or _("OK")))
    new.open_div(class_="avlegend timeline")
    new.h3(_('Timeline colors'))
    new.div(_("UP") if what == "host" else _("OK"), class_="state state0")
    old.write('<div class="state state1">%s</div>'    % _("WARN"))
    old.write('<div class="state state2">%s</div>' % (what == "host" and _("DOWN") or _("CRIT")))
    old.write('<div class="state state3">%s</div>' % (what == "host" and _("UNREACH") or _("UNKNOWN")))
    old.write('<div class="state flapping">%s</div>' % _("Flapping"))
    new.div(_("WARN"), class_="state state1")
    new.div(_("DOWN") if what == "host" else _("CRIT"), class_="state state2")
    new.div(_("UNREACH") if what == "host" else _("UNKNOWN"), class_="state state3")
    new.div(_("Flapping"), class_="state flapping")
    old.write('<div class="state hostdown">%s</div>' % _("H.Down"))
    old.write('<div class="state downtime">%s</div>' % _("Downtime"))
    old.write('<div class="state ooservice">%s</div>' % _("OO/Service"))
    old.write('<div class="state unmonitored">%s</div>' % _("unmonitored"))
    old.write('</div>')
    new.div(_("H.Down"), class_="state hostdown")
    new.div(_("Downtime"), class_="state downtime")
    new.div(_("OO/Service"), class_="state ooservice")
    new.div(_("unmonitored"), class_="state unmonitored")
    new.close_div()

    compare_and_empty(old, new)

def test_2b():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    what = "service"

    old.write('<div class="avlegend timeline">')
    old.write('<h3>%s</h3>' % _('Timeline colors'))
    old.write('<div class="state state0">%s</div>' % (what == "host" and _("UP") or _("OK")))
    new.open_div(class_="avlegend timeline")
    new.h3(_('Timeline colors'))
    new.div(_("UP") if what == "host" else _("OK"), class_="state state0")
    old.write('<div class="state state1">%s</div>'    % _("WARN"))
    old.write('<div class="state state2">%s</div>' % (what == "host" and _("DOWN") or _("CRIT")))
    old.write('<div class="state state3">%s</div>' % (what == "host" and _("UNREACH") or _("UNKNOWN")))
    old.write('<div class="state flapping">%s</div>' % _("Flapping"))
    new.div(_("WARN"), class_="state state1")
    new.div(_("DOWN") if what == "host" else _("CRIT"), class_="state state2")
    new.div(_("UNREACH") if what == "host" else _("UNKNOWN"), class_="state state3")
    new.div(_("Flapping"), class_="state flapping")
    old.write('<div class="state hostdown">%s</div>' % _("H.Down"))
    old.write('<div class="state downtime">%s</div>' % _("Downtime"))
    old.write('<div class="state ooservice">%s</div>' % _("OO/Service"))
    old.write('<div class="state unmonitored">%s</div>' % _("unmonitored"))
    old.write('</div>')
    new.div(_("H.Down"), class_="state hostdown")
    new.div(_("Downtime"), class_="state downtime")
    new.div(_("OO/Service"), class_="state ooservice")
    new.div(_("unmonitored"), class_="state unmonitored")
    new.close_div()

    compare_and_empty(old, new)

def test_3():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<a href="%s">' % timeline_url)
    new.open_a(href=timeline_url)
    old.write('</a>')
    new.close_a()

    compare_and_empty(old, new)



def test_4a():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    style = "standalone"

    old.write('<div class="timelinerange %s">' % style)
    new.open_div(class_=["timelinerange", style])

    old.write('<div class=from>%s</div><div class=until>%s</div>' % (
    render_date(from_time), render_date(until_time)))
    new.div(render_date(from_time), class_="from")
    new.div(render_date(until_time), class_="until")

    old.write('<div title="%s" class="timelinechoord" style="left: %dpx"></div>' % (title, pixel))
    new.div('', title=title, class_="timelinechoord", style="left: %dpx" % pixel)

    old.write('<table class="timeline %s">' % style)
    old.write('<tr class=timeline>')

    new.open_table(class_=["timeline", style])
    new.open_tr(class_="timeline")

    if style == "standalone" and row_nr != None:
        hovercode = ' onmouseover="timeline_hover(this, %d, 1);" onmouseout="timeline_hover(this, %d, 0);"' % (row_nr, row_nr)
    else:
        hovercode = ""
    old.write('<td%s style="width: %.3f%%" title="%s" class="%s"></td>' % (
    hovercode, width, title, css))
    old.write("</tr></table>")
    old.write("</div>")

    td_attrs = {"style": "width: %.3f%%" % width,
                "title": title,
                "class": css,}
    if style == "standalone" and row_nr is not None:
        td_attrs.update({"onmouseover": "timeline_hover(this, %d, 1);" % row_nr,
                         "onmouseout" : "timeline_hover(this, %d, 0);" % row_nr, })
    new.td('', **td_attrs)
    new.close_tr()
    new.close_table()
    new.close_div()

    compare_and_empty(old, new)

def test_4b():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    style = ""

    old.write('<div class="timelinerange %s">' % style)
    new.open_div(class_=["timelinerange", style])

    old.write('<div class=from>%s</div><div class=until>%s</div>' % (
    render_date(from_time), render_date(until_time)))
    new.div(render_date(from_time), class_="from")
    new.div(render_date(until_time), class_="until")

    old.write('<div title="%s" class="timelinechoord" style="left: %dpx"></div>' % (title, pixel))
    new.div('', title=title, class_="timelinechoord", style="left: %dpx" % pixel)

    old.write('<table class="timeline %s">' % style)
    old.write('<tr class=timeline>')

    new.open_table(class_=["timeline", style])
    new.open_tr(class_="timeline")

    if style == "standalone" and row_nr != None:
        hovercode = ' onmouseover="timeline_hover(this, %d, 1);" onmouseout="timeline_hover(this, %d, 0);"' % (row_nr, row_nr)
    else:
        hovercode = ""
    old.write('<td%s style="width: %.3f%%" title="%s" class="%s"></td>' % (
    hovercode, width, title, css))
    old.write("</tr></table>")
    old.write("</div>")

    td_attrs = {"style": "width: %.3f%%" % width,
                "title": title,
                "class": css,}
    if style == "standalone" and row_nr is not None:
        td_attrs.update({"onmouseover": "timeline_hover(this, %d, 1);" % row_nr,
                         "onmouseout" : "timeline_hover(this, %d, 0);" % row_nr, })
    new.td('', **td_attrs)
    new.close_tr()
    new.close_table()
    new.close_div()

    compare_and_empty(old, new)

def test_5():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<h3>')
    new.open_h3()

    compare_and_empty(old, new)


