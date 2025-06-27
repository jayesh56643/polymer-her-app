
import streamlit as st
import joblib
import os

# Auto-train model if not found
if not os.path.exists("polymer_her_predictor.pkl"):
    import ml_model  # This will train and save the model

from polymer_data import get_polymer_properties

# Load trained ML model
model = joblib.load("polymer_her_predictor.pkl")

# Streamlit UI
st.title("🔬 Polymer Photocatalyst Predictor")
st.markdown("Predict hydrogen production rate based on polymer properties")

# Dropdown options
polymer_options = [
    "Polyaniline",
    "Polythiophene",
    "Polybenzothiadiazole",
    "Polypyrrole"
]

# User selection
polymer_name = st.selectbox("Choose a Polymer", polymer_options)

# Fetch properties
properties = get_polymer_properties(polymer_name)

if properties:
    st.subheader("📋 Polymer Properties (Auto-Fetched)")
    st.write(f"**Bandgap (eV):** {properties['Bandgap']}")
    st.write(f"**Stability:** {properties['Stability']}")
    st.write(f"**Surface Area:** {properties['Surface_Area']} m²/g")

    # Prepare input for model
    input_features = [[
        properties["Bandgap"],
        properties["Stability"],
        properties["Surface_Area"]
    ]]

    # Predict HER
    prediction = model.predict(input_features)[0]

    st.success(f"💧 Predicted Hydrogen Evolution Rate (HER): **{prediction:.2f} µmol/h/g**")
else:
    st.error("❌ Properties not found for the selected polymer.")
