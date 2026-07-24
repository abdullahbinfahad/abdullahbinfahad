import streamlit as st

st.set_page_config(page_title="Abdullah Bin Fahad", page_icon="🧠", layout="wide")

# ---- THEME TOGGLE ----
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

light = st.session_state.theme == "light"
bg = "#ffffff" if light else "#0a0a0a"
card_bg = "rgba(0,0,0,0.04)" if light else "rgba(255,255,255,0.05)"
txt = "#1a1a1a" if light else "#e0e0e0"
muted = "#555" if light else "#aaa"
accent = "#1a1a1a" if light else "#ffffff"
border = "rgba(0,0,0,0.08)" if light else "rgba(255,255,255,0.1)"
shadow = "0 4px 20px rgba(0,0,0,0.05)" if light else "0 4px 20px rgba(0,0,0,0.4)"
progress_bg = "linear-gradient(90deg, #333, #666)" if light else "linear-gradient(90deg, #444, #aaa)"
wave_fill = "#f5f7fa" if light else "#0a0a0a"
quote_border = "4px solid #333" if light else "4px solid #888"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..700&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; scroll-behavior: smooth; }}
.stApp {{ background: {bg}; color: {txt}; }}

/* Hero */
.title {{
    font-size: clamp(3rem, 12vw, 5rem); font-weight: 800;
    background: linear-gradient(135deg, {txt}, {muted});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-align: center; line-height: 1.1; margin-top: 0.5em;
}}
.subtitle {{ text-align: center; font-size: 1.2rem; color: {muted}; margin-bottom: 0.5em; }}
.quote {{
    text-align: center; font-style: italic; color: {txt}; font-size: 1.2rem;
    max-width: 600px; margin: 20px auto;
}}

/* Wave divider */
.section-divider {{
    height: 80px; margin: 40px 0 -40px 0; overflow: hidden; line-height: 0;
}}
.section-divider svg {{ display: block; width: calc(100% + 1.3px); height: 80px; transform: rotateY(180deg); }}
.shape-fill {{ fill: {wave_fill}; }}

/* Cards */
.card, .glass {{
    background: {card_bg}; backdrop-filter: blur(10px);
    border: 1px solid {border}; border-radius: 24px; padding: 40px;
    margin: 30px 0; box-shadow: {shadow}; transition: 0.3s;
}}
.card:hover, .glass:hover {{ transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.08); }}

/* Quote card (for philosophy) */
.quote-card {{
    background: {card_bg}; border-left: {quote_border}; border-radius: 12px;
    padding: 20px 25px; margin: 16px 0; font-style: italic; font-size: 1.05rem;
}}

/* Principles grid */
.principle-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }}
.principle-tile {{
    background: {card_bg}; border: 1px solid {border}; border-radius: 20px;
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

/* Locked projects */
.locked-project {{
    background: rgba(30,30,30,0.5); backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.05); border-radius: 20px;
    padding: 25px; text-align: center; color: {muted}; filter: blur(3px);
    user-select: none; pointer-events: none;
}}
.lock-icon {{ font-size: 2rem; margin-bottom: 10px; opacity: 0.6; }}

/* Contact tiles */
.contact-tile {{
    background: {card_bg}; border: 1px solid {border}; border-radius: 20px;
    padding: 25px; text-align: center; transition: 0.3s;
}}
.contact-tile:hover {{ transform: translateY(-4px); border-color: {accent}; }}
.contact-icon {{ font-size: 1.8rem; margin-bottom: 10px; }}

/* Footer */
.footer {{ text-align: center; padding: 40px 20px; color: {muted}; }}

/* Scroll reveal */
.reveal {{ opacity: 0; transform: translateY(20px); transition: all 0.6s ease; }}
.reveal.visible {{ opacity: 1; transform: translateY(0); }}
</style>
""", unsafe_allow_html=True)

# Theme toggle button
_, btn_col = st.columns([5,1])
with btn_col:
    st.button("🌓 Toggle Theme" if light else "☀️ Toggle Theme", on_click=toggle)

# ---- HERO (original text blocks) ----
st.markdown("""
<div class="title">Abdullah Bin Fahad</div>
<div class="subtitle">Automation Student • Entrepreneur • Writer</div>
<div class="quote">
"Humanity forges shields today for its safety;<br>
tomorrow, it shall flee from those very shields to save itself."
</div>
""", unsafe_allow_html=True)

# Wave divider
st.markdown(f"""
<div class="section-divider">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
    </svg>
</div>
""", unsafe_allow_html=True)

# Scroll reveal script
st.components.v1.html("""
<script>
const obs = new IntersectionObserver((e)=>e.forEach(en=>{if(en.isIntersecting) en.target.classList.add('visible')}),{threshold:0.2});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
new MutationObserver(()=>document.querySelectorAll('.reveal:not(.visible)').forEach(el=>obs.observe(el))).observe(document.body,{childList:true,subtree:true});
</script>
""", height=0)

# ---- WHO IS ABDULLAH BIN FAHAD (new identity) ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🌐 Who Is Abdullah Bin Fahad?")
st.markdown("""
**Abdullah Bin Fahad** is a Bangladeshi Automation Engineering student at Nanjing Tech University in China, an AI enthusiast, entrepreneur, writer, and independent thinker.  
His work centers on the intersection of **technology, education, philosophy, and human development**. Rather than viewing AI as a replacement for people, he believes it should **expand human potential, creativity, and critical thinking**.

Driven by curiosity and long‑term vision, he builds projects that combine engineering with real‑world impact. His interests span **AI, robotics, embedded systems, business, psychology, philosophy, and education**. For him, learning is a **continuous process of questioning assumptions, refining ideas, and turning understanding into practical solutions**.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- PERSONAL PHILOSOPHY (quote cards) ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
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
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
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

# ---- MY JOURNEY (timeline) ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
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

# ---- ABOUT ME (original) ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🌍 About Me")
st.markdown("""
<p>I am Abdullah Bin Fahad, an Automation Engineering Student at Nanjing Tech University. I fuse engineering with philosophy, AI with ethics, and business with human behavior to design systems that empower decision‑making at scale.</p>
<p>My work spans <b>AI product development</b>, <b>automation prototyping</b>, <b>philosophical writing</b> (published book "Moral Values"), and <b>cross‑cultural public speaking</b>. I've delivered moral seminars to youth audiences, boosting community engagement by 40%, and authored comprehensive essays that distill complex ethical frameworks into accessible narratives.</p>
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- EDUCATION ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🎓 Education")
st.markdown("""
<h3>Bachelor of Science in Automation Engineering</h3>
<b>Nanjing Tech University, China</b> (2025–2029 Expected)<br>
Core focus: Control Systems, Robotics, PLC, Sensors, C/C++<br>
<h3>Higher Secondary Certificate (Science)</h3>
<b>Bhola Government College, Bangladesh</b> (2022–2024)<br>
Physics, Chemistry, Mathematics, Biology, ICT<br>
<h3>Secondary School Certificate (Science)</h3>
<b>Dhaligour Nagar Secondary School, Bangladesh</b> (2020–2022)
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- KEY ACHIEVEMENTS ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🏆 Key Achievements")
st.markdown("""
<ul>
<li><b>Authored</b> philosophical book "Moral Values", synthesizing 3 ethical frameworks into an accessible 200‑page manuscript now used in 2 local study circles.</li>
<li><b>Delivered</b> 15+ moral seminars on self‑discipline and youth awakening, reaching 500+ attendees and receiving a 95% positive feedback rating.</li>
<li><b>Designed and tested</b> an automation prototype that reduced a repetitive lab process by 30% (timed comparison).</li>
<li><b>Volunteered</b> 100+ hours in cultural exchange programs, presenting Bangladeshi heritage to 200+ international visitors and improving cross‑cultural communication skills.</li>
<li><b>Organized</b> a Science & Technology Fair project on IoT‑based home automation, demonstrated to 300+ students and faculty.</li>
</ul>
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- TECHNICAL SKILLS (progress bars) ----
st.markdown('<div class="reveal"><div class="glass"><h2>⚡ Technical Skills</h2>', unsafe_allow_html=True)

st.markdown("Automation & Control Systems")
st.progress(82)
st.markdown("Python Programming")
st.progress(78)
st.markdown("HTML / CSS")
st.progress(80)
st.markdown("C Programming")
st.progress(72)
st.markdown("Digital Marketing & Content Writing")
st.progress(88)
st.markdown("Video / Audio Editing")
st.progress(85)
st.markdown("Microsoft Office Suite")
st.progress(90)

st.markdown('</div></div>', unsafe_allow_html=True)

# ---- LANGUAGES ----
st.markdown("""
<div class="reveal"><div class="glass">
<h2>🗣 Languages</h2>
• Bangla – Native<br>
• English – Fluent (written & spoken)<br>
• Mandarin Chinese – Intermediate (HSK 3 equivalent)<br>
• Hindi / Urdu – Conversational
</div></div>
""", unsafe_allow_html=True)

# ---- FEATURED PROJECTS (original) ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("""
<h2>🧑🏻‍💻 Featured Project:<br>
1). MarketLens AI (www.marketlens-ai.com)</h2>
<p>MarketLens AI is an intelligent decision‑making agent for Silk Road cross‑border e‑commerce. It answers <b>Which products will perform best in overseas markets?</b> by mining real‑time data, consumer reviews, and tariff risks.</p>
<p>Using <b>API</b> and custom scoring algorithms, it transforms raw market signals into actionable business insights acting as a strategic co‑pilot rather than a dashboard.</p>
<h3>Core Capabilities</h3>
<ul>
<li>Real‑Time Market Trend Intelligence</li>
<li>AI Consumer Review Analysis</li>
<li>Dynamic Product Opportunity Scoring</li>
<li>Tariff & Logistics Risk Simulation</li>
<li>Interactive 3D Data Visualization</li>
<li>Multi‑Language AI Assistant</li>
<li>Competitive Gap Detection</li>
<li>Market Demand Forecasting</li>
<li>Strategic Decision Support</li>
</ul>
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# Smart Calculator
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("""
<h2>2).🧮 Smart Calculator</h2>
<p>A next‑generation educational device designed for students in low‑connectivity regions.</p>
<ul>
<li>✔ AI Assistant for instant homework help</li>
<li>✔ Offline Communication System (mesh networking)</li>
<li>✔ Language Learning Tools (10+ languages)</li>
<li>✔ GPS Tracking for child safety</li>
<li>✔ Educational Games for K‑12 curriculum</li>
<li>✔ Smart Dictionary (offline, contextual)</li>
<li>✔ Productivity System (task scheduling, focus timer)</li>
</ul>
<p><i>Built to bridge the digital divide and foster self‑learning.</i></p>
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- OTHER PROJECTS (locked) ----
st.markdown('<h2 style="margin-top:40px;">🔒 Other Projects (Under Development)</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>AI Research Tool</h3>
        <p>Confidential – details coming soon</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>Automation Dashboard</h3>
        <p>Under NDA – prototype phase</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>Philosophy Platform</h3>
        <p>Early concept – stay tuned</p>
    </div>
    """, unsafe_allow_html=True)

# ---- PHILOSOPHY (original) ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("""
<h2>🧠 Philosophy</h2>
<p>I believe technology should not replace human thinking; it should enhance it. My curiosity extends beyond engineering into the roots of wisdom, ethics, and civilization.</p>
<p>I explore: Intelligence vs Wisdom, Technology vs Humanity, Wealth vs Meaning, Power vs Responsibility, Progress vs Purpose.</p>
<p>Learning is my lifelong pursuit. Independent thought remains the most valuable ability one can cultivate — and systems that serve people, not the other way around, are what I strive to build.</p>
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- VISION ----
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🔭 Vision")
st.markdown("""
> To build technologies that combine **Artificial Intelligence, Engineering, and Education** to make knowledge more accessible, practical, and meaningful for everyone.  
> **Create. Inspire. Empower. Repeat.**
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ---- CONTACT ----
st.markdown("""
<div class="reveal"><div class="glass">
<h2>📬 Contact</h2>
📧 abdullahbinfahad.abf@gmail.com<br>
📱 +86 18105180247<br>
🎓 Nanjing Tech University, Jiangpu Campus, Nanjing, China<br>
🔗 <a href="https://github.com/abdullahbinfahad" target="_blank">github.com/abdullahbinfahad</a>
</div></div>
""", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown(f"""
<div class="footer reveal">
    © 2026 Abdullah Bin Fahad<br>
    <a href="https://www.abdullahbinfahad.info" style="color: {muted};">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
