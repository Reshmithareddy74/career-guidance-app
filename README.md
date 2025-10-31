Problem Statement

Students often struggle to choose suitable career paths after their studies because existing platforms provide generic recommendations. These platforms fail to consider individual academic performance, technical skills, and personal attributes, leading to poor alignment between students’ abilities and their chosen careers.
_____________________________________________________________________________________________________________________________________
Introduction

The AI-Based Career Guidance System is an intelligent web application designed to assist students in identifying the most appropriate career options. By analyzing academic records, technical skills, certifications, soft skills, and personality traits, the system provides personalized career recommendations using advanced AI techniques.
_____________________________________________________________________________________________________________________________________
Purpose: To guide students in making informed career decisions that align with their strengths, interests, and skills, thereby improving their professional satisfaction and success.
_____________________________________________________________________________________________________________________________________
Dataset Used

The dataset for the AI-Based Career Guidance System consists of student academic records and profiles, capturing both quantitative and qualitative information to enable accurate career predictions.

Key Components:

Academic Records:

Marks or grades in subjects such as Operating Systems, Algorithms, Software Engineering, Computer Networks, Electronics, Computer Architecture, and Mathematics.

Technical Skills:

Programming skills, certifications, software proficiency, and coding exposure.

Soft Skills & Personality Traits:

Communication skills, teamwork, problem-solving ability, leadership, and other personality attributes relevant to career success.

Additional Features:

Interests, extracurricular activities, and any other relevant personal or professional experiences.
_____________________________________________________________________________________________________________________________________
Algorithm Used: The system employs Machine Learning, specifically the Random Forest Classifier, to analyze student data and predict suitable career paths. NLP techniques are also integrated to process qualitative information such as interests and skills.
_____________________________________________________________________________________________________________________________________
📂 Career Guidance App – Folder Structure


career-guidance-app/
│
├── .devcontainer/                      # Development container configuration
│   └── devcontainer.json               # VS Code dev container settings
│
├── app.py                              # Main web application (Streamlit or Flask)
├── train_career_model.py               # Script to train the ML career prediction model
├── evaluate_career_model.py            # Script to evaluate the model and generate performance reports
│
├── dataset1.csv                        # Raw dataset with student profiles
├── users.csv                           # User data for predictions
│
├── models/                             # Directory for saved model files
│   ├── career_model.joblib             # Initial trained model
│   ├── career_model_improved.joblib    # Improved Random Forest model
│   ├── career_pipeline.joblib          # Preprocessing pipeline (encoders, scalers, etc.)
│   ├── label_encoder.pkl               # Label encoder for career labels
│   ├── logistic_model.pkl              # Optional logistic regression model
│   ├── scaler.pkl                      # Scaler for numerical features
│   └── features.pkl                    # Saved feature list used during training
│
├── results/                            # Model evaluation results and visualizations
│   ├── classification_report_enhanced.csv   # Detailed class-wise metrics
│   ├── confusion_matrix_enhanced.png        # Confusion matrix heatmap
│   ├── overall_performance_metrics.png      # Summary of overall metrics (accuracy, Top-3 accuracy)
│   ├── per_class_f1_scores.png              # F1-score comparison by class
│   └── precision_recall_comparison.png      # Precision vs recall comparison graph
│
├── requirements.txt                    # Python dependencies
├── README.md                           # Project overview, setup, and usage instructions
└── .gitignore                          # Files/folders to ignore in Git

____________________________________________________________________________________________________________________________________
Objectives:

Provide personalized career recommendations based on academic and personal profiles.

Reduce mismatch between student abilities and career choices.

Incorporate both quantitative (marks, grades) and qualitative (skills, personality) factors.

Enable continuous learning and improvement through feedback.
_____________________________________________________________________________________________________________________________________
Advantages/Uses:

Helps students make data-driven career decisions.

Supports educators and counselors in guiding students.

Identifies skill gaps and suggests areas for improvement.

Improves overall student satisfaction and career success.
_____________________________________________________________________________________________________________________________________
Model Performance 

Overall Accuracy

Accuracy: 83.4% — This indicates the model correctly predicts the exact career label for most students.

Macro Avg Precision: 83.68%

Macro Avg Recall: 83.35%

Macro Avg F1-score: 83.47%

These metrics show that the model performs consistently well across all classes, maintaining a good balance between precision and recall.
______________________________________________________________________________________________________________________________

📊 Model Evaluation & Visualization 

The project has been enhanced with new evaluation scripts and visual reports for better model analysis and interpretability.


evaluate_career_model.py – Evaluates the trained model using test data and generates performance metrics.

classification_report_enhanced.csv – Detailed precision, recall, and F1-scores for each predicted career.

confusion_matrix_enhanced.png – Visual confusion matrix showing prediction vs. actual outcomes.

per_class_f1_scores.png – Bar chart comparing F1-scores across different careers.

precision_recall_comparison.png – Visual comparison of precision and recall per class.

overall_performance_metrics.png – Summary of model performance, including standard and Top-3 accuracies.
Practical Insights

The system can suggest multiple suitable career paths for a student rather than a single rigid choice.

Helps students identify strengths, weaknesses, and skill gaps based on academic and personal profiles.

Enables data-driven career guidance, reducing mismatch between student abilities and career choices.
_______________________________________________________________________________________________________________________________
Insights for Improvement:

Increase dataset size for better representation of each career category.

Feature engineering: include more detailed skill, interest, and project-based features.

Consider multi-label classification since students may be suitable for multiple careers.

Explore ensemble methods or deep learning models for higher predictive performance.
_______________________________________________________________________________________________
Conclusion of Results

The AI-Based Career Guidance System successfully demonstrates that machine learning, combined with academic and personal data, can provide actionable and personalized career guidance. Even though exact predictions are challenging due to overlapping career skill sets, the Top-3 accuracy shows meaningful real-world applicability for helping students choose suitable career paths.




