import requests
import json 

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response_data = json.loads(response.text)
    emotion_predictions = response_data.get("emotionPredictions", [])
    if not emotion_predictions:
        return {"error": "No emotion predictions found"}

    emotion_scores = emotion_predictions[0].get("emotion", {})
    
    # Extract individual scores
    anger_score = emotion_scores.get('anger', 0)
    disgust_score = emotion_scores.get('disgust', 0)
    fear_score = emotion_scores.get('fear', 0)
    joy_score = emotion_scores.get('joy', 0)
    sadness_score = emotion_scores.get('sadness', 0)
    
    # Determine the dominant emotion
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
