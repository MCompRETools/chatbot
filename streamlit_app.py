import streamlit as st
import time
import csv
from datetime import datetime

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Sustainable Digitalization – Teaching Simulation",
    layout="centered"
)

# -------------------------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.last_feedback = ""
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

def update_profile(impact):
    for k, v in impact.items():
        st.session_state.profile[k] += v

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
    st.title("🌱 Sustainable Digital Transformation – Teaching Simulation")

    st.write("""
You are the **Digital Strategy Lead** at *GreenRetail Ltd.*  
Your task is to guide the organization through digital transformation while
balancing:

- Environmental sustainability  
- Economic performance  
- Social responsibility  
- Governance and regulatory compliance
""")

    if st.button("Start Scenario"):
        log_event("Intro", "Scenario started")
        st.session_state.step = 1.0
        st.experimental_rerun()

# -------------------------------------------------
# DECISION + FEEDBACK TEMPLATES
# -------------------------------------------------
def decision_page(level, title, question, options):
    progress(level)
    st.subheader(title)
    return st.radio(question, options)

def feedback_page(level):
    progress(level)
    st.info(st.session_state.last_feedback)
    if st.button("Continue"):
        log_event(f"Feedback {level}", "Viewed feedback")
        st.session_state.step = level + 1
        st.experimental_rerun()

# -------------------------------------------------
# DECISION 1
# -------------------------------------------------
if st.session_state.step == 1.0:
    choice = decision_page(
        1,
        "Decision 1: Cloud Infrastructure",
        "Which cloud strategy should be adopted?",
        [
            "Low-cost fossil-based provider",
            "Renewable-powered provider",
            "Hybrid cloud model"
        ]
    )

    if st.button("Confirm Decision"):
        if choice == "Low-cost fossil-based provider":
            update_profile({"environmental": -2, "economic": 2})
            st.session_state.last_feedback = (
                "Costs decrease, but carbon emissions and regulatory risks increase."
            )
        elif choice == "Renewable-powered provider":
            update_profile({"environmental": 2, "economic": -1})
            st.session_state.last_feedback = (
                "Environmental alignment improves, though operational costs rise."
            )
        else:
            update_profile({"environmental": 1})
            st.session_state.last_feedback = (
                "Balanced approach with added governance complexity."
            )

        log_event("Decision 1", choice)
        st.session_state.step = 1.1
        st.experimental_rerun()

elif st.session_state.step == 1.1:
    feedback_page(1)

# -------------------------------------------------
# DECISION 2
# -------------------------------------------------
elif st.session_state.step == 2.0:
    choice = decision_page(
        2,
        "Decision 2: Data Management",
        "How should customer data be handled?",
        [
            "Collect all available data",
            "Apply data minimization",
            "Outsource analytics"
        ]
    )

    if st.button("Confirm Decision"):
        if choice == "Collect all available data":
            update_profile({"environmental": -1, "social": -2, "governance": -1})
            st.session_state.last_feedback = (
                "Analytics improve, but privacy and energy risks increase."
            )
        elif choice == "Apply data minimization":
            update_profile({"environmental": 1, "social": 2, "governance": 1})
            st.session_state.last_feedback = (
                "Trust and sustainability improve, with limited analytics scope."
            )
        else:
            update_profile({"economic": 1, "governance": -1})
            st.session_state.last_feedback = (
                "Efficiency improves, but transparency declines."
            )

        log_event("Decision 2", choice)
        st.session_state.step = 2.1
        st.experimental_rerun()

elif st.session_state.step == 2.1:
    feedback_page(2)

# -------------------------------------------------
# DECISION 3
# -------------------------------------------------
elif st.session_state.step == 3.0:
    choice = decision_page(
        3,
        "Decision 3: AI Deployment",
        "How should AI be used?",
        [
            "Extensive AI deployment",
            "Selective AI deployment",
            "Avoid AI"
        ]
    )

    if st.button("Confirm Decision"):
        if choice == "Extensive AI deployment":
            update_profile({"economic": 2, "environmental": -1, "social": -1})
            st.session_state.last_feedback = (
                "Efficiency rises, but ethical and environmental risks increase."
            )
        elif choice == "Selective AI deployment":
            update_profile({"economic": 1, "social": 1})
            st.session_state.last_feedback = (
                "Balanced innovation with controlled sustainability impact."
            )
        else:
            update_profile({"environmental": 1, "economic": -1})
            st.session_state.last_feedback = (
                "Risks decrease, but competitiveness may decline."
            )

        log_event("Decision 3", choice)
        st.session_state.step = 3.1
        st.experimental_rerun()

elif st.session_state.step == 3.1:
    progress(3)
    st.info(st.session_state.last_feedback)
    if st.button("Continue"):
        log_event("Feedback 3", "Viewed feedback")
        st.session_state.step = 3.2
        st.experimental_rerun()

# -------------------------------------------------
# 🚨 REGULATORY SHOCK (FIXED STATE)
# -------------------------------------------------
elif st.session_state.step == 3.2:
    st.warning("""
🚨 **Regulatory Update**

New sustainability regulations now require:
- Transparent carbon reporting
- Stronger data governance
- Evidence of employee digital upskilling

All remaining decisions must comply with these requirements.
""")

    log_event("Shock Event", "New regulation introduced")

    if st.button("Acknowledge and Continue"):
        st.session_state.step = 4.0
        st.experimental_rerun()

# -------------------------------------------------
# DECISION 4
# -------------------------------------------------
elif st.session_state.step == 4.0:
    choice = decision_page(
        4,
        "Decision 4: Employee Upskilling",
        "How should employees be supported?",
        [
            "Minimal training",
            "Targeted training",
            "Extensive reskilling"
        ]
    )

    if st.button("Confirm Decision"):
        if choice == "Minimal training":
            update_profile({"social": -2})
            st.session_state.last_feedback = (
                "Short-term savings achieved, but compliance risk increases."
            )
        elif choice == "Targeted training":
            update_profile({"social": 1})
            st.session_state.last_feedback = (
                "Skills improve while managing costs."
            )
        else:
            update_profile({"social": 2, "economic": -1})
            st.session_state.last_feedback = (
                "Long-term resilience and compliance improve."
            )

        log_event("Decision 4", choice)
        st.session_state.step = 4.1
        st.experimental_rerun()

elif st.session_state.step == 4.1:
    feedback_page(4)

# -------------------------------------------------
# DECISION 5
# -------------------------------------------------
elif st.session_state.step == 5.0:
    choice = decision_page(
        5,
        "Decision 5: Sustainability Governance",
        "How should sustainability be governed?",
        [
            "Annual reporting",
            "Real-time sustainability dashboards",
            "Financial KPIs only"
        ]
    )

    if st.button("Confirm Decision"):
        if choice == "Annual reporting":
            update_profile({"governance": 0})
            st.session_state.last_feedback = (
                "Transparency exists, but responsiveness is limited."
            )
        elif choice == "Real-time sustainability dashboards":
            update_profile({"governance": 2})
            st.session_state.last_feedback = (
                "Continuous accountability and regulatory alignment improve."
            )
        else:
            update_profile({"economic": 1, "governance": -2})
            st.session_state.last_feedback = (
                "Financial focus increases, but compliance risk rises."
            )

        log_event("Decision 5", choice)
        st.session_state.step = 5.1
        st.experimental_rerun()

elif st.session_state.step == 5.1:
    feedback_page(5)

# -------------------------------------------------
# FINAL OUTCOME + REFLECTION EXPORT
# -------------------------------------------------
else:
    st.title("📊 Final Sustainability Profile")

    for dim, score in st.session_state.profile.items():
        st.write(f"**{dim.capitalize()}**: {qualitative_label(score)}")

    st.divider()
    st.subheader("Reflection (Manual Grading)")

    reflection = st.text_area(
        "Reflect on your decisions, trade-offs, and response to regulation:",
        height=220
    )

    st.markdown("""
**Assessment rubric (for instructor):**
- Sustainability reasoning (40%)
- Trade-off awareness (30%)
- Regulatory response (30%)
""")

    if st.button("Submit Reflection"):
        save_analytics()

        with open("reflections.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["timestamp", "reflection_text"])
            writer.writerow([datetime.now().isoformat(), reflection])

        st.success("Simulation completed. Reflection and analytics saved.")
