# Definirea clasei pentru rata de date

# Zona de clase


class RataDate:
    def __init__(self, nr_biti: int, nr_secunde: float):
        self._nr_biti = nr_biti
        self._nr_secunde = nr_secunde
        self._rezultat_rata_date = nr_biti / self.nr_secunde

    def __repr__(self):
        return f"Rata de date este: {self.rezultat_rata_date} Biti/s."

    #   Zona de Gettere
    @property
    def nr_biti(self):
        return self._nr_biti

    @property
    def nr_secunde(self):
        return self._nr_secunde

    @property
    def rezultat_rata_date(self):
        return self._rezultat_rata_date

    #   Zona de Settere
    @nr_biti.setter
    def nr_biti(self, val):
        assert isinstance(val, int), \
            f"Nr. de biti \"{val}\" nu este de tip int! Va rugam sa incercati din nou cu o valoarea valida!"
        self._nr_biti = val

    @nr_secunde.setter
    def nr_secunde(self, val):
        assert isinstance(val, int), \
            f"Nr. de secunde \"{val}\" nu este de tip float! Va rugam sa incercati din nou cu o valoare valida!"
        assert val > 0, (f"Nr. secunde \"{val}\" trebuie sa fie mai mare decat 0! "
                         f"Va rugam sa incercati din nou cu o valoarea valida!")
        self._nr_secunde = val

    @rezultat_rata_date.setter
    def rezultat_rata_date(self, val):
        self._rezultat_rata_date = val

    def informatii(self):
        print(f"Rata de date este numarul de biti transmisi pe "
              f"secunda dupa o adjustare a bratelor telegrafului cu {self.nr_secunde} secunde.")


x = RataDate(12, 10)
print(x)
