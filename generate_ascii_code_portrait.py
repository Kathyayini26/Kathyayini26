import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import xml.etree.ElementTree as ET

# Load image
img = Image.open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\kathyayini-photo.png').convert('L')

# Crop to face & shoulders accurately
w, h = img.size
# Let's frame it nicely on the face and upper shoulders
crop_box = (int(w * 0.15), int(h * 0.05), int(w * 0.85), int(h * 0.88))
img_cropped = img.crop(crop_box)

# High-def ASCII Grid dimensions
# 42 rows x 48 columns of actual code characters
num_rows = 40
num_cols = 46

# Enhance local contrast so eyes, smile, hair, and face contours are crystal clear
enhancer = ImageEnhance.Contrast(img_cropped)
img_contrast = enhancer.enhance(1.6)
img_small = img_contrast.resize((num_cols, num_rows), Image.Resampling.LANCZOS)
arr = np.array(img_small, dtype=float)

# Background curtain is ~200-250. Face is ~120-170. Hair and clothes are ~20-60.
# We want dark background in terminal (space/nothing), face to be illuminated, hair to have code outline, smile & eyes highlighted!
bg_val = 210.0

# Calculate mask for person vs background
# Background is top-left/top-right high brightness
# Let's map brightness:
# In the terminal:
# Hair/Sweater: Deep Blue / Cyan accents (#38BDF8 / #1E40AF)
# Face/Skin: Soft glowing Cyan / White (#E2E8F0 / #00F2FE)
# Eyes/Smile: Sharp Bright Cyan (#00F2FE / #FFFFFF)
# Background: Transparent / Dark

box_x = 32.0
box_y = 52.0
card_w = 216.0
card_h = 142.0

step_x = card_w / num_cols
step_y = card_h / num_rows

# Code tokens to weave into her portrait
code_tokens = [
    "def", "AI", "ML", "sql", "01", "np", "pd", "fit", "ds", "bms", "git", "c",
    "{}", "=>", "==", "++", "10", "ai", "ml", "py", "kat", "26", "dev", "net"
]

token_idx = 0
svg_text_elements = []

for r in range(num_rows):
    y = box_y + r * step_y + 3.0
    row_chars = []
    
    for c in range(num_cols):
        val = arr[r, c]
        # Detect background: if r < 12 and (c < 8 or c > 38) and val > 190 -> background
        # Or simple thresholding:
        is_bg = (val > 200) and (r < 18 or c < 6 or c > 40)
        
        if is_bg:
            continue
            
        x = box_x + c * step_x
        
        # Determine character and color based on facial feature intensity
        # val ranges from 15 (dark hair/sweater) to 190 (bright forehead/cheeks)
        if val < 60:  # Dark hair / sweater
            ch = code_tokens[token_idx % len(code_tokens)]
            token_idx += 1
            color = "#1D4ED8"  # Deep blue
            op = 0.55
            size = 3.6
        elif val < 110: # Hair shadows / eyes / eyebrows / mouth contour
            ch = code_tokens[token_idx % len(code_tokens)]
            token_idx += 1
            color = "#38BDF8"  # Bright cyan
            op = 0.90
            size = 4.2
        elif val < 155: # Face skin / cheeks
            ch = "1" if (r + c) % 2 == 0 else "0"
            color = "#00F2FE"  # Electric cyan
            op = 0.75
            size = 3.8
        else: # Face highlights / smile teeth / reflection
            ch = "*" if (r + c) % 3 == 0 else "+"
            color = "#FFFFFF"  # White highlight
            op = 0.95
            size = 4.0
            
        svg_text_elements.append(
            f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" opacity="{op:.2f}" font-size="{size:.1f}">{ch}</text>'
        )

matrix_code_str = "\n    ".join(svg_text_elements)

svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 280" width="800" height="280">
  <defs>
    <linearGradient id="bg-grad-v17" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="50%" stop-color="#0A1128" />
      <stop offset="100%" stop-color="#0F051D" />
    </linearGradient>

    <linearGradient id="border-grad-v17" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="33%" stop-color="#38BDF8" />
      <stop offset="66%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>

    <filter id="code-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Outer Frame -->
  <rect width="800" height="280" rx="16" fill="url(#bg-grad-v17)" stroke="url(#border-grad-v17)" stroke-width="1.8" />

  <!-- Top Accent Shimmer -->
  <rect x="0" y="0" width="800" height="5" rx="2.5" fill="url(#border-grad-v17)" filter="url(#code-glow)" />

  <!-- Top Terminal Header Bar -->
  <g transform="translate(20, 16)">
    <circle cx="10" cy="8" r="4" fill="#FF5F56" />
    <circle cx="24" cy="8" r="4" fill="#FFBD2E" />
    <circle cx="38" cy="8" r="4" fill="#27C93F" />
    <text x="56" y="12" fill="#64748B" font-family="'Fira Code', monospace" font-size="11" font-weight="700">kathyayini26 / .hostfile --live</text>
  </g>

  <!-- LEFT CARD: REAL CODE TEXT MATRIX PORTRAIT OF KATHYAYINI -->
  <g transform="translate(24, 38)">
    <rect width="240" height="224" rx="12" fill="#0D1117" stroke="#38BDF8" stroke-width="1.2" filter="url(#code-glow)" />

    <!-- Card Top Label -->
    <text x="14" y="20" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" letter-spacing="1">VISUAL_MAP / PORTRAIT_GLOBAL</text>
    <line x1="14" y1="26" x2="226" y2="26" stroke="#1E293B" stroke-width="1" />

    <!-- Rotating Radar Scanner Circle -->
    <circle cx="120" cy="118" r="75" fill="none" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="0 120 118" to="360 120 118" dur="14s" repeatCount="indefinite" />
    </circle>

    <!-- PURE CODE TEXT WEAVING YOUR PORTRAIT (FACE, EYES, SMILE & HAIR IN ACTUAL CODE TOKENS) -->
    <g font-family="'Fira Code', monospace" font-weight="700" filter="url(#code-glow)">
    {matrix_code_str}
    </g>

    <!-- Scanning Laser Line -->
    <line x1="16" y1="50" x2="224" y2="50" stroke="#00F2FE" stroke-width="1.5" filter="url(#code-glow)">
      <animate attributeName="y1" values="35;205;35" dur="3.5s" repeatCount="indefinite" />
      <animate attributeName="y2" values="35;205;35" dur="3.5s" repeatCount="indefinite" />
    </line>

    <!-- Status Bar -->
    <rect x="14" y="196" width="212" height="18" rx="4" fill="#161B22" />
    <circle cx="24" cy="205" r="3" fill="#10B981" />
    <text x="32" y="208" fill="#34D399" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700">CODE_PORTRAIT_STREAM [200_OK]</text>
  </g>

  <!-- RIGHT CARD: TERMINAL DEVELOPER INFO -->
  <g transform="translate(280, 38)">
    <rect width="496" height="224" rx="12" fill="#0D1117" stroke="#334155" stroke-width="1.2" />

    <!-- Terminal Prompt Content -->
    <g font-family="'Fira Code', monospace" font-size="11" font-weight="500" fill="#CBD5E1">
      <text x="18" y="24">
        <tspan fill="#38BDF8" font-weight="800">SYSTEM.INFO</tspan> <tspan fill="#64748B">/ HARDWARE.SYS / 700</tspan>
      </text>

      <line x1="18" y1="32" x2="478" y2="32" stroke="#1E293B" stroke-width="1" />

      <text x="18" y="50"><tspan fill="#94A3B8">Subject:</tspan>     <tspan fill="#F8FAFC" font-weight="800">Kathyayini Prabhu</tspan></text>
      <text x="18" y="68"><tspan fill="#94A3B8">Role:</tspan>        <tspan fill="#38BDF8" font-weight="700">3rd Year AI &amp; Data Science Student</tspan></text>
      <text x="18" y="86"><tspan fill="#94A3B8">Affiliation:</tspan> <tspan fill="#E2E8F0">BMS College of Engineering (BMSCE)</tspan></text>
      <text x="18" y="104"><tspan fill="#94A3B8">Base:</tspan>        <tspan fill="#E2E8F0">Bengaluru, India</tspan></text>
      <text x="18" y="122"><tspan fill="#94A3B8">Status:</tspan>      <tspan fill="#34D399" font-weight="700">Researching / Building / Engineering</tspan></text>

      <line x1="18" y1="130" x2="478" y2="130" stroke="#1E293B" stroke-width="1" />

      <text x="18" y="146"><tspan fill="#34D399" font-weight="800">RESEARCH.ITEM</tspan></text>
      <text x="18" y="162"> <tspan fill="#94A3B8">Primary:</tspan>    <tspan fill="#F8FAFC">Machine Learning, AI &amp; Data Science</tspan></text>
      <text x="18" y="178"> <tspan fill="#94A3B8">Direction:</tspan>  <tspan fill="#F8FAFC">Predictive Models &amp; SQL Architectures</tspan></text>
    </g>

    <!-- Bottom Action Badges -->
    <g transform="translate(18, 192)">
      <rect width="64" height="20" rx="4" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
      <text x="32" y="14" fill="#94A3B8" font-family="'Fira Code', monospace" font-size="9" font-weight="700" text-anchor="middle">GITHUB</text>

      <rect x="72" width="95" height="20" rx="4" fill="#1E293B" stroke="#38BDF8" stroke-width="0.8" />
      <text x="119.5" y="14" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">KATHYAYINI</text>

      <rect x="175" width="95" height="20" rx="4" fill="#0969DA" />
      <text x="222.5" y="14" fill="#FFFFFF" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">&#9650; PORTFOLIO</text>

      <rect x="278" width="60" height="20" rx="4" fill="#1E293B" stroke="#34D399" stroke-width="0.8" />
      <text x="308" y="14" fill="#34D399" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">BMSCE</text>

      <rect x="346" width="112" height="20" rx="4" fill="#1E293B" stroke="#A78BFA" stroke-width="0.8" />
      <text x="402" y="14" fill="#A78BFA" font-family="'Fira Code', monospace" font-size="9" font-weight="800" text-anchor="middle">AI / DS / ASSETS</text>
    </g>
  </g>
</svg>'''

# Validate XML strictly
ET.fromstring(svg_code)
print("Code Portrait XML Validation: 100% PASSED!")

with open(r'C:\Users\Kathyayini\.gemini\antigravity\scratch\Kathyayini-12\assets\header-codepreview.svg', 'w', encoding='utf-8') as f:
    f.write(svg_code)

print("header-codepreview.svg written successfully!")
