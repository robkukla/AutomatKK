from uniwersalne_funkcje import *


def nieruchomosci(self):

    dane1_edit = {'Typ': 'dom', 'Nazwa': 'Dom jednorodzinny', 'Ulica': 'Różowa', 'Nr domu': '11',
                  'Miejscowość': 'Wrocław', 'Nr. mieszkania': '1', 'Poczta': 'Krzyki', 'Kod pocztowy': '22-018'}

    dane1_combobox = {'Typ': 'dom', 'Kategoria': 'domy', 'Ulica': 'ul.', 'Województwo': 'dolnośląskie'}

    dane1_asercja = [u'Typ:Edit', u'Nazwa:Edit', u'Ulica:Edit', u'Nr domu:Edit', u'Miejscowość:Edit', u'Nr miesz.:Edit',
                     u'Poczta:Edit', u'Kod:Edit']

    zmiana_drzewa(self, '\\Dłużnicy\\Nieruchomości', 'NIERUCHOMOŚCI')

    dialog_wprowadzanie_danych(self, dane1_edit, dane1_asercja, 'NIERUCHOMOŚCI')
    dialog_wybór_combobox(self, dane1_combobox, 'NIERUCHOMOŚCI')

    logging.info('NIERUCHOMOŚCI - NIERUCHOMOŚĆ - Button - Zapisz')
    self.app.Dialog.Zapisz.Click()

    logging.info('NIERUCHOMOŚCI - ASERCJA - START')
    assert 'Nieruchomości' in self.app[kkvat].Static1.Texts()[0], 'Nieruchomości - nazwa okna.'

    self.app[kkvat].ListView3.Items()[0].ClickInput()
    self.app[kkvat].TypeKeys('{ENTER}')

    dialog_asercja_danych(self, dane1_edit, dane1_asercja, 'NIERUCHOMOŚCI')
    self.app.Dialog.Zapisz.Click()
