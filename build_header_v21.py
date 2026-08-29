import xml.etree.ElementTree as ET

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 290" width="800" height="290">
  <defs>
    <!-- Deep Cyber Dark Background Gradient -->
    <linearGradient id="ide-bg" x1="0%" y1="0%" x2="100%" y2="100%">
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
    <linearGradient id="ide-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="33%" stop-color="#38BDF8" />
      <stop offset="66%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="ide-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Main Container Frame (Single Unified Box) -->
  <rect width="800" height="290" rx="16" fill="url(#ide-bg)" stroke="url(#ide-border)" stroke-width="1.8" />

  <!-- Top Accent Shimmer Line -->
  <rect x="0" y="0" width="800" height="5" rx="2.5" fill="url(#ide-border)" filter="url(#ide-glow)" />

  <!-- Window Header Bar with Active File Tab -->
  <g transform="translate(20, 16)">
    <!-- Traffic light dots -->
    <circle cx="10" cy="8" r="4.5" fill="#FF5F56" />
    <circle cx="26" cy="8" r="4.5" fill="#FFBD2E" />
    <circle cx="42" cy="8" r="4.5" fill="#27C93F" />

    <!-- Active Tab Box -->
    <g transform="translate(68, -4)">
      <path d="M 0 0 L 140 0 L 140 24 L 0 24 Z" fill="#0D1117" stroke="#1E293B" stroke-width="1" />
      <circle cx="14" cy="12" r="3" fill="#38BDF8" />
      <text x="24" y="16" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="700">kathyayini.py</text>
    </g>

    <!-- Right Header Meta -->
    <text x="750" y="15" fill="#64748B" font-family="'Fira Code', monospace" font-size="10" font-weight="500" text-anchor="end">Python 3.12 | UTF-8 | BMSCE Bengaluru</text>
  </g>

  <!-- Divider Line -->
  <line x1="20" y1="42" x2="780" y2="42" stroke="#1E293B" stroke-width="1.2" />

  <!-- SINGLE UNIFIED CODE BODY -->
  <g transform="translate(30, 48)" font-family="'Fira Code', monospace" font-size="11" font-weight="500" fill="#E2E8F0">
    <!-- Line 1: Comment -->
    <text x="0" y="20" fill="#64748B"><tspan fill="#475569">01</tspan>  # Developer Instance &amp; Academic Focus</text>

    <!-- Line 2: Class Definition -->
    <text x="0" y="38">
      <tspan fill="#475569">02</tspan>  <tspan fill="#F43F5E" font-weight="700">class</tspan> <tspan fill="#38BDF8" font-weight="700">KathyayiniPrabhu</tspan><tspan fill="#F8FAFC">:</tspan>
    </text>

    <!-- Line 3: Docstring Greeting -->
    <text x="0" y="56" fill="#94A3B8">
      <tspan fill="#475569">03</tspan>      <tspan fill="#10B981">"""Hi, this is Kathyayini here! 3rd Year AI &amp; Data Science Student @ BMSCE."""</tspan>
    </text>

    <!-- Line 4: __init__ -->
    <text x="0" y="74">
      <tspan fill="#475569">04</tspan>      <tspan fill="#F43F5E">def</tspan> <tspan fill="#34D399">__init__</tspan><tspan fill="#F8FAFC">(self):</tspan>
    </text>

    <!-- Line 5: Details -->
    <text x="0" y="92">
      <tspan fill="#475569">05</tspan>          <tspan fill="#CBD5E1">self.name</tspan> <tspan fill="#F8FAFC">=</tspan> <tspan fill="#00F2FE" font-weight="700">"Kathyayini Prabhu"</tspan>
    </text>
    <text x="0" y="110">
      <tspan fill="#475569">06</tspan>          <tspan fill="#CBD5E1">self.department</tspan> <tspan fill="#F8FAFC">=</tspan> <tspan fill="#00F2FE">"Artificial Intelligence &amp; Data Science (3rd Year)"</tspan>
    </text>
    <text x="0" y="128">
      <tspan fill="#475569">07</tspan>          <tspan fill="#CBD5E1">self.college</tspan> <tspan fill="#F8FAFC">=</tspan> <tspan fill="#00F2FE">"BMS College of Engineering (BMSCE), Bengaluru"</tspan>
    </text>
    <text x="0" y="146">
      <tspan fill="#475569">08</tspan>          <tspan fill="#CBD5E1">self.status</tspan> <tspan fill="#F8FAFC">=</tspan> <tspan fill="#34D399" font-weight="700">"Analyzing Data / Training Models / Building"</tspan>
    </text>

    <!-- Line 9: Execution method -->
    <text x="0" y="164">
      <tspan fill="#475569">09</tspan>      <tspan fill="#F43F5E">def</tspan> <tspan fill="#34D399">mission</tspan><tspan fill="#F8FAFC">(self) -&gt; str:</tspan>
    </text>
    <text x="0" y="182">
      <tspan fill="#475569">10</tspan>          <tspan fill="#F59E0B">return</tspan> <tspan fill="#A78BFA">"Building intelligent ML solutions &amp; optimized database software."</tspan>
    </text>
  </g>

  <!-- BOTTOM TERMINAL OUTPUT & ACTION TRAY -->
  <g transform="translate(24, 240)">
    <!-- Terminal Output Tray Box -->
    <rect width="752" height="36" rx="8" fill="#0D1117" stroke="#1E293B" stroke-width="1" />

    <!-- Terminal Prompt with Blinking Cursor -->
    <g transform="translate(14, 22)">
      <circle cx="4" cy="-3" r="3.5" fill="#10B981" />
      <text x="14" y="0" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700">&gt;&gt;&gt; OUTPUT: [SESSION_ACTIVE] Ready to build &amp; analyze data</text>
      <rect x="360" y="-9" width="6" height="12" fill="#00F2FE">
        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
      </rect>
    </g>

    <!-- Bottom Action Badges inside Tray on the Right -->
    <g transform="translate(420, 8)">
      <rect width="58" height="20" rx="4" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
      <text x="29" y="14" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9" font-weight="700" text-anchor="middle">GITHUB</text>

      <rect x="64" width="62" height="20" rx="4" fill="#1E293B" stroke="#38BDF8" stroke-width="0.8" />
      <text x="95" y="14" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">BMSCE</text>

      <rect x="132" width="95" height="20" rx="4" fill="#0969DA" />
      <text x="179.5" y="14" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">▲ PORTFOLIO</text>

      <rect x="233" width="85" height="20" rx="4" fill="#1E293B" stroke="#A78BFA" stroke-width="0.8" />
      <text x="275.5" y="14" fill="#A78BFA" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">CONNECT</text>
    </g>
  </g>
</svg>'''

# Validate XML strictly
ET.fromstring(svg_content)
print("XML Validation for header-v21.svg: 100% PASSED!")

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\header-v21.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("assets/header-v21.svg created successfully!")
