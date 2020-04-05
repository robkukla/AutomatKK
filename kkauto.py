import tkinter.ttk as ttk
from tkinter import *
from open_app import *

from Sprawa.tytuly_wykonawcze import *
from Sprawa.wierzyciel_dane import *
from Sprawa.peln_wierzyciela import *
from Sprawa.dluznik_dane import *
from Sprawa.peln_dluznika import *
from Sprawa.rachunki import *
from Sprawa.rachunki_wierzyciela import *
from Sprawa.nieruchomosci import *
from Sprawa.ruchomosci import *
from Sprawa.koszty_egzekucji import *
from Sprawa.koszty_sadowe import *
from Sprawa.licytanci import *
from Sprawa.roszczenie import *
from Sprawa.splaty_kosztow_egzekucji import *
from Sprawa.czynnosci import *

from Ognivo.zajecia_KM import *
from Ognivo.zajecia_KMS import *
from Ognivo.zajecia_KMP import *

from Ognivo.zapytania import *

from Ognivo.zapytania_sprawa_KM import *
from Ognivo.zapytania_sprawa_KMS import *
from Ognivo.zapytania_sprawa_KMP import *

from Ksiegowowsc.sprawa import *
from Ksiegowowsc.ksiegowanie_podstawowe import *

from Skorowidz.skorowidz_osoby import *
from Skorowidz.skorowidz_ruchomosci import *
from Skorowidz.skorowidz_nieruchomosci import *

from Historia.historia_blednych_logowan import *
from Historia.historia_logowania import *
from Historia.historia_modyfikacji_pozycji import *
from Historia.historia_spraw import *
from Historia.historia_usunietych_pozycji import *
from Historia.historia_zmian_danych_osobowych import *

from Inne.koperty_i_zwrotki import *
from Inne.generowanie_kopert_w_sprawie import *


class Main:
    """Główna klasa odpowiedzialna za tworzenie GUI. Znajdują się tutaj 2 ramki. 1 Jest odpowiedzialna za przechowywanie
    zakładek, a druga zawiera chceckboxy i przycisk odpalający cały automat"""

    def __init__(self, master):
        """Przypisywanie zmiennych związanych z wszystkimi funkcjami, puste listy, oraz zainicjowanie GUI """
        self.kkvat = 'Kancelaria Komornika - VAT'
        self.app = None
        self.running = False
        self.master = master
        self.checkboxy_sprawa = []
        self.checkboxy_ognivo = []
        self.checkboxy_ksiegowosc = []
        self.checkboxy_skorowidz = []
        self.checkboxy_inne = []
        self.checkboxy_historia = []
        self.checkboxy_rozpoznawanie = []
        self.menu_button = None
        self.submenu_1 = None
        self.submenu_2 = None
        self.menu_list = None

        # *** logger - tworzy plik "logi.log", który pokazuje w którym momencie aplikacja sie wysypała
        logging.basicConfig(filename='logi.log',
                            level=logging.DEBUG,
                            format='%(levelname)s %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S')
        logging.info('----------------------------------------------------------------------NOWY_'
                     'TEST----------------------------------------------------------------------')

        # *** Tytuł okna tkintera ***
        master.title('Automat')

        # *** Tworzenie ramki od zakładek ***
        tabframe = ttk.Notebook(master)

        # *** Tworzenie zakładek ***
        self.sprawa = ttk.Frame(tabframe)
        self.ognivo = ttk.Frame(tabframe)
        self.ksiegowosc = ttk.Frame(tabframe)
        self.skorowidz = ttk.Frame(tabframe)
        self.inne = ttk.Frame(tabframe)
        self.historia = ttk.Frame(tabframe)

        # *** Przypisywanie nazw zakładkom ***
        tabframe.add(self.sprawa, text="Sprawa")
        tabframe.add(self.ognivo, text="Ognivo")
        tabframe.add(self.ksiegowosc, text="Księgowość")
        tabframe.add(self.skorowidz, text="Skorowidz")
        tabframe.add(self.inne, text="Inne")
        tabframe.add(self.historia, text="Historia")

        # *** Podpięcie zakładek pod GUI ***
        tabframe.pack(fill=BOTH, side=TOP, )

        # *** Factory tworzące checkboxy w odpowiednich zakładkach
        self.checkboxy()

    def checkboxy(self):
        """Funkcja odpowiedzialna za tworzenie checkboxów i ich zmiennych (0/1). Dane checkboxa są przepuszczane przez 
        klase MyCheckBox w liście "checkboxy_nazwa", po czym każda pozycja danej listy przechodzi przez pętle do 
        przypisania jej pozycji, zmiennych, tekstu, oraz pozycji w oknie"""

        # *********************************************** SPRAWA *******************************************************
        # *** Tworzenie ramki do zakładki "Sprawa" ***
        sprawa_checkboxesframe = Frame(self.sprawa)

        # *** Zmienne każdego checkboxa (w przyszłości można zrobić pętle na to, bo nie wygląda to najlepiej) ***
        tytuly_wykonawcze_var = IntVar()
        wierzyciel_var = IntVar()
        peln_wierzyciela_var = IntVar()
        rachunki_bankowe_wierzyciela_var = IntVar()
        dluznik_var = IntVar()
        peln_dluznika_var = IntVar()
        rachunki_bankowe_var = IntVar()
        nieruchomosci_var = IntVar()
        ruchomosci_var = IntVar()
        licytanci_var = IntVar()
        roszczenie_var = IntVar()
        koszty_sadowe_var = IntVar()
        koszty_egzekucji_var = IntVar()
        spl_kosztow_egz_var = IntVar()
        czynnosci_var = IntVar()

        # *** Lista tworząca checkboxy do zakładki "Sprawa" ***
        self.checkboxy_sprawa = [
            MyCheckBox('Tytuly wykonawcze', funkcja=tytuly_wykonawcze, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=tytuly_wykonawcze_var),
            MyCheckBox('Wierzyciele', funkcja=wierzyciel_dane, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=wierzyciel_var),
            MyCheckBox('Pelnomocnicy', padx=20, funkcja=peln_wierzyciela, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=peln_wierzyciela_var),
            MyCheckBox('Rachunki Bankowe', padx=20, funkcja=rachunki_bankowe_wierzyciela, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=rachunki_bankowe_wierzyciela_var),
            MyCheckBox('Dłużnicy', funkcja=dluznicy_dane, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=dluznik_var),
            MyCheckBox('Pełnomocnicy', padx=20, funkcja=peln_dluznika, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=peln_dluznika_var),
            MyCheckBox('Rachunki Bankowe', padx=20, funkcja=rachunki_bankowe, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=rachunki_bankowe_var),
            MyCheckBox('Nieruchomości', padx=20, funkcja=nieruchomosci, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=nieruchomosci_var),
            MyCheckBox('Ruchomości', padx=20, funkcja=ruchomosci, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=ruchomosci_var),
            MyCheckBox('Licytanci', funkcja=licytanci, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=licytanci_var),
            MyCheckBox('Roszczenie', padx=20, funkcja=roszczenie, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=roszczenie_var),
            MyCheckBox('Koszty sądowe', padx=20, funkcja=koszty_sadowe, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=koszty_sadowe_var),
            MyCheckBox('Koszty egzekucji', padx=20, funkcja=koszty_egzekucji, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=koszty_egzekucji_var),
            MyCheckBox('Spł. kosztów egz.', padx=40, funkcja=splaty_kosztow_egz, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=spl_kosztow_egz_var),
            MyCheckBox('Czynności', funkcja=czynnosci,menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=czynnosci_var)
        ]

        #  *** Pętla przypisująca każdemu checkboxowi text, zmienną oraz pozycje w zakładce "Sprawa" ***
        checkbox_sprawa_counter = 1
        for checkbox in self.checkboxy_sprawa:
            cb = Checkbutton(sprawa_checkboxesframe,
                             text=checkbox.name,
                             variable=checkbox.var)
            cb.grid(column=0, row=checkbox_sprawa_counter, sticky=W, padx=checkbox.padx)
            checkbox_sprawa_counter += 1

        # *** Przycisk odpalający automat w zakładce "Sprawa" - taki sam znajduje się w każdej zakładce ***
        b = Button(sprawa_checkboxesframe, text="TESTUJ", command=self.sprawdz)
        b.grid(column=1, row=checkbox_sprawa_counter, sticky=E)


        # ******************************************** Ognivo *******************************************************
        # *** Tworzenie ramki do zakładki "Ognivo" ***
        ognivo_checkboxesframe = Frame(self.ognivo)

        zajeciaKM_var = IntVar()
        zajeciaKMS_var = IntVar()
        zajeciaKMP_var = IntVar()
        zapytania_var = IntVar()
        zapytania_sprawaKM_var = IntVar()
        zapytania_sprawaKMS_var = IntVar()
        zapytania_sprawaKMP_var = IntVar()


        # *** Lista tworząca checkboxy do zakładki "Ognivo" ***
        self.checkboxy_ognivo = [
            MyCheckBox('Zajecia KM', padx=40, funkcja=zajeciaKM, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=zajeciaKM_var),
            MyCheckBox('Zajecia KMS', padx=40, funkcja=zajeciaKMS, menu_button='Repertorium',
                       submenu_1='KMS', submenu_2=False, menu_list='dodaj sprawę', var=zajeciaKMS_var),
            MyCheckBox('Zajecia KMP', padx=40, funkcja=zajeciaKMP, menu_button='Repertorium',
                       submenu_1='KMP', submenu_2=False, menu_list='dodaj sprawę', var=zajeciaKMP_var),
            MyCheckBox('Zapytania', padx=40, funkcja=zapytania, menu_button='Biurowość',
                       submenu_1='Ognivo2', submenu_2='e-Zapytania (wysłane/odebrane)', menu_list=False, var=zapytania_var),
            MyCheckBox('Zapytania w sprawie KM', padx=40, funkcja=zapytania_sprawaKM, menu_button='Repertorium',
                       submenu_1='KM', submenu_2=False, menu_list='dodaj sprawę', var=zapytania_sprawaKM_var),
            MyCheckBox('Zapytania w sprawie KMS', padx=40, funkcja=zapytania_sprawaKMS, menu_button='Repertorium',
                       submenu_1='KMS', submenu_2=False, menu_list='dodaj sprawę', var=zapytania_sprawaKMS_var),
            MyCheckBox('Zapytania w sprawie KMP', padx=40, funkcja=zapytania_sprawaKMP, menu_button='Repertorium',
                       submenu_1='KMP', submenu_2=False, menu_list='dodaj sprawę', var=zapytania_sprawaKMP_var)]

        #  *** Pętla przypisująca każdemu checkboxowi text, zmienną oraz pozycje w zakładce "Ognivo" ***
        checkbox_ognivo_counter = 1
        for checkbox in self.checkboxy_ognivo:
            cb = Checkbutton(ognivo_checkboxesframe,
                             text=checkbox.name,
                             variable=checkbox.var)
            cb.grid(column=0, row=checkbox_ognivo_counter, sticky=W, padx=checkbox.padx)
            checkbox_ognivo_counter += 1

        # *** Przycisk odpalający automat w zakładce "Ognivo" - taki sam znajduje się w każdej zakładce ***
        b = Button(ognivo_checkboxesframe, text="TESTUJ", command=self.sprawdz)
        b.grid(column=1, row=checkbox_ognivo_counter, sticky=E)

        # ******************************************** Księgowość *****************************************************
        # *** Tworzenie ramki do zakładki "Księgowość" ***
        ksiegowosc_checkboxesframe = Frame(self.ksiegowosc)

        ksiegowosc_sprawa_var = IntVar()
        ksiegowanie_podstawowe_var = IntVar()

        self.checkboxy_ksiegowosc = [
            MyCheckBox('Założenie spraw', padx=40, funkcja=sprawa, menu_button='Repertorium', submenu_1='KM', submenu_2=False,
                       menu_list='dodaj sprawę', var=ksiegowosc_sprawa_var),
            MyCheckBox('Podstawowe rozksięgowanie', padx=40, funkcja=ksiegowanie_podstawowe, menu_button='Księgowość',
                       submenu_1='Księguj', submenu_2=False, menu_list=False, var=ksiegowanie_podstawowe_var)]

        checkbox_ksiegowosc_counter = 1
        for checkbox in self.checkboxy_ksiegowosc:
            cb = Checkbutton(ksiegowosc_checkboxesframe,
                             text=checkbox.name,
                             variable=checkbox.var)
            cb.grid(column=0, row=checkbox_ksiegowosc_counter, sticky=W, padx=checkbox.padx)
            checkbox_ksiegowosc_counter += 1

        # *** Przycisk odpalający automat w zakładce "Ognivo" - taki sam znajduje się w każdej zakładce ***
        b = Button(ksiegowosc_checkboxesframe, text="TESTUJ", command=self.sprawdz)
        b.grid(column=1, row=checkbox_ksiegowosc_counter, sticky=E)


        # ******************************************** SKOROWIDZ *******************************************************
        # *** Tworzenie ramki do zakładki "Skorowidz" ***
        skorowidz_checkboxesframe = Frame(self.skorowidz)

        # *** Zmienne każdego checkboxa (w przyszłości można zrobić pętle na to, bo nie wygląda to najlepiej) ***
        skorowidz_dluznicy_var = IntVar()
        skorowidz_wierzyciele_var = IntVar()
        skorowidz_pelnomocnicy_var = IntVar()
        skorowidz_trzeciodluznicy_var = IntVar()
        skorowidz_licytanci_var = IntVar()
        skorowidz_uczestnicy_var = IntVar()
        skorowidz_wszystkie_var = IntVar()
        skorowidz_nieruchomosci_var = IntVar()
        skorowidz_ruchomosci_var = IntVar()

        # *** Lista tworząca checkboxy do zakładki "Skorowidz" ***
        self.checkboxy_skorowidz = [
            MyCheckBox('Dłużnicy', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Dłużnicy', submenu_2=False, menu_list=False, var=skorowidz_dluznicy_var),
            MyCheckBox('Wierzyciele', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Wierzyciele', submenu_2=False, menu_list=False, var=skorowidz_wierzyciele_var),
            MyCheckBox('Pełnomocnicy', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Pełnomocnicy', submenu_2=False, menu_list=False, var=skorowidz_pelnomocnicy_var),
            MyCheckBox('Trzeciodłużnicy', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Trzeciodłużnicy', submenu_2=False, menu_list=False, var=skorowidz_trzeciodluznicy_var),
            MyCheckBox('Licytanci', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Licytanci', submenu_2=False, menu_list=False, var=skorowidz_licytanci_var),
            MyCheckBox('Uczestnicy postępowania', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Uczestnicy postępowania', submenu_2=False, menu_list=False, var=skorowidz_uczestnicy_var),
            MyCheckBox('Wszystkie osoby', funkcja=skorowidz_osoby_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Wszystkie osoby', submenu_2=False, menu_list=False, var=skorowidz_wszystkie_var),
            MyCheckBox('Nieruchomości', funkcja=skorowidz_nieruchomosci_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Nieruchomości', submenu_2=False, menu_list=False, var=skorowidz_nieruchomosci_var),
            MyCheckBox('Ruchomości', funkcja=skorowidz_ruchomosci_filtrowanie, menu_button='Skorowidz',
                       submenu_1='Ruchomości', submenu_2=False, menu_list=False, var=skorowidz_ruchomosci_var)]

        #  *** Pętla przypisująca każdemu checkboxowi text, zmienną oraz pozycje w zakładce "Skorowidz" ***
        checkboxy_skorowidz_counter = 1
        for checkbox in self.checkboxy_skorowidz:
            cb = Checkbutton(skorowidz_checkboxesframe,
                             text=checkbox.name,
                             variable=checkbox.var)
            cb.grid(column=0, row=checkboxy_skorowidz_counter, sticky=W, padx=checkbox.padx)
            checkboxy_skorowidz_counter += 1

        # *** Przycisk odpalający automat w zakładce "Skorowidz" - taki sam znajduje się w każdej zakładce ***
        b = Button(skorowidz_checkboxesframe, text="TESTUJ", command=self.sprawdz)
        b.grid(column=1, row=checkboxy_skorowidz_counter, sticky=E)

        # ********************************************** INNE **********************************************************
        # *** Tworzenie ramki do zakładki "Skorowidz" ***
        inne_checkboxesframe = Frame(self.inne)

        # *** Zmienne każdego checkboxa (w przyszłości można zrobić pętle na to, bo nie wygląda to najlepiej) ***
        koperty_i_zwrotki_var = IntVar()
        generowanie_kopert_w_sprawie_var = IntVar()

        # *** Lista tworząca checkboxy do zakładki "Inne" ***
        self.checkboxy_inne = [
            MyCheckBox('Generowanie kopert w sprawie', funkcja=generowanie_kopert_w_sprawie, menu_button='Repertorium',
                       submenu_1= 'KM', submenu_2=False, menu_list= 'dodaj sprawę', var=generowanie_kopert_w_sprawie_var),
            MyCheckBox('Drukowanie kopert i zwrotek', funkcja=koperty_i_zwrotki_filtrowanie, menu_button='Inne',
                       submenu_1='Koperty i zwrotki', submenu_2=False, menu_list=False, var=koperty_i_zwrotki_var)]

        #  *** Pętla przypisująca każdemu checkboxowi text, zmienną oraz pozycje w zakładce "Inne" ***
        checkboxy_inne_counter = 1
        for checkbox in self.checkboxy_inne:
            cb = Checkbutton(inne_checkboxesframe,
                             text=checkbox.name,
                             variable=checkbox.var)
            cb.grid(column=0, row=checkboxy_inne_counter, sticky=W, padx=checkbox.padx)
            checkboxy_inne_counter += 1

        # *** Przycisk odpalający automat w zakładce "Inne" - taki sam znajduje się w każdej zakładce ***
        b = Button(inne_checkboxesframe, text="TESTUJ", command=self.sprawdz)
        b.grid(column=1, row=checkboxy_skorowidz_counter, sticky=E)

        # ****************************************** HISTORIA **********************************************************
        # *** Tworzenie ramki do zakładki "Historia" ***
        historia_checkboxesframe = Frame(self.historia)

        # *** Zmienne każdego checkboxa (w przyszłości można zrobić pętle na to, bo nie wygląda to najlepiej) ***
        historia_spraw_var = IntVar()
        historia_logowania_var = IntVar()
        historia_blednych_logowan_var = IntVar()
        historia_zmian_var = IntVar()
        historia_usunietych_var = IntVar()
        historia_modyfikacji_var = IntVar()

        # *** Lista tworząca checkboxy do zakładki "Historia" ***
        self.checkboxy_historia = [
            MyCheckBox('Historia spraw', funkcja=historia_spraw_filtrowanie,
                       menu_button='Historia', submenu_1='Historia spraw', submenu_2=False, menu_list=None,
                       var=historia_spraw_var),
            MyCheckBox('Historia logowania', funkcja=historia_logowania_filtrowanie,
                       menu_button='Historia', submenu_1='Historia logowania', submenu_2=False, menu_list=None,
                       var=historia_logowania_var),
            MyCheckBox('Historia błędnych logowań', funkcja=historia_blednych_logowan_filtrowanie,
                       menu_button='Historia', submenu_1='Historia błędnych logowań', submenu_2=False, menu_list=None,
                       var=historia_blednych_logowan_var),
            MyCheckBox('Historia zmian danych osobowych', funkcja=historia_zmian_danych_osobowych_filtrowanie,
                       menu_button='Historia', submenu_1='Historia zmian danych osobowych', submenu_2=False, menu_list=None,
                       var=historia_zmian_var),
            MyCheckBox('Historia usuniętych pozycji', funkcja=historia_usunietych_pozycji_filtrowanie,
                       menu_button='Historia', submenu_1='Historia usuniętych pozycji', submenu_2=False, menu_list=None,
                       var=historia_usunietych_var),
            MyCheckBox('Historia modyfikacji pozycji', funkcja=historia_modyfikacji_pozycji_filtrowanie,
                       menu_button='Historia', submenu_1='Historia modyfikacji pozycji', submenu_2=False, menu_list=None,
                       var=historia_modyfikacji_var)]

        #  *** Pętla przypisująca każdemu checkboxowi text, zmie    nną oraz pozycje w zakładce "Historia" ***
        checkboxy_historia_counter = 1
        for checkbox in self.checkboxy_historia:
            cb = Checkbutton(historia_checkboxesframe,
                             text=checkbox.name,
                             variable=checkbox.var)
            cb.grid(column=0, row=checkboxy_historia_counter, sticky=W, padx=checkbox.padx)
            checkboxy_historia_counter += 1

        # *** Przycisk odpalający automat w zakładce "Inne" - taki sam znajduje się w każdej zakładce ***
        b = Button(historia_checkboxesframe, text="TESTUJ", command=self.sprawdz)
        b.grid(column=1, row=checkboxy_skorowidz_counter, sticky=E)

        # *** "Pakowanie" wszystkich zakładek z ich składnikami do głownego okna ***
        sprawa_checkboxesframe.pack()
        ognivo_checkboxesframe.pack()
        ksiegowosc_checkboxesframe.pack()
        skorowidz_checkboxesframe.pack()
        inne_checkboxesframe.pack()
        historia_checkboxesframe.pack()

    def sprawdz(self):
        """ Funkcja wywoływana poprzez naciśnięcie przycisku "TESTUJ". Sprawdza które chceckboxy sa zaznaczone, po czym 
        po kolei przechodzi do odpowiedniego okna, sprawdza czy aplikacja jest już włączona a ostatecznie odpala dla 
        nich ich funkcje, które zostały przypisane w klasie MyCheckBox"""
        lista_checkboxów = [self.checkboxy_sprawa, self.checkboxy_ognivo, self.checkboxy_ksiegowosc,
                            self.checkboxy_skorowidz, self.checkboxy_inne, self.checkboxy_historia]
        count = 0
        for i in lista_checkboxów:
            for checkbox in i:
                if checkbox.var.get():
                    self.menu_button = checkbox.menu_button
                    self.submenu_1 = checkbox.submenu_1
                    self.submenu_2 = checkbox.submenu_2
                    self.menu_list = checkbox.menu_list
                    if self.running is False:
                        startapp(self)
                    checkbox.foo(self)
                    count += 1


class MyCheckBox:
    """Klasa oddpowiedzialna za przypisywanie zmiennych checkboxów - służy do trzymania ich w liście danej zakładki"""
    def __init__(self, name, funkcja, menu_button, submenu_1, submenu_2, var, menu_list, padx=0):
        self.name = name
        self.var = var
        self.padx = padx
        self.foo = funkcja
        self.menu_button = menu_button
        self.submenu_1 = submenu_1
        self.submenu_2 = submenu_2
        self.menu_list = menu_list

# *** Zainicjowanie GUI ***
root = Tk()
my_gui = Main(root)
root.mainloop()
