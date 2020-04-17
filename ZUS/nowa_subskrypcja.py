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
    debtor_dialog.child_window(title='ZUS alimenty').draw_outline()
    debtor_dialog.child_window(title='ZUS alimenty').click()

    debtor_dialog.child_window(title="Utwórz subskrypcję", class_name="Button").click()
    #https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
    debtor_dialog.type_keys('{ENTER}')
    debtor_dialog.type_keys('{ESC}')
    my_app.type_keys('{F7}')
    my_app.type_keys('{ESC}')



