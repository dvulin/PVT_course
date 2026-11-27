# pvtfunctions/real_gas.py

class RealGas:
  """Jednostavni proračuni iz jednadžbe stanja realnog plina: p * V = Z * n * R * T."""

  R = 8.314462618  # J / (mol * K)

  @staticmethod
  def pressure(V, Z = 1.0, n = 1.0, T = 288.15) -> float:
    """Tlak p [Pa] iz V [m3], Z [-], n [mol] i T [K]."""
    return (Z * n * RealGas.R * T) / V
    
  @staticmethod
  def density(p, molar_mass_kg_mol, Z = 1.0, T = 288.15) -> float:
    """Gustoća rho [kg/m3] iz p [Pa], molarne mase M [kg/mol], Z [-] i T [K]."""
    return (p * molar_mass_kg_mol) / (Z * RealGas.R * T)