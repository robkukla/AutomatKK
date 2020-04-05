from filtrowanie import *
from uniwersalne_funkcje import *
import logging


def skorowidz_nieruchomosci_filtrowanie(self):

    dane_edit = {'Nazwa nieruchomości': [u'Nazwa nieruchomości:Edit', 4],
                 'Miejscowość': ['Miejscowość:Edit', 5],
                 'Ulica': ['Ulica:Edit', 5],
                 'Numer domu': ['Numer domu:Edit', False],
                 'Dłuznik': ['Dłuznik:Edit', 6],
                 'Syngatura': ['Sygnatura akt sądowych:Edit', 13]}

    dane_combobox = {'Wierzyciel masowy': [['Wierzyciel masowy:Combobox', False], [4, 0, 0]],
                     'Status sprawy': [['Status sprawy:Combobox', False], [4, 0, 0]],
                     'Typ nieruchomości': [['Typ nieruchomości:Combobox', 1], [3, 2, 0]],
                     'Licytacje': [['licytacje.komornik.pl:Combobox', False], [2, 0, 0]],
                     'Vat': [['VAT:Combobox', False], [1, -1, 2]]}

    logging.info('')
    logging.info('SKOROWIDZ - NIERUCHOMOŚCI - przejście do widoku')
    logging.info('')
    for key, value in dane_edit.items():
        logging.info('SKOROWIDZ - NIERUCHOMOŚCI - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('SKOROWIDZ - NIERUCHOMOŚCI - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('SKOROWIDZ - NIERUCHOMOŚCI - Checkboxy - Daty')
    data_filtr(self, count=12)

    logging.info('SKOROWIDZ - NIERUCHOMOŚCI -Combobox i Edit - Typ i numer sprawy')
    numery_spraw_filtr(self, 'Numery spraw:Edit', numer_kolumny=9)

    time.sleep(3)
    self.app[kkvat].TypeKeys('{ESC}')
