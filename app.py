import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pickle

st.set_page_config(page_title="BioScan", layout="wide")
from pytorch_tabnet.tab_model import TabNetClassifier

@st.cache_resource
def load_model():
    model = TabNetClassifier()
    model.load_model("tabnet_model.zip")   # 🔥 use .zip here
    return model

tabnet_model = load_model()

# Disease labels used by the TabNet model
disease_labels = ["Fit", "Diabetes", "Anemia", "Hypertension", "Heart Disease"]

# --------------------------
# PAGE CONTROL (FIXED)
# --------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_to(page):
    st.session_state.page = page

# --------------------------
# DUMMY ML MODEL
# --------------------------
def predict_risk(data):
    score = np.mean(list(data.values()))
    
    if score > 120:
        return "High Risk", 0.85
    elif score > 80:
        return "Medium Risk", 0.60
    else:
        return "Low Risk", 0.30

# --------------------------
# SIDEBAR NAVIGATION
# --------------------------
st.sidebar.title("🧠 BioScan System")

if st.sidebar.button("🏠 Home"):
    go_to("Home")
if st.sidebar.button("🧪 Analysis"):
    go_to("Analysis")
if st.sidebar.button("📊 Results"):
    go_to("Results")
if st.sidebar.button("📄 About"):
    go_to("About")

page = st.session_state.page

# ==========================
# HOME
# ==========================
if page == "Home":

    # =========================
    # GLOBAL CSS (BETTER STYLE)
    # =========================
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(120deg, #0f172a, #1e3a8a);
        padding: 60px;
        border-radius: 20px;
        color: white;
    }
    .section {
        padding: 40px 0px;
    }
    .card {
        background: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    }
    .contact-box {
        background: linear-gradient(120deg, #1e293b, #0f172a);
        padding: 40px;
        border-radius: 15px;
        color: white;
    }
     

    .card {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
    color: #111827;
    transition: 0.3s;
}
    .card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 15px 30px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)
    # =========================
    # HERO SECTION
    # =========================
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown("""
        <div class="hero">
            <h1>🧬 BioScan AI Diagnostic System</h1>
            <p>
            Transforming healthcare using Artificial Intelligence.  
            Detect diseases early, reduce risks, and make smarter decisions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Diagnosis"):
            go_to("Analysis")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1580281657527-47c8b7f6a7b2",
            use_container_width=True
        )

    st.write("")

    # =========================
    # AI IMPACT SECTION
    # =========================
    st.markdown("## 🧠 How AI is Transforming Healthcare")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        Artificial Intelligence enables early detection of diseases by analyzing 
        complex biomarker patterns.

        With BioScan:
        - Multiple health parameters are analyzed together  
        - Machine learning predicts disease risk  
        - Personalized insights are generated  

        This reduces diagnosis time and improves accuracy significantly.
        """)

    st.write("---")

    # =========================
    # FEATURES SECTION
    # =========================
    st.markdown("## 🔍 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🧪 Multi-Biomarker Analysis<br><br>Analyze multiple parameters simultaneously.</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">🤖 AI Prediction<br><br>Predict disease risks using trained models.</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">📊 Visual Reports<br><br>Understand results through graphs.</div>', unsafe_allow_html=True)

    st.write("---")

    # =========================
    # WORKFLOW SECTION
    # =========================
    st.markdown("## ⚙️ How BioScan Works")

    st.markdown("""
    1. Enter patient biomarker data  
    2. AI processes the data  
    3. Risk prediction is generated  
    4. Detailed report is displayed  
    """)

    st.write("---")

    # =========================
    # EXTRA CONTENT (MAKE PAGE LONGER)
    # =========================
    st.markdown("## 🌍 Why This Matters")

    st.markdown("""
    Healthcare systems often struggle with late diagnosis.  
    BioScan helps in early detection, which can prevent severe conditions.

    Benefits include:
    - Reduced healthcare costs  
    - Faster diagnosis  
    - Better patient outcomes  
    """)

    st.write("---")

    # =========================
    # CONTACT SECTION (EMAIL)
    # =========================
    st.markdown("## 📩 Contact Us")

    with st.container():
        st.markdown('<div class="contact-box">', unsafe_allow_html=True)

        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        if st.button("📨 Send Message"):
            if name and email and message:
                st.success("Message sent successfully (demo mode).")
                # You can connect SMTP here
            else:
                st.error("Please fill all fields")

        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    # =========================
    # FINAL CTA
    # =========================
    st.markdown("### 🚀 Ready to analyze your health?")

    if st.button("👉 Run Analysis Now"):
        go_to("Analysis")

# ==========================
# ==========================
# ANALYSIS PAGE (TABNET INTEGRATED)
# ==========================
elif page == "Analysis":

    st.title("🧪 Patient Biomarker Input")

    col1, col2, col3 = st.columns(3)

    with col1:
        glucose = st.number_input("Glucose (mg/dL)", 50, 300, 120)
        hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.6)
        sbp = st.number_input("Systolic BP", 80, 200, 120)

    with col2:
        dbp = st.number_input("Diastolic BP", 40, 130, 80)
        ldl = st.number_input("LDL", 50, 200, 100)
        hdl = st.number_input("HDL", 20, 100, 50)

    with col3:
        triglycerides = st.number_input("Triglycerides", 50, 300, 140)
        hemoglobin = st.number_input("Hemoglobin", 8.0, 18.0, 13.5)
        mcv = st.number_input("MCV", 70, 110, 90)

    # --------------------------
    # RUN ANALYSIS (REAL MODEL)
    # --------------------------
    if st.button("🚀 Run Diagnostic Analysis"):

        data = {
            "Glucose": glucose,
            "HbA1c": hba1c,
            "SBP": sbp,
            "DBP": dbp,
            "LDL": ldl,
            "HDL": hdl,
            "Triglycerides": triglycerides,
            "Hemoglobin": hemoglobin,
            "MCV": mcv
        }

        # 🔥 Convert input to correct format
        input_data = np.array([[
            data["Glucose"],
            data["HbA1c"],
            data["SBP"],
            data["DBP"],
            data["LDL"],
            data["HDL"],
            data["Triglycerides"],
            data["Hemoglobin"],
            data["MCV"]
        ]])

        # 🔥 REAL TABNET PREDICTION
        
        probs = tabnet_model.predict_proba(input_data)[0]
        disease = tabnet_model.predict(input_data)[0]

        # 🔥 CONFIDENCE + RISK
        confidence = float(np.max(probs))

        if confidence > 0.75:
            risk = "High Risk"
        elif confidence > 0.5:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"

        # --------------------------
        # STORE RESULTS (IMPORTANT)
        # --------------------------
        st.session_state.data = data
        st.session_state.probs = probs
        st.session_state.disease = disease
        st.session_state.result = (risk, confidence)
        st.session_state.analysis_done = True

        st.success("✅ Analysis Completed Successfully")

    # --------------------------
    # NAVIGATION BUTTON (FIXED)
    # --------------------------
    if st.session_state.get("analysis_done", False):

        if st.button("👉 View Results"):
            st.session_state.page = "Results"
            st.rerun()
# ==========================
# ==========================
# RESULTS PAGE (TABNET INTEGRATED)
# ==========================
elif page == "Results":

    st.title("📊 BioScan Diagnostic Report")

    # --------------------------
    # CHECK DATA
    # --------------------------
    if "data" not in st.session_state or "probs" not in st.session_state:
        st.warning("⚠️ Please run analysis first.")
    else:
        data = st.session_state.data
        probs = st.session_state.probs
        disease = st.session_state.disease

        # --------------------------
        # CONFIDENCE + RISK FROM MODEL
        # --------------------------
        confidence = float(np.max(probs))

        if confidence > 0.75:
            risk = "High Risk"
        elif confidence > 0.5:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"

        # --------------------------
        # HEADER
        # --------------------------
        st.subheader("✅ Analysis Complete")

        # --------------------------
        # MAIN RESULT
        # --------------------------
        st.subheader("🧾 Predicted Disease")

        if disease == "Healthy":
            st.success("✅ No disease detected (Healthy)")
            st.write("All biomarkers are within normal clinical range.")
        else:
            st.error(f"⚠️ Detected Condition: {disease}")

        st.write("---")

        # --------------------------
        # RISK + CONFIDENCE
        # --------------------------
        st.markdown(f"""
        ### 📌 Overall Risk Level: **{risk}**
        **Confidence Score:** {round(confidence * 100, 2)}%
        """)

        if risk == "Low Risk":
            st.success("No major disease risk detected. You are in good health.")
        elif risk == "Medium Risk":
            st.warning("Moderate risk detected. Lifestyle changes recommended.")
        else:
            st.error("High risk detected. Immediate medical consultation advised.")

        st.write("---")

        # --------------------------
        # HEALTH SUMMARY
        # --------------------------
        st.subheader("🩺 Health Summary")

        if disease == "Diabetes":
            st.write("""
            - High glucose and HbA1c levels detected  
            - Indicates possible Type 2 Diabetes  
            - Requires sugar monitoring  
            """)
        elif disease == "Anemia":
            st.write("""
            - Low hemoglobin detected  
            - Indicates possible anemia  
            - May require iron supplementation  
            """)
        elif disease == "Hypertension":
            st.write("""
            - Elevated blood pressure levels  
            - Risk of hypertension  
            """)
        elif disease == "Heart Disease":
            st.write("""
            - Cholesterol imbalance observed  
            - Possible cardiovascular risk  
            """)
        else:
            st.write("""
            - All biomarkers are within normal range  
            """)

        st.write("---")

        

        # --------------------------
        # BIOMARKER GRAPH
        # --------------------------
        st.subheader("📊 Biomarker Visualization")

        fig2, ax2 = plt.subplots()
        ax2.bar(data.keys(), data.values())
        plt.xticks(rotation=45)
        st.pyplot(fig2)

        st.write("---")

        # --------------------------
        # NAVIGATION
        # --------------------------
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔄 Re-Analyze"):
                st.session_state.page = "Analysis"
                st.rerun()

        with col2:
            if st.button("🏠 Back to Home"):
                st.session_state.page = "Home"
                st.rerun()

# ==========================
# ABOUT PAGE
# ==========================
elif page == "About":

    st.title("📄 About BioScan")

    st.markdown("""
    BioScan is an AI-based diagnostic system that uses biomarker data to predict disease risk.

    ### 🔬 Model
    - Multi-Layer Perceptron (MLP)
    - ROC-AUC evaluation

    ### 🎯 Goal
    Early detection and prevention of diseases.
    """)