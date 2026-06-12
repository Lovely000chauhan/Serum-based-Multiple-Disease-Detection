import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="BioScan", layout="wide")

from pytorch_tabnet.tab_model import TabNetClassifier

@st.cache_resource
def load_model():
    model = TabNetClassifier()
    model.load_model("tabnet_model.zip")
    return model

tabnet_model = load_model()

# Disease labels used by the TabNet model
disease_labels = ["Fit", "Diabetes", "Anemia", "Hypertension", "Heart Disease"]

# --------------------------
# PAGE CONTROL
# --------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_to(page):
    # FIX 1: go_to() must call st.rerun() or navigation has no effect
    st.session_state.page = page
    st.rerun()

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
    st.markdown("""
<style>
.main { background-color: #0B1120; }

.hero-card {
    background: linear-gradient(135deg,#2563EB,#1D4ED8);
    padding: 60px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0px 15px 40px rgba(37,99,235,0.35);
}

.feature-card {
    background: #111827;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #374151;
    text-align: center;
}

.feature-card:hover {
    transform: translateY(-5px);
    transition: 0.3s;
}

.section-title {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    padding: 40px;
    color: #9CA3AF;
}
</style>
""", unsafe_allow_html=True)

    # FIX 2: Hero card and all Home content was accidentally nested inside
    # the `with col1` block. Moved everything to top-level.
    st.markdown("""
<div class="hero-card">

# 🧬 BioScan AI Diagnostic System

### AI-Powered Multi Disease Detection Platform

Detect diseases early using advanced Machine Learning and Biomarker Analysis.

</div>
""", unsafe_allow_html=True)

    st.write("---")

    # Impact metrics
    st.markdown("<h2 class='section-title'>📈 BioScan Impact</h2>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Accuracy", "94.7%")
    with c2:
        st.metric("Patients", "25,000+")
    with c3:
        st.metric("Diseases", "4+")
    with c4:
        st.metric("Predictions", "1M+")

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Diagnosis", use_container_width=True):
            go_to("Analysis")

        st.image(
            "https://images.pexels.com/photos/7089401/pexels-photo-7089401.jpeg",
            use_container_width=True
        )

    st.write("")

    # AI Impact section
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

    # Key Features
    st.markdown("<h2 class='section-title'>🔍 Key Features</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>🧪 Biomarker Analysis</h3>
        <p>Analyze multiple health parameters simultaneously.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>🤖 AI Prediction</h3>
        <p>TabNet based disease prediction engine.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-card">
        <h3>📊 Visual Reports</h3>
        <p>Interactive charts and diagnostic reports.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # Diseases supported
    st.markdown("<h2 class='section-title'>🩺 Diseases Supported</h2>", unsafe_allow_html=True)

    d1, d2, d3, d4 = st.columns(4)
    with d1:
        st.success("🩸 Diabetes")
    with d2:
        st.warning("💉 Anemia")
    with d3:
        st.error("❤️ Heart Disease")
    with d4:
        st.info("📈 Hypertension")

    st.write("---")

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

    st.markdown("<h2 class='section-title'>⚙️ How BioScan Works</h2>", unsafe_allow_html=True)
    st.markdown("""
    ### 1️⃣ Enter Biomarker Data
    ⬇️
    ### 2️⃣ AI Model Processing
    ⬇️
    ### 3️⃣ Disease Detection
    ⬇️
    ### 4️⃣ Risk Assessment
    ⬇️
    ### 5️⃣ Diagnostic Report
    """)

    st.write("---")

    st.markdown("<h2 class='section-title'>🌍 Why BioScan?</h2>", unsafe_allow_html=True)
    st.info("""
    ✔ Early Disease Detection

    ✔ Reduced Diagnostic Time

    ✔ Better Healthcare Decisions

    ✔ AI-Powered Medical Insights

    ✔ Easy to Use Interface
    """)

    # Contact section
    st.markdown("## 📩 Contact Us")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("📨 Send Message"):
        if name and email and message:
            st.success("Message sent successfully (demo mode).")
        else:
            st.error("Please fill all fields.")
    # FIX 3: Removed the floating </div> close tag that had no matching open tag

    st.write("---")

    st.markdown("<h2 class='section-title'>⭐ User Feedback</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.success("⭐⭐⭐⭐⭐\n\nFast and accurate disease prediction.")
    with col2:
        st.info("⭐⭐⭐⭐⭐\n\nModern AI powered healthcare platform.")

    st.write("---")

    # FIX 4: Removed duplicate Impact metrics section (was copy-pasted twice)

    st.markdown("## 💬 User Feedback")
    st.info("⭐ 4.9/5 User Satisfaction")
    st.success("✔ Early Detection Support")
    st.warning("✔ AI Powered Risk Assessment")

    st.write("---")

    st.markdown("# 🚀 Ready to Analyze Your Health?")

    if st.button("👉 Run Analysis Now", use_container_width=True):
        go_to("Analysis")

    st.markdown("""
    <div class="footer">

    ### 🧬 BioScan AI Diagnostic System

    Empowering Healthcare Through Artificial Intelligence

    © 2026 BioScan

    </div>
    """, unsafe_allow_html=True)

# ==========================
# ANALYSIS PAGE
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

        probs = tabnet_model.predict_proba(input_data)[0]
        disease = tabnet_model.predict(input_data)[0]

        

        confidence = float(np.max(probs))

        if confidence > 0.75:
            risk = "High Risk"
        elif confidence > 0.5:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"

        st.session_state.data = data
        st.session_state.probs = probs
        st.session_state.disease = disease
        st.session_state.result = (risk, confidence)
        st.session_state.analysis_done = True

        st.success("✅ Analysis Completed Successfully")

    if st.session_state.get("analysis_done", False):
        if st.button("👉 View Results"):
            go_to("Results")

# ==========================
# RESULTS PAGE
# ==========================
elif page == "Results":

    st.title("📊 BioScan Diagnostic Report")

    if "data" not in st.session_state or "probs" not in st.session_state:
        st.warning("⚠️ Please run analysis first.")
    else:
        data = st.session_state.data
        probs = st.session_state.probs
        disease = st.session_state.disease

        confidence = float(np.max(probs))

        if confidence > 0.75:
            risk = "High Risk"
        elif confidence > 0.5:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"

        st.subheader("✅ Analysis Complete")

        st.subheader("🧾 Predicted Disease")

        if disease == "Fit":
            st.success("✅ No disease detected (Healthy)")
            st.write("All biomarkers are within normal clinical range.")
        else:
            st.error(f"⚠️ Detected Condition: {disease}")

        st.write("---")

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
            st.write("- All biomarkers are within normal range")

        st.write("---")


        st.write("---")

        st.subheader("📊 Biomarker Visualization")

        fig2, ax2 = plt.subplots()
        ax2.bar(data.keys(), data.values())
        plt.xticks(rotation=45, ha="right")
        ax2.set_title("Input Biomarker Values")
        st.pyplot(fig2)

        st.write("---")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Re-Analyze"):
                go_to("Analysis")
        with col2:
            if st.button("🏠 Back to Home"):
                go_to("Home")

# ==========================
# ABOUT PAGE
# ==========================
elif page == "About":

    st.title("📄 About BioScan")

    st.markdown("""
    BioScan is an AI-based diagnostic system that uses biomarker data to predict disease risk.

    ### 🔬 Model
    # FIX 7: Corrected model description from MLP to TabNet
    - TabNet (Attentive Tabular Learning)
    - Multi-class classification across 5 conditions
    - ROC-AUC evaluation

    ### 🎯 Goal
    Early detection and prevention of diseases.

    ### 🩺 Diseases Covered
    - Diabetes  
    - Anemia  
    - Hypertension  
    - Heart Disease  
    - Fit (Healthy)
    """)