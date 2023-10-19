from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cmd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic (3).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hashir Ahmed "
PAGE_ICON = "👋"
NAME = "Hashir Ahmed"
DESCRIPTION = """
Work on Python, WebMaker, Game maker
"""
EMAIL = "hashirahmed13451@gmail.com"
SOCIAL_MEDIA = {
    "Discord": "https://discord.com",
    "Redit": "https://www.reddit.com/user/Shadow_Boi13451",
    "GitHub": "https://github.com/Hashir-Ahmed123"
}   
PROJECT = {
    "🏆 I'we made an an Discord Bot"
    "🏆 I maked an Website"
    "🏆 I made an game"
    "🏆 and im trying to make a Mobile App"
    "🏆 I am learning Artificall intellagnce"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ----LOAD CSS, PDF & PRORFIL PIC -----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# ---- HERO SECTION ----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📬", EMAIL)

# ----- SOCIAL LINKS -----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (Platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{Platform}]([{link}])")

# ----- EXPERIENCE & QULIFICATION ----
st.write("#")
st.subheader("Experiance & Qulification")
st.write(
    """
- 3 Month of experince in html and css
- Fast at my work
- Strong hand in html, css and python
- 2 Month of experince in python   
    """
)

# --- SKILLS ----
st.write("#")
st.subheader("Skill")
st.write(
    """
- 👨‍💻 Programming: Python (turtle, streamlit, kivy), html, css, c#
- 🖼️ Graphic Desgin: Adobe Photoshaop, Photopea, Adobe Illustrator
"""
)
