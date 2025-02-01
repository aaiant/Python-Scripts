class Latenta:
    def __init__(self, marimea_fisierului: float, viteza_de_propagare: float, unitate_de_masura_a_vitezei: str,
                 distanta: float, unitate_de_masura_a_distantei: str, viteza_internet: float,
                 unitatea_de_masura_a_vitezei_internetului: str):

        self.marimea_fisierului = marimea_fisierului
        self.viteza_de_propagare = viteza_de_propagare
        self.unitate_de_masura_a_vitezei = unitate_de_masura_a_vitezei
        self.distanta = distanta
        self.unitate_de_masura_a_distantei = unitate_de_masura_a_distantei
        self.viteza_internet = viteza_internet
        self.viteza_internet_afisare = viteza_internet
        self.unitatea_de_masura_a_vitezei_internetului = unitatea_de_masura_a_vitezei_internetului
        self.intarzierea_de_propagare = None
        self.intarzierea_de_transmisie = None
        self.latenta = None
        self.latenta_formatata = None

        self.transformarea_vitezei()
        self.transformarea_distantei()
        self.transformarea_vitezei_internetului()

        self.determinarea_intarzierii_de_propagare()
        self.determinarea_intarzierii_de_transmisie()
        self.determinarea_latentei()

    #   Zona de Gettere

    @property
    def viteza_de_propagare(self):
        return self._viteza_de_propagare

    @property
    def unitate_de_masura_a_vitezei(self):
        return self._unitate_de_masura_a_vitezei

    @property
    def distanta(self):
        return self._distanta

    @property
    def marimea_fisierului(self):
        return self._marimea_fisierului

    @property
    def unitate_de_masura_a_distantei(self):
        return self._unitate_de_masura_a_distantei

    @property
    def viteza_internet(self):
        return self._viteza_internet

    @property
    def viteza_internet_afisare(self):
        return self._viteza_internet_afisare

    @property
    def unitatea_de_masura_a_vitezei_internetului(self):
        return self._unitatea_de_masura_a_vitezei_internetului

    @property
    def intarzierea_de_propagare(self):
        return self._intarzierea_de_propagare

    @property
    def intarzierea_de_transmisie(self):
        return self._intarzierea_de_transmisie

    @property
    def latenta(self):
        return self._latenta

    @property
    def latenta_formatata(self):
        return self._latenta_formatata

        #   Zona de Settere
    @marimea_fisierului.setter
    def marimea_fisierului(self, val):
        assert isinstance(val, float), (f"Marimea fisierului \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._marimea_fisierului = val

    @unitate_de_masura_a_vitezei.setter
    def unitate_de_masura_a_vitezei(self, val):
        assert isinstance(val, str), (f"Unitatea de masura \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitate_de_masura_a_vitezei = val.lower()

    @viteza_de_propagare.setter
    def viteza_de_propagare(self, val):
        assert isinstance(val, float), (f"Viteza de propagare \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._viteza_de_propagare = val

    @distanta.setter
    def distanta(self, val):
        assert isinstance(val, float), (f"Distanta \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._distanta = val

    @unitate_de_masura_a_distantei.setter
    def unitate_de_masura_a_distantei(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a distantei \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitate_de_masura_a_distantei = val.lower()

    @viteza_internet.setter
    def viteza_internet(self, val):
        assert isinstance(val, float), (f"Viteza internetului \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._viteza_internet = val

    @viteza_internet_afisare.setter
    def viteza_internet_afisare(self, val):
        assert isinstance(val, float), (f"Viteza internetului \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._viteza_internet_afisare = val

    @unitatea_de_masura_a_vitezei_internetului.setter
    def unitatea_de_masura_a_vitezei_internetului(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a vitezei internetului \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitatea_de_masura_a_vitezei_internetului = val.capitalize()

    @intarzierea_de_propagare.setter
    def intarzierea_de_propagare(self, val):
        self._intarzierea_de_propagare = val

    @intarzierea_de_transmisie.setter
    def intarzierea_de_transmisie(self, val):
        self._intarzierea_de_transmisie = val

    @latenta.setter
    def latenta(self, val):
        self._latenta = val

    @latenta_formatata.setter
    def latenta_formatata(self, val):
        self._latenta_formatata = val

    def __repr__(self):
        return f""" *{self.viteza_internet_afisare}{self.unitatea_de_masura_a_vitezei_internetului.capitalize()}

File size: {self.marimea_fisierului} Bits
Date rate: {self.viteza_internet} Bits/s
Propagation delay = {self.distanta} m / {self.viteza_de_propagare} m/s =  {self.intarzierea_de_propagare} s
Transmission delay = {self.marimea_fisierului} Bits / {self.viteza_internet} Bits/s = {self.intarzierea_de_transmisie} s
Waiting time = 0 s
Latency = propagation delay + transmission delay = {self.intarzierea_de_propagare} s + {self._intarzierea_de_transmisie} s = {self.latenta} s = {self.latenta_formatata}
"""

    def transformarea_vitezei(self):
        match self.unitate_de_masura_a_vitezei:
            #   Prima parte (distanta/s)
            case "mm/s":
                self.viteza_de_propagare *= 10 ** (-3)
            case "cm/s":
                self.viteza_de_propagare *= 10 ** (-2)
            case "dm/s":
                self.viteza_de_propagare *= 10 ** (-1)
            case "m/s":
                self.viteza_de_propagare = self.viteza_de_propagare
            case "dam/s":
                self.viteza_de_propagare *= 10
            case "hm/s":
                self.viteza_de_propagare *= 10 ** 2
            case "km/s":
                self.viteza_de_propagare *= 10 ** 3
            #   A doua parte (distanta/min)
            case "mm/min":
                self.viteza_de_propagare *= 10**(-3) / 60
            case "cm/min":
                self.viteza_de_propagare *= 10 ** (-2) / 60
            case "dm/min":
                self.viteza_de_propagare *= 10 ** (-1) / 60
            case "m/min":
                self.viteza_de_propagare = self.viteza_de_propagare / 60
            case "dam/min":
                self.viteza_de_propagare *= 10 / 60
            case "hm/min":
                self.viteza_de_propagare *= 10 ** 2 / 60
            case "km/min":
                self.viteza_de_propagare *= 10 ** 3 / 60
            #   A treia parte (distanta/h)
            case "mm/h":
                self.viteza_de_propagare *= 10 ** (-3) / 3600
            case "cm/h":
                self.viteza_de_propagare *= 10 ** (-2) / 3600
            case "dm/h":
                self.viteza_de_propagare *= 10 ** (-1) / 3600
            case "m/h":
                self.viteza_de_propagare = self.viteza_de_propagare / 3600
            case "dam/h":
                self.viteza_de_propagare *= 10 / 3600
            case "hm/h":
                self.viteza_de_propagare *= 10 ** 2 / 3600
            case "km/h":
                self.viteza_de_propagare *= 10 ** 3 / 3600
            case _:
                self.unitate_de_masura_a_vitezei.lower()

    def transformarea_distantei(self):
        match self.unitate_de_masura_a_distantei:
            case "mm":
                self.distanta *= 10 ** (-3)
            case "cm":
                self.distanta *= 10 ** (-2)
            case "dm":
                self.distanta *= 10 ** (-1)
            case "m":
                self.distanta = self.distanta
            case "dam":
                self.distanta *= 10
            case "hm":
                self.distanta *= 10 ** 2
            case "km":
                self.distanta *= 10 ** 3
            case _:
                self.unitate_de_masura_a_distantei.lower()

    def transformarea_vitezei_internetului(self):
        match self.unitatea_de_masura_a_vitezei_internetului:
            case "Kbps":
                self.viteza_internet *= 10**3
            case "Mbps":
                self.viteza_internet *= 10**6
            case "Gbps":
                self.viteza_internet *= 10**9
            case "Tbps":
                self.viteza_internet *= 10**12
            case "Pbps":
                self.viteza_internet *= 10**15
            case _:
                self._viteza_internet = self.viteza_internet

    def determinarea_intarzierii_de_propagare(self):
        self.intarzierea_de_propagare = self.distanta / self.viteza_de_propagare

    def determinarea_intarzierii_de_transmisie(self):
        self.intarzierea_de_transmisie = self.marimea_fisierului / self.viteza_internet

    def determinarea_latentei(self):
        self.latenta = self.intarzierea_de_propagare + self.intarzierea_de_transmisie
        self.latenta_formatata = f"{int(self.latenta / 60)} min {((self.latenta / 60) - int(self.latenta / 60)) * 60} s"


x = Latenta(30.0*10**6, 200000.0, "km/s", 5000.0, "km", 64.0, "kbps")
print(x)
