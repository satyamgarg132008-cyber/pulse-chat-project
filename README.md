# 💬 PulseChat - Real-Time Animated Multi-User Chat

An ultra-modern, real-time animated chat application built with Python and Streamlit.

## 🚀 Features
- **Real-Time Multi-User Sync:** Messages automatically sync across all open browser windows, tabs, and mobile devices every 2.5s using `streamlit-autorefresh` and shared in-memory state.
- **Multiple Channels:** Seamlessly switch between `#general`, `#dev-talk`, and `#random`.
- **Custom Personas:** Set custom usernames and avatar icons.
- **Rich Animations:**
  - Floating ambient neon gradient orbs.
  - Pulsing radar live connection indicator.
  - Slide-up bouncing message bubbles.
  - Quick emoji spark reaction buttons.
  - Interactive confetti and balloon celebrations!

## 💻 Local Run
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```
3. Open two browser tabs to `http://localhost:8501` and chat in real-time!

## ☁️ Deploy to Streamlit Community Cloud
1. Push this folder to a GitHub repository (e.g. `pulse-chat-app`).
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New App**.
3. Select your repo and click **Deploy**!
