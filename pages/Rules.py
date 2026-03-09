import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Decision Tree Rules", layout="wide")

# --- Custom CSS for Colors and Styling ---
st.markdown("""
<style>
    .rule-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 15px;
        color: white;
        margin: 10px 0;
        border-left: 5px solid #4ECDC4;
    }
    
    .rule-box-high {
        border-left: 5px solid #FF6B6B;
    }
    
    .title-style {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #FFE66D, #95E1D3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
    }
    
    .tree-level {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        color: white;
    }
    
    .condition-box {
        background: rgba(255,255,255,0.1);
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
        border-left: 4px solid #FFE66D;
    }
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<h1 class="title-style">📋 Decision Tree Rules 📋</h1>', unsafe_allow_html=True)

# --- Introduction ---
st.markdown("""
<div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 20px; color: white; text-align: center;">
    <h3>🤖 How the AI Model Makes Predictions</h3>
    <p>This page shows the exact decision rules used by the machine learning model to predict diabetes risk.
    The rules are derived from a decision tree trained on the Pima Indian Diabetes Dataset.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- Decision Tree Rules ---
st.markdown("<h2 style='color: #FF6B6B;'>🌳 Complete Decision Tree Rules</h2>", unsafe_allow_html=True)

# Root decision
st.markdown("""
<div class="tree-level">
    <h3>🔷 Step 1: Check BMI (Body Mass Index)</h3>
    <div class="condition-box">
        <strong>IF BMI is missing or unknown:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #4ECDC4, #44A08D); padding: 5px 10px; border-radius: 5px;"><strong>LOW RISK</strong></span>
    </div>
</div>
""", unsafe_allow_html=True)

# First split
st.markdown("""
<div class="tree-level">
    <h3>🔷 Step 2: BMI Threshold Check</h3>
    <div class="condition-box">
        <strong>IF BMI ≤ 26.92401:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #4ECDC4, #44A08D); padding: 5px 10px; border-radius: 5px;"><strong>LOW RISK</strong></span>
    </div>
    <div class="condition-box">
        <strong style="color: #FF6B6B;">IF BMI > 26.92401:</strong><br>
        ➜ Continue to Step 3
    </div>
</div>
""", unsafe_allow_html=True)

# Second split
st.markdown("""
<div class="tree-level">
    <h3>🔷 Step 3: Check Glucose Level (When BMI > 26.92401)</h3>
    <div class="condition-box">
        <strong>IF Glucose is missing or unknown:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #4ECDC4, #44A08D); padding: 5px 10px; border-radius: 5px;"><strong>LOW RISK</strong></span>
    </div>
    <div class="condition-box">
        <strong>IF Glucose ≤ 127.5 mg/dL:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #4ECDC4, #44A08D); padding: 5px 10px; border-radius: 5px;"><strong>LOW RISK</strong></span>
    </div>
    <div class="condition-box">
        <strong style="color: #FF6B6B;">IF Glucose > 127.5 mg/dL:</strong><br>
        ➜ Continue to Step 4
    </div>
</div>
""", unsafe_allow_html=True)

# Third split (final)
st.markdown("""
<div class="tree-level">
    <h3>🔷 Step 4: Check Age (When BMI > 26.92401 AND Glucose > 127.5)</h3>
    <div class="condition-box">
        <strong>IF Age is missing or unknown:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #4ECDC4, #44A08D); padding: 5px 10px; border-radius: 5px;"><strong>LOW RISK</strong></span>
    </div>
    <div class="condition-box">
        <strong style="color: #FF6B6B;">IF Age ≤ 28.5 years:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #FF6B6B, #ee5a6f); padding: 5px 10px; border-radius: 5px;"><strong>HIGH RISK ⚠️</strong></span>
    </div>
    <div class="condition-box">
        <strong style="color: #FF6B6B;">IF Age > 28.5 years:</strong><br>
        ➜ Result: <span style="background: linear-gradient(90deg, #FF6B6B, #ee5a6f); padding: 5px 10px; border-radius: 5px;"><strong>HIGH RISK ⚠️</strong></span>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- Key Thresholds ---
st.markdown("<h2 style='color: #FF6B6B;'>🎯 Key Decision Thresholds</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 20px; color: white; text-align: center;'>
        <h3>📏 BMI Threshold</h3>
        <h1 style='color: #FFE66D; margin: 10px 0;'>26.92</h1>
        <p>Critical boundary for initial risk assessment</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; padding: 20px; color: white; text-align: center;'>
        <h3>🩸 Glucose Threshold</h3>
        <h1 style='color: #FFE66D; margin: 10px 0;'>127.5</h1>
        <p>Blood sugar level boundary (mg/dL)</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #FF6B6B 0%, #ee5a6f 100%); border-radius: 10px; padding: 20px; color: white; text-align: center;'>
        <h3>🎂 Age Threshold</h3>
        <h1 style='color: #FFE66D; margin: 10px 0;'>28.5</h1>
        <p>Critical age milestone</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- Decision Matrix ---
st.markdown("<h2 style='color: #FF6B6B;'>📊 Decision Summary Table</h2>", unsafe_allow_html=True)

st.markdown("""
<table style='width: 100%; border-collapse: collapse;'>
    <tr style='background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white;'>
        <th style='padding: 12px; text-align: left;'>Condition</th>
        <th style='padding: 12px; text-align: left;'>Result</th>
    </tr>
    <tr style='background: #f0f0f0;'>
        <td style='padding: 12px; border-bottom: 1px solid #ddd;'><strong>BMI ≤ 26.92</strong></td>
        <td style='padding: 12px; border-bottom: 1px solid #ddd;'><span style='background: linear-gradient(90deg, #4ECDC4, #44A08D); color: white; padding: 5px 10px; border-radius: 5px;'><strong>LOW RISK ✅</strong></span></td>
    </tr>
    <tr>
        <td style='padding: 12px; border-bottom: 1px solid #ddd;'><strong>BMI > 26.92 AND Glucose ≤ 127.5</strong></td>
        <td style='padding: 12px; border-bottom: 1px solid #ddd;'><span style='background: linear-gradient(90deg, #4ECDC4, #44A08D); color: white; padding: 5px 10px; border-radius: 5px;'><strong>LOW RISK ✅</strong></span></td>
    </tr>
    <tr style='background: #f0f0f0;'>
        <td style='padding: 12px; border-bottom: 1px solid #ddd;'><strong>BMI > 26.92 AND Glucose > 127.5 AND Age ≤ 28.5</strong></td>
        <td style='padding: 12px; border-bottom: 1px solid #ddd;'><span style='background: linear-gradient(90deg, #FF6B6B, #ee5a6f); color: white; padding: 5px 10px; border-radius: 5px;'><strong>HIGH RISK ⚠️</strong></span></td>
    </tr>
    <tr>
        <td style='padding: 12px;'><strong>BMI > 26.92 AND Glucose > 127.5 AND Age > 28.5</strong></td>
        <td style='padding: 12px;'><span style='background: linear-gradient(90deg, #FF6B6B, #ee5a6f); color: white; padding: 5px 10px; border-radius: 5px;'><strong>HIGH RISK ⚠️</strong></span></td>
    </tr>
</table>
""", unsafe_allow_html=True)

st.divider()

# --- Important Information ---
st.markdown("""
<div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 20px; color: white;">
    <h3>ℹ️ How to Interpret These Rules</h3>
    <ul style='margin: 10px 0;'>
        <li><strong>The model uses a decision tree</strong> - It makes decisions by comparing values to specific thresholds</li>
        <li><strong>Rules are sequential</strong> - The model checks conditions in order, moving deeper into the tree</li>
        <li><strong>Only key features matter</strong> - BMI, Glucose, and Age are the primary decision factors</li>
        <li><strong>Threshold-based decisions</strong> - The exact thresholds were determined during model training</li>
        <li><strong>Missing data handled</strong> - If any critical value is missing, the model defaults to LOW RISK</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- Model Information ---
st.markdown("""
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; padding: 20px; color: white;">
    <h3>🔬 Model Details</h3>
    <ul style='margin: 10px 0;'>
        <li><strong>Model Type:</strong> Decision Tree Classifier</li>
        <li><strong>Dataset:</strong> Pima Indian Diabetes Dataset (UCI ML Repository)</li>
        <li><strong>Training Data:</strong> Females 21 years or older of Pima Indian heritage</li>
        <li><strong>Features Used:</strong> 7 health measurements</li>
        <li><strong>Tree Depth:</strong> 4 levels</li>
        <li><strong>Decision Path:</strong> BMI → Glucose → Age</li>
    </ul>
</div>
""", unsafe_allow_html=True)
