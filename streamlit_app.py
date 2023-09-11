# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 11:52:40 2023

@author: shvy
"""


import streamlit as st
import csv
import os

st.title("ASC to CSV Converter")

uploaded_file = st.file_uploader("Upload an ASCII file (ASC)", type=["asc"])

if uploaded_file is not None:
    file_name = os.path.splitext(uploaded_file.name)[0]

    
    data = []
    header = ["POINT_NR", "MEA_DEVI"]

    
    current_point_nr = None
    current_mea_devi = None


    def extract_data_from_ascii(file):
        for line in file:
            line = line.decode("utf-8").strip()  
            if line.startswith("POINT_NR :"):
                current_point_nr = line.split(":")[1].strip()
                current_mea_devi = None
            elif line.startswith("MEA_DEVI"):
                current_mea_devi = line.split(":")[1].strip()
                if current_point_nr and current_mea_devi:
                    data.append([current_point_nr, current_mea_devi])

    
    extract_data_from_ascii(uploaded_file)

    
    output_csv = f"{file_name}.csv"

    
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)  
        writer.writerows(data)   

    st.success(f'Data has been successfully extracted and saved to {output_csv}.')
