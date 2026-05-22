import streamlit as st
import os
# You would use a free library like 'google-generativeai' or 'groq'
import groq  

st.title("🤖 ➡️ 🧍 The De-AI-ifier")
st.subheader("Strip the corporate robot out of your text instantly.")

# User Input
user_input = st.text_area("Paste your sterile AI text here:", placeholder="Artificial intelligence is transforming...")

# Our secret sauce system prompt from earlier
SYSTEM_PROMPT = """
You are an advanced text 'De-AI-ifier'. Strip out polished, corporate structure. 
Use highly irregular sentence lengths, lowercase, trailing ellipses '...', 
and natural internet shortcuts (u, fr, ngl, bc). Sound like a real human texting.
"""

if st.button("Humanize It ✨"):
    if user_input:
        with st.spinner("Shattering the corporate shell..."):
            # Initialize free API client (using an environment variable for safety)
            client = groq.Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # Call the model
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant", # Free, ultra-fast model
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ]
            )
            
            output_text = completion.choices[0].message.content
            
            # Display the result
            st.success("Boom. Real human text:")
            st.write(output_text)
    else:
        st.warning("Put some text in the box first, dude!")
