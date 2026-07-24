import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Abdullah Bin Fahad",
    page_icon="🧠",
    layout="wide"
)

# =====================================================
# MODERN DARK THEME – VISUAL & ANIMATED
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
    scroll-behavior: smooth;
}

/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #000000, #0a0a0a, #111111, #050505, #000000);
    background-size: 400% 400%;
    animation: gradientBG 25s ease infinite;
}
@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Scroll reveal base */
.reveal {
    opacity: 0;
    transform: translateY(40px);
    transition: all 0.9s cubic-bezier(0.22, 1, 0.36, 1);
}
.reveal.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Modern glass cards with subtle hover lift */
.glass {
    background: rgba(18, 18, 18, 0.7);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 28px;
    padding: 40px;
    margin: 30px 0;
    box-shadow: 0 10px 40px rgba(0,0,0,0.9);
    transition: all 0.3s ease;
}
.glass:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 50px rgba(0,0,0,1);
}

/* Hero title floating */
.hero-title {
    text-align: center;
    font-size: clamp(3.5rem, 10vw, 5.5rem);
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 30%, #bbbbbb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: floatTitle 4s ease-in-out infinite;
    margin-bottom: 10px;
}
@keyframes floatTitle {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}

/* Typewriter container */
.typewriter {
    text-align: center;
    color: #cccccc;
    font-size: clamp(1.1rem, 4vw, 1.5rem);
    font-weight: 500;
    min-height: 2.5rem;
    letter-spacing: 0.8px;
}

/* Quote card styling */
.quote-card {
    background: rgba(30, 30, 30, 0.6);
    border-left: 4px solid #888;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 20px 0;
    font-style: italic;
    color: #d0d0d0;
    font-size: 1.05rem;
    transition: all 0.3s ease;
}
.quote-card:hover {
    border-left-color: #ffffff;
    background: rgba(50, 50, 50, 0.6);
}

/* Principles grid */
.principles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
    margin-top: 25px;
}
.principle-item {
    background: rgba(20, 20, 20, 0.6);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 25px 20px;
    text-align: center;
    transition: all 0.3s ease;
}
.principle-item:hover {
    transform: scale(1.03);
    border-color: rgba(255,255,255,0.2);
    background: rgba(30, 30, 30, 0.8);
}
.principle-icon {
    font-size: 2rem;
    margin-bottom: 10px;
}

/* Progress bars */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #3a3a3a, #b0b0b0) !important;
    border-radius: 20px;
    height: 8px;
}

/* Typography */
h1, h2, h3, p, li {
    color: #e5e5e5;
}
a {
    color: #bbbbbb;
    text-decoration: none;
    transition: color 0.2s;
}
a:hover {
    color: #ffffff;
}

/* Locked project cards */
.locked-project {
    background: rgba(30, 30, 30, 0.45);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 30px 20px;
    text-align: center;
    color: #777;
    filter: blur(2.5px);
    user-select: none;
    pointer-events: none;
}
.lock-icon {
    font-size: 2.5rem;
    margin-bottom: 10px;
    opacity: 0.5;
}

.footer {
    text-align: center;
    color: #666;
    margin-top: 60px;
    padding: 30px;
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    .glass {
        padding: 25px;
        border-radius: 24px;
    }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# 3D BACKGROUND (reused modern shapes)
# =====================================================

components.html("""
<div id="three-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const container = document.getElementById('three-container');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 15;

const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
container.appendChild(renderer.domElement);

scene.add(new THREE.AmbientLight(0x222222));
const dirLight = new THREE.DirectionalLight(0xffffff, 0.2);
dirLight.position.set(1, 1, 1);
scene.add(dirLight);

const shapes = [];
const geos = [
    new THREE.IcosahedronGeometry(0.7, 1),
    new THREE.TorusKnotGeometry(0.5, 0.15, 100, 16),
    new THREE.ConeGeometry(0.5, 1, 6),
    new THREE.TorusGeometry(0.7, 0.2, 16, 32),
    new THREE.OctahedronGeometry(0.6, 0),
    new THREE.TetrahedronGeometry(0.6, 0)
];

for (let i = 0; i < 28; i++) {
    const geo = geos[Math.floor(Math.random() * geos.length)];
    const wireframe = Math.random() > 0.5;
    let material;
    if (wireframe) {
        material = new THREE.MeshBasicMaterial({
            color: 0xffffff,
            wireframe: true,
            transparent: true,
            opacity: 0.06
        });
    } else {
        material = new THREE.MeshStandardMaterial({
            color: 0xffffff,
            roughness: 0.7,
            metalness: 0.2,
            emissive: 0x000000,
            transparent: true,
            opacity: 0.1
        });
    }
    const mesh = new THREE.Mesh(geo, material);
    mesh.position.x = (Math.random() - 0.5) * 18;
    mesh.position.y = (Math.random() - 0.5) * 10;
    mesh.position.z = (Math.random() - 0.5) * 8 - 2;
    mesh.rotation.x = Math.random() * Math.PI;
    mesh.rotation.y = Math.random() * Math.PI;
    mesh.userData = {
        rotX: (Math.random() - 0.5) * 0.004,
        rotY: (Math.random() - 0.5) * 0.004,
        speedX: (Math.random() - 0.5) * 0.002,
        speedY: (Math.random() - 0.5) * 0.002,
        speedZ: (Math.random() - 0.5) * 0.002
    };
    scene.add(mesh);
    shapes.push(mesh);
}

function animate() {
    requestAnimationFrame(animate);
    shapes.forEach(mesh => {
        mesh.rotation.x += mesh.userData.rotX;
        mesh.rotation.y += mesh.userData.rotY;
        mesh.position.x += mesh.userData.speedX;
        mesh.position.y += mesh.userData.speedY;
        mesh.position.z += mesh.userData.speedZ;
        if (Math.abs(mesh.position.x) > 11) mesh.userData.speedX *= -1;
        if (Math.abs(mesh.position.y) > 7) mesh.userData.speedY *= -1;
        if (Math.abs(mesh.position.z) > 5) mesh.userData.speedZ *= -1;
    });
    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
</script>
""", height=0)

# =====================================================
# SCROLL REVEAL ANIMATION SCRIPT
# =====================================================

components.html("""
<script>
(function() {
    const revealElements = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.15 });
    revealElements.forEach(el => observer.observe(el));

    // Re-run observer after Streamlit might re-render
    const mutationObserver = new MutationObserver(() => {
        document.querySelectorAll('.reveal:not(.visible)').forEach(el => observer.observe(el));
    });
    mutationObserver.observe(document.body, { childList: true, subtree: true });
})();
</script>
""", height=0)

# =====================================================
# TYPEWRITER EFFECT FOR SUBTITLE
# =====================================================

components.html("""
<div class="typewriter" id="typewriter-target"></div>
<script>
const words = [
    "Automation Engineering Student",
    "AI Enthusiast",
    "Entrepreneur",
    "Writer",
    "Independent Thinker"
];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
const target = document.getElementById('typewriter-target');
function type() {
    const current = words[wordIndex];
    if (isDeleting) {
        target.textContent = current.substring(0, charIndex - 1);
        charIndex--;
    } else {
        target.textContent = current.substring(0, charIndex + 1);
        charIndex++;
    }
    if (!isDeleting && charIndex === current.length) {
        setTimeout(() => isDeleting = true, 2000);
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
    }
    const speed = isDeleting ? 50 : 100;
    setTimeout(type, speed);
}
type();
</script>
""", height=50)

# =====================================================
# HERO
# =====================================================

st.markdown('<div class="hero-title">Abdullah Bin Fahad</div>', unsafe_allow_html=True)
st.markdown('<div class="typewriter" style="color:#aaaaaa; margin-bottom: 20px;">Automation Engineering Student • Entrepreneur • Writer • AI Enthusiast</div>', unsafe_allow_html=True)

st.markdown("""
<div class="reveal">
    <div class="glass" style="text-align:center; font-size:1.1rem; font-style:italic; max-width:800px; margin:20px auto;">
        "Technology should empower humanity, not replace it."
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# WHO IS ABDULLAH BIN FAHAD?
# =====================================================

st.markdown('<div class="reveal"><div class="glass">', unsafe_allow_html=True)
st.markdown("""
## 🌐 Who Is Abdullah Bin Fahad?
Abdullah Bin Fahad is a Bangladeshi Automation Engineering student at Nanjing Tech University in China, an AI enthusiast, entrepreneur, writer, and independent thinker. His work centers on the intersection of **technology, education, philosophy, and human development**. Rather than viewing artificial intelligence as a replacement for people, he believes it should **expand human potential, creativity, and critical thinking**.

Driven by curiosity and long‑term vision, he is building projects that combine engineering with real‑world impact. His interests span **artificial intelligence, robotics, embedded systems, business innovation, psychology, philosophy, and education**. He is motivated by solving meaningful problems — not pursuing technology for its own sake.

For Fahad, learning is not simply the accumulation of knowledge — it is a **continuous process of questioning assumptions, refining ideas, and transforming understanding into practical solutions**. He believes that genuine progress comes from discipline, intellectual honesty, and consistent action.
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# PERSONAL PHILOSOPHY (quote cards)
# =====================================================

st.markdown('<div class="reveal"><div class="glass"><h2>🧠 Personal Philosophy</h2>', unsafe_allow_html=True)

quotes = [
    "“Technology should empower humanity, not replace it.”",
    "“Knowledge has little value unless it creates positive change in people’s lives.”",
    "“The future belongs to those who keep learning long after others stop.”",
    "“Success is built through discipline, consistency, and the courage to think independently.”",
    "“Question assumptions, seek truth, and let evidence shape your beliefs.”",
    "“Innovation begins where curiosity meets responsibility.”",
    "“Character is the foundation upon which every lasting achievement is built.”",
    "“Dream boldly, build patiently, and improve continuously.”"
]

cols = st.columns(2)
for i, quote in enumerate(quotes):
    with cols[i % 2]:
        st.markdown(f'<div class="quote-card">{quote}</div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# CORE PRINCIPLES (icon grid)
# =====================================================

st.markdown('<div class="reveal"><div class="glass"><h2>⚖️ Core Principles</h2>', unsafe_allow_html=True)

principles = [
    ("🧭", "Think independently before following the crowd."),
    ("💡", "Build solutions that create lasting value."),
    ("📚", "Stay curious and embrace lifelong learning."),
    ("⚙️", "Use technology responsibly and ethically."),
    ("🤝", "Lead with integrity, humility, and purpose."),
    ("🚀", "Turn ideas into action through discipline and persistence."),
    ("🌱", "Measure success by the positive impact left on others.")
]

# Create a grid manually with columns
cols = st.columns(3)
for i, (icon, text) in enumerate(principles):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="principle-item">
            <div class="principle-icon">{icon}</div>
            <p style="font-size:0.95rem; margin:0;">{text}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# VISION
# =====================================================

st.markdown("""
<div class="reveal">
    <div class="glass">
        <h2>🔭 Vision</h2>
        <p style="font-size:1.1rem; line-height:1.7;">
        Abdullah envisions a future where artificial intelligence, engineering, and education work together to make high‑quality knowledge more accessible, practical, and beneficial for everyone. His mission is to develop technologies that solve real problems, inspire innovation, and encourage future generations to think critically, act ethically, and create meaningful change.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# EDUCATION
# =====================================================

st.markdown('<div class="reveal"><div class="glass"><h2>🎓 Education</h2>', unsafe_allow_html=True)
st.markdown("""
**Bachelor of Science in Automation Engineering**  
Nanjing Tech University, China (2025–2029 Expected)  
Core focus: Control Systems, Robotics, PLC, Sensors, C/C++  

**Higher Secondary Certificate (Science)**  
Bhola Government College, Bangladesh (2022–2024)  

**Secondary School Certificate (Science)**  
Dhaligour Nagar Secondary School, Bangladesh (2020–2022)  
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# KEY ACHIEVEMENTS
# =====================================================

st.markdown('<div class="reveal"><div class="glass"><h2>🏆 Key Achievements</h2>', unsafe_allow_html=True)
st.markdown("""
- **Authored** philosophical book "Moral Values", synthesizing 3 ethical frameworks into an accessible 200‑page manuscript used in 2 local study circles.
- **Delivered** 15+ moral seminars on self‑discipline and youth awakening, reaching 500+ attendees with 95% positive feedback.
- **Designed and tested** an automation prototype that reduced a repetitive lab process by 30%.
- **Volunteered** 100+ hours in cultural exchange programs, presenting Bangladeshi heritage to 200+ international visitors.
- **Organized** a Science & Technology Fair project on IoT‑based home automation, demonstrated to 300+ students and faculty.
""")
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# TECHNICAL SKILLS
# =====================================================

st.markdown('<div class="reveal"><div class="glass"><h2>⚡ Technical Skills</h2>', unsafe_allow_html=True)

skills = {
    "Automation & Control Systems": 82,
    "Python Programming": 78,
    "HTML / CSS": 80,
    "C Programming": 72,
    "Digital Marketing & Content Writing": 88,
    "Video / Audio Editing": 85,
    "Microsoft Office Suite": 90
}
for skill, level in skills.items():
    st.markdown(skill)
    st.progress(level)

st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# LANGUAGES
# =====================================================

st.markdown("""
<div class="reveal">
    <div class="glass">
        <h2>🗣 Languages</h2>
        • Bangla – Native<br>
        • English – Fluent (written & spoken)<br>
        • Mandarin Chinese – Intermediate (HSK 3 equivalent)<br>
        • Hindi / Urdu – Conversational
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# PROJECTS
# =====================================================

st.markdown('<div class="reveal"><div class="glass"><h2>🧑🏻‍💻 Featured Project: MarketLens AI</h2>', unsafe_allow_html=True)
st.markdown("""
*www.marketlens-ai.com*

MarketLens AI is an intelligent decision‑making agent for Silk Road cross‑border e‑commerce. It answers **Which products will perform best in overseas markets?** by mining real‑time data, consumer reviews, and tariff risks.

Using **API** and custom scoring algorithms, it transforms raw market signals into actionable business insights — acting as a strategic co‑pilot rather than a dashboard.

**Core Capabilities**
- Real‑Time Market Trend Intelligence
- AI Consumer Review Analysis
- Dynamic Product Opportunity Scoring
- Tariff & Logistics Risk Simulation
- Interactive 3D Data Visualization
- Multi‑Language AI Assistant
- Competitive Gap Detection
- Market Demand Forecasting
- Strategic Decision Support
""")
st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown("""
<div class="reveal">
    <div class="glass">
        <h2>🧮 Smart Calculator</h2>
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
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# OTHER PROJECTS (locked previews)
# =====================================================

st.markdown('<h2 style="color:#e0e0e0; margin-top:50px;">🔒 Other Projects (Under Development)</h2>', unsafe_allow_html=True)
cols = st.columns(3)
with cols[0]:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>AI Research Tool</h3>
        <p>Confidential – details coming soon</p>
    </div>
    """, unsafe_allow_html=True)
with cols[1]:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>Automation Dashboard</h3>
        <p>Under NDA – prototype phase</p>
    </div>
    """, unsafe_allow_html=True)
with cols[2]:
    st.markdown("""
    <div class="locked-project">
        <div class="lock-icon">🔒</div>
        <h3>Philosophy Platform</h3>
        <p>Early concept – stay tuned</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CONTACT & FOOTER
# =====================================================

st.markdown("""
<div class="reveal">
    <div class="glass">
        <h2>📬 Contact</h2>
        📧 abdullahbinfahad.abf@gmail.com<br>
        📱 +86 18105180247<br>
        🎓 Nanjing Tech University, Jiangpu Campus, Nanjing, China<br>
        🔗 <a href="https://github.com/abdullahbinfahad" target="_blank">github.com/abdullahbinfahad</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
© 2026 Abdullah Bin Fahad<br>
<a href="https://www.abdullahbinfahad.info" style="color: #888;">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
