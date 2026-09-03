import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO OS (assets/hero-os.svg)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="50%" stop-color="#091428" />
      <stop offset="100%" stop-color="#120726" />
    </linearGradient>

    <linearGradient id="cyber-cyan-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="hero-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Main Cyber Shell Frame -->
  <rect width="850" height="250" rx="16" fill="url(#hero-bg)" stroke="url(#cyber-cyan-purple)" stroke-width="1.8" />

  <!-- Top Accent Laser Strip -->
  <rect x="0" y="0" width="850" height="4" rx="2" fill="url(#cyber-cyan-purple)" filter="url(#hero-glow)" />

  <!-- Window Header OS Bar -->
  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">AI_OPERATING_SYSTEM // KATHYAYINI_KERNEL_V4.0 // ACTIVE</text>
    <text x="800" y="12" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS.STATUS: OPTIMAL &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- LEFT HERO PROFILE DATA -->
  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#hero-glow)" />

    <text x="20" y="38" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="14" font-weight="700">Engineering Intelligence From Data</text>
    
    <text x="20" y="96" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">BMS College of Engineering (BMSCE) &#8226; Bengaluru, India</text>

    <!-- Core Domain Badges -->
    <g transform="translate(20, 118)">
      <rect width="112" height="24" rx="12" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
      <text x="56" y="16" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">ARTIFICIAL INTEL</text>

      <rect x="122" width="125" height="24" rx="12" fill="#161B22" stroke="#34D399" stroke-width="1" />
      <text x="184.5" y="16" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">MACHINE LEARNING</text>

      <rect x="257" width="105" height="24" rx="12" fill="#161B22" stroke="#818CF8" stroke-width="1" />
      <text x="309.5" y="16" fill="#818CF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">DATA SCIENCE</text>

      <rect x="372" width="115" height="24" rx="12" fill="#161B22" stroke="#C084FC" stroke-width="1" />
      <text x="429.5" y="16" fill="#C084FC" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SOFTWARE ENG</text>
    </g>
  </g>

  <!-- RIGHT SIDE: 3D NEURAL COGNITION VISUAL -->
  <g transform="translate(560, 50)">
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#hero-glow)" />

    <!-- Radar Circle -->
    <circle cx="127" cy="88" r="62" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="4 4" />
    <circle cx="127" cy="88" r="60" fill="none" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="0 127 88" to="360 127 88" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- Synapses -->
    <g stroke-width="1" opacity="0.6">
      <line x1="45" y1="45" x2="127" y2="35" stroke="#38BDF8" />
      <line x1="45" y1="88" x2="127" y2="88" stroke="#34D399" />
      <line x1="45" y1="130" x2="127" y2="140" stroke="#818CF8" />
      
      <line x1="127" y1="35" x2="210" y2="88" stroke="#C084FC" />
      <line x1="127" y1="88" x2="210" y2="88" stroke="#00F2FE" />
      <line x1="127" y1="140" x2="210" y2="88" stroke="#34D399" />
    </g>

    <!-- Nodes -->
    <circle cx="45" cy="45" r="4.5" fill="#00F2FE" />
    <circle cx="45" cy="88" r="4.5" fill="#38BDF8" />
    <circle cx="45" cy="130" r="4.5" fill="#818CF8" />

    <circle cx="127" cy="35" r="5" fill="#34D399" filter="url(#hero-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="88" r="6" fill="#00F2FE" filter="url(#hero-glow)">
      <animate attributeName="r" values="5;7.5;5" dur="1.8s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="140" r="5" fill="#C084FC" filter="url(#hero-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2.4s" repeatCount="indefinite" />
    </circle>

    <!-- Output Core -->
    <circle cx="210" cy="88" r="8" fill="#818CF8" filter="url(#hero-glow)">
      <animate attributeName="r" values="7;10;7" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="210" cy="88" r="4" fill="#FFFFFF" />

    <!-- Text Tag -->
    <text x="127.5" y="165" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" text-anchor="middle">AI_PIPELINE: ACTIVE_FIT</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. INTERACTIVE TERMINAL (assets/terminal-ai.svg)
# -------------------------------------------------------------
terminal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="100%" stop-color="#05080E" />
    </linearGradient>

    <linearGradient id="term-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#term-bg)" stroke="url(#term-border)" stroke-width="1.5" />

  <!-- Terminal Top Bar -->
  <g transform="translate(18, 16)">
    <circle cx="8" cy="6" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="6" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="6" r="4.5" fill="#27C93F" />
    <text x="60" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">kathyayini@ai-command-center: ~ (zsh)</text>
    <text x="800" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">&#9889; LATENCY: 12ms | CLOUD_SYNC</text>
  </g>

  <line x1="15" y1="36" x2="835" y2="36" stroke="#1E293B" stroke-width="1" />

  <!-- Terminal Content Lines -->
  <g transform="translate(24, 52)" font-family="'Fira Code', monospace" font-size="11" font-weight="500">
    <!-- whoami -->
    <text x="0" y="16">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">whoami</tspan>
    </text>
    <text x="18" y="34" fill="#34D399" font-weight="700">&#8594; Kathyayini Prabhu [AI &amp; Data Science Engineer @ BMSCE Bengaluru]</text>

    <!-- expertise -->
    <text x="0" y="58">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">expertise</tspan>
    </text>
    <text x="18" y="76" fill="#CBD5E1">
      <tspan fill="#00F2FE">&#9670; Artificial Intelligence</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#34D399">&#9670; Machine Learning</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#818CF8">&#9670; Data Science</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#C084FC">&#9670; Software Engineering</tspan>
    </text>

    <!-- currently_building -->
    <text x="0" y="100">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">currently_building</tspan>
    </text>
    <text x="18" y="118" fill="#CBD5E1">
      <tspan fill="#F59E0B">&#9658; BioWeaver</tspan> <tspan fill="#94A3B8">[Knowledge Graph AI &amp; Gene-Disease Discovery]</tspan>
      &nbsp;&nbsp;&nbsp;
      <tspan fill="#38BDF8">&#9658; AI Maritime Risk</tspan> <tspan fill="#94A3B8">[Logistics Forecasting &amp; Route Risk]</tspan>
    </text>

    <!-- mission -->
    <text x="0" y="142">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">mission</tspan>
    </text>
    <text x="18" y="160" fill="#F8FAFC" font-weight="700">&#10024; "Building intelligent systems that solve real-world problems and drive actionable decisions."</text>

    <!-- Prompt cursor -->
    <text x="0" y="184">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#34D399">echo "Ready to innovate"</tspan>
    </text>
    <rect x="235" y="173" width="7" height="13" fill="#00F2FE">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. ENGINEERING EVOLUTION ROADMAP (assets/roadmap.svg)
# -------------------------------------------------------------
roadmap_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 380" width="850" height="380">
  <defs>
    <linearGradient id="road-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0A0F24" />
    </linearGradient>

    <linearGradient id="road-line" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
  </defs>

  <rect width="850" height="380" rx="14" fill="url(#road-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Title Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">ENGINEERING EVOLUTION // ARCHITECTURAL TIMELINE</text>
    <text x="790" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10" text-anchor="end">CONTINUOUS INNOVATION &#9654;</text>
  </g>

  <line x1="30" y1="46" x2="820" y2="46" stroke="#1E293B" stroke-width="1" />

  <!-- Center Glowing Spine Line -->
  <line x1="425" y1="70" x2="425" y2="340" stroke="url(#road-line)" stroke-width="2.5" stroke-dasharray="6 4" />

  <!-- STAGE 1: SMARTCANE (Left) -->
  <g transform="translate(110, 65)">
    <rect width="280" height="42" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="14" y="20" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="11" font-weight="800">1. SMARTCANE</text>
    <text x="14" y="34" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9">Assistive IoT Navigation for Visually Impaired</text>
  </g>
  <circle cx="425" cy="86" r="6" fill="#00F2FE" />

  <!-- STAGE 2: Smart Attendance (Right) -->
  <g transform="translate(460, 115)">
    <rect width="280" height="42" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="14" y="20" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="11" font-weight="800">2. Smart Attendance &amp; Timetable</text>
    <text x="14" y="34" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9">Automated EdTech Optimization System</text>
  </g>
  <circle cx="425" cy="136" r="6" fill="#34D399" />

  <!-- STAGE 3: RoadWatch BIMSTEC (Left) -->
  <g transform="translate(110, 165)">
    <rect width="280" height="42" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="14" y="20" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="11" font-weight="800">3. RoadWatch BIMSTEC</text>
    <text x="14" y="34" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9">Transportation &amp; Infrastructure Analytics</text>
  </g>
  <circle cx="425" cy="186" r="6" fill="#F59E0B" />

  <!-- STAGE 4: BioWeaver (Right) -->
  <g transform="translate(460, 215)">
    <rect width="280" height="42" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1.2" />
    <text x="14" y="20" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="11" font-weight="800">4. BioWeaver</text>
    <text x="14" y="34" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9">AI Knowledge Graphs &#8226; Gene-Disease Discovery</text>
  </g>
  <circle cx="425" cy="236" r="6.5" fill="#818CF8" />

  <!-- STAGE 5: AI Maritime Risk (Left) -->
  <g transform="translate(110, 265)">
    <rect width="280" height="42" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1.2" />
    <text x="14" y="20" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="11" font-weight="800">5. AI Maritime Risk Intelligence</text>
    <text x="14" y="34" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9">Logistics Intelligence &#8226; Port Risk Forecasting</text>
  </g>
  <circle cx="425" cy="286" r="6.5" fill="#C084FC" />

  <!-- STAGE 6: Future AI Research (Right) -->
  <g transform="translate(460, 315)">
    <rect width="280" height="42" rx="8" fill="#161B22" stroke="#00F2FE" stroke-width="1.5" />
    <text x="14" y="20" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9733; Future AI Research Systems</text>
    <text x="14" y="34" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9">Explainable AI &amp; Autonomous Agent Frameworks</text>
  </g>
  <circle cx="425" cy="336" r="7.5" fill="#00F2FE" />
</svg>'''

# -------------------------------------------------------------
# 4. PROJECT GALAXY (assets/galaxy.svg)
# -------------------------------------------------------------
galaxy_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 300" width="850" height="300">
  <defs>
    <linearGradient id="gal-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040610" />
      <stop offset="100%" stop-color="#0D0721" />
    </linearGradient>
  </defs>

  <rect width="850" height="300" rx="14" fill="url(#gal-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#818CF8" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">PROJECT GALAXY // INTERCONNECTED INTELLIGENCE NODES</text>
    <text x="790" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10" text-anchor="end">GRAPH TOPOLOGY</text>
  </g>
  <line x1="30" y1="46" x2="820" y2="46" stroke="#1E293B" stroke-width="1" />

  <!-- Starfield & Nodes -->
  <g transform="translate(425, 175)">
    <!-- Orbits -->
    <ellipse cx="0" cy="0" rx="360" ry="85" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="3 3" />
    <ellipse cx="0" cy="0" rx="220" ry="55" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="4 4" />

    <!-- Center Core Node -->
    <circle cx="0" cy="0" r="32" fill="#0D1117" stroke="#00F2FE" stroke-width="2" />
    <circle cx="0" cy="0" r="26" fill="#161B22" />
    <text x="0" y="-4" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">KATHYAYINI</text>
    <text x="0" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="8" font-weight="700" text-anchor="middle">AI CORE</text>

    <!-- Synapses -->
    <line x1="0" y1="0" x2="-260" y2="-50" stroke="#38BDF8" stroke-width="1.2" opacity="0.6" />
    <line x1="0" y1="0" x2="-140" y2="45" stroke="#34D399" stroke-width="1.2" opacity="0.6" />
    <line x1="0" y1="0" x2="0" y2="-65" stroke="#818CF8" stroke-width="1.2" opacity="0.6" />
    <line x1="0" y1="0" x2="160" y2="-45" stroke="#C084FC" stroke-width="1.2" opacity="0.6" />
    <line x1="0" y1="0" x2="260" y2="35" stroke="#F59E0B" stroke-width="1.2" opacity="0.6" />
    <line x1="0" y1="0" x2="0" y2="65" stroke="#00F2FE" stroke-width="1.2" opacity="0.6" />

    <!-- Node 1: Computational Biology -->
    <g transform="translate(-260, -50)">
      <rect x="-70" y="-18" width="140" height="36" rx="18" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" />
      <text x="0" y="-2" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">BioWeaver</text>
      <text x="0" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="7" text-anchor="middle">Computational Bio</text>
    </g>

    <!-- Node 2: Logistics Intelligence -->
    <g transform="translate(160, -45)">
      <rect x="-75" y="-18" width="150" height="36" rx="18" fill="#0D1117" stroke="#C084FC" stroke-width="1.2" />
      <text x="0" y="-2" fill="#C084FC" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">AI Maritime Risk</text>
      <text x="0" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="7" text-anchor="middle">Logistics Intel</text>
    </g>

    <!-- Node 3: Transportation Analytics -->
    <g transform="translate(-140, 45)">
      <rect x="-70" y="-18" width="140" height="36" rx="18" fill="#0D1117" stroke="#34D399" stroke-width="1.2" />
      <text x="0" y="-2" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">RoadWatch</text>
      <text x="0" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="7" text-anchor="middle">Traffic Analytics</text>
    </g>

    <!-- Node 4: Assistive Tech -->
    <g transform="translate(260, 35)">
      <rect x="-65" y="-18" width="130" height="36" rx="18" fill="#0D1117" stroke="#F59E0B" stroke-width="1.2" />
      <text x="0" y="-2" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SMARTCANE</text>
      <text x="0" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="7" text-anchor="middle">Assistive IoT</text>
    </g>

    <!-- Node 5: EdTech Automation -->
    <g transform="translate(0, -65)">
      <rect x="-75" y="-16" width="150" height="32" rx="16" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="0" y="4" fill="#818CF8" font-family="'Fira Code', monospace" font-size="8" font-weight="800" text-anchor="middle">Smart Attendance &amp; TT</text>
    </g>

    <!-- Node 6: Future AI Systems -->
    <g transform="translate(0, 65)">
      <rect x="-75" y="-16" width="150" height="32" rx="16" fill="#0D1117" stroke="#00F2FE" stroke-width="1.2" />
      <text x="0" y="4" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="8" font-weight="800" text-anchor="middle">&#10024; Future AI Research</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. AI COMMAND CENTER (assets/command-center.svg)
# -------------------------------------------------------------
command_center_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="850" height="280">
  <defs>
    <linearGradient id="cmd-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0B1021" />
    </linearGradient>
  </defs>

  <rect width="850" height="280" rx="14" fill="url(#cmd-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">AI COMMAND CENTER // TECHNICAL CAPABILITY TELEMETRY</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">STACK READY &#9679;</text>
  </g>
  <line x1="30" y1="46" x2="820" y2="46" stroke="#1E293B" stroke-width="1" />

  <!-- 5 TELEMETRY COLUMNS -->
  
  <!-- Column 1: Core Languages -->
  <g transform="translate(30, 60)">
    <rect width="144" height="200" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="14" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="10" font-weight="800">01 // LANGUAGES</text>
    <line x1="14" y1="32" x2="130" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(14, 52)" font-family="'Fira Code', monospace" font-size="10" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#34D399">&#9654;</tspan> Python</text>
      <text x="0" y="30"><tspan fill="#34D399">&#9654;</tspan> SQL</text>
      <text x="0" y="60"><tspan fill="#34D399">&#9654;</tspan> C</text>
    </g>
  </g>

  <!-- Column 2: AI & ML Stack -->
  <g transform="translate(190, 60)">
    <rect width="168" height="200" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="14" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="800">02 // AI &amp; ML STACK</text>
    <line x1="14" y1="32" x2="154" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(14, 52)" font-family="'Fira Code', monospace" font-size="10" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9670;</tspan> Machine Learning</text>
      <text x="0" y="26"><tspan fill="#00F2FE">&#9670;</tspan> Data Science</text>
      <text x="0" y="52"><tspan fill="#00F2FE">&#9670;</tspan> Scikit-Learn</text>
      <text x="0" y="78"><tspan fill="#00F2FE">&#9670;</tspan> Pandas &amp; NumPy</text>
      <text x="0" y="104"><tspan fill="#00F2FE">&#9670;</tspan> Predictive Models</text>
    </g>
  </g>

  <!-- Column 3: Full-Stack & Dev -->
  <g transform="translate(374, 60)">
    <rect width="154" height="200" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="14" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="10" font-weight="800">03 // DEV ENGINE</text>
    <line x1="14" y1="32" x2="140" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(14, 52)" font-family="'Fira Code', monospace" font-size="10" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> React</text>
      <text x="0" y="28"><tspan fill="#818CF8">&#9658;</tspan> Flask</text>
      <text x="0" y="56"><tspan fill="#818CF8">&#9658;</tspan> Git</text>
      <text x="0" y="84"><tspan fill="#818CF8">&#9658;</tspan> GitHub</text>
      <text x="0" y="112"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
    </g>
  </g>

  <!-- Column 4: Database Systems -->
  <g transform="translate(544, 60)">
    <rect width="134" height="200" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="14" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="10" font-weight="800">04 // DATABASE</text>
    <line x1="14" y1="32" x2="120" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(14, 52)" font-family="'Fira Code', monospace" font-size="10" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9679;</tspan> MySQL</text>
      <text x="0" y="28"><tspan fill="#F59E0B">&#9679;</tspan> Relational SQL</text>
      <text x="0" y="56"><tspan fill="#F59E0B">&#9679;</tspan> Schema Design</text>
      <text x="0" y="84"><tspan fill="#F59E0B">&#9679;</tspan> Query Tuning</text>
    </g>
  </g>

  <!-- Column 5: Currently Exploring -->
  <g transform="translate(694, 60)">
    <rect width="126" height="200" rx="10" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
    <text x="10" y="24" fill="#C084FC" font-family="'Fira Code', monospace" font-size="9" font-weight="800">05 // EXPLORING</text>
    <line x1="10" y1="32" x2="116" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(10, 52)" font-family="'Fira Code', monospace" font-size="10" fill="#CBD5E1">
      <text x="0" y="0"><tspan fill="#C084FC">&#9733;</tspan> Docker</text>
      <text x="0" y="28"><tspan fill="#C084FC">&#9733;</tspan> FastAPI</text>
      <text x="0" y="56"><tspan fill="#C084FC">&#9733;</tspan> MLOps</text>
      <text x="0" y="84"><tspan fill="#C084FC">&#9733;</tspan> LLM Agents</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. ENGINEERING MILESTONES (assets/milestones.svg)
# -------------------------------------------------------------
milestones_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 180" width="850" height="180">
  <defs>
    <linearGradient id="mile-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#091024" />
    </linearGradient>
  </defs>

  <rect width="850" height="180" rx="14" fill="url(#mile-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">ENGINEERING MILESTONES // PROVEN EXECUTION</text>
    <text x="790" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10" text-anchor="end">VERIFIED BUILD LOGS</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 3 Impact Cards -->
  <g transform="translate(30, 58)">
    <!-- Card 1 -->
    <rect width="250" height="102" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="14" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; BioWeaver Platform</text>
    <text x="14" y="44" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5">Engineered Knowledge Graph</text>
    <text x="14" y="60" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5">for Gene-Disease Hypothesis</text>
    <text x="14" y="84" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">STATUS: ACTIVE RESEARCH</text>

    <!-- Card 2 -->
    <g transform="translate(268, 0)">
      <rect width="250" height="102" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="14" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; Maritime Risk Engine</text>
      <text x="14" y="44" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5">Developed AI Logistics</text>
      <text x="14" y="60" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5">&amp; Route Forecasting Models</text>
      <text x="14" y="84" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">STATUS: CORE DEPLOYED</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(536, 0)">
      <rect width="254" height="102" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="14" y="24" fill="#C084FC" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; Assistive SMARTCANE</text>
      <text x="14" y="44" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5">Built intelligent sensing</text>
      <text x="14" y="60" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5">&amp; navigation guidance hardware</text>
      <text x="14" y="84" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">STATUS: PROTOTYPE COMPLETE</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 7. MISSION CONTROL FOOTER (assets/footer-hud.svg)
# -------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 160" width="850" height="160">
  <defs>
    <linearGradient id="foot-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0D0721" />
    </linearGradient>

    <linearGradient id="foot-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="160" rx="14" fill="url(#foot-bg)" stroke="url(#foot-border)" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">MISSION CONTROL // SYSTEM STATUS HUD</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">&#9679; ALL SYSTEMS OPERATIONAL</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Telemetry Grid -->
  <g transform="translate(30, 62)" font-family="'Fira Code', monospace" font-size="10.5">
    <!-- Box 1 -->
    <rect width="185" height="74" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="0.8" />
    <text x="12" y="22" fill="#94A3B8">CURRENT OBJECTIVE</text>
    <text x="12" y="44" fill="#38BDF8" font-weight="700">Build Impactful</text>
    <text x="12" y="60" fill="#38BDF8" font-weight="700">AI Systems</text>

    <!-- Box 2 -->
    <g transform="translate(198, 0)">
      <rect width="185" height="74" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="0.8" />
      <text x="12" y="22" fill="#94A3B8">DOMAIN &amp; FOCUS</text>
      <text x="12" y="44" fill="#34D399" font-weight="700">Artificial Intelligence</text>
      <text x="12" y="60" fill="#CBD5E1">ML &amp; Research</text>
    </g>

    <!-- Box 3 -->
    <g transform="translate(396, 0)">
      <rect width="185" height="74" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="0.8" />
      <text x="12" y="22" fill="#94A3B8">BASE LOCATION</text>
      <text x="12" y="44" fill="#818CF8" font-weight="700">Bengaluru, India</text>
      <text x="12" y="60" fill="#CBD5E1">BMSCE Campus</text>
    </g>

    <!-- Box 4 -->
    <g transform="translate(594, 0)">
      <rect width="196" height="74" rx="6" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="12" y="22" fill="#94A3B8">SYSTEM STATUS</text>
      <text x="12" y="44" fill="#34D399" font-weight="800">ONLINE &#9679;</text>
      <text x="12" y="60" fill="#00F2FE">Ready for Opportunities</text>
    </g>
  </g>
</svg>'''

files = [
    ("hero-os.svg", hero_svg),
    ("terminal-ai.svg", terminal_svg),
    ("roadmap.svg", roadmap_svg),
    ("galaxy.svg", galaxy_svg),
    ("command-center.svg", command_center_svg),
    ("milestones.svg", milestones_svg),
    ("footer-hud.svg", footer_svg),
]

for filename, content in files:
    try:
        ET.fromstring(content)
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Validated & Written: {filename}")
    except Exception as e:
        print(f"FAILED on {filename}: {e}")

print("All AI OS SVG assets generated successfully!")
