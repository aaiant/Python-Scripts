#   Zona de import
from ScheletPtClase import Schelet


class ProdusCuIntarziereALatimiiDeBanda(Schelet):
    def __init__(self, viteza_de_internet: float, unitatea_de_masura_a_vitezei_de_internet: str,
                 distanta: float, unitatea_de_masura_a_distantei: str,
                 viteza_de_propagare: float, unitatea_de_masura_a_vitezei_de_propagare: str,
                 dimensiunea_fisierului: float, unitatea_de_masura_a_dimensiunii_fisierului: str):
        super().__init__(viteza_de_internet, unitatea_de_masura_a_vitezei_de_internet,
                         distanta, unitatea_de_masura_a_distantei, viteza_de_propagare,
                         unitatea_de_masura_a_vitezei_de_propagare, dimensiunea_fisierului,
                         unitatea_de_masura_a_dimensiunii_fisierului)
        self.round_trip_time_rtt = None
        self.round_trip_time_rtt = None
        self.determinarea_rtt_ului()

    #   Zona de Gettere

    @property
    def round_trip_time_rtt(self):
        return self._round_trip_time_rtt

    #   Zona de Settere

    @round_trip_time_rtt.setter
    def round_trip_time_rtt(self, val):
        self._round_trip_time_rtt = val

    def __repr__(self):
        return f"""1)
RTT = (2 * distance) / propagation speed

RTT = (2 * distance) / propagation speed
RTT = (2 * {self.distanta} m) / {self.viteza_de_propagare} m / s
RRT = {2 * self.distanta} m / {self.viteza_de_propagare} m / s
RTT = {self.round_trip_time_rtt} s

2)
Signal propagation speed  = {self.viteza_de_propagare}m / s
Distance = {self.distanta}m 
Transmission delay = 0 s
Waiting time = 0 s
                            {self.distanta} m
Propagation delay =  ----------------------------- = {self.intarzierea_de_propagare} s 
                            {self.viteza_de_propagare} m / s
                            
        {self.viteza_de_internet} Bits/s * {self.intarzierea_de_propagare} s = {self.nr_de_biti} Bits
                                            = {self.nr_de_biti / 10**3} MBits
                                            
3)

File size: {self.dimensiunea_fisierului} {self.unitatea_de_masura_a_dimensiunii_fisierului} = {self.nr_de_bytes_ai_fisierului} Bytes = {self.nr_de_biti_ai_fisierului} Bits
Data rate: {self.viteza_de_internet} Bits/s
Propagation delay =  {self.distanta} m / {self.viteza_de_propagare} m / s
                  = {self.intarzierea_de_propagare} s 
Transmission delay = {self.nr_de_biti_ai_fisierului} Bits / {self.viteza_de_internet} Bits/s
                   = {self.intarzierea_de_transmisie} s 
Witing time = 0 s
Latency = propagation delay + transmission delay + waiting time
        = {self.intarzierea_de_propagare} s + {self.intarzierea_de_transmisie} s
        = {self.latenta} s
        = {self.latenta_formatata}
"""

    def determinarea_rtt_ului(self):
        self.round_trip_time_rtt = (2 * self.distanta) / self.viteza_de_propagare


x = ProdusCuIntarziereALatimiiDeBanda(128.0, "kbps", 55000000.0,
                                      "km", 299792458.0, "m/s",
                                      20.0, "MB")
print(x)
