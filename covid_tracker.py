import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('covid_data.csv')
    print("Data loaded successfully.\n")
except FileNotFoundError:
    print("Error: File not found.\n")

print(df.head())

print("\nMissing values:\n", df.isnull().sum())

df.fillna(0, inplace=True)

print("\nStatistical summary:\n", df.describe())

plt.figure(figsize=(10, 5))
df['cases'].plot(kind='line', title='COVID-19 Cases Over Time')
plt.xlabel('Index')
plt.ylabel('Cases')
plt.savefig('cases_line_chart.png')
plt.close()

if 'country' in df.columns:
    df.groupby('country')['cases'].sum().nlargest(10).plot(kind='bar', title='Top 10 Countries by Cases')
    plt.ylabel('Total Cases')
    plt.tight_layout()
    plt.savefig('top_countries_bar_chart.png')
    plt.close()
