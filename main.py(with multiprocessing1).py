#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#main.py(with multiprocessing)

import os
import sys
import pandas as pd
import multiprocessing as mp

# Check Python version
print("Python version used: ", sys.version)

# Check if input directory is provided as command line argument
if len(sys.argv) < 2:
    print("Please provide the absolute path to the directory containing input_data as command line argument.")
    sys.exit(1)

input_dir = sys.argv[1]

# Load input datasets using multiprocessing
def load_csv(file_path):
    return pd.read_csv(file_path).replace('.', '').fillna('#')

pool = mp.Pool(processes=3)
input1_path = os.path.join(input_dir,r"C:\Users\91997\ecg1.csv")
input2_path = os.path.join(input_dir,r"C:\Users\91997\ecg2.csv")
input3_path = os.path.join(input_dir,r"C:\Users\91997\ecg3.csv")

result = pool.map(load_csv, [input1_path, input2_path, input3_path])
df_input1, df_input2, df_input3 = result

# Sort input datasets by index
df_input1 = df_input1.sort_index()
df_input2 = df_input2.sort_index()
df_input3 = df_input3.sort_index()

# Perform mapping conformance exercise
# Extrapolate the relationship between input and output data
# simple concatenation of input datasets
df_output = pd.concat([df_input1, df_input2, df_input3], axis=1)

# Write result to output file
output_path = os.path.join(input_dir, "result.csv")
df_output.to_csv(r"C:\Users\Public", index=False)

print("Conversion completed. Output saved to:",r"C:\Users")


# In[ ]:




