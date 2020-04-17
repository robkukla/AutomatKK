from filtrowanie import *
from uniwersalne_funkcje import *


def skorowidz_osoby_filtrowanie(self):
    """"Funkcja odpowiedzialna za wyczerpujące testy filtrów w poziomie skorowidza dla wszystkiego typu osób z osobna:
    wierzyciele, dłużnicy, pełnomocnicy, trzeciodłużnicy, licytanci, uczestnicy postępowania oraz wszystkie osoby.
    Można popróbować z uwzględnieniem checkboxów, ale narazie może być (19.04.2017)  21 kolumn"""

    dane_edit = {'Nazwa1': ['Nazwisko (nazwa1):Edit', 1],
                 'Nazwa2': ['Imię Nazwa2:Edit', 2],
                 'Pesel': ['Pesel:Edit', 12],
                 'NIP': ['NIP:Edit', 10],
                 'Miejscowość': ['Miejscowość:Edit', 3],
                 'Ulica': ['Ulica:Edit', 4],
                 'Nr. domu': ['Numer domu:Edit', 5],
                 'Kraj': ['Kraj:Edit', 5],
                 'Nr. dokumentu': ['Numer dokumentu:Edit', 13],
                 'Regon': ['Regon:Edit', 11]}

    dane_combobox = {'Typ osoby': [['Typ osoby:Combobox', 14], [9, 0, 0]],
                     'Typ': [[u'&Typ:Combobox', False], [2, 0, 2]],
                     'Wierzyciel masowy': [[u'Wierzyciel masowy:combobox', False], [5, 0, 0]],
                     'Status': [[u'Status:combobox', False], [11, 0, 0]]}

    log_typ = str(self.app[kkvat].Static1.Texts()[0].split('Skorowidz osób - ')[1].upper())

    logging.info('')
    logging.info('SKOROWIDZ - ' + log_typ + ' - Przejście do widoku')
    logging.info('')
    for key, value in dane_edit.items():
        logging.info('SKOROWIDZ - ' + log_typ + '- Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('SKOROWIDZ - ' + log_typ + '- Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('SKOROWIDZ - ' + log_typ + ' - Combobox i Edit - Typ i numer sprawy')
    numery_spraw_filtr(self, 'Numery spraw:Edit', numer_kolumny=8)

    time.sleep(3)
    self.app[kkvat].type_keys('{ESC}')

    time.sleep(3)
    self.app[kkvat].type_keys('{ESC}')
