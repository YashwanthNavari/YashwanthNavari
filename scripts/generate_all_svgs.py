"""
Script to generate all advanced Engineering Command Center SVGs.
Uses 100% pure standard ASCII characters (and / + / // / •) to guarantee flawless rendering.
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

def make_iot_cloud_architecture():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="100%" height="200">
  <defs>
    <linearGradient id="iotBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .node-title { font-size: 11.5px; font-weight: 700; fill: #F8FAFC; }
    .node-desc { font-size: 8.5px; fill: #94A3B8; }
    .flow-arrow { stroke: #F97316; stroke-width: 1.5; stroke-dasharray: 4 3; }
    .tag { font-size: 8px; font-weight: 700; fill: #38BDF8; }
  </style>

  <rect x="2" y="2" width="876" height="196" rx="10" fill="url(#iotBg)" stroke="#334155" stroke-width="1.2" />

  <!-- Section Title -->
  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #F97316; letter-spacing: 1px;">END-TO-END CYBER-PHYSICAL IOT AND CLOUD TOPOLOGY</text>
  </g>

  <!-- Step 1: Sensors -->
  <g transform="translate(20, 48)">
    <rect x="0" y="0" width="150" height="130" rx="8" fill="#0B1120" stroke="#F59E0B" stroke-width="1" />
    <circle cx="20" cy="22" r="6" fill="#F59E0B" />
    <text x="34" y="26" class="mono node-title">01. SENSORS</text>
    <text x="14" y="52" class="mono node-desc">• Soil N-P-K Sensors</text>
    <text x="14" y="68" class="mono node-desc">• DHT22 Temp / Hum</text>
    <text x="14" y="84" class="mono node-desc">• Optical CV Feed</text>
    <text x="14" y="112" class="mono tag">UART / SPI / I2C</text>
  </g>

  <!-- Flow 1 -->
  <line x1="172" y1="113" x2="194" y2="113" class="flow-arrow" />
  <polygon points="196,113 190,110 190,116" fill="#F97316" />

  <!-- Step 2: Patented Node -->
  <g transform="translate(196, 48)">
    <rect x="0" y="0" width="150" height="130" rx="8" fill="#0B1120" stroke="#F97316" stroke-width="1.2" />
    <circle cx="20" cy="22" r="6" fill="#F97316" />
    <text x="34" y="26" class="mono node-title">02. PATENTED M2M</text>
    <text x="14" y="52" class="mono node-desc">• Design: 470097-001</text>
    <text x="14" y="68" class="mono node-desc">• Embedded C Kernel</text>
    <text x="14" y="84" class="mono node-desc">• Power Duty-Cycle</text>
    <text x="14" y="112" class="mono tag">0% Packet Loss</text>
  </g>

  <!-- Flow 2 -->
  <line x1="348" y1="113" x2="370" y2="113" class="flow-arrow" />
  <polygon points="372,113 366,110 366,116" fill="#F97316" />

  <!-- Step 3: Gateway -->
  <g transform="translate(372, 48)">
    <rect x="0" y="0" width="150" height="130" rx="8" fill="#0B1120" stroke="#38BDF8" stroke-width="1" />
    <circle cx="20" cy="22" r="6" fill="#38BDF8" />
    <text x="34" y="26" class="mono node-title">03. INGESTION</text>
    <text x="14" y="52" class="mono node-desc">• FastAPI Async Core</text>
    <text x="14" y="68" class="mono node-desc">• WebSockets Stream</text>
    <text x="14" y="84" class="mono node-desc">• Token Auth &amp; TLS</text>
    <text x="14" y="112" class="mono tag">Sub-15ms Latency</text>
  </g>

  <!-- Flow 3 -->
  <line x1="524" y1="113" x2="546" y2="113" class="flow-arrow" />
  <polygon points="548,113 542,110 542,116" fill="#F97316" />

  <!-- Step 4: Storage -->
  <g transform="translate(548, 48)">
    <rect x="0" y="0" width="150" height="130" rx="8" fill="#0B1120" stroke="#10B981" stroke-width="1" />
    <circle cx="20" cy="22" r="6" fill="#10B981" />
    <text x="34" y="26" class="mono node-title">04. PERSISTENCE</text>
    <text x="14" y="52" class="mono node-desc">• PostgreSQL Relational</text>
    <text x="14" y="68" class="mono node-desc">• Timescale Metric Log</text>
    <text x="14" y="84" class="mono node-desc">• Redis Cache Layer</text>
    <text x="14" y="112" class="mono tag">ACID Transactions</text>
  </g>

  <!-- Flow 4 -->
  <line x1="700" y1="113" x2="722" y2="113" class="flow-arrow" />
  <polygon points="724,113 718,110 718,116" fill="#F97316" />

  <!-- Step 5: Dashboard -->
  <g transform="translate(724, 48)">
    <rect x="0" y="0" width="136" height="130" rx="8" fill="#0B1120" stroke="#A855F7" stroke-width="1" />
    <circle cx="20" cy="22" r="6" fill="#A855F7" />
    <text x="34" y="26" class="mono node-title">05. DASHBOARD</text>
    <text x="14" y="52" class="mono node-desc">• React 3D WebGL</text>
    <text x="14" y="68" class="mono node-desc">• Streamlit Graphs</text>
    <text x="14" y="84" class="mono node-desc">• Live Alert Triage</text>
    <text x="14" y="112" class="mono tag">Interactive UI</text>
  </g>
</svg>'''

def make_algorithmic_mastery():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 180" width="100%" height="180">
  <defs>
    <linearGradient id="algoBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .algo-title { font-size: 12px; font-weight: 700; fill: #F8FAFC; }
    .algo-sub { font-size: 9px; fill: #94A3B8; }
    .algo-tag { font-size: 8px; font-weight: 700; fill: #38BDF8; }
  </style>

  <rect x="2" y="2" width="876" height="176" rx="10" fill="url(#algoBg)" stroke="#334155" stroke-width="1.2" />

  <!-- Section Header -->
  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #38BDF8; letter-spacing: 1px;">CORE ALGORITHMIC EXPERTISE AND COMPLEXITY PROFILES</text>
  </g>

  <!-- 4 Pillars -->
  <!-- Card 1 -->
  <g transform="translate(20, 42)">
    <rect x="0" y="0" width="200" height="118" rx="6" fill="#0B1120" stroke="#F97316" stroke-width="1" />
    <text x="14" y="24" class="mono algo-title">Graph Theory and Trees</text>
    <text x="14" y="44" class="mono algo-sub">• Dijkstra &amp; A* Shortest Path</text>
    <text x="14" y="60" class="mono algo-sub">• Topological Sorting (DAG)</text>
    <text x="14" y="76" class="mono algo-sub">• AVL and Segment Trees</text>
    <text x="14" y="100" class="mono algo-tag">O(V + E) Optimization</text>
  </g>

  <!-- Card 2 -->
  <g transform="translate(232, 42)">
    <rect x="0" y="0" width="200" height="118" rx="6" fill="#0B1120" stroke="#38BDF8" stroke-width="1" />
    <text x="14" y="24" class="mono algo-title">Dynamic Programming</text>
    <text x="14" y="44" class="mono algo-sub">• Tabulation and Memoization</text>
    <text x="14" y="60" class="mono algo-sub">• Knapsack and LCS Vectors</text>
    <text x="14" y="76" class="mono algo-sub">• Bitmask DP on Subsets</text>
    <text x="14" y="100" class="mono algo-tag">State Space Pruning</text>
  </g>

  <!-- Card 3 -->
  <g transform="translate(444, 42)">
    <rect x="0" y="0" width="200" height="118" rx="6" fill="#0B1120" stroke="#10B981" stroke-width="1" />
    <text x="14" y="24" class="mono algo-title">Spatial and Vector Search</text>
    <text x="14" y="44" class="mono algo-sub">• K-D Tree Dimensional Index</text>
    <text x="14" y="60" class="mono algo-sub">• Cosine Similarity Matrix</text>
    <text x="14" y="76" class="mono algo-sub">• PCA Dimensional Reduction</text>
    <text x="14" y="100" class="mono algo-tag">Sub-Linear Latency</text>
  </g>

  <!-- Card 4 -->
  <g transform="translate(656, 42)">
    <rect x="0" y="0" width="204" height="118" rx="6" fill="#0B1120" stroke="#A855F7" stroke-width="1" />
    <text x="14" y="24" class="mono algo-title">System Concurrency</text>
    <text x="14" y="44" class="mono algo-sub">• Thread Pool Coroutines</text>
    <text x="14" y="60" class="mono algo-sub">• Deadlock-Free Mutex Gates</text>
    <text x="14" y="76" class="mono algo-sub">• Non-Blocking Message Queues</text>
    <text x="14" y="100" class="mono algo-tag">Async High-Throughput</text>
  </g>
</svg>'''

def make_cicd_lifecycle():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 160" width="100%" height="160">
  <defs>
    <linearGradient id="cicdBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', monospace; }
    .phase-num { font-size: 9px; font-weight: 800; fill: #F97316; }
    .phase-name { font-size: 11px; font-weight: 700; fill: #F8FAFC; }
    .phase-sub { font-size: 8.5px; fill: #94A3B8; }
    .arrow { stroke: #38BDF8; stroke-width: 1.5; stroke-dasharray: 3 3; }
  </style>

  <rect x="2" y="2" width="876" height="156" rx="10" fill="url(#cicdBg)" stroke="#334155" stroke-width="1.2" />

  <g transform="translate(20, 24)">
    <text x="0" y="0" class="mono" style="font-size: 12px; font-weight: 800; fill: #10B981; letter-spacing: 1px;">AUTOMATED CI/CD AND DEPLOYMENT LIFECYCLE</text>
  </g>

  <!-- 5 Pipeline Stages -->
  <!-- Stage 1 -->
  <g transform="translate(20, 42)">
    <rect x="0" y="0" width="150" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="12" y="20" class="mono phase-num">PHASE 01</text>
    <text x="12" y="38" class="mono phase-name">Lint and Typing</text>
    <text x="12" y="58" class="mono phase-sub">• Flake8 / Black</text>
    <text x="12" y="74" class="mono phase-sub">• TypeScript Strict</text>
  </g>

  <line x1="172" y1="91" x2="194" y2="91" class="arrow" />

  <!-- Stage 2 -->
  <g transform="translate(196, 42)">
    <rect x="0" y="0" width="150" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="12" y="20" class="mono phase-num">PHASE 02</text>
    <text x="12" y="38" class="mono phase-name">Unit and Integr.</text>
    <text x="12" y="58" class="mono phase-sub">• PyTest Suites</text>
    <text x="12" y="74" class="mono phase-sub">• Model Validation</text>
  </g>

  <line x1="348" y1="91" x2="370" y2="91" class="arrow" />

  <!-- Stage 3 -->
  <g transform="translate(372, 42)">
    <rect x="0" y="0" width="150" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="12" y="20" class="mono phase-num">PHASE 03</text>
    <text x="12" y="38" class="mono phase-name">Container Build</text>
    <text x="12" y="58" class="mono phase-sub">• Multi-Stage Docker</text>
    <text x="12" y="74" class="mono phase-sub">• Layer Caching</text>
  </g>

  <line x1="524" y1="91" x2="546" y2="91" class="arrow" />

  <!-- Stage 4 -->
  <g transform="translate(548, 42)">
    <rect x="0" y="0" width="150" height="98" rx="6" fill="#0B1120" stroke="#334155" stroke-width="1" />
    <text x="12" y="20" class="mono phase-num">PHASE 04</text>
    <text x="12" y="38" class="mono phase-name">Cloud Deploy</text>
    <text x="12" y="58" class="mono phase-sub">• AWS ECS / Lambda</text>
    <text x="12" y="74" class="mono phase-sub">• Zero-Downtime</text>
  </g>

  <line x1="700" y1="91" x2="722" y2="91" class="arrow" />

  <!-- Stage 5 -->
  <g transform="translate(724, 42)">
    <rect x="0" y="0" width="136" height="98" rx="6" fill="#0B1120" stroke="#10B981" stroke-width="1.2" />
    <text x="12" y="20" class="mono phase-num" style="fill: #10B981;">PHASE 05</text>
    <text x="12" y="38" class="mono phase-name">Telemetry Guard</text>
    <text x="12" y="58" class="mono phase-sub">• Health Watchdog</text>
    <text x="12" y="74" class="mono phase-sub">• Auto-Rollback</text>
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
    with open(os.path.join("profile", "iot-cloud-end-to-end-architecture.svg"), "w", encoding="utf-8") as f:
        f.write(make_iot_cloud_architecture())

    with open(os.path.join("profile", "algorithmic-mastery.svg"), "w", encoding="utf-8") as f:
        f.write(make_algorithmic_mastery())

    with open(os.path.join("profile", "cicd-lifecycle.svg"), "w", encoding="utf-8") as f:
        f.write(make_cicd_lifecycle())

    print("All SVGs updated and generated.")

if __name__ == "__main__":
    main()
