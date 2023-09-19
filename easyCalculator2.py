# import the streamlit library
import streamlit as st
import math  # Import the math module for scientific calculations
import numpy as np
# the speed of light
c = 299792458

# Create a dictionary to store unit conversions (to meters)
unit_conversions = {
    'um': 1e-6,
    'nm': 1e-9,
    'pm': 1e-12,
    'kHz':1e3,
    'MHz':1e6,
    'GHz':1e9,
    'THz':1e12
}

# Give a title to our app
st.title('Optical Calculator')

st.header('Input:')
# Take the first number input and select the input unit
col1, col2 = st.columns(2)
with col1:
    cwl = st.number_input('Enter the $\lambda$')
with col2:
    cwl_unit = st.selectbox(
        'Unit',
        ('nm', 'pm')
    )

# Take the second number input and select the output unit
col3, col4 = st.columns(2)
with col3:
    delta_nv = st.number_input('Enter the $\Delta\nv$')
with col4:
    delta_nv_unit = st.selectbox(
        'Unit',
        ('kHz', 'MHz', 'GHz','THz')
    )

# Perform unit conversion
cwl = cwl * unit_conversions[cwl_unit]
delta_nv = delta_nv * unit_conversions[delta_nv_unit]

# output
st.header('Output:')
if cwl != 0:  # Check for division by zero
    nv = c/cwl/1e12 # in THz
else:
    nv = 0
        # st.error("Division by zero is not allowed")
st.markdown(f'$\nv=$ :red[{nv:.5e}] THz')

omega = nv*2*np.pi
st.markdown(f'$\omega=$ :red[{omega:.5e}] THz')

if cwl !=0:
    fwhm=delta_nv/(c/cwl/cwl)*1e9 # in nm
else: fwhm=0
st.markdown(f'$\Delta\lambda=$ :red[{fwhm:.5e}] nm')

if fwhm !=0:
    coherenceLength = cwl*cwl/(fwhm*1e-9)
else: coherenceLength = 0
st.markdown(f'$l_c=$ :red[{coherenceLength:.5e}] m')

coherenceTime = coherenceLength/c *1e9 #in ns
st.markdown(f'$l_t=$ :red[{coherenceTime:.5e}] ns')

# Convert the result to the selected output unit

