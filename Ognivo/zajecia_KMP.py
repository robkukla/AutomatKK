from uniwersalne_funkcje import *
from time import sleep
from pywinauto.application import Application


def zajeciaKMP(self):
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

    dane5_edit = {
        'Nazwa1': 'Anna',
        'Nazwa2': 'Nowak',
        'Ulica': 'Nowa',
        'Numer': '1',
        'Miejscowość': 'Kraków',
        'Kod': '11-222',
        'Poczta': 'Krakowska',
        'Nip1': '',
        'Nip2': '2850087181',
        'Pesel': '90060402194'
    }

    dane5_combobox = {
        'Adres': 'ul.'
    }

    dane5_asercja = [u'Nazwa1:Edit', u'Nazwa2:Edit', u'&Ulica:Edit', u'Num&er:Edit', u'* &Miejscowość:Edit',
                     u'* &Kod:Edit', u'Poczta:Edit', u'NIP:Edit1', u'NIP:Edit2', u'Pesel:Edit']

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
    self.app.Dialog.Edit2.type_keys('Kmp1')
    self.app.Dialog.Zapisz.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    assert 'Tytuły wykonawcze' in self.app[kkvat].Static1.Texts()[0], 'Tytuły wykonawcze - nazwa okna.'

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
    self.app.Dialog.Button.Click()
    self.app.Dialog.OK.Click()
    # self.app[kkvat].type_keys('^a^s')

    # *** Inne ***#

    self.app[kkvat].TreeView.GetItem([u'Inne (sz:9 sw 0)']).Click()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].Button4.Click()
    self.app.Dialog.CheckBox3.Click()
    self.app.Dialog.Button.Click()
    logging.info('Dodanie zabezpieczenia')
    sleep(2)
    self.app[kkvat].ComboBox9.Select(2).Click()
    self.app.Dialog.Button1.ClickInput()
    self.app.Dialog.type_keys('{DOWN 2}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(3)
    self.app.dialog.Button1.Click()
    self.app.Dialog.Button3.Click()
    logging.info('Dodanie organu egzekucyjnego')

    # *** Alimenty ***#

    zmiana_drzewa(self, '\\Stan sprawy\\Alimenty', 'ROSZCZENIE')

    logging.info('ROSZCZENIE - wprowadzenie nowego roszczenia')
    self.app.Dialog.Wait('ready')
    logging.info('ROSZCZENIE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys('10000')
    logging.info('ROSZCZENIE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** Decyzje UWW/NFAL ***#
    """
    zmiana_drzewa(self, '\\Stan sprawy\\Decyzje UWW/NFAL', 'ROSZCZENIE')

    logging.info('ROSZCZENIE - wprowadzenie nowego roszczenia')
    self.app.Dialog.Wait('ready')
    logging.info('ROSZCZENIE - Edit - Kwota')
    self.app.Dialog.Edit1.type_keys('10000')
    logging.info('ROSZCZENIE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()
    """

    # *** Czynność ***#
    self.app[kkvat].TreeView.GetItem([u'Czynności']).Click()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{TAB}')

    self.app[kkvat].syslistview2.RightClick()
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Nie.Click()
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Nie.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow(self)
    logging.info('Zawiadomienie o Zajeciu wierzytelności z rachunku bankowego')

    pozycja2(self)
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 8}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zawiadomienie o aktualnym stanie zadłużenia')

    pozycja2(self)
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 7}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Nie.Click()
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Nie.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow(self)
    logging.info('Zawiadomienie o Zajeciu wierzytelności z rachunku bankowego- zabezpieczenie')

    pozycja2(self)
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 6}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zawiadomienie o aktualnym stanie zadłużenia- zabezpieczenie')

    pozycja2(self)
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 5}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zawiadomienie o uchyleniu zajecia')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 4}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Nie.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow(self)
    logging.info('Zawiadomienie o przejęciu sprawy w wyniku zbiegu egzekucji')

    pozycja2(self)
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 3}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Wezwanie do wykonania obowiązku')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 2}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zawiadomienie ograniczeniu zajęcia')

    # *** Uczesticy postępowania ***#

    self.app[kkvat].type_keys('{TAB}')
    zmiana_drzewa(self, '\\Uczestnicy postęp.', 'UCZESTNICY POSTĘPOWANIA')
    dialog_wprowadzanie_danych(self, dane5_edit, dane5_asercja, 'UCZESTNICY POSTĘP. - DANE')
    dialog_wybór_combobox(self, dane5_combobox, 'UCZESTNICY POSTĘP. - DANE')
    self.app.Dialog.Zapisz.Click()

    zmiana_zakładki(self, 1, 'UCZESTNICY POSTĘP. - DANE KONTA BANKOWEGO')
    self.app.Dialog.type_keys('{DOWN}')
    self.app.Dialog.type_keys('{INSERT}')
    self.app.Dialog.Edit.type_keys("10902687")  # Nazwa1
    # self.app.Dialog.Button1.Click()
    self.app.Dialog.Button3.Click()

    self.app[kkvat].TreeView.GetItem([u'Czynności']).Click()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{TAB}')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{UP 1}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zezwolenie na wypłatę bieżących alimentów lub rent')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.type_keys('{ENTER}')
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Uchylenie zezwolenie na wypłatę bieżących alimentów lub rent')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 1}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zezwolenie na wypłate wynagrodzeń z zajętego rachunku')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 2}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zwolnienie od egzekucji udziału w rachunku bankowym osób trzecich')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 3}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Żądanie udzielenia informacji')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 4}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zapytanie o kwotę wolną od zajęcia')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 5}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zawiadomienie o wykorzystaniu kwoty wolnej od zajęcia')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 6}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Nie.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow(self)
    logging.info('Informacje o zmianie numeru konta')

    self.app[kkvat].type_keys('{TAB}')
    self.app[kkvat].TreeView.GetItem([u'Inne (sz:9; sw 0)']).Click()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].ComboBox9.Select(5).Click()
    self.app.Dialog.Button1.ClickInput()
    self.app.Dialog.type_keys('{DOWN 2}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(3)
    self.app.dialog.Button1.Click()
    self.app.Dialog.Button3.Click()
    logging.info('Dodanie organu egzekucyjnego')

    self.app[kkvat].TreeView.GetItem([u'Czynności']).Click()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{TAB}')
    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 7}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Zawiadomienie o przekazaniu sprawy administracyjnemu organowi egzekucyjnemu')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 8}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Nie.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow(self)
    logging.info('Zawiadomienie o przejęciu sprawy')

    pozycja2(self)

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 9}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Wezwanie do przekazania sprawy')

    pozycja2(self)

    # self.app[kkvat].ListViewa.RightClick()
    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{DOWN 6}')
    self.app[kkvat].type_keys('{ENTER}')
    sleep(2)
    logging.info('wybor')
    self.app.Dialog.ClickInput()
    self.app.Dialog.type_keys('{DOWN 10}')
    self.app.Dialog.type_keys('{ENTER}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()
    self.app.Dialog.Tak.Click()
    self.app.Dialog.Button.Click()
    sleep(8)

    wybor_certyfikatow2(self)
    logging.info('Wyjaśnienie niezgodności danych')

    zapis(self)



