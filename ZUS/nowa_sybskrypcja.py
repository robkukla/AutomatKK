from uniwersalne_funkcje import *
from time import sleep
from pywinauto.application import Application

TEST_NAME_PREFIX = "PUE ZUS"
TEST_NAME = "Nowa subskrypcja"


def nowa_sub(self):
    logging.info("%s - Test: %s", TEST_NAME_PREFIX, TEST_NAME)
    my_app = self.app.window(title_re=u'Kancelaria Komornika - VAT')
    my_app.TreeView.get_item("\\Dłużnicy").click_input()
    my_app.type_keys('{ENTER}')
    my_app.ListView2.draw_outline()
    my_app.ListView2.set_focus()
    my_app.ListView2.double_click()
    debtor_dialog = self.app.Dialog
    debtor_dialog.draw_outline()
