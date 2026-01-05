import streamlit as st
import json
from datetime import datetime, date
import os

# Configuration de la page
st.set_page_config(
    page_title="🏋️ Programme Sport Maison",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fichier pour sauvegarder les données
DATA_FILE = "progress_data.json"

def load_data():
    """Charge les données sauvegardées"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "luca": {"poids_history": [], "seances_completees": [], "poids_actuel": 88},
        "sonia": {"poids_history": [], "seances_completees": [], "poids_actuel": 75}
    }

def save_data(data):
    """Sauvegarde les données"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Charger les données
if 'data' not in st.session_state:
    st.session_state.data = load_data()

# Citations motivantes
CITATIONS = [
    "💪 La douleur d'aujourd'hui est la force de demain !",
    "🔥 Chaque répétition te rapproche de ton objectif !",
    "⭐ Tu es plus fort(e) que tu ne le penses !",
    "🏆 Les champions sont faits de sueur et de persévérance !",
    "💫 Ton seul concurrent, c'est toi d'hier !",
    "🎯 Un petit progrès chaque jour mène à de grands résultats !",
    "🚀 La discipline bat la motivation !",
    "💎 Ton corps peut tout supporter, c'est ton mental qu'il faut convaincre !",
    "🌟 Pas d'excuses, que des résultats !",
    "⚡ La sueur d'aujourd'hui, c'est le sourire de demain !"
]

# CSS personnalisé pour un design professionnel
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 10px 30px;
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        color: white;
        font-weight: 600;
        font-size: 16px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }

    .profile-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
    }

    .profile-card-luca {
        background: linear-gradient(145deg, rgba(102,126,234,0.2), rgba(118,75,162,0.1));
    }

    .profile-card-sonia {
        background: linear-gradient(145deg, rgba(236,72,153,0.2), rgba(239,68,68,0.1));
    }

    .profile-name {
        font-size: 32px;
        font-weight: 700;
        color: white;
        margin-bottom: 5px;
    }

    .profile-stats {
        display: flex;
        gap: 20px;
        margin-top: 15px;
        flex-wrap: wrap;
    }

    .stat-item {
        background: rgba(255,255,255,0.1);
        padding: 10px 20px;
        border-radius: 10px;
        text-align: center;
    }

    .stat-value {
        font-size: 20px;
        font-weight: 600;
        color: #fff;
    }

    .stat-label {
        font-size: 12px;
        color: rgba(255,255,255,0.7);
    }

    .objective-box {
        background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(16,185,129,0.1));
        border-left: 4px solid #22c55e;
        padding: 15px 20px;
        border-radius: 0 10px 10px 0;
        margin-top: 15px;
    }

    .objective-title {
        color: #22c55e;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 5px;
    }

    .objective-text {
        color: white;
        font-size: 14px;
    }

    .materiel-box {
        background: linear-gradient(135deg, rgba(59,130,246,0.2), rgba(37,99,235,0.1));
        border-left: 4px solid #3b82f6;
        padding: 15px 20px;
        border-radius: 0 10px 10px 0;
        margin-top: 10px;
    }

    .materiel-title {
        color: #3b82f6;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 5px;
    }

    .materiel-text {
        color: white;
        font-size: 13px;
    }

    .motivation-box {
        background: linear-gradient(135deg, rgba(245,158,11,0.3), rgba(234,88,12,0.2));
        border: 2px solid #f59e0b;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
    }

    .motivation-text {
        color: #fbbf24;
        font-size: 18px;
        font-weight: 600;
    }

    .progress-box {
        background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .progress-title {
        color: white;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .streak-box {
        background: linear-gradient(135deg, rgba(239,68,68,0.2), rgba(220,38,38,0.1));
        border: 2px solid #ef4444;
        padding: 15px 25px;
        border-radius: 15px;
        text-align: center;
        display: inline-block;
    }

    .streak-number {
        font-size: 36px;
        font-weight: 700;
        color: #ef4444;
    }

    .streak-label {
        font-size: 12px;
        color: rgba(255,255,255,0.7);
    }

    .day-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .day-card:hover {
        transform: translateY(-5px);
        border-color: rgba(102,126,234,0.5);
        box-shadow: 0 10px 30px rgba(102,126,234,0.2);
    }

    .day-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }

    .day-name {
        font-size: 18px;
        font-weight: 600;
        color: white;
    }

    .day-badge {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 12px;
        color: white;
        font-weight: 500;
    }

    .day-badge-cardio {
        background: linear-gradient(135deg, #f97316, #ef4444);
    }

    .day-badge-repos {
        background: linear-gradient(135deg, #22c55e, #10b981);
    }

    .exercise-item {
        background: rgba(255,255,255,0.05);
        padding: 12px 15px;
        border-radius: 10px;
        margin: 8px 0;
        display: flex;
        align-items: center;
        gap: 10px;
        color: rgba(255,255,255,0.9);
        font-size: 14px;
    }

    .exercise-icon {
        font-size: 20px;
    }

    .video-container {
        background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .video-title {
        font-size: 20px;
        font-weight: 600;
        color: white;
        margin-bottom: 15px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 10px;
        font-weight: 500;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(102,126,234,0.4);
    }

    .btn-sonia > button {
        background: linear-gradient(135deg, #ec4899 0%, #ef4444 100%) !important;
    }

    h1, h2, h3 {
        color: white !important;
    }

    .calendar-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.1));
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .calendar-title {
        font-size: 24px;
        font-weight: 700;
        color: white;
    }

    .calendar-subtitle {
        font-size: 14px;
        color: rgba(255,255,255,0.7);
    }

    /* Progress bar custom */
    .progress-container {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        height: 25px;
        margin: 10px 0;
        overflow: hidden;
    }

    .progress-bar-luca {
        background: linear-gradient(90deg, #667eea, #764ba2);
        height: 100%;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 12px;
        transition: width 0.5s ease;
    }

    .progress-bar-sonia {
        background: linear-gradient(90deg, #ec4899, #ef4444);
        height: 100%;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 12px;
        transition: width 0.5s ease;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
    }

    /* Checkbox styling */
    .stCheckbox {
        background: rgba(255,255,255,0.05);
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PROGRAMMES OPTIMISÉS - MEILLEURS EXERCICES MAISON SANS/PEU MATÉRIEL
# ============================================================================

# Programme LUCA - Prise de masse + Abdos + Bras (1m95, 88kg -> 90kg muscle)
PROGRAMME_LUCA = {
    "Lundi": {
        "type": "Pectoraux & Triceps",
        "badge_class": "",
        "exercices": [
            {"nom": "Pompes classiques", "icon": "💪", "series": "4x20", "video": "https://www.youtube.com/watch?v=IODxDxX7oi4", "desc": "Base pour pectoraux"},
            {"nom": "Pompes diamant", "icon": "💎", "series": "4x12", "video": "https://www.youtube.com/watch?v=J0DnG1_S92I", "desc": "Triceps + pecs intérieurs"},
            {"nom": "Pompes déclinées (pieds surélevés)", "icon": "📐", "series": "3x15", "video": "https://www.youtube.com/watch?v=SKPab2YC9AY", "desc": "Haut des pectoraux"},
            {"nom": "Pompes archer", "icon": "🏹", "series": "3x8/côté", "video": "https://www.youtube.com/watch?v=LpnJXyuRsWg", "desc": "Force unilatérale"},
            {"nom": "Dips sur chaises", "icon": "🪑", "series": "4x15", "video": "https://www.youtube.com/watch?v=HCf97NPYeGY", "desc": "Triceps puissants"},
            {"nom": "Pompes serrées", "icon": "🔥", "series": "3x15", "video": "https://www.youtube.com/watch?v=5M7JMb5jhq4", "desc": "Finition triceps"},
        ]
    },
    "Mardi": {
        "type": "Dos & Biceps",
        "badge_class": "",
        "exercices": [
            {"nom": "Tractions pronation (barre de porte)", "icon": "🚪", "series": "4x max", "video": "https://www.youtube.com/watch?v=eGo4IYlbE5g", "desc": "Meilleur exo dos"},
            {"nom": "Tractions supination (chin-ups)", "icon": "💪", "series": "3x max", "video": "https://www.youtube.com/watch?v=brhRXlOhWB8", "desc": "Dos + biceps"},
            {"nom": "Rowing inversé (sous une table)", "icon": "🪑", "series": "4x12", "video": "https://www.youtube.com/watch?v=OYUxXMGVuuU", "desc": "Épaisseur dos"},
            {"nom": "Superman hold", "icon": "🦸", "series": "4x30sec", "video": "https://www.youtube.com/watch?v=cc6UVRS7PW4", "desc": "Lombaires"},
            {"nom": "Curl biceps (bouteilles d'eau 5-6L)", "icon": "🍶", "series": "4x15", "video": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo", "desc": "Volume biceps"},
            {"nom": "Curl isométrique (serviette)", "icon": "🧲", "series": "3x20sec", "video": "https://www.youtube.com/watch?v=nRXF8LZqqss", "desc": "Intensité max"},
        ]
    },
    "Mercredi": {
        "type": "Abdos Intenses",
        "badge_class": "day-badge-cardio",
        "exercices": [
            {"nom": "Crunchs", "icon": "🎯", "series": "4x25", "video": "https://www.youtube.com/watch?v=Xyd_fa5zoEU", "desc": "Abdos supérieurs"},
            {"nom": "Relevé de jambes au sol", "icon": "🦵", "series": "4x15", "video": "https://www.youtube.com/watch?v=JB2oyawG9KI", "desc": "Abdos inférieurs"},
            {"nom": "Planche", "icon": "📏", "series": "4x1min", "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c", "desc": "Gainage profond"},
            {"nom": "Planche latérale", "icon": "📐", "series": "3x45sec/côté", "video": "https://www.youtube.com/watch?v=K2VljzCC16g", "desc": "Obliques"},
            {"nom": "Mountain climbers", "icon": "⛰️", "series": "4x30sec", "video": "https://www.youtube.com/watch?v=nmwgirgXLYM", "desc": "Cardio + abdos"},
            {"nom": "Bicycle crunch", "icon": "🚴", "series": "3x20", "video": "https://www.youtube.com/watch?v=9FGilxCbdz8", "desc": "Obliques définition"},
            {"nom": "Dead bug", "icon": "🐛", "series": "3x12/côté", "video": "https://www.youtube.com/watch?v=4XLEnwUr1d8", "desc": "Stabilisation core"},
        ]
    },
    "Jeudi": {
        "type": "Épaules & Bras",
        "badge_class": "",
        "exercices": [
            {"nom": "Pike push-ups", "icon": "🔺", "series": "4x12", "video": "https://www.youtube.com/watch?v=sposDXWEB0A", "desc": "Épaules avant"},
            {"nom": "Handstand contre mur", "icon": "🤸", "series": "3x30sec", "video": "https://www.youtube.com/watch?v=xIdKwIB3M3E", "desc": "Épaules complètes"},
            {"nom": "Élévations latérales (bouteilles)", "icon": "🦅", "series": "4x15", "video": "https://www.youtube.com/watch?v=3VcKaXpzqRo", "desc": "Deltoïdes latéraux"},
            {"nom": "Pompes pseudo planche", "icon": "🏋️", "series": "3x10", "video": "https://www.youtube.com/watch?v=odcPqBOlJlY", "desc": "Épaules avant intenses"},
            {"nom": "Curl marteau (bouteilles)", "icon": "🔨", "series": "4x12", "video": "https://www.youtube.com/watch?v=zC3nLlEvin4", "desc": "Brachial + biceps"},
            {"nom": "Triceps extensions sol", "icon": "💥", "series": "3x12", "video": "https://www.youtube.com/watch?v=_gsUck-7M74", "desc": "Longue portion triceps"},
        ]
    },
    "Vendredi": {
        "type": "Jambes & Core",
        "badge_class": "",
        "exercices": [
            {"nom": "Squats", "icon": "🦵", "series": "4x20", "video": "https://www.youtube.com/watch?v=aclHkVaku9U", "desc": "Quadriceps"},
            {"nom": "Squats bulgares", "icon": "🇧🇬", "series": "3x12/jambe", "video": "https://www.youtube.com/watch?v=2C-uNgKwPLE", "desc": "Force unilatérale"},
            {"nom": "Fentes marchées", "icon": "🚶", "series": "3x20 total", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U", "desc": "Jambes complètes"},
            {"nom": "Pont fessier une jambe", "icon": "🌉", "series": "3x15/jambe", "video": "https://www.youtube.com/watch?v=AVAXhy6pl7o", "desc": "Fessiers puissants"},
            {"nom": "Pistol squat (assisté)", "icon": "🔫", "series": "3x5/jambe", "video": "https://www.youtube.com/watch?v=vq5-vdgJc0I", "desc": "Force avancée"},
            {"nom": "Mollets sur marche", "icon": "🦶", "series": "4x25", "video": "https://www.youtube.com/watch?v=gwLzBJYoWlI", "desc": "Mollets"},
            {"nom": "Hollow body hold", "icon": "🍌", "series": "3x30sec", "video": "https://www.youtube.com/watch?v=LlDNef_Ztsc", "desc": "Core profond"},
        ]
    }
}

# Programme SONIA - Perte de poids (1m50, 75kg -> 60-65kg)
PROGRAMME_SONIA = {
    "Lundi": {
        "type": "Cardio Brûle-Graisse",
        "badge_class": "day-badge-cardio",
        "exercices": [
            {"nom": "Jumping jacks", "icon": "⭐", "series": "4x45sec", "video": "https://www.youtube.com/watch?v=c4DAnQ6DtF8", "desc": "Échauffement cardio"},
            {"nom": "High knees (genoux hauts)", "icon": "🦵", "series": "4x30sec", "video": "https://www.youtube.com/watch?v=D0CzP4JHbKQ", "desc": "Brûle calories"},
            {"nom": "Burpees modifiés", "icon": "🔥", "series": "3x10", "video": "https://www.youtube.com/watch?v=dZgVxmf6jkA", "desc": "Full body intense"},
            {"nom": "Mountain climbers", "icon": "⛰️", "series": "4x30sec", "video": "https://www.youtube.com/watch?v=nmwgirgXLYM", "desc": "Cardio + abdos"},
            {"nom": "Squat jumps", "icon": "🦘", "series": "3x12", "video": "https://www.youtube.com/watch?v=U4s4mEQ5VqU", "desc": "Jambes explosives"},
            {"nom": "Corde à sauter (ou sans corde)", "icon": "🪢", "series": "3x1min", "video": "https://www.youtube.com/watch?v=u3zgHI8QnqE", "desc": "Cardio efficace"},
        ]
    },
    "Mardi": {
        "type": "Cuisses & Fessiers",
        "badge_class": "",
        "exercices": [
            {"nom": "Squats", "icon": "🦵", "series": "4x20", "video": "https://www.youtube.com/watch?v=aclHkVaku9U", "desc": "Base cuisses"},
            {"nom": "Sumo squats", "icon": "🏋️", "series": "4x15", "video": "https://www.youtube.com/watch?v=9ZuXKqRbT9k", "desc": "Intérieur cuisses"},
            {"nom": "Fentes arrière", "icon": "🚶", "series": "3x12/jambe", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U", "desc": "Galbe cuisses"},
            {"nom": "Pont fessier", "icon": "🌉", "series": "4x25", "video": "https://www.youtube.com/watch?v=OUgsJ8-Vi0E", "desc": "Fessiers bombés"},
            {"nom": "Donkey kicks", "icon": "🐴", "series": "3x20/jambe", "video": "https://www.youtube.com/watch?v=BX67kECR0h0", "desc": "Haut des fessiers"},
            {"nom": "Fire hydrant", "icon": "🔥", "series": "3x15/jambe", "video": "https://www.youtube.com/watch?v=La3xYT8MGks", "desc": "Fessiers côtés"},
            {"nom": "Clam shells", "icon": "🐚", "series": "3x20/côté", "video": "https://www.youtube.com/watch?v=kfUgsfeEj_4", "desc": "Hanches"},
        ]
    },
    "Mercredi": {
        "type": "HIIT Brûle-Graisse",
        "badge_class": "day-badge-cardio",
        "exercices": [
            {"nom": "Burpees sans saut", "icon": "🔥", "series": "4x8", "video": "https://www.youtube.com/watch?v=dZgVxmf6jkA", "desc": "Full body"},
            {"nom": "Speed skaters", "icon": "⛸️", "series": "4x30sec", "video": "https://www.youtube.com/watch?v=d1J3bkXgQf4", "desc": "Cardio latéral"},
            {"nom": "Squat pulses", "icon": "💫", "series": "3x30sec", "video": "https://www.youtube.com/watch?v=WGE1DYu9g5s", "desc": "Brûle cuisses"},
            {"nom": "Step ups (sur marche/chaise)", "icon": "📦", "series": "3x15/jambe", "video": "https://www.youtube.com/watch?v=dQqApCGd5Ss", "desc": "Cardio + jambes"},
            {"nom": "Planche", "icon": "📏", "series": "4x45sec", "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c", "desc": "Gainage"},
            {"nom": "Jumping lunges (ou alternées)", "icon": "🦘", "series": "3x10/jambe", "video": "https://www.youtube.com/watch?v=y7Iug7eC0dk", "desc": "Explosivité"},
        ]
    },
    "Jeudi": {
        "type": "Haut du Corps & Abdos",
        "badge_class": "",
        "exercices": [
            {"nom": "Pompes sur genoux", "icon": "💪", "series": "4x12", "video": "https://www.youtube.com/watch?v=jWxvty2KROs", "desc": "Pectoraux débutant"},
            {"nom": "Pompes inclinées (sur table)", "icon": "📐", "series": "3x15", "video": "https://www.youtube.com/watch?v=4dF1DOWzf20", "desc": "Progression pompes"},
            {"nom": "Dips sur chaise", "icon": "🪑", "series": "3x12", "video": "https://www.youtube.com/watch?v=HCf97NPYeGY", "desc": "Triceps"},
            {"nom": "Crunchs", "icon": "🎯", "series": "4x20", "video": "https://www.youtube.com/watch?v=Xyd_fa5zoEU", "desc": "Abdos hauts"},
            {"nom": "Bicycle crunch", "icon": "🚴", "series": "3x20", "video": "https://www.youtube.com/watch?v=9FGilxCbdz8", "desc": "Obliques"},
            {"nom": "Leg raises au sol", "icon": "🦵", "series": "3x15", "video": "https://www.youtube.com/watch?v=JB2oyawG9KI", "desc": "Abdos bas"},
            {"nom": "Planche latérale", "icon": "📐", "series": "3x30sec/côté", "video": "https://www.youtube.com/watch?v=K2VljzCC16g", "desc": "Taille fine"},
        ]
    },
    "Vendredi": {
        "type": "Full Body Brûle-Graisse",
        "badge_class": "day-badge-cardio",
        "exercices": [
            {"nom": "Jumping jacks", "icon": "⭐", "series": "3x1min", "video": "https://www.youtube.com/watch?v=c4DAnQ6DtF8", "desc": "Échauffement"},
            {"nom": "Squats + press épaules", "icon": "🏋️", "series": "4x15", "video": "https://www.youtube.com/watch?v=nKxPrWyTU4k", "desc": "Combo complet"},
            {"nom": "Pompes sur genoux", "icon": "💪", "series": "3x10", "video": "https://www.youtube.com/watch?v=jWxvty2KROs", "desc": "Haut du corps"},
            {"nom": "Fentes alternées", "icon": "🚶", "series": "3x20 total", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U", "desc": "Jambes"},
            {"nom": "Mountain climbers", "icon": "⛰️", "series": "4x30sec", "video": "https://www.youtube.com/watch?v=nmwgirgXLYM", "desc": "Cardio final"},
            {"nom": "Planche", "icon": "📏", "series": "3x1min", "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c", "desc": "Finition core"},
            {"nom": "Stretch récupération", "icon": "🧘", "series": "5min", "video": "https://www.youtube.com/watch?v=g_tea8ZNk5A", "desc": "Récupération"},
        ]
    }
}

def afficher_motivation():
    """Affiche une citation motivante aléatoire"""
    import random
    citation = random.choice(CITATIONS)
    st.markdown(f"""
    <div class="motivation-box">
        <div class="motivation-text">{citation}</div>
    </div>
    """, unsafe_allow_html=True)

def afficher_progression(prefix, poids_initial, poids_objectif, is_perte=False):
    """Affiche la section de suivi de progression"""
    data = st.session_state.data[prefix]

    st.markdown("### 📊 Suivi de Progression")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Mise à jour du poids
        st.markdown("**📝 Mettre à jour ton poids**")
        new_poids = st.number_input(
            "Poids actuel (kg)",
            min_value=40.0,
            max_value=150.0,
            value=float(data.get('poids_actuel', poids_initial)),
            step=0.1,
            key=f"{prefix}_poids_input"
        )

        if st.button("💾 Enregistrer", key=f"{prefix}_save_poids"):
            today = str(date.today())
            # Éviter les doublons pour le même jour
            history = data.get('poids_history', [])
            history = [h for h in history if h['date'] != today]
            history.append({'date': today, 'poids': new_poids})
            data['poids_history'] = history[-30:]  # Garder les 30 derniers
            data['poids_actuel'] = new_poids
            st.session_state.data[prefix] = data
            save_data(st.session_state.data)
            st.success("✅ Poids enregistré !")
            st.rerun()

    with col2:
        # Calcul de la progression
        poids_actuel = data.get('poids_actuel', poids_initial)

        if is_perte:
            # Pour la perte de poids
            total_a_perdre = poids_initial - poids_objectif
            deja_perdu = poids_initial - poids_actuel
            progression = min(max((deja_perdu / total_a_perdre) * 100, 0), 100) if total_a_perdre > 0 else 0
            restant = poids_actuel - poids_objectif
        else:
            # Pour la prise de masse
            total_a_prendre = poids_objectif - poids_initial
            deja_pris = poids_actuel - poids_initial
            progression = min(max((deja_pris / total_a_prendre) * 100, 0), 100) if total_a_prendre > 0 else 0
            restant = poids_objectif - poids_actuel

        st.markdown(f"""
        <div style="text-align: center; padding: 15px;">
            <div style="font-size: 14px; color: rgba(255,255,255,0.7);">Progression</div>
            <div style="font-size: 32px; font-weight: 700; color: {'#22c55e' if progression >= 50 else '#f59e0b'};">{progression:.1f}%</div>
            <div style="font-size: 12px; color: rgba(255,255,255,0.5);">{'Reste ' + str(abs(round(restant, 1))) + ' kg'}</div>
        </div>
        """, unsafe_allow_html=True)

    # Barre de progression
    bar_class = "progress-bar-sonia" if is_perte else "progress-bar-luca"
    st.markdown(f"""
    <div class="progress-container">
        <div class="{bar_class}" style="width: {progression}%;">
            {progression:.0f}%
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Historique graphique
    if data.get('poids_history'):
        st.markdown("**📈 Évolution du poids**")
        history = data['poids_history']
        dates = [h['date'] for h in history]
        poids_list = [h['poids'] for h in history]

        chart_data = {"Date": dates, "Poids (kg)": poids_list}
        st.line_chart(chart_data, x="Date", y="Poids (kg)")

def afficher_seances_semaine(prefix, programme):
    """Affiche le tracker de séances de la semaine"""
    data = st.session_state.data[prefix]
    seances = data.get('seances_completees', [])
    today = str(date.today())
    week_start = str(date.today().isocalendar()[1])

    st.markdown("### ✅ Séances de la semaine")

    cols = st.columns(5)
    jours = list(programme.keys())

    for idx, jour in enumerate(jours):
        with cols[idx]:
            seance_key = f"{week_start}_{jour}"
            is_done = seance_key in seances

            if st.checkbox(
                f"{'✅' if is_done else '⬜'} {jour}",
                value=is_done,
                key=f"{prefix}_check_{jour}"
            ):
                if seance_key not in seances:
                    seances.append(seance_key)
            else:
                if seance_key in seances:
                    seances.remove(seance_key)

    # Sauvegarder
    data['seances_completees'] = seances[-50:]  # Garder les 50 dernières
    st.session_state.data[prefix] = data
    save_data(st.session_state.data)

    # Afficher le nombre de séances cette semaine
    seances_semaine = len([s for s in seances if s.startswith(week_start)])
    st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <span style="font-size: 24px; font-weight: 700; color: #22c55e;">{seances_semaine}/5</span>
        <span style="color: rgba(255,255,255,0.7);"> séances cette semaine</span>
    </div>
    """, unsafe_allow_html=True)

def afficher_profil_luca():
    poids_actuel = st.session_state.data['luca'].get('poids_actuel', 88)
    st.markdown(f"""
    <div class="profile-card profile-card-luca">
        <div class="profile-name">👨 LUCA</div>
        <div class="profile-stats">
            <div class="stat-item">
                <div class="stat-value">1m95</div>
                <div class="stat-label">Taille</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{poids_actuel} kg</div>
                <div class="stat-label">Poids actuel</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">90 kg</div>
                <div class="stat-label">Objectif</div>
            </div>
        </div>
        <div class="objective-box">
            <div class="objective-title">🎯 OBJECTIFS</div>
            <div class="objective-text">Prise de masse musculaire • Perdre du ventre • Abdos visibles • Bras musclés</div>
        </div>
        <div class="materiel-box">
            <div class="materiel-title">🛠️ MATÉRIEL CONSEILLÉ (optionnel)</div>
            <div class="materiel-text">Barre de traction porte (~15€) • Bouteilles d'eau 5-6L • 2 chaises solides</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def afficher_profil_sonia():
    poids_actuel = st.session_state.data['sonia'].get('poids_actuel', 75)
    st.markdown(f"""
    <div class="profile-card profile-card-sonia">
        <div class="profile-name">👩 SONIA</div>
        <div class="profile-stats">
            <div class="stat-item">
                <div class="stat-value">1m50</div>
                <div class="stat-label">Taille</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{poids_actuel} kg</div>
                <div class="stat-label">Poids actuel</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">60-65 kg</div>
                <div class="stat-label">Objectif</div>
            </div>
        </div>
        <div class="objective-box">
            <div class="objective-title">🎯 OBJECTIFS</div>
            <div class="objective-text">Perdre 10 à 15 kg • Tonifier cuisses & fessiers • Ventre plat</div>
        </div>
        <div class="materiel-box">
            <div class="materiel-title">🛠️ MATÉRIEL CONSEILLÉ (optionnel)</div>
            <div class="materiel-text">Tapis de yoga (~10€) • Corde à sauter (~5€) • Une chaise ou marche</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def afficher_calendrier(programme, prefix):
    """Affiche le calendrier avec les exercices"""

    st.markdown("""
    <div class="calendar-header">
        <div class="calendar-title">📅 Programme de la Semaine</div>
        <div class="calendar-subtitle">Clique sur un exercice pour voir le tutoriel vidéo en français</div>
    </div>
    """, unsafe_allow_html=True)

    jours = list(programme.keys())

    # Créer 5 colonnes pour les 5 jours
    cols = st.columns(5)

    for idx, jour in enumerate(jours):
        with cols[idx]:
            info = programme[jour]
            badge_class = info.get("badge_class", "")

            st.markdown(f"""
            <div class="day-card">
                <div class="day-header">
                    <span class="day-name">{jour}</span>
                </div>
                <span class="day-badge {badge_class}">{info['type']}</span>
            </div>
            """, unsafe_allow_html=True)

            # Afficher les exercices comme boutons
            for ex in info["exercices"]:
                button_label = f"{ex['icon']} {ex['nom']}"
                if st.button(button_label, key=f"{prefix}_{jour}_{ex['nom']}", use_container_width=True, help=ex.get('desc', '')):
                    st.session_state[f"{prefix}_selected_exercise"] = ex
                    st.session_state[f"{prefix}_selected_day"] = jour

def afficher_video(prefix):
    """Affiche la vidéo sélectionnée"""
    key_exercise = f"{prefix}_selected_exercise"
    key_day = f"{prefix}_selected_day"

    if key_exercise in st.session_state and st.session_state[key_exercise]:
        ex = st.session_state[key_exercise]
        jour = st.session_state.get(key_day, "")

        st.markdown("---")

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(f"""
            <div class="video-container">
                <div class="video-title">{ex['icon']} {ex['nom']}</div>
                <p style="color: rgba(255,255,255,0.7); margin-bottom: 10px;">
                    <strong>Séries:</strong> {ex['series']} | <strong>{ex.get('desc', '')}</strong>
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Extraire l'ID de la vidéo YouTube
            video_url = ex['video']
            if "watch?v=" in video_url:
                video_id = video_url.split("watch?v=")[1].split("&")[0]
            else:
                video_id = video_url.split("/")[-1]

            # Afficher la vidéo
            st.video(f"https://www.youtube.com/watch?v={video_id}")

            if st.button("❌ Fermer la vidéo", key=f"{prefix}_close", use_container_width=True):
                st.session_state[key_exercise] = None
                st.rerun()

# Titre principal
st.markdown("""
<h1 style="text-align: center; font-size: 2.5rem; margin-bottom: 10px;">
    🏋️ Programme Sport Maison 💪
</h1>
<p style="text-align: center; color: rgba(255,255,255,0.6); margin-bottom: 30px;">
    Sans matériel ou avec très peu • Exercices efficaces à la maison
</p>
""", unsafe_allow_html=True)

# Citation motivante
afficher_motivation()

# Création des onglets
tab1, tab2 = st.tabs(["👨 LUCA - Prise de Masse", "👩 SONIA - Perte de Poids"])

with tab1:
    afficher_profil_luca()

    # Section progression
    with st.expander("📊 **SUIVI DE PROGRESSION** - Clique pour ouvrir", expanded=True):
        afficher_progression("luca", poids_initial=88, poids_objectif=90, is_perte=False)
        st.markdown("---")
        afficher_seances_semaine("luca", PROGRAMME_LUCA)

    st.markdown("---")
    afficher_calendrier(PROGRAMME_LUCA, "luca")
    afficher_video("luca")

with tab2:
    afficher_profil_sonia()

    # Section progression
    with st.expander("📊 **SUIVI DE PROGRESSION** - Clique pour ouvrir", expanded=True):
        afficher_progression("sonia", poids_initial=75, poids_objectif=62.5, is_perte=True)
        st.markdown("---")
        afficher_seances_semaine("sonia", PROGRAMME_SONIA)

    st.markdown("---")
    afficher_calendrier(PROGRAMME_SONIA, "sonia")
    afficher_video("sonia")

# Footer avec conseils
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.7); padding: 20px;">
    <h3 style="color: #22c55e;">💡 Conseils pour réussir</h3>
    <p>💧 <strong>Bois 2-3L d'eau par jour</strong> • 🍎 <strong>Mange équilibré (protéines à chaque repas)</strong></p>
    <p>😴 <strong>Dors 7-8h minimum</strong> • 📈 <strong>La régularité > L'intensité</strong></p>
    <p style="font-size: 12px; margin-top: 15px; color: rgba(255,255,255,0.5);">
        Weekend = repos actif (marche, étirements) pour récupérer 🧘
    </p>
</div>
""", unsafe_allow_html=True)
