#   Zona de importuri
import sys


class Schelet:
    lista_cu_diferitele_componente_adecvate = ["CD", "DVD", "Blu-Rays", "HDD", "SSD", "Stick"]

    def __init__(self, spatiul_produs_anual: float, unitatea_de_masura_a_spatiului_produs_anual: str,
                 lista_componente: list):
        self.spatiul_produs_anual = spatiul_produs_anual
        self.unitatea_de_masura_a_spatiului_produs_anual = unitatea_de_masura_a_spatiului_produs_anual
        self.lista_componente = lista_componente
        self.toate_componentele = {}
        self.toate_componentele_formatate = {}
        self.spatiu_produs_anual_formatat = spatiul_produs_anual
        self.unitatea_de_masura_a_spatiului_produs_anual_formatat = unitatea_de_masura_a_spatiului_produs_anual

        self.citirea_componentelor_si_spatiul_acestora()
        self.transformarea_um_in_bytes()
        self.transformare_grosimii_in_mm()
        self.transformarea_spatiului_anual()

        print(self.toate_componentele_formatate)

        #   Zona de Gettere

    @property
    def spatiul_produs_anual(self):
        return self._spatiul_produs_anual

    @property
    def unitatea_de_masura_a_spatiului_produs_anual(self):
        return self._unitatea_de_masura_a_spatiului_produs_anual

    @property
    def lista_componente(self):
        return self._lista_componente

    @property
    def toate_componentele(self):
        return self._toate_componentele

    @property
    def toate_componentele_formatate(self):
        return self._toate_componentele_formatate

    @property
    def spatiu_produs_anual_formatat(self):
        return self._spatiu_produs_anual_formatat

    @property
    def unitatea_de_masura_a_spatiului_produs_anual_formatat(self):
        return self._unitatea_de_masura_a_spatiului_produs_anual_formatat

    #   Zona de Settere

    @spatiul_produs_anual.setter
    def spatiul_produs_anual(self, val):
        assert isinstance(val, float), (f"Spatiul produs anual \"{val}\" nu este de tip float! "
                                        f"Va rugam sa introducti o valoare valida!")
        self._spatiul_produs_anual = val

    @unitatea_de_masura_a_spatiului_produs_anual.setter
    def unitatea_de_masura_a_spatiului_produs_anual(self, val):
        assert isinstance(val, str), (f"Unitatea de masura a spatiului de stocare produs anual \"{val}\" nu "
                                      f"este de tip str! Va rugam sa introduceti o valoare valida!")
        self._unitatea_de_masura_a_spatiului_produs_anual = val

    @toate_componentele.setter
    def toate_componentele(self, val):
        self._toate_componentele = val

    @toate_componentele_formatate.setter
    def toate_componentele_formatate(self, val):
        self._toate_componentele_formatate = val

    @spatiu_produs_anual_formatat.setter
    def spatiu_produs_anual_formatat(self, val):
        self._spatiu_produs_anual_formatat = val

    @unitatea_de_masura_a_spatiului_produs_anual_formatat.setter
    def unitatea_de_masura_a_spatiului_produs_anual_formatat(self, val):
        self._unitatea_de_masura_a_spatiului_produs_anual_formatat = val

    @lista_componente.setter
    def lista_componente(self, val):
        assert isinstance(val, list), (f"Lista care contine componenta \"{val}\"ar trebui sa fie de tip list, dar "
                                       f"in cazul dvs. este de tip {type(val)}! Va rugam sa introduceti valori valide!")
        """Verificare tuturor datelor din lista introdusa 
        (fiecare valoarea trebuie sa fie precum componentele definite in clasa); 
        Atributul clasei: lista_cu_diferitele_componente_adecvate"""
        val_adevar = False
        for componenta in val:
            for componenta_adecvata in Schelet.lista_cu_diferitele_componente_adecvate:
                if componenta == componenta_adecvata:
                    val_adevar = True
            if not val_adevar:
                print(f"O componenta definita de dvs. \"{componenta}\" nu corespunde cerintelor!")
                sys.exit()
        self._lista_componente = val

    def __repr__(self):
        text_afisat = f"""Attention: Calculate the solutions for both options:
{self.spatiul_produs_anual} {self.unitatea_de_masura_a_spatiului_produs_anual} = {self.spatiul_produs_anual} * 10^15 Bytes <= this way, the hardware manufacture calculate
{self.spatiul_produs_anual} {self.unitatea_de_masura_a_spatiului_produs_anual} = {self.spatiul_produs_anual} * 2^50 Bytes <= this way, the operating system calculate
"""
        idx = 0
        for valoare in self.toate_componentele_formatate.values():
            text_afisat += f"""Solutions for {self.lista_componente[idx]} with {self.spatiul_produs_anual} {self.unitatea_de_masura_a_spatiului_produs_anual}:
                                                    {self.spatiul_produs_anual}
            Number of {self.lista_componente[idx]}s:            ----------------------------------- = {self.spatiul_produs_anual / valoare[0]['SpatiuDeStocare']}
                                                {valoare[0]['SpatiuDeStocare']}
            {self.lista_componente[idx]} stack height:          {self.spatiul_produs_anual / valoare[0]['SpatiuDeStocare']} * {valoare[2]['Grosime']} = {(self.spatiul_produs_anual / valoare[0]['SpatiuDeStocare']) * (valoare[2]['Grosime'])} m 


Solutions for {self.lista_componente[idx]} with {self.spatiu_produs_anual_formatat} {self.unitatea_de_masura_a_spatiului_produs_anual_formatat}:
                                                    {self.spatiu_produs_anual_formatat}
            Number of {self.lista_componente[idx]}s:            ----------------------------------- = {self.spatiu_produs_anual_formatat / valoare[0]['SpatiuDeStocare']}
                                                {valoare[0]['SpatiuDeStocare']}
            {self.lista_componente[idx]} stack height:          {self.spatiu_produs_anual_formatat / valoare[0]['SpatiuDeStocare']} * {valoare[2]['Grosime']} = {(self.spatiu_produs_anual_formatat / valoare[0]['SpatiuDeStocare']) * (valoare[2]['Grosime'])} m 



"""
            idx += 1
        return text_afisat

    def citirea_componentelor_si_spatiul_acestora(self):

        for componenta in self.lista_componente:
            spatiul_de_stocare_al_fiecarei_componente = {}
            unitatea_de_masura_a_fiecarei_componente = {}
            grosimea_fiecarei_componente = {}
            unitatea_de_masura_a_grosimii_fiecarei_componente = {}
            lista_cu_date = []

            spatiu = float(input(f"Spatiul de stocare al componentei \"{componenta}\": "))
            spatiul_de_stocare_al_fiecarei_componente.update({"SpatiuDeStocare": spatiu})
            unitatea_de_masura_a_componentei = input(f"Unitatea de masura a componentei \"{componenta}\": ")
            unitatea_de_masura_a_fiecarei_componente.update({"UM_SpatiuDeStocare": unitatea_de_masura_a_componentei.upper()})
            grosime = float(input(f"Grosimea componentei \"{componenta}\": "))
            grosimea_fiecarei_componente.update({"Grosime": grosime})
            unitatea_de_masura_a_grosimii_componentei = input(f"Unitatea de masura a grosimii componentei "
                                                              f"\"{componenta}\": ")
            unitatea_de_masura_a_grosimii_fiecarei_componente.update(
                {"UM_Grosime": unitatea_de_masura_a_grosimii_componentei.lower()})

            lista_cu_date.append(spatiul_de_stocare_al_fiecarei_componente)
            lista_cu_date.append(unitatea_de_masura_a_fiecarei_componente)
            lista_cu_date.append(grosimea_fiecarei_componente)
            lista_cu_date.append(unitatea_de_masura_a_grosimii_fiecarei_componente)

            self.toate_componentele.update({str(componenta): lista_cu_date})
            self.toate_componentele_formatate = self.toate_componentele
            print('\n')

    def transformarea_um_in_bytes(self):
        #   Citirea valorilor din dictionar
        for valoare in self.toate_componentele_formatate.values():
            match valoare[1]["UM_SpatiuDeStocare"]:
                case "MB":
                    valoare[0]["SpatiuDeStocare"] *= 10**6
                    valoare[1]["UM_SpatiuDeStocare"] = "Byte"
                case "GB":
                    valoare[0]["SpatiuDeStocare"] *= 10**9
                    valoare[1]["UM_SpatiuDeStocare"] = "Byte"
                case "TB":
                    valoare[0]["SpatiuDeStocare"] *= 10**12
                    valoare[1]["UM_SpatiuDeStocare"] = "Byte"
                case "PB":
                    valoare[0]["SpatiuDeStocare"] *= 10**15
                    valoare[1]["UM_SpatiuDeStocare"] = "Byte"

    def transformare_grosimii_in_mm(self):
        #   Citirea valorilor din dictionar
        for valoare in self.toate_componentele_formatate.values():
            match valoare[3]["UM_Grosime"]:
                case "mm":
                    valoare[2]["Grosime"] *= 10**(-3)
                    valoare[3]["UM_Grosime"] = "m"
                case "cm":
                    valoare[2]["Grosime"] *= 10**(-2)
                    valoare[3]["UM_Grosime"] = "m"
                case "dm":
                    valoare[2]["Grosime"] *= 10**(-1)
                    valoare[3]["UM_Grosime"] = "mm"
                case "dam":
                    valoare[2]["Grosime"] *= 10 ** 1
                    valoare[3]["UM_Grosime"] = "m"
                case "hm":
                    valoare[2]["Grosime"] *= 10 ** 2
                    valoare[3]["UM_Grosime"] = "m"
                case "km":
                    valoare[2]["Grosime"] *= 10 ** 3
                    valoare[3]["UM_Grosime"] = "m"

    def transformarea_spatiului_anual(self):
        match self.unitatea_de_masura_a_spatiului_produs_anual:
            case "KB":
                self.spatiul_produs_anual *= 10**3
                self.spatiu_produs_anual_formatat *= 2**10
                self.unitatea_de_masura_a_spatiului_produs_anual = "Byte"
                self.unitatea_de_masura_a_spatiului_produs_anual_formatat = "Byte"
            case "MB":
                self.spatiul_produs_anual *= 10**6
                self.spatiu_produs_anual_formatat *= 2**20
                self.unitatea_de_masura_a_spatiului_produs_anual = "Byte"
                self.unitatea_de_masura_a_spatiului_produs_anual_formatat = "Byte"
            case "GB":
                self.spatiul_produs_anual *= 10**9
                self.spatiu_produs_anual_formatat *= 2**30
                self.unitatea_de_masura_a_spatiului_produs_anual = "Byte"
                self.unitatea_de_masura_a_spatiului_produs_anual_formatat = "Byte"
            case "TB":
                self.spatiul_produs_anual *= 10**12
                self.spatiu_produs_anual_formatat *= 2**40
                self.unitatea_de_masura_a_spatiului_produs_anual = "Byte"
                self.unitatea_de_masura_a_spatiului_produs_anual_formatat = "Byte"
            case "PB":
                self.spatiul_produs_anual *= 10**15
                self.spatiu_produs_anual_formatat *= 2**50
                self.unitatea_de_masura_a_spatiului_produs_anual = "Byte"
                self.unitatea_de_masura_a_spatiului_produs_anual_formatat = "Byte"
