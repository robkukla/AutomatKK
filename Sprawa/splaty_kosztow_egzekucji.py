from uniwersalne_funkcje import *


def splaty_kosztow_egz(self):
    logging.info('')
    logging.info('SPŁATY KOSZTÓW EGZEKUCJI - Treeview - Wybór pola w drzewie')
    logging.info('')
    self.app[kkvat].TreeView.GetItem([u'Stan sprawy', u'Koszty egzekucji', u'Spłaty kosztów egz.']).ClickInput()
    logging.info('SPŁATY KOSZTÓW EGZEKUCJI - Akcja - Dodanie nowej spłaty kosztów egzekucji')
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{INSERT}')
    logging.info('SPŁATY KOSZTÓW EGZEKUCJI - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys('3450')
    logging.info('SPŁATY KOSZTÓW EGZEKUCJI - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** SPŁATY KOSZTÓW EGZEKUCJI - Asercja ***
    logging.info('')
    logging.info('SPŁATY KOSZTÓW EGZEKUCJI - ASERCJA - START')
    assert 'Spłaty kosztów egz.' in self.app[kkvat].Static1.Texts()[0], 'Spłaty kosztów egzekucji - nazwa okna.'

    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == '34,50', 'Niepoprawny Edit 1'

    logging.info('SPŁATY KOSZTÓW EGZEKUCJI - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()
