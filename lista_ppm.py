import logging


def lista_rozwijana(self, menu_list):
    """Funkcja odpowiedzialna za wybór poszczególnego
        pola z listy rozwijanej po kliknięciu ppm w pustym
         miejscu"""

    # *** Zmienne ***
    self.kkvat = 'Kancelaria Komornika - VAT'
    kkvat = self.kkvat

    # *** Wybór z 1 poziomu menu ***
    if menu_list == 'dodaj sprawę':
        logging.info('REPERTORIUM - Akcja - Prawy przycisk myszy, dodanie nowej sprawy')
        self.app[kkvat].type_keys('{DOWN}')
        self.app[kkvat].type_keys('{ENTER}')

    if menu_list == 'edytuj sprawę':
        for i in range(2):
            logging.info('REPERTORIUM - Akcja - Prawy przycisk myszy, edytowanie sprawy')
            self.app[kkvat].type_keys('{DOWN}')
        self.app[kkvat].type_keys('{ENTER}')

    if menu_list == 'usuń sprawę':
        for i in range(3):
            logging.info('REPERTORIUM - Akcja - Prawy przycisk myszy, usunięcie sprawy')
            self.app[kkvat].type_keys('{DOWN}')
        self.app[kkvat].type_keys('{ENTER}')

