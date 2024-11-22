import streamlit as st
def Gen_Eff(V, CL, IL, K, Rsh, Ra):

    # Calculate shunt field current
    Ish = V / Rsh
    
    # Calculate armature current
    Ia = K * IL - Ish
    
    # Calculate copper losses
    CUL = (Ish*2) * Rsh + (Ia*2) * Ra
    
    # Calculate efficiency
    Eff = (K * V * IL) / (K * V * IL + CL/1000 + CUL) * 100
    
    return Eff, CUL

# Streamlit App
st.title("DC Shunt Generator Efficiency Calculator")

# User Inputs
st.header("Input Parameters")
V = st.number_input("Voltage (V)", min_value=0.0, value=220.0, step=10.0)
CL = st.number_input("Core Losses (CL) in kilowatts", min_value=0.0, value=200.0, step=10.0)
IL = st.number_input("Full Load Current (IL) in Amps", min_value=0.0, value=50.0, step=1.0)
K = st.number_input("Loading on Generator (K)", min_value=0.0, value=1.0, step=0.1)
Rsh = st.number_input("Shunt Field Resistance (Rsh) in ohms", min_value=0.0, value=50.0, step=1.0)
Ra = st.number_input("Armature Resistance (Ra) in ohms", min_value=0.0, value=0.5, step=0.1)

# Calculate Efficiency and Copper Losses
if st.button("Calculate"):
    efficiency, copper_losses = Gen_Eff(V, CL, IL, K, Rsh, Ra)
    st.success(f"Efficiency: {efficiency:.2f}%")
    st.info(f"Copper Losses (CUL): {copper_losses:.2f} W")