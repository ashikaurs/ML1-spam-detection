import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Clean the messages
def clean_text(text):
    text = text.lower()
    return text.strip()


df["clean_message"] = df["message"].apply(clean_text)


# Input
X = df["clean_message"]

# Output/answer
y = df["label"]


# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Total messages:", len(df))
print("Training messages:", len(X_train))
print("Testing messages:", len(X_test))

print("\nTraining labels:")
print(y_train.value_counts())

print("\nTesting labels:")
print(y_test.value_counts())