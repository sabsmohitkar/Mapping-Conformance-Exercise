#!/usr/bin/env python
# coding: utf-8

# In[23]:


# main.py

import os
import sys
import pandas as pd

# Check Python version
print("Python version used: ", sys.version)

# Check if input directory is provided as command line argument
if len(sys.argv) < 2:
    print("Please provide the absolute path to the directory containing input_data as command line argument.")
    sys.exit(1)

input_dir = sys.argv[1]

# Load input datasets
input1_path = os.path.join(input_dir,r"C:\Users\91997\ecg1.csv")
input2_path = os.path.join(input_dir,r"C:\Users\91997\ecg2.csv")
input3_path = os.path.join(input_dir,r"C:\Users\91997\ecg3.csv")

df_input1 = pd.read_csv(input1_path)
df_input2 = pd.read_csv(input2_path)
df_input3 = pd.read_csv(input3_path)

# Perform mapping conformance exercise
# Extrapolate the relationship between input and output data

df_input1 = pd.read_csv(input1_path).replace('.', '').fillna('#')
df_input2 = pd.read_csv(input2_path).replace('.', '').fillna('#')
df_input3 = pd.read_csv(input3_path).replace('.', '').fillna('#')

# Sort input datasets by index
df_input1 = df_input1.sort_index()
df_input2 = df_input2.sort_index()
df_input3 = df_input3.sort_index()
# the relationship is a simple concatenation of input datasets
df_output = pd.concat([df_input1, df_input2, df_input3], axis=1)

# Write result to output file
output_dir = r"C:\Users\Public" 
output_path = os.path.join(output_dir, "result.csv")
df_output.to_csv(output_path, index=False)
print("Conversion completed. Output saved to:", output_path)


# In[ ]:




