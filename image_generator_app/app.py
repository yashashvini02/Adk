import streamlit as st
import google.generativeai as genai

# 👉 Configure your Gemini API key (get it from https://makersuite.google.com/app)
genai.configure(api_key="AIzaSyCFEtNTLIZeQJVL-Ay4TgHgMN8Ttb26NwM")

# Initialize model
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="AI Social Media Content Agent", layout="centered")
st.title("🤖 AI Social Media Content Agent")

st.markdown("This agent understands your business and generates platform-ready content with optimized hashtags and image ideas.")

# 🔹 Step 1: Business input
business_goal = st.text_area("📝 Describe your business or campaign goal:", placeholder="E.g. We sell eco-friendly fitness wear for young adults.")

# 🔹 Step 2: Platform & Tone Selection
platforms = st.multiselect(
    "📍 Choose platforms to target:",
    ["Instagram", "LinkedIn", "Twitter", "Facebook", "YouTube Shorts", "Pinterest"],
    default=["Instagram", "Twitter"]
)

tone = st.selectbox(
    "🎙️ Select the desired tone for the posts:",
    ["Professional", "Witty", "Casual", "Inspiring", "Playful"]
)

# 🔹 Step 3: Generate Button
if st.button("🚀 Generate Social Media Posts") and business_goal:
    with st.spinner("Thinking like a marketing expert..."):
        prompt = f"""
You are a top-tier social media strategist. Given the following business description:

{business_goal}

Your task is to:
1. Select the best posting style and tone based on the chosen platforms: {', '.join(platforms)}.
2. Generate **3 tailored social media posts**.
3. Optimize each post with trending and relevant hashtags.
4. At the end, suggest creative **image ideas** for each post (no actual images yet).

Write in a clear and clean format.
"""

        try:
            response = model.generate_content(prompt)
            st.success("✅ Content Generated!")
            st.markdown("### 📢 Social Media Posts")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.info("👆 Enter details and click the button to generate posts.")

st.markdown("---")
st.caption("💡 Built with Gemini + Streamlit. DALL·E image generation support coming soon.")
