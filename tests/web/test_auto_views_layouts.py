
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
from tools import compare_html , gentest, compare_and_empty, prettify
from table import Table


row_id = lambda a, b: "%s_%s" % (a, b)
view = "view"
row = "row"
rows = ["1", "2", "3"]
num_tds = 3
num_columns = 3
odd = "odd"
cell = "cell"
num_cells = 4
thispart = "blabla"
css_classes = ["css", "test"]
css_class = "test"
is_open = True
trclass = "row"
tdclass = "col"
index = 1
num_rows = 3
sclass = "class"
rendered = [  ["1", "2", "3", "4", "5", "6"], ["1", "2", "3", "4", "5", "6"], ["1", "2", "3", "4", "5", "6"], ["1", "2", "3", "4", "5", "6"], ["1", "2", "3", "4", "5", "6"] ]
css = "lol"
cont = "TRUE"
content = "HALLO TEST!"




def test_0():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<input type=checkbox name=\"%s\" value=%d />" %
                                    (row_id(view, row), num_tds + 1))
    new.input(type_="checkbox", name=row_id(view, row), value=(num_tds+1))
    old.write("<td class=checkbox>")
    new.open_td(class_="checkbox")
    old.write("</td>")
    new.close_td()
    old.write("<th><input type=button class=checkgroup name=_toggle_group"
               " onclick=\"toggle_group_rows(this);\" value=\"%s\" /></th>" % _('X'))
    new.open_th()
    new.input(type_="button", class_="checkgroup", name="_toggle_group", 
               onclick="toggle_group_rows(this);", value=_('X'))
    new.close_th()

    compare_and_empty(old, new)


def test_1():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<table class="data single">\n')
    new.open_table(class_="data single")
    old.write("<tr class=gap><td class=gap colspan=%d></td></tr>\n" % (1 + num_columns))
    new.open_tr(class_="gap")
    new.td("", class_="gap", colspan=(num_columns + 1))
    new.close_tr()
    old.write('<tr class="data %s0">' % odd)
    new.open_tr(class_="data %s0" % odd)
    old.write("<td class=left>%s</td>" % cell)
    new.open_td(class_="left")
    new.write(cell)
    new.close_td()
    old.write("<td class=gap style=\"border-style: none;\" colspan=%d></td>" % (1 + num_columns - len(thispart)))
    old.write("</tr>\n")
    new.td('', class_="gap", style="border-style: none;", colspan=(1 + num_columns - len(thispart)))
    new.close_tr()
    old.write("</table>\n")
    old.write("</div>\n")
    new.close_table()
    new.close_div()

    compare_and_empty(old, new)


def test_2():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    old.write("<table class=groupheader cellspacing=0 cellpadding=0 border=0><tr class=groupheader>")
    new.open_table(class_="groupheader", cellspacing=0,  cellpadding=0, border=0)
    new.open_tr(class_="groupheader")
    old.write("<td>,</td>")
    new.td(",")
    old.write("</tr></table>\n")
    new.close_tr()
    new.close_table()
    old.write("<table class=data>")
    new.open_table(class_="data")
    old.write("<tr>")
    new.open_tr()
    old.write("</tr>\n")
    new.close_tr()

    hide = " style=\"display:none\""
    hide_new = "display:none"

    old.write('<tr class="data %s"%s>' % (" ".join(css_classes), hide))
    new.open_tr(class_=["data"] + css_classes, style=hide_new)

    compare_and_empty(old, new)


def test_5():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()
    old.write("</table>\n")
    new.close_table()
    old.write("<table class=\"boxlayout%s\"><tr>" % (css_class and " "+css_class or ""))
    new.open_table(class_=["boxlayout", css_class if css_class else ''])
    new.open_tr()
    old.write("<td class=boxcolumn>")
    new.open_td(class_="boxcolumn")
    old.write("</td>")
    old.write("</tr></table>\n")
    new.close_td()
    new.close_tr()
    new.close_table()
    closed_class = not is_open and " closed" or ""
    old.write("<tr class=\"data grouped_row_header%s %s0\">" %
                                            (closed_class, trclass))
    old.write("<td colspan=\"%d\" onclick=\"toggle_grouped_rows("
               "'grouped_rows', '%s', this, %d)\">" %
                (num_cells, index, num_rows))
    old.write('<img align=absbottom class="treeangle nform %s" src="images/tree_black_closed.png">' %
                                    ("open" if is_open else "closed"))
    old.write("%s (%d)</td>" % ("title", num_rows))
    old.write("</tr>")
    new.open_tr(class_=["data", "grouped_row_header", "closed" if not is_open else '', "%s0" % trclass])
    new.open_td(colspan=num_cells, 
                 onclick="toggle_grouped_rows('grouped_rows', '%s', this, %d)" % (index, num_rows))
    new.img(align="absbottom", class_=["treeangle", "nform", "open" if is_open else "closed"], src="images/tree_black_closed.png")
    new.write("%s (%d)" % ("title", num_rows))
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_6():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<table class=\"data tiled\">\n")
    new.open_table(class_="data tiled")

    old.write("</td></tr>\n")
    old.write("<tr><td><table class=groupheader><tr class=groupheader>")
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td()
    new.open_table(class_="groupheader")
    new.open_tr(class_="groupheader")
    old.write("<td>,</td>")
    new.td(',')
    old.write('</tr></table></td></tr>'
                           '<tr><td class=tiles>\n')
    new.close_tr()
    new.close_table()
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td(class_="tiles")

    old.write("<tr><td class=tiles>")
    new.open_tr()
    new.open_td(class_="tiles")
    old.write('<div class="tile %s"><table>' % sclass)
    new.open_div(class_=["tile", sclass])
    new.open_table()

    old.write("<tr><td class=\"tl %s\">" % (rendered[1][0],))
    new.open_tr()
    new.open_td(class_=["tl", rendered[1][0]])
    old.write("%s</td><td class=\"tr %s\">%s</td></tr>\n" % \
                    (rendered[1][1], rendered[2][0], rendered[2][1]))
    old.write("<tr><td colspan=2 class=\"center %s\">%s</td></tr>\n" % \
                    (rendered[0][0], rendered[0][1]))
    new.write("%s" % rendered[1][1])
    new.close_td()
    new.open_td(class_=["tr", rendered[2][0]])
    new.write("%s" % rendered[2][1])
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td(colspan=2, class_=["center", rendered[0][0]])
    new.write("%s" % rendered[0][1])
    new.close_td()
    new.close_tr()
    old.write("<tr><td colspan=2 class=\"cont %s\">%s</td></tr>\n" % \
                        (css, cont))
    old.write("<tr><td class=\"bl %s\">%s</td><td class=\"br %s\">%s</td></tr>\n" % \
                    (rendered[3][0], rendered[3][1], rendered[4][0], rendered[4][1]))
    old.write("</table></div>\n")
    new.open_tr()
    new.open_td(colspan=2, class_=["cont", css])
    new.write("%s" % cont)
    new.close_td()
    new.close_tr()
    new.open_tr()
    new.open_td(class_=["bl", rendered[3][0]])
    new.write("%s" % rendered[3][1])
    new.close_td()
    new.open_td(class_=["br", rendered[4][0]])
    new.write("%s" % rendered[4][1])
    new.close_td()
    new.close_tr()
    new.close_table()
    new.close_div()
    old.write("</td></tr>\n")
    old.write("</table>\n")
    new.close_td()
    new.close_tr()
    new.close_table()

    #print '%s\n%s' % (prettify(old.plugged_text), new.plugged_text)

    compare_and_empty(old, new)


def test_10():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<table class='data table'>\n")
    new.open_table(class_='data table')

    old.write("<tr>")
    new.open_tr()
    old.write('<th></th>')
    new.th('')
    old.write('<td class=gap></td>')
    new.td('', class_="gap")
    old.write("</tr>\n")
    new.close_tr()


    old.write('<td class=gap></td>')
    old.write("<td class=fillup colspan=%d></td>" % num_cells)
    old.write("</tr>\n")
    new.td('', class_="gap")
    new.td('', class_="fillup", colspan=num_cells)
    new.close_tr()


    old.write("<tr class=groupheader>")
    old.write("<td class=groupheader colspan=%d><table class=groupheader cellspacing=0 cellpadding=0 border=0><tr>" %
                         (num_cells * (num_columns + 2) + (num_columns - 1)))
    new.open_tr(class_="groupheader")
    new.open_td(class_="groupheader", colspan=(num_cells * (num_columns + 2) + (num_columns - 1)))
    new.open_table(class_="groupheader", cellspacing=0, cellpadding=0, border=0)
    new.open_tr()
    old.write("<td>,</td>")
    new.td(',')
    old.write("</tr></table></td></tr>\n")
    new.close_tr()
    new.close_table()
    new.close_td()
    new.close_tr()

    old.write("</tr>\n")
    new.close_tr()

    hide = " style=\"display:none\""
    hide_new = "display:none"
    old.write('<tr class="data %s"%s>' % (" ".join(css_classes), hide))
    new.open_tr(class_=["data"] + css_classes, style=hide_new)
    old.write('<td class=gap></td>')
    new.open_td(class_="gap")
    new.close_td()


    old.write('<td class=gap></td>')
    old.write("<td class=fillup colspan=%d></td>" % num_cells)
    old.write("</tr>\n")
    old.write("</table>\n")
    new.td('', class_="gap")
    new.td('', class_="fillup", colspan=num_cells)
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_18():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<table class="data matrix">')
    new.open_table(class_="data matrix")
    old.write('<tr class="data %s0">' % odd)
    old.write('<td class=matrixhead>%s</td>' % cell)
    new.open_tr(class_="data %s0" % odd)
    new.open_td(class_="matrixhead")
    new.write(cell)
    new.close_td()

    compare_and_empty(old, new)


def test_19():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<td class="left %s">%s</td>' % (tdclass, content))
    old.write("</tr>")
    new.open_td(class_=["left", tdclass])
    new.write(content)
    new.close_td()
    new.close_tr()

    compare_and_empty(old, new)


def test_20():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('<tr class="data %s0">' % odd)
    new.open_tr(class_="data %s0" % odd)
    old.write('<td class="left %s">%s</td>' % (tdclass, content))
    new.open_td(class_=["left", tdclass])
    new.write(content)
    new.close_td()
    old.write("<td></td>")
    new.td('')
    old.write("<td class=cell><table>")
    new.open_td(class_="cell")
    new.open_table()

    compare_and_empty(old, new)


def test_21():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("<tr>")
    old.write('<td class="%s">%s</td>' % (tdclass, content))
    new.open_tr()
    new.open_td(class_=tdclass)
    new.write(content)
    new.close_td()
    old.write("</tr>")
    new.close_tr()
    old.write("</table></td>")
    old.write('</tr>')
    new.close_table()
    new.close_td()
    new.close_tr()
    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)

