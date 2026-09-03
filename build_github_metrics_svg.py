import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = r"C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets"

metrics_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 160" width="850" height="160">
  <defs>
    <linearGradient id="gm-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#091024" />
    </linearGradient>

    <filter id="gm-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="850" height="160" rx="14" fill="url(#gm-bg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="12" fill="#00F2FE" font-family="'Fira Code', monospace" font-size="13" font-weight="800" letter-spacing="1">GITHUB TELEMETRY // REALTIME DEVELOPER METRICS</text>
    <text x="790" y="12" fill="#34D399" font-family="'Fira Code', monospace" font-size="10" font-weight="700" text-anchor="end">&#9679; TELEMETRY ONLINE</text>
  </g>
  <line x1="30" y1="44" x2="820" y2="44" stroke="#1E293B" stroke-width="1" />

  <!-- 4 Stats Boxes -->
  <g transform="translate(30, 60)" font-family="'Fira Code', monospace">
    <!-- Box 1 -->
    <g transform="translate(0, 0)">
      <rect width="185" height="76" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1" />
      <text x="14" y="24" fill="#94A3B8" font-size="10">TOTAL REPOSITORIES</text>
      <text x="14" y="54" fill="#38BDF8" font-size="20" font-weight="800">12+</text>
      <text x="70" y="54" fill="#34D399" font-size="9.5" font-weight="700">&#8593; Active</text>
    </g>

    <!-- Box 2 -->
    <g transform="translate(198, 0)">
      <rect width="185" height="76" rx="8" fill="#0D1117" stroke="#34D399" stroke-width="1" />
      <text x="14" y="24" fill="#94A3B8" font-size="10">TOTAL CONTRIBUTIONS</text>
      <text x="14" y="54" fill="#34D399" font-size="20" font-weight="800">110+</text>
      <text x="95" y="54" fill="#00F2FE" font-size="9.5" font-weight="700">&#9889; Year 2026</text>
    </g>

    <!-- Box 3 -->
    <g transform="translate(396, 0)">
      <rect width="185" height="76" rx="8" fill="#0D1117" stroke="#818CF8" stroke-width="1" />
      <text x="14" y="24" fill="#94A3B8" font-size="10">PRIMARY DOMAIN</text>
      <text x="14" y="48" fill="#818CF8" font-size="12" font-weight="800">AI &amp; Data Science</text>
      <text x="14" y="64" fill="#CBD5E1" font-size="9.5">Python &#8226; ML &#8226; SQL</text>
    </g>

    <!-- Box 4 -->
    <g transform="translate(594, 0)">
      <rect width="196" height="76" rx="8" fill="#0D1117" stroke="#C084FC" stroke-width="1" />
      <text x="14" y="24" fill="#94A3B8" font-size="10">COMMIT INTEGRITY</text>
      <text x="14" y="54" fill="#C084FC" font-size="18" font-weight="800">100%</text>
      <text x="90" y="54" fill="#34D399" font-size="9.5" font-weight="700">&#9679; Verified</text>
    </g>
  </g>
</svg>'''

ET.fromstring(metrics_svg)
path = os.path.join(OUTPUT_DIR, "github-metrics.svg")
with open(path, "w", encoding="utf-8") as f:
    f.write(metrics_svg)
print("github-metrics.svg created successfully!")
