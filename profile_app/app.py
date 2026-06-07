import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Abdullah Bin Fahad",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# ADVANCED CSS + ANIMATED BACKGROUND + GLASSMORPHISM
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    overflow-x:hidden;
}

/* Animated Gradient */
.stApp{
    background: linear-gradient(-45deg,#020617,#0f172a,#0f766e,#312e81,#111827);
    background-size: 500% 500%;
    animation: gradientBG 20s ease infinite;
}

@keyframes gradientBG{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Glass Card */
.glass{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 25px;
    padding: 30px;
    margin-top:20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: all 0.4s ease;
}

.glass:hover{
    transform: translateY(-8px) scale(1.02);
}

.title{
    text-align:center;
    font-size:70px;
    font-weight:800;
    color:white;
}

.subtitle{
    text-align:center;
    color:#d1d5db;
    font-size:22px;
    margin-bottom:20px;
}

.quote{
    text-align:center;
    color:#f8fafc;
    font-size:24px;
    font-style:italic;
}

.footer{
    text-align:center;
    color:#94a3b8;
    margin-top:50px;
    padding:20px;
}

h1,h2,h3,p,li{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# PARTICLES + 3D EFFECTS
# =====================================================

components.html("""
<div id="particles-js"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js"></script>

<script>
particlesJS("particles-js",{
 particles:{
   number:{value:120},
   color:{value:"#ffffff"},
   shape:{type:"circle"},
   opacity:{value:0.25},
   size:{value:3},
   move:{
      enable:true,
      speed:2
   }
 }
});
</script>

<style>
#particles-js{
position:fixed;
width:100%;
height:100%;
top:0;
left:0;
z-index:-1;
}
</style>
""", height=0)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="title">
Abdullah Bin Fahad
</div>

<div class="subtitle">
Automation Student • AI Builder • Entrepreneur • Writer • Philosopher
</div>

<div class="quote">
"I do not seek to predict the future. I seek to build it."
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =====================================================
# ABOUT
# =====================================================

st.markdown("""
<div class="glass">

<h2>🌍 About Me</h2>

I am Abdullah Bin Fahad, an Automation Engineering student at
Nanjing Tech University.

My interests span Artificial Intelligence, Automation,
Entrepreneurship, Technology Innovation, Philosophy,
Business Strategy, Psychology, and Human Behavior.

I am deeply interested in understanding how intelligence,
technology, and decision-making can be combined to create
systems that solve real-world problems at scale.

My long-term vision is to build globally impactful AI products,
technology companies, and intelligent systems that empower
people to make better decisions.

</div>
""", unsafe_allow_html=True)

# =====================================================
# EDUCATION
# =====================================================

st.markdown("""
<div class="glass">

<h2>🎓 Education</h2>

<b>Nanjing Tech University</b><br>

Bachelor of Engineering (Automation)

School of Electrical Engineering and Control Science

China

</div>
""", unsafe_allow_html=True)

# =====================================================
# SKILLS
# =====================================================

st.markdown("""
<div class="glass">
<h2>⚡ Skills</h2>
</div>
""", unsafe_allow_html=True)

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

# =====================================================
# MARKETLENS AI
# =====================================================

st.markdown("""
<div class="glass">

<h2>🚀 Featured Project — MarketLens AI</h2>

<p>

MarketLens AI is an intelligent decision-making agent
built specifically for Silk Road cross-border e-commerce.

It answers one of the most critical questions facing
international sellers:

<b>Which products will perform best in overseas markets?</b>

By combining real-time market intelligence,
consumer review mining, dynamic opportunity scoring,
and advanced AI frameworks including DeepSeek,
MarketLens AI transforms large amounts of market data
into clear and actionable business insights.

Rather than functioning as a traditional analytics platform,
it serves as a strategic co-pilot for global trade,
helping exporters identify profitable opportunities,
understand customer demand,
and make confident data-driven decisions.

</p>

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

<p>

I believe technology should not replace human thinking;
it should enhance it.

My curiosity extends beyond engineering into philosophy,
economics, psychology, ethics, and civilization.

I am particularly interested in exploring:

• Intelligence vs Wisdom

• Technology vs Humanity

• Wealth vs Meaning

• Power vs Responsibility

• Progress vs Purpose

I view learning as a lifelong pursuit and believe that
independent thinking remains one of the most valuable
abilities a person can develop.

My goal is not only to build successful systems,
but also to understand the deeper principles that shape
human decisions, societies, and the future.

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

st.markdown("""
<div class="glass">
<h2>📊 Snapshot</h2>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Focus", "AI & Automation")

with c2:
    st.metric("Mission", "Global Impact")

with c3:
    st.metric("Vision", "Entrepreneur")

# =====================================================
# CONTACT
# =====================================================

st.markdown("""
<div class="glass">

<h2>📬 Contact</h2>

📧 abdullahbinfahad.abf@gmail.com

🎓 Nanjing Tech University

🌏 China

</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

© 2026 Abdullah Bin Fahad
</div>
www.abdullahbinfahad.info

</div>
""", unsafe_allow_html=True)

