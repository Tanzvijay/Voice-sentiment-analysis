Voice Sentiment Analysis using Streamlit
This Python script provides a simple web application for performing sentiment analysis on voice inputs. It utilizes Streamlit for the user interface, SpeechRecognition for transcribing speech from microphone or uploaded audio files, VADER Sentiment Analysis for sentiment analysis, and Pydub for audio file processing.

Features:
Microphone Input: Allows users to record their voice using a microphone and analyze the sentiment of their speech.
Upload Audio File: Enables users to upload an MP3 audio file for sentiment analysis.
Real-time Sentiment Analysis: Provides instant sentiment analysis results after recording or uploading audio.
Visualization: Visualizes sentiment scores using Matplotlib for better understanding.
How to Use:
Install the required dependencies mentioned in requirements.txt.
Run the script using streamlit run voice_sentiment_analysis.py.
Choose between microphone or upload options.
Record speech or upload an MP3 file.
View sentiment analysis results.
Dependencies:
streamlit
speech_recognition
vaderSentiment
pydub
matplotlib
Usage:
Clone the repository.
Install dependencies using pip install -r requirements.txt.
Run the script using streamlit run voice_sentiment_analysis.py.
Contributing:
Contributions are welcome! Feel free to open issues or pull requests.
