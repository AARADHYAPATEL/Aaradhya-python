import streamlit as st
from transformers import pipeline
import cv2
import mediapipe as mp
import pyttsx3
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

tf.compat.v1.reset_default_graph()

# Voice engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice
except Exception as e:
    st.error(f"Error initializing text-to-speech engine: {e}")

# NLP Assistant using Hugging Face
@st.cache
def get_nlp_pipeline():
    return pipeline("text-generation", model="gpt2")


nlp = get_nlp_pipeline()

# Streamlit UI
st.title("Advanced AI Companion (No OpenAI) 🚀")
st.write("This AI can assist with NLP, computer vision, and automation tasks!")

# Tabbed interface
tab1, tab2, tab3 = st.tabs(["📚 NLP Assistant", "🔍 Computer Vision", "📊 Analytics & Automation"])

# NLP Assistant
with tab1:
    st.header("Your Text Assistant")
    user_input = st.text_input("Ask me anything or give a task!")
    if user_input:
        with st.spinner("Thinking..."):
            response = nlp(user_input, max_length=100, num_return_sequences=1)
            st.write(f"**AI Response:** {response[0]['generated_text']}")

        # Voice feedback
        if st.checkbox("Read response aloud"):
            engine.say(response[0]['generated_text'])
            engine.runAndWait()

# Computer Vision
with tab2:
    st.header("Real-Time Object Recognition")
    st.write("Click 'Start' to enable the camera and identify objects in real-time.")
    if st.button("Start"):
        cap = cv2.VideoCapture(0)
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            try:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Failed to capture image")
                        break

                    # Convert frame to RGB for MediaPipe
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = pose.process(rgb_frame)

                    # Draw pose annotations
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                    cv2.imshow("AI Vision", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            finally:
                cap.release()
                cv2.destroyAllWindows()

# Analytics and Automation
with tab3:
    st.header("Data Insights & Tools")
    st.write("Upload a CSV file for analysis or generate tasks based on your needs.")

    uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("**Preview of Data:**", df.head())

        # Visualization
        st.write("**Select a column for visualization:**")
        column = st.selectbox("Choose a column", df.columns)
        if column:
            try:
                if pd.api.types.is_numeric_dtype(df[column]):
                    plt.figure(figsize=(10, 6))
                    df[column].hist()
                    st.pyplot(plt)
                else:
                    st.error("Selected column is not numeric.")
            except Exception as e:
                st.error(f"Error plotting histogram: {e}")

    st.write("**Automation Tasks:**")
    task = st.text_input("Describe your automation needs:")
    if task:
        st.write("Performing your automation...")
        st.success("Task executed (simulate the action).")
