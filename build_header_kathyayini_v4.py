import xml.etree.ElementTree as ET

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 280" width="800" height="280">
  <defs>
    <!-- Deep Cyber Dark Background Gradient -->
    <linearGradient id="main-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
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
    <linearGradient id="main-border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="33%" stop-color="#38BDF8" />
      <stop offset="66%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="main-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Main Container Frame -->
  <rect width="800" height="280" rx="16" fill="url(#main-bg-grad)" stroke="url(#main-border-grad)" stroke-width="1.8" />

  <!-- Top Accent Shimmer Line -->
  <rect x="0" y="0" width="800" height="5" rx="2.5" fill="url(#main-border-grad)" filter="url(#main-glow)" />

  <!-- Top Terminal Header Bar -->
  <g transform="translate(20, 16)">
    <circle cx="10" cy="8" r="4" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4" fill="#FFBD2E" />
    <circle cx="38" cy="8" r="4" fill="#27C93F" />
    <text x="56" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="11" font-weight="700">kathyayini26 / .hostfile --live</text>
  </g>

  <!-- LEFT CARD: LIVE CODE GREETING (ANALYZING DATA & TRAINING MODELS) -->
  <g transform="translate(24, 38)">
    <rect width="255" height="224" rx="12" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#main-glow)" />

    <!-- Card Top Label -->
    <text x="14" y="20" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" letter-spacing="1">DEV_INIT / INTRO.PY</text>
    <line x1="14" y1="26" x2="241" y2="26" stroke="#1E293B" stroke-width="1" />

    <!-- IDE Code Window Content -->
    <g transform="translate(14, 34)" font-family="'Fira Code', monospace" font-size="9.5">
      <!-- Line 1: Comment -->
      <text x="0" y="14" fill="#64748B"># initialize developer session</text>
      
      <!-- Line 2: Function definition -->
      <text x="0" y="32">
        <tspan fill="#F43F5E" font-weight="700">def</tspan> <tspan fill="#34D399" font-weight="700">welcome</tspan><tspan fill="#F8FAFC">():</tspan>
      </text>

      <!-- Line 3: Message string -->
      <text x="12" y="52">
        <tspan fill="#F59E0B">msg</tspan> <tspan fill="#F8FAFC">=</tspan> <tspan fill="#00F2FE" font-weight="700">"Hi, this is"</tspan>
      </text>
      <text x="48" y="70">
        <tspan fill="#00F2FE" font-weight="700">"Kathyayini here!"</tspan>
      </text>

      <!-- Line 4: Return statement (Analyzing data & training models) -->
      <text x="12" y="90">
        <tspan fill="#F43F5E">return</tspan> <tspan fill="#A78BFA" font-weight="600">"Analyzing data &amp;"</tspan>
      </text>
      <text x="64" y="106">
        <tspan fill="#A78BFA" font-weight="600">training models."</tspan>
      </text>

      <!-- Line 5: Execution Terminal Call -->
      <text x="0" y="124" fill="#E2E8F0">
        <tspan fill="#34D399">&gt;&gt;&gt;</tspan> <tspan fill="#F8FAFC">print(welcome())</tspan>
      </text>

      <!-- Line 6: Printed Output with Glowing Cyan Cursor -->
      <rect x="0" y="132" width="227" height="24" rx="4" fill="#161B22" />
      <text x="8" y="148" fill="#34D399" font-weight="800">Hi, this is Kathyayini here!</text>
      <rect x="202" y="139" width="6" height="11" fill="#00F2FE">
        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
      </rect>
    </g>

    <!-- Bottom Status Bar inside Left Card -->
    <rect x="14" y="196" width="227" height="18" rx="4" fill="#161B22" />
    <circle cx="24" cy="205" r="3" fill="#10B981" />
    <text x="32" y="208" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">CODE_EXEC [SESSION_ACTIVE]</text>
  </g>

  <!-- RIGHT CARD: CLEAN PROFILE DETAILS + LIVE ANIMATED TELEMETRY PULSE -->
  <g transform="translate(295, 38)">
    <rect width="481" height="224" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" />

    <!-- Terminal Prompt Content Rows -->
    <g font-family="'Fira Code', monospace" font-size="11" font-weight="500" fill="#CBD5E1">
      <!-- Row 1: Header -->
      <text x="18" y="24">
        <tspan fill="#38BDF8" font-weight="800">SYSTEM.INFO</tspan> <tspan fill="#64748B">/ HARDWARE.SYS / 700</tspan>
      </text>

      <line x1="18" y1="32" x2="463" y2="32" stroke="#1E293B" stroke-width="1" />

      <!-- Core Details Block -->
      <text x="18" y="52"><tspan fill="#94A3B8">Name:</tspan>        <tspan fill="#F8FAFC" font-weight="800">Kathyayini Prabhu</tspan></text>
      <text x="18" y="72"><tspan fill="#94A3B8">Role:</tspan>        <tspan fill="#38BDF8" font-weight="700">3rd Year AI &amp; Data Science Student</tspan></text>
      <text x="18" y="92"><tspan fill="#94A3B8">Affiliation:</tspan> <tspan fill="#E2E8F0">BMS College of Engineering (BMSCE)</tspan></text>
      <text x="18" y="112"><tspan fill="#94A3B8">Base:</tspan>        <tspan fill="#E2E8F0">Bengaluru, India</tspan></text>
      <text x="18" y="132"><tspan fill="#94A3B8">Status:</tspan>      <tspan fill="#34D399" font-weight="700">Analyzing Data / Building / Engineering</tspan></text>

      <!-- Line Separator -->
      <line x1="18" y1="142" x2="463" y2="142" stroke="#1E293B" stroke-width="1" />
    </g>

    <!-- LIVE ANIMATED TELEMETRY ACTIVITY MONITOR (CLEAN & UNIQUE) -->
    <g transform="translate(18, 150)">
      <rect width="445" height="30" rx="6" fill="#161B22" stroke="#334155" stroke-width="0.8" />
      
      <!-- Pulsing Activity Line -->
      <path d="M 12 15 L 60 15 L 75 6 L 90 24 L 105 10 L 120 18 L 135 15 L 200 15" fill="none" stroke="#00F2FE" stroke-width="1.6" filter="url(#main-glow)">
        <animate attributeName="stroke-dasharray" values="0,300; 300,0" dur="2.5s" repeatCount="indefinite" />
      </path>

      <!-- Activity Metrics Text -->
      <text x="215" y="19" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="8.5">
        SIGNAL: <tspan fill="#34D399" font-weight="700">STABLE</tspan> | ML_PIPELINE: <tspan fill="#38BDF8" font-weight="700">ONLINE</tspan>
      </text>

      <circle cx="430" cy="15" r="3.5" fill="#10B981">
        <animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite" />
      </circle>
    </g>

    <!-- Bottom Action Pills Row -->
    <g transform="translate(18, 192)">
      <rect width="64" height="20" rx="4" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
      <text x="32" y="14" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9" font-weight="700" text-anchor="middle">GITHUB</text>

      <rect x="72" width="70" height="20" rx="4" fill="#1E293B" stroke="#38BDF8" stroke-width="0.8" />
      <text x="107" y="14" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">BMSCE</text>

      <rect x="150" width="105" height="20" rx="4" fill="#0969DA" />
      <text x="202.5" y="14" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">▲ PORTFOLIO</text>

      <rect x="263" width="85" height="20" rx="4" fill="#1E293B" stroke="#34D399" stroke-width="0.8" />
      <text x="305.5" y="14" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">PROJECTS</text>

      <rect x="356" width="95" height="20" rx="4" fill="#1E293B" stroke="#A78BFA" stroke-width="0.8" />
      <text x="403.5" y="14" fill="#A78BFA" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">CONNECT</text>
    </g>
  </g>
</svg>'''

# Validate XML strictly
ET.fromstring(svg_content)
print("XML Validation for header-kathyayini.svg (v4): 100% PASSED!")

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\header-kathyayini.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("assets/header-kathyayini.svg updated successfully!")
