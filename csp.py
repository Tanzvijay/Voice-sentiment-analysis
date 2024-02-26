import streamlit as st
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pydub import AudioSegment
import io
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

def main():
    st.title("Voice Sentiment Analysis")

    audio_input = st.radio("Select Input Source", ("Microphone", "Upload Audio File"))

    # Initialize the SpeechRecognition recognizer
    recognizer = sr.Recognizer()

    if audio_input == "Microphone":
        with st.spinner("Clearing background noise..."):
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
            st.success("Background noise cleared.")

        st.write("Say something:")

        if st.button("Start Recording"):
            with st.spinner("Recording..."):
                recorded_audio = recognize_speech(recognizer)
                if recorded_audio:
                    st.success("Done recording.")
                    sentiment = perform_sentiment_analysis(recorded_audio)
                    st.write(f"Your message: {recorded_audio}")
                    st.write(f"Sentiment Analysis: {sentiment}")

                    # Plot sentiment scores
                    plot_sentiment(sentiment)

    else:  # Upload Audio File
        uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])
        if uploaded_file:
            with st.spinner("Processing uploaded file..."):
                audio_bytes = uploaded_file.read()
                # Convert MP3 to WAV format (assuming it's stereo, you can adjust channels=1 if it's mono)
                wav_audio = AudioSegment.from_mp3(io.BytesIO(audio_bytes)).set_channels(1).set_frame_rate(16000)
                wav_audio.export("temp.wav", format="wav")

                with st.spinner("Transcribing uploaded audio..."):
                    audio_text = recognize_audio_from_wav(recognizer, "temp.wav")

                if audio_text:
                    sentiment = perform_sentiment_analysis(audio_text)
                    st.write(f"Transcription from uploaded audio: {audio_text}")
                    st.write(f"Sentiment Analysis: {sentiment}")

                    # Plot sentiment scores
                    plot_sentiment(sentiment)

def recognize_speech(recognizer):
    try:
        with sr.Microphone() as source:
            recorded_audio = recognizer.listen(source)
        return recognizer.recognize_google(recorded_audio, language="en-US")
    except Exception as ex:
        st.error(f"Error: {ex}")
        return None

def recognize_audio_from_wav(recognizer, audio_path):
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language="en-US")
    except Exception as ex:
        st.error(f"Error: {ex}")
        return None

def perform_sentiment_analysis(text):
    analyser = SentimentIntensityAnalyzer()
    vader_scores = analyser.polarity_scores(text)
    return vader_scores

def plot_sentiment(sentiment):
    labels = sentiment.keys()
    values = [sentiment[label] for label in labels]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel("Sentiment Categories")
    ax.set_ylabel("Sentiment Scores")
    ax.set_title("Sentiment Analysis")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
