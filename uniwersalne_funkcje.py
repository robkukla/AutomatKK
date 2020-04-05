import logging
import time
from win32api import GetSystemMetrics
import pywinauto
from time import sleep
from pywinauto.application import Application


kkvat = 'Kancelaria Komornika - VAT'


def zmiana_drzewa(self, nazwa, text):
    logging.info('')
    logging.info(text + ' - Treeview - Wybór pola w drzewie')
    logging.info('')
    self.app[kkvat].TreeView.GetItem(nazwa).ClickInput()
    logging.info(text + ' - Akcja - Dodanie nowego Pola')
    self.app[kkvat].TypeKeys('{ENTER}')
    self.app[kkvat].TypeKeys('{INSERT}')


def zmiana_zakładki(self, nazwa, text):
    logging.info('')
    logging.info(text + ' - Zmiana zakładki')
    logging.info('')
    self.app.Dialog.TabControl.WrapperObject().Select(nazwa)


def dialog_wprowadzanie_danych(self, dict_edit, list_edit, text, i=0, j=1):
    for key, value in dict_edit.items():
        logging.info(text + ' - Edit - ' + key)
        if self.app.Dialog[list_edit[i]].Texts()[0] != '':
            self.app.Dialog['Edit' + str(j+1)].TypeKeys('^a{BACKSPACE}')
        self.app.Dialog['Edit' + str(j)].TypeKeys(value, with_spaces=True)
        i += 1
        j += 1


def dialog_wybór_combobox(self, dict_combobox, text):
    i = 1
    for key, value in dict_combobox.items():
        logging.info(text + ' - Combobox - ' + key)
        self.app.Dialog['ComboBox' + str(i)].Select(value)
        i += 1


def dialog_asercja_danych(self, dict_edit, list_edit, text):
    logging.info(text)
    i = 0
    for key, value in dict_edit.items():
        print(value, self.app.Dialog[list_edit[i]].Texts()[0])
        assert self.app.Dialog[list_edit[i]].Texts()[0] == value, 'Niepoprawny Edit - ' + key
        i += 1


def pozycja(self):
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 1 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))


def pozycja2(self):
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 1 / 2)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))


def zapis(self):
    logging.info('SPRAWA - F7 - wyjście z zapisem')
    time.sleep(3)
    self.app[kkvat].TypeKeys('{F7}')


def resetowanie(self):
    time.sleep(3)
    self.app[kkvat].TypeKeys('{ESC}')


def wybor_certyfikatow(self):
    forma = Application().connect(title_re=".*certyfikatu.*")
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Button5.Click()
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').TypeKeys('{ENTER}')
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Edit2.TypeKeys('1111')
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').OK.Click()
    sleep(8)
    forma.Window_(title='').Button4.Click()
    sleep(2)
    forma.Window_(title='Wybór certyfikatu NIEKWALIFIKOWANEGO (logowanie)').TypeKeys('{ENTER}')
    forma.Window_(title='Kancelaria Komornika - VAT').OK.Click()
    sleep(4)
    self.app.Dialog.Nie.Click()


def wybor_certyfikatow2(self):
    forma = Application().connect(title_re=".*certyfikatu.*")
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Button5.Click()
    #forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').TypeKeys('{DOWN 2}')
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').TypeKeys('{ENTER}')
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Edit2.TypeKeys('1111')
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').OK.Click()
    sleep(8)
    forma.Window_(title='Wybór certyfikatu NIEKWALIFIKOWANEGO (logowanie)').TypeKeys('{ENTER}')
    forma.Window_(title='Kancelaria Komornika - VAT').OK.Click()
    sleep(4)
    self.app.Dialog.Nie.Click()


"""def proste_rozksiegowanie(self):
    self.app[kkvat].ListView.DoubleClick()
    self.app[kkvat].TypeKeys('{F7}')
    sleep(2)
    self.app.dialog.Zapisz.Click()"""