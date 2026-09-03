import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO ENGINEER (assets/hero-engineer.svg)
# -------------------------------------------------------------
hero_engineer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="he-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814">
        <animate attributeName="stop-color" values="#050814; #091326; #0F0922; #050814" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#091326">
        <animate attributeName="stop-color" values="#091326; #160F30; #06192E; #091326" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#0F0922">
        <animate attributeName="stop-color" values="#0F0922; #050814; #091326; #0F0922" dur="12s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <linearGradient id="he-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="he-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Frame -->
  <rect width="850" height="250" rx="16" fill="url(#he-bg)" stroke="url(#he-border)" stroke-width="1.8" />
  <rect x="0" y="0" width="850" height="4.5" rx="2.25" fill="url(#he-border)" filter="url(#he-glow)" />

  <!-- Window Header Bar -->
  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">AI_ENGINEER_PROFILE // KATHYAYINI_PRABHU // LIVE</text>
    <text x="800" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">STATUS: ACTIVE &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- Left Hero Details -->
  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#he-glow)" />

    <text x="20" y="38" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="15" font-weight="700">AI &amp; Data Science Engineer</text>
    
    <text x="20" y="96" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">BMS College of Engineering (BMSCE) &#8226; Bengaluru, India</text>

    <!-- Core Badges -->
    <g transform="translate(20, 118)">
      <rect width="115" height="24" rx="12" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
      <text x="57.5" y="16" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">ARTIFICIAL INTEL</text>

      <rect x="125" width="125" height="24" rx="12" fill="#161B22" stroke="#34D399" stroke-width="1" />
      <text x="187.5" y="16" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">MACHINE LEARNING</text>

      <rect x="260" width="105" height="24" rx="12" fill="#161B22" stroke="#818CF8" stroke-width="1" />
      <text x="312.5" y="16" fill="#818CF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">DATA SCIENCE</text>

      <rect x="375" width="115" height="24" rx="12" fill="#161B22" stroke="#C084FC" stroke-width="1" />
      <text x="432.5" y="16" fill="#C084FC" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SOFTWARE ENG</text>
    </g>
  </g>

  <!-- Right Neural & Hologram Graphic -->
  <g transform="translate(560, 50)">
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#he-glow)" />

    <!-- Animated Particles -->
    <circle cx="50" cy="40" r="1.5" fill="#00F2FE" opacity="0.8">
      <animate attributeName="cy" values="40;140;40" dur="6s" repeatCount="indefinite" />
    </circle>
    <circle cx="180" cy="130" r="2" fill="#34D399" opacity="0.7">
      <animate attributeName="cy" values="130;30;130" dur="7s" repeatCount="indefinite" />
    </circle>
    <circle cx="210" cy="50" r="1.8" fill="#C084FC" opacity="0.8">
      <animate attributeName="cy" values="50;150;50" dur="5s" repeatCount="indefinite" />
    </circle>

    <!-- Radar Circle -->
    <circle cx="127" cy="88" r="62" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="4 4" />
    <circle cx="127" cy="88" r="60" fill="none" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="0 127 88" to="360 127 88" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- Synapses -->
    <g stroke-width="1" opacity="0.65">
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

    <circle cx="127" cy="35" r="5" fill="#34D399" filter="url(#he-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="88" r="6.5" fill="#00F2FE" filter="url(#he-glow)">
      <animate attributeName="r" values="5;8;5" dur="1.8s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="140" r="5" fill="#C084FC" filter="url(#he-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2.4s" repeatCount="indefinite" />
    </circle>

    <circle cx="210" cy="88" r="8" fill="#818CF8" filter="url(#he-glow)">
      <animate attributeName="r" values="7;10;7" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="210" cy="88" r="4" fill="#FFFFFF" />

    <text x="127.5" y="165" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" text-anchor="middle">AI_INFERENCE: ONLINE</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. INTERACTIVE TERMINAL (assets/terminal-interactive.svg)
# -------------------------------------------------------------
terminal_interactive_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="ti-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C16" />
      <stop offset="100%" stop-color="#04070F" />
    </linearGradient>

    <linearGradient id="ti-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#ti-bg)" stroke="url(#ti-border)" stroke-width="1.5" />

  <!-- Top Bar -->
  <g transform="translate(18, 16)">
    <circle cx="8" cy="6" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="6" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="6" r="4.5" fill="#27C93F" />
    <text x="60" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">kathyayini@ai-workstation: ~ (zsh)</text>
    <text x="800" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">&#9889; SESSION_ACTIVE</text>
  </g>
  <line x1="15" y1="36" x2="835" y2="36" stroke="#1E293B" stroke-width="1" />

  <!-- Terminal Commands -->
  <g transform="translate(24, 52)" font-family="'Fira Code', monospace" font-size="11" font-weight="500">
    <text x="0" y="16">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">whoami</tspan>
    </text>
    <text x="18" y="34" fill="#34D399" font-weight="700">&#8594; Kathyayini Prabhu [AI &amp; Data Science Engineer @ BMSCE Bengaluru]</text>

    <text x="0" y="58">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">focus</tspan>
    </text>
    <text x="18" y="76" fill="#CBD5E1">
      <tspan fill="#00F2FE">&#9670; Artificial Intelligence</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#34D399">&#9670; Machine Learning</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#818CF8">&#9670; Data Science</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#C084FC">&#9670; Software Engineering</tspan>
    </text>

    <text x="0" y="100">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">currently_learning</tspan>
    </text>
    <text x="18" y="118" fill="#CBD5E1">
      <tspan fill="#F59E0B">&#9658; MLOps</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#38BDF8">&#9658; FastAPI</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#C084FC">&#9658; LLM Agents</tspan>&nbsp;&nbsp;&nbsp;&nbsp;
      <tspan fill="#34D399">&#9658; Advanced Machine Learning</tspan>
    </text>

    <text x="0" y="142">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">mission</tspan>
    </text>
    <text x="18" y="160" fill="#F8FAFC" font-weight="700">&#10024; "Build intelligent systems that transform data into decisions."</text>

    <text x="0" y="184">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#34D399">echo "Engineering Intelligence From Data"</tspan>
    </text>
    <rect x="375" y="173" width="7" height="13" fill="#00F2FE">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. CAPABILITY MATRIX (assets/capability-matrix.svg)
# -------------------------------------------------------------
capability_matrix_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 310" width="850" height="310">
  <defs>
    <linearGradient id="cm-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0B0F22" />
    </linearGradient>

    <filter id="cm-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="310" rx="14" fill="url(#cm-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">CAPABILITY MATRIX // 4 CORE TECHNICAL PILLARS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">PRODUCTION READY &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 4 CARDS GRID (2x2) -->
  
  <!-- Card 1: AI & ML -->
  <g transform="translate(30, 60)">
    <rect width="380" height="110" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="16" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; 01 // ARTIFICIAL INTEL &amp; ML</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#34D399">&#9658;</tspan> Machine Learning</text>
      <text x="180" y="0"><tspan fill="#34D399">&#9658;</tspan> Deep Learning</text>
      <text x="0" y="22"><tspan fill="#34D399">&#9658;</tspan> Predictive Modeling</text>
      <text x="180" y="22"><tspan fill="#34D399">&#9658;</tspan> Feature Engineering</text>
      <text x="0" y="44"><tspan fill="#34D399">&#9658;</tspan> Model Evaluation</text>
      <text x="180" y="44"><tspan fill="#34D399">&#9658;</tspan> Scikit-Learn</text>
    </g>
  </g>

  <!-- Card 2: Data Science & Analytics -->
  <g transform="translate(430, 60)">
    <rect width="390" height="110" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="16" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; 02 // DATA SCIENCE &amp; ANALYTICS</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9658;</tspan> Data Analysis</text>
      <text x="180" y="0"><tspan fill="#00F2FE">&#9658;</tspan> Pandas &amp; NumPy</text>
      <text x="0" y="22"><tspan fill="#00F2FE">&#9658;</tspan> Data Visualization</text>
      <text x="180" y="22"><tspan fill="#00F2FE">&#9658;</tspan> Statistical Analysis</text>
      <text x="0" y="44"><tspan fill="#00F2FE">&#9658;</tspan> Data Processing</text>
      <text x="180" y="44"><tspan fill="#00F2FE">&#9658;</tspan> Exploratory Analysis</text>
    </g>
  </g>

  <!-- Card 3: Software Engineering -->
  <g transform="translate(30, 182)">
    <rect width="380" height="110" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="16" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; 03 // SOFTWARE ENGINEERING</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Python</text>
      <text x="180" y="0"><tspan fill="#818CF8">&#9658;</tspan> Flask</text>
      <text x="0" y="22"><tspan fill="#818CF8">&#9658;</tspan> FastAPI</text>
      <text x="180" y="22"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
      <text x="0" y="44"><tspan fill="#818CF8">&#9658;</tspan> Git</text>
      <text x="180" y="44"><tspan fill="#818CF8">&#9658;</tspan> GitHub</text>
    </g>
  </g>

  <!-- Card 4: Database Systems -->
  <g transform="translate(430, 182)">
    <rect width="390" height="110" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="16" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9670; 04 // DATABASE SYSTEMS</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9658;</tspan> SQL &amp; MySQL</text>
      <text x="180" y="0"><tspan fill="#F59E0B">&#9658;</tspan> Database Design</text>
      <text x="0" y="22"><tspan fill="#F59E0B">&#9658;</tspan> Query Optimization</text>
      <text x="180" y="22"><tspan fill="#F59E0B">&#9658;</tspan> Relational Modeling</text>
      <text x="0" y="44"><tspan fill="#F59E0B">&#9658;</tspan> Indexing &amp; Schemas</text>
      <text x="180" y="44"><tspan fill="#F59E0B">&#9658;</tspan> Query Performance</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. LEARNING DASHBOARD (assets/learning-dashboard.svg)
# -------------------------------------------------------------
learning_dashboard_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="ld-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#091024" />
    </linearGradient>

    <filter id="ld-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#ld-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">CURRENT LEARNING DASHBOARD // TRAJECTORY METRICS</text>
    <text x="790" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">IN PROGRESS &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 6 PROGRESS CARDS (2x3) -->
  <g transform="translate(36, 60)" font-family="'Fira Code', monospace" font-size="10.5">
    
    <!-- 1. MLOps -->
    <g transform="translate(0, 0)">
      <rect width="370" height="48" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="14" y="20" fill="#E2E8F0" font-weight="700">MLOps</text>
      <text x="310" y="20" fill="#38BDF8" font-weight="800">80%</text>
      <rect x="14" y="28" width="340" height="8" rx="4" fill="#161B22" />
      <rect x="14" y="28" width="272" height="8" rx="4" fill="#38BDF8" filter="url(#ld-glow)">
        <animate attributeName="width" values="250;272;250" dur="3s" repeatCount="indefinite" />
      </rect>
    </g>

    <!-- 2. FastAPI -->
    <g transform="translate(395, 0)">
      <rect width="380" height="48" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="14" y="20" fill="#E2E8F0" font-weight="700">FastAPI</text>
      <text x="320" y="20" fill="#34D399" font-weight="800">90%</text>
      <rect x="14" y="28" width="350" height="8" rx="4" fill="#161B22" />
      <rect x="14" y="28" width="315" height="8" rx="4" fill="#34D399" filter="url(#ld-glow)" />
    </g>

    <!-- 3. LLM Agents -->
    <g transform="translate(0, 58)">
      <rect width="370" height="48" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="14" y="20" fill="#E2E8F0" font-weight="700">LLM Agents &amp; Frameworks</text>
      <text x="310" y="20" fill="#818CF8" font-weight="800">70%</text>
      <rect x="14" y="28" width="340" height="8" rx="4" fill="#161B22" />
      <rect x="14" y="28" width="238" height="8" rx="4" fill="#818CF8" filter="url(#ld-glow)">
        <animate attributeName="width" values="220;238;220" dur="3.5s" repeatCount="indefinite" />
      </rect>
    </g>

    <!-- 4. Advanced ML -->
    <g transform="translate(395, 58)">
      <rect width="380" height="48" rx="8" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="14" y="20" fill="#E2E8F0" font-weight="700">Advanced Machine Learning</text>
      <text x="320" y="20" fill="#00F2FE" font-weight="800">90%</text>
      <rect x="14" y="28" width="350" height="8" rx="4" fill="#161B22" />
      <rect x="14" y="28" width="315" height="8" rx="4" fill="#00F2FE" filter="url(#ld-glow)" />
    </g>

    <!-- 5. System Design -->
    <g transform="translate(0, 116)">
      <rect width="370" height="48" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="14" y="20" fill="#E2E8F0" font-weight="700">System Design</text>
      <text x="310" y="20" fill="#C084FC" font-weight="800">75%</text>
      <rect x="14" y="28" width="340" height="8" rx="4" fill="#161B22" />
      <rect x="14" y="28" width="255" height="8" rx="4" fill="#C084FC" filter="url(#ld-glow)" />
    </g>

    <!-- 6. Cloud Fundamentals -->
    <g transform="translate(395, 116)">
      <rect width="380" height="48" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="14" y="20" fill="#E2E8F0" font-weight="700">Cloud Fundamentals &amp; Docker</text>
      <text x="320" y="20" fill="#F59E0B" font-weight="800">80%</text>
      <rect x="14" y="28" width="350" height="8" rx="4" fill="#161B22" />
      <rect x="14" y="28" width="280" height="8" rx="4" fill="#F59E0B" filter="url(#ld-glow)">
        <animate attributeName="width" values="260;280;260" dur="2.8s" repeatCount="indefinite" />
      </rect>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. ENGINEERING STATS (assets/engineering-stats.svg)
# -------------------------------------------------------------
engineering_stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 160" width="850" height="160">
  <defs>
    <linearGradient id="es-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0B1024" />
    </linearGradient>

    <filter id="es-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="160" rx="14" fill="url(#es-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- 4 STATS CARDS -->
  <g transform="translate(24, 20)">
    <!-- 1. AI & ML -->
    <g transform="translate(0, 0)">
      <rect width="188" height="120" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#es-glow)" />
      <text x="14" y="28" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#129504; AI &amp; ML</text>
      <line x1="14" y1="36" x2="174" y2="36" stroke="#1E293B" stroke-width="1" />
      <g transform="translate(14, 54)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
        <text x="0" y="0"><tspan fill="#34D399">&#9654;</tspan> Predictive Models</text>
        <text x="0" y="22"><tspan fill="#34D399">&#9654;</tspan> Feature Engineering</text>
        <text x="0" y="44"><tspan fill="#34D399">&#9654;</tspan> Data Pipelines</text>
      </g>
    </g>

    <!-- 2. Data Science -->
    <g transform="translate(204, 0)">
      <rect width="188" height="120" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1.2" filter="url(#es-glow)" />
      <text x="14" y="28" fill="#34D399" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#128202; Data Science</text>
      <line x1="14" y1="36" x2="174" y2="36" stroke="#1E293B" stroke-width="1" />
      <g transform="translate(14, 54)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
        <text x="0" y="0"><tspan fill="#00F2FE">&#9654;</tspan> Analytics</text>
        <text x="0" y="22"><tspan fill="#00F2FE">&#9654;</tspan> Visualization</text>
        <text x="0" y="44"><tspan fill="#00F2FE">&#9654;</tspan> Statistics</text>
      </g>
    </g>

    <!-- 3. Software Engineering -->
    <g transform="translate(408, 0)">
      <rect width="188" height="120" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1.2" filter="url(#es-glow)" />
      <text x="14" y="28" fill="#818CF8" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#128187; Software Eng</text>
      <line x1="14" y1="36" x2="174" y2="36" stroke="#1E293B" stroke-width="1" />
      <g transform="translate(14, 54)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
        <text x="0" y="0"><tspan fill="#818CF8">&#9654;</tspan> Backend Systems</text>
        <text x="0" y="22"><tspan fill="#818CF8">&#9654;</tspan> REST APIs</text>
        <text x="0" y="44"><tspan fill="#818CF8">&#9654;</tspan> Version Control</text>
      </g>
    </g>

    <!-- 4. Database Systems -->
    <g transform="translate(612, 0)">
      <rect width="190" height="120" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1.2" filter="url(#es-glow)" />
      <text x="14" y="28" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#128452; Databases</text>
      <line x1="14" y1="36" x2="176" y2="36" stroke="#1E293B" stroke-width="1" />
      <g transform="translate(14, 54)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
        <text x="0" y="0"><tspan fill="#F59E0B">&#9654;</tspan> SQL &amp; MySQL</text>
        <text x="0" y="22"><tspan fill="#F59E0B">&#9654;</tspan> Query Tuning</text>
        <text x="0" y="44"><tspan fill="#F59E0B">&#9654;</tspan> Schema Design</text>
      </g>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. FOOTER QUOTE (assets/footer-quote.svg)
# -------------------------------------------------------------
footer_quote_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 140" width="850" height="140">
  <defs>
    <linearGradient id="fq-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0E0720" />
    </linearGradient>

    <linearGradient id="fq-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>

    <filter id="fq-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="140" rx="14" fill="url(#fq-bg)" stroke="url(#fq-border)" stroke-width="1.5" />

  <!-- Animated Quote Text -->
  <g transform="translate(425, 60)" text-anchor="middle">
    <text x="0" y="0" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="18" font-weight="800" filter="url(#fq-glow)" letter-spacing="1">
      "Engineering Intelligence From Data"
    </text>
    <text x="0" y="32" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="11">
      [PROCESS COMPLETED] &#8226; SESSION STATUS: ONLINE &#9679; &#8226; BENGALURU, INDIA
    </text>
  </g>

  <!-- Terminal ending pulse line -->
  <line x1="200" y1="115" x2="650" y2="115" stroke="#1E293B" stroke-width="1" />
  <circle cx="425" cy="115" r="3" fill="#34D399">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.2s" repeatCount="indefinite" />
  </circle>
</svg>'''

files = [
    ("hero-engineer.svg", hero_engineer_svg),
    ("terminal-interactive.svg", terminal_interactive_svg),
    ("capability-matrix.svg", capability_matrix_svg),
    ("learning-dashboard.svg", learning_dashboard_svg),
    ("engineering-stats.svg", engineering_stats_svg),
    ("footer-quote.svg", footer_quote_svg),
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

print("All Ultimate Engineer SVG assets generated successfully!")
