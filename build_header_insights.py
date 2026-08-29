import xml.etree.ElementTree as ET

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 280" width="800" height="280">
  <defs>
    <!-- Deep Cyber Dark Background Gradient -->
    <linearGradient id="insights-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814">
        <animate attributeName="stop-color" values="#050814; #0A1128; #0F172A; #050814" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#0A1128">
        <animate attributeName="stop-color" values="#0A1128; #1E1B4B; #092540; #0A1128" dur="12s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#0F051D">
        <animate attributeName="stop-color" values="#0F051D; #050814; #0A1128; #0F051D" dur="12s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Neon Cyber Border Gradient -->
    <linearGradient id="insights-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="33%" stop-color="#38BDF8" />
      <stop offset="66%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="insights-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Main Container Frame -->
  <rect width="800" height="280" rx="16" fill="url(#insights-bg)" stroke="url(#insights-border)" stroke-width="1.8" />

  <!-- Top Accent Shimmer Line -->
  <rect x="0" y="0" width="800" height="5" rx="2.5" fill="url(#insights-border)" filter="url(#insights-glow)" />

  <!-- Top Terminal Header Bar -->
  <g transform="translate(20, 16)">
    <circle cx="10" cy="8" r="4" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4" fill="#FFBD2E" />
    <circle cx="38" cy="8" r="4" fill="#27C93F" />
    <text x="56" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="11" font-weight="700">kathyayini26 / .hostfile --live</text>
  </g>

  <!-- LEFT CARD: ML MODEL INSIGHTS, LOSS CONVERGENCE & FEATURE IMPORTANCE GRAPHS -->
  <g transform="translate(24, 38)">
    <rect width="240" height="224" rx="12" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#insights-glow)" />

    <!-- Card Top Label -->
    <text x="14" y="20" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" letter-spacing="1">ML_INSIGHTS / MODEL_ANALYTICS</text>
    <line x1="14" y1="26" x2="226" y2="26" stroke="#1E293B" stroke-width="1" />

    <!-- SECTION 1: ML ACCURACY & LOSS CONVERGENCE GRAPH -->
    <g transform="translate(14, 34)">
      <!-- Graph Frame Box -->
      <rect width="212" height="74" rx="6" fill="#161B22" stroke="#334155" stroke-width="0.8" />
      
      <!-- Graph Grid Lines -->
      <line x1="10" y1="18" x2="202" y2="18" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="2 2" />
      <line x1="10" y1="36" x2="202" y2="36" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="2 2" />
      <line x1="10" y1="54" x2="202" y2="54" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="2 2" />

      <!-- Accuracy Curve (Rising to 98.6%) -->
      <path d="M 12 56 Q 60 48 100 28 T 170 16 T 200 12" fill="none" stroke="#34D399" stroke-width="2" filter="url(#insights-glow)">
        <animate attributeName="d" values="M 12 56 Q 60 48 100 28 T 170 16 T 200 12; M 12 56 Q 60 40 100 32 T 170 18 T 200 12; M 12 56 Q 60 48 100 28 T 170 16 T 200 12" dur="5s" repeatCount="indefinite" />
      </path>

      <!-- Loss Curve (Descending to 0.014) -->
      <path d="M 12 18 Q 50 24 90 44 T 160 56 T 200 60" fill="none" stroke="#38BDF8" stroke-width="1.8" filter="url(#insights-glow)" opacity="0.85">
        <animate attributeName="d" values="M 12 18 Q 50 24 90 44 T 160 56 T 200 60; M 12 18 Q 50 32 90 48 T 160 54 T 200 60; M 12 18 Q 50 24 90 44 T 160 56 T 200 60" dur="5s" repeatCount="indefinite" />
      </path>

      <!-- Pulsing Data Point Nodes -->
      <circle cx="100" cy="28" r="3.5" fill="#34D399" filter="url(#insights-glow)">
        <animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite" />
      </circle>
      <circle cx="200" cy="12" r="4" fill="#00F2FE" filter="url(#insights-glow)">
        <animate attributeName="r" values="3.5;6;3.5" dur="1.8s" repeatCount="indefinite" />
      </circle>

      <text x="14" y="14" fill="#34D399" font-family="'Fira Code', monospace" font-size="7.5" font-weight="700">ACC: 98.6%</text>
      <text x="14" y="68" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="7.5" font-weight="700">LOSS: 0.014</text>
      <text x="140" y="68" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="7.5">EPOCHS: 100</text>
    </g>

    <!-- SECTION 2: ML FEATURE IMPORTANCE / DATA ANALYTICS BARS -->
    <g transform="translate(14, 116)" font-family="'Fira Code', monospace" font-size="8">
      <text x="0" y="8" fill="#CBD5E1" font-weight="700">FEATURE IMPORTANCE MATRIX</text>

      <!-- Bar 1: Neural Weights -->
      <text x="0" y="24" fill="#94A3B8">Neural_Weights</text>
      <rect x="86" y="16" width="95" height="9" rx="4.5" fill="#38BDF8" filter="url(#insights-glow)">
        <animate attributeName="width" values="95;110;95" dur="3s" repeatCount="indefinite" />
      </rect>
      <text x="190" y="24" fill="#38BDF8" font-weight="700">0.92</text>

      <!-- Bar 2: Data Signals -->
      <text x="0" y="38" fill="#94A3B8">Data_Signals</text>
      <rect x="86" y="30" width="80" height="9" rx="4.5" fill="#34D399" filter="url(#insights-glow)">
        <animate attributeName="width" values="80;92;80" dur="3.5s" repeatCount="indefinite" />
      </rect>
      <text x="190" y="38" fill="#34D399" font-weight="700">0.78</text>

      <!-- Bar 3: SQL Schema -->
      <text x="0" y="52" fill="#94A3B8">SQL_Schema_Tuning</text>
      <rect x="86" y="44" width="65" height="9" rx="4.5" fill="#F59E0B" filter="url(#insights-glow)">
        <animate attributeName="width" values="65;75;65" dur="2.8s" repeatCount="indefinite" />
      </rect>
      <text x="190" y="52" fill="#F59E0B" font-weight="700">0.64</text>

      <!-- Bar 4: Predictive Score -->
      <text x="0" y="66" fill="#94A3B8">Predictive_Score</text>
      <rect x="86" y="58" width="50" height="9" rx="4.5" fill="#A78BFA" filter="url(#insights-glow)">
        <animate attributeName="width" values="50;62;50" dur="3.2s" repeatCount="indefinite" />
      </rect>
      <text x="190" y="66" fill="#A78BFA" font-weight="700">0.51</text>
    </g>

    <!-- Bottom Status Bar inside Left Card -->
    <rect x="14" y="196" width="212" height="18" rx="4" fill="#161B22" />
    <circle cx="24" cy="205" r="3" fill="#10B981" />
    <text x="32" y="208" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">ROC_AUC: 0.99 [OPTIMAL_FIT]</text>
  </g>

  <!-- RIGHT CARD: TERMINAL DEVELOPER INFO (SYSTEM.INFO / HARDWARE.SYS / 700) -->
  <g transform="translate(280, 38)">
    <rect width="496" height="224" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" />

    <!-- Terminal Prompt Content Rows -->
    <g font-family="'Fira Code', monospace" font-size="11" font-weight="500" fill="#CBD5E1">
      <!-- Row 1: Header -->
      <text x="18" y="24">
        <tspan fill="#38BDF8" font-weight="800">SYSTEM.INFO</tspan> <tspan fill="#64748B">/ HARDWARE.SYS / 700</tspan>
      </text>

      <line x1="18" y1="32" x2="478" y2="32" stroke="#1E293B" stroke-width="1" />

      <!-- Core Details Block -->
      <text x="18" y="50"><tspan fill="#94A3B8">Subject:</tspan>     <tspan fill="#F8FAFC" font-weight="800">Kathyayini Prabhu</tspan></text>
      <text x="18" y="68"><tspan fill="#94A3B8">Role:</tspan>        <tspan fill="#38BDF8" font-weight="700">3rd Year AI &amp; Data Science Student</tspan></text>
      <text x="18" y="86"><tspan fill="#94A3B8">Affiliation:</tspan> <tspan fill="#E2E8F0">BMS College of Engineering (BMSCE)</tspan></text>
      <text x="18" y="104"><tspan fill="#94A3B8">Base:</tspan>        <tspan fill="#E2E8F0">Bengaluru, India</tspan></text>
      <text x="18" y="122"><tspan fill="#94A3B8">Status:</tspan>      <tspan fill="#34D399" font-weight="700">Researching / Building / Engineering</tspan></text>

      <!-- Line Separator -->
      <line x1="18" y1="130" x2="478" y2="130" stroke="#1E293B" stroke-width="1" />

      <!-- Research Item Section -->
      <text x="18" y="146"><tspan fill="#34D399" font-weight="800">RESEARCH.ITEM</tspan></text>
      <text x="18" y="162"> <tspan fill="#94A3B8">Primary:</tspan>    <tspan fill="#F8FAFC">Machine Learning, AI &amp; Data Science</tspan></text>
      <text x="18" y="178"> <tspan fill="#94A3B8">Direction:</tspan>  <tspan fill="#F8FAFC">Predictive Models &amp; SQL Architectures</tspan></text>
    </g>

    <!-- Bottom Action Pills Row -->
    <g transform="translate(18, 192)">
      <rect width="64" height="20" rx="4" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
      <text x="32" y="14" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9" font-weight="700" text-anchor="middle">GITHUB</text>

      <rect x="72" width="95" height="20" rx="4" fill="#1E293B" stroke="#38BDF8" stroke-width="0.8" />
      <text x="119.5" y="14" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">KATHYAYINI</text>

      <rect x="175" width="95" height="20" rx="4" fill="#0969DA" />
      <text x="222.5" y="14" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">▲ PORTFOLIO</text>

      <rect x="278" width="60" height="20" rx="4" fill="#1E293B" stroke="#34D399" stroke-width="0.8" />
      <text x="308" y="14" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">BMSCE</text>

      <rect x="346" width="112" height="20" rx="4" fill="#1E293B" stroke="#A78BFA" stroke-width="0.8" />
      <text x="402" y="14" fill="#A78BFA" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">AI / DS / ASSETS</text>
    </g>
  </g>
</svg>'''

ET.fromstring(svg_content)
print("XML Validation for header-insights.svg: 100% PASSED!")

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\header-insights.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("assets/header-insights.svg created successfully!")
