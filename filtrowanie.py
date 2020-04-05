import time
import pywinauto

kkvat = 'Afx:00400000:8:00010003:00000000:03790277'


# **** FILTROWANIE EDITÓW ***
def edit_filtr(self, edit, numer_kolumny):

    dane = {'Duże znaki': 'DUZE', 'Małe znaki': 'male', 'Polskie znaki': 'ęóąśłżźćń',
            'Znaki specjalne': '!@#$%^& *_+:>?<', 'Cyfry': '1234567890', 'Dużo znaków': '661348verrvve01234232dvfsvev',
            '2 cyfry': '32', 'x': 'jan', 'x1': '96090402194', 'x2': 'wie'}

    for key, value in dane.items():
        try:
            self.app[kkvat][edit].TypeKeys(value)
            self.app[kkvat].Filtruj.ClickInput()
            if str(self.app[kkvat].ListView.texts()[1]) != ' ( brak ) ':
                if numer_kolumny is not False:
                    rect = self.app[kkvat].ListView.Header.GetColumnRectangle(numer_kolumny - 1)
                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert value.lower() in self.app[kkvat].ListView.texts()[numer_kolumny].lower()
                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert value.lower() in self.app[kkvat].ListView.texts()[numer_kolumny].lower()
            self.app[kkvat][edit].TypeKeys('^a{BACKSPACE}')
        except OSError:
            pass


# **** FILTROWANIE EDITÓW ***
def edit_filtrx(self, edit):

    dane = {'Małe znaki': 'male', 'x': 'komkom', 'a': 'Mikstat', '3': '32'}
    rozpoznano = False

    ilosc_kolumn = self.app[kkvat].ListView.Header.ItemCount()

    for key, value in dane.items():
        try:
            self.app[kkvat][edit].TypeKeys(value)
            print('aaa')
            self.app[kkvat].Filtruj.ClickInput()
            print('sas')
            if str(self.app[kkvat].ListView.texts()[1]) != ' ( brak ) ':
                numer_kolumny = 0
                while numer_kolumny < ilosc_kolumn:
                    if value.lower() in self.app[kkvat].ListView.texts()[numer_kolumny].lower():
                        print(self.app[kkvat].ListView.texts()[numer_kolumny].lower())
                        plik = open("kontrolki.txt", "a")
                        plik.write(str(edit[0]) + ' ' + str(numer_kolumny) + '\n')
                        plik.close()
                        rozpoznano = True
                        numer_kolumny = ilosc_kolumn
                    numer_kolumny += 1
                    print(numer_kolumny)
            self.app[kkvat][edit].TypeKeys('{BACKSPACE}' * len(value))
        except OSError:
            pass
"""
                if numer_kolumny is not False:
                    rect = self.app[kkvat].ListView.Header.GetColumnRectangle(numer_kolumny - 1)
                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert value.lower() in self.app[kkvat].ListView.texts()[numer_kolumny].lower()
                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert value.lower() in self.app[kkvat].ListView.texts()[numer_kolumny].lower()
            self.app[kkvat][edit].TypeKeys('^a{BACKSPACE}')
        
"""


# *** FILTROWANIE NUMERÓW SPRAW ***
def numery_spraw_filtr(self, edit, numer_kolumny, combobox=u'Typ:combobox', end=0, start=0):

    dane = {'Prawidłowo': '1/17', 'Zakres': '1-5', 'Zły zakres': '5-1', 'Dużo znaków': '12345678912345678912345678912',
            'Duże litery': 'JAN', 'Małe litery': 'male', 'Polskie znaki': 'ęóąśłżźćń',
            'Znaki specjalne': '!@#$%^& *_+:>?<'}

    typ_sprawy_count = start
    for i in range(len(dane)):
        while typ_sprawy_count < self.app[kkvat]['Typ:Combobox'].ItemCount() - 1:
            for key, value in dane.items():
                self.app[kkvat][combobox].Select(typ_sprawy_count)
                self.app[kkvat][edit].TypeKeys(value)
                self.app[kkvat].Filtruj.ClickInput()

                if str(self.app[kkvat].ListView.texts()[1]) != ' ( brak ) ':
                    rect = self.app[kkvat].ListView.Header.GetColumnRectangle(numer_kolumny - 1)

                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert self.app[kkvat]['Typ:Combobox'].SelectedText() in \
                        list(self.app[kkvat].ListView.texts()[numer_kolumny])

                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert self.app[kkvat]['Typ:Combobox'].SelectedText() in \
                        list(self.app[kkvat].ListView.texts()[numer_kolumny])

                self.app[kkvat][edit].TypeKeys('{BACKSPACE}' * len(value))

            typ_sprawy_count += 1

    self.app[kkvat][combobox].Select(end)


# *** FILTROWANIE COMBOBOXÓW ***
def combobox_filtr(self, combobox_nazwa, numer_kolumny, count, start=0, end=0):

    combobox_count = start

    while combobox_count < count:
        combobox_count += 1
        self.app[kkvat][combobox_nazwa].Select(combobox_count)
        self.app[kkvat].Filtruj.ClickInput()

        if str(self.app[kkvat].ListView.texts()[1]) != ' ( brak ) ':
            if self.app[kkvat].ListView.texts()[numer_kolumny] != '':
                if numer_kolumny is not False:
                    rect = self.app[kkvat].ListView.Header.GetColumnRectangle(numer_kolumny - 1)

                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert self.app[kkvat][combobox_nazwa].SelectedText().lower() in \
                        self.app[kkvat].ListView.texts()[numer_kolumny].lower()

                    self.app[kkvat].ListView.header.click_input(coords=rect.mid_point())
                    assert self.app[kkvat][combobox_nazwa].SelectedText().lower() in \
                        self.app[kkvat].ListView.texts()[numer_kolumny].lower()

    self.app[kkvat][combobox_nazwa].Select(end)


# *** FILTROWANIE DAT ***
def data_filtr(self, count):

    petla = 0
    while petla < count:
        petla += 2
        datatimepicker1 = u'DataTimePicker' + str(petla-1)
        datatimepicker2 = u'DataTimePicker' + str(petla)
        self.app[kkvat][datatimepicker1].set_time(2019, 3, 2, 1, 14, 20, 1, 5)
        self.app[kkvat].Filtruj.ClickInput()
        self.app[kkvat][datatimepicker1].Click()
        self.app[kkvat].TypeKeys('{SPACE}')
        self.app[kkvat][datatimepicker2].set_time(1987, 3, 2, 1, 14, 20, 1, 5)
        self.app[kkvat].Filtruj.ClickInput()
        self.app[kkvat][datatimepicker2].Click()
        self.app[kkvat].TypeKeys('{SPACE}')
