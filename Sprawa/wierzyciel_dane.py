from uniwersalne_funkcje import *
from time import sleep

def wierzyciel_dane(self):

    # *** Słowniki i listy z danymi ***
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
                'Kraj': 'Polska',
                'Ulica dod.': 'Czerwona',
                'Nr. ulicy dod': '33',
                'Miejscowość dod.': 'Wrocław',
                'Kod pocztowy dod.': '02-500',
                'Poczta dod.': 'Wrocław',
                'Gmina dod.': 'Wrocław',
                'Powiat dod.': 'Wrocław',
                'Województwo dod.': 'Dolnośląskie',
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

    dane2_asercja = [u'GUID MPE:Edit', u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'&NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2',
                     u'Numer:Edit', u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Tel. kom.:Edit', u'Email:Edit',
                     u'Email faktury VAT:Edit', u'Informacje dodatk.:Edit']

    dane3_edit = {
                'Opis dodatkowy': 'Firma testowa',
                'Ulica': 'Zielona',
                'Nr. ulicy': '22',
                'Miejscowość': 'Kraków',
                'Kod pocztowy': '30-092',
                'Poczta': 'Dębniki',
                'Gmina': 'Kraków',
                'Powiat': 'Kraków',
                'Województwo': 'Małopolskie'
    }

    dane3_asercja = [u'Nazwa:Edit', u'Adres dla fakturyEdit0', u'Numer:Edit', u'Miejscowość.:Edit', u'Kod:Edit1',
                     u'Poczta:Edit2', u'Gmina:Edit', u'Powiat:Edit2', u'Woj.:Edit']

    # *** Wybór drzewa "Wierzyciele" ***
    zmiana_drzewa(self, '\\Wierzyciele', 'WIERZYCIELE')

    # *** Okno wyszukiwania danych ***
    logging.info('WIERZYCIELE - Akcja - Okno wyszukiwania danych')
    logging.info('')
    self.app.Dialog.Zapisz.Click()
    sleep(10)
    self.app.Dialog.Zapisz.Click()

    # *** 1 Zakładka "Dane podst" ***
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'WIERZYCIELE - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'WIERZYCIELE - DANE PODSTAWOWE')
    """
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
    """
    # *** 3 Zakładka "Dane uzupełniające" ***
    zmiana_zakładki(self, 1, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')

    logging.info('WIERZYCIELE - DANE UZUPEŁNIAJĄCE - Combobox - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')
    self.app.Dialog.print_control_identifiers()

    # *** 4 zakładka "Dane dodatkowe" ***
    zmiana_zakładki(self, 2, 'WIERZYCIELE - DANE DODATKOWE')

    logging.info('WIERZYCIELE - DANE DODATKOWE - Checkbox - Adres dla faktury')
    self.app.Dialog.Chceckbox0.CheckByClick()
    logging.info('WIERZYCIELE - DANE UZUPEŁNIAJĄCE - Combobox - Typ dokumentu')
    self.app.Dialog.ComboBox.Select(1)
    dialog_wprowadzanie_danych(self, dane3_edit, dane3_asercja, 'WIERZYCIELE - DANE DODATKOWE')

    # *** Zapis utworzonego Wierzyciela ***
    self.app.Dialog.Wait('ready')
    logging.info('WIERZYCIELE - DANE DODATKOWE - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    # *** Asercja wprowadzonych danych ***
    logging.info('')
    logging.info('WIERZYCIELE - ASERCJA - START')
    assert 'Wierzyciele' in self.app[kkvat].Static1.Texts()[0], 'Wierzyciele - nazwa okna.'

    # *** Wejście do utworzonego wierzyciela ***
    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].type_keys('{ENTER}')

    logging.info('WIERZYCIELE - ASERCJA - Zakładka "Dane podstawowe"')
    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'WIERZYCIELE - ASERCJA - DANE PODSTAWOWE')
    zmiana_zakładki(self, 1, 'WIERZYCIELE - DANE UZUPEŁNIAJĄCE')
    dialog_asercja_danych(self, dane2_edit, dane2_asercja, 'WIERZYCIELE - ASERCJA - DANE UZUPEŁNIAJĄCE')
    zmiana_zakładki(self, 2, 'WIERZYCIELE - DANE DODATKOWE')
    dialog_asercja_danych(self, dane3_edit, dane3_asercja, 'WIERZYCIELE - ASERCJA - DANE DODATKOWE')
    logging.info('WIERZYCIELE - KONIEC ASERCJI')
    self.app.Dialog.Zapisz.Click()
