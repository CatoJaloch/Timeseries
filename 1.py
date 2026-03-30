import pandas as pd
#read csv
df = pd.read_csv('sian_variety.csv')
# listing the  week numbers available for use
week_numbers = df['week_number'].unique()
print("Available week numbers Sian:", week_numbers)
#Available week numbers: [45 46 47 48 49 50 51 52  1  2  3  4  5  6  7  8  9 10 11]

#read csv
df = pd.read_csv('gtf_variety.csv')
# listing the  week numbers available for use
week_numbers = df['week_number'].unique()
print("Available week numbers GTF:", week_numbers)
#Available week numbers GTF: [45 46 47 48 49 50 51 52  1  2  3  4  5  6  7  8  9 10 11]

#checking for null values in both datasets
files = ["sian_variety.csv", "gtf_variety.csv"]

for file in files:
    df = pd.read_csv(file)
    print(f"\n{file} null values per column:\n", df.isnull().sum())
    #drop rows where field_harvest is 0
    df.drop(df[df["field_harvests"]== 0].index, inplace=True)
    print('dropped rows where field_harvests is 0')
