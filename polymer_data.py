
# polymer_data.py

polymer_properties = {
    "Polyaniline": {"Bandgap": 2.2, "Stability": 8.5, "Surface_Area": 120},
    "Polythiophene": {"Bandgap": 2.0, "Stability": 7.5, "Surface_Area": 115},
    "Polybenzothiadiazole": {"Bandgap": 1.8, "Stability": 9.0, "Surface_Area": 140},
    "Polypyrrole": {"Bandgap": 2.4, "Stability": 7.0, "Surface_Area": 110},
}

def get_polymer_properties(polymer_name):
    return polymer_properties.get(polymer_name, None)
