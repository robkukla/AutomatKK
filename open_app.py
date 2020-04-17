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
        self.app = Application().connect(title_re=u'Kancelaria Komornika - VAT')
        logging.info('URUCHAMIANIE - ...podłączono')

    # *** Jeśli nie jest włączona - włącz ją i się zaloguj ***
    else:
        logging.info('URUCHAMIANIE - Uruchamianie Kancelarii komornika')
        self.app = Application().start(cmd_line=u'"C:\\Program Files (x86)\\Kancelaria Komornika\\komornik.exe" ')
        logging.info("Czekam 30 sek. na zaladowanie aplikacji")
        sleep(30)
        # DANE DO LOGOWANIA!!!!!!!!!!!!!!!!!!!!!
        logging.info('URUCHAMIANIE - LOGOWANIE - Edit - Login')
        self.app.Dialog.Edit.type_keys('r')
        logging.info('URUCHAMIANIE - LOGOWANIE - Edit - Hasło')
        self.app.Dialog.Edit2.type_keys('x')
        logging.info('URUCHAMIANIE - LOGOWANIE - Button - Zaloguj')
        self.app.Dialog.Zaloguj.Click()

    # *** Przypadek minimalizującego się okna! ***
    logging.info('URUCHAMIANIE - Maksymalizowanie okna (zapobiegawczo)')
    self.app[kkvat].maximize()

    logging.info("odpoczywam 3 s.")
    sleep(3)

    # *** Wejscie do danego pola menu glownego ***
    logging.info('OKNO GŁÓWNE - Akcja - Wybor pola z menu glownego wg. zmiennych menu_button, submenu_1')
    menu_glowne(self, self.menu_button, self.submenu_1, self.submenu_2)

    # Jeśli testy są w repertorium - przejdź do odpowiedniego okna
    if self.menu_button == 'Repertorium':

        # *** Otwarcie listy rozwijanej w repertorium przy uzyciu ppm ***
        list_pos_x = int(GetSystemMetrics(0) / 2)
        list_pos_y = int(GetSystemMetrics(1) * 2 / 3)
        pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))

        # dodawanie sprawy lub otwarcie istniejącej
        if self.menu_list == 'dodaj sprawę':
            # *** Wybrannie danego pola z listy rozwijanej ***
            lista_rozwijana(self, self.menu_list)

            # *** Tworzenie sprawy ***
            self.app.Dialog.Wait('ready')
            self.app.Dialog.Zapisz.Click()
        elif "znajdz sprawę" in self.menu_list:
            logging.info("OKNO GłÓWNE - Akcja - " + self.menu_list)
            pos = self.menu_list.find(":")
            if pos > 0:
                nr_sprawy = self.menu_list[pos + 1:]
                sleep(3)
                nr_sprawy_edit = self.app[kkvat].child_window(class_name="MDIClient")\
                    .child_window(title="Repertorium spraw", class_name="AfxFrameOrView140").\
                    child_window(title="Tab1", class_name="SysTabControl32").Edit1
                nr_sprawy_edit.draw_outline()
                nr_sprawy_edit.set_text(nr_sprawy)
                nr_sprawy_edit.type_keys('{ENTER}')

                self.app[kkvat].child_window(class_name="MDIClient").child_window(title="Repertorium spraw",
                                                                                  class_name="AfxFrameOrView140")\
                    .child_window(class_name="SysListView32", title="", found_index=0)\
                    .double_click()
