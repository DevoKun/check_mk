
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


whatname = "WUT!?!"
title = "TITLE"


def test_0():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_1():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr>')
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_2():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr>')
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_3():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr>')
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)



def test_5():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    old.write("<tr><td>")
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td()
    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_6():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr></table>')
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_7():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_8():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td><td>')
    new.close_td()
    new.open_td()
    old.write('</td></tr></table>')
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_9():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td><td>')
    new.close_td()
    new.open_td()
    old.write('</td><td>')
    new.close_td()
    new.open_td()

    compare_and_empty(old, new)


def test_10():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td><td>')
    new.close_td()
    new.open_td()
    old.write('</td><td>')
    new.close_td()
    new.open_td()

    compare_and_empty(old, new)


def test_11():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td><td>")
    new.close_td()
    new.open_td()

    compare_and_empty(old, new)


def test_12():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_13():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_14():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_15():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_16():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_17():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_18():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr></table>')
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_19():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<tr><td>")
    new.open_tr()
    new.open_td()
    old.write('</td></tr>')
    old.write("<tr><td>")
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td()
    old.write('</td></tr>')
    old.write('<tr><td>')
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td()
    old.write("</td><td>")
    new.close_td()
    new.open_td()
    old.write('</td></tr>')
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_20():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_21():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_22():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_23():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr></table>')
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_24():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<tr><td>')
    new.open_tr()
    new.open_td()

    compare_and_empty(old, new)


def test_25():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<tr><td>')
    new.open_tr()
    new.open_td()
    old.write('</td><td>')
    new.close_td()
    new.open_td()

    compare_and_empty(old, new)


def test_26():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_27():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_28():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_29():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_30():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td></tr>')
    new.close_td()
    new.close_tr()
    old.write('</td></tr>')
    new.close_td()
    new.close_tr()
    old.write('</td></tr>')
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_31():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write(" <nobr>")
    new.open_nobr()

    compare_and_empty(old, new)


def test_32():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<br><br>")
    new.br()
    new.br()

    compare_and_empty(old, new)


def test_33():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<div class=multigroup>')
    new.open_div(class_="multigroup")
    old.write(" <nobr>")
    new.open_nobr()

    compare_and_empty(old, new)


def test_34():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write(" <nobr>")
    new.open_nobr()

    compare_and_empty(old, new)


def test_35():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<table class=filtertime>")
    new.open_table(class_="filtertime")
    old.write("<tr><td>%s:</td>" % whatname)
    new.open_tr()
    new.open_td()
    new.write("%s:" % whatname)
    new.close_td()
    old.write("</td><td>")
    new.close_td()
    new.open_td()
    old.write("</td></tr>")
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_36():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<table cellspacing=0 cellpadding=0>")
    new.open_table(cellspacing=0, cellpadding=0)

    compare_and_empty(old, new)


def test_37():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<td></td></tr>")
    new.open_td()
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_38():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<table class=alertstatefilter><tr><td>")
    new.open_table(class_="alertstatefilter")
    new.open_tr()
    new.open_td()
    old.write("<u>%s:</u></td><td>" % title)
    new.u("%s:" % title)
    new.close_td()
    new.open_td()
    old.write("</td><td>")
    new.close_td()
    new.open_td()
    old.write("</td></tr></table>")
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_39():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<tr><td>')
    new.open_tr()
    new.open_td()
    old.write('</td><td>')
    new.close_td()
    new.open_td()
    old.write('</td><td>')
    new.close_td()
    new.open_td()
    old.write('</td></tr>')
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_40():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td><td>")
    new.close_td()
    new.open_td()
    old.write("</td><td>")
    new.close_td()
    new.open_td()

    compare_and_empty(old, new)

