import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Diabetes Risk Assessment", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for Colors and Styling ---
st.markdown("""
<style>
    /* Main background and text colors */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Title styling */
    .title-style {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #FFE66D, #95E1D3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
    }
    
    /* Input containers with gradient */
    .input-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #FF6B6B 0%, #FFE66D 50%, #4ECDC4 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 16px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
    }
    
    /* Metric styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Result boxes */
    .result-high-risk {
        background: linear-gradient(135deg, #FF6B6B 0%, #ee5a6f 100%);
        border-left: 5px solid #FF6B6B;
    }
    
    .result-low-risk {
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        border-left: 5px solid #4ECDC4;
    }
</style>
""", unsafe_allow_html=True)

# --- Provided Prediction Function ---
def predict_diabetes(glucose=None, blood_pressure=None, skinfold=None, insulin=None, bmi=None, diabetes_pedigree=None, age=None):
    """ 
    Predictor for Diabetes from model/67bc2fe854e70fb808f13db3
    """
    if (bmi is None):
        return 'false'
    if (bmi > 26.92401):
        if (glucose is None):
            return 'false'
        if (glucose > 127.5):
            if (age is None):
                return 'false'
            if (age <= 28.5):
                return 'true'
            if (age > 28.5):
                return 'true'
        if (glucose <= 127.5):
            return 'false'
    if (bmi <= 26.92401):
        return 'false'
    return 'false'

# --- Title with Colorful Gradient ---
st.markdown('<h1 class="title-style">🏥 Diabetes Risk Assessment Tool 🏥</h1>', unsafe_allow_html=True)

# --- Description with colored background ---
st.markdown("""
<div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 20px; color: white; text-align: center;">
    <h3>💉 Powered by Machine Learning</h3>
    <p>Based on health data from females 21 years or older of Pima Indian heritage.<br>
    <strong>Source:</strong> UCI Machine Learning Repository</p>
</div>
""", unsafe_allow_html=True)

st.write("")  # Spacing

# --- Patient Vitals Input Section ---
st.markdown("<h2 style='color: #FF6B6B;'>📊 Enter Your Patient Vitals</h2>", unsafe_allow_html=True)

# Using columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 20px; color: white;'><h3>🩺 Physical Measurements</h3></div>", unsafe_allow_html=True)
    glucose = st.number_input("🔹 Glucose level (mg/dL)", min_value=0.0, max_value=300.0, value=100.0, step=1.0)
    blood_pressure = st.number_input("🔹 Blood Pressure (mm Hg)", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
    skinfold = st.number_input("🔹 Skinfold Thickness (mm)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
    insulin = st.number_input("🔹 Insulin level (IU/mL)", min_value=0.0, max_value=900.0, value=79.0, step=1.0)

with col2:
    st.markdown("<div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; padding: 20px; color: white;'><h3>⚖️ Metrics & History</h3></div>", unsafe_allow_html=True)
    bmi = st.number_input("🔹 BMI (Body Mass Index)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
    diabetes_pedigree = st.number_input("🔹 Diabetes Pedigree Function", min_value=0.000, max_value=3.000, value=0.500, step=0.001)
    age = st.number_input("🔹 Age (years)", min_value=21, max_value=120, value=25, step=1)

st.write("")  # Spacing

# --- Calculate Risk Button ---
col_button_left, col_button_center, col_button_right = st.columns([1, 1, 1])
with col_button_center:
    calculate_btn = st.button("🎯 Calculate Diabetes Risk", use_container_width=True)

# --- Results Section ---
if calculate_btn:
    prediction = predict_diabetes(glucose, blood_pressure, skinfold, insulin, bmi, diabetes_pedigree, age)
    
    st.divider()
    
    # Create result visualization
    col_result1, col_result2 = st.columns([1, 2])
    
    with col_result1:
        if prediction == 'true':
            st.markdown("""
            <div style='background: linear-gradient(135deg, #FF6B6B 0%, #ee5a6f 100%); border-radius: 15px; padding: 30px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.2);'>
                <h1 style='font-size: 60px; margin: 0;'>⚠️</h1>
                <h2 style='margin: 10px 0;'>HIGH RISK</h2>
                <p style='font-size: 18px; margin: 0;'>Diabetes Risk Detected</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%); border-radius: 15px; padding: 30px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.2);'>
                <h1 style='font-size: 60px; margin: 0;'>✅</h1>
                <h2 style='margin: 10px 0;'>LOW RISK</h2>
                <p style='font-size: 18px; margin: 0;'>Healthy Profile Detected</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col_result2:
        if prediction == 'true':
            st.markdown("""
            <div style='background: linear-gradient(135deg, #FF6B6B 0%, #ee5a6f 100%); border-radius: 15px; padding: 20px; color: white;'>
                <h3>Assessment Result</h3>
                <p style='font-size: 16px;'><strong>⚠️ High Risk of Diabetes</strong></p>
                <p>Based on the provided health measurements, the AI model indicates a higher risk of diabetes.</p>
                <p style='margin-top: 15px; font-weight: bold;'>Recommendations:</p>
                <ul style='margin: 10px 0;'>
                    <li>Please consult with a healthcare professional immediately</li>
                    <li>Request a formal medical evaluation</li>
                    <li>Consider lifestyle modifications</li>
                    <li>Increase physical activity and improve diet</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%); border-radius: 15px; padding: 20px; color: white;'>
                <h3>Assessment Result</h3>
                <p style='font-size: 16px;'><strong>✅ Low Risk of Diabetes</strong></p>
                <p>Based on the provided health measurements, the AI model indicates a lower risk of diabetes.</p>
                <p style='margin-top: 15px; font-weight: bold;'>Recommendations:</p>
                <ul style='margin: 10px 0;'>
                    <li>Continue maintaining your healthy lifestyle</li>
                    <li>Regular exercise and balanced diet</li>
                    <li>Schedule periodic health check-ups</li>
                    <li>This is a preliminary assessment, not a medical diagnosis</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# --- Footer with important information ---
st.divider()
st.markdown("""
<div style='background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 15px; color: white; text-align: center;'>
    <p><strong>⚕️ Disclaimer:</strong> This tool is for educational purposes only and should not replace professional medical advice. 
    Always consult a qualified healthcare provider for accurate diagnosis and treatment.</p>
</div>
""", unsafe_allow_html=True)