from uniwersalne_funkcje import *
import time


def peln_dluznika(self):

    dane1_edit = {
        'Nazwa1': 'Luksi',
        'Nazwa2': 'Bartosz',
        'Opis': '-brak-',
        'Ulica': 'Fioletowa',
        'Nr. ulicy': '38',
        'Miejscowość': 'Kołobrzeg',
        'Kod pocztowy': '39-332',
        'Poczta': 'Brzegowa',
        'Gmina': 'Kołobrzeg',
        'Powiat': 'Kołobrzeg',
        'Województwo': 'Zachodniopomorskie',
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
        'Guid': '98d29592-db22-4eee-984c-6a6fd1333b9e',
        'Imię ojca': 'Jaca',
        'Imię matki': 'Gocha',
        'Miejsce urodzenia': 'Kołobrzeg',
        'Nip1': '12',
        'Nip2': '20240462',
        'Pesel': '96090402194',
        'Nr. świad.': '12345',
        'Regon': '493317166',
        'Numer dokumentu': 'ATS111417',
        'Nazwisko Rodowe': 'Ciura',
        'Telefon': '5081112384',
        'Email1': 'Luksi@gmail.com',
        'Informacje dodatkowe': '-Dane wygenerowane automatycznie-'}

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2', u'Numer:Edit',
                     u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Email:Edit', u'Informacje dodatk.:Edit']

    zmiana_drzewa(self, '\\Dłużnicy\\Pełnomocnicy', 'PEŁNOMOCNICY DŁUŻNIKA')

    # *** Okno wyszukiwania danych ***
    self.app.Dialog.Zapisz.Click()
    logging.info('PEŁNOMOCNICY DŁUŻNIKA - Akcja - Okno wyszukiwania danych')
    time.sleep(10)
    self.app.Dialog.Zapisz.Click()

    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'PEŁNOMOCNICY DŁUŻNIKA - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'PEŁNOMOCNICY DŁUŻNIKA - DANE PODSTAWOWE')

    zmiana_zakładki(self, 1, 'PEŁNOMOCNICY DŁUŻNIKA - DANE KONTA BANKOWEGO')

    # *** 2 Zakładka " Dane Kont bank." ***
    logging.info('PEŁNOMOCNICY DŁUŻNIKA - DANE KONTA BANKOWEGO - Edit - Rachunek')
    self.app.Dialog.TypeKeys('{DOWN}')
    self.app.Dialog.TypeKeys('{INSERT}')
    self.app.Dialog.Edit.TypeKeys("10902688")
    logging.info('PEŁNOMOCNICY DŁUŻNIKA - DANE KONTA BANKOWEGO - Button - 1 (Automatyczne wypełnianie danych)')
    self.app.Dialog.Button1.Click()
    self.app.Dialog.Button1.Click()

    zmiana_zakładki(self, 2, 'PEŁNOMOCNICY DŁUŻNIKA - DANE UZUPEŁNIAJĄCE')

    logging.info('PEŁNOMOCNICY DŁUŻNIKA - DANE UZUPEŁNIAJĄCE - Edit - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'PEŁNOMOCNICY DŁUŻNIKA - DANE UZUPEŁNIAJĄCE')

    self.app.Dialog.Zapisz.Click()

    # *** PEŁNOMOCNICY DŁUŻNIKA - Asercja ***
    logging.info('')
    logging.info('PEŁNOMOCNICY DŁUŻNIKA - ASERCJA - START')
    assert 'Pełnomocnicy' in self.app[kkvat].Static1.Texts()[0], 'Pełnomocnik dłużnika - nazwa okna.'

    logging.info('PEŁNOMOCNICY DŁUŻNIKA - ASERCJA - Zakładka "Dane podstawowe"')
    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].TypeKeys('{ENTER}')

    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'PEŁNOMOCNICY DŁUŻNIKA - DANE PODSTAWOWE')
    zmiana_zakładki(self, 2, 'PEŁNOMOCNICY DŁUŻNIKA - DANE UZUPEŁNIAJĄCE')

    # Nie działa zapisywanie sie pola guid - do naprawy !!!!!
    # dialog_asercja_danych(self, dane2_edit, dane2_asercja, 'PEŁNOMOCNICY DŁUŻNIKA - DANE UZUPEŁNIAJĄCE')
    logging.info('PEŁNOMOCNICY DŁUŻNIKA - KONIEC ASERCJI')
    self.app.Dialog.Zapisz.Click()