import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
import joblib

# Load your dataset
df = pd.read_csv('ObesityDataSet.csv')

# Drop rows with missing values just in case
df = df.dropna()

# Define features and target
X = df.drop(columns=['NObeyesdad'])
y = df['NObeyesdad']

# Define which features are numeric and which are categorical
numeric_features = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE', 'BMI']
categorical_features = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Classifiers
clf1 = RandomForestClassifier(random_state=42)
clf2 = GradientBoostingClassifier(random_state=42)
clf3 = SVC(probability=True, random_state=42)

# Voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('gb', clf2),
    ('svc', clf3)
], voting='soft')

# Full pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', voting_clf)
])

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved to model.pkl")
