import pandas as pd
df=pd.read_csv("avg.csv")
# Assuming your data is in a pandas DataFrame named df with columns 'ecg' and 'class'
# Filter rows where class is 1 and sum the corresponding ECG values
sum_normal_ecg = df[df['class'] == 1]['ecg'].sum()

# Count the number of ECG values classified as 1
count_normal_ecg = len(df[df['class'] == 1])

# Calculate the average normal ECG value
if count_normal_ecg > 0:
    average_normal_ecg = sum_normal_ecg / count_normal_ecg
    print("Average of normal ECG values:", average_normal_ecg)
else:
    print("No normal ECG values found in the data.")
