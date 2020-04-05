from uniwersalne_funkcje import *
from time import sleep
import logging
import time
from pywinauto.application import Application
kkvat = 'Kancelaria Komornika - VAT'


def dane_do_sprawy(self):
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
        'Numer dokumentu': 'ATS211397',
        'Nazwisko Rodowe': 'Nowak',
        'Telefon': '508572384',
        'Tek. kom': '503968464',
        'Email1': 'jkowalski@gmail.com',
        'Email2': 'jkowalski2@gmail.com',
        'Informacje dodatkowe': '-Dane wygenerowane automatycznie-'
    }

    dane1_asercja = [u'Nazwa1:Edit', u'Nazwa2:Edit', u'Opis dod.:Edit', u'&Ulica:Edit', u'Num&er:Edit',
                     u'* &Miejscowość:Edit', u'* &Kod:Edit', u'* &Miejscowość:Edit2', u'* &Gmina:Edit',
                     u'* Powiat:Edit', u'* Woj.:Edit', u'Kraj:Edit', u'U&lica:Edit', u'Numer:Edit', u'Miejscowość:Edit',
                     u'Kod:Edit', u'Poczta:Edit', u'Gmina:Edit', u'Powiat:Edit', u'Woj.:Edit', u'Kraj:Edit2']

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'&NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2',
                     u'Numer:Edit', u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Tel. kom.:Edit', u'Email:Edit',
                     u'Email faktury VAT:Edit', u'Informacje dodatk.:Edit']

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
        'Regon': '493317166',
        'Numer dokumentu': 'ATS211397',
        'Nazwisko Rodowe': 'Janik',
        'Telefon': '508572384',
        'Telefon Kom': '503968464',
        'Email1': 'Mbiałek@gmail.com',
        'Email2': 'Mbiałek2@gmail.com',
        'Informacje dodatkowe': '-Dane wygenerowane automatycznie-'
    }

    dane4_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2', u'Numer:Edit',
                     u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Tel. kom.:Edit', u'Email:Edit',
                     u'Email faktury VAT:Edit', u'Informacje dodatk.:Edit']


    # *** Tytuł wykonawczy ***#
    logging.info('')
    logging.info('TYTUŁY WYKONAWCZE - Treeview - Wybór pola w drzewie')
    logging.info('')

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    logging.info('TYTUŁY WYKONAWCZE - Akcja - Dodanie nowego tytułu wykonawczego')
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    assert 'Tytuły wykonawcze' in self.app[kkvat].Static1.Texts()[0], 'Tytuły wykonawcze - nazwa okna.'

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
    self.app.Dialog.Zapisz.Click()
    sleep(5)
    self.app.Dialog.Zapisz.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'WIERZYCIELE - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'WIERZYCIELE - DANE PODSTAWOWE')

    # *** 2 Zakładka "Dane konta bankowego" ***
    zmiana_zakładki(self, 1, 'WIERZYCIELE - DANE KONTA BANKOWEGO')

    logging.info('WIERZYCIELE - DANE KONTA BANKOWEGO - Akcja - Dodanie nowego nr. konta bankowego')
    self.app.Dialog.type_keys('{DOWN}')
    self.app.Dialog.type_keys('{INSERT}')
    logging.info('WIERZYCIELE - DANE KONTA BANKOWEGO - Edit - Rachunek')
    self.app.Dialog.Edit.type_keys("10902688")  # Nazwa1
    logging.info('WIERZYCIELE - DANE KONTA BANKOWEGO - Button - 1 (Automatyczne wypełnianie danych)')
    self.app.Dialog.Button1.Click()
    self.app.Dialog.Button1.Click()

    # *** 3 Zakładka "Dane uzupełniające" ***
    zmiana_zakładki(self, 2, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')

    logging.info('WIERZYCIELE - DANE UZUPEŁNIAJĄCE - Combobox - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit,dane2_asercja, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')
    self.app.Dialog.print_control_identifiers()

    # *** Zapis utworzonego Wierzyciela ***
    self.app.Dialog.Wait('ready')
    logging.info('WIERZYCIELE - DANE DODATKOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    # *** Asercja wprowadzonych danych ***
    logging.info('')
    logging.info('WIERZYCIELE - ASERCJA - START')
    assert 'Wierzyciele' in self.app[kkvat].Static1.Texts()[0], 'Wierzyciele - nazwa okna.'

    # *** Dłużnik ***#
    zmiana_drzewa(self, '\\Dłużnik', 'Dłużnik')

    # *** Okno wyszukiwania danych ***
    logging.info('DŁUŻNICY - Akcja - Okno wyszukiwania danych')
    logging.info('')
    self.app.Dialog.Zapisz.Click()
    time.sleep(5)
    self.app.Dialog.Zapisz.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane3_edit, dane3_asercja, 'DŁUŻNICY - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane3_combobox, 'DŁUŻNICY - DANE PODSTAWOWE')

    # *** 2 Zakładka "Dane konta bankowego" ***
    zmiana_zakładki(self, 1, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')

    logging.info('Dłużnik - DANE UZUPEŁNIAJĄCE - Combobox - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane4_edit, dane4_asercja, 'DŁUŻNICY - DANE UZUPEŁNIAJĄCE')

    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Wait('ready')
    self.app.Dialog.Nie.Click()

    logging.info('')
    logging.info('DŁUŻNICY - ASERCJA - START')
    assert 'Dłużnicy' in self.app[kkvat].Static1.Texts()[0], 'Dłużnicy - nazwa okna.'

    # *** Rachunki bankowe ***#

    zmiana_drzewa(self, '\\Dłużnicy\\Rachunki bankowe', 'RACHUNKI BANKOWE')
    self.app.Dialog.Wait('ready')
    logging.info('RACHUNKI BANKOWE - Edit - Rachunek')
    self.app.Dialog.Edit1.type_keys('70200001')
    self.app.Dialog.Button1.Click()
    logging.info('RACHUNKI BANKOWE - Button - 1 (Automatyczne wypełnianie danych)')
    logging.info('RACHUNKI BANKOWE - Button - OK')
    self.app.Dialog.OK.Click()


    # *** Roszczenie ***#

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    logging.info('ROSZCZENIE - wprowadzenie nowego roszczenia')
    self.app.Dialog.Wait('ready')
    logging.info('ROSZCZENIE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys('10000')
    logging.info('ROSZCZENIE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** ROSZCZENIE - Asercja ***
    logging.info('')
    logging.info('ROSZCZENIE - ASERCJA - START')
    assert 'Roszczenie' in self.app[kkvat].Static1.Texts()[0], 'Roszczenie - nazwa okna.'
