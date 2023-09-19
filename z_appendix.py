#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:56:14 2023

@author: libo
"""
import streamlit as st

st.header('主要公式：')
st.latex(r''' k\lambda = 2 \pi ''')
st.latex(r''' \nu=\frac{c}{\lambda}  ''')
st.latex(r''' \Delta\nu=\frac{c}{\lambda^2}\Delta\lambda  ''')
st.latex(r''' \omega=ck  ''')
st.latex(r''' l_c=\frac{\lambda^2}{\Delta\lambda}  ''')