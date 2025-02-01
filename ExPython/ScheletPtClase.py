class Schelet:
    def __init__(self, viteza_de_internet: float, unitatea_de_masura_a_vitezei_de_internet: str,
                 distanta: float, unitatea_de_masura_a_distantei: str,
                 viteza_de_propagare: float, unitatea_de_masura_a_vitezei_de_propagare: str,
                 dimensiunea_fisierului: float, unitatea_de_masura_a_dimensiunii_fisierului: str):

        self.viteza_de_internet = viteza_de_internet
        self.unitatea_de_masura_a_vitezei_de_internet = unitatea_de_masura_a_vitezei_de_internet
        self.distanta = distanta
        self.unitatea_de_masura_a_distantei = unitatea_de_masura_a_distantei
        self.viteza_de_propagare = viteza_de_propagare
        self.unitatea_de_masura_a_vitezei_de_propagare = unitatea_de_masura_a_vitezei_de_propagare
        self.dimensiunea_fisierului = dimensiunea_fisierului
        self.unitatea_de_masura_a_dimensiunii_fisierului = unitatea_de_masura_a_dimensiunii_fisierului
        self.intarzierea_de_propagare = None
        self.nr_de_biti = None
        self.intarzierea_de_transmisie = None
        self.nr_de_bytes_ai_fisierului = None
        self.nr_de_biti_ai_fisierului = None
        self.latenta = None
        self.latenta_formatata = None

        self.transformarea_vitezei()
        self.transformarea_distantei()
        self.transformarea_vitezei_internetului()

        self.determinarea_intarzierii_de_propagare()
        self.determinarea_nr_de_biti()
        self.determinare_nr_de_biti_ai_fisierului()
        self.determinarea_intarzierii_de_transmisie()
        self.determinarea_latentei()

    #   Zona de Gettere

    @property
    def viteza_de_internet(self):
        return self._viteza_de_internet

    @property
    def unitatea_de_masura_a_vitezei_de_internet(self):
        return self._unitatea_de_masura_a_vitezei_de_internet

    @property
    def distanta(self):
        return self._distanta

    @property
    def unitatea_de_masura_a_distantei(self):
        return self._unitatea_de_masura_a_distantei

    @property
    def viteza_de_propagare(self):
        return self._viteza_de_propagare

    @property
    def unitatea_de_masura_a_vitezei_de_propagare(self):
        return self._unitatea_de_masura_a_vitezei_de_propagare

    @property
    def nr_de_biti(self):
        return self._nr_de_biti

    @property
    def intarzierea_de_transmisie(self):
        return self._intarzierea_de_transmisie

    @property
    def dimensiunea_fisierului(self):
        return self._dimensiunea_fisierului

    @property
    def unitatea_de_masura_a_dimensiunii_fisierului(self):
        return self._unitatea_de_masura_a_dimensiunii_fisierului

    @property
    def nr_de_bytes_ai_fisierului(self):
        return self._nr_de_bytes_ai_fisierului

    @property
    def nr_de_biti_ai_fisierului(self):
        return self._nr_de_biti_ai_fisierului

    @property
    def latenta(self):
        return self._latenta

    @property
    def latenta_formatata(self):
        return self._latenta_formatata

    #   Zona de Settere

    @viteza_de_internet.setter
    def viteza_de_internet(self, val):
        assert isinstance(val, float), (f"Viteza de internet \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._viteza_de_internet = val

    @unitatea_de_masura_a_vitezei_de_internet.setter
    def unitatea_de_masura_a_vitezei_de_internet(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a vitezei internetului \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitatea_de_masura_a_vitezei_de_internet = val.capitalize()

    @distanta.setter
    def distanta(self, val):
        assert isinstance(val, float), (f"Distanta \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._distanta = val

    @unitatea_de_masura_a_distantei.setter
    def unitatea_de_masura_a_distantei(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a distantei \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitatea_de_masura_a_distantei = val.lower()

    @viteza_de_propagare.setter
    def viteza_de_propagare(self, val):
        assert isinstance(val, float), (f"Viteza de propagare \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._viteza_de_propagare = val

    @unitatea_de_masura_a_vitezei_de_propagare.setter
    def unitatea_de_masura_a_vitezei_de_propagare(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a vitezei de propagare \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitatea_de_masura_a_vitezei_de_propagare = val.capitalize()

    @nr_de_biti.setter
    def nr_de_biti(self, val):
        self._nr_de_biti = val

    @intarzierea_de_transmisie.setter
    def intarzierea_de_transmisie(self, val):
        self._intarzierea_de_transmisie = val

    @dimensiunea_fisierului.setter
    def dimensiunea_fisierului(self, val):
        assert isinstance(val, float), (f"Dimensiunea imaginii \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introduceti o data valida!")
        self._dimensiunea_fisierului = val

    @unitatea_de_masura_a_dimensiunii_fisierului.setter
    def unitatea_de_masura_a_dimensiunii_fisierului(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a dimensiunii imaginii \"{val}\" nu este de tip str! "
                                      f"Va rugam sa introduceti o data valida!")
        self._unitatea_de_masura_a_dimensiunii_fisierului = val

    @nr_de_bytes_ai_fisierului.setter
    def nr_de_bytes_ai_fisierului(self, val):
        self._nr_de_bytes_ai_fisierului = val

    @nr_de_biti_ai_fisierului.setter
    def nr_de_biti_ai_fisierului(self, val):
        self._nr_de_biti_ai_fisierului = val

    @latenta.setter
    def latenta(self, val):
        self._latenta = val

    @latenta_formatata.setter
    def latenta_formatata(self, val):
        self._latenta_formatata = val

    def transformarea_vitezei(self):
        match self.unitatea_de_masura_a_vitezei_de_propagare:
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
                pass

    def transformarea_distantei(self):
        match self.unitatea_de_masura_a_distantei:
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
                pass

    def transformarea_vitezei_internetului(self):
        match self.unitatea_de_masura_a_vitezei_de_internet:
            case "Kbps":
                self.viteza_de_internet *= 10**3
            case "Mbps":
                self.viteza_de_internet *= 10**6
            case "Gbps":
                self.viteza_de_internet *= 10**9
            case "Tbps":
                self.viteza_de_internet *= 10**12
            case "Pbps":
                self.viteza_de_internet *= 10**15
            case _:
                pass

    def determinarea_intarzierii_de_propagare(self):
        self.intarzierea_de_propagare = self.distanta / self.viteza_de_propagare

    def determinarea_nr_de_biti(self):
        self.nr_de_biti = self.intarzierea_de_propagare * self.viteza_de_internet

    def determinarea_intarzierii_de_transmisie(self):
        self.intarzierea_de_transmisie = self.nr_de_biti_ai_fisierului / self.viteza_de_internet

    def determinare_nr_de_biti_ai_fisierului(self):
        self.nr_de_bytes_ai_fisierului = self.dimensiunea_fisierului * 2**20
        self.nr_de_biti_ai_fisierului = self.nr_de_bytes_ai_fisierului * 8

    def determinarea_latentei(self):
        self.latenta = self.intarzierea_de_propagare + self.intarzierea_de_transmisie
        self.latenta_formatata = f"{int(self.latenta / 60)} min {((self.latenta / 60) - int(self.latenta / 60)) * 60} s"
