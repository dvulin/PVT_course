# -*- coding: utf-8 -*-
"""
25.11.2026. Uvod u PVT

pV = nRT
n = m/M
p*M = rho*R*T

"""
import CoolProp.CoolProp as CP
import pandas as pd

fluid = "Water"
#M = 28.97                   # g/mol    | molarna masa zraka
M = 18.015                  # g/mol     | molarna masa vode
p = 101325                  # Pa        | tlak sustava
T = 15.6+273.15             # K         | temperatura sustava
R = 8.31446261815324        # J⋅mol⁻¹K⁻¹| opća plinska konstanta
rho = p*M/(R*T)

Q = CP.PropsSI('T','P',101325,'Q',0, fluid)
M_kg_mol = CP.PropsSI("molar_mass", fluid)
Pc_Pa = CP.PropsSI("Pcrit", fluid)
Tc_K = CP.PropsSI("Tcrit", fluid)
omega = CP.PropsSI("acentric", fluid)
M = M_kg_mol*1000

fluid_database = {
                "i": [],            # ime komponente
                "M": [],
                "Pc": [], 
                "Tc": []
                  }

def add_component(c_name, zi=None):
    fluid_database["i"].append(c_name)
    fluid_database["M"].append(CP.PropsSI("molar_mass", c_name)*1000)
    fluid_database["Pc"].append(CP.PropsSI("Pcrit", fluid))
    fluid_database["Tc"].append(CP.PropsSI("Tcrit", fluid))
    return fluid_database


add_component("Water")
add_component("CO2")
fluid_table = pd.DataFrame(fluid_database)
