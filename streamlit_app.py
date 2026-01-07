import streamlit as st
import time
import csv
from datetime import datetime

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Sustainable Digitalization – GreenRetail Simulation",
    layout="centered"
)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.last_feedback = ""
    st.session_state.last_impact = {}
    st.session_state.start_time = time.time()
    st.session_state.analytics = []
    st.session_state.profile = {
        "environmental": 0,
        "economic": 0,
        "social": 0,
        "governance": 0
    }

# -------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------
def log_event(stage, label):
    elapsed = round(time.time() - st.session_state.start_time, 2)
    st.session_state.analytics.append({
        "timestamp": datetime.now().isoformat(),
        "stage": stage,
        "event": label,
        "elapsed_seconds": elapsed
    })
    st.session_state.start_time = time.time()

def apply_impact(impact):
    st.session_state.last_impact = impact
    for k, v in impact.items():
        st.session_state.profile[k] += v

def rollback_impact():
    for k, v in st.session_state.last_impact.items():
        st.session_state.profile[k] -= v
    st.session_state.last_impact = {}

def qualitative_label(score):
    if score >= 2:
        return "Strong alignment"
    elif score >= 0:
        return "Moderate alignment"
    else:
        return "Weak alignment"

def save_analytics():
    with open("learning_analytics.csv", "a", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["timestamp", "stage", "event", "elapsed_seconds"]
        )
        if f.tell() == 0:
            writer.writeheader()
        writer.writerows(st.session_state.analytics)

def progress(level):
    st.progress(level / 5)
    st.caption(f"Progress: Level {level} of 5")

# -------------------------------------------------
# INTRO PAGE
# -------------------------------------------------
if st.session_state.step == 0:
    st.title("🌱 GreenRetail Ltd. – Sustainable Digital Transformation")

    st.markdown("""
### Company Overview
**GreenRetail Ltd.** is a mid-sized omnichannel (across all channels, including online, mobile, and in-store)
retail organization operating across physical stores and a rapidly growing digital platform. The company sells consumer
goods sourced from regional suppliers, emphasizing ethical sourcing and customer trust.

### What GreenRetail Delivers
- Affordable and accessible retail products  
- Seamless digital shopping experiences  
- Transparent supply-chain information  
- Personalized customer engagement through digital platforms  

### Sustainability Policies
GreenRetail has committed to:
- Reducing digital and operational carbon footprint  
- Responsible data usage and customer privacy  
- Fair labor practices across digital and physical operations  
- Compliance with emerging sustainability regulations  

### Organizational Culture
The company promotes:
- Collaboration between IT, business, and sustainability teams  
- Employee well-being and continuous learning  
- Ethical decision-making over short-term gains  
- Openness to change, but with internal resistance to rapid digital disruption  

### Your Role
You are the **Digital Strategy Lead**, responsible for guiding GreenRetail’s digital
transformation while balancing **business performance** and **sustainability goals**.

You will face a series of decisions. Each decision has trade-offs.
There are **no perfect answers**.
""")

    if st.button("Begin Scenario"):
        log_event("Intro", "Scenario started")
        st.session_state.step = 1.0
        st.experimental_rerun()

# -------------------------------------------------
# DECISION 1
# -------------------------------------------------
elif st.session_state.step == 1.0:
    progress(1)
    st.subheader("Decision 1: Digital Infrastructure")

    st.markdown("""
Scenario Context
GreenRetail’s existing IT infrastructure is aging and energy-inefficient.
Customer demand forecasting and inventory optimization require scalable
digital infrastructure. However, leadership is concerned about rising energy
consumption and public sustainability commitments.
""")

    choice = st.radio(
        "Which infrastructure strategy should be adopted?",
        [
            "Low-cost fossil-fuel-based cloud",
            "Renewable-powered cloud provider",
            "Hybrid cloud model"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Low-cost"):
            update_profile({"environmental": -2, "economic": 2})
            st.session_state.last_feedback = (
                "This choice improves short-term cost efficiency but significantly "
                "increases carbon emissions and exposes the company to reputational "
                "and regulatory risks."
            )
        elif choice.startswith("Renewable"):
            update_profile({"environmental": 2, "economic": -1})
            st.session_state.last_feedback = (
                "This option strongly supports environmental sustainability and "
                "aligns with GreenRetail’s public commitments, though it increases "
                "operational costs."
            )
        else:
            update_profile({"environmental": 1})
            st.session_state.last_feedback = (
                "The hybrid approach balances flexibility and emissions reduction, "
                "but increases governance and operational complexity."
            )

        apply_impact(impact)
        st.session_state.last_feedback = feedback
        log_event("Decision 1", choice)
        st.session_state.step = 1.1
        st.experimental_rerun()
