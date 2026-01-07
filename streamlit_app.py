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
retail organization operating across physical stores and a rapidly growing digital platform.
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
                "increases carbon emissions."
            )
        elif choice.startswith("Renewable"):
            update_profile({"environmental": 2, "economic": -1})
            st.session_state.last_feedback = (
                "This option strongly supports environmental sustainability."
            )
        else:
            update_profile({"environmental": 1})
            st.session_state.last_feedback = (
                "The hybrid approach balances flexibility and emissions reduction."
            )

        apply_impact(impact)
        st.session_state.last_feedback = feedback
        log_event("Decision 1", choice)
        st.session_state.step = 1.1
        st.experimental_rerun()

elif st.session_state.step == 1.1:
    st.info(st.session_state.last_feedback)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            rollback_impact()
            st.session_state.step = 1.0
            st.experimental_rerun()
    with col2:
        if st.button("Continue"):
            log_event("Feedback 1", "Viewed")
            st.session_state.step = 2.0
            st.experimental_rerun()
