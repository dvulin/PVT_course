# -*- coding: utf-8 -*-
"""
25.11.2026. Uvod u PVT

pV = nRT
n = m/M
p*M = rho*R*T

"""
import CoolProp.CoolProp as CP
import pandas as pd
from pvtfunctions import RealGas

M_air = CP.Props1SI("M", "Air")*1000   # gmol
m = 1000            # g
n = m/M_air
T = 15.6 + 273.15
V = 0.001
p = RealGas.pressure(V=V, Z=1, n=n, T=T)/1e5
rho_kg_m3 = RealGas.density(p=200e5, molar_mass_kg_mol=0.01604, Z=0.88, T=288.75)

print(f"Tlak: {p:.5f} bar")
print(f"Gustoća: {rho_kg_m3:.4f} kg/m^3")
