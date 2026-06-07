import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Abdullah Bin Fahad",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# ADVANCED CSS + MODERN SHAPES + RESPONSIVE GLASSMORPHISM
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
    cursor: none;  /* hide default cursor for custom */
}

/* custom cursor */
.cursor {
    width: 30px;
    height: 30px;
    border: 2px solid rgba(255,255,255,0.8);
    border-radius: 50%;
    position: fixed;
    pointer-events: none;
    z-index: 9999;
    mix-blend-mode: difference;
    transition: transform 0.2s ease, background 0.2s ease;
    transform: translate(-50%, -50%);
}
.cursor-dot {
    width: 8px;
    height: 8px;
    background: #fff;
    border-radius: 50%;
    position: fixed;
    pointer-events: none;
    z-index: 10000;
    transform: translate(-50%, -50%);
    transition: opacity 0.2s;
}

/* animated background gradient */
.stApp {
    background: linear-gradient(-45deg, #020617, #0f172a, #0f766e, #312e81, #111827);
    background-size: 500% 500%;
    animation: gradientBG 25s ease infinite;
}

@keyframes gradientBG {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* diagonal section dividers (modern shapes) */
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
    fill: rgba(255,255,255,0.03);
}

/* modern glass card with 3d hover and border glow */
.glass {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 30px;
    padding: 35px;
    margin: 25px 0;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(255,255,255,0.05);
    transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    position: relative;
    overflow: hidden;
    transform-style: preserve-3d;
}
.glass:hover {
    transform: translateY(-10px) scale(1.02) rotateX(2deg);
    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 20px 50px rgba(0,0,0,0.6), 0 0 30px rgba(255,255,255,0.2);
}
.glass::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.8s;
}
.glass:hover::before {
    left: 100%;
}

/* title & subtitle with text shadow animation */
.title {
    text-align: center;
    font-size: clamp(3rem, 10vw, 5rem);
    font-weight: 800;
    color: white;
    text-shadow: 0 0 20px rgba(255,255,255,0.3);
    animation: floatText 3s ease-in-out infinite;
}
@keyframes floatText {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}
.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: clamp(1rem, 4vw, 1.4rem);
    margin-bottom: 25px;
    letter-spacing: 1px;
}
.quote {
    text-align: center;
    color: #f8fafc;
    font-size: clamp(1.1rem, 5vw, 1.6rem);
    font-style: italic;
    opacity: 0.9;
}

/* glowing progress bars */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #0f766e, #6d28d9) !important;
    border-radius: 20px;
    box-shadow: 0 0 15px #0f766e;
}

/* buttons and links */
a, button {
    cursor: none;
}

/* responsive adjustments */
@media (max-width: 768px) {
    .glass {
        padding: 20px;
        border-radius: 20px;
    }
    .title {
        font-size: 2.8rem;
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
# 3D BACKGROUND + MOUSE PARALLAX + CUSTOM CURSOR (Three.js)
# =====================================================

components.html("""
<!-- Three.js canvas for 3D floating shapes -->
<div id="three-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -2; pointer-events: none;"></div>

<!-- Custom cursor elements -->
<div class="cursor"></div>
<div class="cursor-dot"></div>

<!-- Particles.js background -->
<div id="particles-js" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js"></script>

<script>
// ---- CUSTOM CURSOR ----
const cursor = document.querySelector('.cursor');
const cursorDot = document.querySelector('.cursor-dot');
document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
    cursorDot.style.left = e.clientX + 'px';
    cursorDot.style.top = e.clientY + 'px';
});
// enlarge cursor on hover over interactive elements
document.querySelectorAll('.glass, a, button, .stProgress, h1, h2, h3').forEach(el => {
    el.addEventListener('mouseenter', () => {
        cursor.style.transform = 'translate(-50%, -50%) scale(1.8)';
        cursor.style.background = 'rgba(255,255,255,0.1)';
        cursorDot.style.opacity = '0.5';
    });
    el.addEventListener('mouseleave', () => {
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
        cursor.style.background = 'transparent';
        cursorDot.style.opacity = '1';
    });
});

// ---- PARTICLES.JS ----
particlesJS("particles-js", {
    particles: {
        number: { value: 100, density: { enable: true, value_area: 800 } },
        color: { value: "#ffffff" },
        shape: { type: "circle" },
        opacity: { value: 0.15, random: true },
        size: { value: 3, random: true },
        line_linked: { enable: true, distance: 150, color: "#ffffff", opacity: 0.1, width: 1 },
        move: { enable: true, speed: 1.5, direction: "none", random: true, out_mode: "out" }
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: { enable: true, mode: "grab" },
            onclick: { enable: true, mode: "push" },
            resize: true
        },
        modes: {
            grab: { distance: 140, line_linked: { opacity: 0.3 } },
            push: { particles_nb: 3 }
        }
    },
    retina_detect: true
});

// ---- THREE.JS 3D FLOATING SHAPES WITH MOUSE PARALLAX ----
const container = document.getElementById('three-container');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 15;

const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
container.appendChild(renderer.domElement);

// Lighting
const ambientLight = new THREE.AmbientLight(0x404066);
scene.add(ambientLight);
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(1, 1, 1);
scene.add(directionalLight);

// Create various geometric shapes
const shapes = [];
const geometryTypes = [
    new THREE.IcosahedronGeometry(0.8, 0),
    new THREE.OctahedronGeometry(0.7, 0),
    new THREE.TetrahedronGeometry(0.6, 0),
    new THREE.TorusKnotGeometry(0.5, 0.15, 64, 8),
    new THREE.DodecahedronGeometry(0.7, 0)
];

for (let i = 0; i < 30; i++) {
    const geo = geometryTypes[Math.floor(Math.random() * geometryTypes.length)];
    const material = new THREE.MeshStandardMaterial({
        color: new THREE.Color(`hsl(${Math.random() * 60 + 180}, 70%, 65%)`),
        roughness: 0.2,
        metalness: 0.5,
        emissive: new THREE.Color(0x0f172a),
        emissiveIntensity: 0.2,
        transparent: true,
        opacity: 0.25
    });
    const mesh = new THREE.Mesh(geo, material);
    mesh.position.x = (Math.random() - 0.5) * 18;
    mesh.position.y = (Math.random() - 0.5) * 10;
    mesh.position.z = (Math.random() - 0.5) * 8 - 2;
    mesh.rotation.x = Math.random() * Math.PI;
    mesh.rotation.y = Math.random() * Math.PI;
    mesh.userData = {
        speedX: (Math.random() - 0.5) * 0.008,
        speedY: (Math.random() - 0.5) * 0.008,
        speedZ: (Math.random() - 0.5) * 0.008,
        rotX: (Math.random() - 0.5) * 0.01,
        rotY: (Math.random() - 0.5) * 0.01
    };
    scene.add(mesh);
    shapes.push(mesh);
}

// Mouse parallax variables
let mouseX = 0, mouseY = 0;
let targetX = 0, targetY = 0;
const windowHalfX = window.innerWidth / 2;
const windowHalfY = window.innerHeight / 2;

document.addEventListener('mousemove', (event) => {
    mouseX = (event.clientX - windowHalfX) / windowHalfX;
    mouseY = (event.clientY - windowHalfY) / windowHalfY;
});

// Animation loop
function animate() {
    requestAnimationFrame(animate);

    // Smooth camera movement based on mouse
    targetX = mouseX * 2;
    targetY = mouseY * 1.5;
    camera.position.x += (targetX - camera.position.x) * 0.05;
    camera.position.y += (-targetY - camera.position.y) * 0.05;
    camera.lookAt(scene.position);

    // Rotate and move shapes
    shapes.forEach(mesh => {
        mesh.rotation.x += mesh.userData.rotX;
        mesh.rotation.y += mesh.userData.rotY;
        mesh.position.x += mesh.userData.speedX;
        mesh.position.y += mesh.userData.speedY;
        mesh.position.z += mesh.userData.speedZ;

        // Boundary wrap
        if (Math.abs(mesh.position.x) > 12) mesh.userData.speedX *= -1;
        if (Math.abs(mesh.position.y) > 8) mesh.userData.speedY *= -1;
        if (Math.abs(mesh.position.z) > 6) mesh.userData.speedZ *= -1;
    });

    renderer.render(scene, camera);
}
animate();

// Handle resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
</script>
""", height=0)

# =====================================================
# HERO SECTION (with wave divider)
# =====================================================

st.markdown("""
<div class="title">Abdullah Bin Fahad</div>
<div class="subtitle">Automation Student • AI Builder • Entrepreneur • Writer • Philosopher</div>
<div class="quote">"I do not seek to predict the future. I seek to build it."</div>
""", unsafe_allow_html=True)

# Wave divider after hero
st.markdown("""
<div class="section-divider">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
    </svg>
</div>
""", unsafe_allow_html=True)

# =====================================================
# ABOUT SECTION (modern glass card)
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
# SKILLS WITH ANIMATED PROGRESS
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
# FEATURED PROJECT (MarketLens AI)
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
<p>I am particularly interested in exploring: <br>• Intelligence vs Wisdom<br>• Technology vs Humanity<br>• Wealth vs Meaning<br>• Power vs Responsibility<br>• Progress vs Purpose</p>
<p>I view learning as a lifelong pursuit and believe that independent thinking remains one of the most valuable abilities a person can develop.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# METRICS (with clean columns)
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
<div style="text-align: center; color: #94a3b8; margin-top: 60px; padding: 30px; font-size: 0.9rem;">
© 2026 Abdullah Bin Fahad<br>
<a href="https://www.abdullahbinfahad.info" style="color: #5eead4; text-decoration: none;">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
