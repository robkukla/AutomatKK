from uniwersalne_funkcje import *

TEST_NAME_PREFIX = "PUE ZUS"
TEST_NAME = "Wysyłka zapytań"


def wysylka_zapytan(self):
    logging.info("%s - Test: %s", TEST_NAME_PREFIX, TEST_NAME)
    my_app = self.app.window(title_re=u'Kancelaria Komornika')
    my_app.child_window(title="Wyślij wnioski", auto_id="simpleButton1", control_type="DevExpress.XtraEditors.SimpleButton").click()

    my_wyb_cert = self.app.window(title_re=u"Wybór certyfikatu")
    my_wyb_cert.draw_outline()
    my_wyb_cert.child_window(title="Wszystkie").click()
