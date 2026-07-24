import streamlit as st

st.set_page_config(
    page_title="Abdullah Bin Fahad – Personal Website",
    page_icon="🧠",
    layout="wide"
)

# ---- THEME TOGGLE ----
if "theme" not in st.session_state:
    st.session_state.theme = "light"  # default white mode

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Inject dynamic CSS based on theme
if st.session_state.theme == "light":
    bg_color = "#ffffff"
    card_bg = "rgba(0,0,0,0.03)"
    text_color = "#1a1a1a"
    muted_color = "#555555"
    accent = "#1a1a1a"
    border_color = "rgba(0,0,0,0.08)"
    shadow = "0 4px 20px rgba(0,0,0,0.05)"
    gradient_bg = "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)"
    card_hover = "0 8px 30px rgba(0,0,0,0.1)"
    progress_bg = "linear-gradient(90deg, #333, #666)"
    hero_text = "linear-gradient(135deg, #111, #333)"
    quote_border = "4px solid #333"
else:
    bg_color = "#0a0a0a"
    card_bg = "rgba(255,255,255,0.04)"
    text_color = "#e0e0e0"
    muted_color = "#aaaaaa"
    accent = "#ffffff"
    border_color = "rgba(255,255,255,0.08)"
    shadow = "0 4px 20px rgba(0,0,0,0.4)"
    gradient_bg = "linear-gradient(135deg, #000000 0%, #1a1a1a 100%)"
    card_hover = "0 8px 30px rgba(0,0,0,0.8)"
    progress_bg = "linear-gradient(90deg, #444, #aaa)"
    hero_text = "linear-gradient(135deg, #fff, #ccc)"
    quote_border = "4px solid #888"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    scroll-behavior: smooth;
}}

.stApp {{
    background: {bg_color};
    color: {text_color};
}}

/* Hero */
.hero-name {{
    font-size: clamp(3rem, 10vw, 5rem);
    font-weight: 700;
    background: {hero_text};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin-bottom: 0.2em;
}}
.hero-role {{
    text-align: center;
    font-size: 1.2rem;
    font-weight: 500;
    color: {muted_color};
    min-height: 2em;
}}
.hero-statement {{
    text-align: center;
    font-size: 1.3rem;
    font-weight: 500;
    color: {text_color};
    max-width: 600px;
    margin: 20px auto;
}}

/* Section cards */
.card {{
    background: {card_bg};
    backdrop-filter: blur(10px);
    border: 1px solid {border_color};
    border-radius: 24px;
    padding: 40px;
    margin: 30px 0;
    box-shadow: {shadow};
    transition: all 0.3s ease;
}}
.card:hover {{
    box-shadow: {card_hover};
    transform: translateY(-2px);
}}

/* Quote card */
.quote-card {{
    background: {card_bg};
    border-left: {quote_border};
    border-radius: 12px;
    padding: 24px 28px;
    margin: 20px 0;
    font-style: italic;
    color: {text_color};
    font-size: 1.1rem;
    transition: 0.2s;
}}
.quote-card:hover {{
    background: rgba(128,128,128,0.1);
}}

/* Principles grid */
.principle-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    margin-top: 20px;
}}
.principle-tile {{
    background: {card_bg};
    border: 1px solid {border_color};
    border-radius: 20px;
    padding: 28px 20px;
    text-align: center;
    transition: 0.3s;
}}
.principle-tile:hover {{
    transform: translateY(-6px);
    border-color: {accent};
}}
.principle-icon {{
    font-size: 2rem;
    margin-bottom: 12px;
}}

/* Timeline */
.timeline {{
    position: relative;
    padding-left: 40px;
    margin: 30px 0;
}}
.timeline::before {{
    content: '';
    position: absolute;
    left: 20px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: {muted_color};
    opacity: 0.3;
}}
.timeline-item {{
    position: relative;
    margin-bottom: 28px;
}}
.timeline-dot {{
    position: absolute;
    left: -30px;
    top: 4px;
    width: 20px;
    height: 20px;
    background: {accent};
    border-radius: 50%;
    box-shadow: 0 0 12px {accent}44;
}}
.timeline-content {{
    font-size: 1.1rem;
    font-weight: 500;
    color: {text_color};
}}

/* Circular progress */
.circular-progress {{
    display: inline-block;
    position: relative;
    width: 90px;
    height: 90px;
}}
.circular-progress svg {{
    transform: rotate(-90deg);
}}
.circle-bg {{
    fill: none;
    stroke: {border_color};
    stroke-width: 6;
}}
.circle-fill {{
    fill: none;
    stroke: {accent};
    stroke-width: 6;
    stroke-linecap: round;
    transition: stroke-dashoffset 1.5s ease;
}}

/* Contact cards */
.contact-tile {{
    background: {card_bg};
    border: 1px solid {border_color};
    border-radius: 20px;
    padding: 28px 20px;
    text-align: center;
    transition: 0.3s;
}}
.contact-tile:hover {{
    transform: translateY(-4px);
    border-color: {accent};
}}
.contact-icon {{
    font-size: 1.8rem;
    margin-bottom: 10px;
}}

/* Footer */
.footer {{
    text-align: center;
    padding: 50px 20px;
    color: {muted_color};
    font-size: 0.9rem;
}}

/* Scroll reveal */
.reveal {{
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.6s ease;
}}
.reveal.visible {{
    opacity: 1;
    transform: translateY(0);
}}
</style>
""", unsafe_allow_html=True)

# Theme toggle button (top right)
col_toggle = st.columns([5,1])[1]
with col_toggle:
    st.button("🌓 Toggle Theme" if st.session_state.theme == "light" else "☀️ Toggle Theme",
              on_click=toggle_theme,
              key="theme_toggle",
              use_container_width=True)

# ---- HERO ----
st.markdown("""
<div class="hero-name" style="margin-top: 20px;">Abdullah Bin Fahad</div>
<div class="hero-role" id="role-text"></div>
<div class="hero-statement">Building technologies that expand human potential.</div>
""", unsafe_allow_html=True)

# Rotating roles (typewriter effect)
roles = [
    "Automation Engineer",
    "AI Entrepreneur",
    "Independent Thinker",
    "Technology Philosopher",
    "Future Visionary"
]
roles_js = ", ".join(f'"{r}"' for r in roles)
st.components.v1.html(f"""
<script>
const roles = [{roles_js}];
let i = 0;
const el = document.getElementById('role-text');
setInterval(() => {{
    el.textContent = roles[i];
    i = (i+1) % roles.length;
}}, 2000);
el.textContent = roles[0];
</script>
""", height=0)

# Scroll reveal (Intersection Observer)
st.components.v1.html("""
<script>
(function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.2 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    new MutationObserver(() => {
        document.querySelectorAll('.reveal:not(.visible)').forEach(el => observer.observe(el));
    }).observe(document.body, { childList: true, subtree: true });
})();
</script>
""", height=0)

# ---- SECTIONS ----

# About Me (Who Is Abdullah Bin Fahad?)
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🌐 Who Is Abdullah Bin Fahad?")
st.markdown("""
**Abdullah Bin Fahad** is a Bangladeshi Automation Engineering student at Nanjing Tech University in China, an AI enthusiast, entrepreneur, writer, and independent thinker.  
His work centers on the intersection of **technology, education, philosophy, and human development**. Rather than viewing artificial intelligence as a replacement for people, he believes it should **expand human potential, creativity, and critical thinking**.

Driven by curiosity and long‑term vision, he builds projects that combine engineering with real‑world impact. His interests span **artificial intelligence, robotics, embedded systems, business innovation, psychology, philosophy, and education**. He is motivated by solving meaningful problems — not pursuing technology for its own sake.

For Fahad, learning is a **continuous process of questioning assumptions, refining ideas, and transforming understanding into practical solutions**. Genuine progress, he believes, comes from discipline, intellectual honesty, and consistent action.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# Personal Philosophy
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🧠 Personal Philosophy")
philosophy_quotes = [
    "Technology should empower humanity, not replace it.",
    "Knowledge has little value unless it creates positive change in people’s lives.",
    "The future belongs to those who keep learning long after others stop.",
    "Success is built through discipline, consistency, and the courage to think independently.",
    "Question assumptions, seek truth, and let evidence shape your beliefs.",
    "Innovation begins where curiosity meets responsibility.",
    "Character is the foundation upon which every lasting achievement is built.",
    "Dream boldly, build patiently, and improve continuously."
]
for q in philosophy_quotes:
    st.markdown(f'<div class="quote-card">“{q}”</div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Core Principles
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## ⚖️ Core Principles")
principles = [
    ("🧭", "Think independently before following the crowd."),
    ("💡", "Build solutions that create lasting value."),
    ("📚", "Stay curious and embrace lifelong learning."),
    ("⚙️", "Use technology responsibly and ethically."),
    ("🤝", "Lead with integrity, humility, and purpose."),
    ("🚀", "Turn ideas into action through discipline and persistence."),
    ("🌱", "Measure success by the positive impact left on others.")
]
cols = st.columns(4)
for i, (icon, text) in enumerate(principles):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="principle-tile">
            <div class="principle-icon">{icon}</div>
            <p style="font-weight:500;">{text}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Journey (Timeline)
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🛤 My Journey")
timeline_items = [
    "Bangladesh – Early curiosity & science background",
    "SSC & HSC – Academic foundation in science",
    "Nanjing Tech University – Automation Engineering (2025–2029)",
    "AI & Entrepreneurship – Building MarketLens AI",
    "Writing & Philosophy – Authored 'Moral Values'",
    "Smart Calculator – Educational tech for underserved students",
    "Future – Expanding into AI, robotics, and global impact"
]
st.markdown('<div class="timeline">', unsafe_allow_html=True)
for item in timeline_items:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">{item}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Skills (Circular Progress)
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## ⚡ Technical Skills")
skills = {
    "Python": 95,
    "C/C++": 80,
    "HTML/CSS": 85,
    "Automation": 90,
    "Digital Marketing": 88,
    "Video Editing": 85,
    "MS Office": 92
}
cols = st.columns(4)
for i, (skill, value) in enumerate(skills.items()):
    with cols[i % 4]:
        radius = 36
        circumference = 2 * 3.14159 * radius
        offset = circumference - (value / 100) * circumference
        st.markdown(f"""
        <div style="text-align:center; margin:20px 0;">
            <div class="circular-progress">
                <svg width="90" height="90" viewBox="0 0 100 100">
                    <circle class="circle-bg" cx="50" cy="50" r="{radius}"></circle>
                    <circle class="circle-fill" cx="50" cy="50" r="{radius}" 
                        stroke-dasharray="{circumference}" 
                        stroke-dashoffset="{circumference}" 
                        data-offset="{offset}"></circle>
                </svg>
                <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); 
                     font-weight:700; color:{accent}; font-size:1.1rem;">{value}%</div>
            </div>
            <div style="font-weight:500; margin-top:8px; color:{text_color};">{skill}</div>
        </div>
        """, unsafe_allow_html=True)

# Animate circles on scroll
st.components.v1.html("""
<script>
function animateCircles() {
    document.querySelectorAll('.circle-fill').forEach(circle => {
        const offset = circle.getAttribute('data-offset');
        if (offset) {
            circle.style.strokeDashoffset = offset;
            circle.removeAttribute('data-offset');
        }
    });
}
const circleObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) animateCircles();
    });
});
document.querySelectorAll('.circular-progress').forEach(el => circleObserver.observe(el));
</script>
""", height=0)
st.markdown('</div></div>', unsafe_allow_html=True)

# Featured Projects
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🧑🏻‍💻 Featured Projects")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### MarketLens AI")
    st.markdown("""
    *www.marketlens-ai.com*  
    An intelligent decision‑making agent for cross‑border e‑commerce.  
    It answers **“Which products will perform best?”** using real‑time market data, consumer reviews, and tariff risk analysis.  
    <br><a href="https://www.marketlens-ai.com" target="_blank">Visit Project →</a>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("### 🧮 Smart Calculator")
    st.markdown("""
    A next‑gen educational device for low‑connectivity regions.  
    Features AI homework help, offline mesh networking, 10+ language learning tools, GPS tracking, and more.  
    *Currently under development.*
    """)
st.markdown('</div></div>', unsafe_allow_html=True)

# Vision
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 🔭 Vision")
st.markdown("""
> To build technologies that combine **Artificial Intelligence, Engineering, and Education** to make knowledge more accessible, practical, and meaningful for everyone.  
> **Create. Inspire. Empower. Repeat.**
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# Contact
st.markdown('<div class="reveal"><div class="card">', unsafe_allow_html=True)
st.markdown("## 📬 Contact")
col1, col2, col3, col4 = st.columns(4)
contacts = [
    ("📧", "Email", "abdullahbinfahad.abf@gmail.com"),
    ("💻", "GitHub", "github.com/abdullahbinfahad"),
    ("📍", "Location", "Nanjing, China"),
    ("📱", "Phone", "+86 18105180247")
]
for col, (icon, label, value) in zip([col1, col2, col3, col4], contacts):
    with col:
        st.markdown(f"""
        <div class="contact-tile">
            <div class="contact-icon">{icon}</div>
            <h4>{label}</h4>
            <p style="font-size:0.9rem; color:{muted_color};">{value}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer reveal">
    Designed & Engineered by Abdullah Bin Fahad<br>
    <span style="font-size:0.8rem;">Building Tomorrow. One Idea at a Time.</span><br>
    <a href="https://www.abdullahbinfahad.info" style="color:{muted_color};">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
