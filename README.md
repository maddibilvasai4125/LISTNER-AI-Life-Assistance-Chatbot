# 🤖 LISTNER - AI-Based Life Assistance Chatbot

<div align="center">

![LISTNER Banner](https://img.shields.io/badge/LISTNER-AI%20Life%20Assistance-purple?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![IBM Watson](https://img.shields.io/badge/IBM-Watson-blue?style=for-the-badge&logo=ibm)](https://www.ibm.com/watson)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-orange?style=for-the-badge&logo=openai)](https://openai.com/)

**"Your dedicated wellness companion, offering guidance and support for career, mental health, domestic violence, and emergencies. Harness AI-driven assistance for a brighter life."**

[Features](#-key-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Team](#-team)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [API Integrations](#-api-integrations)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Team](#-team)
- [License](#-license)

---

## 🌟 Overview

**LISTNER** is an AI-powered life assistance chatbot designed to provide comprehensive support in critical areas affecting public welfare. Built with cutting-edge technologies including IBM Watson, OpenAI GPT, and advanced NLP techniques, LISTNER offers empathetic, personalized assistance for:

- 🆘 **Women's Safety & Domestic Violence Prevention**
- 🧠 **Mental Health Support & Counseling**
- 💼 **Career Guidance & Path Recommendations**
- 🚨 **Emergency Response & Location-Based Assistance**
- 🛡️ **Scam Detection & Prevention**

### 🎯 Project Highlights

- **Multi-channel Support**: WhatsApp, Telegram, and Web Interface
- **Intelligent Sentiment Analysis**: Understands user emotions for personalized responses
- **Real-time Emergency Assistance**: Location-based police station and hospital finder
- **Discreet SOS Escalation**: Silent alert system via Twilio
- **Content Recommendations**: YouTube videos and Spotify playlists for mental wellness
- **Voice Input Support**: Speech-to-text translation for accessibility

---

## 🎯 Problem Statement

In today's fast-paced world, individuals face numerous challenges:

- **Limited Access to Support**: Difficulty finding immediate help for mental health, domestic violence, or career guidance
- **Privacy Concerns**: Fear of judgment prevents people from seeking help
- **Emergency Response Delays**: Slow access to emergency services during critical situations
- **Information Overload**: Overwhelming amount of resources without personalized guidance

**LISTNER addresses these challenges** by providing a 24/7 AI companion that offers confidential, empathetic, and immediate support across multiple domains.

---

## ✨ Key Features

### 🔐 Safety & Emergency

- **Discreet SOS System**: Silent emergency alerts via Twilio SMS/calls
- **Location-Based Services**: 
  - Find nearest police stations with navigation
  - Locate nearby hospitals instantly
  - Emergency contact quick access
- **Domestic Violence Resources**: Safety tips, helpline numbers, and prevention strategies

### 🧠 Mental Health & Wellness

- **Empathetic Counseling**: AI-powered mental health support
- **Sentiment Analysis**: Detects emotional state and provides appropriate responses
- **Stress Management**: Personalized tips and mindfulness exercises
- **Content Therapy**: Curated YouTube videos and Spotify playlists

### 💼 Career Development

- **Intelligent Career Guidance**: Recommendations based on skills, interests, and qualifications
- **Skill Assessment**: Analyze your strengths and suggest career paths
- **Resource Recommendations**: Educational content and learning materials

### 🎙️ Accessibility Features

- **Voice Input**: Speech-to-text for hands-free interaction
- **Multi-language Support**: Communicates in multiple languages
- **Cross-Platform**: Web, WhatsApp, and Telegram integration

---

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **Python 3.8+** - Core programming language
- **IBM Watson** - AI and NLP capabilities
- **OpenAI GPT** - Advanced language understanding

### AI & NLP
- **NLTK** - Natural Language Toolkit for text processing
- **Sentiment Analysis** - Emotion detection algorithms
- **Speech Recognition** - Voice-to-text conversion

### Integrations
- **Twilio** - Emergency SMS/call notifications
- **YouTube API** - Video recommendations
- **Spotify API** - Music therapy playlists
- **Google Maps API** - Location services
- **WhatsApp Business API** - Messaging platform
- **Telegram Bot API** - Chat integration

### Frontend
- **HTML5/CSS3** - Modern web interface
- **JavaScript** - Interactive elements
- **Bootstrap** - Responsive design

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User Interfaces                        │
│          (Web App │ WhatsApp │ Telegram │ Voice)            │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Flask Backend Server                      │
│  ┌────────────┐  ┌──────────┐  ┌─────────────────────┐      │
│  │  Routing   │  │  Session │  │  Request Handler    │      │
│  └────────────┘  └──────────┘  └─────────────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   AI Processing Layer                       │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐     │
│  │ IBM Watson  │  │  OpenAI GPT │  │Sentiment Analysis│     │
│  └─────────────┘  └─────────────┘  └──────────────────┘     │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│              External Services & APIs                       │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐  ┌──────────┐    │
│  │  Twilio  │  │ YouTube   │  │ Spotify  │  │  Maps    │    │
│  └──────────┘  └───────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- API keys for: OpenAI, Twilio, YouTube, Spotify, Google Maps

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/LISTNER-AI-Life-Assistance-Chatbot.git
cd LISTNER-AI-Life-Assistance-Chatbot
```

### Step 2: Create Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory:

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# OpenAI API
OPENAI_API_KEY=your-openai-api-key

# IBM Watson
WATSON_API_KEY=your-watson-api-key
WATSON_URL=your-watson-url

# Twilio Configuration
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=your-twilio-phone-number

# YouTube API
YOUTUBE_API_KEY=your-youtube-api-key

# Spotify API
SPOTIFY_CLIENT_ID=your-spotify-client-id
SPOTIFY_CLIENT_SECRET=your-spotify-client-secret

# Google Maps API
GOOGLE_MAPS_API_KEY=your-google-maps-api-key

# WhatsApp/Telegram (Optional)
WHATSAPP_API_KEY=your-whatsapp-api-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

---

## ⚙️ Configuration

### Database Setup (if applicable)

```bash
# Initialize database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Configure Emergency Contacts

Edit `config/emergency_contacts.json`:

```json
{
  "police": "100",
  "ambulance": "102",
  "women_helpline": "1091",
  "mental_health_helpline": "9152987821"
}
```

---

## 💻 Usage

### Running the Application

```bash
# Activate virtual environment first
source venv/bin/activate  # On macOS/Linux

# Run Flask app
python app.py
```

The application will be available at: `http://localhost:5000`

### Accessing Different Interfaces

1. **Web Interface**: Navigate to `http://localhost:5000`
2. **WhatsApp**: Send a message to your configured WhatsApp Business number
3. **Telegram**: Search for your bot using the bot token
4. **Voice Input**: Click the microphone icon in the web interface

### Example Interactions

```
User: "I need help, I'm in danger"
LISTNER: "I'm really sorry to hear that you're in such a difficult 
situation. Your safety is the top priority. If you're in immediate 
danger in India, please call the emergency number 100 for police 
assistance or 112 for general emergencies."

User: "I'm feeling very stressed about my career"
LISTNER: "I understand career stress can be overwhelming. Let's talk 
about it. What specifically is causing you stress? Your skills, job 
search, or career direction? I'm here to help you navigate this."

User: "Find nearest police station"
LISTNER: [Displays map with 5 nearest police stations with navigation links]
```

---

## 📸 Screenshots

### 🎬 Video Demo

<div align="center">

[![LISTNER Demo Video](https://img.youtube.com/vi/g6QMIEdkbSw/maxresdefault.jpg)](https://youtu.be/g6QMIEdkbSw)

**[▶️ Watch Full Demo on YouTube](https://youtu.be/g6QMIEdkbSw)**

*Experience LISTNER in action - See how AI-powered assistance helps users in real-time*

</div>

---

### 🏠 Home Page - Landing Experience

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 125124.png" alt="LISTNER Home Page " width="800"/>

*Beautiful landing page with clear value proposition and call-to-action*
</div>

**Features Highlighted:**
- Modern purple gradient design with engaging visuals
- Clear navigation: Home, Life Assistance, Services, Contact Us
- Prominent "CHAT NOW!" button for immediate access
- Compelling tagline: "Your dedicated wellness aid, offering guidance and support"

---

### 💬 Chat Interface - AI Conversation

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 124439.png" alt="Police Stations" width="800"/>
<img src="screenshots/Screenshot 2023-09-04 124532.png" alt="Chat Interface" width="800"/>


*Interactive chatbot with real-time sentiment analysis and empathetic responses*
</div>

**Key Features:**
- **Sentiment Analysis Display**: Shows user's emotional state (negative/positive)
- **Empathetic Responses**: AI detects distress and provides appropriate support
- **Emergency Recognition**: Instantly identifies danger keywords
- **Voice Input**: "Start Recording" button for speech-to-text
- **Quick Action Buttons**: Emergency, Chat, Violence shortcuts

---

### 🆘 Emergency Services - Location-Based Help

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 125530.png" alt="About Section" width="800"/>


**Hospital Locator**

<img src="screenshots/Screenshot 2023-09-04 125205.png" alt="Hospitals" width="800"/>

*Location-based emergency services with one-click navigation*
</div>

**Emergency Features:**
- **Real-time Location Detection**: Finds nearest help based on user location
- **Direct Navigation**: One-click "Navigate" buttons to Google Maps
- **Comprehensive Listings**: 5+ nearest police stations and hospitals
- **Complete Addresses**: Full contact information and directions
- **Emergency Contacts**: Quick access to helpline numbers

---

### 🎵 Media Recommendations - Wellness Content

<div align="center">

**YouTube Video &Spotify Music Recommendations**

<img src="screenshots/Screenshot 2023-09-04 124532.png" alt="Chat Interface" width="800"/>

**Content Features:**
- **Context-Aware Suggestions**: Videos/music matched to user's situation
- **Mental Wellness Focus**: Calming and supportive content
- **Embedded Players**: Watch/listen directly within the interface
- **Curated Playlists**: Pre-selected content for different emotional states

---

### 🏥 Emergency Resources Hub

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 125322.png" alt="Emergency Hub" width="800"/>

*Centralized emergency resource center with multiple assistance options*
</div>

**Available Services:**
- Find Nearest Police Stations
- Find Nearest Hospitals
- Emergency Contacts Button
- Mental Health Resources
- Career Guidance Access

---

### 🎯 Services Overview

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 125414.png" alt="Services Page" width="800"/>

*Comprehensive service catalog with clear descriptions*
</div>

**Our Services:**
- **Career Paths**: Personalized career recommendations based on skills
- **Safety Measures**: Domestic violence prevention and safety tips
- **Emergency Resources**: Alert systems and helpline numbers
- **Mental Well-being**: Stress management and mindfulness support

---

### 📞 About Us & Contact

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 125322.png" alt="Emergency Hub" width="800"/>
*Team information and mission statement*
</div>

**About Team @Back_Benchers:**
- Innovation-driven team from G. Pulla Reddy Engineering College
- Award-winning at Smart India Hackathon
- Committed to solving real-world problems through AI
- Passionate about public welfare and safety

---

### 🎨 User Interface Highlights

| Feature | Description | Screenshot |
|---------|-------------|------------|
| **Sentiment Detection** | Real-time emotion analysis | `Screenshot 2023-09-04 124532.png` |
| **Emergency Buttons** | Quick access to critical services | `Screenshot 2023-09-04 125608.png` |
| **Location Services** | GPS-based resource finder | `Screenshot 2023-09-04 125205.png` |
| **Voice Input** | Speech-to-text conversation | `Screenshot 2023-09-04 124621.png` |

### 🎭 Case Studies Display

<div align="center">
<img src="screenshots/Screenshot 2023-09-04 125414.png" alt="Case Studies" width="800"/>

**Problem Solving Journey** | **Innovative Solutions Unveiled**
- Real-world impact stories
- User testimonials
- Success metrics
</div>

---

## 🔌 API Integrations

### OpenAI GPT Integration

```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an empathetic life assistant..."},
        {"role": "user", "content": user_message}
    ]
)
```

### Twilio Emergency Alert

```python
from twilio.rest import Client

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Emergency alert from LISTNER user",
    from_=twilio_number,
    to=emergency_contact
)
```

### Sentiment Analysis

```python
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(user_text)
```

---

## 🔮 Future Enhancements

- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Advanced ML Models**: Custom trained models for better context understanding
- [ ] **Multi-language Support**: Expand to 10+ languages
- [ ] **Video Call Support**: Real-time counselor connections
- [ ] **Community Forum**: Safe space for users to share experiences
- [ ] **Predictive Analytics**: Early warning system for mental health crises
- [ ] **Blockchain Integration**: Secure and anonymous data storage
- [ ] **AR/VR Therapy**: Immersive relaxation experiences

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add tests for new features
- Update documentation accordingly
- Ensure all tests pass before submitting PR

---

## 👥 Team

**Team @Back_Benchers**

### Team Leader
**Bilva Sai Eswar Maddi**
- 🎓 Computer Science and Business Systems
- 🏛️ G. Pulla Reddy Engineering College
- 📧 [catchbilvasai@gmail.com](mailto:catchbilvasai@gmail.com)

### Team Members
- **Siva Bharathi** - AI/ML Development
- **Harika** - Frontend Development
- **Rupa** - Backend Integration

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- IBM Watson for powerful AI capabilities
- OpenAI for GPT integration
- Twilio for emergency communication services
- All open-source libraries and their contributors
- Our mentors and supporters at G. Pulla Reddy Engineering College

---

## 📞 Contact & Support

- **Email**: [catchbilvasai@gmail.com](mailto:catchbilvasai@gmail.com)
- **GitHub Issues**: [Report a bug](https://github.com/yourusername/LISTNER-AI-Life-Assistance-Chatbot/issues)
- **LinkedIn**: [Connect with us](https://linkedin.com/in/yourprofile)

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/yourusername/LISTNER-AI-Life-Assistance-Chatbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/LISTNER-AI-Life-Assistance-Chatbot?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/LISTNER-AI-Life-Assistance-Chatbot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/LISTNER-AI-Life-Assistance-Chatbot)

---

<div align="center">

**Made with ❤️ by Team @Back_Benchers**

*Empowering lives through AI-driven assistance*

⭐ Star this repository if you find it helpful!

</div>
