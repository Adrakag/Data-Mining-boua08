import streamlit as st
import json
import urllib.request
import urllib.error

# Azure endpoint configuration - edit these variables as needed
AZURE_URL = "https://ziz176-boua08-mzjnr.polandcentral.inference.ml.azure.com/score"  # Replace with your actual Azure ML endpoint URL
AZURE_KEY = "sGl0utMTB7kLPVAtS6pjrQtZvrHVhuPxVNUX61W6sLKmvj9dMbdzJQQJ99CEAAAAAAAAAAAAINFRAZML3A5U"  # Replace with your actual Azure API key

# Set page configuration for wide layout
st.set_page_config(layout="wide", page_title="Climate News Virality Predictor")

# Title and description
st.title("🌍 Climate News Virality Predictor")
st.markdown("""
This application predicts whether a climate news article will become popular based on its metadata features.
Input the article details below and click **Predict Popularity** to get the prediction.
""")

# Organize inputs into three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("⏰ Time & Date")
    
    publication_hour = st.slider("Publication Hour", min_value=0, max_value=23, value=12, help="Hour of publication (0-23)")
    
    weekday_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_label = st.selectbox("Weekday", weekday_options, index=0, help="Day of the week")
    weekday_num = weekday_options.index(weekday_label)  # Convert to 0-6
    
    # Automatically determine if it's weekend based on weekday_num
    is_weekend = weekday_num >= 5  # Saturday (5) and Sunday (6) are weekends
    st.checkbox("Is Weekend", value=is_weekend, disabled=True, help="Automatically set based on weekday")

with col2:
    st.subheader("📄 Content Features")
    
    has_author = st.checkbox("Has Author", help="Does the article have an author?")
    has_image = st.checkbox("Has Image", help="Does the article have an image?")
    has_description = st.checkbox("Has Description", help="Does the article have a description?")

with col3:
    st.subheader("📊 Text Metrics")
    
    title_length_chars = st.number_input("Title Length (Characters)", min_value=0, value=50, step=1, help="Number of characters in the title")
    title_word_count = st.number_input("Title Word Count", min_value=0, value=10, step=1, help="Number of words in the title")
    description_length_chars = st.number_input("Description Length (Characters)", min_value=0, value=100, step=1, help="Number of characters in the description")
    description_word_count = st.number_input("Description Word Count", min_value=0, value=20, step=1, help="Number of words in the description")
    title_has_number = st.checkbox("Title Has Number", help="Does the title contain a number?")
    title_has_question = st.checkbox("Title Has Question", help="Does the title contain a question mark?")
    title_has_colon = st.checkbox("Title Has Colon", help="Does the title contain a colon?")

# Predict button and logic
if st.button("🔮 Predict Popularity", type="primary", use_container_width=True):
    # Gather inputs into array in exact order
    input_array = [
        publication_hour,
        weekday_num,
        int(is_weekend),  # Convert boolean to int (0 or 1)
        int(has_author),
        int(has_image),
        int(has_description),
        title_length_chars,
        title_word_count,
        description_length_chars,
        description_word_count,
        int(title_has_number),
        int(title_has_question),
        int(title_has_colon)
    ]
    
    # Prepare JSON payload
    columns = [
        "publication_hour", "weekday_num", "is_weekend", "has_author", "has_image", "has_description",
        "title_length_chars", "title_word_count", "description_length_chars", "description_word_count",
        "title_has_number", "title_has_question", "title_has_colon"
    ]
    
    data = {
        "input_data": {
            "columns": columns,
            "index": [0],
            "data": [input_array]
        },
        "params": {}
    }
    
    # Package the data and add your secret key to the headers
    body = str.encode(json.dumps(data))
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': ('Bearer ' + AZURE_KEY)
    }
    req = urllib.request.Request(AZURE_URL, body, headers)
    
    # Send the request to Azure and display the answer
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        prediction_str = result.decode("utf8")
        st.success(f"Success! Model Prediction: {prediction_str}")
        
        # Parse the prediction for user-friendly message
        prediction = json.loads(prediction_str)[0]
        if prediction == 1:
            st.success("🔥 Prediction: This article will likely be POPULAR!")
        else:
            st.warning("🧊 Prediction: This article will likely NOT be popular.")
    except urllib.error.HTTPError as error:
        st.error(f"The request failed with status code: {error.code}")
        st.error(error.read().decode("utf8", 'ignore'))
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")