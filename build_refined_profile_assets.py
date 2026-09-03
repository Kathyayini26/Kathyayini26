import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO SECTION (assets/hero-os-refined.svg)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="ref-hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
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

    <linearGradient id="ref-hero-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="ref-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="250" rx="16" fill="url(#ref-hero-bg)" stroke="url(#ref-hero-border)" stroke-width="1.8" />
  <rect x="0" y="0" width="850" height="4.5" rx="2.25" fill="url(#ref-hero-border)" filter="url(#ref-glow)" />

  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">AI_OS_DASHBOARD // KATHYAYINI_PRABHU // KERNEL v5.0</text>
    <text x="800" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS.STATUS: ONLINE &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#ref-glow)" />

    <text x="20" y="38" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="15" font-weight="700">AI &amp; Data Science Engineer</text>
    
    <text x="20" y="96" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">BMS College of Engineering (BMSCE) &#8226; CGPA: 9.37</text>

    <!-- 4 Skill Pills: AI, ML, Data Science, SQL & Database Systems -->
    <g transform="translate(20, 118)">
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
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#ref-glow)" />

    <circle cx="127" cy="88" r="22" fill="#161B22" stroke="#00F2FE" stroke-width="1.5" />
    <text x="127" y="92" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">AI_CORE</text>

    <circle cx="127" cy="88" r="62" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="4 4" />
    <circle cx="127" cy="88" r="62" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="0 127 88" to="360 127 88" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- 4 Orbiting Domain Nodes: AI (Top), ML (Right), Data Science (Bottom), SQL (Left) -->
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
# 2. TERMINAL (assets/terminal-refined.svg)
# -------------------------------------------------------------
terminal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 260" width="850" height="260">
  <defs>
    <linearGradient id="ref-term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#080D1F" />
    </linearGradient>

    <linearGradient id="ref-term-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="260" rx="14" fill="url(#ref-term-bg)" stroke="url(#ref-term-border)" stroke-width="1.5" />

  <g transform="translate(18, 16)">
    <circle cx="8" cy="6" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="6" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="6" r="4.5" fill="#27C93F" />
    <text x="60" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">kathyayini@ai-command-center: ~ (zsh)</text>
    <text x="800" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">&#9889; SESSION_ACTIVE</text>
  </g>
  <line x1="15" y1="36" x2="835" y2="36" stroke="#1E293B" stroke-width="1" />

  <g transform="translate(24, 52)" font-family="'Fira Code', monospace" font-size="10.5" font-weight="500">
    <text x="0" y="14">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">whoami</tspan>
    </text>
    <text x="18" y="30" fill="#34D399" font-weight="700">&#8594; Kathyayini Prabhu | AI &amp; Data Science Engineer @ BMSCE</text>

    <text x="0" y="52">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">specialization</tspan>
    </text>
    <text x="18" y="68" fill="#CBD5E1">
      <tspan fill="#00F2FE">&#9670; Artificial Intelligence</tspan>   
      <tspan fill="#34D399">&#9670; Machine Learning</tspan>   
      <tspan fill="#818CF8">&#9670; Data Science</tspan>   
      <tspan fill="#F59E0B">&#9670; SQL &amp; Database Systems</tspan>
    </text>

    <text x="0" y="90">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">currently_building</tspan>
    </text>
    <text x="18" y="106" fill="#CBD5E1">
      <tspan fill="#38BDF8">&#9654; Predictive Analytics</tspan>   
      <tspan fill="#00F2FE">&#9654; AI Applications</tspan>   
      <tspan fill="#34D399">&#9654; Data Science Solutions</tspan>   
      <tspan fill="#C084FC">&#9654; Backend Systems</tspan>
    </text>

    <text x="0" y="128">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">mission</tspan>
    </text>
    <text x="18" y="144" fill="#F8FAFC" font-weight="700">&#10024; "Engineering Intelligence From Data"</text>

    <text x="0" y="166">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">status</tspan>
    </text>
    <text x="18" y="182" fill="#CBD5E1">
      <tspan fill="#34D399">&#9679; Learning</tspan>   
      <tspan fill="#00F2FE">&#9679; Building</tspan>   
      <tspan fill="#C084FC">&#9679; Innovating</tspan>
    </text>

    <text x="0" y="204">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#34D399">run --all-systems</tspan>
    </text>
    <rect x="185" y="193" width="7" height="13" fill="#00F2FE">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. NEURAL BLUEPRINT (assets/neural-blueprint.svg)
# -------------------------------------------------------------
neural_blueprint_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="nb-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>

    <filter id="nb-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#nb-bg)" stroke="#1E293B" stroke-width="1.5" />

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

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1"># NEURAL BLUEPRINT // TRANSFORMING DATA INTO INTELLIGENT SYSTEMS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS_PROFILE &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <g transform="translate(36, 68)">
    <text x="0" y="18" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700">
      I am an Artificial Intelligence &amp; Data Science student focused on building intelligent software systems
    </text>
    <text x="0" y="38" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700">
      through Machine Learning, Data Science, SQL, and backend engineering.
    </text>

    <text x="0" y="68" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">
      My work combines predictive modeling, analytical thinking, and software development to create practical solutions for real-world problems.
    </text>

    <g transform="translate(0, 96)" font-family="'Fira Code', monospace" font-size="9.5">
      <rect width="145" height="26" rx="13" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="72.5" y="17" fill="#00F2FE" font-weight="700" text-anchor="middle">&#9670; Machine Learning</text>

      <rect x="155" width="135" height="26" rx="13" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="222.5" y="17" fill="#34D399" font-weight="700" text-anchor="middle">&#9670; Data Analytics</text>

      <rect x="300" width="165" height="26" rx="13" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="382.5" y="17" fill="#F59E0B" font-weight="700" text-anchor="middle">&#9670; Database Engineering</text>

      <rect x="475" width="160" height="26" rx="13" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="555" y="17" fill="#818CF8" font-weight="700" text-anchor="middle">&#9670; Backend Development</text>

      <rect x="645" width="135" height="26" rx="13" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="712.5" y="17" fill="#C084FC" font-weight="700" text-anchor="middle">&#9670; AI Applications</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. ENGINEERING DOMAINS (assets/engineering-domains.svg)
# -------------------------------------------------------------
domains_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 310" width="850" height="310">
  <defs>
    <linearGradient id="ed-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#070B1F" />
    </linearGradient>

    <filter id="ed-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="310" rx="14" fill="url(#ed-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1"># ENGINEERING DOMAINS // CORE DISCIPLINES</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">4 CORE PILLARS &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Card 1: AI & ML -->
  <g transform="translate(30, 60)">
    <rect width="380" height="110" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="16" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#129504; CARD 1 // ARTIFICIAL INTEL &amp; ML</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 52)" font-family="'Fira Code', monospace" font-size="10.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#34D399">&#9658;</tspan> Machine Learning</text>
      <text x="180" y="0"><tspan fill="#34D399">&#9658;</tspan> Scikit-Learn</text>
      <text x="0" y="24"><tspan fill="#34D399">&#9658;</tspan> Predictive Modeling</text>
      <text x="180" y="24"><tspan fill="#34D399">&#9658;</tspan> Feature Engineering</text>
    </g>
  </g>

  <!-- Card 2: Data Science & Analytics -->
  <g transform="translate(430, 60)">
    <rect width="390" height="110" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="16" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#128202; CARD 2 // DATA SCIENCE &amp; ANALYTICS</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 52)" font-family="'Fira Code', monospace" font-size="10.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9658;</tspan> Data Analysis</text>
      <text x="180" y="0"><tspan fill="#00F2FE">&#9658;</tspan> Pandas &amp; NumPy</text>
      <text x="0" y="24"><tspan fill="#00F2FE">&#9658;</tspan> EDA (Exploratory)</text>
      <text x="180" y="24"><tspan fill="#00F2FE">&#9658;</tspan> Statistical Analysis</text>
    </g>
  </g>

  <!-- Card 3: Software Development -->
  <g transform="translate(30, 182)">
    <rect width="380" height="110" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="16" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#9881; CARD 3 // SOFTWARE DEVELOPMENT</text>
    <line x1="16" y1="32" x2="364" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 52)" font-family="'Fira Code', monospace" font-size="10.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Python</text>
      <text x="180" y="0"><tspan fill="#818CF8">&#9658;</tspan> FastAPI &amp; Flask</text>
      <text x="0" y="24"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
      <text x="180" y="24"><tspan fill="#818CF8">&#9658;</tspan> React &amp; Git / GitHub</text>
    </g>
  </g>

  <!-- Card 4: Database Systems -->
  <g transform="translate(430, 182)">
    <rect width="390" height="110" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="16" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="11" font-weight="800">&#128452; CARD 4 // DATABASE SYSTEMS</text>
    <line x1="16" y1="32" x2="374" y2="32" stroke="#1E293B" stroke-width="1" />
    
    <g transform="translate(16, 52)" font-family="'Fira Code', monospace" font-size="10.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9658;</tspan> SQL &amp; MySQL</text>
      <text x="180" y="0"><tspan fill="#F59E0B">&#9658;</tspan> SQLite</text>
      <text x="0" y="24"><tspan fill="#F59E0B">&#9658;</tspan> Database Design</text>
      <text x="180" y="24"><tspan fill="#F59E0B">&#9658;</tspan> Query Optimization</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. TECHNOLOGY STACK (assets/tech-stack-cards.svg)
# -------------------------------------------------------------
tech_stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="850" height="280">
  <defs>
    <linearGradient id="ts-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>
  </defs>

  <rect width="850" height="280" rx="14" fill="url(#ts-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1"># TECHNOLOGY STACK // 6 SPECIALIZED ARCHITECTURAL CARDS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">ACTIVE STACK &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Row 1 -->
  <g transform="translate(30, 60)">
    <rect width="250" height="95" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="12" y="20" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="10" font-weight="800">01 // PROGRAMMING LANGUAGES</text>
    <line x1="12" y1="26" x2="238" y2="26" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(12, 44)" font-family="'Fira Code', monospace" font-size="10" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#34D399">&#9654;</tspan> Python</text>
      <text x="80" y="0"><tspan fill="#34D399">&#9654;</tspan> SQL</text>
      <text x="145" y="0"><tspan fill="#34D399">&#9654;</tspan> C</text>
    </g>
  </g>

  <g transform="translate(295, 60)">
    <rect width="260" height="95" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="12" y="20" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="800">02 // DATA SCIENCE</text>
    <line x1="12" y1="26" x2="248" y2="26" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(12, 44)" font-family="'Fira Code', monospace" font-size="9.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9670;</tspan> Pandas &amp; NumPy</text>
      <text x="125" y="0"><tspan fill="#00F2FE">&#9670;</tspan> Tableau</text>
      <text x="0" y="20"><tspan fill="#00F2FE">&#9670;</tspan> EDA &amp; Statistical Analysis</text>
    </g>
  </g>

  <g transform="translate(570, 60)">
    <rect width="250" height="95" rx="8" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
    <text x="12" y="20" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="10" font-weight="800">03 // MACHINE LEARNING</text>
    <line x1="12" y1="26" x2="238" y2="26" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(12, 44)" font-family="'Fira Code', monospace" font-size="9.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#34D399">&#9658;</tspan> Machine Learning</text>
      <text x="125" y="0"><tspan fill="#34D399">&#9658;</tspan> Scikit-Learn</text>
      <text x="0" y="20"><tspan fill="#34D399">&#9658;</tspan> Predictive Models</text>
      <text x="125" y="20"><tspan fill="#34D399">&#9658;</tspan> Feature Eng.</text>
    </g>
  </g>

  <!-- Row 2 -->
  <g transform="translate(30, 168)">
    <rect width="250" height="95" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="12" y="20" fill="#818CF8" font-family="'Fira Code', monospace" font-size="10" font-weight="800">04 // BACKEND DEVELOPMENT</text>
    <line x1="12" y1="26" x2="238" y2="26" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(12, 44)" font-family="'Fira Code', monospace" font-size="9.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Flask</text>
      <text x="80" y="0"><tspan fill="#818CF8">&#9658;</tspan> FastAPI</text>
      <text x="155" y="0"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
    </g>
  </g>

  <g transform="translate(295, 168)">
    <rect width="260" height="95" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
    <text x="12" y="20" fill="#C084FC" font-family="'Fira Code', monospace" font-size="10" font-weight="800">05 // DEVELOPMENT TOOLS</text>
    <line x1="12" y1="26" x2="248" y2="26" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(12, 44)" font-family="'Fira Code', monospace" font-size="9.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#C084FC">&#9670;</tspan> Git</text>
      <text x="65" y="0"><tspan fill="#C084FC">&#9670;</tspan> GitHub</text>
      <text x="145" y="0"><tspan fill="#C084FC">&#9670;</tspan> React</text>
    </g>
  </g>

  <g transform="translate(570, 168)">
    <rect width="250" height="95" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="12" y="20" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="10" font-weight="800">06 // DATABASES</text>
    <line x1="12" y1="26" x2="238" y2="26" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(12, 44)" font-family="'Fira Code', monospace" font-size="9.5" fill="#E2E8F0">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9679;</tspan> MySQL</text>
      <text x="90" y="0"><tspan fill="#F59E0B">&#9679;</tspan> SQLite</text>
      <text x="0" y="20"><tspan fill="#F59E0B">&#9679;</tspan> DB Design &amp; Query Tuning</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. INNOVATION LAB (assets/innovation-lab.svg)
# -------------------------------------------------------------
innovation_lab_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 360" width="850" height="360">
  <defs>
    <linearGradient id="il-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#070B1F" />
    </linearGradient>

    <filter id="il-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="360" rx="14" fill="url(#il-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1"># INNOVATION LAB // SELECTED INTELLIGENT SYSTEMS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">ACTIVE BUILDS &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- Card 1: BioWeaver (Rotating DNA strand) -->
  <g transform="translate(30, 60)">
    <rect width="380" height="135" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    
    <g transform="translate(330, 40)">
      <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#38BDF8" stroke-width="1" />
      <path d="M -10 -6 Q 0 0 10 -6 M -10 6 Q 0 0 10 6" stroke="#00F2FE" stroke-width="1.5" fill="none">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="4s" repeatCount="indefinite" />
      </path>
    </g>

    <text x="16" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#129516; BioWeaver</text>
    <text x="16" y="42" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700">Biomedical AI &amp; Discovery Platform</text>
    <text x="16" y="62" fill="#94A3B8" font-family="-apple-system, sans-serif" font-size="10.5">
      AI platform predicting gene-disease interactions with explainable research hypotheses.
    </text>
    
    <g transform="translate(16, 92)" font-family="'Fira Code', monospace" font-size="8.5">
      <rect width="55" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="27.5" y="12.5" fill="#38BDF8" text-anchor="middle">Python</text>
      <rect x="62" width="48" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="86" y="12.5" fill="#38BDF8" text-anchor="middle">Flask</text>
      <rect x="117" width="48" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="141" y="12.5" fill="#38BDF8" text-anchor="middle">React</text>
      <rect x="172" width="92" height="18" rx="4" fill="#161B22" stroke="#38BDF8" />
      <text x="218" y="12.5" fill="#00F2FE" font-weight="700" text-anchor="middle">Gene-Disease AI</text>
    </g>
  </g>

  <!-- Card 2: Maritime Risk AI (Ship & Ocean path) -->
  <g transform="translate(430, 60)">
    <rect width="390" height="135" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    
    <g transform="translate(340, 40)">
      <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#34D399" stroke-width="1" />
      <line x1="-12" y1="4" x2="12" y2="4" stroke="#38BDF8" stroke-width="1" stroke-dasharray="2 2" />
      <polygon points="-6,2 6,2 3,-4 -3,-4" fill="#34D399">
        <animate attributeName="transform" type="translate" values="-4,0; 4,0; -4,0" dur="3s" repeatCount="indefinite" />
      </polygon>
    </g>

    <text x="16" y="24" fill="#34D399" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#128674; Maritime Risk AI</text>
    <text x="16" y="42" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700">Predictive Supply Chain Risk Analytics</text>
    <text x="16" y="62" fill="#94A3B8" font-family="-apple-system, sans-serif" font-size="10.5">
      Predicts vessel route risks, seasonal disruptions, and container port congestion queues.
    </text>

    <g transform="translate(16, 92)" font-family="'Fira Code', monospace" font-size="8.5">
      <rect width="55" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="27.5" y="12.5" fill="#34D399" text-anchor="middle">Python</text>
      <rect x="62" width="48" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="86" y="12.5" fill="#34D399" text-anchor="middle">Flask</text>
      <rect x="117" width="48" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="141" y="12.5" fill="#34D399" text-anchor="middle">React</text>
      <rect x="172" width="92" height="18" rx="4" fill="#161B22" stroke="#34D399" />
      <text x="218" y="12.5" fill="#34D399" font-weight="700" text-anchor="middle">Predictive ML</text>
    </g>
  </g>

  <!-- Card 3: Smart Attendance & Timetable (Moving schedule blocks) -->
  <g transform="translate(30, 205)">
    <rect width="380" height="135" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    
    <g transform="translate(330, 40)">
      <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#818CF8" stroke-width="1" />
      <rect x="-8" y="-8" width="6" height="6" fill="#818CF8">
        <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite" />
      </rect>
      <rect x="2" y="-8" width="6" height="6" fill="#00F2FE">
        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />
      </rect>
      <rect x="-8" y="2" width="6" height="6" fill="#34D399">
        <animate attributeName="opacity" values="0.5;1;0.5" dur="1.5s" repeatCount="indefinite" />
      </rect>
      <rect x="2" y="2" width="6" height="6" fill="#C084FC">
        <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite" />
      </rect>
    </g>

    <text x="16" y="24" fill="#818CF8" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#127891; Smart Attendance &amp; TT</text>
    <text x="16" y="42" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700">Computer Vision + Scheduling System</text>
    <text x="16" y="62" fill="#94A3B8" font-family="-apple-system, sans-serif" font-size="10.5">
      Automated attendance pipeline paired with constraint solver for collision-free schedules.
    </text>

    <g transform="translate(16, 92)" font-family="'Fira Code', monospace" font-size="8.5">
      <rect width="55" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="27.5" y="12.5" fill="#818CF8" text-anchor="middle">Python</text>
      <rect x="62" width="58" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="91" y="12.5" fill="#818CF8" text-anchor="middle">OpenCV</text>
      <rect x="127" width="112" height="18" rx="4" fill="#161B22" stroke="#818CF8" />
      <text x="183" y="12.5" fill="#818CF8" font-weight="700" text-anchor="middle">Constraint Solver</text>
    </g>
  </g>

  <!-- Card 4: RoadWatch (Road line & markers) -->
  <g transform="translate(430, 205)">
    <rect width="390" height="135" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    
    <g transform="translate(340, 40)">
      <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#F59E0B" stroke-width="1" />
      <line x1="-12" y1="6" x2="12" y2="-6" stroke="#334155" stroke-width="2" />
      <circle cx="-6" cy="3" r="2.5" fill="#F59E0B">
        <animate attributeName="opacity" values="1;0.2;1" dur="1s" repeatCount="indefinite" />
      </circle>
      <circle cx="6" cy="-3" r="2.5" fill="#00F2FE">
        <animate attributeName="opacity" values="0.2;1;0.2" dur="1.2s" repeatCount="indefinite" />
      </circle>
    </g>

    <text x="16" y="24" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="12" font-weight="800">&#128739; RoadWatch</text>
    <text x="16" y="42" fill="#CBD5E1" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700">Infrastructure Risk Intelligence</text>
    <text x="16" y="62" fill="#94A3B8" font-family="-apple-system, sans-serif" font-size="10.5">
      Geospatial road hazard telemetry, anomaly classification, and infrastructure condition analytics.
    </text>

    <g transform="translate(16, 92)" font-family="'Fira Code', monospace" font-size="8.5">
      <rect width="55" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="27.5" y="12.5" fill="#F59E0B" text-anchor="middle">Python</text>
      <rect x="62" width="75" height="18" rx="4" fill="#161B22" stroke="#334155" />
      <text x="99.5" y="12.5" fill="#F59E0B" text-anchor="middle">GIS Analytics</text>
      <rect x="144" width="85" height="18" rx="4" fill="#161B22" stroke="#F59E0B" />
      <text x="186.5" y="12.5" fill="#F59E0B" font-weight="700" text-anchor="middle">Data Science</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 7. CURRENT LEARNING JOURNEY (assets/learning-journey.svg)
# -------------------------------------------------------------
learning_journey_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 200" width="850" height="200">
  <defs>
    <linearGradient id="lj-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>

    <linearGradient id="lj-path" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#818CF8" />
    </linearGradient>
  </defs>

  <rect width="850" height="200" rx="14" fill="url(#lj-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1"># CURRENT LEARNING JOURNEY // PATH CONNECTIONS (NO PERCENTAGES)</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">&#9679; TRAJECTORY ONLINE</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <line x1="75" y1="100" x2="775" y2="100" stroke="url(#lj-path)" stroke-width="2" stroke-dasharray="6 4" opacity="0.6" />

  <g transform="translate(60, 65)">
    <rect width="135" height="70" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <circle cx="16" cy="18" r="4" fill="#10B981" />
    <text x="26" y="21" fill="#10B981" font-family="'Fira Code', monospace" font-size="8" font-weight="700">ACTIVE LEARNING</text>
    <text x="12" y="44" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="10" font-weight="700">Advanced ML</text>
    <text x="12" y="58" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="8.5">Ensemble &amp; Neural</text>
  </g>

  <g transform="translate(210, 65)">
    <rect width="135" height="70" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <circle cx="16" cy="18" r="4" fill="#10B981" />
    <text x="26" y="21" fill="#10B981" font-family="'Fira Code', monospace" font-size="8" font-weight="700">ACTIVE LEARNING</text>
    <text x="12" y="44" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="10" font-weight="700">FastAPI</text>
    <text x="12" y="58" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="8.5">High-Speed APIs</text>
  </g>

  <g transform="translate(360, 65)">
    <rect width="135" height="70" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <circle cx="16" cy="18" r="4" fill="#F59E0B" />
    <text x="26" y="21" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="8" font-weight="700">EXPLORING</text>
    <text x="12" y="44" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="10" font-weight="700">MLOps Fund.</text>
    <text x="12" y="58" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="8.5">CI/CD &amp; Pipelines</text>
  </g>

  <g transform="translate(510, 65)">
    <rect width="135" height="70" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <circle cx="16" cy="18" r="4" fill="#38BDF8" />
    <text x="26" y="21" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="8" font-weight="700">BUILDING</text>
    <text x="12" y="44" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="10" font-weight="700">System Design</text>
    <text x="12" y="58" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="8.5">Microservices</text>
  </g>

  <g transform="translate(660, 65)">
    <rect width="135" height="70" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
    <circle cx="16" cy="18" r="4" fill="#10B981" />
    <text x="26" y="21" fill="#10B981" font-family="'Fira Code', monospace" font-size="8" font-weight="700">ACTIVE LEARNING</text>
    <text x="12" y="44" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="10" font-weight="700">SQL Tuning</text>
    <text x="12" y="58" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="8.5">Query Optimization</text>
  </g>

  <g transform="translate(250, 160)" font-family="'Fira Code', monospace" font-size="9" fill="#94A3B8">
    <circle cx="10" cy="10" r="3.5" fill="#10B981" />
    <text x="20" y="13">🟢 Active Learning</text>
    
    <circle cx="140" cy="10" r="3.5" fill="#F59E0B" />
    <text x="150" y="13">🟡 Exploring</text>
    
    <circle cx="250" cy="10" r="3.5" fill="#38BDF8" />
    <text x="260" y="13">🔵 Building Projects</text>
  </g>
</svg>'''

files = [
    ("hero-os-refined.svg", hero_svg),
    ("terminal-refined.svg", terminal_svg),
    ("neural-blueprint.svg", neural_blueprint_svg),
    ("engineering-domains.svg", domains_svg),
    ("tech-stack-cards.svg", tech_stack_svg),
    ("innovation-lab.svg", innovation_lab_svg),
    ("learning-journey.svg", learning_journey_svg),
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

print("All Refined Profile SVG assets generated successfully!")
