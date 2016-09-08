
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

odd = "odd"
content = "<tag> content <content/> </tag>"
rendered_cells = [ ("test_css", "<content/"), ("test_css", "<content count=\"1\"/>"), ("test_css", "<content count=\"2\"/>") ]
cells = ["cell0", "cell1", "cell2"]
rows = cells
num_columns = 2

def test_0():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    odd = "odd"
    old.write('<table class="mobile data">')
    new.open_table(class_="mobile data")

    # Paint header

    # Paint data rows
    for row in rows:
        odd = odd == "odd" and "even" or "odd"
        old.write('<tr class="%s0">' % odd)
        new.open_tr(class_="%s0" % odd)
        for n, cell in enumerate(cells):
            if n > 0 and n % num_columns == 0:
                old.write('</tr><tr class="%s0">' % odd)
                new.close_tr()
                new.open_tr(class_="%s0" % odd)
            if n == len(cells) - 1 and n % num_columns != (num_columns - 1):
                tdattrs = 'colspan="%d"' % (num_columns - (n % num_columns))
            else:
                tdattrs = ""
        old.write('</row>')
        new.close_row()
    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_1():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    odd = "odd"
    old.write('<ul class="mobilelist" data-role="listview">\n')
    new.open_ul(**{"class_":"mobilelist", "data-role":"listview"})

    # Paint data rows
    for row in rows:
        old.write('<li>')
        new.open_li()
        if rendered_cells: # First cell (assumedly state) is left
            old.write('<p class="ui-li-aside ui-li-desc %s">%s</p>' % rendered_cells[0])
            rendered_class, rendered_content = rendered_cells[0]
            new.open_p(class_="ui-li-aside ui-li-desc %s" % rendered_class)
            new.write(rendered_content)
            new.close_p()

            if len(rendered_cells) > 1:
                content = " &middot; ".join([ rendered_cell[1] for rendered_cell
                                              in rendered_cells[1:num_columns+1]])
                old.write('<h3>%s</h3>' % content)
                new.open_h3()
                new.write(content)
                new.close_h3()

                for rendered_cell, cell in zip(rendered_cells[num_columns+1:],
                                               cells[num_columns+1:]):
                    old.write('<p class="ui-li-desc">')
                    rendered_class, rendered_content = rendered_cell
                    new.open_p(class_="ui-li-desc")
                    old.write(': <span class="%s">%s</span></p>\n' % rendered_cell)
                    new.write(': ')
                    new.open_span(class_=rendered_class)
                    new.write(rendered_content)
                    new.close_span()
                    new.close_p()

        old.write('</li>\n')
        new.close_li()
    old.write('</ul>')
    new.close_ul()

    compare_and_empty(old, new)


def test_2():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()

    for row in rows:
        old.write('<table class=dataset>')
        new.open_table(class_="dataset")
        for i, cell in enumerate(cells):
            tdclass, content = rendered_cells[i]
            if not content:
                continue # Omit empty cells

            old.write('<tr class=header>')
            old.write('<th>%s</th></tr>\n' % cell)
            old.write('<tr class=data>')
            new.open_tr(class_="header")
            new.open_th()
            new.write(cell)
            new.close_th()
            new.close_tr()

            new.open_tr(class_="data")
            old.write('</tr>\n')
            new.close_tr()

        old.write('</table>')
        new.close_table()

    compare_and_empty(old, new)

