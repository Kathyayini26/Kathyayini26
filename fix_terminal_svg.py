import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"

terminal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="850" height="250">
  <defs>
    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="100%" stop-color="#05080E" />
    </linearGradient>

    <linearGradient id="term-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <rect width="850" height="250" rx="14" fill="url(#term-bg)" stroke="url(#term-border)" stroke-width="1.5" />

  <!-- Terminal Top Bar -->
  <g transform="translate(18, 16)">
    <circle cx="8" cy="6" r="4.5" fill="#FF5F56" />
    <circle cx="24" cy="6" r="4.5" fill="#FFBD2E" />
    <circle cx="40" cy="6" r="4.5" fill="#27C93F" />
    <text x="60" y="10" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="10.5" font-weight="700">kathyayini@ai-command-center: ~ (zsh)</text>
    <text x="800" y="10" fill="#34D399" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" text-anchor="end">&#9889; LATENCY: 12ms | CLOUD_SYNC</text>
  </g>

  <line x1="15" y1="36" x2="835" y2="36" stroke="#1E293B" stroke-width="1" />

  <!-- Terminal Content Lines -->
  <g transform="translate(24, 52)" font-family="'Fira Code', monospace" font-size="11" font-weight="500">
    <!-- whoami -->
    <text x="0" y="16">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">whoami</tspan>
    </text>
    <text x="18" y="34" fill="#34D399" font-weight="700">&#8594; Kathyayini Prabhu [AI &amp; Data Science Engineer @ BMSCE Bengaluru]</text>

    <!-- expertise -->
    <text x="0" y="58">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">expertise</tspan>
    </text>
    <text x="18" y="76" fill="#CBD5E1">
      <tspan fill="#00F2FE">&#9670; Artificial Intelligence</tspan>   
      <tspan fill="#34D399">&#9670; Machine Learning</tspan>   
      <tspan fill="#818CF8">&#9670; Data Science</tspan>   
      <tspan fill="#C084FC">&#9670; Software Engineering</tspan>
    </text>

    <!-- currently_building -->
    <text x="0" y="100">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">currently_building</tspan>
    </text>
    <text x="18" y="118" fill="#CBD5E1">
      <tspan fill="#F59E0B">&#9658; BioWeaver</tspan> <tspan fill="#94A3B8">[Knowledge Graph AI &amp; Gene-Disease Discovery]</tspan>
      <tspan fill="#38BDF8">&#9658; AI Maritime Risk</tspan> <tspan fill="#94A3B8">[Logistics Forecasting &amp; Route Risk]</tspan>
    </text>

    <!-- mission -->
    <text x="0" y="142">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#F8FAFC">mission</tspan>
    </text>
    <text x="18" y="160" fill="#F8FAFC" font-weight="700">&#10024; "Building intelligent systems that solve real-world problems and drive actionable decisions."</text>

    <!-- Prompt cursor -->
    <text x="0" y="184">
      <tspan fill="#38BDF8" font-weight="800">$</tspan> <tspan fill="#34D399">echo "Ready to innovate"</tspan>
    </text>
    <rect x="235" y="173" width="7" height="13" fill="#00F2FE">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

ET.fromstring(terminal_svg)
path = os.path.join(OUTPUT_DIR, "terminal-ai.svg")
with open(path, "w", encoding="utf-8") as f:
    f.write(terminal_svg)
print("terminal-ai.svg fixed and written successfully!")
