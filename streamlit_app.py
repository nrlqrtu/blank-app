import streamlit as st
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Streamlit app layout
st.title("Voice Recognition with Streamlit")

# Function to recognize speech
def recognize_voice():
    with sr.Microphone() as source:
        st.info("Please speak something...")
        audio_data = recognizer.listen(source)
        st.success("Recording complete! Processing...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from the service."

# Button to start voice recognition
if st.button("Start Voice Recognition"):
    result = recognize_voice()
    st.write("You said: ", result)
