from uniwersalne_funkcje import *
from time import sleep


def tytuly_wykonawcze(self):
    """
    Funkcja sprawdzająca tytuły wykonawcze. Aktualne rzeczy:
    - Dodawanie wszystkich aktualnych typów tytułów wykonawczych z comboboxa
    - Porównywanie wprowadzonych nazw z tym co się wyświetla na liście
    
    TO DO:
    - Kombinacje z pozostałymi danymi możliwymi do wprowadzenia
    """
    pozycje = 0
    lista_tytulow = []
    logging.info('')
    logging.info('TYTUŁY WYKONAWCZE - Treeview - Wybór pola w drzewie')
    logging.info('')

    sleep(1.5)
    self.app[kkvat].TreeView.GetItem([u'Tytuły Wykonawcze']).Click()
    logging.info('TYTUŁY WYKONAWCZE - Akcja - Dodanie nowego tytułu wykonawczego')
    self.app[kkvat].type_keys('{ENTER}')

    self.app[kkvat].type_keys('{INSERT}')
    for item in range(self.app.Dialog.Combobox.ItemCount() - 1):
        self.app.Dialog.ComboBox1.Select(item + 1)
        lista_tytulow.append(self.app.Dialog.ComboBox1.SelectedText())
        logging.info('TYTUŁY WYKONAWCZE - Combobox - Typ tytułu wykonawczego - '
                     + self.app.Dialog.ComboBox1.SelectedText())
        self.app.Dialog.Zapisz.Click()
        pozycje += 1
        self.app[kkvat].type_keys('{INSERT}')

    self.app.Dialog.Anuluj.Click()

    logging.info('TYTUŁY WYKONAWCZE - ASERCJA')
    dlugosc_tytuly = len(self.app[kkvat].ListView2.texts())

    assert 'Tytuły wykonawcze' in self.app[kkvat].Static1.Texts()[0], 'Tytuły wykonawcze - nazwa okna.'
    assert len(self.app[kkvat].ListView2.texts()[1:dlugosc_tytuly:10]) == pozycje, 'Niepoprawna ilość tytułów wyk.'
    assert lista_tytulow == self.app[kkvat].ListView2.texts()[1:dlugosc_tytuly:10], 'Niepoprawne tytuły wykonawcze'
