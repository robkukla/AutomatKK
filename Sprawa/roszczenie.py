from uniwersalne_funkcje import *


def roszczenie(self):
    dane1 = {
        'Kwota': '0,21',
        'Mnożnik': '0,33',
        'Kolejn': '2',
        'Rodzaj': 'N - Odsetki od kwoty',
        'Oprocentowanie': 'S - Skarbowe'}

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')
    self.app.Dialog.print_control_identifiers()

    logging.info('ROSZCZENIE - wprowadzenie nowego roszczenia')
    self.app.Dialog.Wait('ready')
    logging.info('ROSZCZENIE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'])
    logging.info('ROSZCZENIE - Edit - Mnożnik')
    self.app.Dialog.Edit4.type_keys(dane1['Mnożnik'])
    logging.info('ROSZCZENIE - Edit - Kolejn')
    self.app.Dialog.Edit5.type_keys(dane1['Kolejn'])
    logging.info('ROSZCZENIE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox2.Select(dane1['Rodzaj'])
    logging.info('ROSZCZENIE - Combobox - oprocentowanie')
    self.app.Dialog.ComboBox3.Select(dane1['Oprocentowanie'])

    # *** Zaznaczenie checkboxa "nie zamykaj okna" ***
    logging.info('ROSZCZENIE - Checkbox - "Nie zamykaj okna"')
    self.app.Dialog.Chceckbox0.CheckByClick()
    self.app.Dialog.Zapisz.Click()

    dane2 = {'Kwota': '350,00', 'Mnożnik': '0,03', 'Kolejn': '23', 'Rodzaj': 'T - Kwota z odsetkami',
             'Oprocentowanie': 'I - Indywidualne'}
    logging.info('ROSZCZENIE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane2['Kwota'])
    logging.info('ROSZCZENIE - Edit - Mnożnik')
    self.app.Dialog.Edit4.type_keys(dane2['Mnożnik'])
    logging.info('ROSZCZENIE - Edit - Kolejn')
    self.app.Dialog.Edit5.type_keys(dane2['Kolejn'])
    logging.info('ROSZCZENIE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox2.Select(dane2['Rodzaj'])
    logging.info('ROSZCZENIE - Combobox - oprocentowanie')
    self.app.Dialog.ComboBox3.Select(dane2['Oprocentowanie'])

    # *** Odznaznaczenie checkboxa "nie zamykaj okna" ***
    logging.info('ROSZCZENIE - Checkbox - "Nie zamykaj okna"')
    self.app.Dialog.Chceckbox0.UnCheck()

    logging.info('ROSZCZENIE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** ROSZCZENIE - Asercja ***
    logging.info('')
    logging.info('ROSZCZENIE - ASERCJA - START')
    assert 'Roszczenie' in self.app[kkvat].Static1.Texts()[0], 'Roszczenie - nazwa okna.'

    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane1['Kwota'], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane1['Rodzaj'], 'Niepoprawny Combobox 1'
    assert self.app.Dialog[u'Mnożnik:Edit'].Texts()[0] == dane1['Mnożnik'], 'Niepoprawny Edit 2'
    assert self.app.Dialog[u'Kolejn.:Edit'].Texts()[0] == dane1['Kolejn'], 'Niepoprawny Edit 3'
    assert self.app.Dialog[u'Oprocentowanie:Combobox'].Texts()[0] == dane1['Oprocentowanie'], 'Niepoprawny Combobox 2'

    self.app.Dialog.Zapisz.Click()

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane2['Kwota'], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane2['Rodzaj'], 'Niepoprawny Combobox 1'
    assert self.app.Dialog[u'Mnożnik:Edit'].Texts()[0] == dane2['Mnożnik'], 'Niepoprawny Edit 2'
    assert self.app.Dialog[u'Kolejn.:Edit'].Texts()[0] == dane2['Kolejn'], 'Niepoprawny Edit 3'
    assert self.app.Dialog[u'Oprocentowanie:Combobox'].Texts()[0] == dane2['Oprocentowanie'], 'Niepoprawny Combobox 2'

    logging.info('ROSZCZENIE - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()
