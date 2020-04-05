from uniwersalne_funkcje import *
from time import sleep
from pywinauto.application import Application


def zapytania(self):
    # *** wejscie do zakładki ***#

    self.app[kkvat].type_keys('{DOWN 9}')
    self.app[kkvat].type_keys('{RIGHT}')
    self.app[kkvat].type_keys('{ENTER}')

    pozycja(self)

    # *** Dodanie nowego zapytania ***#

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')
    self.app.Dialog.Wait('ready')

    # *** wybór sprawy ***#

    self.app.Dialog.Edit.type_keys('1/18')
    self.app.Dialog.type_keys('{TAB}')

    self.app.Dialog.Button.Click()

    # *** Dodawanie pojedynczych bankow ***#

    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 2}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 3}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 4}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 5}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 6}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 7}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 8}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 9}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 10}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Button.Click()
    self.app.Dialog.type_keys('{DOWN 11}')
    self.app.Dialog.type_keys('{ENTER}')
    self.app.Dialog.Zapisz.Click()

    pozycja(self)

    # *** Dodawanie dla drugiej sprawy ***#

    self.app[kkvat].type_keys('{DOWN}')
    self.app[kkvat].type_keys('{ENTER}')
    self.app.Dialog.Wait('ready')

    self.app.Dialog.Edit.type_keys('2/18')
    self.app.Dialog.type_keys('{TAB}')

    # *** Dodawnie zestawu***#

    self.app.Dialog.Button2.Click()
    self.app.Dialog.OK.Click()
    self.app.Dialog.Zapisz.Click()

    # *** Zaznaczenie wszystkich pozycji***#

    self.app[kkvat].Button3.Click()
    self.app[kkvat].ListView2.Click()
    self.app[kkvat].type_keys('^a^c')
    self.app[kkvat].Button2.Click()

    sleep(8)
    forma = Application().connect(title_re=".*certyfikatu.*")
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Wait('visible')
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').SetFocus()
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Button5.Click()
    # forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').type_keys('{ENTER}')
    forma.Window_(title='Wybór certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Button4.Click()
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Edit2.ClickInput()
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').Edit2.type_keys('1111')
    forma.Window_(title='Podaj PIN do certyfikatu KWALIFIKOWANEGO (podpis elektroniczny)').OK.Click()
    sleep(10)
    #forma.Window_(title='Wybór certyfikatu NIEKWALIFIKOWANEGO (logowanie)').type_keys('{ENTER}')
    forma.Window_(title='Wybór certyfikatu NIEKWALIFIKOWANEGO (logowanie)').Button4.Click()
    forma.Window_(title='Kancelaria Komornika - VAT').OK.Click()










    """
    Pętla do wyboru pozycji na liście
    for item in range(self.app.Dialog.List1.ItemCount() - 1):
        self.app.Dialog.List1.Select(item + 1)
        lista_tytulow.append(self.app.Dialog.ComboBox1.SelectedText())
        logging.info('TYTUŁY WYKONAWCZE - Combobox - Typ tytułu wykonawczego - '
                     + self.app.Dialog.ComboBox1.SelectedText())
        self.app.Dialog.Zapisz.Click()
        pozycje += 1
        self.app[kkvat].type_keys('{INSERT}')
    """

    #self.app[kkvat].ListView2.RightClick()
    #self.app[kkvat].type_keys('{DOWN}')

