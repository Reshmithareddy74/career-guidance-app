# train_career_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# ------------------------
# Load Dataset
# ------------------------
data = pd.read_csv("dataset1.csv")  # Replace with your dataset path

# ------------------------
# Feature Engineering
# ------------------------
# Academic columns
academic_cols = [
    'Operating System Marks','Algorithms Marks','Software Engineering Marks',
    'Computer Networks Marks','Electronics Marks','Computer Architecture Marks','Mathematics Marks'
]

# Skill / practical exposure columns
skill_cols = [
    'Coding Skill Rating',
    'Communication Skill Rating',
    'Public Speaking Skill',
    'Logical Reasoning Score',
    'Number of Hackathons Attended',
    'Number of Internships Attended',
]

# Convert academic columns to numeric
for col in academic_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')
data[academic_cols] = data[academic_cols].fillna(0)

# Convert skill columns to numeric
for col in skill_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')
data[skill_cols] = data[skill_cols].fillna(0)

# Compute derived features
data['Average Marks'] = data[academic_cols].mean(axis=1)
data['Practical Exposure Score'] = data[skill_cols].mean(axis=1)

# ------------------------
# Define features and target
# ------------------------
numeric_features = ['Average Marks', 'Practical Exposure Score']

categorical_features = [
    'Interest Type',
    'Interested Career Area',
    'Personality',
    'Memory Capacity',
    'Reading and Writing Skill',
    'Worked As a Team',
    'Willingness to Work for Long Period',
    'Preference: Job vs. Higher Studies',
    'Type of Company Preferred',
    'Self-Learning Ability'
]

X = data[numeric_features + categorical_features]
y = data['Predicted Career Options']

# ------------------------
# Preprocessing Pipeline
# ------------------------
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

# ------------------------
# Random Forest Pipeline
# ------------------------
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    ))
])

# ------------------------
# Train the Model
# ------------------------
pipeline.fit(X, y)

# ------------------------
# Save Trained Model
# ------------------------
joblib.dump(pipeline, "career_model.joblib")
print("Training complete! Model saved as career_model.joblib")
