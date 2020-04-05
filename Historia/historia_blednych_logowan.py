from filtrowanie import *
from uniwersalne_funkcje import *


def historia_blednych_logowan_filtrowanie(self):
    dane_edit = {'Opis': ['Opis:Edit', 3]}

    dane_combobox = {'Nr. stanowiska': [['Nr. stan:ComboBox', 1], [3, 0, 1]]}

    for key, value in dane_edit.items():
        logging.info('HISTORIA BŁĘDNYCH LOGOWAŃ - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('HISTORIA BŁĘDNYCH LOGOWAŃ - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('HISTORIA BŁĘDNYCH LOGOWAŃ - Checkboxy - Daty')
    data_filtr(self, count=2)

    time.sleep(3)
    self.app[kkvat].TypeKeys('{ESC}')
