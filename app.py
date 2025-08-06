import streamlit as st
from crew_builder import build_truthscribe_crew
from utils.fact_memory import store_fact
import random

fun_facts = [
    "🎶 aespa is coming back this September 5th — mark your calendar!",
    "🧛‍♀️ Wednesday Season 2 is out now (sorry, I'm a fan).",
    "🎤 Katseye is the next big thing? Stay tuned.",
    "💡 Pro tip: Lower LLM temperature = more serious tone.",
    "🧠 Did you know? Chroma memory prevents hallucination.",
    "☕️ Grab a coffee... the agents are doing their best!",
    "📡 Research agents are surfing the web for the truth..."
]

loading_message = random.choice(fun_facts)

# Streamlit page config
st.set_page_config(page_title="Truthscribe: AI Blog Generator", page_icon="📰", layout="wide")

st.title("🧠 Truthscribe: AI Blog Generator, powered by CrewAI")
st.markdown("Generate accurate blog content using multi-agent AI and verified facts.")

# --- Sidebar: Topic Input ---
with st.sidebar:
    st.header("📝 Topic Settings")
    topic = st.text_area(
        "Enter your topic",
        height=100,
        placeholder="Enter the topic you want to generate content about..."
    )
    temperature = st.slider(
        "Temperature (creativity)", 0.0, 1.0, 0.15,
        help="Lower = more factual and precise. Higher = more creative and varied, but possibly less accurate."
    )
    generate = st.button("🚀 Generate Article")

    st.markdown("---")

    # --- Fact Injection Optional Prompt ---
    st.subheader("🔎 Want to boost the article’s accuracy?")
    inject_prompt = st.radio(
        "Improve the result with your own trusted input.",
        ["No, just generate it", "Yes, let me add a fact"],
        index=0
    )
    if inject_prompt == "Yes, let me add a fact":
        st.markdown("### 🧠 Add a Verified Fact into Memory")
        injected_fact = st.text_area("Enter the fact", height=100)
        injected_source = st.text_input("Source URL")
        injected_confidence = st.selectbox("Confidence Level", ["High", "Medium", "Low"])
        injected_topic = st.text_input("Topic (optional)", value=topic)
        save_fact = st.button("💾 Save Fact")

        if save_fact:
            if injected_fact and injected_source:
                store_fact(
                    fact_text=injected_fact,
                    metadata={
                        "topic": injected_topic,
                        "source": injected_source,
                        "confidence": injected_confidence
                    }
                )
                st.success("✅ Fact saved to memory!")
            else:
                st.warning("⚠️ Please provide both a fact and a source URL.")

# --- Main Content Generation ---
if generate and topic:
    with st.spinner(f"Generating article... {loading_message}"):
        try:
            result = build_truthscribe_crew(topic)
            st.subheader("📰 Final Output")
            st.markdown(result.raw)
            st.download_button(
                "💾 Download as Markdown",
                data=result.raw,
                file_name=f"{topic.replace(' ', '_').lower()}_article.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error(f"🚨 Error: {str(e)}")

st.markdown("---")
st.caption("Built with Streamlit + CrewAI + Chroma + Wikipedia + Serper")
