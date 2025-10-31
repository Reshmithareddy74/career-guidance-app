# =====================================================
# 📊 Enhanced Evaluation for Career Prediction Model
# =====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import confusion_matrix, classification_report, top_k_accuracy_score

# =====================================================
# 1️⃣ Load Trained Model & Dataset
# =====================================================
model_filename = "career_model_improved.joblib"
dataset_filename = "dataset1.csv"

# Load model
pipeline = joblib.load(model_filename)
print(f"✅ Loaded trained model: {model_filename}")

# Load dataset
df = pd.read_csv(dataset_filename)
print(f"✅ Loaded dataset: {dataset_filename}")
print(f"📊 Dataset shape: {df.shape}")

# =====================================================
# 2️⃣ Recreate Derived Columns (as done in training)
# =====================================================
# These were created inside train_career_model_improved.py
df['Technical Exposure'] = (
    df['Coding Skill Rating']
    + df['Number of Hackathons Attended']
    + df['Number of Internships Attended']
)
df['Soft Skills'] = (
    df['Communication Skill Rating']
    + df['Public Speaking Skill']
)

# =====================================================
# 3️⃣ Define Features & Target
# =====================================================
target_column = "Predicted Career Options"
X = df.drop(columns=[target_column])
y = df[target_column]

# =====================================================
# 4️⃣ Generate Predictions
# =====================================================
print("\n🔍 Generating predictions...")
y_pred = pipeline.predict(X)
y_proba = pipeline.predict_proba(X)
classes = pipeline.classes_

# =====================================================
# 5️⃣ Confusion Matrix & Classification Report
# =====================================================
cm = confusion_matrix(y, y_pred, labels=classes)
cm_df = pd.DataFrame(cm, index=classes, columns=classes)

report = classification_report(y, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

# Top-3 Accuracy
top3_acc = top_k_accuracy_score(y, y_proba, k=3)
print(f"\n🎯 Top-3 Accuracy: {top3_acc * 100:.2f}%")

# =====================================================
# 6️⃣ Visualizations
# =====================================================
plt.figure(figsize=(10, 8))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Confusion Matrix - Career Prediction Model", fontsize=14)
plt.xlabel("Predicted Career")
plt.ylabel("Actual Career")
plt.tight_layout()
plt.savefig("confusion_matrix_enhanced.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=report_df.index[:-3], y=report_df['f1-score'][:-3], palette="coolwarm")
plt.title("Per-Class F1-Score - Career Prediction Model", fontsize=14)
plt.ylabel("F1-Score")
plt.xlabel("Career Category")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("per_class_f1_scores.png")
plt.show()

report_df.iloc[:-3, :][['precision', 'recall']].plot(kind='bar', figsize=(10,6), color=['skyblue', 'lightcoral'])
plt.title("Precision vs Recall by Career", fontsize=14)
plt.ylabel("Score")
plt.xlabel("Career Category")
plt.xticks(rotation=45, ha='right')
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig("precision_recall_comparison.png")
plt.show()

# =====================================================
# 7️⃣ Save Outputs
# =====================================================
report_df.to_csv("classification_report_enhanced.csv", index=True)
print("\n✅ All enhanced visuals and reports saved successfully!")
print("📂 Files created:")
print("   - confusion_matrix_enhanced.png")
print("   - per_class_f1_scores.png")
print("   - precision_recall_comparison.png")
print("   - classification_report_enhanced.csv")


# =====================================================
# 8️⃣ Overall Performance Metrics Visualization
# =====================================================

# Calculate overall metrics
accuracy = report_df.loc['accuracy', 'precision'] if 'accuracy' in report_df.index else (y_pred == y).mean()
precision = report_df.loc['weighted avg', 'precision']
recall = report_df.loc['weighted avg', 'recall']
f1 = report_df.loc['weighted avg', 'f1-score']

# Create a dataframe for visualization
overall_metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'Top-3 Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Score': [accuracy * 100, top3_acc * 100, precision * 100, recall * 100, f1 * 100]
})

# Plot as a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x='Metric', y='Score', data=overall_metrics, palette='viridis')
plt.title("Overall Performance Metrics - Career Prediction Model", fontsize=14)
plt.ylabel("Score (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("overall_performance_metrics.png")
plt.show()

print("📊 Overall performance metrics image saved as: overall_performance_metrics.png")

