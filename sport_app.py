import streamlit as st
import json
from datetime import datetime, date, timedelta
import os
import random

# Configuration de la page
st.set_page_config(
    page_title="FitHome Pro",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fichier pour sauvegarder les données
DATA_FILE = "progress_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "luca": {"poids_history": [], "seances_completees": [], "poids_actuel": 88, "streak": 0},
        "sonia": {"poids_history": [], "seances_completees": [], "poids_actuel": 75, "streak": 0}
    }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

if 'data' not in st.session_state:
    st.session_state.data = load_data()

# CSS Professionnel - Thème sombre forcé
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    /* ========== FORCER LE THEME SOMBRE SUR TOUT ========== */

    /* Fond principal - FORCER NOIR */
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
    .stApp > header, section[data-testid="stSidebar"],
    [data-testid="stToolbar"], [data-testid="stDecoration"],
    .element-container, .stMarkdown, div.block-container {
        background: #0d0d12 !important;
        background-color: #0d0d12 !important;
    }

    html, body, [data-testid="stAppViewBlockContainer"] {
        background: #0d0d12 !important;
        background-color: #0d0d12 !important;
    }

    /* Supprimer tous les fonds blancs */
    .css-1d391kg, .css-12oz5g7, .css-1avcm0n, .css-18e3th9,
    .css-1dp5vir, .css-hxt7ib, .e1fqkh3o3, .e1fqkh3o4,
    [data-baseweb="tab-panel"], .stTabs > div > div {
        background: #0d0d12 !important;
        background-color: #0d0d12 !important;
    }

    * {
        font-family: 'Outfit', sans-serif !important;
    }

    .main .block-container {
        padding: 1.5rem 2rem !important;
        max-width: 1200px !important;
        background: #0d0d12 !important;
    }

    /* Masquer éléments Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {
        visibility: hidden !important;
        display: none !important;
    }
    .stDeployButton {display: none !important;}

    /* ========== ONGLETS ========== */
    .stTabs [data-baseweb="tab-list"] {
        background: #1a1a24 !important;
        border-radius: 16px !important;
        padding: 6px !important;
        gap: 6px !important;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 12px !important;
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 12px 24px !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7c3aed, #ec4899) !important;
        color: white !important;
    }

    .stTabs [data-baseweb="tab-panel"] {
        background: #0d0d12 !important;
    }

    /* ========== HERO CARD ========== */
    .hero-card {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #ec4899 100%) !important;
        border-radius: 24px !important;
        padding: 32px !important;
        margin-bottom: 24px !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .hero-card::before {
        content: "" !important;
        position: absolute !important;
        top: -50% !important;
        right: -20% !important;
        width: 300px !important;
        height: 300px !important;
        background: rgba(255,255,255,0.1) !important;
        border-radius: 50% !important;
    }

    .hero-greeting {
        font-size: 16px !important;
        color: rgba(255,255,255,0.8) !important;
        margin-bottom: 4px !important;
    }

    .hero-name {
        font-size: 32px !important;
        font-weight: 800 !important;
        color: white !important;
        margin-bottom: 16px !important;
    }

    .hero-stats {
        display: flex !important;
        gap: 24px !important;
    }

    .hero-stat {
        text-align: center !important;
    }

    .hero-stat-value {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: white !important;
    }

    .hero-stat-label {
        font-size: 12px !important;
        color: rgba(255,255,255,0.7) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    .streak-badge {
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
        background: rgba(255,255,255,0.2) !important;
        padding: 8px 16px !important;
        border-radius: 50px !important;
        margin-top: 16px !important;
    }

    .streak-badge-text {
        color: white !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* ========== NOUVEAU CALENDRIER MODERNE ========== */
    .calendar-container {
        margin: 20px 0 !important;
    }

    .calendar-header {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        margin-bottom: 20px !important;
    }

    .calendar-title {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }

    .calendar-week {
        font-size: 14px !important;
        color: #7c3aed !important;
        font-weight: 600 !important;
    }

    .day-cards {
        display: flex !important;
        gap: 12px !important;
        overflow-x: auto !important;
        padding-bottom: 10px !important;
    }

    .day-card {
        min-width: 140px !important;
        background: linear-gradient(145deg, #1e1e2a, #252535) !important;
        border-radius: 20px !important;
        padding: 20px 16px !important;
        text-align: center !important;
        border: 2px solid transparent !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .day-card::before {
        content: "" !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 4px !important;
        background: linear-gradient(90deg, #7c3aed, #ec4899) !important;
        opacity: 0 !important;
        transition: opacity 0.3s ease !important;
    }

    .day-card:hover {
        transform: translateY(-4px) !important;
        border-color: rgba(124, 58, 237, 0.3) !important;
        box-shadow: 0 10px 30px rgba(124, 58, 237, 0.2) !important;
    }

    .day-card:hover::before {
        opacity: 1 !important;
    }

    .day-card.today {
        border-color: #7c3aed !important;
        box-shadow: 0 0 20px rgba(124, 58, 237, 0.3) !important;
    }

    .day-card.today::before {
        opacity: 1 !important;
    }

    .day-card.completed {
        background: linear-gradient(145deg, #065f46, #047857) !important;
        border-color: #10b981 !important;
    }

    .day-card.completed::before {
        background: #10b981 !important;
        opacity: 1 !important;
    }

    .day-name {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #94a3b8 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 8px !important;
    }

    .day-card.completed .day-name {
        color: rgba(255,255,255,0.8) !important;
    }

    .day-workout {
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        margin-bottom: 8px !important;
        line-height: 1.3 !important;
    }

    .day-info {
        display: flex !important;
        justify-content: center !important;
        gap: 12px !important;
        margin-top: 10px !important;
    }

    .day-info-item {
        font-size: 11px !important;
        color: #64748b !important;
    }

    .day-card.completed .day-info-item {
        color: rgba(255,255,255,0.7) !important;
    }

    .day-status {
        margin-top: 12px !important;
        font-size: 20px !important;
    }

    .day-status-done {
        color: #10b981 !important;
    }

    .day-status-pending {
        color: #4b5563 !important;
    }

    /* ========== WORKOUT CARD ========== */
    .workout-card {
        background: #1a1a24 !important;
        border-radius: 24px !important;
        padding: 24px !important;
        margin: 16px 0 !important;
        border: 1px solid rgba(255,255,255,0.05) !important;
    }

    .workout-badge {
        background: linear-gradient(135deg, #7c3aed, #ec4899) !important;
        padding: 6px 14px !important;
        border-radius: 50px !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        color: white !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    .workout-title {
        font-size: 24px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        margin-top: 12px !important;
    }

    .workout-meta {
        display: flex !important;
        gap: 16px !important;
        margin-top: 12px !important;
    }

    .workout-meta-item {
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        color: #94a3b8 !important;
        font-size: 14px !important;
    }

    /* ========== EXERCICES ========== */
    .exercise-item {
        display: flex !important;
        align-items: center !important;
        gap: 16px !important;
        padding: 16px !important;
        background: #252532 !important;
        border-radius: 16px !important;
        margin-bottom: 10px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        border: 1px solid transparent !important;
    }

    .exercise-item:hover {
        background: rgba(124, 58, 237, 0.15) !important;
        border-color: #7c3aed !important;
        transform: translateX(4px) !important;
    }

    .exercise-icon-box {
        width: 52px !important;
        height: 52px !important;
        background: linear-gradient(135deg, #7c3aed, #ec4899) !important;
        border-radius: 14px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 24px !important;
        flex-shrink: 0 !important;
    }

    .exercise-name {
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        margin-bottom: 2px !important;
    }

    .exercise-sets {
        font-size: 13px !important;
        color: #94a3b8 !important;
    }

    /* ========== PROGRESS ========== */
    .progress-card {
        background: #1a1a24 !important;
        border-radius: 20px !important;
        padding: 24px !important;
        margin: 16px 0 !important;
    }

    .progress-title {
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }

    .progress-value {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #10b981 !important;
    }

    .progress-bar {
        height: 10px !important;
        background: #252532 !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }

    .progress-fill {
        height: 100% !important;
        background: linear-gradient(90deg, #10b981, #34d399) !important;
        border-radius: 10px !important;
    }

    /* ========== OBJECTIF ========== */
    .objective-card {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(52, 211, 153, 0.1)) !important;
        border: 1px solid #10b981 !important;
        border-radius: 16px !important;
        padding: 20px !important;
        margin: 16px 0 !important;
    }

    .objective-label {
        font-size: 12px !important;
        font-weight: 600 !important;
        color: #10b981 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 8px !important;
    }

    .objective-text {
        font-size: 15px !important;
        color: #ffffff !important;
        line-height: 1.5 !important;
    }

    /* ========== VIDEO ========== */
    .video-card {
        background: #1a1a24 !important;
        border-radius: 20px !important;
        padding: 24px !important;
        margin: 20px 0 !important;
        border: 2px solid #7c3aed !important;
    }

    .video-icon {
        width: 60px !important;
        height: 60px !important;
        background: linear-gradient(135deg, #ef4444, #f97316) !important;
        border-radius: 16px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 28px !important;
    }

    .video-title {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }

    .video-subtitle {
        font-size: 14px !important;
        color: #94a3b8 !important;
    }

    /* ========== BOUTONS ========== */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #ec4899) !important;
        color: white !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.4) !important;
    }

    /* ========== SELECTBOX & INPUTS ========== */
    .stSelectbox > div > div,
    .stSelectbox [data-baseweb="select"] > div,
    [data-baseweb="select"] {
        background: #1a1a24 !important;
        background-color: #1a1a24 !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    .stSelectbox svg {
        fill: #ffffff !important;
    }

    [data-baseweb="popover"] > div {
        background: #1a1a24 !important;
        background-color: #1a1a24 !important;
    }

    [data-baseweb="menu"] {
        background: #1a1a24 !important;
        background-color: #1a1a24 !important;
    }

    [role="option"] {
        background: #1a1a24 !important;
        color: #ffffff !important;
    }

    [role="option"]:hover {
        background: #252532 !important;
    }

    /* ========== EXPANDER ========== */
    .streamlit-expanderHeader {
        background: #1a1a24 !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    .streamlit-expanderContent {
        background: #1a1a24 !important;
        border-color: rgba(255,255,255,0.1) !important;
    }

    /* Number input */
    .stNumberInput > div > div > input {
        background: #1a1a24 !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
    }

    /* ========== TEXTES ========== */
    .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown div {
        color: #94a3b8 !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }

    p, span, div, label {
        color: #e2e8f0 !important;
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.1) !important;
    }

    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem !important;
        }

        .hero-card {
            padding: 24px !important;
        }

        .hero-name {
            font-size: 26px !important;
        }

        .hero-stats {
            gap: 16px !important;
        }

        .hero-stat-value {
            font-size: 22px !important;
        }

        .week-days {
            gap: 4px !important;
        }

        .day-item {
            padding: 12px 4px !important;
        }

        .day-number {
            font-size: 15px !important;
        }

        .workout-title {
            font-size: 20px !important;
        }

        .exercise-item {
            padding: 12px !important;
        }

        .exercise-icon-box {
            width: 44px !important;
            height: 44px !important;
            font-size: 20px !important;
        }

        .exercise-name {
            font-size: 14px !important;
        }
    }

    @media (max-width: 480px) {
        .hero-stats {
            flex-wrap: wrap !important;
        }

        .day-letter {
            font-size: 10px !important;
        }

        .day-number {
            font-size: 14px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PROGRAMMES
# ============================================================================

JOURS_SEMAINE = ["Lun", "Mar", "Mer", "Jeu", "Ven"]

# VIDÉOS YOUTUBE EN FRANÇAIS (Tibo InShape, Sissy MUA, Lucile Woodward, etc.)
PROGRAMME_LUCA = {
    "Lun": {"titre": "Pectoraux & Triceps", "duree": "35", "kcal": "280", "couleur": "#7c3aed", "exercices": [
        {"nom": "Pompes classiques", "icon": "💪", "sets": "4×20", "video": "https://www.youtube.com/watch?v=5eSM88TFzAs"},
        {"nom": "Pompes diamant", "icon": "💎", "sets": "4×12", "video": "https://www.youtube.com/watch?v=pMzWJe0vAmk"},
        {"nom": "Pompes déclinées", "icon": "📐", "sets": "3×15", "video": "https://www.youtube.com/watch?v=5eSM88TFzAs"},
        {"nom": "Dips sur chaises", "icon": "🪑", "sets": "4×15", "video": "https://www.youtube.com/watch?v=0326dy_-CzM"},
        {"nom": "Pompes serrées", "icon": "🔥", "sets": "3×15", "video": "https://www.youtube.com/watch?v=pMzWJe0vAmk"},
    ]},
    "Mar": {"titre": "Dos & Biceps", "duree": "40", "kcal": "320", "couleur": "#3b82f6", "exercices": [
        {"nom": "Tractions", "icon": "🚪", "sets": "4×max", "video": "https://www.youtube.com/watch?v=gOhJPXHdj4U"},
        {"nom": "Rowing inversé", "icon": "🪑", "sets": "4×12", "video": "https://www.youtube.com/watch?v=hXTc1mDnZCw"},
        {"nom": "Superman", "icon": "🦸", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=z6PJMT2y8GQ"},
        {"nom": "Curl biceps", "icon": "🍶", "sets": "4×15", "video": "https://www.youtube.com/watch?v=in7PaeYlhrM"},
        {"nom": "Curl marteau", "icon": "🔨", "sets": "3×12", "video": "https://www.youtube.com/watch?v=in7PaeYlhrM"},
    ]},
    "Mer": {"titre": "Abdos Intenses", "duree": "30", "kcal": "250", "couleur": "#ef4444", "exercices": [
        {"nom": "Crunchs", "icon": "🎯", "sets": "4×25", "video": "https://www.youtube.com/watch?v=9pgJPbE7oAQ"},
        {"nom": "Relevé de jambes", "icon": "🦵", "sets": "4×15", "video": "https://www.youtube.com/watch?v=9pgJPbE7oAQ"},
        {"nom": "Planche", "icon": "📏", "sets": "4×1min", "video": "https://www.youtube.com/watch?v=TvxNkmjdhMM"},
        {"nom": "Mountain climbers", "icon": "⛰️", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=wQq3ybaLZeA"},
        {"nom": "Bicycle crunch", "icon": "🚴", "sets": "3×20", "video": "https://www.youtube.com/watch?v=9pgJPbE7oAQ"},
    ]},
    "Jeu": {"titre": "Épaules & Bras", "duree": "35", "kcal": "260", "couleur": "#f59e0b", "exercices": [
        {"nom": "Pike push-ups", "icon": "🔺", "sets": "4×12", "video": "https://www.youtube.com/watch?v=5eSM88TFzAs"},
        {"nom": "Élévations latérales", "icon": "🦅", "sets": "4×15", "video": "https://www.youtube.com/watch?v=FeJP4E4Z-PY"},
        {"nom": "Handstand au mur", "icon": "🤸", "sets": "3×30s", "video": "https://www.youtube.com/watch?v=qQVxyTPBsR8"},
        {"nom": "Curl concentration", "icon": "💪", "sets": "3×12", "video": "https://www.youtube.com/watch?v=in7PaeYlhrM"},
        {"nom": "Triceps extensions", "icon": "💥", "sets": "3×15", "video": "https://www.youtube.com/watch?v=0326dy_-CzM"},
    ]},
    "Ven": {"titre": "Jambes & Core", "duree": "40", "kcal": "350", "couleur": "#10b981", "exercices": [
        {"nom": "Squats", "icon": "🦵", "sets": "4×20", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
        {"nom": "Fentes marchées", "icon": "🚶", "sets": "3×20", "video": "https://www.youtube.com/watch?v=D7KaRcUTQeE"},
        {"nom": "Pont fessier", "icon": "🌉", "sets": "4×15", "video": "https://www.youtube.com/watch?v=wPM8icPu6H8"},
        {"nom": "Squats bulgares", "icon": "🇧🇬", "sets": "3×12", "video": "https://www.youtube.com/watch?v=D7KaRcUTQeE"},
        {"nom": "Mollets", "icon": "🦶", "sets": "4×25", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
    ]},
}

PROGRAMME_SONIA = {
    "Lun": {"titre": "Cardio Brûle-Graisse", "duree": "30", "kcal": "350", "couleur": "#ef4444", "exercices": [
        {"nom": "Jumping jacks", "icon": "⭐", "sets": "4×45s", "video": "https://www.youtube.com/watch?v=iSSAk4XCsRA"},
        {"nom": "Montées de genoux", "icon": "🦵", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=iSSAk4XCsRA"},
        {"nom": "Burpees modifiés", "icon": "🔥", "sets": "3×10", "video": "https://www.youtube.com/watch?v=qLBImHhCXSw"},
        {"nom": "Mountain climbers", "icon": "⛰️", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=wQq3ybaLZeA"},
        {"nom": "Squat jumps", "icon": "🦘", "sets": "3×12", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
    ]},
    "Mar": {"titre": "Cuisses & Fessiers", "duree": "35", "kcal": "280", "couleur": "#ec4899", "exercices": [
        {"nom": "Squats", "icon": "🦵", "sets": "4×20", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
        {"nom": "Sumo squats", "icon": "🏋️", "sets": "4×15", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
        {"nom": "Pont fessier", "icon": "🌉", "sets": "4×25", "video": "https://www.youtube.com/watch?v=wPM8icPu6H8"},
        {"nom": "Donkey kicks", "icon": "🐴", "sets": "3×20", "video": "https://www.youtube.com/watch?v=wPM8icPu6H8"},
        {"nom": "Fire hydrant", "icon": "🔥", "sets": "3×15", "video": "https://www.youtube.com/watch?v=wPM8icPu6H8"},
    ]},
    "Mer": {"titre": "HIIT Brûle-Graisse", "duree": "25", "kcal": "400", "couleur": "#f97316", "exercices": [
        {"nom": "Burpees", "icon": "🔥", "sets": "4×8", "video": "https://www.youtube.com/watch?v=qLBImHhCXSw"},
        {"nom": "Speed skaters", "icon": "⛸️", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=iSSAk4XCsRA"},
        {"nom": "Squat pulses", "icon": "💫", "sets": "3×30s", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
        {"nom": "Step ups", "icon": "📦", "sets": "3×15", "video": "https://www.youtube.com/watch?v=D7KaRcUTQeE"},
        {"nom": "Planche", "icon": "📏", "sets": "4×45s", "video": "https://www.youtube.com/watch?v=TvxNkmjdhMM"},
    ]},
    "Jeu": {"titre": "Haut du Corps & Abdos", "duree": "30", "kcal": "220", "couleur": "#8b5cf6", "exercices": [
        {"nom": "Pompes sur genoux", "icon": "💪", "sets": "4×12", "video": "https://www.youtube.com/watch?v=5eSM88TFzAs"},
        {"nom": "Dips sur chaise", "icon": "🪑", "sets": "3×12", "video": "https://www.youtube.com/watch?v=0326dy_-CzM"},
        {"nom": "Crunchs", "icon": "🎯", "sets": "4×20", "video": "https://www.youtube.com/watch?v=9pgJPbE7oAQ"},
        {"nom": "Bicycle crunch", "icon": "🚴", "sets": "3×20", "video": "https://www.youtube.com/watch?v=9pgJPbE7oAQ"},
        {"nom": "Planche latérale", "icon": "📐", "sets": "3×30s", "video": "https://www.youtube.com/watch?v=TvxNkmjdhMM"},
    ]},
    "Ven": {"titre": "Full Body", "duree": "35", "kcal": "380", "couleur": "#10b981", "exercices": [
        {"nom": "Jumping jacks", "icon": "⭐", "sets": "3×1min", "video": "https://www.youtube.com/watch?v=iSSAk4XCsRA"},
        {"nom": "Squats + press", "icon": "🏋️", "sets": "4×15", "video": "https://www.youtube.com/watch?v=m0GcZ24pK6k"},
        {"nom": "Pompes", "icon": "💪", "sets": "3×10", "video": "https://www.youtube.com/watch?v=5eSM88TFzAs"},
        {"nom": "Fentes alternées", "icon": "🚶", "sets": "3×20", "video": "https://www.youtube.com/watch?v=D7KaRcUTQeE"},
        {"nom": "Planche", "icon": "📏", "sets": "3×1min", "video": "https://www.youtube.com/watch?v=TvxNkmjdhMM"},
    ]},
}

# ============================================================================
# FONCTIONS
# ============================================================================

def get_week_number():
    return str(date.today().isocalendar()[1])

def get_completed_days(prefix):
    week = get_week_number()
    seances = st.session_state.data[prefix].get('seances_completees', [])
    return [s.split('_')[1] for s in seances if s.startswith(week)]

def toggle_day(prefix, jour):
    week = get_week_number()
    key = f"{week}_{jour}"
    seances = st.session_state.data[prefix].get('seances_completees', [])
    if key in seances:
        seances.remove(key)
    else:
        seances.append(key)
    st.session_state.data[prefix]['seances_completees'] = seances[-100:]
    save_data(st.session_state.data)

def afficher_hero(prefix, nom, poids_actuel, objectif, is_homme=True):
    completed = len(get_completed_days(prefix))
    total_seances = len(st.session_state.data[prefix].get('seances_completees', []))

    greeting = "Salut" if is_homme else "Hello"
    emoji = "👨" if is_homme else "👩"

    st.markdown(f"""
    <div class="hero-card">
        <div class="hero-greeting">{greeting}, prêt(e) à t'entraîner ?</div>
        <div class="hero-name">{emoji} {nom}</div>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-value">{poids_actuel}</div>
                <div class="hero-stat-label">kg actuel</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">{objectif}</div>
                <div class="hero-stat-label">kg objectif</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">{total_seances}</div>
                <div class="hero-stat-label">séances</div>
            </div>
        </div>
        <div class="streak-badge">
            <span>🔥</span>
            <span class="streak-badge-text">{completed}/5 cette semaine</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def afficher_objectif(is_perte=False):
    if is_perte:
        texte = "Perdre 10-15 kg • Tonifier cuisses & fessiers • Ventre plat"
    else:
        texte = "Prise de masse musculaire • Abdos visibles • Bras musclés"

    st.markdown(f"""
    <div class="objective-card">
        <div class="objective-label">🎯 Objectif</div>
        <div class="objective-text">{texte}</div>
    </div>
    """, unsafe_allow_html=True)

def afficher_progression(prefix, poids_initial, poids_objectif, is_perte=False):
    poids_actuel = st.session_state.data[prefix].get('poids_actuel', poids_initial)

    if is_perte:
        total = poids_initial - poids_objectif
        fait = poids_initial - poids_actuel
    else:
        total = poids_objectif - poids_initial
        fait = poids_actuel - poids_initial

    prog = min(max((fait / total) * 100, 0), 100) if total > 0 else 0

    st.markdown(f"""
    <div class="progress-card">
        <div class="progress-header">
            <div class="progress-title">📊 Progression</div>
            <div class="progress-value">{prog:.0f}%</div>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {prog}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("⚖️ Mettre à jour mon poids"):
        new_poids = st.number_input("Poids (kg)", min_value=40.0, max_value=150.0,
                                     value=float(poids_actuel), step=0.1, key=f"{prefix}_poids")
        if st.button("💾 Enregistrer", key=f"{prefix}_save"):
            st.session_state.data[prefix]['poids_actuel'] = new_poids
            save_data(st.session_state.data)
            st.success("✅ Poids enregistré !")
            st.rerun()

def afficher_calendrier(prefix, programme):
    completed = get_completed_days(prefix)
    today_name = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"][date.today().weekday()]
    week_num = get_week_number()

    # Noms complets des jours
    jours_complets = {"Lun": "LUNDI", "Mar": "MARDI", "Mer": "MERCREDI", "Jeu": "JEUDI", "Ven": "VENDREDI"}

    st.markdown(f"""
    <div class="calendar-container">
        <div class="calendar-header">
            <div class="calendar-title">📅 Ta semaine</div>
            <div class="calendar-week">Semaine {week_num}</div>
        </div>
        <div class="day-cards">
    """, unsafe_allow_html=True)

    cards_html = ""
    for jour in JOURS_SEMAINE:
        is_done = jour in completed
        is_today = jour == today_name
        workout = programme[jour]

        classes = []
        if is_done:
            classes.append("completed")
        if is_today and not is_done:
            classes.append("today")

        status_icon = "✓" if is_done else "○"
        status_class = "day-status-done" if is_done else "day-status-pending"

        cards_html += f"""
        <div class="day-card {' '.join(classes)}">
            <div class="day-name">{jours_complets[jour]}</div>
            <div class="day-workout">{workout['titre']}</div>
            <div class="day-info">
                <span class="day-info-item">⏱ {workout['duree']}min</span>
                <span class="day-info-item">🔥 {workout['kcal']}kcal</span>
            </div>
            <div class="day-status {status_class}">{status_icon}</div>
        </div>
        """

    st.markdown(cards_html + "</div></div>", unsafe_allow_html=True)

    # Boutons pour marquer comme fait
    st.markdown("##### Marquer comme fait :")
    cols = st.columns(5)
    for i, jour in enumerate(JOURS_SEMAINE):
        with cols[i]:
            is_done = jour in completed
            label = f"✓ {jour}" if is_done else f"○ {jour}"
            if st.button(label, key=f"{prefix}_toggle_{jour}", use_container_width=True):
                toggle_day(prefix, jour)
                st.rerun()

def afficher_workout(prefix, programme):
    jour = st.selectbox("Choisis ton jour", JOURS_SEMAINE, key=f"{prefix}_jour")
    workout = programme[jour]

    st.markdown(f"""
    <div class="workout-card">
        <div class="workout-header">
            <div>
                <div class="workout-badge">JOUR {JOURS_SEMAINE.index(jour) + 1}</div>
                <div class="workout-title">{workout['titre']}</div>
                <div class="workout-meta">
                    <div class="workout-meta-item">⏱️ {workout['duree']} min</div>
                    <div class="workout-meta-item">🔥 {workout['kcal']} kcal</div>
                    <div class="workout-meta-item">💪 {len(workout['exercices'])} exercices</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="exercise-list">', unsafe_allow_html=True)

    for ex in workout['exercices']:
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown(f"""
            <div class="exercise-item">
                <div class="exercise-icon-box">{ex['icon']}</div>
                <div class="exercise-content">
                    <div class="exercise-name">{ex['nom']}</div>
                    <div class="exercise-sets">{ex['sets']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("▶", key=f"{prefix}_{jour}_{ex['nom']}"):
                st.session_state[f"{prefix}_video"] = ex

    st.markdown('</div>', unsafe_allow_html=True)

def afficher_video(prefix):
    key = f"{prefix}_video"
    if key in st.session_state and st.session_state[key]:
        ex = st.session_state[key]

        st.markdown(f"""
        <div class="video-card">
            <div class="video-header">
                <div class="video-icon">{ex['icon']}</div>
                <div>
                    <div class="video-title">{ex['nom']}</div>
                    <div class="video-subtitle">{ex['sets']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        video_id = ex['video'].split("watch?v=")[1].split("&")[0] if "watch?v=" in ex['video'] else ex['video'].split("/")[-1]
        st.video(f"https://www.youtube.com/watch?v={video_id}")

        if st.button("❌ Fermer la vidéo", key=f"{prefix}_close"):
            st.session_state[key] = None
            st.rerun()

# ============================================================================
# APP
# ============================================================================

tab1, tab2 = st.tabs(["👨 LUCA", "👩 SONIA"])

with tab1:
    poids = st.session_state.data['luca'].get('poids_actuel', 88)
    afficher_hero("luca", "LUCA", poids, 90, True)
    afficher_objectif(is_perte=False)
    afficher_progression("luca", 88, 90, False)
    afficher_calendrier("luca", PROGRAMME_LUCA)
    st.markdown("---")
    afficher_workout("luca", PROGRAMME_LUCA)
    afficher_video("luca")

with tab2:
    poids = st.session_state.data['sonia'].get('poids_actuel', 75)
    afficher_hero("sonia", "SONIA", poids, 62, False)
    afficher_objectif(is_perte=True)
    afficher_progression("sonia", 75, 62, True)
    afficher_calendrier("sonia", PROGRAMME_SONIA)
    st.markdown("---")
    afficher_workout("sonia", PROGRAMME_SONIA)
    afficher_video("sonia")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #64748b;">
    <p>💪 <strong>FitHome Pro</strong></p>
    <p style="font-size: 12px;">Weekend = Repos actif 🧘</p>
</div>
""", unsafe_allow_html=True)
