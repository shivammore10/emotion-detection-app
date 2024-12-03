"""
Flask application for emotion detection using Watson NLP.
"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint for detecting emotions in a given statement.
    Accepts a JSON payload with a 'statement' key and returns
    the emotion analysis result.
    """
    data = request.get_json()
    text_to_analyze = data.get('statement', '')

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_message}), 200

if __name__ == '__main__':
    app.run(debug=True)
