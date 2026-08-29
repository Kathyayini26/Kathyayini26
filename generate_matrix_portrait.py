import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Load image
img = Image.open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\kathyayini-photo.png').convert('L')

# Crop to center face & shoulders
w, h = img.size
crop_box = (int(w * 0.12), int(h * 0.04), int(w * 0.88), int(h * 0.96))
img_cropped = img.crop(crop_box)

# Enhance contrast & sharpness
enhancer = ImageEnhance.Contrast(img_cropped)
img_contrast = enhancer.enhance(1.9)
img_sharp = img_contrast.filter(ImageFilter.SHARPEN)

# Scanline resolution inside the 240x224 card
num_rows = 44
num_cols = 52
img_small = img_sharp.resize((num_cols, num_rows), Image.Resampling.LANCZOS)
arr = np.array(img_small, dtype=float)

# Background is bright white curtain, person is darker
# Calculate intensity where foreground/person is bright
person_intensity = 255.0 - arr

# Normalize
p_min = person_intensity.min()
p_max = person_intensity.max()
norm = (person_intensity - p_min) / (p_max - p_min + 1e-5) * 255.0

# Slightly boost face highlights
norm = np.clip(norm * 1.35 - 15, 0, 255)

box_x = 34.0
box_y = 52.0
card_w = 212.0
card_h = 142.0

step_x = card_w / num_cols
step_y = card_h / num_rows

# Build scanlines paths grouped by brightness levels for maximum rendering speed & quality
paths_bright = []
paths_med = []
paths_dim = []

for r in range(num_rows):
    y = box_y + r * step_y
    for c in range(num_cols):
        val = norm[r, c]
        if val > 30:
            x1 = box_x + c * step_x
            x2 = x1 + step_x * 0.85
            seg = f"M{x1:.1f},{y:.1f}H{x2:.1f}"
            if val > 170:
                paths_bright.append(seg)
            elif val > 95:
                paths_med.append(seg)
            else:
                paths_dim.append(seg)

path_bright_str = " ".join(paths_bright)
path_med_str = " ".join(paths_med)
path_dim_str = " ".join(paths_dim)

svg_body = f'''<svg fill="none" width="800" height="280" viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Deep Cyber Dark Background Gradient -->
    <linearGradient id="cyber-bg-matrix" x1="0%" y1="0%" x2="100%" y2="100%">
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
    <linearGradient id="cyber-border-matrix" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="33%" stop-color="#38BDF8" />
      <stop offset="66%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="matrix-glow-fx" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Main Container Frame -->
  <rect width="800" height="280" rx="16" fill="url(#cyber-bg-matrix)" stroke="url(#cyber-border-matrix)" stroke-width="1.8" />

  <!-- Top Accent Shimmer Line -->
  <rect x="0" y="0" width="800" height="5" rx="2.5" fill="url(#cyber-border-matrix)" filter="url(#matrix-glow-fx)" />

  <!-- Top Terminal Header Bar -->
  <g transform="translate(20, 16)">
    <circle cx="10" cy="8" r="4" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4" fill="#FFBD2E" />
    <circle cx="38" cy="8" r="4" fill="#27C93F" />
    <text x="56" y="12" fill="#64748B" font-family="'Fira Code', 'Courier New', monospace" font-size="11" font-weight="700">kathyayini26 / .hostfile --live</text>
  </g>

  <!-- LEFT CARD: HOLOGRAPHIC SCANLINE MATRIX PORTRAIT (GENERATED FROM YOUR PHOTO) -->
  <g transform="translate(24, 38)">
    <rect width="240" height="224" rx="12" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#matrix-glow-fx)" />

    <!-- Card Top Label -->
    <text x="14" y="20" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" letter-spacing="1">VISUAL_MAP / PORTRAIT_GLOBAL</text>
    <line x1="14" y1="26" x2="226" y2="26" stroke="#1E293B" stroke-width="1" />

    <!-- Radar Grid Background Overlay -->
    <circle cx="120" cy="118" r="75" fill="none" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="4 4" />
    <circle cx="120" cy="118" r="48" fill="none" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="4 4" />

    <!-- Rotating Radar Scanner Circle -->
    <circle cx="120" cy="118" r="75" fill="none" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.65">
      <animateTransform attributeName="transform" type="rotate" from="0 120 118" to="360 120 118" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- MATRIX SCANLINE PATHS OF YOUR PHOTO (HIGH PERFORMANCE PURE VECTOR) -->
    <g filter="url(#matrix-glow-fx)" stroke-linecap="round">
      <!-- Dim Scanlines -->
      <path d="{path_dim_str}" stroke="#1E40AF" stroke-width="1.2" stroke-opacity="0.45" />
      <!-- Medium Scanlines -->
      <path d="{path_med_str}" stroke="#38BDF8" stroke-width="1.8" stroke-opacity="0.85" />
      <!-- Bright Highlights (Face & Smile & Contour) -->
      <path d="{path_bright_str}" stroke="#00F2FE" stroke-width="2.4" stroke-opacity="1.0" />
    </g>

    <!-- Scanning Laser Line Moving Vertically -->
    <line x1="16" y1="50" x2="224" y2="50" stroke="#00F2FE" stroke-width="1.5" filter="url(#matrix-glow-fx)">
      <animate attributeName="y1" values="35;205;35" dur="3.5s" repeatCount="indefinite" />
      <animate attributeName="y2" values="35;205;35" dur="3.5s" repeatCount="indefinite" />
    </line>

    <!-- Bottom Status Bar inside Left Card -->
    <rect x="14" y="196" width="212" height="18" rx="4" fill="#161B22" />
    <circle cx="24" cy="205" r="3" fill="#10B981" />
    <text x="32" y="208" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">KATHYAYINI_MATRIX [SYNC_OK]</text>
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

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\header-matrix.svg', 'w', encoding='utf-8') as f:
    f.write(svg_body)

print("Optimized header-matrix.svg written successfully!")
