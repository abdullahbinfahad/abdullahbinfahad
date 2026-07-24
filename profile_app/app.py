import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="Abdullah Bin Fahad", page_icon="🧠", layout="wide")

# ====================================================
# THEME SYSTEM: Light / Dark / Cyber
# ====================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def cycle_theme():
    themes = ["light", "dark", "cyber"]
    idx = themes.index(st.session_state.theme)
    st.session_state.theme = themes[(idx + 1) % 3]

random_quote = random.choice([
    "Technology should empower humanity, not replace it.",
    "Knowledge has little value unless it creates positive change.",
    "Dream boldly. Build patiently. Improve continuously.",
    "Question assumptions. Seek truth. Follow evidence.",
    "Innovation begins where curiosity meets responsibility.",
    "Character is the foundation of every lasting achievement.",
    "Success is built through discipline, consistency, and independent thinking.",
    "Humanity forges shields today for its safety; tomorrow, it shall flee from those very shields to save itself."
])

# ====================================================
# CSS Variables by Theme
# ====================================================
theme = st.session_state.theme
if theme == "light":
    bg_main = "#f8f9fa"
    bg_card = "rgba(0,0,0,0.03)"
    text_primary = "#111"
    text_secondary = "#444"
    accent = "#111"
    border = "rgba(0,0,0,0.08)"
    progress_grad = "linear-gradient(90deg, #222, #666)"
    wave_fill = "#f8f9fa"
    glow_color = "0,0,0"
    hero_gradient = "linear-gradient(135deg, #111, #444)"
    card_shadow = "0 4px 20px rgba(0,0,0,0.05)"
    phi_bg = "rgba(255,255,255,0.7)"
elif theme == "dark":
    bg_main = "#0a0a0a"
    bg_card = "rgba(255,255,255,0.05)"
    text_primary = "#e0e0e0"
    text_secondary = "#aaa"
    accent = "#ffffff"
    border = "rgba(255,255,255,0.08)"
    progress_grad = "linear-gradient(90deg, #444, #aaa)"
    wave_fill = "#0a0a0a"
    glow_color = "255,255,255"
    hero_gradient = "linear-gradient(135deg, #ffffff, #cccccc)"
    card_shadow = "0 4px 20px rgba(0,0,0,0.4)"
    phi_bg = "rgba(10,10,10,0.8)"
else:  # cyber
    bg_main = "#050510"
    bg_card = "rgba(0,255,255,0.05)"
    text_primary = "#e0ffff"
    text_secondary = "#7fdbdb"
    accent = "#00ffff"
    border = "rgba(0,255,255,0.2)"
    progress_grad = "linear-gradient(90deg, #00ffff, #0080ff)"
    wave_fill = "#050510"
    glow_color = "0,255,255"
    hero_gradient = "linear-gradient(135deg, #00ffff, #0088ff)"
    card_shadow = "0 0 25px rgba(0,255,255,0.2)"
    phi_bg = "rgba(5,5,16,0.85)"

# ====================================================
# GLOBAL STYLES
# ====================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..900&display=swap');
html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    scroll-behavior: smooth;
}}
.stApp {{
    background: {bg_main};
    color: {text_primary};
}}

/* ---------- Hero ---------- */
.hero-name {{
    font-size: clamp(3rem, 12vw, 7rem);
    font-weight: 900;
    background: {hero_gradient};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    line-height: 1;
    margin: 0.3em 0 0.1em 0;
    letter-spacing: -0.02em;
}}
.hero-roles {{
    text-align: center;
    font-size: 1.4rem;
    color: {text_secondary};
    min-height: 2.5em;
    font-weight: 500;
}}
.hero-statement {{
    text-align: center;
    font-size: 1.5rem;
    font-weight: 600;
    color: {text_primary};
    max-width: 700px;
    margin: 20px auto 10px;
}}
.scroll-indicator {{
    text-align: center;
    color: {text_secondary};
    margin-top: 30px;
    animation: floatDown 2s infinite;
}}
@keyframes floatDown {{
    0%,100%{{ transform: translateY(0); opacity:0.6; }}
    50%{{ transform: translateY(10px); opacity:1; }}
}}

/* ---------- Cards & Glass ---------- */
.glass, .card {{
    background: {bg_card};
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid {border};
    border-radius: 28px;
    padding: 40px;
    margin: 40px 0;
    box-shadow: {card_shadow};
    transition: 0.3s;
}}
.glass:hover, .card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba({glow_color},0.15);
}}

/* ---------- Wave Divider ---------- */
.section-divider {{
    height: 80px;
    margin: 40px 0 -40px 0;
    overflow: hidden;
}}
.section-divider svg {{
    display: block;
    width: calc(100% + 1.3px);
    height: 80px;
    transform: rotateY(180deg);
}}
.shape-fill {{
    fill: {wave_fill};
}}

/* ---------- Philosophy Full‑screen Cards ---------- */
.phi-card {{
    min-height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px;
    margin: 0;
    opacity: 0;
    transform: scale(0.94);
    transition: all 0.8s cubic-bezier(0.22,1,0.36,1);
    scroll-snap-align: start;
    will-change: opacity, transform;
    background: {phi_bg};
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-radius: 40px;
    margin: 20px 0;
}}
.phi-card.visible {{
    opacity: 1;
    transform: scale(1);
}}
.phi-quote {{
    font-size: clamp(2rem, 8vw, 4.5rem);
    font-weight: 800;
    text-align: center;
    line-height: 1.2;
    background: {hero_gradient};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    max-width: 900px;
    /* Fallback for non-webkit */
    color: {text_primary};
}}

/* ---------- Principles Grid ---------- */
.principle-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
}}
.principle-tile {{
    background: {bg_card};
    border: 1px solid {border};
    border-radius: 24px;
    padding: 30px 20px;
    text-align: center;
    transition: 0.3s;
}}
.principle-tile:hover {{
    transform: translateY(-8px);
    border-color: {accent};
    box-shadow: 0 10px 30px rgba({glow_color},0.2);
}}
.principle-icon {{
    font-size: 2.2rem;
    margin-bottom: 12px;
}}

/* ---------- Horizontal Timeline ---------- */
.timeline-horizontal {{
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    gap: 40px;
    padding: 30px 0;
    scroll-snap-type: x mandatory;
}}
.timeline-node {{
    flex: 0 0 auto;
    width: 160px;
    text-align: center;
    position: relative;
    padding: 20px 10px;
    scroll-snap-align: center;
}}
.timeline-node::before {{
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, {accent}, transparent);
    opacity: 0.3;
    z-index: -1;
}}
.timeline-dot {{
    width: 20px;
    height: 20px;
    background: {accent};
    border-radius: 50%;
    margin: 0 auto 15px;
    box-shadow: 0 0 20px {accent};
}}
.timeline-year {{
    font-weight: 700;
    color: {accent};
    margin-bottom: 5px;
}}
.timeline-text {{
    color: {text_secondary};
    font-size: 0.9rem;
}}

/* ---------- Animated Counters ---------- */
.stat-card {{
    text-align: center;
    padding: 20px;
    background: {bg_card};
    border-radius: 20px;
    border: 1px solid {border};
    transition: 0.3s;
}}
.stat-card:hover {{
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba({glow_color},0.15);
}}
.stat-number {{
    font-size: 3rem;
    font-weight: 800;
    color: {accent};
}}
.stat-label {{
    color: {text_secondary};
    font-weight: 500;
}}

/* ---------- Locked Projects ---------- */
.locked-project {{
    background: rgba(30,30,30,0.6);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    color: {text_secondary};
    filter: blur(3px);
    user-select: none;
    pointer-events: none;
}}
.lock-icon {{
    font-size: 2.5rem;
    margin-bottom: 10px;
    opacity: 0.5;
}}

/* ---------- Contact Tiles ---------- */
.contact-tile {{
    background: {bg_card};
    border: 1px solid {border};
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    transition: 0.3s;
}}
.contact-tile:hover {{
    transform: translateY(-5px);
    border-color: {accent};
    box-shadow: 0 10px 25px rgba({glow_color},0.15);
}}
.contact-icon {{
    font-size: 2rem;
    margin-bottom: 12px;
}}

/* ---------- Footer ---------- */
.footer {{
    text-align: center;
    padding: 60px 20px;
    color: {text_secondary};
    background: linear-gradient(180deg, transparent 0%, {bg_main} 80%);
}}

/* ---------- Hidden Roadmap ---------- */
#hidden-roadmap {{
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    background: {bg_card};
    backdrop-filter: blur(30px);
    border: 2px solid {accent};
    border-radius: 30px;
    padding: 40px;
    z-index: 9999;
    color: {text_primary};
    box-shadow: 0 0 60px rgba({glow_color},0.3);
    max-width: 500px;
}}
#hidden-roadmap.visible {{
    display: block;
}}

/* ---------- Reveal Animation ---------- */
.reveal {{
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.7s ease;
}}
.reveal.visible {{
    opacity: 1;
    transform: translateY(0);
}}

/* ---------- Responsive ---------- */
@media (max-width: 768px) {{
    .glass, .card {{
        padding: 25px;
    }}
    .timeline-horizontal {{
        flex-direction: column;
        gap: 20px;
    }}
    .timeline-node::before {{
        top: 0;
        bottom: auto;
        left: 50%;
        width: 2px;
        height: 100%;
    }}
}}
</style>
""", unsafe_allow_html=True)

# ====================================================
# THEME TOGGLE BUTTON
# ====================================================
col_toggle = st.columns([5,1])[1]
with col_toggle:
    theme_label = {"light":"☀️ Light","dark":"🌙 Dark","cyber":"🌀 Cyber"}
    st.button(f"Theme: {theme_label[theme]}", on_click=cycle_theme, use_container_width=True)

# ====================================================
# JAVASCRIPT: Scroll Reveal, Philosophy Cards, Easter Eggs
# ====================================================
components.html(f"""
<script>
// Unified Intersection Observer for .reveal and .phi-card
const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
        if(entry.isIntersecting) {{
            entry.target.classList.add('visible');
            // For stat-cards we trigger counters via custom event
            if(entry.target.classList.contains('stat-card')) {{
                const counters = entry.target.querySelectorAll('.count-up');
                counters.forEach(counter => {{
                    const target = parseInt(counter.getAttribute('data-target'));
                    if(!target) return;
                    const suffix = counter.getAttribute('data-suffix') || '';
                    let start = 0;
                    const duration = 1500;
                    const step = timestamp => {{
                        if(!start) start = timestamp;
                        const progress = Math.min((timestamp - start) / duration, 1);
                        counter.textContent = Math.floor(progress * target) + suffix;
                        if(progress < 1) requestAnimationFrame(step);
                    }};
                    requestAnimationFrame(step);
                }});
                observer.unobserve(entry.target);
            }}
        }}
    }});
}}, {{ threshold: 0.2 }});

// Observe existing elements
document.querySelectorAll('.reveal, .phi-card').forEach(el => observer.observe(el));

// MutationObserver for dynamically added elements
const mutationObserver = new MutationObserver(() => {{
    document.querySelectorAll('.reveal:not(.visible), .phi-card:not(.visible)').forEach(el => observer.observe(el));
}});
mutationObserver.observe(document.body, {{ childList: true, subtree: true }});

// Easter egg 1: typing 'future' reveals hidden roadmap
let typed = '';
document.addEventListener('keydown', (e) => {{
    typed += e.key.toLowerCase();
    if(typed.includes('future')) {{
        document.getElementById('hidden-roadmap')?.classList.add('visible');
        typed = '';
        setTimeout(() => {{
            const roadmap = document.getElementById('hidden-roadmap');
            if(roadmap) roadmap.classList.remove('visible');
        }}, 6000);
    }}
    if(typed.length > 20) typed = typed.slice(-20);
}});

// Easter egg 2: double‑click toggles theme
let clickTimer;
document.addEventListener('click', (e) => {{
    if(clickTimer) {{
        clearTimeout(clickTimer);
        clickTimer = null;
        const btns = window.parent.document.querySelectorAll('button');
        for(let btn of btns) {{
            if(btn.innerText.includes('Theme:')) {{
                btn.click();
                break;
            }}
        }}
    }} else {{
        clickTimer = setTimeout(() => clickTimer = null, 400);
    }}
}});

// Random toast quote
setTimeout(() => {{
    const toast = document.createElement('div');
    toast.style.position = 'fixed';
    toast.style.bottom = '20px';
    toast.style.right = '20px';
    toast.style.background = '{bg_card}';
    toast.style.color = '{text_primary}';
    toast.style.padding = '15px 25px';
    toast.style.borderRadius = '15px';
    toast.style.border = '1px solid {border}';
    toast.style.backdropFilter = 'blur(15px)';
    toast.style.zIndex = '9999';
    toast.style.fontStyle = 'italic';
    toast.textContent = '"{random_quote}"';
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 7000);
}}, 1500);
</script>
""", height=0)

# ====================================================
# 3D NEURAL NETWORK BACKGROUND
# ====================================================
components.html(f"""
<div id="bg-canvas" style="position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000000, 0.0005);
const camera = new THREE.PerspectiveCamera(60, innerWidth/innerHeight, 0.1, 100);
camera.position.z = 50;
const renderer = new THREE.WebGLRenderer({{ alpha: true, antialias: true }});
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
document.getElementById('bg-canvas').appendChild(renderer.domElement);

const particleCount = 1000;
const positions = new Float32Array(particleCount * 3);
for(let i=0; i<particleCount*3; i+=3) {{
    positions[i] = (Math.random()-0.5)*120;
    positions[i+1] = (Math.random()-0.5)*60;
    positions[i+2] = (Math.random()-0.5)*60 - 20;
}}
const pGeo = new THREE.BufferGeometry();
pGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
const pMat = new THREE.PointsMaterial({{
    size: 0.2, color: new THREE.Color('{accent}'), transparent: true,
    opacity: 0.3, blending: THREE.AdditiveBlending
}});
const particles = new THREE.Points(pGeo, pMat);
scene.add(particles);

// Lines between close particles
const lineMat = new THREE.LineBasicMaterial({{ color: new THREE.Color('{accent}'), transparent: true, opacity: 0.08 }});
const linesGroup = new THREE.Group();
for(let i=0; i<particleCount; i++) {{
    const x1 = positions[i*3], y1 = positions[i*3+1], z1 = positions[i*3+2];
    for(let j=i+1; j<particleCount; j++) {{
        const x2 = positions[j*3], y2 = positions[j*3+1], z2 = positions[j*3+2];
        if(Math.hypot(x1-x2, y1-y2, z1-z2) < 12) {{
            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.Float32BufferAttribute([x1,y1,z1, x2,y2,z2], 3));
            const line = new THREE.Line(geo, lineMat);
            linesGroup.add(line);
        }}
    }}
}}
scene.add(linesGroup);

function animate() {{
    requestAnimationFrame(animate);
    particles.rotation.y += 0.0002;
    linesGroup.rotation.y = particles.rotation.y;
    renderer.render(scene, camera);
}}
animate();
window.addEventListener('resize', () => {{
    camera.aspect = innerWidth/innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
}});
</script>
""", height=0)

# ====================================================
# HERO (one line name)
# ====================================================
st.markdown(f"""
<div class="hero-name">ABDULLAH BIN FAHAD</div>
<div class="hero-roles" id="role-cycler"></div>
<div class="hero-statement">Building technologies that expand human potential.</div>
<div class="scroll-indicator">▼ &nbsp; Scroll to Discover</div>
""", unsafe_allow_html=True)

roles = ["Engineer", "Builder", "Thinker", "Entrepreneur", "Philosopher"]
components.html(f"""
<script>
const roles = {roles};
let idx = 0;
const el = document.getElementById('role-cycler');
setInterval(() => {{ el.textContent = roles[idx]; idx = (idx+1) % roles.length; }}, 1500);
el.textContent = roles[0];
</script>
""", height=0)

# Wave divider
st.markdown(f"""
<div class="section-divider">
    <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
    </svg>
</div>
""", unsafe_allow_html=True)

# ====================================================
# WHO IS ABDULLAH BIN FAHAD
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🌐 Who Is Abdullah Bin Fahad?")
st.markdown("""
**Abdullah Bin Fahad** is a Bangladeshi Automation Engineering student at Nanjing Tech University in China, an AI enthusiast, entrepreneur, writer, and independent thinker.  
His work centers on the intersection of **technology, education, philosophy, and human development**. Rather than viewing AI as a replacement for people, he believes it should **expand human potential, creativity, and critical thinking**.

Driven by curiosity and long‑term vision, he builds projects that combine engineering with real‑world impact. His interests span **AI, robotics, embedded systems, business, psychology, philosophy, and education**. For him, learning is a **continuous process of questioning assumptions, refining ideas, and turning understanding into practical solutions**.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# PHILOSOPHY FULL‑SCREEN CARDS (now clearly visible)
# ====================================================
quotes = [
    "Technology<br>should empower humanity,<br>not replace it.",
    "Knowledge has little value<br>unless it creates positive change.",
    "Dream boldly.<br>Build patiently.<br>Improve continuously.",
    "Question assumptions.<br>Seek truth.<br>Follow evidence.",
    "Innovation begins where<br>curiosity meets responsibility.",
    "Character is the foundation<br>of every lasting achievement."
]
for q in quotes:
    st.markdown(f"""
    <div class="phi-card">
        <div class="phi-quote">{q}</div>
    </div>
    """, unsafe_allow_html=True)

# ====================================================
# CORE PRINCIPLES
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## ⚖️ Core Principles")
principles = [
    ("🧠","Think Independently"),
    ("💡","Build Lasting Value"),
    ("📚","Lifelong Learning"),
    ("⚙️","Ethical Technology"),
    ("🤝","Integrity & Humility"),
    ("🚀","Action & Discipline"),
    ("🌍","Positive Impact"),
    ("✨","Curiosity Forever")
]
cols = st.columns(4)
for i, (icon, title) in enumerate(principles):
    with cols[i%4]:
        st.markdown(f"""
        <div class="principle-tile">
            <div class="principle-icon">{icon}</div>
            <h4 style="color:{text_primary}; margin:0;">{title}</h4>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# JOURNEY – Horizontal Timeline
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🛤 My Journey")
journey = [
    ("Bangladesh", "Early Curiosity"),
    ("Village", "Science Foundation"),
    ("Technology", "SSC & HSC"),
    ("China", "Nanjing Tech"),
    ("Automation", "Engineering"),
    ("AI", "MarketLens"),
    ("Entrepreneur", "Startup Vision"),
    ("Future", "Global Impact")
]
st.markdown('<div class="timeline-horizontal">', unsafe_allow_html=True)
for year, desc in journey:
    st.markdown(f"""
    <div class="timeline-node">
        <div class="timeline-dot"></div>
        <div class="timeline-year">{year}</div>
        <div class="timeline-text">{desc}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# ORIGINAL SECTIONS (About, Education, Achievements)
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🌍 About Me")
st.markdown("""
I am Abdullah Bin Fahad, an Automation Engineering Student at Nanjing Tech University. I fuse engineering with philosophy, AI with ethics, and business with human behavior to design systems that empower decision‑making at scale.

My work spans **AI product development**, **automation prototyping**, **philosophical writing** (published book "Moral Values"), and **cross‑cultural public speaking**. I've delivered moral seminars to youth audiences, boosting community engagement by 40%, and authored comprehensive essays that distill complex ethical frameworks into accessible narratives.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🎓 Education")
st.markdown("""
**Bachelor of Science in Automation Engineering**  
Nanjing Tech University, China (2025–2029 Expected)  
Core: Control Systems, Robotics, PLC, Sensors, C/C++

**Higher Secondary Certificate (Science)**  
Bhola Government College, Bangladesh (2022–2024)

**Secondary School Certificate (Science)**  
Dhaligour Nagar Secondary School, Bangladesh (2020–2022)
""")
st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🏆 Key Achievements")
st.markdown("""
- **Authored** "Moral Values", synthesizing 3 ethical frameworks into a 200‑page manuscript.
- **Delivered** 15+ moral seminars, reaching 500+ attendees (95% positive feedback).
- **Designed** an automation prototype reducing lab process time by 30%.
- **Volunteered** 100+ hours in cultural exchange, presenting Bangladeshi heritage to 200+ visitors.
- **Organized** IoT‑based home automation demo at Science Fair (300+ students/faculty).
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# TECHNICAL SKILLS
# ====================================================
st.markdown('<div class="reveal"><div class="glass"><h2>⚡ Technical Skills</h2>', unsafe_allow_html=True)
skills = [
    ("Automation & Control Systems", 82),
    ("Python Programming", 78),
    ("HTML / CSS", 80),
    ("C Programming", 72),
    ("Digital Marketing & Content Writing", 88),
    ("Video / Audio Editing", 85),
    ("Microsoft Office Suite", 90)
]
for name, val in skills:
    st.markdown(f'<div style="display:flex; justify-content:space-between; font-weight:500;"><span>{name}</span><span>{val}%</span></div>', unsafe_allow_html=True)
    st.progress(val)
st.markdown('</div></div>', unsafe_allow_html=True)

# Languages
st.markdown("""
<div class="reveal"><div class="glass">
<h2>🗣 Languages</h2>
• Bangla – Native<br>
• English – Fluent<br>
• Mandarin Chinese – Intermediate (HSK 3)<br>
• Hindi/Urdu – Conversational
</div></div>
""", unsafe_allow_html=True)

# ====================================================
# PROJECTS with 3D mockups
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🧑🏻‍💻 Featured Projects")
col1, col2 = st.columns(2)
with col1:
    # 3D laptop
    components.html("""
    <div style="width:100%; height:280px;" id="laptop3d"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    const container = document.getElementById('laptop3d');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth/280, 0.1, 100);
    camera.position.set(0,1,8);
    const renderer = new THREE.WebGLRenderer({alpha:true, antialias:true});
    renderer.setSize(container.clientWidth, 280);
    container.appendChild(renderer.domElement);
    scene.add(new THREE.AmbientLight(0x444444));
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(1,1,1); scene.add(light);
    const base = new THREE.Mesh(new THREE.BoxGeometry(3.5,0.1,2.2), new THREE.MeshStandardMaterial({color:0x333333, roughness:0.3, metalness:0.8}));
    base.position.y = -1.2; scene.add(base);
    const screen = new THREE.Mesh(new THREE.BoxGeometry(3.3,2.2,0.05), new THREE.MeshStandardMaterial({color:0x111122, emissive:0x000033, roughness:0.2}));
    screen.position.set(0,0.3,-1.2); screen.rotation.x = -0.3; scene.add(screen);
    function animate(){ requestAnimationFrame(animate); screen.rotation.y += 0.005; base.rotation.y = screen.rotation.y; renderer.render(scene,camera); }
    animate();
    </script>
    """, height=280)
    st.markdown("**MarketLens AI** — Intelligent cross‑border e‑commerce agent. Real‑time market intelligence, consumer review analysis, tariff risk simulation. [Visit →](https://www.marketlens-ai.com)")
with col2:
    components.html("""
    <div style="width:100%; height:280px;" id="calc3d"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    const c2 = document.getElementById('calc3d');
    const scene2 = new THREE.Scene();
    const cam2 = new THREE.PerspectiveCamera(45, c2.clientWidth/280, 0.1, 100);
    cam2.position.set(0,0.5,7);
    const renderer2 = new THREE.WebGLRenderer({alpha:true});
    renderer2.setSize(c2.clientWidth, 280);
    c2.appendChild(renderer2.domElement);
    scene2.add(new THREE.AmbientLight(0x444444));
    const l2 = new THREE.DirectionalLight(0xffffff,0.8); l2.position.set(1,1,1); scene2.add(l2);
    const body = new THREE.Mesh(new THREE.BoxGeometry(2.5,3.5,0.5), new THREE.MeshStandardMaterial({color:0x1a1a1a, roughness:0.2, metalness:0.9}));
    scene2.add(body);
    const scr = new THREE.Mesh(new THREE.PlaneGeometry(2,0.7), new THREE.MeshBasicMaterial({color:0x3366ff, transparent:true, opacity:0.8}));
    scr.position.set(0,0.8,0.26); scene2.add(scr);
    function animate2(){ requestAnimationFrame(animate2); body.rotation.y += 0.008; scr.rotation.y = body.rotation.y; renderer2.render(scene2,cam2); }
    animate2();
    </script>
    """, height=280)
    st.markdown("**🧮 Smart Calculator** — Educational device for low‑connectivity areas. AI assistant, offline mesh, 10+ languages, GPS. *Coming soon.*")
st.markdown('</div></div>', unsafe_allow_html=True)

# Locked projects
st.markdown('<h2 style="margin-top:50px;">🔒 Other Projects (Under Development)</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>AI Research Tool</h3>
        <p>Confidential</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>Automation Dashboard</h3>
        <p>Under NDA</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>Philosophy Platform</h3>
        <p>Early concept</p>
    </div>
    """, unsafe_allow_html=True)

# ====================================================
# ACHIEVEMENT WALL (animated counters)
# ====================================================
st.markdown('<div class="reveal"><div class="glass"><h2>📊 By the Numbers</h2>', unsafe_allow_html=True)
cols = st.columns(5)
stats = [("15+","Seminars"),("6+","Projects"),("4+","Research Areas"),("500+","Audience"),("4","Languages")]
for col, (num, label) in zip(cols, stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number count-up" data-target="{num.replace('+','')}" data-suffix="+">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# PHILOSOPHY (original)
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🧠 Philosophy")
st.markdown("""
I believe technology should not replace human thinking; it should enhance it. My curiosity extends beyond engineering into the roots of wisdom, ethics, and civilization.

I explore: Intelligence vs Wisdom, Technology vs Humanity, Wealth vs Meaning, Power vs Responsibility, Progress vs Purpose.

Learning is my lifelong pursuit. Independent thought remains the most valuable ability one can cultivate — and systems that serve people, not the other way around, are what I strive to build.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# VISION
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 🔭 Vision")
st.markdown(f"""
> To build technologies that combine **Artificial Intelligence, Engineering, and Education** to make knowledge more accessible, practical, and meaningful for everyone.
>
> **Create. Inspire. Empower. Repeat.**
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# CONTACT
# ====================================================
st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("## 📬 Contact")
c1,c2,c3,c4 = st.columns(4)
contacts = [
    ("📧","Email","abdullahbinfahad.abf@gmail.com"),
    ("💻","GitHub","github.com/abdullahbinfahad"),
    ("📍","Location","Nanjing, China"),
    ("📱","Phone","+86 18105180247")
]
for col,(icon,title,val) in zip([c1,c2,c3,c4], contacts):
    with col:
        st.markdown(f"""
        <div class="contact-tile">
            <div class="contact-icon">{icon}</div>
            <h4>{title}</h4>
            <p style="font-size:0.9rem;">{val}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ====================================================
# FOOTER
# ====================================================
st.markdown(f"""
<div class="footer">
    <span style="font-size:1.5rem; font-weight:600;">Building Tomorrow.</span><br>
    <span style="font-size:1rem;">One Idea. One Innovation. One Step at a Time.</span><br><br>
    © 2026 Abdullah Bin Fahad<br>
    <a href="https://www.abdullahbinfahad.info" style="color:{text_secondary};">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)

# ====================================================
# HIDDEN ROADMAP (easter egg)
# ====================================================
st.markdown(f"""
<div id="hidden-roadmap">
    <h3 style="color:{accent};">🚀 Secret Roadmap</h3>
    <p>2025 – MarketLens AI</p>
    <p>2025 – Smart Calculator</p>
    <p>2026 – AI Research Platform</p>
    <p>2027 – Education System</p>
    <p>2028 – Global Startup</p>
    <p>2030 – Impact millions</p>
    <p style="font-size:0.8rem; color:{text_secondary};">(type 'future' anywhere to show this)</p>
</div>
""", unsafe_allow_html=True)
