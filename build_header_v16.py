import base64

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\kathyayini-photo.png', 'rb') as f:
    b64_str = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg fill="none" width="800" height="280" viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Deep Cyber Dark Background Gradient -->
    <linearGradient id="cyber-bg-v16" x1="0%" y1="0%" x2="100%" y2="100%">
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
    <linearGradient id="cyber-border-v16" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="33%" stop-color="#38BDF8" />
      <stop offset="66%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="cyber-glow-v16" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <!-- Avatar Clip Circle -->
    <clipPath id="avatar-clip">
      <circle cx="120" cy="118" r="70" />
    </clipPath>
  </defs>

  <!-- Main Container Frame -->
  <rect width="800" height="280" rx="16" fill="url(#cyber-bg-v16)" stroke="url(#cyber-border-v16)" stroke-width="1.8" />

  <!-- Top Accent Shimmer Line -->
  <rect x="0" y="0" width="800" height="5" rx="2.5" fill="url(#cyber-border-v16)" filter="url(#cyber-glow-v16)" />

  <!-- Top Terminal Header Bar -->
  <g transform="translate(20, 16)">
    <circle cx="10" cy="8" r="4" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4" fill="#FFBD2E" />
    <circle cx="38" cy="8" r="4" fill="#27C93F" />
    <text x="56" y="12" fill="#64748B" font-family="'Fira Code', 'Courier New', monospace" font-size="11" font-weight="700">kathyayini26 / .hostfile --live</text>
  </g>

  <!-- LEFT CARD: USER'S ACTUAL PHOTO EMBEDDED IN HOLOGRAPHIC TERMINAL -->
  <g transform="translate(24, 38)">
    <rect width="240" height="224" rx="12" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#cyber-glow-v16)" />

    <!-- Card Top Label -->
    <text x="14" y="20" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" letter-spacing="1">VISUAL_MAP / PORTRAIT_GLOBAL</text>
    <line x1="14" y1="26" x2="226" y2="26" stroke="#1E293B" stroke-width="1" />

    <!-- Rotating Radar Scanner Circle around Photo -->
    <circle cx="120" cy="118" r="75" fill="none" stroke="#00F2FE" stroke-width="1.5" stroke-dasharray="8 6" opacity="0.85" filter="url(#cyber-glow-v16)">
      <animateTransform attributeName="transform" type="rotate" from="0 120 118" to="360 120 118" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- USER'S ACTUAL PHOTO EMBEDDED WITH CLIP PATH -->
    <image href="data:image/png;base64,{b64_str}" x="40" y="38" width="160" height="160" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)" />

    <!-- Scanning Laser Line Moving Vertically Over Photo -->
    <line x1="16" y1="50" x2="224" y2="50" stroke="#00F2FE" stroke-width="1.8" filter="url(#cyber-glow-v16)">
      <animate attributeName="y1" values="35;200;35" dur="3.5s" repeatCount="indefinite" />
      <animate attributeName="y2" values="35;200;35" dur="3.5s" repeatCount="indefinite" />
    </line>

    <!-- Bottom Status Bar inside Left Card -->
    <rect x="14" y="196" width="212" height="18" rx="4" fill="#161B22" />
    <circle cx="24" cy="205" r="3" fill="#10B981" />
    <text x="32" y="208" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">KATHYAYINI_PHOTO [LIVE]</text>
  </g>

  <!-- RIGHT CARD: TERMINAL DEVELOPER INFO (SYSTEM.INFO / HARDWARE.SYS / 700) -->
  <g transform="translate(280, 38)">
    <rect width="496" height="224" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" />

    <!-- Terminal Prompt Content Rows -->
    <g font-family="'Fira Code', 'Courier New', monospace" font-size="11" font-weight="500" fill="#CBD5E1">
      <!-- Row 1: Header -->
      <text x="18" y="24">
        <tspan fill="#38BDF8" font-weight="800">SYSTEM.INFO</tspan> <tspan fill="#64748B">/ HARDWARE.SYS / 700</tspan>
      </text>

      <line x1="18" y1="32" x2="478" y2="32" stroke="#1E293B" stroke-width="1" />

      <!-- Core Details Block -->
      <text x="18" y="50"><tspan fill="#94A3B8">Subject:</tspan>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<tspan fill="#F8FAFC" font-weight="800">Kathyayini Prabhu</tspan></text>
      <text x="18" y="68"><tspan fill="#94A3B8">Role:</tspan>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<tspan fill="#38BDF8" font-weight="700">3rd Year AI &amp; Data Science Student</tspan></text>
      <text x="18" y="86"><tspan fill="#94A3B8">Affiliation:</tspan>&nbsp;<tspan fill="#E2E8F0">BMS College of Engineering (BMSCE)</tspan></text>
      <text x="18" y="104"><tspan fill="#94A3B8">Base:</tspan>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<tspan fill="#E2E8F0">Bengaluru, India</tspan></text>
      <text x="18" y="122"><tspan fill="#94A3B8">Status:</tspan>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<tspan fill="#34D399" font-weight="700">Researching / Building / Engineering</tspan></text>

      <!-- Line Separator -->
      <line x1="18" y1="130" x2="478" y2="130" stroke="#1E293B" stroke-width="1" />

      <!-- Research Item Section -->
      <text x="18" y="146"><tspan fill="#34D399" font-weight="800">RESEARCH.ITEM</tspan></text>
      <text x="18" y="162">&nbsp;<tspan fill="#94A3B8">Primary:</tspan>&nbsp;&nbsp;&nbsp;&nbsp;<tspan fill="#F8FAFC">Machine Learning, AI &amp; Data Science</tspan></text>
      <text x="18" y="178">&nbsp;<tspan fill="#94A3B8">Direction:</tspan>&nbsp;&nbsp;<tspan fill="#F8FAFC">Predictive Models &amp; SQL Architectures</tspan></text>
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

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\header-v16.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("header-v16.svg created successfully!")
