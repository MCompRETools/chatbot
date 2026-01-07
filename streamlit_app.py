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
            impact = {"environmental": -2, "economic": 2}
            feedback = (
                "This choice improves short-term cost efficiency but significantly "
                "increases carbon emissions and exposes the company to reputational "
                "and regulatory risks."
            )
        elif choice.startswith("Renewable"):
            impact = {"environmental": 2, "economic": -1}
            feedback = (
                "This option strongly supports environmental sustainability and "
                "aligns with GreenRetail’s public commitments, though it increases "
                "operational costs."
            )
        else:
            impact = {"environmental": 1}
            feedback = (
                "The hybrid approach balances flexibility and emissions reduction, "
                "but increases governance and operational complexity."
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

# -------------------------------------------------
# DECISION 2
# -------------------------------------------------
elif st.session_state.step == 2.0:
    progress(2)
    st.subheader("Decision 2: Customer Data Management")

    st.markdown("""
### Scenario Context
GreenRetail plans to use customer data to personalize services and improve
demand forecasting. However, increased data collection raises concerns
around privacy, energy use, and customer trust.
""")

    choice = st.radio(
        "How should customer data be managed?",
        [
            "Collect all available data",
            "Apply data minimization principles",
            "Outsource analytics to third parties"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Collect"):
            impact = {"social": -2, "environmental": -1, "governance": -1}
            feedback = (
                "While analytics capabilities increase, this approach undermines "
                "privacy, increases storage energy consumption, and may reduce "
                "customer trust."
            )
        elif choice.startswith("Apply"):
            impact = {"social": 2, "environmental": 1, "governance": 1}
            feedback = (
                "Data minimization strengthens trust, reduces energy use, and "
                "aligns well with ethical and regulatory expectations."
            )
        else:
            impact = {"economic": 1, "governance": -1}
            feedback = (
                "Outsourcing simplifies operations but reduces transparency and "
                "control over sustainability practices."
            )

        apply_impact(impact)
        st.session_state.last_feedback = feedback
        log_event("Decision 2", choice)
        st.session_state.step = 2.1
        st.experimental_rerun()

elif st.session_state.step == 2.1:
    st.info(st.session_state.last_feedback)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            rollback_impact()
            st.session_state.step = 2.0
            st.experimental_rerun()
    with col2:
        if st.button("Continue"):
            log_event("Feedback 2", "Viewed")
            st.session_state.step = 3.0
            st.experimental_rerun()

# -------------------------------------------------
# DECISION 3
# -------------------------------------------------
elif st.session_state.step == 3.0:
    progress(3)
    st.subheader("Decision 3: AI and Automation")

    st.markdown("""
### Scenario Context
AI can significantly improve efficiency in logistics, pricing, and customer
support. However, concerns exist regarding energy consumption, workforce
impact, and algorithmic transparency.
""")

    choice = st.radio(
        "How should AI be used?",
        [
            "Extensive AI deployment",
            "Selective AI deployment",
            "Avoid AI"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Extensive"):
            impact = {"economic": 2, "environmental": -1, "social": -1}
            feedback = (
                "Efficiency improves significantly, but energy use rises and "
                "employee concerns about automation increase."
            )
        elif choice.startswith("Selective"):
            impact = {"economic": 1, "social": 1}
            feedback = (
                "This balanced approach enables innovation while maintaining "
                "ethical oversight and manageable energy consumption."
            )
        else:
            impact = {"environmental": 1, "economic": -1}
            feedback = (
                "Avoiding AI reduces risks but may limit competitiveness "
                "and innovation potential."
            )

        apply_impact(impact)
        st.session_state.last_feedback = feedback
        log_event("Decision 3", choice)
        st.session_state.step = 3.1
        st.experimental_rerun()

elif st.session_state.step == 3.1:
    st.info(st.session_state.last_feedback)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            rollback_impact()
            st.session_state.step = 3.0
            st.experimental_rerun()
    with col2:
        if st.button("Continue"):
            log_event("Feedback 3", "Viewed")
            st.session_state.step = 3.2
            st.experimental_rerun()

# -------------------------------------------------
# REGULATORY SHOCK
# -------------------------------------------------
elif st.session_state.step == 3.2:
    st.warning("""
🚨 **Regulatory Update**

New regulations require:
- Carbon reporting for digital systems
- Stronger data governance
- Evidence of employee digital training
""")

    log_event("Shock Event", "Regulatory update")

    if st.button("Acknowledge and Continue"):
        st.session_state.step = 4.0
        st.experimental_rerun()

# -------------------------------------------------
# DECISION 4 – ORGANIZATIONAL CULTURE
# -------------------------------------------------
elif st.session_state.step == 4.0:
    progress(4)
    st.subheader("Decision 4: Organizational Culture")

    st.markdown("""
### Scenario Context
Digital transformation is causing anxiety among employees.
Some fear job displacement, while others lack confidence in using new systems.
Leadership must decide how organizational culture should evolve.
""")

    choice = st.radio(
        "What cultural change should be implemented?",
        [
            "Maintain existing performance-driven culture",
            "Promote inclusive learning and participation",
            "Introduce strict digital performance monitoring"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Maintain"):
            impact = {"social": -1}
            feedback = (
                "Maintaining the status quo avoids disruption but fails to address "
                "employee concerns, risking disengagement and resistance."
            )
        elif choice.startswith("Promote"):
            impact = {"social": 2}
            feedback = (
                "Inclusive learning and participation strengthen trust, well-being, "
                "and long-term social sustainability."
            )
        else:
            impact = {"social": -2}
            feedback = (
                "Strict monitoring may improve short-term output but damages trust "
                "and organizational culture."
            )

        apply_impact(impact)
        st.session_state.last_feedback = feedback
        log_event("Decision 4", choice)
        st.session_state.step = 4.1
        st.experimental_rerun()

elif st.session_state.step == 4.1:
    st.info(st.session_state.last_feedback)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            rollback_impact()
            st.session_state.step = 4.0
            st.experimental_rerun()
    with col2:
        if st.button("Continue"):
            log_event("Feedback 4", "Viewed")
            st.session_state.step = 5.0
            st.experimental_rerun()

# -------------------------------------------------
# DECISION 5 – GOVERNANCE
# -------------------------------------------------
elif st.session_state.step == 5.0:
    progress(5)
    st.subheader("Decision 5: Sustainability Governance")

    st.markdown("""
### Scenario Context
GreenRetail must demonstrate accountability for sustainability outcomes.
Stakeholders demand transparency, while leadership seeks actionable insights.
""")

    choice = st.radio(
        "How should sustainability performance be governed?",
        [
            "Annual sustainability reporting",
            "Real-time sustainability dashboards",
            "Focus mainly on financial KPIs"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Annual"):
            impact = {"governance": 0}
            feedback = (
                "Annual reporting offers transparency but limits timely corrective action."
            )
        elif choice.startswith("Real-time"):
            impact = {"governance": 2}
            feedback = (
                "Real-time dashboards improve accountability and regulatory compliance."
            )
        else:
            impact = {"economic": 1, "governance": -2}
            feedback = (
                "Financial focus increases risk of sustainability blind spots."
            )

        apply_impact(impact)
        st.session_state.last_feedback = feedback
        log_event("Decision 5", choice)
        st.session_state.step = 5.1
        st.experimental_rerun()

elif st.session_state.step == 5.1:
    st.info(st.session_state.last_feedback)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            rollback_impact()
            st.session_state.step = 5.0
            st.experimental_rerun()
    with col2:
        if st.button("View Final Outcome"):
            st.session_state.step = 6
            st.experimental_rerun()

# -------------------------------------------------
# FINAL OUTCOME + REFLECTION
# -------------------------------------------------
else:
    st.title("📊 Final Sustainability Profile")

    for dim, score in st.session_state.profile.items():
        st.write(f"**{dim.capitalize()} sustainability:** {qualitative_label(score)}")

    st.divider()
    st.subheader("Reflection")

    reflection = st.text_area(
        "Reflect on your decisions and sustainability trade-offs:",
        height=220
    )

    if st.button("Submit Reflection"):
        save_analytics()
        with open("reflections.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["timestamp", "reflection_text"])
            writer.writerow([datetime.now().isoformat(), reflection])

        st.success("Simulation completed. Thank you for participating.")
