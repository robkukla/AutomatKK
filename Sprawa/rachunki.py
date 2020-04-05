from uniwersalne_funkcje import *


def rachunki_bankowe(self):
    zmiana_drzewa(self, '\\Dłużnicy\\Rachunki bankowe', 'RACHUNKI BANKOWE')
    self.app.Dialog.Wait('ready')
    logging.info('RACHUNKI BANKOWE - Edit - Rachunek')
    self.app.Dialog.Edit1.type_keys('19400008')
    self.app.Dialog.Button1.Click()
    logging.info('RACHUNKI BANKOWE - Button - 1 (Automatyczne wypełnianie danych)')
    self.app.Dialog.Button.Click()
    logging.info('RACHUNKI BANKOWE - Button - OK')
    self.app.Dialog.OK.Click()

    logging.info('PEŁNOMOCNICY DŁUŻNIKA - ASERCJA - START')
    assert 'Rachunki bankowe' in self.app[kkvat].Static1.Texts()[0], 'Rachunki bankowe - nazwa okna.'

    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    assert '19400008' in self.app.Dialog[u'Rachunek:Edit'].Texts()[0]
    self.app.Dialog.OK.Click()
    logging.info('PEŁNOMOCNICY DŁUŻNIKA - ASERCJA - KONIEC')
