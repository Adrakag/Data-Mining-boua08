import streamlit as st

# --- Provided Prediction Function ---
def predict_diabetes(glucose=None, blood_pressure=None, skinfold=None, insulin=None, bmi=None, diabetes_pedigree=None, age=None):
    """ 
    Predictor for Diabetes from model/67bc2fe854e70fb808f13db3
    """
    # (Insert the full nested if/else logic from your BigML.txt file here)
    # Example structure:
    if (bmi is None):
        return 'false'
    if (bmi > 26.92401):
        if (glucose is None):
            return 'false'
        # ... remainder of the provided decision tree code ...
        return 'false' 

# --- User Interface & Input Validation ---
st.title("Diabetes Risk Assessment Tool")
st.markdown("Based on health data from females 21 years or older of Pima Indian heritage. Source: UCI Machine Learning Repository.")

st.header("Patient Vitals")

# Using Streamlit's number_input for built-in validation (setting realistic min/max ranges)
col1, col2 = st.columns(2)

with col1:
    glucose = st.number_input("Glucose level", min_value=0.0, max_value=300.0, value=100.0, step=1.0)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
    skinfold = st.number_input("Skinfold Thickness (mm)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
    insulin = st.number_input("Insulin level (IU/mL)", min_value=0.0, max_value=900.0, value=79.0, step=1.0)

with col2:
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.000, max_value=3.000, value=0.500, step=0.001)
    # Validation ensures age is at least 21, matching the dataset constraints
    age = st.number_input("Age (years)", min_value=21, max_value=120, value=25, step=1) 

# --- User-Friendly Output ---
if st.button("Calculate Risk"):
    prediction = predict_diabetes(glucose, blood_pressure, skinfold, insulin, bmi, diabetes_pedigree, age)
    
    st.divider()
    if prediction == 'true':
        st.error("⚠️ **Assessment Result: High Risk of Diabetes**")
        st.write("Please consult with a healthcare professional for a formal medical evaluation.")
    else:
        st.success("✅ **Assessment Result: Low Risk of Diabetes**")
        st.write("Continue maintaining a healthy lifestyle. This is a preliminary assessment, not a medical diagnosis.")