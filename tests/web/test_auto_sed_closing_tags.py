
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

def test_0():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_1():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_2():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_3():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_4():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_5():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</ul>\n')
    new.close_ul()
    old.write('</li>\n')
    new.close_li()

    compare_and_empty(old, new)


def test_6():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>\n")
    new.close_ul()
    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_7():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td>')
    new.close_td()

    compare_and_empty(old, new)


def test_8():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_9():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    featured_tag_names = ['html', 'head', 'body', 'header', 'footer',\
    'div', 'a', 'script', 'form', 'button',\
    'table', 'th', 'tr', 'td', 'ul', 'li']
    featured_tag_names = ['html', 'head', 'body', 'header', 'footer', 'center',\
    'div', 'a', 'b', 'script', 'form', 'button', 'p', 'span', \
    'table', 'th', 'tr', 'td', 'row', 'ul', 'li', 'br', 'nobr']

    compare_and_empty(old, new)


def test_10():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</div>\n')
    new.close_div()
    old.write("</div>\n")
    new.close_div()
    old.write("</div>\n")
    new.close_div()
    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_11():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>\n")
    new.close_table()

    compare_and_empty(old, new)


def test_12():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</div>\n')
    new.close_div()
    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_13():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>\n") # close content
    new.close_div() # close content

    compare_and_empty(old, new)


def test_14():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</ul>')
    new.close_ul()

    compare_and_empty(old, new)


def test_15():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</ul>\n')
    new.close_ul()
    old.write('</ul>\n')
    new.close_ul()

    compare_and_empty(old, new)


def test_16():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</li>')
    old.write("</ul>\n")
    new.close_li()
    new.close_ul()

    compare_and_empty(old, new)


def test_17():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</li>")
    new.close_li()

    compare_and_empty(old, new)


def test_18():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_19():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</div>\n')
    new.close_div()

    compare_and_empty(old, new)


def test_20():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</script>\n")
    new.close_script()

    compare_and_empty(old, new)


def test_21():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</div>\n')
    new.close_div()

    compare_and_empty(old, new)


def test_22():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_23():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</a>\n')
    new.close_a()

    compare_and_empty(old, new)


def test_24():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_25():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()
    old.write('</td>')
    new.close_td()

    compare_and_empty(old, new)


def test_26():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>")
    old.write("</table>")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_27():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</span>')
    new.close_span()

    compare_and_empty(old, new)


def test_28():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()

    compare_and_empty(old, new)


def test_29():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>")
    new.close_tr()
    old.write("</td>")
    new.close_td()

    compare_and_empty(old, new)


def test_30():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</select>\n")
    new.close_select()

    compare_and_empty(old, new)


def test_31():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_32():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td>')
    new.close_td()

    compare_and_empty(old, new)


def test_33():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td>')
    new.close_td()

    compare_and_empty(old, new)


def test_34():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_35():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</span>\n')
    new.close_span()

    compare_and_empty(old, new)


def test_36():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_37():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</span>')
    new.close_span()
    old.write('</span>\n')
    new.close_span()

    compare_and_empty(old, new)


def test_38():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_39():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>\n")
    new.close_ul()

    compare_and_empty(old, new)


def test_40():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()
    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_41():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()
    old.write("</tr>")
    new.close_tr()
    old.write("</tr>")
    new.close_tr()
    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_42():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()
    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_43():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</li>')
    old.write('</ul>')
    new.close_li()
    new.close_ul()

    compare_and_empty(old, new)


def test_44():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_45():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</a>')
    new.close_a()
    old.write('</li>\n')
    old.write('</ul>\n')
    new.close_li()
    new.close_ul()

    compare_and_empty(old, new)


def test_46():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</p>')
    new.close_p()

    compare_and_empty(old, new)


def test_47():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</div>\n")
    new.close_div()

    compare_and_empty(old, new)


def test_48():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</a>")
    new.close_a()

    compare_and_empty(old, new)


def test_49():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td>')
    new.close_td()

    compare_and_empty(old, new)


def test_50():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</p>")
    new.close_p()

    compare_and_empty(old, new)


def test_51():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_52():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_53():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()

    compare_and_empty(old, new)


def test_54():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    old.write("</center>")
    new.close_table()
    new.close_center()

    compare_and_empty(old, new)


def test_55():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</a>')
    new.close_a()

    compare_and_empty(old, new)


def test_56():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()

    compare_and_empty(old, new)


def test_57():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>")
    old.write("</table>")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_58():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</b>")
    old.write("</ul>")
    new.close_b()
    new.close_ul()

    compare_and_empty(old, new)


def test_59():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_60():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_61():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_62():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</li>')
    new.close_li()

    compare_and_empty(old, new)


def test_63():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_64():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</tr>\n')
    new.close_tr()

    compare_and_empty(old, new)


def test_65():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</tr>\n')
    new.close_tr()

    compare_and_empty(old, new)


def test_66():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</table>\n')
    new.close_table()

    compare_and_empty(old, new)


def test_67():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_68():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_69():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_70():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_71():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>\n")
    new.close_table()

    compare_and_empty(old, new)


def test_72():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_73():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</ul>')
    new.close_ul()

    compare_and_empty(old, new)


def test_74():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()
    old.write("</tr>\n")
    new.close_tr()
    old.write("</tr>\n")
    old.write("</table>\n")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_75():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_76():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    old.write("</table>\n")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_77():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    old.write("</table>\n")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_78():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>\n")
    new.close_table()

    compare_and_empty(old, new)


def test_79():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</ul>')
    new.close_ul()

    compare_and_empty(old, new)


def test_80():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</ul>')
    new.close_ul()

    compare_and_empty(old, new)


def test_81():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_82():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_83():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</form>')
    new.close_form()

    compare_and_empty(old, new)


def test_84():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_85():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)


def test_86():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_87():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()
    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_88():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()
    old.write("</span>")
    new.close_span()
    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_89():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</span>")
    new.close_span()
    old.write("</span>")
    new.close_span()

    compare_and_empty(old, new)


def test_90():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</tr>')
    new.close_tr()

    compare_and_empty(old, new)


def test_91():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</td>')
    old.write('</tr>')
    old.write('</table>')
    new.close_td()
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_92():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()

    compare_and_empty(old, new)


def test_93():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()
    old.write("</table>\n")
    old.write("</div>\n")
    new.close_table()
    new.close_div()

    compare_and_empty(old, new)


def test_94():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()

    compare_and_empty(old, new)


def test_95():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()
    old.write("</table>\n")
    new.close_table()

    compare_and_empty(old, new)


def test_96():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()

    compare_and_empty(old, new)


def test_97():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>")
    new.close_tr()

    compare_and_empty(old, new)


def test_98():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>\n")
    new.close_table()

    compare_and_empty(old, new)


def test_99():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()

    compare_and_empty(old, new)


def test_100():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()

    compare_and_empty(old, new)


def test_101():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()

    compare_and_empty(old, new)


def test_102():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    old.write("</table>\n")
    new.close_tr()
    new.close_table()

    compare_and_empty(old, new)


def test_103():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>")
    new.close_tr()

    compare_and_empty(old, new)


def test_104():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>")
    new.close_tr()
    old.write('</tr>')
    new.close_tr()
    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_105():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_106():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</tr>\n")
    new.close_tr()

    compare_and_empty(old, new)


def test_107():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</row>')
    old.write('</table>')
    new.close_row()
    new.close_table()

    compare_and_empty(old, new)


def test_108():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</li>\n')
    old.write('</ul>')
    new.close_li()
    new.close_ul()

    compare_and_empty(old, new)


def test_109():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</tr>\n')
    new.close_tr()
    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_110():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</nobr>")
    new.close_nobr()

    compare_and_empty(old, new)


def test_111():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</nobr>")
    new.close_nobr()

    compare_and_empty(old, new)


def test_112():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</nobr>")
    new.close_nobr()

    compare_and_empty(old, new)


def test_113():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</table>")
    new.close_table()

    compare_and_empty(old, new)


def test_114():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</td>")
    new.close_td()
    old.write("</tr>\n")
    new.close_tr()
    old.write("</table>\n")
    new.close_table()

    compare_and_empty(old, new)


def test_115():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write('</table>')
    new.close_table()

    compare_and_empty(old, new)


def test_116():
    old = HTMLOrigTester()
    new = HTMLCheck_MKTester()
    old.plug()
    new.plug()


    old.write("</ul>")
    new.close_ul()

    compare_and_empty(old, new)

