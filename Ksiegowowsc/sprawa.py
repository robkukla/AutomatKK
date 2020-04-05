from uniwersalne_funkcje import *
from time import sleep
from lista_ppm import *
from pywinauto.application import Application


def sprawa(self):
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
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
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
    self.app.Dialog.Edit1.type_keys('10000')
    logging.info('ROSZCZENIE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    zapis(self)

###kolejna
    sleep(2)
    # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

    # dodawanie sprawy
    if self.menu_list == 'dodaj sprawę':
        # *** Wybrannie danego pola z listy rozwijanej ***
        lista_rozwijana(self, self.menu_list)

        # *** Tworzenie sprawy ***
        self.app.Dialog.Wait('ready')
        self.app.Dialog.Edit.type_keys('100/18')
        self.app.Dialog.Zapisz.Click()

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
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

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    self.app.Dialog.Wait('ready')
    self.app.Dialog.Edit1.type_keys('100000')
    self.app.Dialog.Button.Click()
    zapis(self)

    ###kolejna
    sleep(2)
    # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

    # dodawanie sprawy
    if self.menu_list == 'dodaj sprawę':
        # *** Wybrannie danego pola z listy rozwijanej ***
        lista_rozwijana(self, self.menu_list)

        # *** Tworzenie sprawy ***
        self.app.Dialog.Wait('ready')
        self.app.Dialog.Edit.type_keys('101/18')
        self.app.Dialog.Zapisz.Click()

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
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

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    self.app.Dialog.Wait('ready')
    self.app.Dialog.Edit1.type_keys('5000000')
    self.app.Dialog.Zapisz.Click()
    #self.app[kkvat].type_keys('F7')
    zapis(self)

    ###kolejna
    sleep(2)
    # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

    # dodawanie sprawy
    if self.menu_list == 'dodaj sprawę':
        # *** Wybrannie danego pola z listy rozwijanej ***
        lista_rozwijana(self, self.menu_list)

        # *** Tworzenie sprawy ***
        self.app.Dialog.Wait('ready')
        self.app.Dialog.Edit.type_keys('102/18')
        self.app.Dialog.Zapisz.Click()

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
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

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    self.app.Dialog.Wait('ready')
    self.app.Dialog.Edit1.type_keys('768000654')
    self.app.Dialog.Zapisz.Click()
    #self.app[kkvat].type_keys('F7')
    zapis(self)

    ###kolejna
    sleep(2)
    # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

    # dodawanie sprawy
    if self.menu_list == 'dodaj sprawę':
        # *** Wybrannie danego pola z listy rozwijanej ***
        lista_rozwijana(self, self.menu_list)

        # *** Tworzenie sprawy ***
        self.app.Dialog.Wait('ready')
        self.app.Dialog.Edit.type_keys('103/18')
        self.app.Dialog.Zapisz.Click()

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
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

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    self.app.Dialog.Wait('ready')
    self.app.Dialog.Edit1.type_keys('3500000')
    self.app.Dialog.Zapisz.Click()
    #self.app[kkvat].type_keys('F7')
    zapis(self)

    ###kolejna
    sleep(2)
    # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

    # dodawanie sprawy
    if self.menu_list == 'dodaj sprawę':
        # *** Wybrannie danego pola z listy rozwijanej ***
        lista_rozwijana(self, self.menu_list)

        # *** Tworzenie sprawy ***
        self.app.Dialog.Wait('ready')
        self.app.Dialog.Edit.type_keys('104/18')
        self.app.Dialog.Zapisz.Click()

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.Combobox.Select(u'Postanowienie')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    # *** Wierzyciel ***#
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
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

    zmiana_drzewa(self, '\\Stan sprawy\\Roszczenie', 'ROSZCZENIE')

    self.app.Dialog.Wait('ready')
    self.app.Dialog.Edit1.type_keys('325674000')
    self.app.Dialog.Zapisz.Click()
    #self.app[kkvat].type_keys('F7')
    zapis(self)