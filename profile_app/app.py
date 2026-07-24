import streamlit as st

st.set_page_config(page_title="Abdullah Bin Fahad", page_icon="🧠", layout="wide")

# ---- THEME ----
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Theme‑aware CSS
light = st.session_state.theme == "light"
bg = "#ffffff" if light else "#0a0a0a"
card = "rgba(0,0,0,0.04)" if light else "rgba(255,255,255,0.05)"
txt = "#1a1a1a" if light else "#e0e0e0"
muted = "#555" if light else "#aaa"
accent = "#1a1a1a" if light else "#ffffff"
border = "rgba(0,0,0,0.08)" if light else "rgba(255,255,255,0.1)"
shadow = "0 4px 20px rgba(0,0,0,0.05)" if light else "0 4px 20px rgba(0,0,0,0.4)"
progress_bg = "linear-gradient(90deg, #333, #666)" if light else "linear-gradient(90deg, #444, #aaa)"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..700&display=swap');

html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; scroll-behavior: smooth; }}
.stApp {{ background: {bg}; color: {txt}; }}

/* Hero */
.hero-name {{
    font-size: clamp(3rem, 12vw, 6rem); font-weight: 800;
    background: linear-gradient(135deg, {txt}, {muted});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-align: center; line-height: 1.1; margin-top: 0.3em;
}}
.hero-role {{ text-align: center; font-size: 1.2rem; color: {muted}; min-height: 2em; }}
.hero-statement {{ text-align: center; font-size: 1.3rem; font-weight: 500; color: {txt}; max-width: 600px; margin: 20px auto; }}

/* Card */
.card {{
    background: {card}; backdrop-filter: blur(10px); border: 1px solid {border};
    border-radius: 24px; padding: 40px; margin: 30px 0; box-shadow: {shadow};
    transition: 0.3s;
}}
.card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.08); }}

/* Quote */
.quote-card {{
    background: {card}; border-left: 4px solid {accent};
    border-radius: 12px; padding: 20px 25px; margin: 16px 0;
    font-style: italic; font-size: 1.05rem;
}}

/* Principles */
.principle-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }}
.principle-tile {{
    background: {card}; border: 1px solid {border}; border-radius: 20px;
    padding: 25px 15px; text-align: center; transition: 0.3s;
}}
.principle-tile:hover {{ transform: translateY(-6px); border-color: {accent}; }}
.principle-icon {{ font-size: 2rem; margin-bottom: 10px; }}

/* Timeline */
.timeline {{ position: relative; padding-left: 40px; margin: 30px 0; }}
.timeline::before {{ content:''; position: absolute; left: 20px; top:0; bottom:0; width:2px; background:{muted}; opacity:0.3; }}
.timeline-item {{ position: relative; margin-bottom: 28px; }}
.timeline-dot {{ position: absolute; left:-30px; top:4px; width:20px; height:20px; background:{accent}; border-radius:50%; box-shadow:0 0 10px {accent}44; }}
.timeline-content {{ font-weight:500; }}

/* Skills progress bars */
.skill-label {{ display: flex; justify-content: space-between; font-weight:500; margin-top: 20px; }}
.stProgress > div > div > div > div {{ background: {progress_bg} !important; border-radius: 20px; }}

/* Contact */
.contact-tile {{
    background: {card}; border: 1px solid {border}; border-radius: 20px;
    padding: 25px; text-align: center; transition: 0.3s;
}}
.contact-tile:hover {{ transform: translateY(-4px); border-color: {accent}; }}
.contact-icon {{ font-size: 1.8rem; margin-bottom: 10px; }}

/* Footer */
.footer {{ text-align: center; padding: 40px 20px; color: {muted}; }}

/* Reveal */
.reveal {{ opacity: 0; transform: translateY(20px); transition: all 0.6s ease; }}
.reveal.visible {{ opacity: 1; transform: translateY(0); }}
</style>
""", unsafe_allow_html=True)

# Theme toggle button
_, btn_col = st.columns([5,1])
with btn_col:
    st.button("🌓 Toggle Theme" if light else "☀️ Toggle Theme", on_click=toggle)

# ---- HERO ----
st.markdown('<div class="hero-name">Abdullah Bin Fahad</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-role" id="role-rotator"></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-statement">Building technologies that expand human potential.</div>', unsafe_allow_html=True)

# Rotating roles
roles = ["Automation Engineer","AI Entrepreneur","Independent Thinker","Technology Philosopher","Future Visionary"]
st.components.v1.html(f"""
<script>
const r = {roles};
let i=0;
const el=document.getElementById('role-rotator');
setInterval(()=>{{el.textContent=r[i]; i=(i+1)%r.length}},2000);
el.textContent=r[0];
</script>
""", height=0)

# Scroll reveal
st.components.v1.html("""
<script>
const obs = new IntersectionObserver((e)=>e.forEach(en=>{if(en.isIntersecting) en.target.classList.add('visible')}),{threshold:0.2});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
new MutationObserver(()=>document.querySelectorAll('.reveal:not(.visible)').forEach(el=>obs.observe(el))).observe(document.body,{childList:true,subtree:true});
</script>
""", height=0)

# ---- WHO IS ABDULLAH ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🌐 Who Is Abdullah Bin Fahad?")
st.markdown("""
**Abdullah Bin Fahad** is a Bangladeshi Automation Engineering student at Nanjing Tech University in China, an AI enthusiast, entrepreneur, writer, and independent thinker.  
His work centers on the intersection of **technology, education, philosophy, and human development**. Rather than viewing AI as a replacement for people, he believes it should **expand human potential, creativity, and critical thinking**.

Driven by curiosity and long‑term vision, he builds projects that combine engineering with real‑world impact. His interests span **AI, robotics, embedded systems, business, psychology, philosophy, and education**. For him, learning is a **continuous process of questioning assumptions, refining ideas, and turning understanding into practical solutions**.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- PHILOSOPHY QUOTES ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🧠 Personal Philosophy")
for q in [
    "Technology should empower humanity, not replace it.",
    "Knowledge has little value unless it creates positive change in people’s lives.",
    "The future belongs to those who keep learning long after others stop.",
    "Success is built through discipline, consistency, and independent thinking.",
    "Innovation begins where curiosity meets responsibility.",
    "Character is the foundation of every lasting achievement."
]:
    st.markdown(f'<div class="quote-card">“{q}”</div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- CORE PRINCIPLES ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## ⚖️ Core Principles")
principles = [
    ("🧭","Think independently before following the crowd."),
    ("💡","Build solutions that create lasting value."),
    ("📚","Stay curious and embrace lifelong learning."),
    ("⚙️","Use technology responsibly and ethically."),
    ("🤝","Lead with integrity, humility, and purpose."),
    ("🚀","Turn ideas into action through discipline."),
    ("🌱","Measure success by the positive impact left on others.")
]
cols = st.columns(4)
for i, (icon, text) in enumerate(principles):
    with cols[i%4]:
        st.markdown(f'<div class="principle-tile"><div class="principle-icon">{icon}</div><p style="font-weight:500;">{text}</p></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- TIMELINE ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🛤 My Journey")
st.markdown('<div class="timeline">', unsafe_allow_html=True)
for item in [
    "Bangladesh – Early curiosity & science foundation",
    "SSC & HSC – Academic excellence in science",
    "Nanjing Tech University – Automation Engineering (2025–2029)",
    "AI & Entrepreneurship – Building MarketLens AI",
    "Writing & Philosophy – Authored 'Moral Values'",
    "Smart Calculator – Educational tech for underserved students"
]:
    st.markdown(f'<div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">{item}</div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- SKILLS (progress bars) ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## ⚡ Technical Skills")
skills = {
    "Python": 95, "C/C++": 80, "HTML/CSS": 85,
    "Automation & Control": 90, "Digital Marketing": 88,
    "Video Editing": 85, "Microsoft Office": 92
}
for skill, val in skills.items():
    st.markdown(f'<div class="skill-label"><span>{skill}</span><span>{val}%</span></div>', unsafe_allow_html=True)
    st.progress(val)
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- PROJECTS ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🧑🏻‍💻 Featured Projects")
c1, c2 = st.columns(2)
with c1:
    st.markdown("### MarketLens AI")
    st.markdown("""
    *www.marketlens-ai.com*  
    AI decision‑making agent for cross‑border e‑commerce.  
    Real‑time market intelligence, consumer review analysis, tariff risk simulation.  
    <a href="https://www.marketlens-ai.com" target="_blank">Visit project →</a>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("### 🧮 Smart Calculator")
    st.markdown("""
    Educational device for low‑connectivity regions.  
    AI homework help, offline mesh networking, 10+ languages, GPS tracking.  
    *Coming soon.*
    """)
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- VISION ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🔭 Vision")
st.markdown("""
> To build technologies that combine **Artificial Intelligence, Engineering, and Education** to make knowledge more accessible, practical, and meaningful for everyone.  
> **Create. Inspire. Empower. Repeat.**
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- CONTACT ----
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 📬 Contact")
c1, c2, c3, c4 = st.columns(4)
for col, (icon, label, value) in zip([c1,c2,c3,c4], [
    ("📧","Email","abdullahbinfahad.abf@gmail.com"),
    ("💻","GitHub","github.com/abdullahbinfahad"),
    ("📍","Location","Nanjing, China"),
    ("📱","Phone","+86 18105180247")
]):
    with col:
        st.markdown(f'<div class="contact-tile"><div class="contact-icon">{icon}</div><h4>{label}</h4><p style="font-size:0.9rem;">{value}</p></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown(f"""
<div class="footer reveal">
    Designed & Engineered by Abdullah Bin Fahad<br>
    <span style="font-size:0.85rem;">Building Tomorrow. One Idea at a Time.</span><br>
    <a href="https://www.abdullahbinfahad.info">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
