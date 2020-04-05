from uniwersalne_funkcje import *


def stan_sprawy(self):
    """Sporo zmiennych do przypisania, masa sprawdzania"""
    logging.info('')
    logging.info('STAN SPRAWY - Treeview - Wybór pola w drzewie')
    logging.info('')
    kkvat = 'Kancelaria Komornika - VAT - [Kowalski Jan  KONTRA  Białek Michał]'
    self.app[kkvat].TreeView.GetItem([u'Stan sprawy']).ClickInput()
    self.app[kkvat].TypeKeys('{ENTER}')
    ss_do_zaplaty = float(self.app[kkvat].Edit4.Texts()[0].replace(',', '.').replace(' ', ''))
    ss_opl_stos_8_naleznosc = float(self.app[kkvat].Edit5.Texts()[0].replace(',', '.'))
    ss_opl_stos_8_do_zaplaty = float(self.app[kkvat].Edit6.Texts()[0].replace(',', '.'))
    ss_wierzyciel_naleznosc = float(self.app[kkvat].Edit7.Texts()[0].replace(',', '.'))
    ss_wierzyciel_do_pobrania = float(self.app[kkvat].Edit10.Texts()[0].replace(',', '.'))
    ss_koszty_sadowe_naleznosc = float(self.app[kkvat].Edit31.Texts()[0].replace(',', '.'))
    ss_koszty_sadowe_do_pobrania = float(self.app[kkvat].Edit34.Texts()[0].replace(',', '.'))
    ss_razem_naleznosc = float(self.app[kkvat].Edit43.Texts()[0].replace(',', '.'))
    ss_razem_do_pobrania = float(self.app[kkvat].Edit46.Texts()[0].replace(',', '.'))
    ss_koszty_egz_brutto_naleznosc = float(self.app[kkvat].Edit51.Texts()[0].replace(',', '.'))
    ss_koszty_egz_brutto_pobrano = float(self.app[kkvat].Edit52.Texts()[0].replace(',', '.'))
    ss_koszty_egz_brutto_do_pobrania = float(self.app[kkvat].Edit54.Texts()[0].replace(',', '.'))
    ss_ogolem_naleznosc = float(self.app[kkvat].Edit55.Texts()[0].replace(',', '.'))
    ss_ogolem_pobrano = float(self.app[kkvat].Edit56.Texts()[0].replace(',', '.'))
    ss_ogolem_do_pobrania = float(self.app[kkvat].Edit58.Texts()[0].replace(',', '.'))
    ss_porto = float(self.app[kkvat].Edit60.Texts()[0].replace(',', '.'))
    ss_opl_stosunkowa_do_pobrania = float(self.app[kkvat].Edit63.Texts()[0].replace(',', '.'))
    ss_vat = float(self.app[kkvat].Edit67.Texts()[0].replace(',', '.'))
    ss_opl_stosunkowa_8_pobrano = float(self.app[kkvat].Edit68.Texts()[0].replace(',', '.'))
    ss_koszty_egz_vat_naleznosc = float(self.app[kkvat].Edit69.Texts()[0].replace(',', '.'))
    ss_koszty_egz_vat_do_pobrano = float(self.app[kkvat].Edit70.Texts()[0].replace(',', '.'))
    ss_koszty_egz_vat_do_uznania = float(self.app[kkvat].Edit71.Texts()[0].replace(',', '.'))
    ss_koszty_egz_vat_do_pobrania = float(self.app[kkvat].Edit72.Texts()[0].replace(',', '.'))
    ss_koszty_egz_netto_naleznosc = float(self.app[kkvat].Edit73.Texts()[0].replace(',', '.'))
    ss_koszty_egz_netto_pobrano = float(self.app[kkvat].Edit74.Texts()[0].replace(',', '.'))

    assert ('%.2f'%(ss_koszty_egz_brutto_naleznosc - ss_koszty_egz_brutto_pobrano == ss_koszty_egz_brutto_do_pobrania))
    assert ('%.2f'%(ss_koszty_egz_vat_naleznosc - ss_koszty_egz_vat_do_pobrano == ss_koszty_egz_vat_do_pobrania))
    assert ('%.2f'%(ss_ogolem_naleznosc - ss_ogolem_pobrano == ss_ogolem_do_pobrania))
    assert ('%.2f'%(ss_ogolem_do_pobrania + ss_porto + ss_opl_stosunkowa_do_pobrania + ss_vat == ss_do_zaplaty))
    assert ('%.2f'%(ss_do_zaplaty - ss_opl_stos_8_naleznosc - ss_opl_stosunkowa_8_pobrano == ss_opl_stos_8_do_zaplaty))