from uniwersalne_funkcje import *


def koszty_egzekucji(self):
    logging.info('')
    logging.info('KOSZTY EGZEKUCJI - Treeview - Wybór pola w drzewie')
    logging.info('')
    self.app[kkvat].TreeView.GetItem([u'Stan sprawy', u'Koszty egzekucji']).ClickInput()
    logging.info('KOSZTY EGZEKUCJI - Akcja - Dodanie nowych kosztów egzekucji')
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{INSERT}')
    logging.info('KOSZTY EGZEKUCJI - OPŁATY STAŁE - ART.53 - SPIS INWENTARZA - Treeview - Wybór pola w drzewie')
    self.app.Dialog.TreeView.GetItem([u'Opłaty Stałe', u'Art.53 - Spis inwentarza.']).Click()
    logging.info('KOSZTY EGZEKUCJI - OPŁATY STAŁE - ART.53 - SPIS INWENTARZA - Treeview - Edit - Ilość godzin')
    self.app.Dialog.Edit1.type_keys('2')
    logging.info('KOSZTY EGZEKUCJI - OPŁATY STAŁE - ART.53 - SPIS INWENTARZA - Button - Dalej')
    self.app.Dialog.Dalej.Click()
    logging.info('KOSZTY EGZEKUCJI - OPŁATY STAŁE - ART.53 - SPIS INWENTARZA - DANE - Edit - Naliczone')
    self.app.Dialog.Edit1.type_keys('3450')
    logging.info('KOSZTY EGZEKUCJI - OPŁATY STAŁE - ART.53 - SPIS INWENTARZA - DANE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    #self.app.Dialog.Zapisz.Click()

    # *** KOSZTY EGZEKUCJI - Asercja ***
    logging.info('')
    logging.info('KOSZTY EGZEKUCJI - ASERCJA - START')
    assert 'Koszty egzekucji' in self.app[kkvat].Static1.Texts()[0], 'Koszty egzekucji - nazwa okna.'

    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Naliczone::Edit'].Texts()[0] == '34,50', 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Przepis prawny::Edit'].Texts()[0] == 'Art.53', 'Niepoprawny Edit 1'

    logging.info('KOSZTY EGZEKUCJI - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()
