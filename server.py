"""Web app used to determine scores for different emotions"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """The function analyzes entered text to determine scores for different emotions"""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = emotions['dominant_emotion']
    if dominant_emotion is None:
        response = "Invalid text! Please try again!"
    else:
        response = f"""For the given statement, the system response is 'anger': {anger},
         'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. The dominant
          emotion is <strong>{dominant_emotion}</strong>."""
    return response

@app.route("/")
def render_index_page():
    """The function starts the web app"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
