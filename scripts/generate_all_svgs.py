"""
Master SVG Suite Generator for Navari Yashwanth Reddy's Engineering Command Center.
Generates all bespoke, self-hosted, 100% XML-compliant vector graphics with 0 external API dependencies.
"""
import os
import xml.etree.ElementTree as ET

def make_section_header(title, subtitle, tag, color="#F97316", secondary="#38BDF8"):
    tag_clean = tag.replace("-", "_").replace(" ", "_")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 62" width="100%" height="62">
  <defs>
    <linearGradient id="secBg_{tag_clean}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#090E1A" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="secBorder_{tag_clean}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{color}" />
      <stop offset="50%" stop-color="{secondary}" />
      <stop offset="100%" stop-color="#10B981" />
    </linearGradient>
    <filter id="glow_{tag_clean}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono {{ font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace; }}
    .sec-title {{ font-size: 14px; font-weight: 800; fill: {color}; letter-spacing: 1.5px; text-transform: uppercase; }}
    .sec-sub {{ font-size: 10px; font-weight: 600; fill: #94A3B8; letter-spacing: 0.8px; text-transform: uppercase; }}
    .badge-text {{ font-size: 9px; font-weight: 700; fill: #F8FAFC; text-anchor: middle; }}
    .pulse-node {{ animation: pulseNode_{tag_clean} 2.5s infinite ease-in-out; }}
    @keyframes pulseNode_{tag_clean} {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.4; }}
    }}
  </style>

  <!-- Container -->
  <rect x="2" y="2" width="876" height="58" rx="8" fill="url(#secBg_{tag_clean})" stroke="#334155" stroke-width="1.2" />
  <path d="M 2 12 L 12 2 M 878 12 L 868 2 M 2 50 L 12 60 M 878 50 L 868 60" stroke="{color}" stroke-width="1.5" />

  <!-- Left Indicator -->
  <g transform="translate(18, 31)">
    <circle cx="0" cy="0" r="5" fill="{color}" class="pulse-node" filter="url(#glow_{tag_clean})" />
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF" />
  </g>

  <!-- Titles -->
  <text x="36" y="27" class="mono sec-title">{title}</text>
  <text x="36" y="45" class="mono sec-sub">{subtitle}</text>

  <!-- Right Cyber Tag -->
  <g transform="translate(740, 18)">
    <rect x="0" y="0" width="115" height="24" rx="4" fill="#0B1120" stroke="{color}" stroke-width="1" />
    <text x="57.5" y="16" class="mono badge-text">// {tag}</text>
  </g>
</svg>'''

def make_project_card(name, category, lang, desc1, desc2, metrics, color="#F97316"):
    name_clean = name.replace("-", "_").replace(" ", "_")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 150" width="100%" height="150">
  <defs>
    <linearGradient id="pcardBg_{name_clean}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="60%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <filter id="pcardShadow_{name_clean}" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <style>
    .mono {{ font-family: 'Fira Code', 'JetBrains Mono', monospace; }}
    .p-title {{ font-size: 13.5px; font-weight: 700; fill: {color}; }}
    .p-cat {{ font-size: 9px; font-weight: 700; fill: #94A3B8; text-transform: uppercase; letter-spacing: 0.8px; }}
    .p-desc {{ font-size: 10px; fill: #CBD5E1; }}
    .p-metric {{ font-size: 9px; font-weight: 600; fill: #38BDF8; }}
    .pill-box {{ rx: 3px; fill: #1E293B; }}
    .pill-txt {{ font-size: 8.5px; font-weight: 700; fill: #F8FAFC; text-anchor: middle; }}
  </style>

  <rect x="2" y="2" width="416" height="146" rx="10" fill="url(#pcardBg_{name_clean})" stroke="#334155" stroke-width="1.2" filter="url(#pcardShadow_{name_clean})" />
  <line x1="16" y1="36" x2="404" y2="36" stroke="#1E293B" stroke-width="1" />

  <!-- Top Line: Title and Category -->
  <g transform="translate(18, 24)">
    <text x="0" y="0" class="mono p-title">{name}</text>
    <text x="384" y="0" class="mono p-cat" text-anchor="end">{category}</text>
  </g>

  <!-- Description -->
  <g transform="translate(18, 56)">
    <text x="0" y="0" class="mono p-desc">{desc1}</text>
    <text x="0" y="16" class="mono p-desc">{desc2}</text>
  </g>

  <!-- Footer Tags and Metrics -->
  <g transform="translate(18, 102)">
    <rect x="0" y="0" width="86" height="20" class="pill-box" stroke="{color}" stroke-width="0.8" />
    <text x="43" y="13.5" class="mono pill-txt">{lang}</text>

    <text x="384" y="14" class="mono p-metric" text-anchor="end">⚡ {metrics}</text>
  </g>
</svg>'''

def make_interactive_terminal():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 220" width="100%" height="220">
  <defs>
    <linearGradient id="termBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040A" />
      <stop offset="100%" stop-color="#080E1A" />
    </linearGradient>
  </defs>

  <style>
    .term-font { font-family: 'Fira Code', 'JetBrains Mono', 'Courier New', monospace; }
    .term-prompt { font-size: 11.5px; font-weight: 700; fill: #10B981; }
    .term-cmd { font-size: 11.5px; font-weight: 600; fill: #F8FAFC; }
    .term-ok { font-size: 11px; font-weight: 700; fill: #38BDF8; }
    .term-text { font-size: 11px; fill: #94A3B8; }
    .term-highlight { font-size: 11px; font-weight: 700; fill: #F59E0B; }
    .term-cursor { animation: blinkCur 1s infinite; fill: #10B981; }
    @keyframes blinkCur { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
  </style>

  <rect x="2" y="2" width="876" height="216" rx="10" fill="url(#termBg)" stroke="#1E293B" stroke-width="1.5" />

  <!-- Terminal Top Bar -->
  <rect x="2" y="2" width="876" height="32" rx="10" fill="#0B1120" />
  <circle cx="20" cy="17" r="5" fill="#EF4444" />
  <circle cx="36" cy="17" r="5" fill="#F59E0B" />
  <circle cx="52" cy="17" r="5" fill="#10B981" />
  <text x="440" y="21" class="term-font" style="font-size: 10px; font-weight: 600; fill: #64748B; text-anchor: middle;">yashwanth@command-node-01: ~ (zsh)</text>

  <!-- Commands and Outputs -->
  <g transform="translate(24, 60)">
    <text x="0" y="0" class="term-font term-prompt">yashwanth@node-01<tspan fill="#64748B">:</tspan><tspan fill="#38BDF8">~</tspan><tspan fill="#F8FAFC">$</tspan></text>
    <text x="180" y="0" class="term-font term-cmd">./init_production_matrix.sh --mode=mission-critical</text>

    <text x="0" y="26" class="term-font term-ok">[OK]</text>
    <text x="36" y="26" class="term-font term-text">Linux Kernel 6.1.0-x86_64 loaded • Distributed coroutine runtime active</text>

    <text x="0" y="48" class="term-font term-ok">[OK]</text>
    <text x="36" y="48" class="term-font term-text">Hardware Driver initialized • <tspan class="term-highlight">Patent No: 470097-001</tspan> M2M bus verified</text>

    <text x="0" y="70" class="term-font term-ok">[OK]</text>
    <text x="36" y="70" class="term-font term-text">AI Inference Server listening on <tspan fill="#10B981">tcp://0.0.0.0:8000</tspan> (FastAPI + YOLO + SMOTE)</text>

    <text x="0" y="92" class="term-font term-ok">[OK]</text>
    <text x="36" y="92" class="term-font term-text">3D WebGL Portfolio link mapped: <tspan fill="#38BDF8">https://yashwanthnavari.github.io/yashwanth-portfolio/</tspan></text>

    <text x="0" y="120" class="term-font term-prompt">yashwanth@node-01<tspan fill="#64748B">:</tspan><tspan fill="#38BDF8">~</tspan><tspan fill="#F8FAFC">$</tspan></text>
    <text x="180" y="120" class="term-font term-cmd">status --telemetry --verbose</text>
    <rect x="420" y="108" width="8" height="14" class="term-cursor" />
  </g>
</svg>'''

def make_model_benchmarks():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 180" width="100%" height="180">
  <defs>
    <linearGradient id="benchBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .b-num { font-size: 22px; font-weight: 800; }
    .b-label { font-size: 10px; font-weight: 700; fill: #94A3B8; text-transform: uppercase; }
    .b-desc { font-size: 9px; fill: #CBD5E1; }
  </style>

  <rect x="2" y="2" width="876" height="176" rx="10" fill="url(#benchBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #F97316; letter-spacing: 1px;">EMPIRICAL SYSTEM BENCHMARKS AND RUNTIME LATENCY</text>
  </g>

  <!-- 4 Benchmark Cards -->
  <!-- Card 1: CV Latency -->
  <g transform="translate(20, 44)">
    <rect x="0" y="0" width="200" height="114" rx="6" fill="#0B1120" stroke="#38BDF8" stroke-width="1" />
    <text x="16" y="32" class="mono b-num" style="fill: #38BDF8;">18.2 ms</text>
    <text x="16" y="52" class="mono b-label">Computer Vision Inference</text>
    <text x="16" y="72" class="mono b-desc">• YOLOv8 / OpenCV Cuda</text>
    <text x="16" y="88" class="mono b-desc">• 55 FPS Real-Time Stream</text>
  </g>

  <!-- Card 2: False Negative Rate -->
  <g transform="translate(232, 44)">
    <rect x="0" y="0" width="200" height="114" rx="6" fill="#0B1120" stroke="#10B981" stroke-width="1" />
    <text x="16" y="32" class="mono b-num" style="fill: #10B981;">0.00%</text>
    <text x="16" y="52" class="mono b-label">Clinical False-Negative Rate</text>
    <text x="16" y="72" class="mono b-desc">• SMOTE Imbalance Ratio</text>
    <text x="16" y="88" class="mono b-desc">• Cost-Sensitive Risk Bound</text>
  </g>

  <!-- Card 3: M2M Packet Delivery -->
  <g transform="translate(444, 44)">
    <rect x="0" y="0" width="200" height="114" rx="6" fill="#0B1120" stroke="#F59E0B" stroke-width="1" />
    <text x="16" y="32" class="mono b-num" style="fill: #F59E0B;">99.98%</text>
    <text x="16" y="52" class="mono b-label">M2M Ingestion Fidelity</text>
    <text x="16" y="72" class="mono b-desc">• Patent 470097-001 Protocol</text>
    <text x="16" y="88" class="mono b-desc">• Zero Buffer Overflow</text>
  </g>

  <!-- Card 4: Compression Ratio -->
  <g transform="translate(656, 44)">
    <rect x="0" y="0" width="204" height="114" rx="6" fill="#0B1120" stroke="#A855F7" stroke-width="1" />
    <text x="16" y="32" class="mono b-num" style="fill: #A855F7;">82.4%</text>
    <text x="16" y="52" class="mono b-label">Bundle Bloat Reduction</text>
    <text x="16" y="72" class="mono b-desc">• DeveloperZip AST Engine</text>
    <text x="16" y="88" class="mono b-desc">• Intelligent Cache Prune</text>
  </g>
</svg>'''

def make_pcb_pinout():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="100%" height="200">
  <defs>
    <linearGradient id="pcbBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06120D" />
      <stop offset="50%" stop-color="#0B1C14" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .pcb-title { font-size: 12px; font-weight: 800; fill: #10B981; letter-spacing: 1px; }
    .pin-label { font-size: 9px; font-weight: 700; fill: #F59E0B; }
    .pin-sub { font-size: 8.5px; fill: #94A3B8; }
    .chip-text { font-size: 11px; font-weight: 800; fill: #F8FAFC; text-anchor: middle; }
  </style>

  <rect x="2" y="2" width="876" height="196" rx="10" fill="url(#pcbBg)" stroke="#059669" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono pcb-title">PATENT 470097-001 HARDWARE SCHEMATIC AND PINOUT ARCHITECTURE</text>
  </g>

  <!-- Center Microcontroller Chip -->
  <g transform="translate(440, 114)">
    <rect x="-100" y="-45" width="200" height="90" rx="6" fill="#0B1120" stroke="#10B981" stroke-width="1.5" />
    <text x="0" y="-12" class="mono chip-text">PATENTED M2M MCU</text>
    <text x="0" y="6" class="mono" style="font-size: 9px; fill: #10B981; text-anchor: middle;">32-BIT DUAL CORE @ 240MHz</text>
    <text x="0" y="24" class="mono" style="font-size: 8px; fill: #64748B; text-anchor: middle;">LOW POWER SLEEP STATES</text>
  </g>

  <!-- Left Pin Bus: Sensor Input -->
  <g transform="translate(40, 60)">
    <rect x="0" y="0" width="240" height="110" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono pin-label">BUS A: ANALOG / DIGITAL SENSORS</text>
    <text x="14" y="44" class="mono pin-sub">• GPIO 32-35 : ADC 12-Bit Soil N-P-K</text>
    <text x="14" y="62" class="mono pin-sub">• GPIO 21 (SDA) / 22 (SCL) : I2C Bus</text>
    <text x="14" y="80" class="mono pin-sub">• GPIO 18,19,23 : SPI High-Speed Bus</text>
  </g>

  <line x1="280" y1="114" x2="340" y2="114" stroke="#10B981" stroke-width="1.5" stroke-dasharray="3 3" />

  <!-- Right Pin Bus: Telemetry & Power -->
  <g transform="translate(600, 60)">
    <rect x="0" y="0" width="240" height="110" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono pin-label" style="fill: #38BDF8;">BUS B: TELEMETRY AND POWER REG</text>
    <text x="14" y="44" class="mono pin-sub">• TX0 / RX0 : Hardware UART Ingestion</text>
    <text x="14" y="62" class="mono pin-sub">• LDO Step-Down : 5.0V to 3.3V Low-Noise</text>
    <text x="14" y="80" class="mono pin-sub">• RF Transceiver : 2.4GHz M2M Uplink</text>
  </g>

  <line x1="540" y1="114" x2="600" y2="114" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3" />
</svg>'''

def make_microservices_architecture():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="100%" height="200">
  <defs>
    <linearGradient id="msBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .ms-title { font-size: 11px; font-weight: 700; fill: #F8FAFC; }
    .ms-sub { font-size: 8.5px; fill: #94A3B8; }
    .ms-tag { font-size: 8px; font-weight: 700; fill: #38BDF8; }
    .ms-arr { stroke: #38BDF8; stroke-width: 1.5; stroke-dasharray: 3 3; }
  </style>

  <rect x="2" y="2" width="876" height="196" rx="10" fill="url(#msBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #38BDF8; letter-spacing: 1px;">DISTRIBUTED MICROSERVICES AND HIGH-AVAILABILITY CLOUD TOPOLOGY</text>
  </g>

  <!-- Node 1: Client Gateway -->
  <g transform="translate(20, 48)">
    <rect x="0" y="0" width="180" height="130" rx="6" fill="#0B1120" stroke="#F97316" stroke-width="1" />
    <text x="14" y="24" class="mono ms-title">01. REVERSE PROXY</text>
    <text x="14" y="48" class="mono ms-sub">• NGINX / Envoy Gateway</text>
    <text x="14" y="66" class="mono ms-sub">• Rate Limiting (Token Bucket)</text>
    <text x="14" y="84" class="mono ms-sub">• SSL/TLS Termination</text>
    <text x="14" y="112" class="mono ms-tag">HTTPS / WSS / gRPC</text>
  </g>

  <line x1="202" y1="113" x2="238" y2="113" class="ms-arr" />

  <!-- Node 2: App Services -->
  <g transform="translate(240, 48)">
    <rect x="0" y="0" width="190" height="130" rx="6" fill="#0B1120" stroke="#38BDF8" stroke-width="1" />
    <text x="14" y="24" class="mono ms-title">02. ASYNC CORE</text>
    <text x="14" y="48" class="mono ms-sub">• FastAPI REST Service</text>
    <text x="14" y="66" class="mono ms-sub">• JWT / RBAC Middleware</text>
    <text x="14" y="84" class="mono ms-sub">• Non-Blocking Coroutines</text>
    <text x="14" y="112" class="mono ms-tag">PyTest 100% Tested</text>
  </g>

  <line x1="432" y1="113" x2="468" y2="113" class="ms-arr" />

  <!-- Node 3: AI Inference Workers -->
  <g transform="translate(470, 48)">
    <rect x="0" y="0" width="190" height="130" rx="6" fill="#0B1120" stroke="#A855F7" stroke-width="1" />
    <text x="14" y="24" class="mono ms-title">03. INFERENCE WORKERS</text>
    <text x="14" y="48" class="mono ms-sub">• PyTorch &amp; YOLO Pipeline</text>
    <text x="14" y="66" class="mono ms-sub">• SMOTE Imbalance Classifier</text>
    <text x="14" y="84" class="mono ms-sub">• OpenCV GPU Streaming</text>
    <text x="14" y="112" class="mono ms-tag">18.2ms per Frame</text>
  </g>

  <line x1="662" y1="113" x2="698" y2="113" class="ms-arr" />

  <!-- Node 4: Sharded Storage -->
  <g transform="translate(700, 48)">
    <rect x="0" y="0" width="160" height="130" rx="6" fill="#0B1120" stroke="#10B981" stroke-width="1" />
    <text x="14" y="24" class="mono ms-title">04. STORAGE</text>
    <text x="14" y="48" class="mono ms-sub">• PostgreSQL ACID</text>
    <text x="14" y="66" class="mono ms-sub">• Redis Pub/Sub Cache</text>
    <text x="14" y="84" class="mono ms-sub">• AWS S3 Object Store</text>
    <text x="14" y="112" class="mono ms-tag">Sub-5ms Query</text>
  </g>
</svg>'''

def make_cnn_architecture():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 180" width="100%" height="180">
  <defs>
    <linearGradient id="cnnBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .c-title { font-size: 11px; font-weight: 700; fill: #F8FAFC; }
    .c-sub { font-size: 8.5px; fill: #94A3B8; }
    .c-tag { font-size: 8px; font-weight: 700; fill: #C084FC; }
    .c-arr { stroke: #C084FC; stroke-width: 1.5; stroke-dasharray: 3 3; }
  </style>

  <rect x="2" y="2" width="876" height="176" rx="10" fill="url(#cnnBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #C084FC; letter-spacing: 1px;">DEEP CONVOLUTIONAL NEURAL NETWORK (CNN) VISION PIPELINE</text>
  </g>

  <!-- Stage 1 -->
  <g transform="translate(20, 44)">
    <rect x="0" y="0" width="180" height="114" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono c-title">01. INPUT TENSOR</text>
    <text x="14" y="44" class="mono c-sub">• 224 x 224 x 3 RGB Frame</text>
    <text x="14" y="62" class="mono c-sub">• Data Augmentation Norm</text>
    <text x="14" y="80" class="mono c-sub">• Grayscale / CLAHE Equal</text>
    <text x="14" y="98" class="mono c-tag">Pre-processed</text>
  </g>

  <line x1="202" y1="101" x2="238" y2="101" class="c-arr" />

  <!-- Stage 2 -->
  <g transform="translate(240, 44)">
    <rect x="0" y="0" width="190" height="114" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono c-title">02. FEATURE EXTRACTOR</text>
    <text x="14" y="44" class="mono c-sub">• Conv2D (3x3, 64-256 Filters)</text>
    <text x="14" y="62" class="mono c-sub">• BatchNorm + ReLU Activations</text>
    <text x="14" y="80" class="mono c-sub">• Residual Skip Connections</text>
    <text x="14" y="98" class="mono c-tag">Hierarchical Edges</text>
  </g>

  <line x1="432" y1="101" x2="468" y2="101" class="c-arr" />

  <!-- Stage 3 -->
  <g transform="translate(470, 44)">
    <rect x="0" y="0" width="190" height="114" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono c-title">03. BOTTLENECK &amp; POOL</text>
    <text x="14" y="44" class="mono c-sub">• Max Pooling 2x2 Spatial</text>
    <text x="14" y="62" class="mono c-sub">• Global Average Pooling (GAP)</text>
    <text x="14" y="80" class="mono c-sub">• Dropout 0.4 Regularization</text>
    <text x="14" y="98" class="mono c-tag">Zero Overfitting</text>
  </g>

  <line x1="662" y1="101" x2="698" y2="101" class="c-arr" />

  <!-- Stage 4 -->
  <g transform="translate(700, 44)">
    <rect x="0" y="0" width="160" height="114" rx="6" fill="#0B1120" stroke="#C084FC" stroke-width="1.2" />
    <text x="14" y="22" class="mono c-title">04. CLASSIFIER</text>
    <text x="14" y="44" class="mono c-sub">• Dense Softmax (7 Class)</text>
    <text x="14" y="62" class="mono c-sub">• Cross-Entropy Loss</text>
    <text x="14" y="80" class="mono c-sub">• Bounding Box Triage</text>
    <text x="14" y="98" class="mono c-tag">Live Overlay</text>
  </g>
</svg>'''

def make_zero_trust_security():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 180" width="100%" height="180">
  <defs>
    <linearGradient id="secModelBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .s-title { font-size: 11.5px; font-weight: 700; fill: #F8FAFC; }
    .s-sub { font-size: 8.5px; fill: #94A3B8; }
    .s-tag { font-size: 8px; font-weight: 700; fill: #EF4444; }
  </style>

  <rect x="2" y="2" width="876" height="176" rx="10" fill="url(#secModelBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #EF4444; letter-spacing: 1px;">ZERO-TRUST CYBERSECURITY AND DEFENSE MATRIX</text>
  </g>

  <!-- 4 Pillars -->
  <g transform="translate(20, 44)">
    <rect x="0" y="0" width="200" height="114" rx="6" fill="#0B1120" stroke="#EF4444" stroke-width="1" />
    <text x="14" y="22" class="mono s-title">01. AUTHENTICATION</text>
    <text x="14" y="44" class="mono s-sub">• Cryptographic mTLS Handshake</text>
    <text x="14" y="62" class="mono s-sub">• JWT Secret Hash Rotation</text>
    <text x="14" y="80" class="mono s-sub">• Public Key Verification</text>
    <text x="14" y="100" class="mono s-tag">Zero Replay Attacks</text>
  </g>

  <g transform="translate(232, 44)">
    <rect x="0" y="0" width="200" height="114" rx="6" fill="#0B1120" stroke="#F59E0B" stroke-width="1" />
    <text x="14" y="22" class="mono s-title">02. AUTHORIZATION (RBAC)</text>
    <text x="14" y="44" class="mono s-sub">• Role-Based Endpoint Isolation</text>
    <text x="14" y="62" class="mono s-sub">• Principle of Least Privilege</text>
    <text x="14" y="80" class="mono s-sub">• Scoped Token Claims</text>
    <text x="14" y="100" class="mono s-tag" style="fill: #F59E0B;">Strict Granularity</text>
  </g>

  <g transform="translate(444, 44)">
    <rect x="0" y="0" width="200" height="114" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono s-title">03. INPUT DEFENSE</text>
    <text x="14" y="44" class="mono s-sub">• SQL Injection Escaping</text>
    <text x="14" y="62" class="mono s-sub">• XSS Content Sanitization</text>
    <text x="14" y="80" class="mono s-sub">• Rate-Limited Brute Force Guard</text>
    <text x="14" y="100" class="mono s-tag" style="fill: #38BDF8;">OWASP Compliant</text>
  </g>

  <g transform="translate(656, 44)">
    <rect x="0" y="0" width="204" height="114" rx="6" fill="#0B1120" stroke="#10B981" stroke-width="1" />
    <text x="14" y="22" class="mono s-title">04. ENCRYPTION</text>
    <text x="14" y="44" class="mono s-sub">• AES-256 GCM at Rest</text>
    <text x="14" y="62" class="mono s-sub">• TLS 1.3 in Transit</text>
    <text x="14" y="80" class="mono s-sub">• Hardware HSM Keystore</text>
    <text x="14" y="100" class="mono s-tag" style="fill: #10B981;">End-to-End Encrypted</text>
  </g>
</svg>'''

def make_career_roadmap():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 190" width="100%" height="190">
  <defs>
    <linearGradient id="roadBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .r-year { font-size: 12px; font-weight: 800; fill: #F97316; }
    .r-title { font-size: 10.5px; font-weight: 700; fill: #F8FAFC; }
    .r-sub { font-size: 8.5px; fill: #94A3B8; }
  </style>

  <rect x="2" y="2" width="876" height="186" rx="10" fill="url(#roadBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #F59E0B; letter-spacing: 1px;">CAREER AND ENGINEERING INNOVATION MILESTONES</text>
  </g>

  <!-- Horizontal Timeline Bar -->
  <line x1="40" y1="58" x2="840" y2="58" stroke="#334155" stroke-width="2" />

  <!-- 5 Milestones -->
  <!-- 2022 -->
  <g transform="translate(60, 58)">
    <circle cx="0" cy="0" r="6" fill="#38BDF8" />
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF" />
    <text x="0" y="22" class="mono r-year" text-anchor="middle">2022</text>
    <text x="0" y="38" class="mono r-title" text-anchor="middle">Algorithms Core</text>
    <text x="0" y="52" class="mono r-sub" text-anchor="middle">Data Structures</text>
    <text x="0" y="66" class="mono r-sub" text-anchor="middle">Java and Python</text>
  </g>

  <!-- 2023 -->
  <g transform="translate(240, 58)">
    <circle cx="0" cy="0" r="6" fill="#10B981" />
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF" />
    <text x="0" y="22" class="mono r-year" text-anchor="middle" style="fill: #10B981;">2023</text>
    <text x="0" y="38" class="mono r-title" text-anchor="middle">Embedded Systems</text>
    <text x="0" y="52" class="mono r-sub" text-anchor="middle">Microcontroller IO</text>
    <text x="0" y="66" class="mono r-sub" text-anchor="middle">Sensor Bus Routing</text>
  </g>

  <!-- 2024 -->
  <g transform="translate(430, 58)">
    <circle cx="0" cy="8" r="8" fill="#F59E0B" />
    <circle cx="0" cy="8" r="3.5" fill="#FFFFFF" />
    <text x="0" y="30" class="mono r-year" text-anchor="middle" style="fill: #F59E0B;">2024</text>
    <text x="0" y="46" class="mono r-title" text-anchor="middle" style="fill: #F59E0B;">Patent Granted</text>
    <text x="0" y="60" class="mono r-sub" text-anchor="middle">Design: 470097-001</text>
    <text x="0" y="74" class="mono r-sub" text-anchor="middle">Govt. of India</text>
  </g>

  <!-- 2025 -->
  <g transform="translate(620, 58)">
    <circle cx="0" cy="0" r="6" fill="#C084FC" />
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF" />
    <text x="0" y="22" class="mono r-year" text-anchor="middle" style="fill: #C084FC;">2025</text>
    <text x="0" y="38" class="mono r-title" text-anchor="middle">Production AI/ML</text>
    <text x="0" y="52" class="mono r-sub" text-anchor="middle">Multi-Agent AI</text>
    <text x="0" y="66" class="mono r-sub" text-anchor="middle">Computer Vision</text>
  </g>

  <!-- 2026 -->
  <g transform="translate(800, 58)">
    <circle cx="0" cy="0" r="6" fill="#F97316" />
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF" />
    <text x="0" y="22" class="mono r-year" text-anchor="middle" style="fill: #F97316;">2026</text>
    <text x="0" y="38" class="mono r-title" text-anchor="middle">Distributed Cloud</text>
    <text x="0" y="52" class="mono r-sub" text-anchor="middle">3D WebGL Portfolios</text>
    <text x="0" y="66" class="mono r-sub" text-anchor="middle">Enterprise Scale</text>
  </g>
</svg>'''

def make_trophy_showcase():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 160" width="100%" height="160">
  <defs>
    <linearGradient id="tropBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140C1A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .t-head { font-size: 11px; font-weight: 800; fill: #F59E0B; }
    .t-body { font-size: 9px; fill: #F8FAFC; }
    .t-sub { font-size: 8px; fill: #94A3B8; }
  </style>

  <rect x="2" y="2" width="876" height="156" rx="10" fill="url(#tropBg)" stroke="#F59E0B" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #F59E0B; letter-spacing: 1px;">ACADEMIC HONORS AND ENGINEERING DISTINCTIONS</text>
  </g>

  <!-- 4 Award Columns -->
  <!-- Award 1 -->
  <g transform="translate(20, 42)">
    <rect x="0" y="0" width="200" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono t-head">🏆 GRANTED PATENT</text>
    <text x="14" y="42" class="mono t-body">Design No: 470097-001</text>
    <text x="14" y="60" class="mono t-sub">• Govt. of India Intellectual Property</text>
    <text x="14" y="76" class="mono t-sub">• IoT Connectivity Architecture</text>
  </g>

  <!-- Award 2 -->
  <g transform="translate(232, 42)">
    <rect x="0" y="0" width="200" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono t-head" style="fill: #38BDF8;">🎓 WOXSEN SCHOLAR</text>
    <text x="14" y="42" class="mono t-body">Data Science Scholar</text>
    <text x="14" y="60" class="mono t-sub">• Woxsen University, Hyderabad</text>
    <text x="14" y="76" class="mono t-sub">• AI Systems and Analytics</text>
  </g>

  <!-- Award 3 -->
  <g transform="translate(444, 42)">
    <rect x="0" y="0" width="200" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono t-head" style="fill: #10B981;">🥇 HACKERRANK VERIFIED</text>
    <text x="14" y="42" class="mono t-body">5-Star Python and React</text>
    <text x="14" y="60" class="mono t-sub">• Problem Solving Proficiency</text>
    <text x="14" y="76" class="mono t-sub">• Frontend and Go Proficiency</text>
  </g>

  <!-- Award 4 -->
  <g transform="translate(656, 42)">
    <rect x="0" y="0" width="204" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono t-head" style="fill: #C084FC;">📜 GLOBAL SPECIALIZATIONS</text>
    <text x="14" y="42" class="mono t-body">Duke, NYU and UC Irvine</text>
    <text x="14" y="60" class="mono t-sub">• Quantum, Cyber Defense, C</text>
    <text x="14" y="76" class="mono t-sub">• Alberta OOP Architecture</text>
  </g>
</svg>'''

def make_collaboration_protocol():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 150" width="100%" height="150">
  <defs>
    <linearGradient id="collabBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .c-head { font-size: 11.5px; font-weight: 700; fill: #F8FAFC; }
    .c-desc { font-size: 8.5px; fill: #94A3B8; }
    .c-act { font-size: 8px; font-weight: 700; fill: #10B981; }
  </style>

  <rect x="2" y="2" width="876" height="146" rx="10" fill="url(#collabBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #10B981; letter-spacing: 1px;">COLLABORATION PROTOCOL AND ENGINEERING DIRECTIVES</text>
  </g>

  <!-- 3 Action Blocks -->
  <g transform="translate(20, 42)">
    <rect x="0" y="0" width="268" height="88" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono c-head">🔬 Research and AI Inquiries</text>
    <text x="14" y="42" class="mono c-desc">• Multi-Agent LLM Orchestration</text>
    <text x="14" y="58" class="mono c-desc">• Computer Vision and Model Optimization</text>
    <text x="14" y="76" class="mono c-act">Open for High-Impact Projects</text>
  </g>

  <g transform="translate(304, 42)">
    <rect x="0" y="0" width="268" height="88" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono c-head">🖲️ Hardware and IoT Architecture</text>
    <text x="14" y="42" class="mono c-desc">• Patented M2M Device Integration</text>
    <text x="14" y="58" class="mono c-desc">• Embedded C and Edge Telemetry</text>
    <text x="14" y="76" class="mono c-act">Patent Design 470097-001</text>
  </g>

  <g transform="translate(588, 42)">
    <rect x="0" y="0" width="272" height="88" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="14" y="22" class="mono c-head">💼 Technical Handshake</text>
    <text x="14" y="42" class="mono c-desc">• Full-Stack Distributed Microservices</text>
    <text x="14" y="58" class="mono c-desc">• Interactive 3D WebGL Applications</text>
    <text x="14" y="76" class="mono c-act">LinkedIn and GitHub Direct</text>
  </g>
</svg>'''

def main():
    os.makedirs("profile", exist_ok=True)

    # Section Headers
    headers = [
        ("section-core-directives.svg", "THE CORE DIRECTIVES", "SYSTEMS ARCHITECTURE AND OPERATIONAL PHILOSOPHY", "DIRECTIVES", "#F97316", "#38BDF8"),
        ("section-telemetry.svg", "LIVE COMMAND TELEMETRY", "REAL-TIME COMPUTE, HEALTH AND TELEMETRY GAUGES", "TELEMETRY", "#38BDF8", "#10B981"),
        ("section-hardware.svg", "PATENTED HARDWARE AND M2M IOT", "GRANTED INVENTION SCHEMATICS AND FIRMWARE ROUTING", "PATENT-470097", "#F59E0B", "#F97316"),
        ("section-ai-pipeline.svg", "DETERMINISTIC MACHINE LEARNING", "END-TO-END INFERENCE AND ZERO-FALSE-NEGATIVE TRIAGE", "AI-ENGINE", "#C084FC", "#38BDF8"),
        ("section-flagship-projects.svg", "VERIFIED FLAGSHIP SYSTEMS", "DEPLOYED PRODUCTION PLATFORMS AND REPOSITORIES", "REPOSITORIES", "#10B981", "#38BDF8"),
        ("section-tech-arsenal.svg", "THE MASTER TECHNICAL ARSENAL", "LAYER-BY-LAYER COMPUTATIONAL STACK AND RUNTIMES", "TECH-STACK", "#F97316", "#A855F7"),
        ("section-credentials.svg", "VERIFIED ACADEMIC CREDENTIALS", "FORMAL CERTIFICATIONS AND ENGINEERING ACCREDITATIONS", "ACCREDITATION", "#38BDF8", "#10B981"),
        ("section-comm-links.svg", "COMMAND NETWORK HANDSHAKE", "OFFICIAL SOCIAL AND PROFESSIONAL COMM-LINKS", "COMM-LINKS", "#F97316", "#38BDF8"),
        ("section-research.svg", "APPLIED RESEARCH AND ML BENCHMARKS", "DATA SCIENCE PAPERS AND UNSUPERVISED STUDIES", "RESEARCH", "#F97316", "#38BDF8"),
        ("section-philosophy.svg", "ENGINEERING PHILOSOPHY AND PRINCIPLES", "FIRST-PRINCIPLES SYSTEMS AND ROBUST DESIGN RULES", "PHILOSOPHY", "#10B981", "#38BDF8"),
        ("section-iot-architecture.svg", "IOT TO CLOUD TOPOLOGY", "PHYSICAL INGESTION AND ASYNC TELEMETRY FLOW", "TOPOLOGY", "#F97316", "#10B981"),
        ("section-algorithmic-mastery.svg", "ALGORITHMIC COMPLEXITY AND DATA STRUCTURES", "COMPUTATIONAL OPTIMIZATIONS AND GRAPH THEORY", "ALGORITHMS", "#38BDF8", "#A855F7"),
        ("section-cicd-lifecycle.svg", "AUTOMATED CI/CD AND DEPLOYMENT LIFECYCLE", "CONTAINERIZATION AND RESILIENT ZERO-DOWNTIME RELEASES", "DEVOPS", "#10B981", "#38BDF8"),
        ("section-hardware-pinout.svg", "PATENTED HARDWARE PINOUT AND BUS SCHEMATICS", "LOW-LEVEL EMBEDDED BUSES AND POWER MANAGEMENT", "HARDWARE", "#10B981", "#F59E0B"),
        ("section-model-benchmarks.svg", "EMPIRICAL SYSTEM BENCHMARKS AND LATENCY", "MEASURED COMPUTATIONAL RUNTIME PERFORMANCE", "BENCHMARKS", "#F97316", "#38BDF8"),
        ("section-terminal-session.svg", "INTERACTIVE RUNTIME TERMINAL SESSION", "SIMULATED LINUX SHELL AND SERVICE INITIALIZATION", "CLI-NODE", "#10B981", "#38BDF8"),
        ("section-microservices.svg", "DISTRIBUTED CLOUD MICROSERVICES", "HIGH-AVAILABILITY ASYNC INGESTION AND GATEWAY", "MICROSERVICES", "#38BDF8", "#10B981"),
        ("section-cnn-architecture.svg", "DEEP LEARNING CONVOLUTIONAL VISION PIPELINE", "CNN HIERARCHICAL FEATURE EXTRACTION AND TRIAGE", "CNN-VISION", "#C084FC", "#38BDF8"),
        ("section-zero-trust-security.svg", "ZERO-TRUST CYBERSECURITY AND DEFENSE", "ENTERPRISE RBAC, MTLS AND HARDENED CRYPTO GATES", "SECURITY", "#EF4444", "#F59E0B"),
        ("section-roadmap-timeline.svg", "CAREER AND INNOVATION ROADMAP", "MILESTONES FROM ALGORITHMS TO GRANTED PATENTS", "ROADMAP", "#F59E0B", "#F97316"),
        ("section-trophies-accolades.svg", "ACADEMIC HONORS AND DISTINCTIONS", "GOVERNMENT PATENTS AND TOP CERTIFICATIONS", "HONORS", "#F59E0B", "#10B981"),
        ("section-collaboration-protocol.svg", "COLLABORATION PROTOCOL AND GUIDELINES", "TECHNICAL HANDSHAKE AND RESEARCH INQUIRIES", "PROTOCOL", "#10B981", "#38BDF8"),
    ]

    for fname, title, sub, tag, c1, c2 in headers:
        with open(os.path.join("profile", fname), "w", encoding="utf-8") as f:
            f.write(make_section_header(title, sub, tag, c1, c2))

    # Project Cards
    projects = [
        ("card-supportsphere.svg", "SupportSphere-AI", "AI Multi-Agent", "TypeScript / AI", "Enterprise conversational agent workflows", "with contextual retrieval and real-time dispatch.", "Multi-Agent System", "#F97316"),
        ("card-agrisathi.svg", "AgriSathi V3", "Agri-Tech Decision", "TypeScript / ML", "Soil N-P-K crop suitability recommendation", "and CNN-based leaf disease identification.", "1 Star • Deployed", "#10B981"),
        ("card-neurovision.svg", "NeuroVision ML", "Computer Vision", "Python / YOLO", "Custom deep learning YOLO object detection", "fine-tuned with real-time OpenCV inference.", "1 Star • Real-Time", "#38BDF8"),
        ("card-smartcampus.svg", "Smart Campus Network", "Security / Network", "Python / Security", "Zero-Trust automated access control simulation", "with RBAC segment isolation and firewall rules.", "1 Star • Zero-Trust", "#EAB308"),
        ("card-cricbuzz.svg", "Cricbuzz LiveStats", "Telemetry / Analytics", "PostgreSQL / ML", "Real-time sports match telemetry stream", "persisted in PostgreSQL and visual Streamlit.", "Live Streamlit UI", "#A855F7"),
        ("card-developerzip.svg", "DeveloperZip", "Developer Tooling", "TypeScript / Desktop", "Intelligent AST-aware project compression", "stripping node_modules and cache bloat by 80%.", "Desktop Utility", "#F97316"),
        ("card-netflix-clustering.svg", "Netflix ML Clustering", "Unsupervised NLP", "Jupyter / Python", "Topic modeling and K-Means clustering", "on multi-genre catalog with PCA vector spaces.", "NLP + Clustering", "#EF4444"),
        ("card-heart-disease.svg", "Heart Risk Prediction", "Supervised Clinical", "JavaScript / ML", "Clinical cardiovascular risk assessment", "with feature importance and calibrated thresholds.", "Clinical ML", "#EC4899"),
        ("card-deepfer.svg", "DeepFER-Live", "Facial Emotion CNN", "Python / Keras", "Real-time webcam facial emotion recognition", "trained on FER-2013 with OpenCV stream overlays.", "Real-Time CNN", "#38BDF8"),
    ]

    for fname, name, cat, lang, d1, d2, met, col in projects:
        with open(os.path.join("profile", fname), "w", encoding="utf-8") as f:
            f.write(make_project_card(name, cat, lang, d1, d2, met, col))

    # Architecture Schematics
    with open(os.path.join("profile", "interactive-terminal.svg"), "w", encoding="utf-8") as f:
        f.write(make_interactive_terminal())

    with open(os.path.join("profile", "model-benchmarks.svg"), "w", encoding="utf-8") as f:
        f.write(make_model_benchmarks())

    with open(os.path.join("profile", "pcb-pinout-diagram.svg"), "w", encoding="utf-8") as f:
        f.write(make_pcb_pinout())

    with open(os.path.join("profile", "microservices-architecture.svg"), "w", encoding="utf-8") as f:
        f.write(make_microservices_architecture())

    with open(os.path.join("profile", "cnn-neural-architecture.svg"), "w", encoding="utf-8") as f:
        f.write(make_cnn_architecture())

    with open(os.path.join("profile", "zero-trust-security-model.svg"), "w", encoding="utf-8") as f:
        f.write(make_zero_trust_security())

    with open(os.path.join("profile", "career-roadmap-timeline.svg"), "w", encoding="utf-8") as f:
        f.write(make_career_roadmap())

    with open(os.path.join("profile", "accolades-trophy-showcase.svg"), "w", encoding="utf-8") as f:
        f.write(make_trophy_showcase())

    with open(os.path.join("profile", "collaboration-protocol.svg"), "w", encoding="utf-8") as f:
        f.write(make_collaboration_protocol())

    print("All SVGs updated and generated.")

if __name__ == "__main__":
    main()
