from uniwersalne_funkcje import *


def koszty_sadowe(self):
    logging.info('')
    logging.info('KOSZTY SĄDOWE - Treeview - Wybór pola w drzewie')
    logging.info('')
    self.app[kkvat].TreeView.GetItem([u'Stan sprawy', u'Koszty sądowe']).ClickInput()
    logging.info('KOSZTY SĄDOWE - wprowadzenie nowych kosztów sądowych')
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Wait('ready')

    dane1 = {'Kwota': ['33,44', '3,24', '231,44'], 'Rodzaj': ['K - Koszt klauzuli', 'A - Zasądzone koszty adwokackie',
                                                              'E - Koszt poprzedniej egzekucji']}
    logging.info('KOSZTY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'][0])
    logging.info('KOSZTY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox2.Select(dane1['Rodzaj'][0])
    logging.info('KOSZTY SĄDOWE - Checkbox - Nie zamykaj okna')
    self.app.Dialog.Chceckbox0.CheckByClick()
    logging.info('KOSZTY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('KOSZTY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'][1])
    logging.info('KOSZTY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox2.Select(dane1['Rodzaj'][1])
    logging.info('KOSZTY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('KOSZTY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'][2])
    logging.info('KOSZTY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox2.Select(dane1['Rodzaj'][2])
    logging.info('KOSZTY SĄDOWE - Checkbox - Nie zamykaj okna')
    self.app.Dialog.Chceckbox0.UnCheck()
    logging.info('KOSZTY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** KOSZTY SĄDOWE - Asercja ***
    logging.info('')
    logging.info('KOSZTY SĄDOWE - ASERCJA - START')
    assert 'Koszty sądowe' in self.app[kkvat].Static1.Texts()[0], 'Koszty sądowe - nazwa okna.'

    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane1['Kwota'][0], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane1['Rodzaj'][0], 'Niepoprawny Combobox 1'

    self.app.Dialog.Zapisz.Click()

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane1['Kwota'][1], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane1['Rodzaj'][1], 'Niepoprawny Combobox 1'

    self.app.Dialog.Zapisz.Click()

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane1['Kwota'][2], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane1['Rodzaj'][2], 'Niepoprawny Combobox 1'

    logging.info('KOSZTY SĄDOWE - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()
