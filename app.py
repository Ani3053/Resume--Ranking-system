import streamlit as st
from src.preprocess import load_resumes
from src.screening import rank_resumes

st.set_page_config(page_title="Resume Ranking System", layout="centered")
st.markdown("""
<style>
/* Header */
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(0,0,0,0.6);
    padding: 10px 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}

/* Logo circle */
.logo {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: white;
    font-size: 18px;
}

/* Title text */
.header-title {
    color: white;
    font-size: 20px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    color: white;
    margin-top: 30px;
    font-size: 14px;
    opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)

# Header UI
st.markdown("""
<div class="header">
    <div class="logo">Resumez</div>
    <div class="header-title">Resume Ranking System</div>
</div>
""", unsafe_allow_html=True)

# 🌌 Background + global styling
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                url("https://images.unsplash.com/photo-1522202176988-66273c2fd55f");
    background-size: cover;
    background-position: center;
}

/* Title */
.title {
    text-align: center;
    color: white;
    font-size: 40px;
    font-weight: bold;
}

/* Glass card */
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
    backdrop-filter: blur(10px);
    transition: 0.3s;
}

/* Hover effect */
.card:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 15px #00c6ff;
}

/* Button */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

/* Text */
.white-text {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>📄 Resume Ranking System</div>", unsafe_allow_html=True)

# Input
st.markdown("<p class='white-text'>Enter Job Description</p>", unsafe_allow_html=True)
job_desc = st.text_area("", placeholder="Python, ML, NLP, Pandas...", height=120)

# Button
if st.button("🚀 Rank Resumes"):
    if job_desc.strip() == "":
        st.warning("Enter job description")
    else:
        resumes = load_resumes()
        results = rank_resumes(resumes, job_desc)
        results = sorted(results, key=lambda x: x[1], reverse=True)

        st.markdown("<h2 class='white-text'>📊 Results</h2>", unsafe_allow_html=True)

        # Results UI
        for i, (name, score) in enumerate(results, 1):
            st.markdown(f"""
            <div class="card">
                <h4 class="white-text">#{i} - {name}</h4>
                <p class="white-text">Score: <b>{score:.4f}</b></p>
            </div>
            """, unsafe_allow_html=True)

            # Progress bar
            st.progress(min(int(score * 100), 100))

        # Highlight best
        best = results[0]
        st.success(f"🏆 Best Match: {best[0]} ({best[1]:.4f})")

        st.markdown("""
<div class="footer">
    Created by <b>Aniruddh</b> & <b>Ananth</b>
</div>
""", unsafe_allow_html=True)