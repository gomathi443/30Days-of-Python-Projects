import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Load CSV
file_path = r"C:\Users\TmC\Downloads\archive\2018-2019_Daily_Attendance_20240429.csv"
df = pd.read_csv(file_path)
# Step 2: Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d', errors='coerce')
df.dropna(subset=['Date'], inplace=True)
# Step 3: Filter for a specific school (change this if needed)
school_code = "01M015"
df_school = df[df["School DBN"] == school_code].copy()
# Step 4: Calculate Attendance and Absence Rates
df_school['Attendance Rate (%)'] = (df_school['Present'] / df_school['Enrolled']) * 100
df_school['Absence Rate (%)'] = (df_school['Absent'] / df_school['Enrolled']) * 100
# 📈 Plot 1: Daily Attendance Rate
plt.figure(figsize=(12, 5))
plt.plot(df_school['Date'], df_school['Attendance Rate (%)'], color='blue', marker='o')
plt.title(f"📈 Daily Attendance Rate - {school_code}")
plt.xlabel("Date")
plt.ylabel("Attendance Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
# 📊 Plot 2: Present vs Absent (First 30 Days Only)
df_plot = df_school.head(30)
plt.figure(figsize=(14, 6))
plt.bar(df_plot['Date'], df_plot['Present'], label='Present', color='green')
plt.bar(df_plot['Date'], df_plot['Absent'], label='Absent', color='red', bottom=df_plot['Present'])
plt.title(f" Present vs  Absent - First 30 Days - {school_code}")
plt.xlabel("Date")
plt.ylabel("Number of Students")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# 📉 Plot 3: 7-Day Rolling Average Attendance Rate
df_school['7-Day Avg'] = df_school['Attendance Rate (%)'].rolling(window=7).mean()
plt.figure(figsize=(12, 5))
plt.plot(df_school['Date'], df_school['7-Day Avg'], color='orange')
plt.title(f" 7-Day Rolling Avg Attendance - {school_code}")
plt.xlabel("Date")
plt.ylabel("Rolling Avg Attendance (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
# 📆 Plot 4: Monthly Average Attendance Rate
df_school['Month'] = df_school['Date'].dt.to_period('M')
monthly_avg = df_school.groupby('Month')['Attendance Rate (%)'].mean().reset_index()
