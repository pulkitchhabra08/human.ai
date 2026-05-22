import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(
    page_title="The De-AI-ifier", 
    page_icon="🧍", 
    layout="centered"
)

# 2. Injecting the Sleek Glow UI inspired by image_41c106.jpg
st.markdown("""
    <style>
    /* Premium dark gradient background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #101a30 0%, #070a13 70%) !important;
        color: #f0f3f9 !important;
    }
    
    /* Sleek top pill banner */
    .top-pill {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 6px 16px;
        border-radius: 30px;
        display: inline-block;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 12px;
        color: #38bdf8;
        margin-bottom: 30px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    /* Clean, sleek modern titles */
    h1 {
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 700;
        letter-spacing: -1px;
        font-size: 3rem !important;
        text-align: center;
        margin-bottom: 5px !important;
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 1.25rem;
        text-align: center;
        margin-bottom: 40px;
        font-family: -apple-system, sans-serif;
    }
    
    /* Glassmorphism Instruction Card */
    .premium-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 35px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .card-title {
        color: #38bdf8;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }
    
    /* Clean modern inputs */
    .stTextArea textarea {
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 15px !important;
        backdrop-filter: blur(8px);
        font-size: 15px;
    }
    
    .stTextArea textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2) !important;
    }
    
    /* Neon glowing action button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #38bdf8 0%, #2563eb 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 30px !important;
        border-radius: 30px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
        margin-top: 10px;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(56, 189, 248, 0.6) !important;
    }
    
    /* Minimalist luxury footer */
    .premium-footer {
        margin-top: 80px;
        font-size: 12px;
        color: #64748b;
        text-align: center;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        padding-top: 25px;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Layout Render
st.markdown("<div style='text-align: center;'><span class='top-pill'>✨ VERSION 1.0 // SHATTER THE ROBOT LAYER</span></div>", unsafe_allow_html=True)

st.title("The De-AI-ifier")
st.markdown("<div class='subtitle'>Smarter. Faster. Actually sounds like a real person.</div>", unsafe_allow_html=True)

# Unhinged Premium Copy
st.markdown("""
<div class="premium-card">
    <div class="card-title">// THE PROTOCOL</div>
    <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 0;">
        Look, we all know AI text sounds like a mid-level manager trying to hit a word count. It's sterile, it's boring, and it uses words like "testament" and "delve" way too much. Paste your robotic garbage below, hit the button, and we will inject actual human texture—slang, chaos, trailing thoughts, and real energy.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. User Input Field
user_input = st.text_area("ENTER THE ROBOT COMPOSITION:", placeholder="Paste the text you want to cleanse of corporate rot...", height=150)

# System Prompt
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

# 5. Run it
if st.button("Shatter the Corporate Shell ⚡"):
    if user_input:
        with st.spinner("Purging corporate buzzwords..."):
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
                
                st.markdown("<br><div style='color: #38bdf8; font-weight: 600; font-size: 14px; letter-spacing: 1px;'>// HUMAN ENGINE OUTPUT:</div>", unsafe_allow_html=True)
                st.write(output_text)
            except Exception as e:
                st.error(f"Ah snap, something went wrong: {e}")
    else:
        st.warning("You gotta paste some corporate text first, chief.")

# 6. Unhinged Luxury Footer Signature
st.markdown("""
<div class="premium-footer">
    MADE BY A HUMAN FED UP WITH BORING AI RESPONSES — <span style="color: #ffffff; font-weight: 600;">PULKIT CHHABRA</span>
</div>
""", unsafe_allow_html=True)
