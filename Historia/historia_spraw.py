from filtrowanie import *
import logging


def historia_spraw_filtrowanie(self):
    dane_edit = {'Nr stanowiska': ['Nr stanowiska:Edit', 4]}

    dane_combobox = {'Użytkownik': [['Uzytkownik:Combobox', 3], [3, 0, 0]],
                     'Operacja':  [['Operacja:Combobox', False], [3, 0, 3]]}

    for key, value in dane_edit.items():
        logging.info('HISTORIA SPRAW - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('HISTORIA SPRAW - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('HISTORIA SPRAW - Combobox i Edit - Typ i numer sprawy')
    numery_spraw_filtr(self, 'Sprawa:Edit', numer_kolumny=1)

    logging.info('HISTORIA SPRAW - Checkboxy - Daty')
    data_filtr(self, count=2)

    time.sleep(3)
    self.app[kkvat].TypeKeys('{ESC}')