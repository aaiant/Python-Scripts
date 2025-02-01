# Definirea clasei pentru timpul de transfer


# Zona de clase


class TimpTransfer:
    def __init__(self, comprimat: bool, procent: int, latime: int, inaltime: int, culoare_adevarata: bool,
                 nr_biti_transferati: int, tip_biti_transferati: str):
        self._comprimat = comprimat
        self._procent = procent
        self._latime = latime
        self._inaltime = inaltime
        self._culoare_adevarata = culoare_adevarata
        self._nr_biti_transferati = nr_biti_transferati
        self._tip_biti_transferati = tip_biti_transferati

        if comprimat is True:
            self._dimensiune_initiala = self.latime * self.inaltime - (self.latime * self.inaltime) * procent / 100
        else:
            self._dimensiune_initiala = self.latime * self.inaltime

        if culoare_adevarata is True:
            self._nr_total_de_biti = int(self.dimensiune_initiala * 3 * 8)
        else:
            self._nr_total_de_biti = int(self.dimensiune_initiala * 8)

        if self.tip_biti_transferati == "Kbps":
            self.rata_transfer = int(nr_biti_transferati * 10**3)
        elif self.tip_biti_transferati == "Mbps":
            self.rata_transfer = int(nr_biti_transferati * 10**6)
        elif self.tip_biti_transferati == "Gbps":
            self.rata_transfer = int(nr_biti_transferati * 10**9)

        self.nr_secunde_transfer = self.nr_total_de_biti / self.rata_transfer
        self.nr_minute_transfer_total = int(self.nr_secunde_transfer / 60)
        self.nr_secunde_transfer_total = (self.nr_secunde_transfer / 60 - self.nr_minute_transfer_total) * 60

    def __repr__(self):
        return (f"Date: [Nr. biti: {self.nr_total_de_biti}\nRata de transfer: {self.rata_transfer}\n"
                f"Nr. de secunde: {self.nr_secunde_transfer}\nTimp de transfer: "
                f"{self.nr_minute_transfer_total} min {self.nr_secunde_transfer_total} s]")

    #   Zona de Gettere

    @property
    def comprimat(self):
        return self._comprimat

    @property
    def procent(self):
        return self._procent

    @property
    def latime(self):
        return self._latime

    @property
    def inaltime(self):
        return self._inaltime

    @property
    def culoare_adevarata(self):
        return self._culoare_adevarata

    @property
    def nr_biti_transferati(self):
        return self._nr_biti_transferati

    @property
    def tip_biti_transferati(self):
        return self._tip_biti_transferati

    @property
    def dimensiune_initiala(self):
        return self._dimensiune_initiala

    @property
    def nr_total_de_biti(self):
        return self._nr_total_de_biti

    @property
    def nr_secunde_transfer(self):
        return self._nr_secunde_transfer

    #   Zona de Settere
    @comprimat.setter
    def comprimat(self, val):
        assert isinstance(val, bool), \
            f"Comprimat \"{val}\" nu este de tip bool! Va rugam sa introduceti o valoare valida!"
        self._comprimat = val

    @procent.setter
    def procent(self, val):
        assert isinstance(val, int), \
            f"Procent \"{val}\" nu este de tip int! Va rugam sa introduceti o valoare valida!"
        self._procent = val

    @latime.setter
    def latime(self, val):
        assert isinstance(val, int), \
            f"Latimea \"{val}\" nu este de tip int! Va rugam sa introduceti o valoare valida!"
        self._latime = val

    @inaltime.setter
    def inaltime(self, val):
        assert isinstance(val, int), \
            f"Inaltimea \"{val}\" nu este de tip int! Va rugam sa introduceti o valoare valida!"
        self._inaltime = val

    @culoare_adevarata.setter
    def culoare_adevarata(self, val):
        assert isinstance(val, bool), \
            (f"Culoarea adevarata \"{val}\" nu este de tip bool! "
             f"Va rugam sa introduceti o valoarea valida!")
        self._culoare_adevarata = val

    @nr_biti_transferati.setter
    def nr_biti_transferati(self, val):
        assert isinstance(val, int), \
            (f"Nr. de biti transferati pe secunda \"{val}\" nu este de tip int! "
             f"Va rugam sa introduceti o valoarea valida!")
        self._nr_biti_transferati = val

    @tip_biti_transferati.setter
    def tip_biti_transferati(self, val):
        assert isinstance(val, str), \
            (f"Unitatea de masura \"{val}\" nu este de tip: kbps, Mbps, Gbps. "
             f"Va rugam sa introduceti o valoarea valida!")
        self._tip_biti_transferati = val

    @dimensiune_initiala.setter
    def dimensiune_initiala(self, val):
        self._dimensiune_initiala = val

    @nr_total_de_biti.setter
    def nr_total_de_biti(self, val):
        self._nr_total_de_biti = val

    @nr_secunde_transfer.setter
    def nr_secunde_transfer(self, val):
        self._nr_secunde_transfer = val


x = TimpTransfer(True, 85, 1920, 1080, True, 1, "Mbps")
print(x)
