
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

pie_diameter = 6
pie_id = 4
pies = [1,2,3]
url = "www.mathias-kettner.de"
name = "TEST"
color="red"
count = "10"
nr = 5
dashlet = {'snapin': 'JO', }
content = "<tag> Hallo Tester! </tag>"

def test_0():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write(
    '<table class=dashlet_overview>'
    '<tr><td valign=top>'
    '<a href="http://mathias-kettner.de/check_mk.html"><img style="margin-right: 30px;" src="images/check_mk.trans.120.png"></a>'
    '</td>'
    '<td><h2>Check_MK Multisite</h2>'
    'Welcome to Check_MK Multisite. If you want to learn more about Multisite, please visit '
    'our <a href="http://mathias-kettner.de/checkmk_multisite.html">online documentation</a>. '
    'Multisite is part of <a href="http://mathias-kettner.de/check_mk.html">Check_MK</a> - an Open Source '
    'project by <a href="http://mathias-kettner.de">Mathias Kettner</a>.'
    '</td>'
    )
    old.write('</tr></table>')
    new.open_table(class_="dashlet_overview")
    new.open_tr()
    new.open_td(valign="top")
    new.open_a(href="http://mathias-kettner.de/check_mk.html")
    new.img(src="images/check_mk.trans.120.png", style="margin-right: 30px;")
    new.close_a()
    new.close_td()
    new.open_td()
    new.h2("Check_MK Multisite")
    new.write_html('Welcome to Check_MK Multisite. If you want to learn more about Multisite, please visit '
    'our <a href="http://mathias-kettner.de/checkmk_multisite.html">online documentation</a>. '
    'Multisite is part of <a href="http://mathias-kettner.de/check_mk.html">Check_MK</a> - an Open Source '
    'project by <a href="http://mathias-kettner.de">Mathias Kettner</a>.')
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_1():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write('<a href="http://mathias-kettner.de/check_mk.html">'
    '<img style="margin-right: 30px;" src="images/check_mk.trans.120.png"></a>')
    new.open_a(href="http://mathias-kettner.de/check_mk.html")
    new.img(style="margin-right: 30px;", src="images/check_mk.trans.120.png")
    new.close_a()

    compare_and_empty(old, new)


def test_2():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()
    old.write("<div class=stats>")
    old.write('<canvas class=pie width=%d height=%d id="%s_stats" style="float: left"></canvas>' %
    (pie_diameter, pie_diameter, pie_id))
    old.write('<img src="images/globe.png" class="globe">')
    new.open_div(class_="stats")
    new.canvas('', class_="pie", id_ = "%s_stats" % pie_id, width=pie_diameter, height=pie_diameter, style="float: left")
    new.img(src="images/globe.png", class_="globe")
    old.write('<table class="hoststats%s" style="float:left">' % (
    len(pies) > 1 and " narrow" or ""))
    new.open_table(class_=["hoststats"] + (["narrow"] if len(pies) > 0 else []), style="float:left")

    compare_and_empty(old, new)


def test_3():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    new.open_tr()
    new.open_th()
    new.open_a(href=url)
    new.write(name) # TODO: Escapable?
    new.close_a()
    new.close_th()
    new.open_td(class_="color", style="background-color: %s" % color if color else '')
    new.close_td()
    old.write('<tr><th><a href="%s">%s</a></th>' % (url, name))
    style = ''
    if color:
        style = ' style="background-color: %s"' % color
    old.write('<td class=color%s>'
    '</td><td><a href="%s">%s</a></td></tr>' % (style, url, count))
    new.open_td()
    new.open_a(href = url)
    new.write(count)  # TODO
    new.close_a()
    new.close_td()
    old.write("</table>")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_4():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    new.close_div()
    old.write("</div>")

    compare_and_empty(old, new)


def test_5():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write('<div id="dashlet_graph_%d"></div>' % (nr))
    new.div('', id_="dashlet_graph_%d" % nr)

    compare_and_empty(old, new)


def test_6():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write("<div class=nodata><div class=msg>")
    new.open_div(class_="nodata")
    new.open_div(class_="msg")
    old.write("</div></div>")
    new.close_div()
    new.close_div()

    compare_and_empty(old, new)


def test_7():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write('<body class="side">\n')
    old.write('<div id="check_mk_sidebar">\n')
    old.write('<div id="side_content">\n')
    old.write("<div id=\"snapin_container_%s\" class=snapin>\n" % dashlet['snapin'])
    old.write("<div id=\"snapin_%s\" class=\"content\">\n" % (dashlet['snapin']))
    new.open_body(class_="side")
    new.open_div(id_ = "check_mk_sidebar")
    new.open_div(id_="side_content")
    new.open_div(id_="snapin_container_%s" % dashlet['snapin'], class_="snapin")
    new.open_div(id_="snapin_%s" % dashlet['snapin'], class_="content")
    old.write('</div>\n')
    old.write('</div>\n')
    old.write('</div>\n')
    old.write('</div>\n')
    new.close_div()
    new.close_div()
    new.close_div()
    new.close_div()

    compare_and_empty(old, new)


def test_8():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write('<div class="notify_users">')
    new.open_div(class_="notify_users")

    compare_and_empty(old, new)


def test_9():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write("</div>")
    new.close_div()

    compare_and_empty(old, new)


def test_10():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write('<div class="has_failed_notifications">'
    '  <div class="failed_notifications_inner">%s</div>'
    '</div>' % content)
    new.open_div(class_="has_failed_notifications")
    new.open_div(class_="failed_notifications_inner")
    new.write(content)
    new.close_div()
    new.close_div()

    compare_and_empty(old, new)

