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

# CSS Professionnel - Inspiré Nike Training, Freeletics, Fitbod
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    :root {
        --bg-primary: #13131a;
        --bg-secondary: #1c1c26;
        --bg-card: #23232f;
        --accent-purple: #7c3aed;
        --accent-pink: #ec4899;
        --accent-blue: #3b82f6;
        --accent-green: #10b981;
        --accent-orange: #f97316;
        --text-primary: #ffffff;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
    }

    * {
        font-family: 'Outfit', sans-serif;
    }

    /* Fond principal */
    .stApp {
        background: var(--bg-primary) !important;
    }

    .main .block-container {
        padding: 1.5rem 2rem;
        max-width: 1200px;
    }

    /* Masquer éléments Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Onglets modernes */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg-secondary);
        border-radius: 16px;
        padding: 6px;
        gap: 6px;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: var(--text-secondary);
        font-weight: 600;
        font-size: 15px;
        padding: 12px 24px;
    }

    .stTabs [aria-selected="true"] {
        background: var(--accent-purple) !important;
        color: white !important;
    }

    /* === COMPOSANTS CUSTOM === */

    /* Hero Card */
    .hero-card {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #ec4899 100%);
        border-radius: 24px;
        padding: 32px;
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }

    .hero-card::before {
        content: "";
        position: absolute;
        top: -50%;
        right: -20%;
        width: 300px;
        height: 300px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
    }

    .hero-greeting {
        font-size: 16px;
        color: rgba(255,255,255,0.8);
        margin-bottom: 4px;
    }

    .hero-name {
        font-size: 32px;
        font-weight: 800;
        color: white;
        margin-bottom: 16px;
    }

    .hero-stats {
        display: flex;
        gap: 24px;
    }

    .hero-stat {
        text-align: center;
    }

    .hero-stat-value {
        font-size: 28px;
        font-weight: 700;
        color: white;
    }

    .hero-stat-label {
        font-size: 12px;
        color: rgba(255,255,255,0.7);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Streak Badge */
    .streak-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.2);
        padding: 8px 16px;
        border-radius: 50px;
        margin-top: 16px;
    }

    .streak-badge-text {
        color: white;
        font-weight: 600;
        font-size: 14px;
    }

    /* Calendrier semaine horizontal */
    .week-calendar {
        background: var(--bg-card);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
    }

    .week-title {
        font-size: 18px;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 16px;
    }

    .week-days {
        display: flex;
        justify-content: space-between;
        gap: 8px;
    }

    .day-item {
        flex: 1;
        text-align: center;
        padding: 16px 8px;
        border-radius: 16px;
        background: var(--bg-secondary);
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }

    .day-item:hover {
        border-color: var(--accent-purple);
        transform: translateY(-2px);
    }

    .day-item.active {
        background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink));
        border-color: transparent;
    }

    .day-item.completed {
        background: var(--accent-green);
    }

    .day-letter {
        font-size: 12px;
        font-weight: 600;
        color: var(--text-secondary);
        margin-bottom: 4px;
    }

    .day-item.active .day-letter,
    .day-item.completed .day-letter {
        color: rgba(255,255,255,0.8);
    }

    .day-number {
        font-size: 18px;
        font-weight: 700;
        color: var(--text-primary);
    }

    .day-item.active .day-number,
    .day-item.completed .day-number {
        color: white;
    }

    .day-check {
        font-size: 16px;
        margin-top: 4px;
    }

    /* Workout Card */
    .workout-card {
        background: var(--bg-card);
        border-radius: 24px;
        padding: 24px;
        margin: 16px 0;
        border: 1px solid rgba(255,255,255,0.05);
    }

    .workout-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 20px;
    }

    .workout-badge {
        background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink));
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 11px;
        font-weight: 700;
        color: white;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .workout-title {
        font-size: 24px;
        font-weight: 700;
        color: var(--text-primary);
        margin-top: 12px;
    }

    .workout-meta {
        display: flex;
        gap: 16px;
        margin-top: 12px;
    }

    .workout-meta-item {
        display: flex;
        align-items: center;
        gap: 6px;
        color: var(--text-secondary);
        font-size: 14px;
    }

    /* Exercise List */
    .exercise-list {
        margin-top: 20px;
    }

    .exercise-item {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 16px;
        background: var(--bg-secondary);
        border-radius: 16px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }

    .exercise-item:hover {
        background: rgba(124, 58, 237, 0.15);
        border-color: var(--accent-purple);
        transform: translateX(4px);
    }

    .exercise-icon-box {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink));
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        flex-shrink: 0;
    }

    .exercise-content {
        flex: 1;
    }

    .exercise-name {
        font-size: 16px;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 2px;
    }

    .exercise-sets {
        font-size: 13px;
        color: var(--text-secondary);
    }

    .exercise-play {
        width: 40px;
        height: 40px;
        background: var(--accent-purple);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 14px;
    }

    /* Progress Card */
    .progress-card {
        background: var(--bg-card);
        border-radius: 20px;
        padding: 24px;
        margin: 16px 0;
    }

    .progress-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }

    .progress-title {
        font-size: 16px;
        font-weight: 600;
        color: var(--text-primary);
    }

    .progress-value {
        font-size: 18px;
        font-weight: 700;
        color: var(--accent-green);
    }

    .progress-bar {
        height: 10px;
        background: var(--bg-secondary);
        border-radius: 10px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--accent-green), #34d399);
        border-radius: 10px;
        transition: width 0.5s ease;
    }

    /* Objective Card */
    .objective-card {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(52, 211, 153, 0.1));
        border: 1px solid var(--accent-green);
        border-radius: 16px;
        padding: 20px;
        margin: 16px 0;
    }

    .objective-label {
        font-size: 12px;
        font-weight: 600;
        color: var(--accent-green);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .objective-text {
        font-size: 15px;
        color: var(--text-primary);
        line-height: 1.5;
    }

    /* Video Modal */
    .video-card {
        background: var(--bg-card);
        border-radius: 20px;
        padding: 24px;
        margin: 20px 0;
        border: 2px solid var(--accent-purple);
    }

    .video-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 20px;
    }

    .video-icon {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #ef4444, #f97316);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
    }

    .video-title {
        font-size: 20px;
        font-weight: 700;
        color: var(--text-primary);
    }

    .video-subtitle {
        font-size: 14px;
        color: var(--text-secondary);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink)) !important;
        color: white !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.4) !important;
    }

    /* Selectbox */
    .stSelectbox > div > div {
        background: var(--bg-card) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: var(--bg-card) !important;
        border-radius: 12px !important;
    }

    /* Text colors */
    .stMarkdown p, .stMarkdown span {
        color: var(--text-secondary) !important;
    }

    h1, h2, h3, h4 {
        color: var(--text-primary) !important;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }

        .hero-card {
            padding: 24px;
        }

        .hero-name {
            font-size: 26px;
        }

        .hero-stats {
            gap: 16px;
        }

        .hero-stat-value {
            font-size: 22px;
        }

        .week-days {
            gap: 4px;
        }

        .day-item {
            padding: 12px 4px;
        }

        .day-number {
            font-size: 15px;
        }

        .workout-title {
            font-size: 20px;
        }

        .exercise-item {
            padding: 12px;
        }

        .exercise-icon-box {
            width: 44px;
            height: 44px;
            font-size: 20px;
        }

        .exercise-name {
            font-size: 14px;
        }
    }

    @media (max-width: 480px) {
        .hero-stats {
            flex-wrap: wrap;
        }

        .day-letter {
            font-size: 10px;
        }

        .day-number {
            font-size: 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PROGRAMMES
# ============================================================================

JOURS_SEMAINE = ["Lun", "Mar", "Mer", "Jeu", "Ven"]

PROGRAMME_LUCA = {
    "Lun": {"titre": "Pectoraux & Triceps", "duree": "35", "kcal": "280", "couleur": "#7c3aed", "exercices": [
        {"nom": "Pompes classiques", "icon": "💪", "sets": "4×20", "video": "https://www.youtube.com/watch?v=IODxDxX7oi4"},
        {"nom": "Pompes diamant", "icon": "💎", "sets": "4×12", "video": "https://www.youtube.com/watch?v=J0DnG1_S92I"},
        {"nom": "Pompes déclinées", "icon": "📐", "sets": "3×15", "video": "https://www.youtube.com/watch?v=SKPab2YC9AY"},
        {"nom": "Dips sur chaises", "icon": "🪑", "sets": "4×15", "video": "https://www.youtube.com/watch?v=HCf97NPYeGY"},
        {"nom": "Pompes serrées", "icon": "🔥", "sets": "3×15", "video": "https://www.youtube.com/watch?v=5M7JMb5jhq4"},
    ]},
    "Mar": {"titre": "Dos & Biceps", "duree": "40", "kcal": "320", "couleur": "#3b82f6", "exercices": [
        {"nom": "Tractions", "icon": "🚪", "sets": "4×max", "video": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
        {"nom": "Rowing inversé", "icon": "🪑", "sets": "4×12", "video": "https://www.youtube.com/watch?v=OYUxXMGVuuU"},
        {"nom": "Superman", "icon": "🦸", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=cc6UVRS7PW4"},
        {"nom": "Curl biceps", "icon": "🍶", "sets": "4×15", "video": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo"},
        {"nom": "Curl marteau", "icon": "🔨", "sets": "3×12", "video": "https://www.youtube.com/watch?v=zC3nLlEvin4"},
    ]},
    "Mer": {"titre": "Abdos Intenses", "duree": "30", "kcal": "250", "couleur": "#ef4444", "exercices": [
        {"nom": "Crunchs", "icon": "🎯", "sets": "4×25", "video": "https://www.youtube.com/watch?v=Xyd_fa5zoEU"},
        {"nom": "Relevé de jambes", "icon": "🦵", "sets": "4×15", "video": "https://www.youtube.com/watch?v=JB2oyawG9KI"},
        {"nom": "Planche", "icon": "📏", "sets": "4×1min", "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c"},
        {"nom": "Mountain climbers", "icon": "⛰️", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=nmwgirgXLYM"},
        {"nom": "Bicycle crunch", "icon": "🚴", "sets": "3×20", "video": "https://www.youtube.com/watch?v=9FGilxCbdz8"},
    ]},
    "Jeu": {"titre": "Épaules & Bras", "duree": "35", "kcal": "260", "couleur": "#f59e0b", "exercices": [
        {"nom": "Pike push-ups", "icon": "🔺", "sets": "4×12", "video": "https://www.youtube.com/watch?v=sposDXWEB0A"},
        {"nom": "Élévations latérales", "icon": "🦅", "sets": "4×15", "video": "https://www.youtube.com/watch?v=3VcKaXpzqRo"},
        {"nom": "Handstand au mur", "icon": "🤸", "sets": "3×30s", "video": "https://www.youtube.com/watch?v=xIdKwIB3M3E"},
        {"nom": "Curl concentration", "icon": "💪", "sets": "3×12", "video": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo"},
        {"nom": "Triceps extensions", "icon": "💥", "sets": "3×15", "video": "https://www.youtube.com/watch?v=_gsUck-7M74"},
    ]},
    "Ven": {"titre": "Jambes & Core", "duree": "40", "kcal": "350", "couleur": "#10b981", "exercices": [
        {"nom": "Squats", "icon": "🦵", "sets": "4×20", "video": "https://www.youtube.com/watch?v=aclHkVaku9U"},
        {"nom": "Fentes marchées", "icon": "🚶", "sets": "3×20", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"},
        {"nom": "Pont fessier", "icon": "🌉", "sets": "4×15", "video": "https://www.youtube.com/watch?v=AVAXhy6pl7o"},
        {"nom": "Squats bulgares", "icon": "🇧🇬", "sets": "3×12", "video": "https://www.youtube.com/watch?v=2C-uNgKwPLE"},
        {"nom": "Mollets", "icon": "🦶", "sets": "4×25", "video": "https://www.youtube.com/watch?v=gwLzBJYoWlI"},
    ]},
}

PROGRAMME_SONIA = {
    "Lun": {"titre": "Cardio Brûle-Graisse", "duree": "30", "kcal": "350", "couleur": "#ef4444", "exercices": [
        {"nom": "Jumping jacks", "icon": "⭐", "sets": "4×45s", "video": "https://www.youtube.com/watch?v=c4DAnQ6DtF8"},
        {"nom": "High knees", "icon": "🦵", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=D0CzP4JHbKQ"},
        {"nom": "Burpees modifiés", "icon": "🔥", "sets": "3×10", "video": "https://www.youtube.com/watch?v=dZgVxmf6jkA"},
        {"nom": "Mountain climbers", "icon": "⛰️", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=nmwgirgXLYM"},
        {"nom": "Squat jumps", "icon": "🦘", "sets": "3×12", "video": "https://www.youtube.com/watch?v=U4s4mEQ5VqU"},
    ]},
    "Mar": {"titre": "Cuisses & Fessiers", "duree": "35", "kcal": "280", "couleur": "#ec4899", "exercices": [
        {"nom": "Squats", "icon": "🦵", "sets": "4×20", "video": "https://www.youtube.com/watch?v=aclHkVaku9U"},
        {"nom": "Sumo squats", "icon": "🏋️", "sets": "4×15", "video": "https://www.youtube.com/watch?v=9ZuXKqRbT9k"},
        {"nom": "Pont fessier", "icon": "🌉", "sets": "4×25", "video": "https://www.youtube.com/watch?v=OUgsJ8-Vi0E"},
        {"nom": "Donkey kicks", "icon": "🐴", "sets": "3×20", "video": "https://www.youtube.com/watch?v=BX67kECR0h0"},
        {"nom": "Fire hydrant", "icon": "🔥", "sets": "3×15", "video": "https://www.youtube.com/watch?v=La3xYT8MGks"},
    ]},
    "Mer": {"titre": "HIIT Brûle-Graisse", "duree": "25", "kcal": "400", "couleur": "#f97316", "exercices": [
        {"nom": "Burpees", "icon": "🔥", "sets": "4×8", "video": "https://www.youtube.com/watch?v=dZgVxmf6jkA"},
        {"nom": "Speed skaters", "icon": "⛸️", "sets": "4×30s", "video": "https://www.youtube.com/watch?v=d1J3bkXgQf4"},
        {"nom": "Squat pulses", "icon": "💫", "sets": "3×30s", "video": "https://www.youtube.com/watch?v=WGE1DYu9g5s"},
        {"nom": "Step ups", "icon": "📦", "sets": "3×15", "video": "https://www.youtube.com/watch?v=dQqApCGd5Ss"},
        {"nom": "Planche", "icon": "📏", "sets": "4×45s", "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c"},
    ]},
    "Jeu": {"titre": "Haut du Corps & Abdos", "duree": "30", "kcal": "220", "couleur": "#8b5cf6", "exercices": [
        {"nom": "Pompes sur genoux", "icon": "💪", "sets": "4×12", "video": "https://www.youtube.com/watch?v=jWxvty2KROs"},
        {"nom": "Dips sur chaise", "icon": "🪑", "sets": "3×12", "video": "https://www.youtube.com/watch?v=HCf97NPYeGY"},
        {"nom": "Crunchs", "icon": "🎯", "sets": "4×20", "video": "https://www.youtube.com/watch?v=Xyd_fa5zoEU"},
        {"nom": "Bicycle crunch", "icon": "🚴", "sets": "3×20", "video": "https://www.youtube.com/watch?v=9FGilxCbdz8"},
        {"nom": "Planche latérale", "icon": "📐", "sets": "3×30s", "video": "https://www.youtube.com/watch?v=K2VljzCC16g"},
    ]},
    "Ven": {"titre": "Full Body", "duree": "35", "kcal": "380", "couleur": "#10b981", "exercices": [
        {"nom": "Jumping jacks", "icon": "⭐", "sets": "3×1min", "video": "https://www.youtube.com/watch?v=c4DAnQ6DtF8"},
        {"nom": "Squats + press", "icon": "🏋️", "sets": "4×15", "video": "https://www.youtube.com/watch?v=nKxPrWyTU4k"},
        {"nom": "Pompes", "icon": "💪", "sets": "3×10", "video": "https://www.youtube.com/watch?v=jWxvty2KROs"},
        {"nom": "Fentes alternées", "icon": "🚶", "sets": "3×20", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"},
        {"nom": "Planche", "icon": "📏", "sets": "3×1min", "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c"},
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

    st.markdown("""<div class="week-calendar"><div class="week-title">📅 Cette semaine</div><div class="week-days">""", unsafe_allow_html=True)

    jours_html = ""
    for jour in JOURS_SEMAINE:
        is_done = jour in completed
        classe = "completed" if is_done else ""
        check = "✓" if is_done else ""
        jours_html += f"""
        <div class="day-item {classe}">
            <div class="day-letter">{jour}</div>
            <div class="day-number">{check if is_done else "○"}</div>
        </div>
        """

    st.markdown(jours_html + "</div></div>", unsafe_allow_html=True)

    # Boutons pour cocher/décocher
    cols = st.columns(5)
    for i, jour in enumerate(JOURS_SEMAINE):
        with cols[i]:
            is_done = jour in completed
            label = "✓" if is_done else "○"
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
