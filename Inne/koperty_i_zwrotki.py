from filtrowanie import *
import logging


def koperty_i_zwrotki_filtrowanie(self):

    dane_edit = {'Nazwa': ['Nazwa:Edit', 3],
                 'Adresat': ['Adresat:Edit', 5],
                 'Kod kreskowy': ['Kod kreskowy:Edit', 12],
                 'Skrót nazwy': ['Skrót nazwy:Edit', 4],
                 'Nr. nadawczy': ['Nr nad.:Edit', False]}

    dane_combobox = {'Rodz. listy': [[u'Rodz. Listy:ComboBox', False], [6, 0, 0]],
                     'Operator pocztowy': [[u'Operator pocztowy:ComboBox', 24], [4, 0, 0]],
                     'Stanowisko': [[u'Operator pocztowy:ComboBox2', 9], [3, 1, 1]],
                     'Symbol': [[u'Symbol:ComboBox', 18], [4, 0, 0]],
                     'Wierzyciel masowy': [[u'Wierzyciel masowy:ComboBox', False], [5, 0, 0]],
                     'Do kogo': [[u'Do kogo:ComboBox', False], [34, 0, 0]],
                     'Status łącz.': [[u'Status łącz:ComboBox', 16], [3, 0, 0]],
                     'Potw. odbioru': [[u'Potw. odbioru:ComboBox', False], [4, 0, 0]],
                     'Guid': [[u'GUID:ComboBox', False], [2, 0, 0]]}

    logging.info('')
    logging.info('INNE - KOPERTY I ZWROTKI - przejście do widoku')
    logging.info('')
    for key, value in dane_edit.items():
        logging.info('INNE - KOPERTY I ZWROTKI - Edit - ' + key)
        edit_filtr(self, edit=value[0], numer_kolumny=value[1])

    for key, value in dane_combobox.items():
        logging.info('INNE - KOPERTY I ZWROTKI - Combobox - ' + key)
        combobox_filtr(self, combobox_nazwa=value[0][0], numer_kolumny=value[0][1],
                       count=value[1][0], start=value[1][1], end=value[1][2])

    logging.info('INNE - KOPERTY I ZWROTKI - Combobox i Edit - Typ i numer sprawy')
    numery_spraw_filtr(self, 'N-ry spraw: (np. 15/00;)Edit', combobox='Kod kreskowy:ComboBox',
                       numer_kolumny=1, start=1, end=0)

    logging.info('INNE - KOPERTY I ZWROTKI - Checkboxy - Daty')
    data_filtr(self, count=12)

    time.sleep(3)
    self.app[kkvat].type_keys('{ESC}')
