import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO SECTION (assets/hero-engineer.svg)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="eng-hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
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

    <linearGradient id="eng-hero-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <filter id="eng-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Frame -->
  <rect width="850" height="250" rx="16" fill="url(#eng-hero-bg)" stroke="url(#eng-hero-border)" stroke-width="1.8" />
  <rect x="0" y="0" width="850" height="4.5" rx="2.25" fill="url(#eng-hero-border)" filter="url(#eng-glow)" />

  <!-- Top Bar -->
  <g transform="translate(24, 18)">
    <circle cx="8" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="4.5" fill="#27C93F" />
    <text x="60" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">AI_ENGINEER_DASHBOARD // KATHYAYINI_PRABHU</text>
    <text x="800" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">SYS.STATUS: ONLINE &#9679;</text>
  </g>

  <line x1="20" y1="42" x2="830" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- Left Details -->
  <g transform="translate(36, 52)">
    <rect x="0" y="8" width="5" height="136" rx="2.5" fill="#00F2FE" filter="url(#eng-glow)" />

    <text x="20" y="34" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" letter-spacing="0.5">Kathyayini Prabhu</text>
    
    <text x="20" y="62" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="14.5" font-weight="700">Artificial Intelligence &amp; Data Science Engineer</text>
    
    <text x="20" y="88" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Transforming Data Into Intelligent Decisions</text>
    <text x="20" y="106" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5">Through AI, Analytics &amp; Software Systems</text>

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
    <rect width="255" height="175" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" filter="url(#eng-glow)" />

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
# 2. NEURAL BLUEPRINT (assets/neural-blueprint-engineer.svg)
# -------------------------------------------------------------
neural_blueprint_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 260" width="850" height="260">
  <defs>
    <linearGradient id="eng-nb-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>

    <filter id="eng-nb-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="260" rx="14" fill="url(#eng-nb-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Animated Neural Lines -->
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
  <g transform="translate(36, 68)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
    <text x="0" y="16" fill="#FFFFFF" font-size="13.5" font-weight="600">
      I am an Artificial Intelligence &amp; Data Science engineer focused on building intelligent systems that transform data into meaningful insights and real-world solutions.
    </text>

    <text x="0" y="40" fill="#38BDF8" font-size="13.5" font-weight="500">
      My work combines Machine Learning, Data Analytics, SQL Engineering, Backend Development, and Software Design to create scalable, data-driven applications.
    </text>

    <text x="0" y="64" fill="#CBD5E1" font-size="13">
      I enjoy solving complex problems through predictive modeling, intelligent automation, analytical thinking, and modern software engineering practices.
    </text>

    <text x="0" y="88" fill="#94A3B8" font-size="12.5" font-style="italic">
      Currently exploring advanced AI systems, data intelligence architectures, and real-world machine learning applications.
    </text>

    <!-- 5 Focus Tags -->
    <g transform="translate(0, 108)" font-family="'Fira Code', monospace" font-size="9">
      <rect width="145" height="24" rx="12" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="72.5" y="15.5" fill="#00F2FE" font-weight="700" text-anchor="middle">&#9670; Machine Learning</text>

      <rect x="155" width="135" height="24" rx="12" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="222.5" y="15.5" fill="#34D399" font-weight="700" text-anchor="middle">&#9670; Data Analytics</text>

      <rect x="300" width="160" height="24" rx="12" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="380" y="15.5" fill="#F59E0B" font-weight="700" text-anchor="middle">&#9670; SQL Engineering</text>

      <rect x="470" width="165" height="24" rx="12" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="552.5" y="15.5" fill="#818CF8" font-weight="700" text-anchor="middle">&#9670; Backend Development</text>

      <rect x="645" width="135" height="24" rx="12" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="712.5" y="15.5" fill="#C084FC" font-weight="700" text-anchor="middle">&#9670; AI Applications</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. INTELLIGENCE DOMAINS (assets/intelligence-domains.svg)
# -------------------------------------------------------------
domains_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 300" width="850" height="300">
  <defs>
    <linearGradient id="eng-id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#070B1F" />
    </linearGradient>

    <filter id="eng-id-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="300" rx="14" fill="url(#eng-id-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">INTELLIGENCE DOMAINS // CORE DISCIPLINES</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">PRODUCTION VERIFIED &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 4 Clean Domain Panels -->
  
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
# 4. TECHNOLOGY STACK (6 SEPARATE FLOATING CARDS) (assets/tech-stack-cards-clean.svg)
# -------------------------------------------------------------
tech_stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="850" height="280">
  <defs>
    <linearGradient id="eng-ts-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#0A1028" />
    </linearGradient>
  </defs>

  <rect width="850" height="280" rx="14" fill="url(#eng-ts-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">TECHNOLOGY STACK // 6 SPECIALIZED SKILL CARDS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">ACTIVE STACK &#9679;</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 6 Specialized Floating Cards (3 columns x 2 rows) -->
  
  <!-- Row 1 -->

  <!-- Card 1: Languages -->
  <g transform="translate(30, 60)">
    <rect width="250" height="95" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
    <text x="14" y="22" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800">LANGUAGES</text>
    <line x1="14" y1="28" x2="236" y2="28" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(14, 48)" font-family="'Fira Code', monospace" font-size="10" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#34D399">&#9654;</tspan> Python</text>
      <text x="80" y="0"><tspan fill="#34D399">&#9654;</tspan> SQL</text>
      <text x="140" y="0"><tspan fill="#34D399">&#9654;</tspan> C</text>
    </g>
  </g>

  <!-- Card 2: Machine Learning -->
  <g transform="translate(295, 60)">
    <rect width="260" height="95" rx="10" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
    <text x="14" y="22" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800">MACHINE LEARNING</text>
    <line x1="14" y1="28" x2="246" y2="28" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(14, 48)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#00F2FE">&#9670;</tspan> Machine Learning</text>
      <text x="125" y="0"><tspan fill="#00F2FE">&#9670;</tspan> Scikit-Learn</text>
      <text x="0" y="20"><tspan fill="#00F2FE">&#9670;</tspan> Predictive Models</text>
      <text x="125" y="20"><tspan fill="#00F2FE">&#9670;</tspan> Feature Eng.</text>
    </g>
  </g>

  <!-- Card 3: Data Analytics -->
  <g transform="translate(570, 60)">
    <rect width="250" height="95" rx="10" fill="#0D1117" stroke="#34D399" stroke-width="1" />
    <text x="14" y="22" fill="#34D399" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800">DATA ANALYTICS</text>
    <line x1="14" y1="28" x2="236" y2="28" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(14, 48)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#34D399">&#9658;</tspan> Pandas &amp; NumPy</text>
      <text x="120" y="0"><tspan fill="#34D399">&#9658;</tspan> Tableau</text>
      <text x="0" y="20"><tspan fill="#34D399">&#9658;</tspan> EDA &amp; Statistics</text>
    </g>
  </g>

  <!-- Row 2 -->

  <!-- Card 4: Backend Development -->
  <g transform="translate(30, 168)">
    <rect width="250" height="95" rx="10" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
    <text x="14" y="22" fill="#818CF8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800">BACKEND DEVELOPMENT</text>
    <line x1="14" y1="28" x2="236" y2="28" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(14, 48)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#818CF8">&#9658;</tspan> Flask</text>
      <text x="75" y="0"><tspan fill="#818CF8">&#9658;</tspan> FastAPI</text>
      <text x="145" y="0"><tspan fill="#818CF8">&#9658;</tspan> REST APIs</text>
    </g>
  </g>

  <!-- Card 5: Databases -->
  <g transform="translate(295, 168)">
    <rect width="260" height="95" rx="10" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
    <text x="14" y="22" fill="#F59E0B" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800">DATABASES</text>
    <line x1="14" y1="28" x2="246" y2="28" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(14, 48)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#F59E0B">&#9679;</tspan> MySQL</text>
      <text x="75" y="0"><tspan fill="#F59E0B">&#9679;</tspan> SQLite</text>
      <text x="140" y="0"><tspan fill="#F59E0B">&#9679;</tspan> SQL</text>
      <text x="0" y="20"><tspan fill="#F59E0B">&#9679;</tspan> Database Design</text>
    </g>
  </g>

  <!-- Card 6: Development Tools -->
  <g transform="translate(570, 168)">
    <rect width="250" height="95" rx="10" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
    <text x="14" y="22" fill="#C084FC" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800">DEVELOPMENT TOOLS</text>
    <line x1="14" y1="28" x2="236" y2="28" stroke="#1E293B" stroke-width="1" />
    <g transform="translate(14, 48)" font-family="'Fira Code', monospace" font-size="9.5" fill="#F8FAFC">
      <text x="0" y="0"><tspan fill="#C084FC">&#9670;</tspan> Git</text>
      <text x="50" y="0"><tspan fill="#C084FC">&#9670;</tspan> GitHub</text>
      <text x="110" y="0"><tspan fill="#C084FC">&#9670;</tspan> React</text>
      <text x="165" y="0"><tspan fill="#C084FC">&#9670;</tspan> VS Code</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. ENGINEERING WORKFLOW (assets/engineering-workflow.svg)
# -------------------------------------------------------------
workflow_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 140" width="850" height="140">
  <defs>
    <linearGradient id="eng-wf-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050816" />
      <stop offset="100%" stop-color="#080D1F" />
    </linearGradient>

    <linearGradient id="eng-wf-arrow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#818CF8" />
    </linearGradient>
  </defs>

  <rect width="850" height="140" rx="14" fill="url(#eng-wf-bg)" stroke="#1E293B" stroke-width="1.5" />

  <g transform="translate(30, 20)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="12" font-weight="800" letter-spacing="1">ENGINEERING WORKFLOW // END-TO-END AI PIPELINE</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">PRODUCTION READY &#9679;</text>
  </g>
  <line x1="30" y1="38" x2="820" y2="38" stroke="#1E293B" stroke-width="1" />

  <!-- 6 Step Pipeline with Animated Connecting Arrows -->
  <g transform="translate(30, 56)" font-family="'Fira Code', monospace">
    <!-- Step 1 -->
    <g transform="translate(0, 0)">
      <rect width="112" height="56" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="10" y="18" fill="#38BDF8" font-size="8" font-weight="700">01 // STEP</text>
      <text x="10" y="34" fill="#F8FAFC" font-size="9" font-weight="700">Problem</text>
      <text x="10" y="46" fill="#F8FAFC" font-size="9" font-weight="700">Identification</text>
    </g>

    <!-- Arrow 1 -->
    <text x="119" y="32" fill="#00F2FE" font-size="12" font-weight="800">&#10132;</text>

    <!-- Step 2 -->
    <g transform="translate(136, 0)">
      <rect width="112" height="56" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="10" y="18" fill="#34D399" font-size="8" font-weight="700">02 // STEP</text>
      <text x="10" y="34" fill="#F8FAFC" font-size="9" font-weight="700">Data</text>
      <text x="10" y="46" fill="#F8FAFC" font-size="9" font-weight="700">Collection</text>
    </g>

    <!-- Arrow 2 -->
    <text x="255" y="32" fill="#34D399" font-size="12" font-weight="800">&#10132;</text>

    <!-- Step 3 -->
    <g transform="translate(272, 0)">
      <rect width="112" height="56" rx="8" fill="#0D1117" stroke="#00F2FE" stroke-width="1" />
      <text x="10" y="18" fill="#00F2FE" font-size="8" font-weight="700">03 // STEP</text>
      <text x="10" y="34" fill="#F8FAFC" font-size="9" font-weight="700">Data</text>
      <text x="10" y="46" fill="#F8FAFC" font-size="9" font-weight="700">Analysis</text>
    </g>

    <!-- Arrow 3 -->
    <text x="391" y="32" fill="#00F2FE" font-size="12" font-weight="800">&#10132;</text>

    <!-- Step 4 -->
    <g transform="translate(408, 0)">
      <rect width="112" height="56" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="10" y="18" fill="#818CF8" font-size="8" font-weight="700">04 // STEP</text>
      <text x="10" y="34" fill="#F8FAFC" font-size="9" font-weight="700">Machine</text>
      <text x="10" y="46" fill="#F8FAFC" font-size="9" font-weight="700">Learning</text>
    </g>

    <!-- Arrow 4 -->
    <text x="527" y="32" fill="#818CF8" font-size="12" font-weight="800">&#10132;</text>

    <!-- Step 5 -->
    <g transform="translate(544, 0)">
      <rect width="112" height="56" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="10" y="18" fill="#C084FC" font-size="8" font-weight="700">05 // STEP</text>
      <text x="10" y="34" fill="#F8FAFC" font-size="9" font-weight="700">Backend</text>
      <text x="10" y="46" fill="#F8FAFC" font-size="9" font-weight="700">Integration</text>
    </g>

    <!-- Arrow 5 -->
    <text x="663" y="32" fill="#C084FC" font-size="12" font-weight="800">&#10132;</text>

    <!-- Step 6 -->
    <g transform="translate(680, 0)">
      <rect width="110" height="56" rx="8" fill="#0D1117" stroke="#F59E0B" stroke-width="1" />
      <text x="10" y="18" fill="#F59E0B" font-size="8" font-weight="700">06 // STEP</text>
      <text x="10" y="34" fill="#F8FAFC" font-size="9" font-weight="700">Production</text>
      <text x="10" y="46" fill="#F8FAFC" font-size="9" font-weight="700">Deployment</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. FOOTER (assets/footer-refined.svg)
# -------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 120" width="850" height="120">
  <defs>
    <linearGradient id="eng-ft-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
  </defs>

  <rect width="850" height="120" rx="12" fill="#050816" stroke="#1E293B" stroke-width="1.2" />

  <line x1="40" y1="22" x2="810" y2="22" stroke="url(#eng-ft-line)" stroke-width="1.5" />

  <text x="425" y="48" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11.5" font-weight="800" letter-spacing="2" text-anchor="middle">
    ARTIFICIAL INTELLIGENCE &#8226; DATA SCIENCE &#8226; SOFTWARE SYSTEMS
  </text>

  <text x="425" y="72" fill="#F8FAFC" font-family="'Fira Code', monospace" font-size="11" font-weight="600" letter-spacing="1" text-anchor="middle">
    "Building Intelligent Solutions Through Data"
  </text>

  <line x1="40" y1="96" x2="810" y2="96" stroke="url(#eng-ft-line)" stroke-width="1.5" />
</svg>'''

files = [
    ("hero-engineer.svg", hero_svg),
    ("neural-blueprint-engineer.svg", neural_blueprint_svg),
    ("intelligence-domains.svg", domains_svg),
    ("tech-stack-cards-clean.svg", tech_stack_svg),
    ("engineering-workflow.svg", workflow_svg),
    ("footer-refined.svg", footer_svg),
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

print("All Engineer Refinement Profile SVG assets generated successfully!")
