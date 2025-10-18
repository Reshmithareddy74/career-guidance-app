# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Career Guidance Website", layout="wide")

# -----------------------------
# Users CSV
# -----------------------------
users_file = "users.csv"
if os.path.exists(users_file):
    users_df = pd.read_csv(users_file)
else:
    users_df = pd.DataFrame(columns=["Username", "Email", "Password"])

# -----------------------------
# Session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None

# -----------------------------
# Navigation Tabs
# -----------------------------
tabs_labels = ["Home", "About Us", "Find Your Career", "Contact"]
tabs = st.tabs(tabs_labels)

# -----------------------------
# Home Tab
# -----------------------------
with tabs[0]:
    st.markdown("""
    <div class="overlay" style="display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
        <h1>💼 AI Powered Career Guidance System</h1>
        <p>Step into the career that’s made for you.</p>
        <img src="https://brainbow.co.in/wp-content/uploads/2020/07/Career-guidance.jpg" 
             style="width:150%; margin-top:20px; border-radius:10px;">
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# About Us Tab
# -----------------------------
with tabs[1]:
    st.markdown("<h1 style='text-align: center;'>👨‍💻 About Us</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size:16px;'>
    Welcome to the <b>AI-Powered Career Guidance Platform</b>, designed to help students and professionals explore  
    the right career paths based on academic performance, skills, and interests.<br><br>
    Our system uses <b>Machine Learning</b> and <b>Data-Driven Insights</b> to provide personalized career recommendations.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)


  # -----------------------------
    # Our Advantages
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>🚀 Our Advantages</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        st.image("https://cdn.analyticsvidhya.com/wp-content/uploads/2024/11/Personalized-Learning-with-Multi-Agentic-Systems-A-CrewAI-Based-DSA-Tutor-.webp",
                 caption="Personalized Guidance", width='content')
    with cols[1]:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
                 caption="Data-Driven Insights", width='content')
    with cols[2]:
        st.image("https://tse1.mm.bing.net/th/id/OIP.21HQoHL3KEL7SYKNFh9vFwHaD7?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
                 caption="Career Insights", width='content')

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    # -----------------------------
    # Why Choose Us
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>💡 Why Choose Us?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size:16px;'>
    • <b>Personalized Career Paths</b> – Tailored suggestions based on your academic scores, skills, and interests.<br>
    • <b>Practical Exposure Insights</b> – Evaluate your coding, communication, and logical reasoning skills.<br>
    • <b>Job Guidance</b> – Recommendations for real-world opportunities.<br>
    • <b>User-Friendly Interface</b> – Simple forms, sliders, and visual outputs for effortless interaction.<br>
    • <b>Actionable Analytics</b> – Graphs and probability-based career predictions to help you make informed choices.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # -----------------------------
    # Metrics / Counters
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>📊 Our Impact</h3>", unsafe_allow_html=True)
    cols_counter = st.columns(3)
    with cols_counter[0]:
        st.metric(label="AI Recommendations", value="500+")
    with cols_counter[1]:
        st.metric(label="Guided Students", value="1,200+")
    with cols_counter[2]:
        st.metric(label="Career Insights Delivered", value="900+")

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    # -----------------------------
    # Explore Your Future
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>🌟 Explore Your Future With Us</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
                 caption="AI Career Predictions", width='content')
        st.markdown("<div style='text-align: center;'>Discover your best-fit career using AI-driven recommendations.</div>", unsafe_allow_html=True)
    with col3:
        st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
                 caption="Guided Roadmap", width='content')
        st.markdown("<div style='text-align: center;'>Plan your roadmap for higher studies or dream job opportunities.</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # -----------------------------
    # Mission Statement
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>🎯 Our Mission</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size:16px;'>
    To empower learners to take confident steps toward rewarding careers by combining the power of <b>Artificial Intelligence</b> with <b>practical guidance</b>.<br>
    To bridge the gap between education and employment using <b>AI</b>.<br>
    Our goal is to make career planning <b>simple, smart, and personalized</b> for every learner.<br>
    Join us to explore a world of career opportunities tailored just for you! 🚀
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Find Your Career Tab
# -----------------------------
with tabs[2]:
    st.title("🎓 Find Your Career")

    # Registration/Login
    if not st.session_state["logged_in"]:
        st.subheader("📝 Register / Login")
        choice = st.radio("Choose an action:", ["Register", "Login"])

        if choice == "Register":
            with st.form("register_form"):
                username = st.text_input("Username")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                submit = st.form_submit_button("Register")

                if submit:
                    if username in users_df["Username"].values:
                        st.error("❌ Username already exists!")
                    elif password != confirm_password:
                        st.error("❌ Passwords do not match!")
                    else:
                        new_user = pd.DataFrame([{
                            "Username": username,
                            "Email": email,
                            "Password": password
                        }])
                        users_df = pd.concat([users_df, new_user], ignore_index=True)
                        users_df.to_csv(users_file, index=False)
                        st.success(f"✅ User '{username}' registered successfully! You can now login.")

        else:  # Login
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")

                if submit:
                    if username in users_df["Username"].values:
                        user_record = users_df[users_df["Username"] == username].iloc[0]
                        if password == user_record["Password"]:
                            st.success(f"✅ Logged in successfully as '{username}'")
                            st.session_state["logged_in"] = True
                            st.session_state["username"] = username
                        else:
                            st.error("❌ Invalid password")
                    else:
                        st.error("❌ Invalid username")

    # Career Prediction Form
    if st.session_state["logged_in"]:
        st.success(f"Welcome, {st.session_state['username']} 👋")

        try:
            model = joblib.load("career_model_improved.joblib")
            st.info("✅ Model loaded successfully!")
        except Exception as e:
            st.error(f"❌ Model loading failed: {e}")
            st.stop()

        col1, col2 = st.columns(2)

        with col1:
            st.header("Enter Your Details")

            # Dataset columns
            os_marks = st.slider("Operating System Marks", 40, 100, 70)
            algo_marks = st.slider("Algorithms Marks", 40, 100, 70)
            se_marks = st.slider("Software Engineering Marks", 40, 100, 70)
            cn_marks = st.slider("Computer Networks Marks", 40, 100, 70)
            elec_marks = st.slider("Electronics Marks", 40, 100, 70)
            ca_marks = st.slider("Computer Architecture Marks", 40, 100, 70)
            math_marks = st.slider("Mathematics Marks", 40, 100, 70)
            tech_exp = st.slider("Technical Exposure", 1, 10, 5)
            soft_skills = st.slider("Soft Skills", 1, 10, 5)
            coding = st.slider("Coding Skill Rating", 1, 10, 5)
            comm = st.slider("Communication Skill Rating", 1, 10, 5)
            pub = st.slider("Public Speaking Skill", 1, 10, 5)
            logic = st.slider("Logical Reasoning Score", 1, 10, 5)
            hack = st.slider("Number of Hackathons Attended", 0, 10, 0)
            intern = st.slider("Number of Internships Attended", 0, 5, 0)
            hours = st.slider("Expected Hours of Work Per Day", 1, 12, 8)

            memory = st.selectbox("Memory Capacity", ['Excellent', 'Medium', 'Poor'])
            read = st.selectbox("Reading and Writing Skill", ['Excellent', 'Medium', 'Average', 'Poor'])
            cert = st.selectbox("Certifications", ['Yes', 'No'])
            teamwork = st.selectbox("Worked As a Team", ['Yes', 'No'])
            personality = st.selectbox("Personality", ['Extrovert', 'Introvert'])
            longwork = st.selectbox("Willingness to Work for Long Period", ['Yes', 'No'])
            preference = st.selectbox("Preference: Job vs. Higher Studies", ['Job', 'Higher Studies'])
            company = st.selectbox("Type of Company Preferred", ['Product-based', 'Service-based'])
            area = st.selectbox("Interested Career Area", ['Developer', 'Analyst', 'Administrator', 'UX Designer', 'Research'])
            selflearn = st.selectbox("Self-Learning Ability", ['Yes', 'No'])
            interest = st.selectbox("Interest Type", ['Technical', 'Management'])

            input_data = pd.DataFrame([{
                'Operating System Marks': os_marks,
                'Algorithms Marks': algo_marks,
                'Software Engineering Marks': se_marks,
                'Computer Networks Marks': cn_marks,
                'Electronics Marks': elec_marks,
                'Computer Architecture Marks': ca_marks,
                'Mathematics Marks': math_marks,
                'Technical Exposure': tech_exp,
                'Soft Skills': soft_skills,
                'Coding Skill Rating': coding,
                'Communication Skill Rating': comm,
                'Public Speaking Skill': pub,
                'Logical Reasoning Score': logic,
                'Number of Hackathons Attended': hack,
                'Number of Internships Attended': intern,
                'Expected Hours of Work Per Day': hours,
                'Memory Capacity': memory,
                'Reading and Writing Skill': read,
                'Certifications': cert,
                'Worked As a Team': teamwork,
                'Personality': personality,
                'Willingness to Work for Long Period': longwork,
                'Preference: Job vs. Higher Studies': preference,
                'Type of Company Preferred': company,
                'Interested Career Area': area,
                'Self-Learning Ability': selflearn,
                'Interest Type': interest
            }])

        with col2:
            st.header("Career Prediction Output")
            if st.button("🔍 Predict Career"):
                try:
                    prediction = model.predict(input_data)[0]
                    probabilities = model.predict_proba(input_data)[0]

                    # Top 3 predictions
                    top3_idx = np.argsort(probabilities)[-3:][::-1]
                    top3_labels = np.array(model.classes_)[top3_idx]
                    top3_probs = probabilities[top3_idx]

                    st.subheader("🎯 Top 3 Career Recommendations")
                    for i in range(3):
                        st.markdown(f"**{i+1}. {top3_labels[i]} — {top3_probs[i]*100:.2f}%**")

                    # Probability bar chart
                    fig, ax = plt.subplots(figsize=(8, 5))
                    max_idx = np.argmax(probabilities)
                    colors = ['green' if i == max_idx else 'gray' for i in range(len(probabilities))]
                    ax.bar(model.classes_, probabilities * 100, color=colors)
                    ax.set_ylabel("Probability (%)")
                    ax.set_title("Career Probability Distribution")
                    ax.set_xticks(range(len(model.classes_)))
                    ax.set_xticklabels(model.classes_, rotation=45, ha="right")
                    st.pyplot(fig)

                    st.success(f"✅ Final Predicted Career: **{prediction}**")

                except Exception as e:
                    st.error(f"Prediction failed: {e}")

# -----------------------------
# Contact Tab
# -----------------------------
with tabs[3]:
    st.markdown("""
    <div style='text-align:center; color:white; background-color:#0C0303; padding:50px; border-radius:10px;'>
        <h1>📞 Contact Us</h1>
        <p>Email: <b>support@careerguidance.com</b></p>
        <p>Phone: <b>+91 9000000000</b></p>
        <p>Address: <b>Hyderabad, India</b></p>
        <hr style="width:50%; margin:30px auto; border:1px solid #555;">
        <h3>🌐 Follow Us</h3>
        <p>
            <a href="https://www.linkedin.com/company/careerguidance" target="_blank">LinkedIn</a> |
            <a href="https://twitter.com/CareerGuidanceAI" target="_blank">Twitter</a> |
            <a href="https://www.instagram.com/careerguidance_ai" target="_blank">Instagram</a>
        </p>
    </div>
    """, unsafe_allow_html=True)