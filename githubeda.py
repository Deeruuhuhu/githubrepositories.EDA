
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\HP\Downloads\github_top_repositories.csv")   # change file name if needed

print("\nFirst 5 Rows:\n", df.head())
print("\nlast five rows:\n ",df.tail())
print("\nShape:", df.shape)
print("\nInfo:\n")
print(df.info())
print("\nSummary:\n", df.describe())

print("\nMissing Values:\n", df.isnull().sum())


df.fillna(0, inplace=True)

print("\nMissing Values:\n", df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("\nDuplicates:", df.duplicated().sum())
df['Primary Language'] = df['Primary Language'].fillna("Unknown").astype(str)
top_languages = df['Primary Language'].value_counts().head(10)

print(top_languages)

plt.bar(top_languages.index,top_languages.values)
plt.title("Top 10 Programming Languages")
plt.xlabel("Language")
plt.ylabel("Number of Repositories")
plt.show()


