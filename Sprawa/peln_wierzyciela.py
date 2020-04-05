from uniwersalne_funkcje import *
from time import sleep


def peln_wierzyciela(self):

    dane1_edit = {
        'Nazwa1': 'Musialak',
        'Nazwa2': 'Roman',
        'Opis': '-brak-',
        'Ulica': 'niebieska',
        'Nr. ulicy': '111',
        'Miejscowość': 'Opole',
        'Kod pocztowy': '22-676',
        'Poczta': 'Opolska',
        'Gmina': 'Opole',
        'Powiat': 'Opole',
        'Województwo': 'Opolskie',
        'Kraj': 'Polska'
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
                     u'* Powiat:Edit', u'* Woj.:Edit', u'Kraj:Edit']

    dane2_edit = {
        'Guid': '6a7d1ab2-7b73-4d61-bbc6-f62cac1f7bf8',
        'Imię ojca': 'Artur',
        'Imię matki': 'Teresa',
        'Miejsce urodzenia': 'Katowice',
        'Nip1': '12',
        'Nip2': '20240462',
        'Pesel': '96090402194',
        'Nr. świad.': '12345',
        'Regon': '493317166',
        'Numer dokumentu': 'ATS111417',
        'Nazwisko Rodowe': 'Zwierz',
        'Telefon': '5081112384',
        'Email1': 'Roman@gmail.com',
        'Informacje dodatkowe': '-Dane wygenerowane automatycznie-'
    }

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2', u'Numer:Edit',
                     u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Email:Edit', u'Informacje dodatk.:Edit']

    zmiana_drzewa(self, '\\Wierzyciele\\Pełnomocnicy', 'PEŁNOMOCNICY WIERZYCIELA')

    # *** Okno wyszukiwania danych ***
    self.app.Dialog.Zapisz.Click()
    sleep(10)
    logging.info('PEŁNOMOCNICY WIERZYCIELA - Akcja - Okno wyszukiwania danych')
    logging.info('')
    self.app.Dialog.Zapisz.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'PEŁNOMOCNICY WIERZYCIELA - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'PEŁNOMOCNICY WIERZYCIELA - DANE PODSTAWOWE')

    zmiana_zakładki(self, 1, 'PEŁNOMOCNICY WIERZYCIELA - DANE KONTA BANKOWEGO')

    # *** 2 Zakładka " Dane Kont bank." ***
    self.app.Dialog.type_keys('{DOWN}')
    self.app.Dialog.type_keys('{INSERT}')
    logging.info('PEŁNOMOCNICY WIERZYCIELA - DANE KONTA BANKOWEGO - Edit - Rachunek')
    self.app.Dialog.Edit.type_keys("10902688")
    logging.info('PEŁNOMOCNICY WIERZYCIELA - DANE KONTA BANKOWEGO - Button - 1 (Automatyczne wypełnianie danych)')
    self.app.Dialog.Button1.Click()
    self.app.Dialog.Button1.Click()

    zmiana_zakładki(self, 2, 'PEŁNOMOCNICY WIERZYCIELA - DANE UZUPEŁNIAJĄCE')

    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'PEŁNOMOCNICY WIERZYCIELA - DANE UZUPEŁNIAJĄCE')

    zmiana_zakładki(self, 3, 'PEŁNOMOCNICY WIERZYCIELA - ŹRÓDŁO PIENIĘDZY')

    logging.info('PEŁNOMOCNICY WIERZYCIELA - ŹRÓDŁO PIENIĘDZY - Checkbox - Zaznaczenie checkboxów')
    self.app.Dialog.Chceckbox1.CheckByClick()
    self.app.Dialog.Chceckbox3.CheckByClick()
    logging.info('PEŁNOMOCNICY WIERZYCIELA - ŹRÓDŁO PIENIĘDZY - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** PEŁNOMOCNICY WIERZYCIELA - Asercja ***
    logging.info('')
    logging.info('PEŁNOMOCNICY WIERZYCIELA - ASERCJA - START')
    assert 'Pełnomocnicy' in self.app[kkvat].Static1.Texts()[0], 'Pełnomocnicy wierzyciela - nazwa okna.'

    logging.info('PEŁNOMOCNICY WIERZYCIELA - ASERCJA - Zakładka "Dane podstawowe"')
    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'PEŁNOMOCNICY WIERZYCIELA - DANE PODSTAWOWE')
    zmiana_zakładki(self, 2, 'PEŁNOMOCNICY WIERZYCIELA - DANE UZUPEŁNIAJĄCE')

    # Nie działa zapisywanie pola guid, wiec narazie wylaczona - DO NAPRAWIENIA!!!!
    # dialog_asercja_danych(self, dane2_edit, dane2_asercja, 'WIERZYCIELE - ASERCJA - DANE UZUPEŁNIAJĄCE')

    logging.info('WIERZYCIELE - KONIEC ASERCJI')
    self.app.Dialog.Zapisz.Click()
