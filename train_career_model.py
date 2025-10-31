# ==========================================================
# 🚀 Train Career Prediction Model 
# ==========================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib
import sys

# -----------------------------
# 1. Load Dataset
# -----------------------------
file_path = "dataset1.csv"

try:
    df = pd.read_csv(file_path)
    print(f"✅ Loaded dataset successfully: {file_path}")
    print(f"📊 Shape: {df.shape}")
except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
    sys.exit(1)

# -----------------------------
# 2. Define Target and Features
# -----------------------------
target_column = "Predicted Career Options"
X = df.drop(columns=[target_column])
y = df[target_column]

# -----------------------------
# 3. Feature Engineering
# -----------------------------
X['Technical Exposure'] = (
    X['Coding Skill Rating'] +
    X['Number of Hackathons Attended'] +
    X['Number of Internships Attended']
)
X['Soft Skills'] = (
    X['Communication Skill Rating'] +
    X['Public Speaking Skill']
)

# Numeric features
numeric_features = [
    'Operating System Marks', 'Algorithms Marks', 'Software Engineering Marks',
    'Computer Networks Marks', 'Electronics Marks', 'Computer Architecture Marks',
    'Mathematics Marks', 'Technical Exposure', 'Soft Skills', 'Expected Hours of Work Per Day'
]

# Categorical features
categorical_features = [
    'Memory Capacity', 'Reading and Writing Skill', 'Certifications', 'Worked As a Team',
    'Personality', 'Willingness to Work for Long Period', 'Preference: Job vs. Higher Studies',
    'Type of Company Preferred', 'Interested Career Area', 'Self-Learning Ability', 'Interest Type'
]

print(f"\n🔢 Numeric features: {numeric_features}")
print(f"🔤 Categorical features: {categorical_features}")

# -----------------------------
# 4. Split Data
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 5. Preprocessing
# -----------------------------
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

# -----------------------------
# 6. Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200, max_depth=20, random_state=42, class_weight='balanced'
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', model)
])

# -----------------------------
# 7. Train Model
# -----------------------------
print("\n🚀 Training model...")
pipeline.fit(X_train, y_train)
print("✅ Training completed!")

# -----------------------------
# 8. Save Model (No Accuracy Shown)
# -----------------------------
model_filename = "career_model_improved.joblib"
joblib.dump(pipeline, model_filename)
print(f"💾 Model saved successfully as '{model_filename}'")

print("\n✅ Model training and saving completed successfully!")
