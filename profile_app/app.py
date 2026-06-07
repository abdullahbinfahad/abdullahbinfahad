import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Abdullah Bin Fahad",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# MODERN BLACK THEME – NO HOVER – FORMAL ANIMATION
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}

/* Deep black animated gradient (no color hues) */
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

/* Section divider shape (dark) */
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

/* Static glass card – no hover effects */
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

/* Title – subtle float */
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
    line-height: 1.6;
}

/* Progress bars – static dark gradient */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #444444, #888888) !important;
    border-radius: 20px;
}

/* All text color */
h1, h2, h3, p, li, div {
    color: #e0e0e0;
}

/* Links */
a {
    color: #999999;
    text-decoration: none;
}

/* Footer */
.footer {
    text-align: center;
    color: #666666;
    margin-top: 60px;
    padding: 30px;
    font-size: 0.9rem;
}

/* Responsive */
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
# 3D BACKGROUND (no mouse effect, slow ambient rotation)
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

// Very dim ambient light
const ambientLight = new THREE.AmbientLight(0x222222);
scene.add(ambientLight);
const dirLight = new THREE.DirectionalLight(0xffffff, 0.3);
dirLight.position.set(1, 1, 1);
scene.add(dirLight);

// Create subtle monochrome shapes
const shapes = [];
const geos = [
    new THREE.IcosahedronGeometry(0.7, 0),
    new THREE.OctahedronGeometry(0.6, 0),
    new THREE.TetrahedronGeometry(0.5, 0),
    new THREE.TorusKnotGeometry(0.45, 0.12, 64, 8),
    new THREE.DodecahedronGeometry(0.6, 0)
];

for (let i = 0; i < 25; i++) {
    const geo = geos[Math.floor(Math.random() * geos.length)];
    const material = new THREE.MeshStandardMaterial({
        color: 0xffffff,
        roughness: 0.5,
        metalness: 0.3,
        emissive: 0x000000,
        emissiveIntensity: 0,
        transparent: true,
        opacity: 0.1
    });
    const mesh = new THREE.Mesh(geo, material);
    mesh.position.x = (Math.random() - 0.5) * 18;
    mesh.position.y = (Math.random() - 0.5) * 10;
    mesh.position.z = (Math.random() - 0.5) * 8 - 2;
    mesh.rotation.x = Math.random() * Math.PI;
    mesh.rotation.y = Math.random() * Math.PI;
    mesh.userData = {
        rotX: (Math.random() - 0.5) * 0.005,
        rotY: (Math.random() - 0.5) * 0.005,
        speedX: (Math.random() - 0.5) * 0.003,
        speedY: (Math.random() - 0.5) * 0.003,
        speedZ: (Math.random() - 0.5) * 0.003
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
# HERO SECTION
# =====================================================

st.markdown("""
<div class="title">Abdullah Bin Fahad</div>
<div class="subtitle">Automation Student • AI Builder • Entrepreneur • Writer • Philosopher</div>
<div class="quote">"Today, what people create for their safety,<br>in the future they will have to run for safety from it."</div>
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
# ABOUT
# =====================================================

st.markdown("""
<div class="glass">
<h2>🌍 About Me</h2>
<p>I am Abdullah Bin Fahad, an Automation Engineering student at Nanjing Tech University. My interests span Artificial Intelligence, Automation, Entrepreneurship, Technology Innovation, Philosophy, Business Strategy, Psychology, and Human Behavior.</p>
<p>I am deeply interested in understanding how intelligence, technology, and decision-making can be combined to create systems that solve real-world problems at scale. My long-term vision is to build globally impactful AI products, technology companies, and intelligent systems that empower people to make better decisions.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# EDUCATION
# =====================================================

st.markdown("""
<div class="glass">
<h2>🎓 Education</h2>
<b>Nanjing Tech University</b><br>
Bachelor of Engineering (Automation)<br>
School of Electrical Engineering and Control Science<br>
China
</div>
""", unsafe_allow_html=True)

# =====================================================
# SKILLS
# =====================================================

st.markdown('<div class="glass"><h2>⚡ Skills</h2>', unsafe_allow_html=True)

st.markdown("Artificial Intelligence")
st.progress(85)
st.markdown("Research & Analysis")
st.progress(92)
st.markdown("Business Strategy")
st.progress(88)
st.markdown("Python Programming")
st.progress(78)
st.markdown("Technical Writing")
st.progress(95)
st.markdown("Automation Engineering")
st.progress(80)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# FEATURED PROJECT – MARKETLENS AI
# =====================================================

st.markdown("""
<div class="glass">
<h2>🚀 Featured Project — MarketLens AI</h2>
<p>MarketLens AI is an intelligent decision-making agent built specifically for Silk Road cross-border e-commerce. It answers the critical question: <b>Which products will perform best in overseas markets?</b></p>
<p>By combining real-time market intelligence, consumer review mining, dynamic opportunity scoring, and advanced AI frameworks including DeepSeek, MarketLens AI transforms large amounts of market data into clear and actionable business insights.</p>
<h3>Core Capabilities</h3>
<ul>
<li>Real-Time Market Trend Intelligence</li>
<li>AI Consumer Review Analysis</li>
<li>Dynamic Product Opportunity Scoring</li>
<li>Tariff & Logistics Risk Simulation</li>
<li>Interactive 3D Data Visualization</li>
<li>Multi-Language AI Assistant</li>
<li>Competitive Gap Detection</li>
<li>Market Demand Forecasting</li>
<li>Strategic Decision Support</li>
</ul>
</div>
""", unsafe_allow_html=True)

# =====================================================
# PHILOSOPHY
# =====================================================

st.markdown("""
<div class="glass">
<h2>🧠 Philosophy</h2>
<p>I believe technology should not replace human thinking; it should enhance it. My curiosity extends beyond engineering into philosophy, economics, psychology, ethics, and civilization.</p>
<p>I am particularly interested in exploring:<br>• Intelligence vs Wisdom<br>• Technology vs Humanity<br>• Wealth vs Meaning<br>• Power vs Responsibility<br>• Progress vs Purpose</p>
<p>I view learning as a lifelong pursuit and believe that independent thinking remains one of the most valuable abilities a person can develop.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

st.markdown('<div class="glass"><h2>📊 Snapshot</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Focus", "AI & Automation")
with c2:
    st.metric("Mission", "Global Impact")
with c3:
    st.metric("Vision", "Entrepreneur")
st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# CONTACT
# =====================================================

st.markdown("""
<div class="glass">
<h2>📬 Contact</h2>
📧 abdullahbinfahad.abf@gmail.com<br>
🎓 Nanjing Tech University<br>
🌏 China
</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
© 2026 Abdullah Bin Fahad<br>
<a href="https://www.abdullahbinfahad.info" style="color: #888;">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
