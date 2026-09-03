import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO IDENTITY (assets/hero-identity.svg)
# -------------------------------------------------------------
hero_identity_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="hid-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="50%" stop-color="#081124" />
      <stop offset="100%" stop-color="#110724" />
    </linearGradient>

    <linearGradient id="hid-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="hid-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Frame -->
  <rect width="850" height="250" rx="16" fill="url(#hid-bg)" stroke="url(#hid-border)" stroke-width="1.8" />
  <rect x="0" y="0" width="850" height="4" rx="2" fill="url(#hid-border)" filter="url(#hid-glow)" />

  <!-- Top Window Bar -->
  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">AI_ENGINEER_CONTROL_CENTER // IDENTITY_KERNEL // V5.0</text>
    <text x="800" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYSTEM STATUS: ONLINE &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- Left Identity Column -->
  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#hid-glow)" />

    <text x="20" y="38" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="14.5" font-weight="700">Engineering Intelligence From Data</text>
    
    <text x="20" y="96" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">BMS College of Engineering (BMSCE) &#8226; Bengaluru, India</text>

    <!-- Focus Badges -->
    <g transform="translate(20, 118)">
      <rect width="112" height="24" rx="12" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
      <text x="56" y="16" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">ARTIFICIAL INTEL</text>

      <rect x="122" width="125" height="24" rx="12" fill="#161B22" stroke="#34D399" stroke-width="1" />
      <text x="184.5" y="16" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">MACHINE LEARNING</text>

      <rect x="257" width="105" height="24" rx="12" fill="#161B22" stroke="#818CF8" stroke-width="1" />
      <text x="309.5" y="16" fill="#818CF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">DATA SCIENCE</text>

      <rect x="372" width="115" height="24" rx="12" fill="#161B22" stroke="#C084FC" stroke-width="1" />
      <text x="429.5" y="16" fill="#C084FC" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SYSTEM THINKER</text>
    </g>
  </g>

  <!-- Right Neural Graphic -->
  <g transform="translate(560, 50)">
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#hid-glow)" />

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

    <circle cx="127" cy="35" r="5" fill="#34D399" filter="url(#hid-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="88" r="6.5" fill="#00F2FE" filter="url(#hid-glow)">
      <animate attributeName="r" values="5;8;5" dur="1.8s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="140" r="5" fill="#C084FC" filter="url(#hid-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2.4s" repeatCount="indefinite" />
    </circle>

    <circle cx="210" cy="88" r="8" fill="#818CF8" filter="url(#hid-glow)">
      <animate attributeName="r" values="7;10;7" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="210" cy="88" r="4" fill="#FFFFFF" />

    <text x="127.5" y="165" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" text-anchor="middle">AI_PIPELINE: ACTIVE_FIT</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. AI ENGINEER DNA (assets/engineer-dna.svg)
# -------------------------------------------------------------
dna_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="850" height="280">
  <defs>
    <linearGradient id="dna-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#091024" />
    </linearGradient>

    <filter id="dna-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="280" rx="14" fill="url(#dna-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">AI ENGINEER DNA // COMPETENCY TELEMETRY MATRIX</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">CALIBRATED &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Telemetry Bars -->
  <g transform="translate(36, 56)" font-family="'Fira Code', monospace" font-size="11">
    <!-- Machine Learning (90%) -->
    <text x="0" y="20" fill="#E2E8F0" font-weight="600">Machine Learning</text>
    <text x="180" y="20" fill="#38BDF8" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9617;</text>
    <rect x="360" y="10" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="10" width="324" height="12" rx="6" fill="#38BDF8" filter="url(#dna-glow)">
      <animate attributeName="width" values="300;324;300" dur="3s" repeatCount="indefinite" />
    </rect>
    <text x="735" y="20" fill="#38BDF8" font-weight="800">90%</text>

    <!-- Python (100%) -->
    <text x="0" y="48" fill="#E2E8F0" font-weight="600">Python Engineering</text>
    <text x="180" y="48" fill="#00F2FE" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</text>
    <rect x="360" y="38" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="38" width="360" height="12" rx="6" fill="#00F2FE" filter="url(#dna-glow)" />
    <text x="735" y="48" fill="#00F2FE" font-weight="800">100%</text>

    <!-- Data Science (80%) -->
    <text x="0" y="76" fill="#E2E8F0" font-weight="600">Data Science &amp; Stats</text>
    <text x="180" y="76" fill="#34D399" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9617;&#9617;</text>
    <rect x="360" y="66" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="66" width="288" height="12" rx="6" fill="#34D399" filter="url(#dna-glow)">
      <animate attributeName="width" values="270;288;270" dur="3.5s" repeatCount="indefinite" />
    </rect>
    <text x="735" y="76" fill="#34D399" font-weight="800">80%</text>

    <!-- SQL & Databases (90%) -->
    <text x="0" y="104" fill="#E2E8F0" font-weight="600">SQL &amp; Database Arch</text>
    <text x="180" y="104" fill="#F59E0B" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9617;</text>
    <rect x="360" y="94" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="94" width="324" height="12" rx="6" fill="#F59E0B" filter="url(#dna-glow)" />
    <text x="735" y="104" fill="#F59E0B" font-weight="800">90%</text>

    <!-- Research & Deep-Tech (80%) -->
    <text x="0" y="132" fill="#E2E8F0" font-weight="600">Research &amp; Deep-Tech</text>
    <text x="180" y="132" fill="#818CF8" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9617;&#9617;</text>
    <rect x="360" y="122" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="122" width="288" height="12" rx="6" fill="#818CF8" filter="url(#dna-glow)" />
    <text x="735" y="132" fill="#818CF8" font-weight="800">80%</text>

    <!-- Problem Solving (100%) -->
    <text x="0" y="160" fill="#E2E8F0" font-weight="600">Problem Solving</text>
    <text x="180" y="160" fill="#00F2FE" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</text>
    <rect x="360" y="150" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="150" width="360" height="12" rx="6" fill="#00F2FE" filter="url(#dna-glow)" />
    <text x="735" y="160" fill="#00F2FE" font-weight="800">100%</text>

    <!-- System Design (70%) -->
    <text x="0" y="188" fill="#E2E8F0" font-weight="600">System Architecture</text>
    <text x="180" y="188" fill="#C084FC" font-weight="800">&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9617;&#9617;&#9617;</text>
    <rect x="360" y="178" width="360" height="12" rx="6" fill="#161B22" />
    <rect x="360" y="178" width="252" height="12" rx="6" fill="#C084FC" filter="url(#dna-glow)" />
    <text x="735" y="188" fill="#C084FC" font-weight="800">70%</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. ENGINEERING PERSONA (assets/persona.svg)
# -------------------------------------------------------------
persona_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 240" width="850" height="240">
  <defs>
    <linearGradient id="pers-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913" />
      <stop offset="100%" stop-color="#0E0720" />
    </linearGradient>

    <linearGradient id="pers-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="240" rx="14" fill="url(#pers-bg)" stroke="url(#pers-border)" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">ENGINEERING PROFILE // PERSONA &amp; PROBLEM-SOLVING ARCHETYPE</text>
    <text x="790" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10" text-anchor="end">KERNEL SPEC</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Content Grid -->
  <g transform="translate(36, 60)" font-family="'Fira Code', monospace" font-size="11">
    <g transform="translate(0, 0)">
      <rect width="370" height="70" rx="8" fill="#0D1117" stroke="#1E293B" stroke-width="1" />
      <text x="14" y="24" fill="#94A3B8">THINKING STYLE</text>
      <text x="14" y="48" fill="#00F2FE" font-size="13" font-weight="800">System Builder &amp; Architect</text>
    </g>

    <g transform="translate(395, 0)">
      <rect width="380" height="70" rx="8" fill="#0D1117" stroke="#1E293B" stroke-width="1" />
      <text x="14" y="24" fill="#94A3B8">ENGINEERING APPROACH</text>
      <text x="14" y="48" fill="#34D399" font-size="13" font-weight="800">Learn &#8594; Build &#8594; Optimize</text>
    </g>

    <g transform="translate(0, 85)">
      <rect width="370" height="75" rx="8" fill="#0D1117" stroke="#1E293B" stroke-width="1" />
      <text x="14" y="22" fill="#94A3B8">FAVOURITE PROBLEMS</text>
      <text x="14" y="42" fill="#F8FAFC" font-size="10.5">Complex Data &#8226; Prediction Systems</text>
      <text x="14" y="60" fill="#CBD5E1" font-size="10">Automation &#8226; Decision Intelligence</text>
    </g>

    <g transform="translate(395, 85)">
      <rect width="380" height="75" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="14" y="22" fill="#94A3B8">CURRENT MISSION</text>
      <text x="14" y="44" fill="#F8FAFC" font-size="10.5" font-weight="700">"Build intelligent systems that solve</text>
      <text x="14" y="62" fill="#38BDF8" font-size="10.5" font-weight="700">real-world problems with data."</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. SKILL CONSTELLATION (assets/constellation.svg)
# -------------------------------------------------------------
constellation_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 300" width="850" height="300">
  <defs>
    <linearGradient id="con-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040610" />
      <stop offset="100%" stop-color="#0B061A" />
    </linearGradient>

    <filter id="con-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="300" rx="14" fill="url(#con-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#818CF8" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">SKILL CONSTELLATION // INTERCONNECTED CAPABILITY GRAPH</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">NODE_TOPOLOGY &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Graph Constellation Nodes -->
  <g transform="translate(425, 175)">
    <!-- Connected Synapse Lines -->
    <g stroke-width="1.4" opacity="0.65">
      <line x1="0" y1="0" x2="-260" y2="-50" stroke="#00F2FE" />
      <line x1="0" y1="0" x2="-140" y2="55" stroke="#38BDF8" />
      <line x1="0" y1="0" x2="0" y2="-65" stroke="#34D399" />
      <line x1="0" y1="0" x2="160" y2="-50" stroke="#F59E0B" />
      <line x1="0" y1="0" x2="260" y2="45" stroke="#818CF8" />
      <line x1="0" y1="0" x2="-200" y2="35" stroke="#C084FC" />
      <line x1="0" y1="0" x2="130" y2="60" stroke="#00F2FE" />

      <!-- Inter-node perimeter links -->
      <line x1="-260" y1="-50" x2="0" y2="-65" stroke="#1E293B" />
      <line x1="0" y1="-65" x2="160" y2="-50" stroke="#1E293B" />
      <line x1="160" y1="-50" x2="260" y2="45" stroke="#1E293B" />
      <line x1="260" y1="45" x2="130" y2="60" stroke="#1E293B" />
      <line x1="130" y1="60" x2="-140" y2="55" stroke="#1E293B" />
      <line x1="-140" y1="55" x2="-200" y2="35" stroke="#1E293B" />
      <line x1="-200" y1="35" x2="-260" y2="-50" stroke="#1E293B" />
    </g>

    <!-- Center Hub: Artificial Intelligence -->
    <circle cx="0" cy="0" r="34" fill="#0D1117" stroke="#00F2FE" stroke-width="2" filter="url(#con-glow)" />
    <circle cx="0" cy="0" r="28" fill="#161B22" />
    <text x="0" y="-4" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="9.5" font-weight="800" text-anchor="middle">ARTIFICIAL</text>
    <text x="0" y="10" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" text-anchor="middle">INTEL</text>

    <!-- Node 1: Python -->
    <g transform="translate(-260, -50)">
      <rect x="-65" y="-16" width="130" height="32" rx="16" fill="#0D1117" stroke="#00F2FE" stroke-width="1.2" />
      <text x="0" y="4" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; Python</text>
    </g>

    <!-- Node 2: Machine Learning -->
    <g transform="translate(0, -65)">
      <rect x="-75" y="-16" width="150" height="32" rx="16" fill="#0D1117" stroke="#34D399" stroke-width="1.2" />
      <text x="0" y="4" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; Machine Learning</text>
    </g>

    <!-- Node 3: Data Science -->
    <g transform="translate(160, -50)">
      <rect x="-65" y="-16" width="130" height="32" rx="16" fill="#0D1117" stroke="#F59E0B" stroke-width="1.2" />
      <text x="0" y="4" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; Data Science</text>
    </g>

    <!-- Node 4: SQL & DB -->
    <g transform="translate(260, 45)">
      <rect x="-60" y="-16" width="120" height="32" rx="16" fill="#0D1117" stroke="#818CF8" stroke-width="1.2" />
      <text x="0" y="4" fill="#818CF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; SQL &amp; MySQL</text>
    </g>

    <!-- Node 5: Research -->
    <g transform="translate(130, 60)">
      <rect x="-55" y="-16" width="110" height="32" rx="16" fill="#0D1117" stroke="#C084FC" stroke-width="1.2" />
      <text x="0" y="4" fill="#C084FC" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; Research</text>
    </g>

    <!-- Node 6: Flask / React -->
    <g transform="translate(-140, 55)">
      <rect x="-65" y="-16" width="130" height="32" rx="16" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" />
      <text x="0" y="4" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; React &amp; Flask</text>
    </g>

    <!-- Node 7: Git & GitHub -->
    <g transform="translate(-200, 35)">
      <rect x="-55" y="-16" width="110" height="32" rx="16" fill="#0D1117" stroke="#34D399" stroke-width="1.2" />
      <text x="0" y="4" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9670; Git / GitHub</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. LIVE INTELLIGENCE FEED (assets/live-feed.svg)
# -------------------------------------------------------------
live_feed_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 230" width="850" height="230">
  <defs>
    <linearGradient id="feed-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0A0F22" />
    </linearGradient>
  </defs>

  <rect width="850" height="230" rx="14" fill="url(#feed-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">LIVE INTELLIGENCE FEED // REALTIME SYSTEM LOGS</text>
    <text x="790" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">STREAMING &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Content Split -->
  <g transform="translate(36, 60)" font-family="'Fira Code', monospace">
    <!-- Left: Currently Exploring -->
    <g transform="translate(0, 0)">
      <rect width="440" height="145" rx="8" fill="#0D1117" stroke="#1E293B" stroke-width="1" />
      <text x="14" y="24" fill="#38BDF8" font-size="11" font-weight="800">ACTIVE LEARNING TRAJECTORY</text>
      <line x1="14" y1="32" x2="426" y2="32" stroke="#1E293B" stroke-width="1" />

      <g transform="translate(14, 52)" font-size="10" fill="#CBD5E1">
        <text x="0" y="0"><tspan fill="#34D399">&#8594;</tspan> Advanced Machine Learning &amp; Predictive Modeling</text>
        <text x="0" y="24"><tspan fill="#34D399">&#8594;</tspan> FastAPI &amp; Docker Microservices</text>
        <text x="0" y="48"><tspan fill="#34D399">&#8594;</tspan> MLOps &amp; Automated Pipeline Deployment</text>
        <text x="0" y="72"><tspan fill="#34D399">&#8594;</tspan> LLM Systems &amp; Multi-Agent Frameworks</text>
      </g>
    </g>

    <!-- Right: Current Modes -->
    <g transform="translate(460, 0)">
      <rect width="320" height="145" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="14" y="24" fill="#34D399" font-size="11" font-weight="800">SYSTEM OPERATING MODES</text>
      <line x1="14" y1="32" x2="306" y2="32" stroke="#1E293B" stroke-width="1" />

      <g transform="translate(14, 56)" font-size="10.5">
        <text x="0" y="0" fill="#94A3B8">Research Mode:</text>
        <text x="150" y="0" fill="#00F2FE" font-weight="800">ACTIVE &#9679;</text>

        <text x="0" y="28" fill="#94A3B8">Building Mode:</text>
        <text x="150" y="28" fill="#34D399" font-weight="800">ACTIVE &#9679;</text>

        <text x="0" y="56" fill="#94A3B8">Learning Mode:</text>
        <text x="150" y="56" fill="#818CF8" font-weight="800">ACTIVE &#9679;</text>
      </g>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. INTERACTIVE TERMINAL (assets/terminal-identity.svg)
# -------------------------------------------------------------
terminal_identity_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 240" width="850" height="240">
  <defs>
    <linearGradient id="term-id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C16" />
      <stop offset="100%" stop-color="#04070F" />
    </linearGradient>

    <linearGradient id="term-id-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="240" rx="14" fill="url(#term-id-bg)" stroke="url(#term-id-border)" stroke-width="1.5" />

  <!-- Top Bar -->
  <g transform="translate(18, 16)">
    <circle cx="8" cy="6" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="6" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="6" r="4.5" fill="#27C93F" />
    <text x="60" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">kathyayini@ai-os: ~ (zsh)</text>
    <text x="800" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">&#9889; SESSION ACTIVE</text>
  </g>
  <line x1="15" y1="36" x2="835" y2="36" stroke="#1E293B" stroke-width="1" />

  <!-- Terminal Commands -->
  <g transform="translate(24, 52)" font-family="'Fira Code', monospace" font-size="11" font-weight="500">
    <text x="0" y="16">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">whoami</tspan>
    </text>
    <text x="18" y="34" fill="#34D399" font-weight="700">&#8594; Kathyayini Prabhu [AI &amp; Data Science Engineer @ BMSCE Bengaluru]</text>

    <text x="0" y="58">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">specialization</tspan>
    </text>
    <text x="18" y="76" fill="#CBD5E1">
      <tspan fill="#00F2FE">&#9670; Artificial Intelligence</tspan>   
      <tspan fill="#34D399">&#9670; Machine Learning</tspan>   
      <tspan fill="#818CF8">&#9670; Data Science</tspan>
    </text>

    <text x="0" y="100">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">currently_learning</tspan>
    </text>
    <text x="18" y="118" fill="#CBD5E1">
      <tspan fill="#F59E0B">&#9658; MLOps</tspan>   
      <tspan fill="#38BDF8">&#9658; FastAPI</tspan>   
      <tspan fill="#C084FC">&#9658; LLM Multi-Agent Frameworks</tspan>
    </text>

    <text x="0" y="142">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">mission</tspan>
    </text>
    <text x="18" y="160" fill="#F8FAFC" font-weight="700">&#10024; "Build intelligent systems that turn data into decisions."</text>

    <text x="0" y="184">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#34D399">echo "Engineering Intelligence From Data"</tspan>
    </text>
    <rect x="375" y="173" width="7" height="13" fill="#00F2FE">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# -------------------------------------------------------------
# 7. MISSION CONTROL (assets/mission-control.svg)
# -------------------------------------------------------------
mission_control_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 160" width="850" height="160">
  <defs>
    <linearGradient id="mc-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0D0721" />
    </linearGradient>

    <linearGradient id="mc-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="160" rx="14" fill="url(#mc-bg)" stroke="url(#mc-border)" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">MISSION CONTROL // SYSTEM STATUS HUD</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">&#9679; ALL SYSTEMS ONLINE</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Telemetry Grid -->
  <g transform="translate(30, 62)" font-family="'Fira Code', monospace" font-size="10.5">
    <!-- Box 1 -->
    <rect width="185" height="74" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="0.8" />
    <text x="12" y="22" fill="#94A3B8">CURRENT OBJECTIVE</text>
    <text x="12" y="44" fill="#38BDF8" font-weight="700">Build Intelligent</text>
    <text x="12" y="60" fill="#38BDF8" font-weight="700">AI Systems</text>

    <!-- Box 2 -->
    <g transform="translate(198, 0)">
      <rect width="185" height="74" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="0.8" />
      <text x="12" y="22" fill="#94A3B8">CURRENT DOMAIN</text>
      <text x="12" y="44" fill="#34D399" font-weight="700">Artificial</text>
      <text x="12" y="60" fill="#34D399" font-weight="700">Intelligence</text>
    </g>

    <!-- Box 3 -->
    <g transform="translate(396, 0)">
      <rect width="185" height="74" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="0.8" />
      <text x="12" y="22" fill="#94A3B8">CURRENT FOCUS</text>
      <text x="12" y="44" fill="#818CF8" font-weight="700">Machine Learning</text>
      <text x="12" y="60" fill="#CBD5E1">&amp; Research</text>
    </g>

    <!-- Box 4 -->
    <g transform="translate(594, 0)">
      <rect width="196" height="74" rx="6" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="12" y="22" fill="#94A3B8">LOCATION &amp; STATUS</text>
      <text x="12" y="44" fill="#F8FAFC" font-weight="700">Bengaluru, India</text>
      <text x="12" y="60" fill="#34D399" font-weight="800">ONLINE &#9679;</text>
    </g>
  </g>
</svg>'''

files = [
    ("hero-identity.svg", hero_identity_svg),
    ("engineer-dna.svg", dna_svg),
    ("persona.svg", persona_svg),
    ("constellation.svg", constellation_svg),
    ("live-feed.svg", live_feed_svg),
    ("terminal-identity.svg", terminal_identity_svg),
    ("mission-control.svg", mission_control_svg),
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

print("All Identity Dashboard SVG assets generated successfully!")
