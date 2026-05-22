import streamlit as st
from groq import Groq

# 1. Custom Page Config & Injecting CSS Vibes
st.set_page_config(
    page_title="The De-AI-ifier", 
    page_icon="😎", 
    layout="centered"
)

# Dark theme overrides and cool fonts (Fixed with unsafe_allow_html=True)
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
    }
    h1 {
        color: #ff4b4b !important;
        font-family: 'Courier New', Courier, monospace;
        font-weight: 800;
    }
    h3 {
        color: #8b949e !important;
        font-family: 'Courier New', Courier, monospace;
    }
    .stTextArea textarea {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px;
    }
    .instruction-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #ff4b4b;
        margin-bottom: 25px;
    }
    .signature {
        margin-top: 50px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 13px;
        color: #8b949e;
        text-align: center;
        border-top: 1px solid #21262d;
        padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. App Header
st.title("🤖 to 😎")
st.title("the de-AI-fier :)")
st.subheader("shattering boring robot text in real time.")

# 3. Cool Instructions Block (Fixed with unsafe_allow_html=True)
st.markdown("""
<div class="instruction-box">
    <span style="color: #ff4b4b; font-weight: bold; font-family: monospace;">// HOW TO USE THIS THING:</span><br>
    <ol style="color: #8b949e; margin-top: 8px; font-family: monospace; font-size: 14px;">
        <li>Go copy whatever sterile, over-polished text some AI just spit out at you.</li>
        <li>Paste that corporate nonsense into the box below.</li>
        <li>Hit the burn button and watch it turn into real, expressive human text.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# 4. User Input
user_input = st.text_area("PASTE YOUR BORING ROBOT TEXT HERE:", placeholder="Artificial intelligence is transforming workflows...", height=150)

# The System Prompt
SYSTEM_PROMPT = """
You are an advanced text 'De-AI-ifier' and linguistic translator. Your sole purpose is to strip out the polished, sterile, corporate structure of AI-generated text and rewrite it with the raw, chaotic, and expressive texture of a real human typing online or texting a friend.

STRICT LINGUISTIC RULES:
1. NO CORPORATE AI TONE: Never start with "Here is...", "Sure, I can help with that", or use balanced paragraphs. Eliminate transition words like "Furthermore", "In conclusion", "Moreover", or "Therefore".
2. SENTENCE CADENCE: Use highly irregular sentence lengths. Mix long, rambling, unfiltered thoughts with sudden, brief, one-or-two-word sentences (e.g., "Yeah.", "Genuinely.").
3. PUNCTUATION & CASUALNESS: Use lowercase heavily or exclusively for casual topics. Use trailing ellipses "..." to signify natural thought pauses. Skip periods at the very end of lines or short thoughts.
4. TEXT SLANG & ABBREVIATIONS: Judiciously replace standard words with common internet shortcuts (u, r, literal/litrally, fr, idk, ngl, bc). Use phonetic lengthening for emphasis (e.g., "sooo", "crazzyy").
5. EXPRESSIVE FILLERS: Inject natural internet speech patterns, filler words, and conversational hooks (e.g., "wait because...", "so like...", "literally think about it", "tbh").
6. THE "TRY-HARD" FILTER: Do not overuse outdated slang. Sound like an authentic, slightly chaotic human typing fast, not a brand trying to be hip. Maintain core meaning, but shatter the formal shell.
"""

# 5. Execution Button
if st.button("HUMANIZE IT ✨", type="primary"):
    if user_input:
        with st.spinner("Shattering the shell..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant", 
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_input}
                    ]
                )
                
                output_text = completion.choices[0].message.content
                
                # Fixed with unsafe_allow_html=True
                st.markdown("<br><b style='color: #ff4b4b; font-family: monospace;'>BOOM. REAL HUMAN TEXT:</b>", unsafe_allow_html=True)
                st.write(output_text)
            except Exception as e:
                st.error(f"Ah snap, something went wrong: {e}")
    else:
        st.warning("Put some text in the box first, dude!")

# 6. Your Custom Signature (Fixed with unsafe_allow_html=True)
st.markdown("""
<div class="signature">
    made by a person fed up with boring ai responses, <span style="color: #ff4b4b;">pulkit chhabra</span>
</div>
""", unsafe_allow_html=True)
