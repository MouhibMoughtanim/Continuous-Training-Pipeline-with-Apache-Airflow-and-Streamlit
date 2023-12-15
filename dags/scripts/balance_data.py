import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter
from sklearn.preprocessing import LabelEncoder

# Load your dataset
# Assuming 'your_dataset.csv' is the name of your CSV file and 'target_column' is the name of your target column
data = pd.read_csv("Weather_Data.csv")

# Encode the target variable 'Description'
label_encoder = LabelEncoder()
data['Description'] = label_encoder.fit_transform(data['Description'])

# Separate features and target
X = data.drop('Description', axis=1)
y = data['Description']

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display class distribution before balancing
print("Class distribution before balancing:", Counter(y_train))

# Undersample the majority class using RandomUnderSampler
undersampler = RandomUnderSampler(sampling_strategy='not minority', random_state=42)
X_train_balanced, y_train_balanced = undersampler.fit_resample(X_train, y_train)

# Display class distribution after balancing
print("Class distribution after balancing:", Counter(y_train_balanced))

# Save the balanced dataset to a new CSV file
balanced_data = pd.concat([X_train_balanced, y_train_balanced], axis=1)
balanced_data.to_csv("balanced_dataset.csv", index=False)

# Now, 'balanced_dataset.csv' contains the balanced version of your dataset
