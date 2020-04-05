from uniwersalne_funkcje import *


def licytanci(self):
    dane1_edit = {
        'Nazwa1': 'Kwaśniewski',
        'Nazwa2': 'Olek',
        'Opis dodatkowy': '-brak-',
        'Ulica': 'Wyborowa',
        'Nr. ulicy': '33',
        'Miejscowość': 'Warszawa',
        'Kod pocztowy': '03-450',
        'Poczta': 'Przedmieście Krakowskie',
        'Gmina': 'Warszawa',
        'Powiat': 'Warszawa',
        'Województwo': 'Mazowieckie'
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
                     u'* Powiat:Edit', u'* Woj.:Edit']

    dane2_edit = {
        'Imię ojca': 'Józef',
        'Imię matki': 'Barbara',
        'Miejsce urodzenia': 'Nowy York',
        'Nip1': '33',
        'Nip2': '20240462',
        'Pesel': '96090402194',
        'Nr. świad.': '12345',
        'Regon': '493317166',
        'Numer dokumentu': 'ATS211397',
        'Nazwisko Rodowe': 'Bęc',
        'Telefon': '508572384',
        'Telefon Kom': '503968464',
        'Email1': 'kwachu@gmail.com',
        'Informacje dodatkowe': '-Dane wygenerowane automatycznie-'
    }

    dane2_asercja = [u'Imię ojca:Edit', u'Imię matki.:Edit', u'Msc. ur.:Edit', u'NIP:Edit1',
                     u'NIP:Edit2', u'Pesel:Edit', u'Inne(nr świad):Edit', u'Regon:Edit2', u'Numer:Edit',
                     u'Nazwisko rodowe:Edit', u'Telefon:Edit', u'Tel. kom.:Edit', u'Email:Edit',
                     u'Informacje dodatk.:Edit']

    zmiana_drzewa(self, '\\Licytanci', 'LICYTANCI')

    # *** Okno wyszukiwania danych ***
    self.app.Dialog.Zapisz.Click()
    logging.info('LICYTANCI - Akcja - Okno wyszukiwania danych')
    time.sleep(10)
    self.app.Dialog.Zapisz.Click()

    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'LICYTANCI - DANE PODSTAWOWE')
    dialog_wybór_combobox(self, dane1_combobox, 'LICYTANCI - DANE PODSTAWOWE')

    zmiana_zakładki(self, 1, 'LICYTANCI - DANE KONTA BANKOWEGO')

    # *** 2 Zakładka " Dane Kont bank." ***
    self.app.Dialog.TypeKeys('{DOWN}')
    self.app.Dialog.TypeKeys('{INSERT}')
    logging.info('LICYTANCI - DANE KONTA BANKOWEGO - Edit - Rachunek')
    self.app.Dialog.Edit.TypeKeys("10902688")  # Nazwa1
    logging.info('LICYTANCI - DANE KONTA BANKOWEGO - Button - 1 (Automatyczne wypelnianie danych)')
    self.app.Dialog.Button1.Click()
    self.app.Dialog.Button1.Click()

    zmiana_zakładki(self, 2, 'LICYTANCI - DANE UZUPEŁNIAJĄCE')
    self.app.Dialog.ComboBox.Select(0)
    dialog_wprowadzanie_danych(self, dane2_edit, dane2_asercja, 'LICYTANCI - DANE UZUPEŁNIAJĄCE', j=2)

    self.app.Dialog.Zapisz.Click()

    # *** WIERZYCIELE - Asercja ***
    logging.info('')
    logging.info('LICYTANCI - ASERCJA - START')
    assert 'Licytanci' in self.app[kkvat].Static1.Texts()[0], 'Licytanci - nazwa okna.'

    logging.info('LICYTANCI - ASERCJA - Zakładka "Dane podstawowe"')
    self.app[kkvat].ListView2.Items()[0].ClickInput()
    self.app[kkvat].TypeKeys('{ENTER}')

    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'LICYTANCI - ASERCJA - DANE PODSTAWOWE')
    zmiana_zakładki(self, 2, 'LICYTANCI - DANE UZUPEŁNIAJĄCE')

    dialog_asercja_danych(self, dane2_edit, dane2_asercja, 'LICYTANCI - ASERCJA - DANE UZUPEŁNIAJĄCE')

    logging.info('LICYTANCI - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()
