from uniwersalne_funkcje import *
from time import sleep
from lista_ppm import *
from pywinauto.application import Application

kkvat = 'Afx:00400000:8:00010003:00000000:039016A5'


def generowanie_kopert_w_sprawie(self):
    dane1_edit = {
        'Nazwa1': 'Kowalski',
        'Nazwa2': 'Jan',
        'Opis': '-brak-',
        'Ulica': 'Zielona',
        'Nr. ulicy': '22',
        'Miejscowość': 'Kraków',
        'Kod pocztowy': '30-092'
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
        'Pesel': '96090402194'
    }

    dane1_asercja = [u'Nazwa1:Edit', u'Nazwa2:Edit', u'Opis dod.:Edit', u'&Ulica:Edit', u'Num&er:Edit',
                     u'* &Miejscowość:Edit', u'* &Kod:Edit', u'* &Miejscowość:Edit2', u'U&lica:Edit', u'Numer:Edit',
                     u'Miejscowość:Edit', u'Kod:Edit']

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'&NIP:Edit2', u'Pesel:Edit']

    dane3_edit = {
        'Nazwa1': 'Białek',
        'Nazwa2': 'Michał',
        'Opis': '-brak-',
        'Ulica': 'Malownicza',
        'Nr. ulicy': '43',
        'Miejscowość': 'Warszawa',
        'Kod pocztowy': '00-015',
        'Poczta': 'Śródmieście'
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
                     u'* &Miejscowość:Edit', u'* &Kod:Edit', u'* &Miejscowość:Edit2', u'U&lica:Edit', u'Numer:Edit',
                     u'Miejscowość:Edit', u'Kod:Edit']

    dane4_edit = {
        'Guid': 'fc0037b9-b37b-4861-a20b-51754f9a5b11',
        'Imię ojca': 'Rafał',
        'Imię matki': 'Bożena',
        'Miejsce urodzenia': 'Nowy Sącz',
        'Nip1': '',
        'Nip2': '2850987181',
        'Pesel': '96090402194'
    }

    dane4_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit']

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    logging.info('TYTUŁY WYKONAWCZE - Akcja - Dodanie nowego tytułu wykonawczego')
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    #self.app.Dialog.Edit2.type_keys('Kp1')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    self.app.Dialog.Anuluj.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'WIERZYCIELE - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'WIERZYCIELE - DANE PODSTAWOWE')

    # *** 2 Zakładka "Dane konta bankowego" ***
    zmiana_zakładki(self, 1, 'WIERZYCIELE - DANE KONTA BANKOWEGO')

    self.app.Dialog.type_keys('{DOWN}')
    self.app.Dialog.type_keys('{INSERT}')
    self.app.Dialog.Edit.type_keys("10902688")  # Nazwa1
    self.app.Dialog.Button1.Click()
    self.app.Dialog.Button1.Click()

    # *** 3 Zakładka "Dane uzupełniające" ***
    zmiana_zakładki(self, 2, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')

    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')
    self.app.Dialog.print_control_identifiers()

    # *** Zapis utworzonego Wierzyciela ***
    self.app.Dialog.Wait('ready')
    self.app.Dialog.Zapisz.Click()

    # *** Dłużnik ***#
    zmiana_drzewa(self, '\\Dłużnik', 'Dłużnik')

    # *** Okno wyszukiwania danych ***
    logging.info('DŁUŻNICY - Akcja - Okno wyszukiwania danych')
    logging.info('')
    self.app.Dialog.Anuluj.Click()

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
    self.app.Dialog.Button2.Click()

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    logging.info('ROSZCZENIE - wprowadzenie nowego roszczenia')
    self.app.Dialog.Wait('ready')
    logging.info('ROSZCZENIE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys('100000')
    logging.info('ROSZCZENIE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    ###Wierzyciel
    self.app[kkvat].TreeView.GetItem([u'Czynności']).ClickInput()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{TAB}')
    self.app[kkvat].type_keys('{ENTER}')
    self.app.Dialog.OK.Click()

    self.app.Dialog.Button4.Click()
    self.app.Dialog.TreeView.DoubleClick()
    self.app.Dialog.type_keys('{DOWN 3}')
    self.app.Dialog.Button4.Click()
    self.app.Dialog.Button4.Click()

    self.app.Dialog.CheckBox2.Click()



