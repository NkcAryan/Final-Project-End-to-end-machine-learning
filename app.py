
import streamlit as st
import joblib
import os

# Correct the model path to be relative to the app.py file
model_path = os.path.join(os.path.dirname(__file__), 'sms_spam_best_model.joblib')

# Load the trained model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Please make sure the model file is in the same directory as app.py.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

# Set up the Streamlit app title and description
st.title("SMS Spam Classifier")
st.write("Enter an SMS message below to classify it as Spam or Ham.")

# Create a text area for user input
message = st.text_area("Message", "Enter your message here...")

# Create a button to trigger the prediction
if st.button("Classify"):
    if message:
        # Make a prediction using the loaded model
        prediction = model.predict([message])[0]
        
        # Display the prediction
        st.subheader("Prediction:")
        if prediction == "spam":
            st.error("This message is classified as **Spam**.")
        else:
            st.success("This message is classified as **Ham**.")
    else:
        st.warning("Please enter a message to classify.")

