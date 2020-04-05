from filtrowanie import *
import logging


def historia_logowania_filtrowanie(self):
    dane_edit = {'Nr stanowiska': ['Nr stanowiska:Edit', 2]}

    dane_combobox = {'Użytkownik': [['Użytkownik:ComboBox', 1], [3, 0, 0]]}

    for key, value in dane_edit.items():
        logging.info('HISTORIA LOGOWANIA - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('HISTORIA LOGOWANIA - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('HISTORIA LOGOWANIA - Checkboxy - Daty')
    data_filtr(self, count=2)

    time.sleep(3)
    self.app[kkvat].type_keys('{ESC}')
