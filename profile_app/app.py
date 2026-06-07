import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Abdullah Bin Fahad",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# DEEP BLACK FORMAL THEME – NO HOVER – NO MOUSE EFFECTS
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}

/* Black animated gradient */
.stApp {
    background: linear-gradient(-45deg, #000000, #0a0a0a, #111111, #050505, #000000);
    background-size: 400% 400%;
    animation: gradientBG 30s ease infinite;
}
@keyframes gradientBG {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Section wave divider */
.section-divider {
    position: relative;
    height: 80px;
    margin: 40px 0 -40px 0;
    overflow: hidden;
    line-height: 0;
}
.section-divider svg {
    position: relative;
    display: block;
    width: calc(100% + 1.3px);
    height: 80px;
    transform: rotateY(180deg);
}
.section-divider .shape-fill {
    fill: #0a0a0a;
}

/* Static glass cards */
.glass {
    background: rgba(20, 20, 20, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 35px;
    margin: 25px 0;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8);
}

/* Locked / blurred project cards */
.locked-project {
    background: rgba(30, 30, 30, 0.5);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    color: #666;
    filter: blur(3px);
    user-select: none;
    pointer-events: none;
    position: relative;
}
.locked-project .lock-icon {
    font-size: 2rem;
    margin-bottom: 10px;
    opacity: 0.6;
}

/* Title float */
.title {
    text-align: center;
    font-size: clamp(3rem, 10vw, 5rem);
    font-weight: 800;
    color: #ffffff;
    animation: floatText 4s ease-in-out infinite;
}
@keyframes floatText {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-4px); }
}

.subtitle {
    text-align: center;
    color: #aaaaaa;
    font-size: clamp(1rem, 4vw, 1.3rem);
    margin-bottom: 25px;
    letter-spacing: 1px;
}

.quote {
    text-align: center;
    color: #e0e0e0;
    font-size: clamp(1.1rem, 5vw, 1.6rem);
    font-style: italic;
    line-height: 1.7;
}

/* Progress bars */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #444444, #888888) !important;
    border-radius: 20px;
}

h1, h2, h3, p, li {
    color: #e0e0e0;
}
a {
    color: #999999;
    text-decoration: none;
}

.footer {
    text-align: center;
    color: #666666;
    margin-top: 60px;
    padding: 30px;
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    .glass {
        padding: 20px;
        border-radius: 20px;
    }
    .section-divider {
        height: 50px;
        margin: 20px 0 -20px 0;
    }
    .section-divider svg {
        height: 50px;
    }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# 3D BACKGROUND – MODERN SHAPES (wireframe + solid)
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

// Low‑light scene
scene.add(new THREE.AmbientLight(0x222222));
const dirLight = new THREE.DirectionalLight(0xffffff, 0.2);
dirLight.position.set(1, 1, 1);
scene.add(dirLight);

// Modern shapes: wireframe + semi‑transparent solids
const shapes = [];
const geos = [
    new THREE.IcosahedronGeometry(0.7, 1),        // smoother sphere
    new THREE.TorusKnotGeometry(0.5, 0.15, 100, 16),
    new THREE.ConeGeometry(0.5, 1, 6),
    new THREE.TorusGeometry(0.7, 0.2, 16, 32),
    new THREE.OctahedronGeometry(0.6, 0),
    new THREE.TetrahedronGeometry(0.6, 0)
];

for (let i = 0; i < 30; i++) {
    const geo = geos[Math.floor(Math.random() * geos.length)];
    // Mix solid and wireframe materials
    const wireframe = Math.random() > 0.5;
    let material;
    if (wireframe) {
        material = new THREE.MeshBasicMaterial({
            color: 0xffffff,
            wireframe: true,
            transparent: true,
            opacity: 0.08
        });
    } else {
        material = new THREE.MeshStandardMaterial({
            color: 0xffffff,
            roughness: 0.6,
            metalness: 0.2,
            emissive: 0x000000,
            transparent: true,
            opacity: 0.12
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
# HERO – Philosophical quote
# =====================================================

st.markdown("""
<div class="title">Abdullah Bin Fahad</div>
<div class="subtitle">Automation Student • AI Builder • Entrepreneur • Writer • Philosopher</div>
<div class="quote">
"Humanity forges shields today for its safety;<br>
tomorrow, it shall flee from those very shields to save itself."
</div>
""", unsafe_allow_html=True)

# Wave divider
st.markdown("""
<div class="section-divider">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
    </svg>
</div>
""", unsafe_allow_html=True)

# =====================================================
# ABOUT (CV inspired strong points)
# =====================================================

st.markdown("""
<div class="glass">
<h2>🌍 About Me</h2>
<p>I am Abdullah Bin Fahad, an Automation Engineering freshman at Nanjing Tech University, awarded a Freshman Scholarship for academic excellence. I fuse engineering with philosophy, AI with ethics, and business with human behavior to design systems that empower decision‑making at scale.</p>
<p>My work spans <b>AI product development</b>, <b>automation prototyping</b>, <b>philosophical writing</b> (published book "Moral Values"), and <b>cross‑cultural public speaking</b>. I've delivered moral seminars to youth audiences, boosting community engagement by 40%, and authored comprehensive essays that distill complex ethical frameworks into accessible narratives.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# EDUCATION (quantified)
# =====================================================

st.markdown("""
<div class="glass">
<h2>🎓 Education</h2>
<h3>Bachelor of Science in Automation Engineering</h3>
<b>Nanjing Tech University, China</b> (2025–2029 Expected)<br>
• Core focus: Control Systems, Robotics, PLC, Sensors, C/C++<br>
<h3>Higher Secondary Certificate (Science)</h3>
<b>Bhola Government College, Bangladesh</b> (2022–2024)<br>
Physics, Chemistry, Mathematics, Biology, ICT<br>

<h3>Secondary School Certificate (Science)</h3>
<b>Dhaligour Nagar Secondary School, Bangladesh</b> (2020–2022)<br>
</div>
""", unsafe_allow_html=True)

# =====================================================
# EXPERIENCE & ACHIEVEMENTS (action verb + result)
# =====================================================

st.markdown("""
<div class="glass">
<h2>🏆 Key Achievements</h2>
<ul>
<li><b>Authored</b> philosophical book "Moral Values", synthesizing 3 ethical frameworks into an accessible 200‑page manuscript now used in 2 local study circles.</li>
<li><b>Delivered</b> 15+ moral seminars on self‑discipline and youth awakening, reaching 500+ attendees and receiving a 95% positive feedback rating.</li>
<li><b>Designed and tested</b> an automation prototype that reduced a repetitive lab process by 30% (timed comparison).</li>
<li><b>Volunteered</b> 100+ hours in cultural exchange programs, presenting Bangladeshi heritage to 200+ international visitors and improving cross‑cultural communication skills.</li>
<li><b>Organized</b> a Science & Technology Fair project on IoT‑based home automation, demonstrated to 300+ students and faculty.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# =====================================================
# TECHNICAL SKILLS (proficiency bars)
# =====================================================

st.markdown('<div class="glass"><h2>⚡ Technical Skills</h2>', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# LANGUAGES
# =====================================================

st.markdown("""
<div class="glass">
<h2>🗣 Languages</h2>
• Bangla – Native<br>
• English – Fluent (written & spoken)<br>
• Mandarin Chinese – Intermediate (HSK 3 equivalent)<br>
• Hindi / Urdu – Conversational
</div>
""", unsafe_allow_html=True)

# =====================================================
# PROJECTS – MarketLens AI
# =====================================================

st.markdown("""
<div class="glass">
<h2>🚀 Featured Project — MarketLens AI</h2>
<p>MarketLens AI is an intelligent decision‑making agent for Silk Road cross‑border e‑commerce. It answers <b>Which products will perform best in overseas markets?</b> by mining real‑time data, consumer reviews, and tariff risks.</p>
<p>Using <b>DeepSeek</b> and custom scoring algorithms, it transforms raw market signals into actionable business insights — acting as a strategic co‑pilot rather than a dashboard.</p>
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
</div>
""", unsafe_allow_html=True)

# =====================================================
# PROJECT – Smart Calculator
# =====================================================

st.markdown("""
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
""", unsafe_allow_html=True)

# =====================================================
# OTHER PROJECTS – LOCKED / BLURRED PREVIEW
# =====================================================

st.markdown('<h2 style="color:#e0e0e0; margin-top:40px;">🔒 Other Projects (Under Development)</h2>', unsafe_allow_html=True)

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

# =====================================================
# PHILOSOPHY
# =====================================================

st.markdown("""
<div class="glass">
<h2>🧠 Philosophy</h2>
<p>I believe technology should not replace human thinking; it should enhance it. My curiosity extends beyond engineering into the roots of wisdom, ethics, and civilization.</p>
<p>I explore: Intelligence vs Wisdom, Technology vs Humanity, Wealth vs Meaning, Power vs Responsibility, Progress vs Purpose.</p>
<p>Learning is my lifelong pursuit. Independent thought remains the most valuable ability one can cultivate — and systems that serve people, not the other way around, are what I strive to build.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# CONTACT & FOOTER
# =====================================================

st.markdown("""
<div class="glass">
<h2>📬 Contact</h2>
📧 abdullahbinfahad.abf@gmail.com<br>
📱 +86 18105180247<br>
🎓 Nanjing Tech University, Jiangpu Campus, Nanjing, China<br>
🔗 <a href="https://github.com/abdullahbinfahad" target="_blank">github.com/abdullahbinfahad</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
© 2026 Abdullah Bin Fahad<br>
<a href="https://www.abdullahbinfahad.info" style="color: #888;">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
