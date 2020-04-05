from lista_ppm import lista_rozwijana
from menu import menu_glowne
from pywinauto.application import Application
import win32ui
from win32api import GetSystemMetrics
import pywinauto
import logging
from time import sleep


def startapp(self):
    """Funckja uruchamiana za każdym razem po kliknięciu przycisku "testuj", w przypadku jeśli jest to 
    pierwsze kliknięcie podczas sesji, to uruchamia aplikacje ze ścieżki KK lub podpina się pod istniejący proces."""
    kkvat = self.kkvat
    self.running = True

    # *** Sprawdza czy aplikacja jest włączona ***
    def isrunning(tmp):
        try:
            if win32ui.FindWindow(None, tmp):
                logging.info('URUCHAMIANIE - Kancelaria Komornika jest uruchomiona!')
                return True
        except win32ui.error:
            return False
        sleep(3)

    # *** Jeśli jest włączona - podłącz się do niej ***
    if isrunning(self.kkvat):
        logging.info('URUCHAMIANIE -Próba podłączenia do uruchomionej aplikacji...')
        self.app = Application().Connect(title_re=u'Kancelaria Komornika - VAT')
        logging.info('URUCHAMIANIE - ...podłączono')

    # *** Jeśli nie jest włączona - włącz ją i się zaloguj ***
    else:
        logging.info('URUCHAMIANIE - Uruchamianie Kancelarii komornika')
        self.app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Kancelaria Komornika\\komornik.exe" ')
        sleep(3)
        # DANE DO LOGOWANIA!!!!!!!!!!!!!!!!!!!!!
        logging.info('URUCHAMIANIE - LOGOWANIE - Edit - Login')
        self.app.Dialog.Edit.TypeKeys('a')
        logging.info('URUCHAMIANIE - LOGOWANIE - Edit - Hasło')
        self.app.Dialog.Edit2.TypeKeys('a')
        logging.info('URUCHAMIANIE - LOGOWANIE - Button - Zaloguj')
        self.app.Dialog.Zaloguj.Click()

    # *** Przypadek minimalizującego się okna! ***
    logging.info('URUCHAMIANIE - Maksymalizowanie okna (zapobiegawczo)')
    self.app[kkvat].Maximize()

    # *** Wejscie do danego pola menu glownego ***
    logging.info('OKNO GŁÓWNE - Akcja - Wybor pola z menu glownego wg. zmiennych menu_button, submenu_1')
    menu_glowne(self, self.menu_button, self.submenu_1, self.submenu_2)

    # Jeśli testy są w repertorium - przejdź do odpowiedniego okna
    if self.menu_button == 'Repertorium':

        # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
        list_pos_x = int(GetSystemMetrics(0) / 2)
        list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
        pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

        # dodawanie sprawy
        if self.menu_list == 'dodaj sprawę':
            # *** Wybrannie danego pola z listy rozwijanej ***
            lista_rozwijana(self, self.menu_list)

            # *** Tworzenie sprawy ***
            self.app.Dialog.Wait('ready')
            self.app.Dialog.Zapisz.Click()

