from filtrowanie import *
import logging


def historia_zmian_danych_osobowych_filtrowanie(self):

    dane_edit = {'Opis': ['Opis:Edit', 1000, 4]}

    dane_combobox = {'Użytkownik': [['Użytkownik:ComboBox', 5], [3, 0, 0]],
                     'Stanowisko': [['Stanowisko:Combobox', 8], [3, 0, 0]],
                     'Źródło danych': [['Źródło danych:Combobox', 9], [2, 0, 0]]}

    for key, value in dane_edit.items():
        logging.info('HISTORIA ZMIAN DANYCH OSOBOWYCH - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('HISTORIA ZMIAN DANYCH OSOBOWYCH - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('HISTORIA ZMIAN DANYCH OSOBOWYCH - Combobox i Edit - Typ i numer sprawy')
    numery_spraw_filtr(self, 'Sprawa:Edit', numer_kolumny=1)

    logging.info('HISTORIA ZMIAN DANYCH OSOBOWYCH - Checkboxy - Daty')
    data_filtr(self, count=2)

    time.sleep(3)
    self.app[kkvat].type_keys('{ESC}')