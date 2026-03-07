from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector", methods=["POST"]) 
def emotion_detector(): 
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    response['form-label'] dominant_emotion = response['dominant_emotion']

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()