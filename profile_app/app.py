import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Abdullah Bin Fahad",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# PREMIUM DARK THEME – CINEMATIC & MINIMAL
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
    scroll-behavior: smooth;
}

/* Background (handled by Three.js) */
.stApp {
    background: #000000;
}

/* Custom cursor glow */
.cursor-glow {
    position: fixed;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(100,100,255,0.15) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    transform: translate(-50%, -50%);
    mix-blend-mode: screen;
    transition: opacity 0.2s;
}
.cursor-glow.hidden {
    opacity: 0;
}

/* Scroll reveal */
.reveal {
    opacity: 0;
    transform: translateY(60px);
    transition: all 0.9s cubic-bezier(0.22, 1, 0.36, 1);
}
.reveal.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Fullscreen hero */
.hero-fullscreen {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    z-index: 2;
}

.hero-title-large {
    font-size: clamp(5rem, 15vw, 10rem);
    font-weight: 900;
    line-height: 1;
    background: linear-gradient(135deg, #ffffff 0%, #c0c0c0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    animation: floatTitle 6s ease-in-out infinite;
    margin-bottom: 10px;
    letter-spacing: -0.02em;
}

@keyframes floatTitle {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

.role-text {
    text-align: center;
    font-size: clamp(1rem, 3.5vw, 1.5rem);
    font-weight: 500;
    color: #aaa;
    letter-spacing: 2px;
    min-height: 2rem;
}

.hero-statement {
    text-align: center;
    font-size: clamp(1.2rem, 4vw, 2rem);
    font-weight: 600;
    color: #ddd;
    max-width: 800px;
    margin: 30px auto;
}

.cta-button {
    display: inline-block;
    padding: 16px 40px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 50px;
    color: #fff;
    font-size: 1rem;
    font-weight: 500;
    letter-spacing: 1px;
    transition: all 0.4s;
    backdrop-filter: blur(10px);
    text-decoration: none;
    cursor: pointer;
}
.cta-button:hover {
    background: rgba(255,255,255,0.15);
    border-color: rgba(255,255,255,0.4);
    transform: translateY(-3px);
    box-shadow: 0 0 30px rgba(255,255,255,0.15);
}

/* Glass card – subtle interaction */
.glass-card {
    background: rgba(18, 18, 18, 0.7);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 32px;
    padding: 50px;
    margin: 40px 0;
    box-shadow: 0 20px 60px rgba(0,0,0,0.9);
    transition: all 0.3s ease;
}
.glass-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255,255,255,0.15);
}

/* Statistics counter cards */
.stat-card {
    text-align: center;
    padding: 30px 20px;
}
.stat-number {
    font-size: clamp(2.5rem, 8vw, 4rem);
    font-weight: 800;
    background: linear-gradient(135deg, #fff, #999);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label {
    color: #aaa;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    margin-top: 8px;
    font-weight: 500;
}

/* Timeline */
.timeline {
    position: relative;
    margin: 50px 0;
    padding-left: 50px;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 25px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.3), transparent);
}
.timeline-item {
    position: relative;
    margin-bottom: 40px;
}
.timeline-dot {
    position: absolute;
    left: -37px;
    top: 5px;
    width: 24px;
    height: 24px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 20px rgba(255,255,255,0.4);
}
.timeline-content {
    color: #ccc;
    font-size: 1.2rem;
    font-weight: 500;
}

/* Full screen philosophy card */
.phi-card {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    opacity: 0;
    transform: scale(0.92);
    transition: all 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    will-change: opacity, transform;
    scroll-snap-align: start;
}
.phi-card.visible {
    opacity: 1;
    transform: scale(1);
}
.phi-quote {
    font-size: clamp(2rem, 8vw, 4.5rem);
    font-weight: 800;
    text-align: center;
    line-height: 1.2;
    background: linear-gradient(135deg, #ffffff 0%, #aaaaaa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    max-width: 900px;
}

/* Principles grid */
.principle-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 25px;
}
.principle-tile {
    background: rgba(20, 20, 20, 0.6);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 24px;
    padding: 30px 20px;
    text-align: center;
    transition: all 0.3s ease;
}
.principle-tile:hover {
    transform: translateY(-8px);
    background: rgba(30,30,30,0.8);
    border-color: rgba(255,255,255,0.2);
    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
}
.principle-icon {
    font-size: 2.2rem;
    margin-bottom: 15px;
    filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));
}

/* Circular progress */
.circular-progress {
    display: inline-block;
    position: relative;
    width: 100px;
    height: 100px;
}
.circular-progress svg {
    transform: rotate(-90deg);
}
.circle-bg {
    fill: none;
    stroke: #222;
    stroke-width: 8;
}
.circle-fill {
    fill: none;
    stroke: url(#gradient);
    stroke-width: 8;
    stroke-linecap: round;
    transition: stroke-dashoffset 1.5s ease;
}

/* Project device mockup */
.device-3d {
    width: 100%;
    height: 400px;
    position: relative;
    border-radius: 20px;
    overflow: hidden;
}

/* Contact cards */
.contact-card {
    background: rgba(20,20,20,0.6);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    transition: 0.3s;
    color: #ddd;
}
.contact-card:hover {
    background: rgba(40,40,40,0.8);
    transform: translateY(-5px);
    border-color: rgba(255,255,255,0.2);
}
.contact-icon {
    font-size: 2rem;
    margin-bottom: 15px;
}

/* Footer gradient */
.gradient-footer {
    text-align: center;
    padding: 60px 20px;
    background: linear-gradient(180deg, transparent 0%, rgba(10,10,10,0.9) 80%);
    color: #666;
    font-size: 0.9rem;
}
.gradient-footer span {
    background: linear-gradient(135deg, #ffffff, #777);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# CUSTOM CURSOR GLOW (JS)
# =====================================================

components.html("""
<div class="cursor-glow" id="cursorGlow"></div>
<script>
const glow = document.getElementById('cursorGlow');
document.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
    glow.classList.remove('hidden');
});
document.addEventListener('mouseout', () => { glow.classList.add('hidden'); });
</script>
""", height=0)

# =====================================================
# 3D BACKGROUND – NEURAL NETWORK / PARTICLES
# =====================================================

components.html("""
<div id="bg-canvas" style="position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const container = document.getElementById('bg-canvas');
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000000, 0.0003);

const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 50;

const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
container.appendChild(renderer.domElement);

// Particles (stars / nodes)
const particlesGeo = new THREE.BufferGeometry();
const particlesCount = 1200;
const posArray = new Float32Array(particlesCount * 3);
for (let i = 0; i < particlesCount * 3; i += 3) {
    posArray[i] = (Math.random() - 0.5) * 120;
    posArray[i+1] = (Math.random() - 0.5) * 60;
    posArray[i+2] = (Math.random() - 0.5) * 60 - 20;
}
particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
const particlesMat = new THREE.PointsMaterial({
    size: 0.15,
    color: 0xffffff,
    transparent: true,
    blending: THREE.AdditiveBlending,
    opacity: 0.7,
});
const particles = new THREE.Points(particlesGeo, particlesMat);
scene.add(particles);

// Neural network lines (connect close nodes)
const linesMaterial = new THREE.LineBasicMaterial({ color: 0x5555ff, transparent: true, opacity: 0.15 });
const maxDist = 15;
const positions = particlesGeo.attributes.position.array;
const lineVertices = [];
for (let i = 0; i < particlesCount; i++) {
    const x1 = positions[i*3], y1 = positions[i*3+1], z1 = positions[i*3+2];
    for (let j = i+1; j < particlesCount; j++) {
        const x2 = positions[j*3], y2 = positions[j*3+1], z2 = positions[j*3+2];
        const dist = Math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2);
        if (dist < maxDist) {
            lineVertices.push(x1, y1, z1);
            lineVertices.push(x2, y2, z2);
        }
    }
}
const linesGeo = new THREE.BufferGeometry();
linesGeo.setAttribute('position', new THREE.Float32BufferAttribute(lineVertices, 3));
const lines = new THREE.LineSegments(linesGeo, linesMaterial);
scene.add(lines);

// Light beams / aurora (simple moving planes)
const auroraGeo = new THREE.PlaneGeometry(100, 30);
const auroraMat = new THREE.ShaderMaterial({
    uniforms: {
        time: { value: 0 },
        color: { value: new THREE.Color(0x3344aa) }
    },
    vertexShader: `
        varying vec2 vUv;
        void main() {
            vUv = uv;
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
    `,
    fragmentShader: `
        varying vec2 vUv;
        uniform float time;
        uniform vec3 color;
        void main() {
            float alpha = sin(vUv.x * 10.0 + time) * 0.2 + 0.1;
            gl_FragColor = vec4(color, alpha);
        }
    `,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false
});
const aurora = new THREE.Mesh(auroraGeo, auroraMat);
aurora.position.set(0, -20, -30);
scene.add(aurora);

const aurora2 = new THREE.Mesh(auroraGeo, auroraMat.clone());
aurora2.material.uniforms.color.value = new THREE.Color(0x6655aa);
aurora2.position.set(0, 30, -35);
scene.add(aurora2);

// Animation
const clock = new THREE.Clock();
function animate() {
    requestAnimationFrame(animate);
    const t = clock.getElapsedTime();
    particles.rotation.y += 0.0001;
    lines.rotation.y = particles.rotation.y;
    aurora.material.uniforms.time.value = t * 0.5;
    aurora2.material.uniforms.time.value = t * 0.8;
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
# SCROLL REVEAL SCRIPT
# =====================================================

components.html("""
<script>
(function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });
    const revealElements = document.querySelectorAll('.reveal, .phi-card');
    revealElements.forEach(el => observer.observe(el));
    // Re-observe after Streamlit rerenders
    const mutationObserver = new MutationObserver(() => {
        document.querySelectorAll('.reveal:not(.visible), .phi-card:not(.visible)').forEach(el => observer.observe(el));
    });
    mutationObserver.observe(document.body, { childList: true, subtree: true });
})();
</script>
""", height=0)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-fullscreen reveal">
    <div class="hero-title-large">ABDULLAH<br>BIN FAHAD</div>
    <div class="role-text" id="rotating-roles"></div>
    <div class="hero-statement">Building technologies that expand human potential.</div>
    <a href="#journey" class="cta-button">Explore My Journey →</a>
</div>
""", unsafe_allow_html=True)

# Rotating roles
components.html("""
<script>
const roles = [
    "Automation Engineer",
    "AI Entrepreneur",
    "Independent Thinker",
    "Technology Philosopher",
    "Future Visionary"
];
let idx = 0;
const el = document.getElementById('rotating-roles');
setInterval(() => {
    el.textContent = roles[idx];
    idx = (idx + 1) % roles.length;
}, 2000);
el.textContent = roles[0];
</script>
""", height=0)

# Anchor
st.markdown('<div id="journey"></div>', unsafe_allow_html=True)

# =====================================================
# STATISTICS (animated counters)
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card" style="display:flex; flex-wrap:wrap; justify-content:space-around;">', unsafe_allow_html=True)
stats = [
    ("6+", "Projects"),
    ("4+", "Research Areas"),
    ("10+", "Technical Skills"),
    ("4", "Languages"),
    ("100%", "Curiosity")
]
for num, label in stats:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number count-up" data-target="{num}">{num}</div>
        <div class="stat-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Counter animation JS
components.html("""
<script>
function animateCounters() {
    document.querySelectorAll('.count-up').forEach(el => {
        const targetText = el.getAttribute('data-target');
        // if it contains a plus or percent, keep it
        const suffix = targetText.includes('+') ? '+' : (targetText.includes('%') ? '%' : '');
        const targetNum = parseFloat(targetText);
        if (isNaN(targetNum)) return;
        let current = 0;
        const increment = targetNum / 60;
        const timer = setInterval(() => {
            current += increment;
            if (current >= targetNum) {
                el.textContent = targetText;
                clearInterval(timer);
            } else {
                el.textContent = Math.floor(current) + suffix;
            }
        }, 30);
        el.removeAttribute('data-target');
    });
}
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
        }
    });
});
document.querySelectorAll('.stat-card').forEach(el => observer.observe(el));
</script>
""", height=0)

# =====================================================
# ABOUT – TIMELINE
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff;">My Journey</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="timeline">
    <div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">Bangladesh – Early curiosity</div></div>
    <div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">Science Student – SSC & HSC</div></div>
    <div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">Engineering – Automation at NJTech</div></div>
    <div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">AI & Entrepreneurship – MarketLens AI</div></div>
    <div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">Writing & Philosophy – "Moral Values"</div></div>
    <div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content">Building Future Products – Smart Calculator & beyond</div></div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# PHILOSOPHY – FULL SCREEN CARDS
# =====================================================

st.markdown('<div class="reveal"><h2 style="color:#fff; text-align:center; margin:80px 0 40px;">Personal Philosophy</h2>', unsafe_allow_html=True)

quotes = [
    "Technology should empower humanity,<br>not replace it.",
    "Knowledge has little value<br>unless it creates positive change.",
    "Dream boldly.<br>Build patiently.<br>Improve continuously.",
    "Question assumptions.<br>Seek truth.<br>Follow evidence.",
    "Innovation begins where curiosity<br>meets responsibility.",
    "Character is the foundation<br>of every lasting achievement.",
    "Success is built through discipline,<br>consistency, and independent thinking."
]

for q in quotes:
    st.markdown(f"""
    <div class="phi-card" id="phi-{hash(q)}">
        <div class="phi-quote">{q}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# CORE PRINCIPLES – ANIMATED CARDS
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff; text-align:center;">Core Principles</h2>', unsafe_allow_html=True)
principles = [
    ("🧠", "Think Independently", "Question before following."),
    ("⚙️", "Build Value", "Create solutions that matter."),
    ("🌍", "Lead with Purpose", "Integrity above recognition."),
    ("✨", "Stay Curious", "Never stop learning."),
    ("🤝", "Ethical Tech", "Responsibility in every line of code."),
    ("🚀", "Discipline & Action", "Ideas become reality through persistence."),
    ("❤️", "Positive Impact", "Measure success by lives improved.")
]
cols = st.columns(4)
for i, (icon, title, desc) in enumerate(principles):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="principle-tile">
            <div class="principle-icon">{icon}</div>
            <h4 style="margin:10px 0; color:#eee;">{title}</h4>
            <p style="color:#999; font-size:0.9rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# SKILLS – CIRCULAR PROGRESS
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff; text-align:center;">Technical Skills</h2>', unsafe_allow_html=True)
skills = {
    "Python": 95,
    "C/C++": 80,
    "HTML/CSS": 85,
    "Automation": 90,
    "Digital Marketing": 88,
    "Video Editing": 85,
    "Office Suite": 92
}
cols = st.columns(4)
for i, (skill, val) in enumerate(skills.items()):
    with cols[i % 4]:
        # SVG circular progress
        radius = 36
        circumference = 2 * 3.14159 * radius
        offset = circumference - (val / 100) * circumference
        st.markdown(f"""
        <div style="text-align:center; margin:20px 0;">
            <div class="circular-progress">
                <svg width="100" height="100" viewBox="0 0 100 100">
                    <defs>
                        <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#ffffff"/>
                            <stop offset="100%" stop-color="#888888"/>
                        </linearGradient>
                    </defs>
                    <circle class="circle-bg" cx="50" cy="50" r="{radius}"></circle>
                    <circle class="circle-fill" cx="50" cy="50" r="{radius}" 
                        stroke-dasharray="{circumference}" 
                        stroke-dashoffset="{circumference}" 
                        data-offset="{offset}"></circle>
                </svg>
                <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-weight:700; color:#fff; font-size:1.1rem;">{val}%</div>
            </div>
            <div style="color:#ccc; margin-top:10px; font-weight:500;">{skill}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# Animate circles on scroll
components.html("""
<script>
function animateCircles() {
    document.querySelectorAll('.circle-fill').forEach(circle => {
        const offset = circle.getAttribute('data-offset');
        circle.style.strokeDashoffset = offset;
        circle.removeAttribute('data-offset');
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

# =====================================================
# PROJECTS – 3D PRODUCT PAGES
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff;">MarketLens AI</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    # 3D mockup placeholder
    components.html("""
    <div style="width:100%; height:350px;" id="marketlens-3d"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    const container = document.getElementById('marketlens-3d');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 100);
    camera.position.z = 7;
    const renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(1,1,1);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0x444444));
    // Laptop mockup
    const base = new THREE.BoxGeometry(4, 0.15, 2.5);
    const baseMat = new THREE.MeshStandardMaterial({color: 0x333333, roughness:0.4, metalness:0.8});
    const baseMesh = new THREE.Mesh(base, baseMat);
    baseMesh.position.y = -1;
    scene.add(baseMesh);
    const screen = new THREE.BoxGeometry(3.8, 2.6, 0.1);
    const screenMat = new THREE.MeshStandardMaterial({color: 0x222233, emissive: new THREE.Color(0x111133), roughness:0.2});
    const screenMesh = new THREE.Mesh(screen, screenMat);
    screenMesh.position.set(0, 0.5, -1.4);
    screenMesh.rotation.x = -0.4;
    scene.add(screenMesh);
    function animate() {
        requestAnimationFrame(animate);
        screenMesh.rotation.y += 0.005;
        baseMesh.rotation.y = screenMesh.rotation.y;
        renderer.render(scene, camera);
    }
    animate();
    window.addEventListener('resize', () => {renderer.setSize(container.clientWidth, container.clientHeight); camera.aspect = container.clientWidth/container.clientHeight; camera.updateProjectionMatrix();});
    </script>
    """, height=350)
with col2:
    st.markdown("""
    <p style="color:#ccc; font-size:1.1rem;">An intelligent decision‑making agent for Silk Road cross‑border e‑commerce, answering <b>Which products will perform best?</b> with real‑time data, consumer reviews, and tariff risk analysis.</p>
    <ul style="color:#bbb;">
        <li>Real‑Time Market Intelligence</li>
        <li>AI Consumer Review Analysis</li>
        <li>Tariff & Logistics Simulation</li>
        <li>Multi‑Language AI Assistant</li>
    </ul>
    <a href="https://www.marketlens-ai.com" target="_blank" class="cta-button" style="display:inline-block; margin-top:20px;">Visit Project →</a>
    """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Smart Calculator
st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff;">Smart Calculator</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    components.html("""
    <div style="width:100%; height:350px;" id="calc-3d"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    const container2 = document.getElementById('calc-3d');
    const scene2 = new THREE.Scene();
    const camera2 = new THREE.PerspectiveCamera(45, container2.clientWidth/container2.clientHeight, 0.1, 100);
    camera2.position.z = 6;
    const renderer2 = new THREE.WebGLRenderer({alpha: true, antialias: true});
    renderer2.setSize(container2.clientWidth, container2.clientHeight);
    container2.appendChild(renderer2.domElement);
    scene2.add(new THREE.AmbientLight(0x444444));
    const dirLight2 = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight2.position.set(1,1,1);
    scene2.add(dirLight2);
    // Calculator body
    const body = new THREE.BoxGeometry(2.5, 3.5, 0.5);
    const bodyMat = new THREE.MeshStandardMaterial({color: 0x1a1a1a, roughness:0.3, metalness:0.9});
    const calcBody = new THREE.Mesh(body, bodyMat);
    scene2.add(calcBody);
    // Screen
    const screenG = new THREE.PlaneGeometry(2, 0.7);
    const screenM = new THREE.MeshBasicMaterial({color: 0x3366ff, transparent:true, opacity:0.8});
    const calcScreen = new THREE.Mesh(screenG, screenM);
    calcScreen.position.set(0, 0.8, 0.26);
    scene2.add(calcScreen);
    function animate2() {
        requestAnimationFrame(animate2);
        calcBody.rotation.y += 0.01;
        calcScreen.rotation.y = calcBody.rotation.y;
        renderer2.render(scene2, camera2);
    }
    animate2();
    window.addEventListener('resize', () => {renderer2.setSize(container2.clientWidth, container2.clientHeight); camera2.aspect = container2.clientWidth/container2.clientHeight; camera2.updateProjectionMatrix();});
    </script>
    """, height=350)
with col2:
    st.markdown("""
    <p style="color:#ccc;">A next‑gen educational device for low‑connectivity areas.</p>
    <ul style="color:#bbb;">
        <li>AI homework assistant</li>
        <li>Offline mesh networking</li>
        <li>10+ language learning tools</li>
        <li>GPS tracking & smart dictionary</li>
    </ul>
    <div class="cta-button" style="margin-top:20px;">Coming Soon</div>
    """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# THE PHILOSOPHER SECTIONS
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff;">The Engineer • The Thinker • The Builder</h2>', unsafe_allow_html=True)
st.markdown("""
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:30px; color:#ccc; margin-top:30px;">
    <div>
        <h3 style="color:#fff;">🔧 The Engineer</h3>
        <p>Automation Engineering student at Nanjing Tech University, bridging engineering, AI, philosophy, and entrepreneurship — technology as a tool for human capability.</p>
    </div>
    <div>
        <h3 style="color:#fff;">🧠 The Thinker</h3>
        <p>Exploring ethics, psychology, education, and the philosophy of progress. Innovation strengthens human creativity, critical thinking, and responsibility.</p>
    </div>
    <div>
        <h3 style="color:#fff;">⚡ The Builder</h3>
        <p>Developing AI software, embedded systems, and educational tech to create practical, long‑term value for individuals and society.</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# VISION – CINEMATIC (globe)
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card" style="display:flex; flex-direction:row; align-items:center; flex-wrap:wrap;">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    components.html("""
    <div style="width:100%; height:400px;" id="globe-3d"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    const globeContainer = document.getElementById('globe-3d');
    const sceneGlobe = new THREE.Scene();
    const cameraGlobe = new THREE.PerspectiveCamera(45, globeContainer.clientWidth/globeContainer.clientHeight, 0.1, 100);
    cameraGlobe.position.z = 6;
    const rendererGlobe = new THREE.WebGLRenderer({alpha: true});
    rendererGlobe.setSize(globeContainer.clientWidth, globeContainer.clientHeight);
    globeContainer.appendChild(rendererGlobe.domElement);
    sceneGlobe.add(new THREE.AmbientLight(0x444444));
    const lightGlobe = new THREE.DirectionalLight(0xffffff, 0.6);
    lightGlobe.position.set(1,1,1);
    sceneGlobe.add(lightGlobe);
    // Wireframe globe
    const globeGeo = new THREE.SphereGeometry(2, 32, 32);
    const globeMat = new THREE.MeshBasicMaterial({color: 0x3377ff, wireframe: true, transparent: true, opacity: 0.4});
    const globe = new THREE.Mesh(globeGeo, globeMat);
    sceneGlobe.add(globe);
    // Particles around
    const particlesGeoGlobe = new THREE.BufferGeometry();
    const pCount = 200;
    const pPositions = new Float32Array(pCount * 3);
    for(let i=0; i<pCount*3; i+=3){
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.acos((Math.random()*2)-1);
        const r = 2.3;
        pPositions[i] = Math.cos(theta) * Math.sin(phi) * r;
        pPositions[i+1] = Math.sin(theta) * Math.sin(phi) * r;
        pPositions[i+2] = Math.cos(phi) * r;
    }
    particlesGeoGlobe.setAttribute('position', new THREE.BufferAttribute(pPositions, 3));
    const pMatGlobe = new THREE.PointsMaterial({color: 0xffffff, size: 0.05, blending: THREE.AdditiveBlending});
    const pSystem = new THREE.Points(particlesGeoGlobe, pMatGlobe);
    sceneGlobe.add(pSystem);
    function animateGlobe(){
        requestAnimationFrame(animateGlobe);
        globe.rotation.y += 0.003;
        pSystem.rotation.y += 0.002;
        rendererGlobe.render(sceneGlobe, cameraGlobe);
    }
    animateGlobe();
    window.addEventListener('resize', () => {rendererGlobe.setSize(globeContainer.clientWidth, globeContainer.clientHeight); cameraGlobe.aspect = globeContainer.clientWidth/globeContainer.clientHeight; cameraGlobe.updateProjectionMatrix();});
    </script>
    """, height=400)
with col2:
    st.markdown("""
    <h2 style="color:#fff;">Vision</h2>
    <p style="color:#ddd; font-size:1.2rem; line-height:1.6;">
        To build technologies that combine <b>Artificial Intelligence, Engineering, and Education</b> to make knowledge more accessible, practical, and meaningful.
    </p>
    <p style="color:#bbb; margin-top:20px;">🌍 Create. Inspire. Empower. Repeat.</p>
    """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# CONTACT CARDS
# =====================================================

st.markdown('<div class="reveal"><div class="glass-card"><h2 style="color:#fff; text-align:center;">Contact</h2>', unsafe_allow_html=True)
cols = st.columns(4)
contacts = [
    ("📧", "Email", "abdullahbinfahad.abf@gmail.com"),
    ("💻", "GitHub", "github.com/abdullahbinfahad"),
    ("📍", "Location", "Nanjing, China"),
    ("📱", "Phone", "+86 18105180247")
]
for col, (icon, label, value) in zip(cols, contacts):
    with col:
        st.markdown(f"""
        <div class="contact-card">
            <div class="contact-icon">{icon}</div>
            <h4 style="color:#fff;">{label}</h4>
            <p style="color:#aaa;">{value}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="gradient-footer reveal">
    <span>Designed & Engineered by Abdullah Bin Fahad</span><br>
    <span>Building Tomorrow. One Idea at a Time.</span><br>
    <a href="https://www.abdullahbinfahad.info" style="color:#888;">www.abdullahbinfahad.info</a>
</div>
""", unsafe_allow_html=True)
