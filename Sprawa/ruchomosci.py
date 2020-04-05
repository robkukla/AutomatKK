from uniwersalne_funkcje import *


def ruchomosci(self):
    dane1_edit = {'Opis': 'Przedmioty', 'Nr. protokołu zaj.': '', 'Dodatkowy opis': '-brak-', 'Cena': '45,00',
                  'PKWIU': '1,00'}

    dane1_asercja = [u'* Opis zajętej ruchomości:Edit', u'Numer protokołu zajęcia:Edit',
                     u'* Dodatkowy opis zajętej ruchomości:Edit', u'* Cena ruchomości:Edit', u'PKWiU:Edit']

    zmiana_drzewa(self, '\\Dłużnicy\\Ruchomości', 'RUCHOMOŚCI')
    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'RUCHOMOŚCI')

    logging.info('RUCHOMOŚCI - DANE RUCHOMOŚCI - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    logging.info('RUCHOMOŚCI - ASERCJA - START')
    assert 'Ruchomości' in self.app[kkvat].Static1.Texts()[0], 'Ruchomości - nazwa okna.'

    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].TypeKeys('{ENTER}')

    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'RUCHOMOŚCI')

    logging.info('RUCHOMOŚCI - ASERCJA - KONIEC')
    self.app.Dialog.Zapisz.Click()