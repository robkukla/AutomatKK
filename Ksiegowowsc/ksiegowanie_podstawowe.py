from uniwersalne_funkcje import *
from time import sleep
from pywinauto.application import Application
import pywinauto

kkvat = 'Afx:00400000:8:00010003:00000000:00051545'


def ksiegowanie_podstawowe(self):
    dane1_edit = {
        'Numer dowodu': '1',
        'Numer sprawy': '100/18',
        'Kwota': '12000'
    }

    dane1_asercja = [u'Numer dowodu:Edit', u'Numer sprawy:Edit', u'Kwota:Edit']

    dane2_edit = {
        'Numer dowodu': '2',
        'Numer sprawy': '101/18',
        'Kwota': '34000'
    }

    dane3_edit = {
        'Numer dowodu': '2',
        'Numer sprawy': '102/18',
        'Kwota': '6817'
    }

    self.app[kkvat].type_keys('{INSERT}')

    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'Wprowadzanie pozycji 1')
    self.app.Dialog.Combobox3.Select(3)
    self.app.Dialog.Combobox6.Select(0)
    self.app.Dialog.Zapisz.Click()

    dialog_wprowadzanie_danych(self, dane2_edit, dane1_asercja, 'Wprowadzanie pozycji 2')
    self.app.Dialog.Combobox3.Select(4)
    self.app.Dialog.Combobox6.Select(0)
    self.app.Dialog.Zapisz.Click()

    dialog_wprowadzanie_danych(self, dane3_edit, dane1_asercja, 'Wprowadzanie pozycji 3')
    self.app.Dialog.Combobox3.Select(23)
    self.app.Dialog.Combobox6.Select(0)
    self.app.Dialog.Zapisz.Click()

    self.app.Dialog.Anuluj.Click()

    ###Rozksiegowanie 1 sprawy
    self.app[kkvat].ListView.DoubleClick()
    sleep(2)
    self.app[kkvat].type_keys('{F7}')
    self.app.Dialog.Zapisz.Click()

    sleep(2)

    ###Rozksiegowanie 2 sprawy
    self.app[kkvat].ListView.DoubleClick()
    sleep(2)
    self.app[kkvat].type_keys('{F7}')
    sleep(2)
    self.app.Dialog.Zapisz.Click()

    ###Rozksiegowanie 3 sprawy
    self.app[kkvat].ListView.DoubleClick()
    self.app[kkvat].TreeView.GetItem([u'Stan sprawy', u'Rozksięgowanie', u'Koszty egzekucji']).ClickInput()
    self.app[kkvat].type_keys('{ENTER}')
    self.app[kkvat].type_keys('{INSERT}')
    self.app.Dialog.TreeView.GetItem([u'Opłaty Stałe', u'Art.53a.1 - Poszukiwanie majątku (3%)']).Click()
    self.app.Dialog.Dalej.Click()
    self.app.Dialog.Zapisz.Click()
    self.app[kkvat].type_keys('{F7}')
    sleep(2)
