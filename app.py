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

import streamlit as st

# -----------------------------
# Helper function: set plain background color
# -----------------------------
def set_bg(color: str = "#a5a6c7"):
    """
    Set a plain background color for the Streamlit app.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


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
# About Us Tab (Final Enhanced, Centered Text)
# -----------------------------
with tabs[1]:
    st.markdown("<h1 style='text-align: center;'>👨‍💻 About Us</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center;'>
    Welcome to the <b>AI-Powered Career Guidance Platform</b>, designed to help students and professionals explore  
    the right career paths based on academic performance, skills, and interests.<br>
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
                 caption="Personalized Guidance", use_container_width=True)
    with cols[1]:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
                 caption="Data-Driven Insights", use_container_width=True)
    with cols[2]:
        st.image("https://tse1.mm.bing.net/th/id/OIP.21HQoHL3KEL7SYKNFh9vFwHaD7?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
                 caption="Career Insights", use_container_width=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # -----------------------------
    # Why Choose Us
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>💡 Why Choose Us?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>
    • <b>Personalized Career Paths</b> – Tailored suggestions based on your academic scores, skills, and interests.<br>
    • <b>Practical Exposure Insights</b> – Evaluate your coding, communication, and logical reasoning skills.<br>
    • <b>Job Guidance</b> – Recommendations for  real-world opportunities.<br>
    • <b>User-Friendly Interface</b> – Simple forms, sliders, and visual outputs for effortless interaction.<br>
    • <b>Actionable Analytics</b> – Graphs and probability-based career predictions to help you make informed choices.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # -----------------------------
    # Animated-style Metrics (Counters)
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
   # -----------------------------
    st.markdown("<h3 style='text-align: center;'>🌟 Explore Your Future With Us</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
                 caption="AI Career Predictions", use_container_width=True)
        st.markdown("<div style='text-align: center;'>Discover your best-fit career using AI-driven recommendations.</div>", unsafe_allow_html=True)
    with col3:
        st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
                 caption="Guided Roadmap", use_container_width=True)
        st.markdown("<div style='text-align: center;'>Plan your roadmap for higher studies or dream job opportunities.</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    
    # -----------------------------
    # Mission Statement
    # -----------------------------
    st.markdown("<h3 style='text-align: center;'>🎯 Our Mission</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>
                
    To empower learners to take confident steps toward rewarding careers by combining the power of <b>Artificial Intelligence</b> with <b>practical guidance</b>.<br>
                
    To bridge the gap between education and employment using <b>Artificial Intelligence</b>.<br>
    
    Our goal is to make career planning <b>simple, smart, and personalized</b> for every learner.<br>
                
    Join us to explore a world of career opportunities tailored just for you! 🚀
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Find Your Career Tab
# -----------------------------
with tabs[2]:
    #set_bg("https://user-gen-media-assets.s3.amazonaws.com/seedream_images/8a84a92b-7a87-49f8-96b2-af704c98c2b8.png", overlay_color="rgba(0,0,0,0.25)")
    #st.markdown("<div class='overlay'></div>", unsafe_allow_html=True)
    st.title("🎓 Find Your Career")

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
                        new_user = pd.DataFrame([{"Username": username, "Email": email, "Password": password}])
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
    
    if st.session_state["logged_in"]:
        st.success(f"Welcome, {st.session_state['username']} 👋")
        #model = joblib.load("career_model.joblib")

        # Load ML model safely
        try:
            model = joblib.load("career_model.joblib")
        except Exception as e:
            st.error(f"Model loading failed: {e}")
            st.stop()  # Stop execution if model cannot be loaded
        
        col1, col2 = st.columns([1,1])
        
        with col1:
            st.header("Enter Your Details")
            os_marks = st.selectbox("Operating System Marks", list(range(40, 101)))
            algo_marks = st.selectbox("Algorithms Marks", list(range(40, 101)))
            se_marks = st.selectbox("Software Engineering Marks", list(range(40, 101)))
            cn_marks = st.selectbox("Computer Networks Marks", list(range(40, 101)))
            electronics_marks = st.selectbox("Electronics Marks", list(range(40, 101)))
            ca_marks = st.selectbox("Computer Architecture Marks", list(range(40, 101)))
            math_marks = st.selectbox("Mathematics Marks", list(range(40, 101)))
            coding_skill = st.slider("Coding Skill Rating", 1, 10, 5)
            communication_skill = st.slider("Communication Skill Rating", 1, 10, 5)
            public_speaking = st.slider("Public Speaking Skill", 1, 10, 5)
            logical_reasoning = st.slider("Logical Reasoning Score", 1, 10, 5)
            hackathons = st.number_input("Number of Hackathons Attended", 0, 10, 0)
            internships = st.number_input("Number of Internships Attended", 0, 5, 0)
            interest_type = st.selectbox("Interest Type", ['Technical', 'Management'])
            career_area = st.selectbox("Interested Career Area", ['Developer', 'Analyst', 'Administrator', 'UX Designer', 'Research'])
            personality = st.selectbox("Personality", ['Extrovert', 'Introvert'])
            memory = st.selectbox("Memory Capacity", ['Excellent', 'Medium', 'Poor'])
            reading = st.selectbox("Reading and Writing Skill", ['Excellent', 'Medium', 'Average', 'Poor'])
            teamwork = st.selectbox("Worked As a Team", ['Yes', 'No'])
            long_hours = st.selectbox("Willingness to Work for Long Period", ['Yes', 'No'])
            preference = st.selectbox("Preference: Job vs. Higher Studies", ['Higher Studies', 'Job'])
            company_type = st.selectbox("Type of Company Preferred", ['Product-based', 'Service-based'])
            self_learning = st.selectbox("Self-Learning Ability", ['Yes', 'No'])
            expected_hours = st.slider("Expected Hours of Work Per Day", 1, 12, 8)

            academic_avg = np.mean([os_marks, algo_marks, se_marks, cn_marks, electronics_marks, ca_marks, math_marks])
            practical_score = np.mean([coding_skill, communication_skill, public_speaking, logical_reasoning, hackathons, internships])

            input_data = pd.DataFrame([{
                'Average Marks': academic_avg,
                'Practical Exposure Score': practical_score,
                'Interest Type': interest_type,
                'Interested Career Area': career_area,
                'Personality': personality,
                'Memory Capacity': memory,
                'Reading and Writing Skill': reading,
                'Worked As a Team': teamwork,
                'Willingness to Work for Long Period': long_hours,
                'Preference: Job vs. Higher Studies': preference,
                'Type of Company Preferred': company_type,
                'Self-Learning Ability': self_learning,
                #'Expected Hours of Work Per Day': expected_hours
            }])
        
        # -----------------------------

# -----------------------------
# Career Prediction Output
# -----------------------------
            with col2:
                st.header("Career Prediction Output")
                if st.button("Predict Career"):
                    prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        top2_idx = np.argsort(probabilities)[-2:][::-1]
        top2_labels = np.array(model.classes_)[top2_idx]
        top2_probs = probabilities[top2_idx]

        st.subheader("🔝 Top 2 Career Recommendations")
        for i in range(2):
            career_name = top2_labels[i]
            prob = top2_probs[i]*100

            

           
            st.markdown(f"### {i+1}. {career_name} — Probability: {prob:.2f}%")
         

        # Optional: Bar chart
        fig, ax = plt.subplots(figsize=(10,5))
        colors = ["red" if p<0.15 else "orange" if p<0.25 else "green" for p in probabilities]
        ax.bar(model.classes_, probabilities*100, color=colors)
        ax.set_ylabel("Probability (%)")
        ax.set_title("📊 Career Probabilities")
        ax.set_xticklabels(model.classes_, rotation=45, ha='right')
        st.pyplot(fig)

        st.success(f"🎯 Final Predicted Career Option: {prediction}")


# -----------------------------
# Contact Tab
# -----------------------------
with tabs[3]:
    # Plain background (no image)
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0C0303;  /* dark background */
        }
        .overlay {
            text-align: center;
            color: white;
            padding: 80px 0;
        }
        a {
            color: #1E90FF;  /* link color */
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #00BFFF;
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="overlay">
            <h1>📞 Contact Us</h1>
            <p>Email: <b>support@careerguidance.com</b></p>
            <p>Phone: <b>+91 9000000000</b></p>
            <p>Address: <b>Hyderabad, India</b></p>
            <hr style="width:50%; margin:30px auto; border:1px solid #555;">
            <h2>🌐 Follow Us on Social Media</h2>
            <p>
                <a href="https://www.linkedin.com/company/careerguidance" target="_blank">LinkedIn</a> |
                <a href="https://twitter.com/CareerGuidanceAI" target="_blank">Twitter (X)</a> |
                <a href="https://www.instagram.com/careerguidance_ai" target="_blank">Instagram</a> |
                <a href="https://www.facebook.com/careerguidanceplatform" target="_blank">Facebook</a>
            </p>
            <p>For more information, visit our <a href="https://careerguidance.com" target="_blank">official website</a>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
