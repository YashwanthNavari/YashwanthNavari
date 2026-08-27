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

    print("All SVGs updated and generated.")

if __name__ == "__main__":
    main()
