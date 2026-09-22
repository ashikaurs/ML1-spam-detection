import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Display first 5 rows
print(df.head())

# Dataset size
print("\nDataset shape:")
print(df.shape)

# Count spam and ham
print("\nLabel distribution:")
print(df["label"].value_counts())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())