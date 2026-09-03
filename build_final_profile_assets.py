import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO SECTION (assets/hero-final.svg)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="fin-hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816">
        <animate attributeName="stop-color" values="#050816; #070B1F; #0A1028; #050816" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#070B1F">
        <animate attributeName="stop-color" values="#070B1F; #0E122C; #06152B; #070B1F" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#0A1028">
        <animate attributeName="stop-color" values="#0A1028; #050816; #070B1F; #0A1028" dur="12s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <linearGradient id="fin-hero-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="fin-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Frame -->
  <rect width="850" height="250" rx="16" fill="url(#fin-hero-bg)" stroke="url(#fin-hero-border)" stroke-width="1.8" />
  <rect x="0" y="0" width="850" height="4.5" rx="2.25" fill="url(#fin-hero-border)" filter="url(#fin-glow)" />

  <!-- Top Bar -->
  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">AI_OPERATING_SYSTEM // KATHYAYINI_PRABHU // KERNEL v6.0</text>
    <text x="800" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS.STATUS: ONLINE &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- Left Hero Details -->
  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#fin-glow)" />

    <text x="20" y="34" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="62" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="14.5" font-weight="700">Artificial Intelligence &amp; Data Science</text>
    
    <text x="20" y="86" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Third-Year AI &amp; Data Science Student &#8226; BMS College of Engineering</text>
    <text x="20" y="104" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5">Building Intelligent Systems Through Data</text>

    <!-- 4 Skill Pills: AI, ML, Data Science, SQL -->
    <g transform="translate(20, 122)">
      <rect width="112" height="24" rx="12" fill="#161B22" stroke="#00F2FE" stroke-width="1" />
      <text x="56" y="16" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">ARTIFICIAL INTEL</text>

      <rect x="122" width="125" height="24" rx="12" fill="#161B22" stroke="#34D399" stroke-width="1" />
      <text x="184.5" y="16" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">MACHINE LEARNING</text>

      <rect x="257" width="105" height="24" rx="12" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
      <text x="309.5" y="16" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">DATA SCIENCE</text>

      <rect x="372" width="118" height="24" rx="12" fill="#161B22" stroke="#F59E0B" stroke-width="1" />
      <text x="431" y="16" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SQL &amp; DATABASES</text>
    </g>
  </g>

  <!-- Right Orbital Representation (AI, ML, Data Science, SQL) -->
  <g transform="translate(560, 50)">
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#fin-glow)" />

    <circle cx="127" cy="88" r="22" fill="#161B22" stroke="#00F2FE" stroke-width="1.5" />
    <text x="127" y="92" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">AI_CORE</text>

    <circle cx="127" cy="88" r="62" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="4 4" />
    <circle cx="127" cy="88" r="62" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="0 127 88" to="360 127 88" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- 4 Orbiting Domain Nodes -->
    <g transform="translate(127, 26)">
      <circle cx="0" cy="0" r="14" fill="#0D1117" stroke="#00F2FE" stroke-width="1.2" />
      <text x="0" y="3.5" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="7.5" font-weight="800" text-anchor="middle">AI</text>
    </g>

    <g transform="translate(189, 88)">
      <circle cx="0" cy="0" r="14" fill="#0D1117" stroke="#34D399" stroke-width="1.2" />
      <text x="0" y="3.5" fill="#34D399" font-family="'Fira Code', monospace" font-size="7.5" font-weight="800" text-anchor="middle">ML</text>
    </g>

    <g transform="translate(127, 150)">
      <circle cx="0" cy="0" r="14" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" />
      <text x="0" y="3.5" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="7.5" font-weight="800" text-anchor="middle">DS</text>
    </g>

    <g transform="translate(65, 88)">
      <circle cx="0" cy="0" r="14" fill="#0D1117" stroke="#F59E0B" stroke-width="1.2" />
      <text x="0" y="3.5" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="7.5" font-weight="800" text-anchor="middle">SQL</text>
    </g>

    <text x="127.5" y="170" fill="#34D399" font-family="'Fira Code', monospace" font-size="8" font-weight="700" text-anchor="middle">ORBITAL SYNCHRONY: ACTIVE</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. NEURAL BLUEPRINT (assets/neural-blueprint-final.svg)
# -------------------------------------------------------------
neural_blueprint_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="fin-nb-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>

    <filter id="fin-nb-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#fin-nb-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Animated Neural Network Lines -->
  <g stroke="#38BDF8" stroke-width="0.8" opacity="0.25">
    <line x1="20" y1="180" x2="200" y2="120">
      <animate attributeName="opacity" values="0.1;0.4;0.1" dur="4s" repeatCount="indefinite" />
    </line>
    <line x1="200" y1="120" x2="400" y2="200">
      <animate attributeName="opacity" values="0.4;0.1;0.4" dur="5s" repeatCount="indefinite" />
    </line>
    <line x1="400" y1="200" x2="650" y2="90">
      <animate attributeName="opacity" values="0.1;0.5;0.1" dur="3.5s" repeatCount="indefinite" />
    </line>
    <line x1="650" y1="90" x2="820" y2="160">
      <animate attributeName="opacity" values="0.5;0.2;0.5" dur="4.5s" repeatCount="indefinite" />
    </line>
  </g>

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">NEURAL BLUEPRINT // TRANSFORMING DATA INTO INTELLIGENT SYSTEMS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS_PROFILE &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Narrative Content -->
  <g transform="translate(36, 68)">
    <text x="0" y="18" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="600">
      I am a Third-Year Artificial Intelligence &amp; Data Science student passionate about designing intelligent systems that solve real-world problems.
    </text>

    <text x="0" y="44" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500">
      My interests span Machine Learning, Data Analytics, SQL Engineering, Backend Development and AI Applications.
    </text>

    <text x="0" y="70" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13">
      I enjoy transforming raw data into actionable intelligence through predictive modeling, software engineering and analytical thinking.
    </text>

    <!-- 5 Focus Tags -->
    <g transform="translate(0, 98)" font-family="'Fira Code', monospace" font-size="9.5">
      <rect width="145" height="26" rx="13" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="72.5" y="17" fill="#00F2FE" font-weight="700" text-anchor="middle">&#9670; Machine Learning</text>

      <rect x="155" width="135" height="26" rx="13" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="222.5" y="17" fill="#34D399" font-weight="700" text-anchor="middle">&#9670; Data Analytics</text>

      <rect x="300" width="160" height="26" rx="13" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="380" y="17" fill="#F59E0B" font-weight="700" text-anchor="middle">&#9670; SQL Engineering</text>

      <rect x="470" width="165" height="26" rx="13" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="552.5" y="17" fill="#818CF8" font-weight="700" text-anchor="middle">&#9670; Backend Development</text>

      <rect x="645" width="135" height="26" rx="13" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="712.5" y="17" fill="#C084FC" font-weight="700" text-anchor="middle">&#9670; AI Applications</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. INTELLIGENCE DOMAINS (assets/intelligence-domains-final.svg)
# -------------------------------------------------------------
domains_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 300" width="850" height="300">
  <defs>
    <linearGradient id="fin-id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#070B1F" />
    </linearGradient>

    <filter id="fin-id-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="300" rx="14" fill="url(#fin-id-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">INTELLIGENCE DOMAINS // CORE DISCIPLINES</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">4 DOMAINS &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 4 Clean Domain Panels (No Card 1/2 numbering, No emojis) -->
  
  <!-- Panel 1: Artificial Intelligence -->
  <g transform="translate(30, 60)">
    <rect width="380" height="105" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="16" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">ARTIFICIAL INTELLIGENCE</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#34D399">&#9658;</tspan> Machine Learning</text>
      <text x="180" y="0"><tspan fill="#34D399">&#9658;</tspan> Predictive Modeling</text>
      <text x="0" y="24"><tspan fill="#34D399">&#9658;</tspan> Feature Engineering</text>
      <text x="180" y="24"><tspan fill="#34D399">&#9658;</tspan> Scikit-Learn</text>
    </g>
  </g>

  <!-- Panel 2: Data Analytics -->
  <g transform="translate(430, 60)">
    <rect width="390" height="105" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="16" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="800">DATA ANALYTICS</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9658;</tspan> Data Analysis</text>
      <text x="180" y="0"><tspan fill="#00F2FE">&#9658;</tspan> EDA (Exploratory)</text>
      <text x="0" y="24"><tspan fill="#00F2FE">&#9658;</tspan> Statistical Analysis</text>
      <text x="180" y="24"><tspan fill="#00F2FE">&#9658;</tspan> Pandas &amp; NumPy</text>
    </g>
  </g>

  <!-- Panel 3: Software Engineering -->
  <g transform="translate(30, 178)">
    <rect width="380" height="105" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="16" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">SOFTWARE ENGINEERING</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Python</text>
      <text x="180" y="0"><tspan fill="#818CF8">&#9658;</tspan> FastAPI</text>
      <text x="0" y="24"><tspan fill="#818CF8">&#9658;</tspan> Flask</text>
      <text x="180" y="24"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
    </g>
  </g>

  <!-- Panel 4: Database Engineering -->
  <g transform="translate(430, 178)">
    <rect width="390" height="105" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="16" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="11" font-weight="800">DATABASE ENGINEERING</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 50)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9658;</tspan> SQL</text>
      <text x="180" y="0"><tspan fill="#F59E0B">&#9658;</tspan> MySQL</text>
      <text x="0" y="24"><tspan fill="#F59E0B">&#9658;</tspan> SQLite</text>
      <text x="180" y="24"><tspan fill="#F59E0B">&#9658;</tspan> Query Optimization</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. TECHNOLOGY STACK (FLOATING CAPSULES) (assets/technology-stack-final.svg)
# -------------------------------------------------------------
tech_stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="fin-ts-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#fin-ts-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">TECHNOLOGY STACK // FLOATING CAPSULES</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">VERIFIED &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 6 Floating Capsule Groups -->
  
  <!-- Group 1: Languages -->
  <g transform="translate(36, 62)" font-family="'Fira Code', monospace" font-size="9.5">
    <text x="0" y="12" fill="#94A3B8" font-size="10" font-weight="700">LANGUAGES:</text>
    <g transform="translate(100, 0)">
      <rect width="65" height="20" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="32.5" y="13.5" fill="#38BDF8" font-weight="700" text-anchor="middle">Python</text>

      <rect x="73" width="50" height="20" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="98" y="13.5" fill="#38BDF8" font-weight="700" text-anchor="middle">SQL</text>

      <rect x="131" width="40" height="20" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="151" y="13.5" fill="#38BDF8" font-weight="700" text-anchor="middle">C</text>
    </g>
  </g>

  <!-- Group 2: Data Science -->
  <g transform="translate(36, 92)" font-family="'Fira Code', monospace" font-size="9.5">
    <text x="0" y="12" fill="#94A3B8" font-size="10" font-weight="700">DATA SCIENCE:</text>
    <g transform="translate(115, 0)">
      <rect width="65" height="20" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="32.5" y="13.5" fill="#34D399" font-weight="700" text-anchor="middle">Pandas</text>

      <rect x="73" width="60" height="20" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="103" y="13.5" fill="#34D399" font-weight="700" text-anchor="middle">NumPy</text>

      <rect x="141" width="68" height="20" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="175" y="13.5" fill="#34D399" font-weight="700" text-anchor="middle">Tableau</text>

      <rect x="217" width="50" height="20" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="242" y="13.5" fill="#34D399" font-weight="700" text-anchor="middle">EDA</text>

      <rect x="275" width="85" height="20" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="317.5" y="13.5" fill="#34D399" font-weight="700" text-anchor="middle">Statistics</text>
    </g>
  </g>

  <!-- Group 3: Machine Learning -->
  <g transform="translate(36, 122)" font-family="'Fira Code', monospace" font-size="9.5">
    <text x="0" y="12" fill="#94A3B8" font-size="10" font-weight="700">MACHINE LEARNING:</text>
    <g transform="translate(145, 0)">
      <rect width="125" height="20" rx="10" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="62.5" y="13.5" fill="#00F2FE" font-weight="700" text-anchor="middle">Machine Learning</text>

      <rect x="133" width="95" height="20" rx="10" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="180.5" y="13.5" fill="#00F2FE" font-weight="700" text-anchor="middle">Scikit-Learn</text>

      <rect x="236" width="135" height="20" rx="10" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="303.5" y="13.5" fill="#00F2FE" font-weight="700" text-anchor="middle">Predictive Modeling</text>

      <rect x="379" width="145" height="20" rx="10" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="451.5" y="13.5" fill="#00F2FE" font-weight="700" text-anchor="middle">Feature Engineering</text>
    </g>
  </g>

  <!-- Group 4: Backend -->
  <g transform="translate(36, 152)" font-family="'Fira Code', monospace" font-size="9.5">
    <text x="0" y="12" fill="#94A3B8" font-size="10" font-weight="700">BACKEND:</text>
    <g transform="translate(80, 0)">
      <rect width="68" height="20" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="34" y="13.5" fill="#818CF8" font-weight="700" text-anchor="middle">FastAPI</text>

      <rect x="76" width="55" height="20" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="103.5" y="13.5" fill="#818CF8" font-weight="700" text-anchor="middle">Flask</text>

      <rect x="139" width="80" height="20" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="179" y="13.5" fill="#818CF8" font-weight="700" text-anchor="middle">REST APIs</text>
    </g>
  </g>

  <!-- Group 5: Tools -->
  <g transform="translate(36, 182)" font-family="'Fira Code', monospace" font-size="9.5">
    <text x="0" y="12" fill="#94A3B8" font-size="10" font-weight="700">TOOLS:</text>
    <g transform="translate(65, 0)">
      <rect width="45" height="20" rx="10" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="22.5" y="13.5" fill="#C084FC" font-weight="700" text-anchor="middle">Git</text>

      <rect x="53" width="62" height="20" rx="10" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="84" y="13.5" fill="#C084FC" font-weight="700" text-anchor="middle">GitHub</text>

      <rect x="123" width="55" height="20" rx="10" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="150.5" y="13.5" fill="#C084FC" font-weight="700" text-anchor="middle">React</text>
    </g>
  </g>

  <!-- Group 6: Databases -->
  <g transform="translate(36, 212)" font-family="'Fira Code', monospace" font-size="9.5">
    <text x="0" y="12" fill="#94A3B8" font-size="10" font-weight="700">DATABASES:</text>
    <g transform="translate(95, 0)">
      <rect width="60" height="20" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="30" y="13.5" fill="#F59E0B" font-weight="700" text-anchor="middle">MySQL</text>

      <rect x="68" width="65" height="20" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="100.5" y="13.5" fill="#F59E0B" font-weight="700" text-anchor="middle">SQLite</text>

      <rect x="141" width="50" height="20" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="166" y="13.5" fill="#F59E0B" font-weight="700" text-anchor="middle">SQL</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. INTELLIGENCE LAB (UNIFIED AUTOMATIC ROTATING SHOWCASE) (assets/intelligence-lab-final.svg)
# -------------------------------------------------------------
lab_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 260" width="850" height="260">
  <defs>
    <linearGradient id="fin-il-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#080D1F" />
    </linearGradient>

    <filter id="fin-il-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="260" rx="14" fill="url(#fin-il-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">INTELLIGENCE LAB // AUTOMATED HORIZONTAL SHOWCASE</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">4 CORE SYSTEMS &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Showcase Sliding Container -->
  <g transform="translate(30, 58)">
    <rect width="790" height="180" rx="12" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#fin-il-glow)" />

    <!-- SLIDE 1: BioWeaver (Visible 0-5s) -->
    <g opacity="1">
      <animate attributeName="opacity" values="1;1;0;0;0;0;0;0;1" keyTimes="0;0.22;0.25;0.47;0.50;0.72;0.75;0.97;1" dur="18s" repeatCount="indefinite" />
      
      <!-- DNA Helix Animation -->
      <g transform="translate(700, 80)">
        <circle cx="0" cy="0" r="32" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
        <path d="M -16 -10 Q 0 0 16 -10 M -16 10 Q 0 0 16 10" stroke="#00F2FE" stroke-width="2.5" fill="none">
          <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="4s" repeatCount="indefinite" />
        </path>
      </g>

      <g transform="translate(24, 28)">
        <rect width="80" height="20" rx="10" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
        <text x="40" y="13.5" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SYSTEM 01</text>

        <text x="0" y="46" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800">BioWeaver</text>
        <text x="0" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11.5" font-weight="700">Biomedical AI &amp; Discovery Platform</text>
        <text x="0" y="90" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">
          AI discovery system predicting gene-disease interactions with explainable research hypotheses.
        </text>

        <!-- Tech Stack -->
        <g transform="translate(0, 106)" font-family="'Fira Code', monospace" font-size="9">
          <text x="0" y="14" fill="#64748B">STACK:</text>
          <rect x="48" width="60" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="78" y="12.5" fill="#38BDF8" text-anchor="middle">Python</text>
          <rect x="114" width="52" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="140" y="12.5" fill="#38BDF8" text-anchor="middle">Flask</text>
          <rect x="172" width="52" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="198" y="12.5" fill="#38BDF8" text-anchor="middle">React</text>
          <rect x="230" width="88" height="18" rx="4" fill="#161B22" stroke="#38BDF8" />
          <text x="274" y="12.5" fill="#00F2FE" font-weight="700" text-anchor="middle">Scikit-Learn</text>
        </g>
      </g>
    </g>

    <!-- SLIDE 2: Maritime Risk AI (Visible 5-9s) -->
    <g opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0;0;0;0;0" keyTimes="0;0.22;0.25;0.47;0.50;0.72;0.75;0.97;1" dur="18s" repeatCount="indefinite" />
      
      <!-- Ocean & Moving Ship Animation -->
      <g transform="translate(700, 80)">
        <circle cx="0" cy="0" r="32" fill="#161B22" stroke="#34D399" stroke-width="1" />
        <line x1="-22" y1="8" x2="22" y2="8" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3" />
        <polygon points="-10,5 10,5 5,-5 -5,-5" fill="#34D399">
          <animate attributeName="transform" type="translate" values="-6,0; 6,0; -6,0" dur="2.5s" repeatCount="indefinite" />
        </polygon>
      </g>

      <g transform="translate(24, 28)">
        <rect width="80" height="20" rx="10" fill="#161B22" stroke="#34D399" stroke-width="1" />
        <text x="40" y="13.5" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SYSTEM 02</text>

        <text x="0" y="46" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800">Maritime Risk AI</text>
        <text x="0" y="68" fill="#34D399" font-family="'Fira Code', monospace" font-size="11.5" font-weight="700">Predictive Supply Chain Risk Analytics</text>
        <text x="0" y="90" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">
          Forecasts vessel route risks, seasonal disruptions, and container port congestion queues.
        </text>

        <g transform="translate(0, 106)" font-family="'Fira Code', monospace" font-size="9">
          <text x="0" y="14" fill="#64748B">STACK:</text>
          <rect x="48" width="60" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="78" y="12.5" fill="#34D399" text-anchor="middle">Python</text>
          <rect x="114" width="52" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="140" y="12.5" fill="#34D399" text-anchor="middle">Flask</text>
          <rect x="172" width="52" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="198" y="12.5" fill="#34D399" text-anchor="middle">React</text>
          <rect x="230" width="105" height="18" rx="4" fill="#161B22" stroke="#34D399" />
          <text x="282.5" y="12.5" fill="#34D399" font-weight="700" text-anchor="middle">Predictive ML</text>
        </g>
      </g>
    </g>

    <!-- SLIDE 3: Smart Attendance (Visible 9-13s) -->
    <g opacity="0">
      <animate attributeName="opacity" values="0;0;0;0;1;1;0;0;0" keyTimes="0;0.22;0.25;0.47;0.50;0.72;0.75;0.97;1" dur="18s" repeatCount="indefinite" />
      
      <!-- CV Scan Grid Animation -->
      <g transform="translate(700, 80)">
        <circle cx="0" cy="0" r="32" fill="#161B22" stroke="#818CF8" stroke-width="1" />
        <rect x="-14" y="-14" width="10" height="10" fill="#818CF8">
          <animate attributeName="opacity" values="0.3;1;0.3" dur="1.5s" repeatCount="indefinite" />
        </rect>
        <rect x="4" y="-14" width="10" height="10" fill="#00F2FE">
          <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite" />
        </rect>
        <rect x="-14" y="4" width="10" height="10" fill="#34D399">
          <animate attributeName="opacity" values="0.5;1;0.5" dur="1.2s" repeatCount="indefinite" />
        </rect>
        <rect x="4" y="4" width="10" height="10" fill="#C084FC">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.4s" repeatCount="indefinite" />
        </rect>
      </g>

      <g transform="translate(24, 28)">
        <rect width="80" height="20" rx="10" fill="#161B22" stroke="#818CF8" stroke-width="1" />
        <text x="40" y="13.5" fill="#818CF8" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SYSTEM 03</text>

        <text x="0" y="46" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800">Smart Attendance &amp; TT</text>
        <text x="0" y="68" fill="#818CF8" font-family="'Fira Code', monospace" font-size="11.5" font-weight="700">Computer Vision + Scheduling System</text>
        <text x="0" y="90" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">
          Automated attendance pipeline with constraint solver for collision-free schedule optimization.
        </text>

        <g transform="translate(0, 106)" font-family="'Fira Code', monospace" font-size="9">
          <text x="0" y="14" fill="#64748B">STACK:</text>
          <rect x="48" width="60" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="78" y="12.5" fill="#818CF8" text-anchor="middle">Python</text>
          <rect x="114" width="65" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="146.5" y="12.5" fill="#818CF8" text-anchor="middle">OpenCV</text>
          <rect x="185" width="125" height="18" rx="4" fill="#161B22" stroke="#818CF8" />
          <text x="247.5" y="12.5" fill="#818CF8" font-weight="700" text-anchor="middle">Constraint Solver</text>
        </g>
      </g>
    </g>

    <!-- SLIDE 4: RoadWatch (Visible 13-18s) -->
    <g opacity="0">
      <animate attributeName="opacity" values="0;0;0;0;0;0;1;1;0" keyTimes="0;0.22;0.25;0.47;0.50;0.72;0.75;0.97;1" dur="18s" repeatCount="indefinite" />
      
      <!-- Satellite Orbit Animation -->
      <g transform="translate(700, 80)">
        <circle cx="0" cy="0" r="32" fill="#161B22" stroke="#F59E0B" stroke-width="1" />
        <ellipse cx="0" cy="0" rx="24" ry="10" fill="none" stroke="#F59E0B" stroke-width="1.2" stroke-dasharray="3 3">
          <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" repeatCount="indefinite" />
        </ellipse>
        <circle cx="16" cy="0" r="3.5" fill="#00F2FE">
          <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" repeatCount="indefinite" />
        </circle>
      </g>

      <g transform="translate(24, 28)">
        <rect width="80" height="20" rx="10" fill="#161B22" stroke="#F59E0B" stroke-width="1" />
        <text x="40" y="13.5" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="8.5" font-weight="800" text-anchor="middle">SYSTEM 04</text>

        <text x="0" y="46" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800">RoadWatch</text>
        <text x="0" y="68" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="11.5" font-weight="700">Infrastructure Risk Intelligence</text>
        <text x="0" y="90" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">
          Geospatial hazard telemetry, anomaly classification, and infrastructure condition analytics.
        </text>

        <g transform="translate(0, 106)" font-family="'Fira Code', monospace" font-size="9">
          <text x="0" y="14" fill="#64748B">STACK:</text>
          <rect x="48" width="60" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="78" y="12.5" fill="#F59E0B" text-anchor="middle">Python</text>
          <rect x="114" width="85" height="18" rx="4" fill="#161B22" stroke="#334155" />
          <text x="156.5" y="12.5" fill="#F59E0B" text-anchor="middle">GIS Analytics</text>
          <rect x="205" width="92" height="18" rx="4" fill="#161B22" stroke="#F59E0B" />
          <text x="251" y="12.5" fill="#F59E0B" font-weight="700" text-anchor="middle">Data Science</text>
        </g>
      </g>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. GITHUB METRICS (REALISTIC REPOS & FOCUS) (assets/github-metrics-final.svg)
# -------------------------------------------------------------
github_metrics_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 140" width="850" height="140">
  <defs>
    <linearGradient id="fin-gm-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>
  </defs>

  <rect width="850" height="140" rx="14" fill="url(#fin-gm-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 20)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="12" font-weight="800" letter-spacing="1">GITHUB TELEMETRY // REALTIME REPOSITORY ACTIVITY</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">LIVE TELEMETRY &#9679;</text>
  </g>
  <line x1="30" y1="38" x2="820" y2="38" stroke="#1E293B" stroke-width="1" />

  <!-- 4 Realistic Telemetry Cards -->
  <g transform="translate(30, 52)" font-family="'Fira Code', monospace">
    <!-- 1 -->
    <g transform="translate(0, 0)">
      <rect width="188" height="68" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="14" y="24" fill="#38BDF8" font-size="18" font-weight="800">6</text>
      <text x="14" y="42" fill="#F8FAFC" font-size="10" font-weight="700">Active Repositories</text>
      <text x="14" y="56" fill="#94A3B8" font-size="8.5">Public Codebases</text>
    </g>

    <!-- 2 -->
    <g transform="translate(204, 0)">
      <rect width="188" height="68" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="14" y="24" fill="#34D399" font-size="13" font-weight="800">MACHINE LEARNING</text>
      <text x="14" y="42" fill="#F8FAFC" font-size="10" font-weight="700">Primary Core Focus</text>
      <text x="14" y="56" fill="#94A3B8" font-size="8.5">Predictive Models</text>
    </g>

    <!-- 3 -->
    <g transform="translate(408, 0)">
      <rect width="188" height="68" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="14" y="24" fill="#818CF8" font-size="13" font-weight="800">DATA SCIENCE</text>
      <text x="14" y="42" fill="#F8FAFC" font-size="10" font-weight="700">Analytics &amp; EDA</text>
      <text x="14" y="56" fill="#94A3B8" font-size="8.5">Statistical Pipelines</text>
    </g>

    <!-- 4 -->
    <g transform="translate(612, 0)">
      <rect width="178" height="68" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="14" y="24" fill="#F59E0B" font-size="13" font-weight="800">BACKEND &amp; SQL</text>
      <text x="14" y="42" fill="#F8FAFC" font-size="10" font-weight="700">Software Systems</text>
      <text x="14" y="56" fill="#94A3B8" font-size="8.5">FastAPI &amp; MySQL</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 7. FOOTER (assets/footer-final.svg)
# -------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 110" width="850" height="110">
  <defs>
    <linearGradient id="fin-ft-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
  </defs>

  <rect width="850" height="110" rx="12" fill="#050816" stroke="#1E293B" stroke-width="1.2" />

  <line x1="40" y1="24" x2="810" y2="24" stroke="url(#fin-ft-line)" stroke-width="1.5" />

  <text x="425" y="50" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">
    AI &#8226; DATA &#8226; SYSTEMS &#8226; INTELLIGENCE
  </text>

  <text x="425" y="74" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="11" font-weight="600" letter-spacing="1" text-anchor="middle">
    "Building Tomorrow's Intelligent Systems"
  </text>

  <line x1="40" y1="92" x2="810" y2="92" stroke="url(#fin-ft-line)" stroke-width="1.5" />
</svg>'''

files = [
    ("hero-final.svg", hero_svg),
    ("neural-blueprint-final.svg", neural_blueprint_svg),
    ("intelligence-domains-final.svg", domains_svg),
    ("technology-stack-final.svg", tech_stack_svg),
    ("intelligence-lab-final.svg", lab_svg),
    ("github-metrics-final.svg", github_metrics_svg),
    ("footer-final.svg", footer_svg),
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

print("All Final Anti-Gravity Profile SVG assets generated successfully!")
