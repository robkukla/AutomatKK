from uniwersalne_funkcje import *
from time import sleep
from menu import *
from pywinauto.application import Application


def zapytania_sprawaKM(self):
    dane1_edit = {
        'Nazwa1': 'Kowalski',
        'Nazwa2': 'Jan',
        'Opis': '-brak-',
        'Ulica': 'Zielona',
        'Nr. ulicy': '22',
        'Miejscowość': 'Kraków',
        'Kod pocztowy': '30-092',
        'Poczta': 'Dębniki',
        'Gmina': 'Kraków',
        'Powiat': 'Kraków',
        'Województwo': 'Małopolskie',
        'Kraj': 'Polska'
    }

    dane1_combobox = {
        'Osoba': '<BRAK>',
        'Typ': 'fizyczna',
        'Adres': 'ul.',
        'Sąd odwoławczy': 2,
        'Status': 0
    }

    dane2_edit = {
        'Guid': 'c9a61d68-2647-4a6f-b1ea-4cc5231ad903',
        'Imię ojca': 'Janusz',
        'Imię matki': 'Ewa',
        'Miejsce urodzenia': 'Nowy Targ',
        'Nip1': '79',
        'Nip2': '20240462',
        'Pesel': '96090402194',
        'Nr. świad.': '12345',
        'Regon': '493317166',
    }

    dane1_asercja = [u'Nazwa1:Edit', u'Nazwa2:Edit', u'Opis dod.:Edit', u'&Ulica:Edit', u'Num&er:Edit',
                     u'* &Miejscowość:Edit', u'* &Kod:Edit', u'* &Miejscowość:Edit2', u'* &Gmina:Edit',
                     u'* Powiat:Edit', u'* Woj.:Edit', u'Kraj:Edit', u'U&lica:Edit', u'Numer:Edit', u'Miejscowość:Edit',
                     u'Kod:Edit', u'Poczta:Edit', u'Gmina:Edit', u'Powiat:Edit', u'Woj.:Edit', u'Kraj:Edit2']

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'&NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2']

    dane3_edit = {
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
        'Kraj': 'Polska'
    }

    dane3_combobox = {
        'Osoba': '<BRAK>',
        'Typ': 'fizyczna',
        'Adres': 'ul.',
        'Adres dod.': 'ul.',
        'Sąd odwoławczy': 3,
        'Status': 0
    }

    dane3_asercja = [u'Nazwa1:Edit', u'Nazwa2:Edit', u'Opis dod.:Edit', u'&Ulica:Edit', u'Num&er:Edit',
                     u'* &Miejscowość:Edit', u'* &Kod:Edit', u'* &Miejscowość:Edit2', u'* &Gmina:Edit',
                     u'* Powiat:Edit', u'* Woj.:Edit', u'Kraj:Edit', u'U&lica:Edit', u'Numer:Edit', u'Miejscowość:Edit',
                     u'Kod:Edit', u'Poczta:Edit', u'Gmina:Edit', u'Powiat:Edit', u'Woj.:Edit', u'Kraj:Edit2']

    dane4_edit = {
        'Guid': 'fc0037b9-b37b-4861-a20b-51754f9a5b11',
        'Imię ojca': 'Rafał',
        'Imię matki': 'Bożena',
        'Miejsce urodzenia': 'Nowy Sącz',
        'Nip1': '',
        'Nip2': '2850987181',
        'Pesel': '96090402194',
        'Nr. świad.': '12345',
        'Regon': '493317166'
    }

    dane4_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2']

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Edit2.type_keys('Km2')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    assert 'Tytuły wykonawcze' in self.app[kkvat].Static1.Texts()[0], 'Tytuły wykonawcze - nazwa okna.'

    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')
    self.app.Dialog.Anuluj.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'WIERZYCIELE - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'WIERZYCIELE - DANE PODSTAWOWE')

    # *** 3 Zakładka "Dane uzupełniające" ***
    zmiana_zakładki(self, 1, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')

    logging.info('WIERZYCIELE - DANE UZUPEŁNIAJĄCE - Combobox - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')
    self.app.Dialog.print_control_identifiers()

    # *** Zapis utworzonego Wierzyciela ***
    self.app.Dialog.Wait('ready')
    logging.info('WIERZYCIELE - DANE DODATKOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    # *** Asercja wprowadzonych danych ***
    logging.info('')
    logging.info('WIERZYCIELE - ASERCJA - START')
    assert 'Wierzyciele' in self.app[kkvat].Static1.Texts()[0], 'Wierzyciele - nazwa okna.'

    # Wierzyciel rachunki
    zmiana_drzewa(self, '\\Wierzyciele\\Rachunki bankowe', 'RACHUNKI BANKOWE')
    self.app.Dialog.Wait('ready')
    logging.info('RACHUNKI BANKOWE - Edit - Rachunek')
    self.app.Dialog.Edit1.type_keys('70200001')
    self.app.Dialog.Button1.Click()
    logging.info('RACHUNKI BANKOWE - Button - 1 (Automatyczne wypełnianie danych)')
    logging.info('RACHUNKI BANKOWE - Button - OK')
    self.app.Dialog.Button.Click()
    self.app.Dialog.OK.Click()

    zmiana_drzewa(self, '\\Dłużnik', 'Dłużnik')
    self.app.Dialog.Anuluj.Click()

    dialog_wprowadzanie_danych(self, dane3_edit, dane3_asercja, 'DŁUŻNICY - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane3_combobox, 'DŁUŻNICY - DANE PODSTAWOWE')

    zmiana_zakładki(self, 1, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')

    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane4_edit, dane4_asercja, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Wait('ready')
    self.app.Dialog.Button2.Click()

    self.app[kkvat].type_keys('^s^c')
    self.app[kkvat].ListView2.DoubleClick()
    self.app.Dialog.Button10.Click()

    # *** Dodawanie pojedynczych bankow ***#

    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 2}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 3}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 4}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 5}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 6}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 7}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 8}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 9}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 10}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Zapisz.Click()

    zapis(self)

    menu_glowne(self, menu_button='Biurowość', submenu_1='Ognivo2', submenu_2='e-Zapytania (wysłane/odebrane)')
    self.app[kkvat].type_keys('{DOWN 9}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].Button3.Click()
    self.app[kkvat].ListView2.Click()
    self.app[kkvat].type_keys('^a^c')
    self.app[kkvat].Button2.Click()

    sleep(5)

    forma = Application().connect(title_re=".*certyfikatu.*")
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Wait('visible')
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').SetFocus()
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Button5.Click()
    #forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').type_keys('{ENTER}')
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Button4.Click()
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Edit2.ClickInput()
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Edit2.type_keys('1111')
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').OK.Click()
    forma.Window_(title='Wybór certyfikatu NIEKWALIFIKOWANEGO (logowanie)').type_keys('{ENTER}')