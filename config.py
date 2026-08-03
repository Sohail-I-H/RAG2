import streamlit as st

from groq import Groq
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings


# ==========================================================
# API KEY
# ==========================================================

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


# ==========================================================
# GROQ CLIENT
# ==========================================================

groq_client = Groq(
    api_key=GROQ_API_KEY
)


# ==========================================================
# CHAT MODEL
# ==========================================================

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)


# ==========================================================
# EMBEDDINGS
# ==========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# ==========================================================
# DATA FILES
# ==========================================================

FAQ_FILE = "data/pragyan_faq_prices.xlsx"


# ==========================================================
# SUPPORTED LANGUAGES
# ==========================================================

LANGUAGES = {

    "English 🇺🇸": {
        "name": "English",
        "tts": "en-US-AriaNeural"
    },

    "ಕನ್ನಡ 🇮🇳": {
        "name": "Kannada",
        "tts": "kn-IN-SapnaNeural"
    },

    "हिन्दी 🇮🇳": {
        "name": "Hindi",
        "tts": "hi-IN-SwaraNeural"
    },

    "தமிழ் 🇮🇳": {
        "name": "Tamil",
        "tts": "ta-IN-PallaviNeural"
    },

    "తెలుగు 🇮🇳": {
        "name": "Telugu",
        "tts": "te-IN-ShrutiNeural"
    },

    "മലയാളം 🇮🇳": {
        "name": "Malayalam",
        "tts": "ml-IN-SobhanaNeural"
    },

    "मराठी 🇮🇳": {
        "name": "Marathi",
        "tts": "mr-IN-AarohiNeural"
    },

    "ગુજરાતી 🇮🇳": {
        "name": "Gujarati",
        "tts": "gu-IN-DhwaniNeural"
    },

    "বাংলা 🇮🇳": {
        "name": "Bengali",
        "tts": "bn-IN-TanishaaNeural"
    },

    "ਪੰਜਾਬੀ 🇮🇳": {
        "name": "Punjabi",
        "tts": "pa-IN-OjasNeural"
    },

    "Español 🇪🇸": {
        "name": "Spanish",
        "tts": "es-ES-ElviraNeural"
    },

    "Français 🇫🇷": {
        "name": "French",
        "tts": "fr-FR-DeniseNeural"
    },

    "Deutsch 🇩🇪": {
        "name": "German",
        "tts": "de-DE-KatjaNeural"
    },

    "Italiano 🇮🇹": {
        "name": "Italian",
        "tts": "it-IT-ElsaNeural"
    },

    "Português 🇵🇹": {
        "name": "Portuguese",
        "tts": "pt-PT-RaquelNeural"
    },

    "日本語 🇯🇵": {
        "name": "Japanese",
        "tts": "ja-JP-NanamiNeural"
    },

    "한국어 🇰🇷": {
        "name": "Korean",
        "tts": "ko-KR-SunHiNeural"
    },

    "中文 🇨🇳": {
        "name": "Chinese",
        "tts": "zh-CN-XiaoxiaoNeural"
    }

}


# ==========================================================
# PERSONAS
# ==========================================================

PERSONAS = {

    "🎓 Student Counselor": {

        "role": "Aarav",

        "prompt": """
You are Aarav, the Student Counselor at PragyanAI.

Use ONLY the retrieved context.

Never make up information.

Guide students professionally.

Encourage enrollment only when supported by the retrieved documents.
"""

    },

    "🏫 Institutional Advisor": {

        "role": "Dr. Kavita",

        "prompt": """
You are Dr. Kavita.

You help Engineering Colleges partner with PragyanAI.

Use ONLY the retrieved context.
"""

    },

    "💼 Enterprise AI Lead": {

        "role": "Rohan",

        "prompt": """
You are Rohan.

You help enterprises recruit PragyanAI engineers.

Use ONLY the retrieved context.
"""

    }

}


# ==========================================================
# WHISPER MODEL
# ==========================================================

WHISPER_MODEL = "whisper-large-v3-turbo"


# ==========================================================
# CHAT MODEL
# ==========================================================

CHAT_MODEL = "llama-3.3-70b-versatile"
