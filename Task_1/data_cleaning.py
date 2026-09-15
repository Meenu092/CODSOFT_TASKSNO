import pandas as pd

df = pd.read_csv("dataset.csv")

print(df)
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nDuplicate Rows:")
print(df[df.duplicated()])

print("\nGender Values:")
print(df["Gender"].unique())

print("\nDepartment Values:")
print(df["Department"].unique())

df = df.drop_duplicates()

print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "M": "Male",
    "female": "Female",
    "F": "Female"
})

df["Department"] = df["Department"].str.strip().str.title()
df["Department"] = df["Department"].replace({
    "It": "IT",
    "Hr": "HR"
})
print("\nGender After Cleaning:")
print(df["Gender"].unique())

print("\nDepartment After Cleaning:")
print(df["Department"].unique())

print("\nData Types Before Cleaning:")
print(df.dtypes)

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

print("\nData Types After Cleaning:")
print(df.dtypes)

print("\nMissing Salary After Conversion:")
print(df["Salary"].isnull().sum())

print("\n--- FINAL CHECK ---")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Cleaned Rows:")
print(df.head())

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")