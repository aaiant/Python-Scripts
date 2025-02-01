#   Zona de importuri
from ScheletPtClase2 import Schelet


class StocareaSiTrimitereaDatelor(Schelet):
    def __init__(self, spatiul_produs_anual: float, unitatea_de_masura_a_spatiului_produs_anual: str,
                 lista_componente: list):
        super().__init__(spatiul_produs_anual, unitatea_de_masura_a_spatiului_produs_anual, lista_componente)


x = StocareaSiTrimitereaDatelor(15.0, "PB", ["DVD", "CD"])
print(x)
