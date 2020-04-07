from uniwersalne_funkcje import *

TEST_NAME_PREFIX = "PUE ZUS"
TEST_NAME = "Wysyłka zapytań"


def wysylka_zapytan(self):
    logging.info("%s - Test: %s", TEST_NAME_PREFIX, TEST_NAME)
    my_app = self.app.window(title_re=u'Kancelaria Komornika - VAT')
    my_app.child_window(title="Wyślij wnioski", auto_id="simpleButton1", control_type="DevExpress.XtraEditors.SimpleButton").click()