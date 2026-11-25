# -*- coding: utf-8 -*-
"""
25.11.2026. Uvod u PVT

pV = nRT
n = m/M
p*M = rho*R*T

"""
import CoolProp.CoolProp as CP
fluid = "Water"
#M = 28.97                   # g/mol    | molarna masa zraka
M = 18.015                  # g/mol     | molarna masa vode
p = 101325                  # Pa        | tlak sustava
T = 15.6+273.15             # K         | temperatura sustava
R = 8.31446261815324        # J⋅mol⁻¹K⁻¹| opća plinska konstanta
rho = p*M/(R*T)

Q = CP.PropsSI('T','P',101325,'Q',0, fluid)
M_kg_mol = CP.PropsSI("molar_mass", fluid)
M = M_kg_mol*1000