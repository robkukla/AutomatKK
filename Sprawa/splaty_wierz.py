from uniwersalne_funkcje import *


def splaty_wierz(self):
    logging.info('')
    logging.info('SPŁATY WIERZYCIELOLWI - Treeview - Wybór pola w drzewie')
    logging.info('')
    self.menu_list = 'dodaj sprawę'

    self.app[kkvat].TreeView.GetItem([u'Stan sprawy', u'Spłaty wierz., Sąd']).ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{INSERT}')

    dane1 = {'Kwota': ['12,83', '1,15', '111,29'], 'Rodzaj': ['Z - Zaległości', 'O - Odsetki',
                                                              'T - Stornowanie']}
    logging.info('SPŁATY WIERZYCIELOLWI - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'][0])
    logging.info('SPŁATY WIERZYCIELOLWI - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane1['Rodzaj'][0])
    logging.info('SPŁATY WIERZYCIELOLWI - Checkbox - Nie zamykaj okna')
    self.app.Dialog.Chceckbox2.CheckByClick()
    logging.info('SPŁATY WIERZYCIELOLWI - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('SPŁATY WIERZYCIELOLWI - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'][1])
    logging.info('SPŁATY WIERZYCIELOLWI - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane1['Rodzaj'][1])
    logging.info('SPŁATY WIERZYCIELOLWI - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('SPŁATY WIERZYCIELOLWI - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane1['Kwota'][2])
    logging.info('SPŁATY WIERZYCIELOLWI - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane1['Rodzaj'][2])
    logging.info('SPŁATY WIERZYCIELOLWI - Checkbox - Nie zamykaj okna')
    self.app.Dialog.Chceckbox2.UnCheck()
    logging.info('SPŁATY WIERZYCIELOLWI - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** SPŁATY WIERZYCIELOLWI - Asercja ***
    logging.info('')
    logging.info('SPŁATY WIERZYCIELOLWI - ASERCJA - START')
    assert 'Spłaty wierzycielowi/sądowi' in self.app[kkvat].Static1.Texts()[0], 'Spłaty wierz., sąd - nazwa okna.'

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

    logging.info('SPŁATY WIERZYCIELOLWI - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()

    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{INSERT}')

    dane2 = {'Kwota': ['2,83', '11,52', '121,90', '31,65'], 'Rodzaj': ['Z - Zwrot zaliczki', 'M - Kwota mylnie wysłana',
                                                                       'T - Stornowanie', 'Y - Kwota wystornowana']}
    logging.info('SPŁATY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane2['Kwota'][0])
    logging.info('SPŁATY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane2['Rodzaj'][0])
    logging.info('SPŁATY SĄDOWE - Checkbox - Nie zamykaj okna')
    self.app.Dialog.Chceckbox2.CheckByClick()
    logging.info('SPŁATY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('SPŁATY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane2['Kwota'][1])
    logging.info('SPŁATY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane2['Rodzaj'][1])
    logging.info('SPŁATY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('SPŁATY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane2['Kwota'][2])
    logging.info('SPŁATY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane2['Rodzaj'][2])
    logging.info('SPŁATY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    logging.info('SPŁATY SĄDOWE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys(dane2['Kwota'][3])
    logging.info('SPŁATY SĄDOWE - Combobox - Rodzaj')
    self.app.Dialog.ComboBox1.Select(dane2['Rodzaj'][3])
    logging.info('SPŁATY SĄDOWE - Checkbox - Nie zamykaj okna')
    self.app.Dialog.Chceckbox2.UnCheck()
    logging.info('SPŁATY SĄDOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** KOSZTY SĄDOWE - Asercja ***
    logging.info('')
    logging.info('SPŁATY SĄDOWE - ASERCJA - START')
    assert 'Spłaty wierzycielowi/sądowi' in self.app[kkvat].Static1.Texts()[0], 'Spłaty wierz., sąd - nazwa okna.'

    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane2['Kwota'][0], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane2['Rodzaj'][0], 'Niepoprawny Combobox 1'

    self.app.Dialog.Zapisz.Click()
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane2['Kwota'][1], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane2['Rodzaj'][1], 'Niepoprawny Combobox 1'

    self.app.Dialog.Zapisz.Click()
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane2['Kwota'][2], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane2['Rodzaj'][2], 'Niepoprawny Combobox 1'

    self.app.Dialog.Zapisz.Click()
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')

    assert self.app.Dialog[u'Kwota::Edit'].Texts()[0] == dane2['Kwota'][3], 'Niepoprawny Edit 1'
    assert self.app.Dialog[u'Rodzaj:Combobox'].Texts()[0] == dane2['Rodzaj'][3], 'Niepoprawny Combobox 1'

    logging.info('SPŁATY SĄDOWE - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()
