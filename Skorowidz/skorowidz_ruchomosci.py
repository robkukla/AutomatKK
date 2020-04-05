from filtrowanie import *
import logging


def skorowidz_ruchomosci_filtrowanie(self):

    dane_edit = {'Opis ruchomości': ['Opis ruchomości:Edit', 1],
                 'Dodatkowy Opis': ['Dodatkowy opis:Edit', 2],
                 'Właściciel Nazwa1': ['Właściciel nazwa1:Edit', 13],
                 'Właściciel Nazwa2': ['Właściciel nazwa2:Edit', 14],
                 'Właściciel Kod': ['Właściciel kod:Edit', 18],
                 'Właściciel Miejscowość': ['Właściciel miejscowość:Edit', 17],
                 'Właściciel Ulica': ['Właściciel ulica:Edit', 15],
                 'Właściciel Poczta': ['Właściciel poczta:Edit', 19],
                 'Właściciel Numer': ['Właściciel numer:Edit', 16]}

    dane_combobox = {'Status ruchomości': [['Status ruchomości:Combobox', False], [2, 0, 0]],
                     'Status sprawy': [['Status sprawy:Combobox', False], [4, 0, 0]],
                     'Licytacje': [['licytacje.komornik.pl:Combobox', False], [2, 0, 0]],
                     'Wyb. ierzyciela': [['Z wyb. wierzyciela:Combobox', 30], [2, 0, 0]],
                     'Rodz. ruchomości': [['Rodzaj ruchomości:Combobox', 12], [2, 0, 0]]}

    logging.info('')
    logging.info('SKOROWIDZ - RUCHOMOŚCI - Przejście do widoku')
    logging.info('')
    for key, value in dane_edit.items():
        logging.info('SKOROWIDZ - RUCHOMOŚCI - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('SKOROWIDZ - RUCHOMOŚCI - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('SKOROWIDZ - RUCHOMOŚCI - Checkboxy - Daty')
    data_filtr(self, count=2)

    logging.info('SKOROWIDZ - RUCHOMOŚCI - Combobox i Edit - Typ i numer sprawy')
    numery_spraw_filtr(self, 'Numery spraw:Edit', numer_kolumny=10)

    time.sleep(3)
    self.app[kkvat].TypeKeys('{ESC}')
