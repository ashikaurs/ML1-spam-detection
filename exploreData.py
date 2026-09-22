import pandas as pd
import re

# Load dataset
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)


# Text cleaning function
def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove consecutive(extra) spaces
    text = re.sub(r"\s+", " ", text) # substitute : re.sub(find , replace , text)

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text) #Find characters that are NOT letters, numbers, or spaces, and replace them with nothing.
    # ^ is negation []-> anything within this considered.

    # Remove leading/trailing spaces
    text = text.strip()

    return text


# Apply cleaning
df["clean_message"] = df["message"].apply(clean_text)
#df["clean_message"]-> creates new column names clea...\
#df["message"]-> using the already present message column.

# See original vs cleaned text
print(df[["message", "clean_message"]].head(10))