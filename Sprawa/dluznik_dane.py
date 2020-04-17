from uniwersalne_funkcje import *
import time


def dluznicy_dane(self):

    dane1_edit = {
        'Nazwa1': 'Białek',
        'Nazwa2': 'Michał',
        'Opis': '-brak-',
        'Ulica': 'Malownicza',
        'Nr. ulicy': '43',
        'Miejscowość': 'Warszawa',
        'Kod pocztowy': '00-015',
        'Poczta': 'Śródmieście',
        'Gmina': 'Warszawa',
        'Powiat': 'Warszawa',
        'Województwo': 'Mazowieckie',
        'Kraj': 'Polska',
        'Ulica dod.': 'Kolorowa',
        'Nr. ulicy dod': '75',
        'Miejscowość dod.': 'Lublin',
        'Kod pocztowy dod.': '89-600',
        'Poczta dod.': 'Lublin',
        'Gmina dod.': 'Lublin',
        'Powiat dod.': 'Lublin',
        'Województwo dod.': 'Lubelskie',
        'Kraj dod.': 'Polska'
    }

    dane1_combobox = {
        'Osoba': '<BRAK>',
        'Typ': 'fizyczna',
        'Adres': 'ul.',
        'Adres dod.': 'ul.',
        'Sąd odwoławczy': 2,
        'Status': 0
    }

    dane1_asercja = [u'Nazwa1:Edit', u'Nazwa2:Edit', u'Opis dod.:Edit', u'&Ulica:Edit', u'Num&er:Edit',
                     u'* &Miejscowość:Edit', u'* &Kod:Edit', u'* &Miejscowość:Edit2', u'* &Gmina:Edit',
                     u'* Powiat:Edit', u'* Woj.:Edit', u'Kraj:Edit', u'U&lica:Edit', u'Numer:Edit', u'Miejscowość:Edit',
                     u'Kod:Edit', u'Poczta:Edit', u'Gmina:Edit', u'Powiat:Edit', u'Woj.:Edit', u'Kraj:Edit2']

    dane2_edit = {
        'Guid': 'fc0037b9-b37b-4861-a20b-51754f9a5b11',
        'Imię ojca': 'Rafał',
        'Imię matki': 'Bożena',
        'Miejsce urodzenia': 'Nowy Sącz',
        'Nip1': '79',
        'Nip2': '20240462',
        'Pesel': '96090402194',
        'Nr. świad.': '12345',
        'Regon': '493317166',
        'Numer dokumentu': 'ATS211397',
        'Nazwisko Rodowe': 'Janik',
        'Telefon': '508572384',
        'Telefon Kom': '503968464',
        'Email1': 'Mbiałek@gmail.com',
        'Email2': 'Mbiałek2@gmail.com',
        'Informacje dodatkowe': '-Dane wygenerowane automatycznie-'
    }

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2', u'Numer:Edit',
                     u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Tel. kom.:Edit', u'Email:Edit',
                     u'Email faktury VAT:Edit', u'Informacje dodatk.:Edit']

    dane3_edit = {
        'Opis dodatkowy': 'Firma białkova',
        'Ulica': 'Sianowa',
        'Nr. ulicy': '33',
        'Miejscowość': 'Starogard Gdański',
        'Kod pocztowy': '22-454',
        'Poczta': 'Starogardzka',
        'Gmina': 'Starogard',
        'Powiat': 'Starogardzki',
        'Województwo': 'Pomorskie'
    }

    dane3_asercja = [u'Nazwa:Edit', u'Działalność gospodarczaEdit0', u'Numer:Edit', u'Miejscowość.:Edit', u'Kod:Edit1',
                     u'Poczta:Edit', u'Gmina:Edit', u'Powiat:Edit', u'Woj.:Edit']

    # *** Wybór drzewa "Dłużnicy" ***
    zmiana_drzewa(self, '\\Dłużnicy', 'Dłużnicy')

    # *** Okno wyszukiwania danych ***
    logging.info('DŁUŻNICY - Akcja - Okno wyszukiwania danych')
    logging.info('')
    self.app.Dialog.Zapisz.Click()
    time.sleep(10)
    self.app.Dialog.Zapisz.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'DŁUŻNICY - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'DŁUŻNICY - DANE PODSTAWOWE')

    # *** 2 Zakładka "Dane konta bankowego" ***
    zmiana_zakładki(self, 1, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')

    logging.info('WIERZYCIELE - DANE UZUPEŁNIAJĄCE - Combobox - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')

    zmiana_zakładki(self, 3, 'DŁUŻNICY - DZIAŁANOŚĆ GOSPODARCZA')

    logging.info('DŁUŻNICY - DZIAŁANOŚĆ GOSPODARCZA - Checkbox - Działaność gospodarcza')
    self.app.Dialog.Chceckbox0.CheckByClick()
    dialog_wprowadzanie_danych(self, dane3_edit, dane3_asercja, 'DZIAŁANOŚĆ GOSPODARCZA')

    logging.info('DŁUŻNICY - DZIAŁANOŚĆ GOSPODARCZA - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Wait('ready')
    self.app.Dialog.Nie.Click()

    logging.info('')
    logging.info('DŁUŻNICY - ASERCJA - START')
    assert 'Dłużnicy' in self.app[kkvat].Static1.Texts()[0], 'Dłużnicy - nazwa okna.'

    logging.info('DŁUŻNICY - ASERCJA - Zakładka "Dane podstawowe"')
    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'DŁUŻNICY - DANE PODSTAWOWE')

    zmiana_zakładki(self, 1, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')
    dialog_asercja_danych(self, dane2_edit, dane2_asercja, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')

    zmiana_zakładki(self, 3, 'DŁUŻNICY - DZIAŁANOŚĆ GOSPODARCZA')
    dialog_asercja_danych(self, dane3_edit, dane3_asercja, 'DŁUŻNICY - DZIAŁANOŚĆ GOSPODARCZA')

    logging.info('DŁUŻNICY - KONIEC ASERCJI')
    self.app.Dialog.Zapisz.Click()
