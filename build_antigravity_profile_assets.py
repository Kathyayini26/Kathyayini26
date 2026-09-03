import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO (assets/antigravity-hero.svg)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="agh-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816">
        <animate attributeName="stop-color" values="#050816; #070B1F; #0A1028; #050816" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#070B1F">
        <animate attributeName="stop-color" values="#070B1F; #120A2B; #07152B; #070B1F" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#0A1028">
        <animate attributeName="stop-color" values="#0A1028; #050816; #070B1F; #0A1028" dur="12s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <linearGradient id="agh-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="agh-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Shell Frame -->
  <rect width="850" height="250" rx="16" fill="url(#agh-bg)" stroke="url(#agh-border)" stroke-width="1.8" />
  <rect x="0" y="0" width="850" height="4.5" rx="2.25" fill="url(#agh-border)" filter="url(#agh-glow)" />

  <!-- Top Header Bar -->
  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">ANTI_GRAVITY_AI_COMMAND_CENTER // KATHYAYINI_PRABHU</text>
    <text x="800" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS.STATUS: ONLINE &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- Left Details -->
  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#agh-glow)" />

    <text x="20" y="38" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="15" font-weight="700">AI &amp; Data Science Engineer</text>
    
    <text x="20" y="96" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">BMS College of Engineering (BMSCE) &#8226; CGPA: 9.37</text>

    <!-- Badges -->
    <g transform="translate(20, 118)">
      <rect width="115" height="24" rx="12" fill="#161B22" stroke="#00F2FE" stroke-width="1" />
      <text x="57.5" y="16" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">ARTIFICIAL INTEL</text>

      <rect x="125" width="125" height="24" rx="12" fill="#161B22" stroke="#34D399" stroke-width="1" />
      <text x="187.5" y="16" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">MACHINE LEARNING</text>

      <rect x="260" width="105" height="24" rx="12" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
      <text x="312.5" y="16" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">DATA SCIENCE</text>

      <rect x="375" width="118" height="24" rx="12" fill="#161B22" stroke="#C084FC" stroke-width="1" />
      <text x="434" y="16" fill="#C084FC" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">KNOWLEDGE GRAPHS</text>
    </g>
  </g>

  <!-- Right Neural Visual -->
  <g transform="translate(560, 50)">
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#agh-glow)" />

    <!-- Floating energy nodes -->
    <circle cx="50" cy="40" r="1.5" fill="#00F2FE" opacity="0.8">
      <animate attributeName="cy" values="40;140;40" dur="6s" repeatCount="indefinite" />
    </circle>
    <circle cx="180" cy="130" r="2" fill="#34D399" opacity="0.7">
      <animate attributeName="cy" values="130;30;130" dur="7s" repeatCount="indefinite" />
    </circle>
    <circle cx="210" cy="50" r="1.8" fill="#C084FC" opacity="0.8">
      <animate attributeName="cy" values="50;150;50" dur="5s" repeatCount="indefinite" />
    </circle>

    <!-- Radar circle -->
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

    <circle cx="127" cy="35" r="5" fill="#34D399" filter="url(#agh-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="88" r="6.5" fill="#00F2FE" filter="url(#agh-glow)">
      <animate attributeName="r" values="5;8;5" dur="1.8s" repeatCount="indefinite" />
    </circle>
    <circle cx="127" cy="140" r="5" fill="#C084FC" filter="url(#agh-glow)">
      <animate attributeName="r" values="4;6.5;4" dur="2.4s" repeatCount="indefinite" />
    </circle>

    <circle cx="210" cy="88" r="8" fill="#818CF8" filter="url(#agh-glow)">
      <animate attributeName="r" values="7;10;7" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="210" cy="88" r="4" fill="#FFFFFF" />

    <text x="127.5" y="165" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" text-anchor="middle">AI_INFERENCE: ACTIVE</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. INTERACTIVE TERMINAL (assets/antigravity-terminal.svg)
# -------------------------------------------------------------
terminal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="agt-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#080D1F" />
    </linearGradient>

    <linearGradient id="agt-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#agt-bg)" stroke="url(#agt-border)" stroke-width="1.5" />

  <!-- Top Bar -->
  <g transform="translate(18, 16)">
    <circle cx="8" cy="6" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="6" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="6" r="4.5" fill="#27C93F" />
    <text x="60" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">kathyayini@ai-command-center: ~ (zsh)</text>
    <text x="800" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">&#9889; SESSION_ACTIVE</text>
  </g>
  <line x1="15" y1="36" x2="835" y2="36" stroke="#1E293B" stroke-width="1" />

  <!-- Commands -->
  <g transform="translate(24, 52)" font-family="'Fira Code', monospace" font-size="11" font-weight="500">
    <text x="0" y="16">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">whoami</tspan>
    </text>
    <text x="18" y="34" fill="#34D399" font-weight="700">&#8594; Kathyayini Prabhu [AI &amp; Data Science Engineer @ BMS College of Engineering]</text>

    <text x="0" y="58">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">specialization</tspan>
    </text>
    <text x="18" y="76" fill="#CBD5E1">
      <tspan fill="#00F2FE">&#9670; Artificial Intelligence</tspan>   
      <tspan fill="#34D399">&#9670; Machine Learning</tspan>   
      <tspan fill="#818CF8">&#9670; Data Science</tspan>   
      <tspan fill="#C084FC">&#9670; Knowledge Graphs</tspan>
    </text>

    <text x="0" y="100">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">mission</tspan>
    </text>
    <text x="18" y="118" fill="#F8FAFC" font-weight="700">&#10024; "Building intelligent systems that transform data into decisions."</text>

    <text x="0" y="146">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#34D399">echo "Engineering Intelligence From Data"</tspan>
    </text>
    <rect x="375" y="135" width="7" height="13" fill="#00F2FE">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. ABOUT (assets/antigravity-about.svg)
# -------------------------------------------------------------
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 210" width="850" height="210">
  <defs>
    <linearGradient id="aga-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>

    <filter id="aga-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="210" rx="14" fill="url(#aga-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">ABOUT // FLOATING INTELLIGENCE PANEL</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">VERIFIED PROFILE &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <g transform="translate(36, 68)">
    <text x="0" y="18" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800">
      Engineering Intelligence From Data
    </text>

    <text x="0" y="46" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400">
      Third-year Artificial Intelligence &amp; Data Science student focused on Machine Learning, Data Science, Knowledge Graphs,
    </text>
    <text x="0" y="66" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400">
      Predictive Analytics and intelligent software systems.
    </text>

    <text x="0" y="96" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">
      Experienced in building AI solutions spanning biomedical research, risk intelligence, infrastructure analytics,
    </text>
    <text x="0" y="114" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">
      computer vision and data-driven decision making.
    </text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. CAPABILITY MATRIX (assets/antigravity-matrix.svg) - NO PERCENTAGES
# -------------------------------------------------------------
matrix_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 310" width="850" height="310">
  <defs>
    <linearGradient id="agm-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#070B1F" />
    </linearGradient>

    <filter id="agm-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="310" rx="14" fill="url(#agm-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">CAPABILITY MATRIX // 4 ANTI-GRAVITY BLOCKS (ZERO PROGRESS BARS)</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">PRODUCTION VERIFIED &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 4 CARDS -->
  
  <!-- Block 1: AI & ML -->
  <g transform="translate(30, 60)">
    <rect width="380" height="110" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="16" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#129504; BLOCK 1 // AI &amp; MACHINE LEARNING</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#34D399">&#9658;</tspan> Machine Learning</text>
      <text x="180" y="0"><tspan fill="#34D399">&#9658;</tspan> Scikit-Learn</text>
      <text x="0" y="22"><tspan fill="#34D399">&#9658;</tspan> Knowledge Graphs</text>
      <text x="180" y="22"><tspan fill="#34D399">&#9658;</tspan> Node2Vec</text>
      <text x="0" y="44"><tspan fill="#34D399">&#9658;</tspan> Predictive Modeling</text>
      <text x="180" y="44"><tspan fill="#34D399">&#9658;</tspan> Feature Engineering</text>
    </g>
  </g>

  <!-- Block 2: Data Science -->
  <g transform="translate(430, 60)">
    <rect width="390" height="110" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="16" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#128202; BLOCK 2 // DATA SCIENCE</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9658;</tspan> EDA (Exploratory Data)</text>
      <text x="190" y="0"><tspan fill="#00F2FE">&#9658;</tspan> Statistical Analysis</text>
      <text x="0" y="22"><tspan fill="#00F2FE">&#9658;</tspan> Data Wrangling</text>
      <text x="190" y="22"><tspan fill="#00F2FE">&#9658;</tspan> Pandas</text>
      <text x="0" y="44"><tspan fill="#00F2FE">&#9658;</tspan> NumPy</text>
      <text x="190" y="44"><tspan fill="#00F2FE">&#9658;</tspan> Tableau</text>
    </g>
  </g>

  <!-- Block 3: Software Engineering -->
  <g transform="translate(30, 182)">
    <rect width="380" height="110" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="16" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9889; BLOCK 3 // SOFTWARE ENGINEERING</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Python</text>
      <text x="180" y="0"><tspan fill="#818CF8">&#9658;</tspan> FastAPI</text>
      <text x="0" y="22"><tspan fill="#818CF8">&#9658;</tspan> Flask</text>
      <text x="180" y="22"><tspan fill="#818CF8">&#9658;</tspan> React</text>
      <text x="0" y="44"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
      <text x="180" y="44"><tspan fill="#818CF8">&#9658;</tspan> Git / GitHub / OpenCV</text>
    </g>
  </g>

  <!-- Block 4: Database Systems -->
  <g transform="translate(430, 182)">
    <rect width="390" height="110" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="16" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#128452; BLOCK 4 // DATABASE SYSTEMS</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9658;</tspan> MySQL</text>
      <text x="190" y="0"><tspan fill="#F59E0B">&#9658;</tspan> SQLite</text>
      <text x="0" y="22"><tspan fill="#F59E0B">&#9658;</tspan> Database Design</text>
      <text x="190" y="22"><tspan fill="#F59E0B">&#9658;</tspan> Query Optimization</text>
      <text x="0" y="44"><tspan fill="#F59E0B">&#9658;</tspan> DBMS Architecture</text>
      <text x="190" y="44"><tspan fill="#F59E0B">&#9658;</tspan> Relational Modeling</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. SKILLS ARSENAL (assets/antigravity-skills.svg) - STRICT RESUME SKILLS
# -------------------------------------------------------------
skills_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="850" height="280">
  <defs>
    <linearGradient id="ags-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>
  </defs>

  <rect width="850" height="280" rx="14" fill="url(#ags-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">SKILLS ARSENAL // FLOATING ANTI-GRAVITY CAPSULES</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">RESUME VERIFIED &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 5 CATEGORY COLUMNS -->
  
  <!-- Languages -->
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

  <!-- AI & ML -->
  <g transform="translate(190, 60)">
    <rect width="168" height="200" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="14" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="800">02 // AI &amp; ML</text>
    <line x1="14" y1="32" x2="154" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(14, 52)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9670;</tspan> Machine Learning</text>
      <text x="0" y="24"><tspan fill="#00F2FE">&#9670;</tspan> Scikit-Learn</text>
      <text x="0" y="48"><tspan fill="#00F2FE">&#9670;</tspan> Predictive Models</text>
      <text x="0" y="72"><tspan fill="#00F2FE">&#9670;</tspan> Feature Engineering</text>
      <text x="0" y="96"><tspan fill="#00F2FE">&#9670;</tspan> Knowledge Graphs</text>
      <text x="0" y="120"><tspan fill="#00F2FE">&#9670;</tspan> Node2Vec</text>
    </g>
  </g>

  <!-- Data Science -->
  <g transform="translate(374, 60)">
    <rect width="154" height="200" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="14" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="10" font-weight="800">03 // DATA SCIENCE</text>
    <line x1="14" y1="32" x2="140" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(14, 52)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Data Science</text>
      <text x="0" y="24"><tspan fill="#818CF8">&#9658;</tspan> EDA</text>
      <text x="0" y="48"><tspan fill="#818CF8">&#9658;</tspan> Statistical Analysis</text>
      <text x="0" y="72"><tspan fill="#818CF8">&#9658;</tspan> Data Wrangling</text>
      <text x="0" y="96"><tspan fill="#818CF8">&#9658;</tspan> Pandas &amp; NumPy</text>
      <text x="0" y="120"><tspan fill="#818CF8">&#9658;</tspan> Tableau &amp; Excel</text>
    </g>
  </g>

  <!-- Development -->
  <g transform="translate(544, 60)">
    <rect width="134" height="200" rx="10" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
    <text x="12" y="24" fill="#C084FC" font-family="'Fira Code', monospace" font-size="10" font-weight="800">04 // DEVELOPMENT</text>
    <line x1="12" y1="32" x2="122" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(12, 52)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#C084FC">&#9654;</tspan> FastAPI</text>
      <text x="0" y="24"><tspan fill="#C084FC">&#9654;</tspan> Flask</text>
      <text x="0" y="48"><tspan fill="#C084FC">&#9654;</tspan> React</text>
      <text x="0" y="72"><tspan fill="#C084FC">&#9654;</tspan> REST APIs</text>
      <text x="0" y="96"><tspan fill="#C084FC">&#9654;</tspan> OpenCV</text>
      <text x="0" y="120"><tspan fill="#C084FC">&#9654;</tspan> Git &amp; GitHub</text>
    </g>
  </g>

  <!-- Databases & CS -->
  <g transform="translate(694, 60)">
    <rect width="126" height="200" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="10" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="9" font-weight="800">05 // DATABASES</text>
    <line x1="10" y1="32" x2="116" y2="32" stroke="#1E293B" stroke-width="1" />

    <g transform="translate(10, 52)" font-family="'Fira Code', monospace" font-size="9.5" fill="#CBD5E1">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9679;</tspan> MySQL</text>
      <text x="0" y="24"><tspan fill="#F59E0B">&#9679;</tspan> SQLite</text>
      <text x="0" y="48"><tspan fill="#F59E0B">&#9679;</tspan> DB Design</text>
      <text x="0" y="72"><tspan fill="#F59E0B">&#9679;</tspan> Query Tuning</text>
      <text x="0" y="96"><tspan fill="#F59E0B">&#9679;</tspan> DBMS</text>
      <text x="0" y="120"><tspan fill="#F59E0B">&#9679;</tspan> Algorithms</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. EDUCATION & CGPA (assets/antigravity-education.svg)
# -------------------------------------------------------------
education_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 170" width="850" height="170">
  <defs>
    <linearGradient id="age-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#080D1F" />
    </linearGradient>
  </defs>

  <rect width="850" height="170" rx="14" fill="url(#age-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">EDUCATION // ACADEMIC INTELLIGENCE MODULE</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">BMSCE BENGALURU &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Degree info -->
  <g transform="translate(36, 68)">
    <text x="0" y="18" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="800">
      Bachelor of Engineering (B.E.) in Artificial Intelligence &amp; Data Science
    </text>
    <text x="0" y="44" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="12" font-weight="600">
      BMS College of Engineering (BMSCE) &#8226; Bengaluru, Karnataka, India
    </text>
    <text x="0" y="68" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="11">
      Specialization: Machine Learning, Knowledge Graphs, Data Science, Relational Database Architecture
    </text>
  </g>

  <!-- CGPA Badge on Right -->
  <g transform="translate(680, 58)">
    <rect width="130" height="85" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1.2" />
    <text x="65" y="24" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="middle">ACADEMIC CGPA</text>
    <text x="65" y="58" fill="#34D399" font-family="'Fira Code', monospace" font-size="28" font-weight="800" text-anchor="middle">9.37</text>
    <text x="65" y="74" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="8" font-weight="700" text-anchor="middle">TOP STANDING</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 7. CERTIFICATION VAULT (assets/antigravity-certifications.svg)
# -------------------------------------------------------------
certifications_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 170" width="850" height="170">
  <defs>
    <linearGradient id="agc-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#080D1F" />
    </linearGradient>
  </defs>

  <rect width="850" height="170" rx="14" fill="url(#agc-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#818CF8" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">CERTIFICATIONS // FLOATING CERTIFICATION VAULT</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">4 VERIFIED CREDENTIALS &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 4 Vault Badges -->
  <g transform="translate(30, 60)" font-family="'Fira Code', monospace">
    <!-- 1 -->
    <g transform="translate(0, 0)">
      <rect width="188" height="85" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="12" y="24" fill="#38BDF8" font-size="9" font-weight="800">&#128737; NUTANIX CLOUD</text>
      <text x="12" y="44" fill="#F8FAFC" font-size="9.5" font-weight="700">Hybrid Cloud</text>
      <text x="12" y="58" fill="#F8FAFC" font-size="9.5" font-weight="700">Certified Pro</text>
      <text x="12" y="74" fill="#34D399" font-size="8.5">Nutanix Cloud</text>
    </g>

    <!-- 2 -->
    <g transform="translate(204, 0)">
      <rect width="188" height="85" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="12" y="24" fill="#34D399" font-size="9" font-weight="800">&#128737; ORACLE SQL</text>
      <text x="12" y="44" fill="#F8FAFC" font-size="9.5" font-weight="700">Oracle SQL</text>
      <text x="12" y="58" fill="#F8FAFC" font-size="9.5" font-weight="700">Certification</text>
      <text x="12" y="74" fill="#00F2FE" font-size="8.5">Oracle Academy</text>
    </g>

    <!-- 3 -->
    <g transform="translate(408, 0)">
      <rect width="188" height="85" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="12" y="24" fill="#C084FC" font-size="9" font-weight="800">&#128737; NPTEL ETHICS</text>
      <text x="12" y="44" fill="#F8FAFC" font-size="9.5" font-weight="700">Ethics in Engg</text>
      <text x="12" y="58" fill="#F8FAFC" font-size="9.5" font-weight="700">Practice</text>
      <text x="12" y="74" fill="#C084FC" font-size="8.5">IIT / NPTEL India</text>
    </g>

    <!-- 4 -->
    <g transform="translate(612, 0)">
      <rect width="178" height="85" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="12" y="24" fill="#F59E0B" font-size="9" font-weight="800">&#128737; C PROGRAMMING</text>
      <text x="12" y="44" fill="#F8FAFC" font-size="9.5" font-weight="700">C Programming</text>
      <text x="12" y="58" fill="#F8FAFC" font-size="9.5" font-weight="700">Certification</text>
      <text x="12" y="74" fill="#F59E0B" font-size="8.5">Foundations</text>
    </g>
  </g>
</svg>'''

files = [
    ("antigravity-hero.svg", hero_svg),
    ("antigravity-terminal.svg", terminal_svg),
    ("antigravity-about.svg", about_svg),
    ("antigravity-matrix.svg", matrix_svg),
    ("antigravity-skills.svg", skills_svg),
    ("antigravity-education.svg", education_svg),
    ("antigravity-certifications.svg", certifications_svg),
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

print("All Anti-Gravity Profile SVG assets generated successfully!")
