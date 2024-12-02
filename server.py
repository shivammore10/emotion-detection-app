from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Extract the input statement from the request JSON
    data = request.get_json()
    text_to_analyze = data.get('statement', '')

    if not text_to_analyze:
        return jsonify({"error": "No statement provided"}), 400

    result = emotion_detector(text_to_analyze) # Use the emotion_detector function

    # Format the response
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    
    return jsonify({"response": response_message}), 200

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
