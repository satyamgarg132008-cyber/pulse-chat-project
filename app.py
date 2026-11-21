import os
import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PulseChat - Real-Time Animated Chat",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- AUTO-REFRESH (Pulls new incoming messages every 2.5 seconds) ---
st_autorefresh(interval=2500, key="pulse_chat_sync_timer")

# --- HIGH-TECH ANIMATED NEON CSS & KEYFRAMES ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Ambient Floating Gradient Mesh */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 10% 15%, rgba(139, 92, 246, 0.22) 0%, transparent 45%),
                    radial-gradient(circle at 90% 85%, rgba(6, 182, 212, 0.22) 0%, transparent 45%),
                    radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.15) 0%, transparent 55%),
                    #070a13 !important;
        color: #f8fafc;
        overflow-x: hidden;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e1322 0%, #06080e 100%) !important;
        border-right: 1px solid rgba(139, 92, 246, 0.25) !important;
    }

    /* Keyframe Animations */
    @keyframes floatOrb {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-20px) scale(1.08); }
    }
    @keyframes slideUpBounce {
        0% { opacity: 0; transform: translateY(18px) scale(0.97); }
        70% { opacity: 0.9; transform: translateY(-3px) scale(1.01); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    @keyframes pulseRadar {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
    }
    @keyframes shimmerText {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    /* Animated Header */
    .chat-header-title {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #c084fc, #38bdf8, #f472b6, #c084fc);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmerText 8s linear infinite;
        margin-bottom: 0.2rem;
    }

    /* Radar Live Indicator */
    .radar-dot {
        width: 10px;
        height: 10px;
        background: #10b981;
        border-radius: 50%;
        display: inline-block;
        animation: pulseRadar 2s infinite;
        margin-right: 6px;
    }

    .live-badge {
        display: inline-flex;
        align-items: center;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 9999px;
        padding: 0.25rem 0.85rem;
        font-size: 0.78rem;
        font-weight: 800;
        color: #34d399;
        letter-spacing: 0.5px;
    }

    /* Message Bubbles with Slide-in Animation */
    .msg-bubble-self {
        animation: slideUpBounce 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.35) 0%, rgba(6, 182, 212, 0.25) 100%);
        border: 1px solid rgba(192, 132, 252, 0.4);
        border-radius: 1.3rem 1.3rem 0.2rem 1.3rem;
        padding: 0.9rem 1.4rem;
        margin-left: auto;
        max-width: 78%;
        margin-bottom: 0.9rem;
        box-shadow: 0 8px 25px rgba(147, 51, 234, 0.25);
        transition: transform 0.2s ease;
    }
    .msg-bubble-self:hover {
        transform: translateY(-2px) scale(1.01);
        border-color: rgba(56, 189, 248, 0.6);
    }

    .msg-bubble-other {
        animation: slideUpBounce 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        background: rgba(17, 24, 39, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 1.3rem 1.3rem 1.3rem 0.2rem;
        padding: 0.9rem 1.4rem;
        margin-right: auto;
        max-width: 78%;
        margin-bottom: 0.9rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(12px);
        transition: transform 0.2s ease;
    }
    .msg-bubble-other:hover {
        transform: translateY(-2px) scale(1.01);
        border-color: rgba(192, 132, 252, 0.4);
    }

    .msg-sender {
        font-weight: 800;
        font-size: 0.85rem;
        color: #38bdf8;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 4px;
    }
    .msg-timestamp {
        font-size: 0.72rem;
        color: #64748b;
        font-weight: 600;
        margin-left: auto;
    }
    .msg-content {
        font-size: 1rem;
        color: #f8fafc;
        line-height: 1.45;
        word-break: break-word;
    }

    /* Custom Chat Input Bar */
    [data-testid="stChatInput"] {
        border-radius: 1.25rem !important;
        border: 1px solid rgba(139, 92, 246, 0.4) !important;
        background: rgba(17, 24, 39, 0.9) !important;
        box-shadow: 0 4px 30px rgba(139, 92, 246, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stChatInput"]:focus-within {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.45) !important;
    }

    /* Channel Radio Items */
    div[role="radiogroup"] > label {
        background: rgba(17, 24, 39, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 0.85rem !important;
        padding: 0.6rem 1rem !important;
        margin-bottom: 0.5rem !important;
        transition: all 0.2s ease !important;
    }
    div[role="radiogroup"] > label:hover {
        border-color: rgba(139, 92, 246, 0.5) !important;
        transform: translateX(4px) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- GLOBAL IN-MEMORY SHARED MULTI-USER CHAT STORE ---
@st.cache_resource
def get_chat_store():
    return {
        "channels": {
            "⚡ #general": [
                {
                    "id": 1,
                    "user": "PulseBot",
                    "avatar": "🤖",
                    "text": "Welcome to PulseChat! Open this link on your phone or in another tab to chat in real time. 🚀",
                    "time": "12:00 PM"
                }
            ],
            "💻 #dev-talk": [
                {
                    "id": 2,
                    "user": "PulseBot",
                    "avatar": "🤖",
                    "text": "Discuss code, tech, bug fixes, and system design here! 💻",
                    "time": "12:00 PM"
                }
            ],
            "🔥 #random": [
                {
                    "id": 3,
                    "user": "PulseBot",
                    "avatar": "🤖",
                    "text": "Share ideas, memes, and casual thoughts! 🎉",
                    "time": "12:00 PM"
                }
            ]
        },
        "next_id": 4,
        "reactions": {}  # message_id -> {"❤️": count, "🔥": count}
    }

store = get_chat_store()

# --- SIDEBAR BRANDING & CONFIG ---
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.2rem 0 0.8rem 0;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 68px; height: 68px; border-radius: 1.4rem; background: linear-gradient(135deg, #9333ea, #06b6d4); box-shadow: 0 0 35px rgba(147, 51, 234, 0.55);">
            <span style="font-size: 2.2rem;">💬</span>
        </div>
        <h2 style="margin: 0.8rem 0 0.2rem 0; font-weight: 900; background: linear-gradient(135deg, #c084fc, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">PulseChat</h2>
        <span class="live-badge"><span class="radar-dot"></span> REAL-TIME SYNC</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👤 Your Persona")
    # Store user identity across reruns
    if "my_username" not in st.session_state:
        st.session_state.my_username = f"User_{str(abs(hash(os.urandom(4))))[:4]}"
    
    my_username = st.text_input("Username", value=st.session_state.my_username)
    st.session_state.my_username = my_username

    avatar_options = ["🚀", "⚡", "🦊", "🤖", "🐱", "🎮", "🌟", "👾", "🔥", "💎"]
    my_avatar = st.selectbox("Avatar Icon", avatar_options, index=0)

    st.markdown("---")
    st.markdown("### 💬 Live Channels")
    channels = list(store["channels"].keys())
    active_channel = st.radio("Select Channel", channels, index=0)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🧹 Clear Room", use_container_width=True):
            store["channels"][active_channel] = []
            st.rerun()
    with c2:
        if st.button("🔄 Sync Now", use_container_width=True):
            st.rerun()

# --- MAIN CHAT HEADER ---
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown(f'<h1 class="chat-header-title">{active_channel}</h1>', unsafe_allow_html=True)
    st.caption("⚡ Live bi-directional message synchronization across all connected clients.")

with header_col2:
    msg_count = len(store["channels"][active_channel])
    st.markdown(f"""
    <div style="text-align: right; padding-top: 1.2rem;">
        <span style="background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.35); padding: 0.4rem 1rem; border-radius: 9999px; font-weight: 800; font-size: 0.85rem; color: #c084fc;">
            💬 {msg_count} Messages
        </span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 0.5rem 0 1.5rem 0;'>", unsafe_allow_html=True)

# --- QUICK EMOJI BAR ---
st.markdown("""
<div style="display: flex; gap: 8px; margin-bottom: 1rem; align-items: center;">
    <span style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; text-transform: uppercase;">Quick Spark:</span>
</div>
""", unsafe_allow_html=True)

q1, q2, q3, q4, q5, q6 = st.columns(6)
quick_emojis = ["🚀 Rocket Launch!", "🔥 Fire!", "❤️ Loving this!", "👏 Great job!", "💡 Brilliant idea!", "🎉 Celebrate!"]

for col, text_emoji in zip([q1, q2, q3, q4, q5, q6], quick_emojis):
    with col:
        if st.button(text_emoji, key=f"quick_{text_emoji}", use_container_width=True):
            now_str = datetime.now().strftime("%I:%M %p")
            msg_obj = {
                "id": store["next_id"],
                "user": my_username,
                "avatar": my_avatar,
                "text": text_emoji,
                "time": now_str
            }
            store["channels"][active_channel].append(msg_obj)
            store["next_id"] += 1
            if "🎉" in text_emoji or "🚀" in text_emoji:
                st.balloons()
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# --- CHAT MESSAGES DISPLAY ---
messages = store["channels"][active_channel]

chat_wrapper = st.container()
with chat_wrapper:
    if not messages:
        st.markdown("""
        <div style="text-align: center; padding: 4rem 1rem; color: #64748b;">
            <span style="font-size: 3rem;">💬</span>
            <h3 style="color: #94a3b8; font-weight: 700; margin-top: 0.5rem;">No messages in this channel yet</h3>
            <p>Type a message below or click a quick spark to kick off the conversation!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in messages:
            is_me = (msg["user"] == my_username)
            bubble_class = "msg-bubble-self" if is_me else "msg-bubble-other"
            sender_label = "You" if is_me else msg["user"]
            sender_color = "#38bdf8" if is_me else "#c084fc"

            st.markdown(f"""
            <div class="{bubble_class}">
                <div class="msg-sender">
                    <span>{msg['avatar']}</span>
                    <span style="color: {sender_color};">{sender_label}</span>
                    <span class="msg-timestamp">{msg['time']}</span>
                </div>
                <div class="msg-content">{msg['text']}</div>
            </div>
            """, unsafe_allow_html=True)

# --- CHAT INPUT BAR ---
st.markdown("<br>", unsafe_allow_html=True)
user_prompt = st.chat_input(f"Type a message in {active_channel}...")

if user_prompt:
    now_str = datetime.now().strftime("%I:%M %p")
    new_message = {
        "id": store["next_id"],
        "user": my_username,
        "avatar": my_avatar,
        "text": user_prompt.strip(),
        "time": now_str
    }
    store["channels"][active_channel].append(new_message)
    store["next_id"] += 1

    # Fun Easter Egg animations
    if any(celebrate_word in user_prompt.lower() for celebrate_word in ["congrats", "celebrate", "party", "launch", "rocket", "win"]):
        st.balloons()
    elif any(snow_word in user_prompt.lower() for snow_word in ["cold", "winter", "snow", "ice", "cool"]):
        st.snow()

    st.rerun()
