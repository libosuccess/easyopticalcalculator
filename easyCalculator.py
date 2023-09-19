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
    'pm': 1e-12
}

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

# Give a title to our app
st.title('Optical Calculator')

st.header('Input:')
# Take the first number input and select the input unit
col1, col2 = st.columns(2)
with col1:
    cwl = st.number_input("Enter the $\lambda$")
with col2:
    cwl_unit = st.selectbox(
        'Select the input unit',
        ('nm', 'pm')
    )

# Take the second number input and select the output unit
col3, col4 = st.columns(2)
with col3:
    fwhm = st.number_input("Enter the $\Delta\lambda$")
with col4:
    fwhm_unit = st.selectbox(
        'Select the output unit',
        ('nm',  'pm')
    )

# Perform unit conversion
cwl = cwl * unit_conversions[cwl_unit]
fwhm = fwhm * unit_conversions[fwhm_unit]

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
    delta_nv=c/cwl/cwl*fwhm 
else: delta_nv=0
st.markdown(f'$\Delta\nv=$ :red[{delta_nv:.5e}] Hz')

if fwhm !=0:
    coherenceLength = cwl*cwl/fwhm
else: coherenceLength = 0
st.markdown(f'$l_c=$ :red[{coherenceLength:.5e}] m')

coherenceTime = coherenceLength/c *1e9 #in ns
st.markdown(f'$l_t=$ :red[{coherenceTime:.5e}] ns')

# Convert the result to the selected output unit
