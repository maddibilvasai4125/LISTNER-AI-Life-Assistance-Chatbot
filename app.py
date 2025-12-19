from flask import Flask, request, render_template, jsonify
from ibm_watson import AssistantV2, NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from twilio.rest import Client
from googleapiclient.discovery import build 
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask_cors import CORS
from ibm_watson import SpeechToTextV1
import speech_recognition as sr
from ibm_watson.websocket import RecognizeCallback, AudioSource 
 

app = Flask(__name__)
CORS(app)


   
 

# Set up Spotify API credentials
spotify_client_id = '**'
spotify_client_secret = '**'
spotify_client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
spotify = spotipy.Spotify(client_credentials_manager=spotify_client_credentials_manager)




 
# Set up YouTube API credentials
youtube_api_key = '**'
youtube = build('youtube', 'v3', developerKey=youtube_api_key)




# Set up Watson Assistant credentials
watson_apikey = '**'
watson_url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/9ec8db12-700e-4609-9219-bb7b7dedca69'
watson_assistant_id = '**'
authenticator = IAMAuthenticator(watson_apikey)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(watson_url)



nlu_apikey = '**'
nlu_url = 'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/ea57ac5d-afd5-4346-8924-8468858bdf55'
nlu_authenticator = IAMAuthenticator(nlu_apikey)
nlu = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=nlu_authenticator
)
nlu.set_service_url(nlu_url)












# Twilio credentials
twilio_account_sid = '**'
twilio_auth_token = '**'
twilio_phone_number = '**'
recipient_phone_number = '**'
twilio_client = Client(twilio_account_sid, twilio_auth_token)

# Dictionary to store user sessions
user_sessions = {}







 


 















 



# Home route to render the chat interface
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')

 

@app.route('/get_hospitals')
def get_hospitals():
    location = request.args.get('location')
    radius =  request.args.get('radius')
    API_KEY = '**'

    api_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': location,
        'radius': 10000,
        'type': 'hospital',
        'key': API_KEY,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/get_police_stations')
def get_police_stations():
    location = request.args.get('location')
    radius = request.args.get('radius')
    API_KEY = '**'  # Replace with your actual API key

    api_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': location,
        'radius': 10000,
        'type': 'police',
        'key': API_KEY,
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500

 




 
























  
# Function to fetch YouTube video recommendations based on user input
def fetch_youtube_recommendations(query):
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id',
        maxResults=5
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
    video_recommendations = []

    for video_id in video_ids:
        video_url = f'https://www.youtube.com/embed/{video_id}'
        video_recommendations.append(video_url)

    return video_recommendations

 





 


# Function to fetch music recommendations from Spotify
def fetch_spotify_recommendations(query):
    results = spotify.search(q=query, type='track', limit=5)
    
    track_recommendations = []
    for track in results['tracks']['items']:
        track_info = {
            'name': track['name'],
            'artists': ', '.join([artist['name'] for artist in track['artists']]),
            'preview_url': track['preview_url']
        }
        track_recommendations.append(track_info)
    
    return track_recommendations





# Chat route to handle user input and respond using Watson Assistant
@app.route('/chat', methods=['POST'])
def chat():
 
    user_input = request.form['user_input']
    session_id = get_or_create_session()
     

     
    
     


    # Call Watson Assistant to get a response
      
    response = assistant.message(
        assistant_id=watson_assistant_id,
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': user_input
        }
    ).get_result()
      
    reply = "I'm sorry, but I couldn't understand your request."
    
    
   

    if 'output' in response and 'generic' in response['output'] and response['output']['generic']:
        reply = response['output']['generic'][0]['text']





    # Analyze sentiment using Watson NLU API
    sentiment = analyze_sentiment(user_input)
    # Implement NLU API call and sentiment analysis here


     

    # Send emergency alert if necessary
    if 'emergency' in reply.lower() or sentiment == 'Negative':
        send_emergency_alert()

     
    # Fetch Spotify music recommendations based on user input
    spotify_recommendations = fetch_spotify_recommendations(user_input)

     
      



    # Fetch YouTube video recommendations based on user input
    youtube_recommendations = fetch_youtube_recommendations(user_input)

    return jsonify({'reply': reply, 'sentiment': sentiment, 'youtube_recommendations': youtube_recommendations,  'spotify_recommendations': spotify_recommendations })




# Function to analyze sentiment using Watson NLU API
def analyze_sentiment(text):
 # Check if the text is too short for sentiment analysis
    if len(text) < 5:  # Adjust the threshold as needed
        return "Neutral"  # Return a default sentiment


    response = nlu.analyze(
        text=text,
        features=Features(sentiment=SentimentOptions())
    ).get_result()
    sentiment = response['sentiment']['document']['label']
    
    return sentiment

     




# Function to send emergency alert via Twilio
def send_emergency_alert():
    message = twilio_client.messages.create(
        body='Emergency: Domestic violence situation detected!',
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"Emergency alert sent! SID: {message.sid}")

# Function to get or create a user session
def get_or_create_session():
    if 'session_id' not in user_sessions:
        response = assistant.create_session(assistant_id=watson_assistant_id).get_result()
        user_sessions['session_id'] = response['session_id']
    return user_sessions['session_id']





 




if __name__ == '__main__':
    app.run( )

