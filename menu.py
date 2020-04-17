import logging


def menu_glowne(self, menu_button, submenu_1=None, submenu_2=None):
    """Funkcja odpowiedzialna za wybór odpowiedniego pola w liście w głównym pasku menu
        menu_button -> główny przycisk
        submenu_1 -> pierwsze podmenu
        subemnu_2...  itd               
           
        Z jakiegoś powodu nie da się podpiąc pod górne menu i nie wykrywa kontrolek, więc trzeba imitować klawiaturę"""

    kkvat = 'Kancelaria Komornika - VAT'

    self.app[kkvat].set_focus()
    self.app[kkvat].type_keys('%')
    if menu_button == 'Repertorium':
        logging.info('OKNO GŁÓWNE - Akcja - Przejście do Repertorium')

        if submenu_1 == 'KM':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu KM')
            self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'KMP':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu KMP')
            for i in range(2):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'KMS':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu KMS')
            for i in range(3):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'KMN':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu KMN')
            for i in range(4):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'KMO':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu KMO')
            for i in range(5):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Skorowidz spraw':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu Skorowidz spraw')
            for i in range(6):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Kalkulator':
            logging.info('OKNO GŁÓWNE - Akcja - Przejście do Submenu Kalkulator')
            for i in range(7):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{RIGHT}')
            self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Skorowidz':
        self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Dłużnicy':
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Wierzyciele':
            for i in range(1):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Pełnomocnicy':
            for i in range(2):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Trzeciodłużnicy':
            for i in range(3):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Licytanci':
            for i in range(4):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Uczestnicy postępowania':
            for i in range(5):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Wszystkie osoby':
            for i in range(6):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Nieruchomości':
            for i in range(7):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Ruchomości':
            for i in range(8):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Księgowość':
        for i in range(2):
            self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Księguj':
            self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Biurowość':
        print("biurowosc")
        for i in range(3):
            self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Wykaz spraw z elementem zagranicznym':
            self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Sprawy z wyboru wierzyciela (wykaz W)':
            for i in range(2):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Zestawienia':
            for i in range(3):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Deklaracje PIT)':
            for i in range(4):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'CEPIK':
            for i in range(5):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'e-Sąd':
            for i in range(6):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Deklaracje wpłat własnych':
            for i in range(7):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'EKW':
            for i in range(8):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'ZUS-EKS - zapytanie o dłużnika':
            for i in range(9):
                self.app[kkvat].type_keys('{DOWN}')
            if submenu_2 == 'ZUS-PUE - wysyłka':
                self.app[kkvat].type_keys('{RIGHT}')
                self.app[kkvat].type_keys('{DOWN}')
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'ZUS-PUE - wysyłka':
            for i in range(9):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Ognivo2':
            for i in range(10):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

            if submenu_2 == 'e-Zapytania (wysłane/odebrane)':
                self.app[kkvat].type_keys('RIGHT')
            self.app[kkvat].type_keys('ENTER')

            if submenu_2 == 'e-Zajęcia (dokumenty do wysłania/wysłane)':
                for i in range(2):
                    self.app[kkvat].type_keys('DOWN')
                self.app[kkvat].type_keys('ENTER')

            if submenu_2 == 'e-Zajęcia (dokumenty odebrane)':
                for i in range(3):
                    self.app[kkvat].type_keys('DOWN')
                self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'ePUAP(e-Zbiegi)':
            for i in range(11):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'pl.ID - rejestr dłużników':
            for i in range(12):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Zlecenia publikacji obwieszczeń':
            for i in range(13):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Import spraw z pliku xml':
            for i in range(14):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Księga druków ścislego zarachowania':
            for i in range(15):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Inwentaryzacja':
            for i in range(16):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Biuro podawcze':
            for i in range(17):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Aplikacja terenowa':
            for i in range(18):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Wiadomości SMS':
            for i in range(19):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')

        if submenu_1 == 'Poczta elektroniczna':
            for i in range(20):
                self.app[kkvat].type_keys('DOWN')
            self.app[kkvat].type_keys('ENTER')


    if menu_button == 'Inne':
        for i in range(4):
            self.app[kkvat].type_keys('{RIGHT}')

        if submenu_1 == 'Koperty i zwrotki':
            self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Konfiguracja':
        for i in range(5):
            self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Historia':
        for i in range(6):
            self.app[kkvat].type_keys('{RIGHT}')

        if submenu_1 == 'Historia spraw':
            self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Historia logowania':
            for i in range(2):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Historia błędnych logowań':
            for i in range(3):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Historia zmian danych osobowych':
            for i in range(4):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Historia usuniętych pozycji':
            for i in range(5):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

        if submenu_1 == 'Historia modyfikacji pozycji':
            for i in range(6):
                self.app[kkvat].type_keys('{DOWN}')
            self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Administracja':
        for i in range(7):
            self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Widok':
        for i in range(8):
            self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')

    if menu_button == 'Program':
        for i in range(9):
            self.app[kkvat].type_keys('{RIGHT}')
        self.app[kkvat].type_keys('{ENTER}')
