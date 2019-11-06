import datetime
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

current_datetime = datetime.datetime.now().strftime("%Y-%m-%d")
current_datetime = str(current_datetime)

print("The current datetime is {}".format(current_datetime))

input_location = '\\\\la-data.data.alpha.jisc.ac.uk\\la-data\\rossuni\\activity\\live\\validation\\'
vle_file = 'vleview.tsv'
attendance_file = 'attendance.tsv'
output_location = '\\\\la-data.data.alpha.jisc.ac.uk\\la-data\\rossuni\\activity\\live\\daily-update\\'

# Creating a dataframe object from report list
df_vle_file = pd.read_csv(input_location + vle_file, sep='\t')
df_attendance_file = pd.read_csv(input_location + attendance_file, sep='\t')

# Create new column of dates (without times)
df_vle_file['filter'] = df_vle_file['TIMESTAMP'].str[:10]
df_attendance_file['filter'] = df_attendance_file['TIMESTAMP'].str[:10]

# Filter dataframes where timestamp is today
df_vle_istoday = df_vle_file.loc[df_vle_file['filter'] == current_datetime]
df_attendance_istoday = df_attendance_file.loc[df_attendance_file['filter'] == current_datetime]

# Drop unnecessary columns
df_vle_istoday = df_vle_istoday.drop(columns=['filter'])
df_attendance_istoday = df_attendance_istoday.drop(columns=['filter'])

print(df_vle_istoday)
print(df_attendance_istoday)

df_vle_istoday.to_csv(output_location + vle_file, sep='\t', index=False, encoding='utf-8',
                     header=True)

df_attendance_istoday.to_csv(output_location + attendance_file, sep='\t', index=False, encoding='utf-8',
                     header=True)