"""
Engineering Command Center Telemetry Generator
Generates self-hosted, high-DPI vector SVG cards for the GitHub profile.
"""
import os
import json
import urllib.request
import urllib.error

def fetch_github_data(username="YashwanthNavari"):
    headers = {"User-Agent": "CommandCenter-Telemetry-Generator"}
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"
    
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    
    user_data = {"public_repos": 18, "followers": 10}
    total_stars = 16
    
    try:
        req = urllib.request.Request(user_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            user_data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Notice: Using cached user metrics ({e})")
        
    try:
        req = urllib.request.Request(repos_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            repos_data = json.loads(response.read().decode())
            if isinstance(repos_data, list):
                total_stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)
    except Exception as e:
        print(f"Notice: Using cached star metrics ({e})")
        
    return {
        "repos": user_data.get("public_repos", 18),
        "stars": max(total_stars, 16),
        "commits": "480+",
        "rank": "A+"
    }

def generate_command_status_bar(out_dir="profile"):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 76" width="100%" height="76">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F97316" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#F97316" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono-font { font-family: 'Fira Code', 'JetBrains Mono', 'Courier New', monospace; }
    .label { font-size: 10.5px; fill: #94A3B8; text-transform: uppercase; letter-spacing: 1.2px; }
    .val { font-size: 12px; font-weight: 700; fill: #F8FAFC; letter-spacing: 0.5px; }
    .val-orange { fill: #FB923C; }
    .val-cyan { fill: #38BDF8; }
    .val-green { fill: #34D399; }
    .pulse-dot {
      animation: pulse 2s infinite ease-in-out;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }
    .grid-line { stroke: #1E293B; stroke-width: 1; stroke-dasharray: 3 3; }
  </style>

  <!-- Container Box -->
  <rect x="2" y="2" width="876" height="72" rx="10" fill="url(#bgGrad)" stroke="url(#borderGrad)" stroke-width="1.5" />

  <!-- Corner Accents -->
  <path d="M 2 14 L 14 2 M 878 14 L 866 2 M 2 62 L 14 74 M 878 62 L 866 74" stroke="#F97316" stroke-width="1.5" fill="none" opacity="0.6" />

  <!-- Partition Grids -->
  <line x1="220" y1="12" x2="220" y2="64" class="grid-line" />
  <line x1="440" y1="12" x2="440" y2="64" class="grid-line" />
  <line x1="660" y1="12" x2="660" y2="64" class="grid-line" />

  <!-- SECTION 1: SYSTEM CORE -->
  <g transform="translate(18, 0)">
    <circle cx="10" cy="38" r="5" fill="#10B981" class="pulse-dot" filter="url(#glow)" />
    <circle cx="10" cy="38" r="2.5" fill="#FFFFFF" />
    <text x="24" y="32" class="mono-font label">COMMAND SYSTEM</text>
    <text x="24" y="50" class="mono-font val val-green">STATUS: OPERATIONAL</text>
  </g>

  <!-- SECTION 2: PATENT & HARDWARE -->
  <g transform="translate(236, 0)">
    <circle cx="10" cy="38" r="4.5" fill="#F97316" filter="url(#glow)" />
    <text x="22" y="32" class="mono-font label">M2M HARDWARE NODE</text>
    <text x="22" y="50" class="mono-font val val-orange">PATENT NO: 470097-001</text>
  </g>

  <!-- SECTION 3: INFERENCE & TELEMETRY -->
  <g transform="translate(456, 0)">
    <circle cx="10" cy="38" r="4.5" fill="#38BDF8" filter="url(#glow)" />
    <text x="22" y="32" class="mono-font label">AI INFERENCE LATENCY</text>
    <text x="22" y="50" class="mono-font val val-cyan">&lt; 12ms / DETERMINISTIC</text>
  </g>

  <!-- SECTION 4: CLOUD & EDGE NODES -->
  <g transform="translate(676, 0)">
    <circle cx="10" cy="38" r="4.5" fill="#A855F7" filter="url(#glow)" />
    <text x="22" y="32" class="mono-font label">DISTRIBUTED NODES</text>
    <text x="22" y="50" class="mono-font val">6 ACTIVE CLUSTERS</text>
  </g>
</svg>'''
    with open(os.path.join(out_dir, "command-status-bar.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_stats_card(metrics, out_dir="profile"):
    stars = metrics["stars"]
    commits = metrics["commits"]
    repos = metrics["repos"]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 220" width="100%" height="220">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="60%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="orangeGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F97316" />
      <stop offset="100%" stop-color="#EA580C" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <style>
    .mono {{ font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace; }}
    .title {{ font-size: 15px; font-weight: 700; fill: #F97316; letter-spacing: 0.8px; }}
    .stat-label {{ font-size: 12.5px; fill: #94A3B8; }}
    .stat-val {{ font-size: 13.5px; font-weight: 700; fill: #F1F5F9; }}
    .icon {{ fill: #F97316; }}
    .rank-circle {{ stroke: #F97316; stroke-width: 3.5; stroke-dasharray: 220; stroke-dashoffset: 40; }}
    .rank-text {{ font-size: 26px; font-weight: 800; fill: #38BDF8; text-anchor: middle; dominant-baseline: central; }}
    .rank-sub {{ font-size: 9.5px; fill: #94A3B8; text-anchor: middle; }}
    .border-glow {{ stroke: #334155; stroke-width: 1.2; }}
  </style>

  <!-- Background -->
  <rect x="2" y="2" width="416" height="216" rx="12" fill="url(#cardBg)" class="border-glow" filter="url(#shadow)" />
  <line x1="16" y1="42" x2="404" y2="42" stroke="#1E293B" stroke-width="1" />

  <!-- Header Title -->
  <g transform="translate(18, 28)">
    <svg class="icon" width="18" height="18" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
    </svg>
    <text x="26" y="14" class="mono title">ENGINEERING TELEMETRY STATS</text>
  </g>

  <!-- Left Stats Block -->
  <g transform="translate(20, 64)">
    <!-- Total Commits -->
    <g transform="translate(0, 10)">
      <circle cx="6" cy="6" r="3" fill="#F97316" />
      <text x="18" y="10" class="mono stat-label">Production Commits:</text>
      <text x="240" y="10" class="mono stat-val" text-anchor="end">{commits}</text>
    </g>

    <!-- Star Count -->
    <g transform="translate(0, 38)">
      <circle cx="6" cy="6" r="3" fill="#38BDF8" />
      <text x="18" y="10" class="mono stat-label">Total Repository Stars:</text>
      <text x="240" y="10" class="mono stat-val" text-anchor="end">{stars} ★</text>
    </g>

    <!-- Pull Requests & Issues -->
    <g transform="translate(0, 66)">
      <circle cx="6" cy="6" r="3" fill="#10B981" />
      <text x="18" y="10" class="mono stat-label">PRs &amp; Issue Resolutions:</text>
      <text x="240" y="10" class="mono stat-val" text-anchor="end">32</text>
    </g>

    <!-- Repositories & Inventions -->
    <g transform="translate(0, 94)">
      <circle cx="6" cy="6" r="3" fill="#A855F7" />
      <text x="18" y="10" class="mono stat-label">Contributed Repos / Patents:</text>
      <text x="240" y="10" class="mono stat-val" text-anchor="end">{repos} / 1 Granted</text>
    </g>

    <!-- System Uptime -->
    <g transform="translate(0, 122)">
      <circle cx="6" cy="6" r="3" fill="#EAB308" />
      <text x="18" y="10" class="mono stat-label">Architecture Reliability:</text>
      <text x="240" y="10" class="mono stat-val" text-anchor="end">99.9%</text>
    </g>
  </g>

  <!-- Right Rank Gauge -->
  <g transform="translate(330, 126)">
    <circle cx="0" cy="0" r="42" fill="#0B1120" stroke="#1E293B" stroke-width="4" />
    <circle cx="0" cy="0" r="42" fill="none" class="rank-circle" stroke="url(#orangeGlow)" transform="rotate(-90)" />
    <text x="0" y="-4" class="mono rank-text">A+</text>
    <text x="0" y="18" class="mono rank-sub">SYSTEM RANK</text>
  </g>
</svg>'''
    with open(os.path.join(out_dir, "stats-card.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_top_langs(out_dir="profile"):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 220" width="100%" height="220">
  <defs>
    <linearGradient id="langsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="60%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace; }
    .title { font-size: 15px; font-weight: 700; fill: #F97316; letter-spacing: 0.8px; }
    .lang-name { font-size: 12.5px; fill: #E2E8F0; }
    .lang-pct { font-size: 12px; font-weight: 700; fill: #94A3B8; }
    .bar-bg { fill: #1E293B; rx: 4px; }
    .bar-fill { rx: 4px; transition: width 0.5s ease-in-out; }
    .border-glow { stroke: #334155; stroke-width: 1.2; }
  </style>

  <!-- Background -->
  <rect x="2" y="2" width="416" height="216" rx="12" fill="url(#langsBg)" class="border-glow" filter="url(#cardShadow)" />
  <line x1="16" y1="42" x2="404" y2="42" stroke="#1E293B" stroke-width="1" />

  <!-- Header Title -->
  <g transform="translate(18, 28)">
    <svg fill="#F97316" width="18" height="18" viewBox="0 0 24 24">
      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
    </svg>
    <text x="26" y="14" class="mono title">TOP COMPUTATIONAL STACK</text>
  </g>

  <!-- Language Progress Bars -->
  <g transform="translate(20, 56)">
    <!-- Python -->
    <g transform="translate(0, 8)">
      <circle cx="6" cy="6" r="4" fill="#3572A5" />
      <text x="16" y="10" class="mono lang-name">Python (AI / ML / Data)</text>
      <text x="380" y="10" class="mono lang-pct" text-anchor="end">46.5%</text>
      <rect x="0" y="16" width="380" height="7" class="bar-bg" />
      <rect x="0" y="16" width="176.7" height="7" class="bar-fill" fill="#3572A5" />
    </g>

    <!-- JavaScript & TypeScript / React -->
    <g transform="translate(0, 38)">
      <circle cx="6" cy="6" r="4" fill="#F7DF1E" />
      <text x="16" y="10" class="mono lang-name">JavaScript / TypeScript (React / APIs)</text>
      <text x="380" y="10" class="mono lang-pct" text-anchor="end">24.2%</text>
      <rect x="0" y="16" width="380" height="7" class="bar-bg" />
      <rect x="0" y="16" width="92" height="7" class="bar-fill" fill="#F7DF1E" />
    </g>

    <!-- Java -->
    <g transform="translate(0, 68)">
      <circle cx="6" cy="6" r="4" fill="#B07219" />
      <text x="16" y="10" class="mono lang-name">Java (Algorithms &amp; Systems)</text>
      <text x="380" y="10" class="mono lang-pct" text-anchor="end">14.8%</text>
      <rect x="0" y="16" width="380" height="7" class="bar-bg" />
      <rect x="0" y="16" width="56.2" height="7" class="bar-fill" fill="#B07219" />
    </g>

    <!-- Embedded C & C++ -->
    <g transform="translate(0, 98)">
      <circle cx="6" cy="6" r="4" fill="#00599C" />
      <text x="16" y="10" class="mono lang-name">Embedded C / C++ (IoT &amp; M2M Hardware)</text>
      <text x="380" y="10" class="mono lang-pct" text-anchor="end">9.5%</text>
      <rect x="0" y="16" width="380" height="7" class="bar-bg" />
      <rect x="0" y="16" width="36.1" height="7" class="bar-fill" fill="#00599C" />
    </g>

    <!-- SQL & Shell -->
    <g transform="translate(0, 128)">
      <circle cx="6" cy="6" r="4" fill="#38BDF8" />
      <text x="16" y="10" class="mono lang-name">SQL / Shell (PostgreSQL, MySQL, Bash)</text>
      <text x="380" y="10" class="mono lang-pct" text-anchor="end">5.0%</text>
      <rect x="0" y="16" width="380" height="7" class="bar-bg" />
      <rect x="0" y="16" width="19" height="7" class="bar-fill" fill="#38BDF8" />
    </g>
  </g>
</svg>'''
    with open(os.path.join(out_dir, "top-langs.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_skill_radar(out_dir="profile"):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 260" width="100%" height="260">
  <defs>
    <linearGradient id="radarBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="60%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="polyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F97316" stop-opacity="0.65" />
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.6" />
    </linearGradient>
    <filter id="radarShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace; }
    .title { font-size: 15px; font-weight: 700; fill: #F97316; letter-spacing: 0.8px; }
    .axis-label { font-size: 10px; font-weight: 600; fill: #CBD5E1; text-anchor: middle; }
    .grid-poly { fill: none; stroke: #334155; stroke-width: 1; stroke-dasharray: 2 2; }
    .axis-line { stroke: #1E293B; stroke-width: 1.2; }
    .data-poly { fill: url(#polyGrad); stroke: #F97316; stroke-width: 2; }
    .data-node { fill: #38BDF8; stroke: #FFFFFF; stroke-width: 1.5; }
    .border-glow { stroke: #334155; stroke-width: 1.2; }
  </style>

  <!-- Background -->
  <rect x="2" y="2" width="416" height="256" rx="12" fill="url(#radarBg)" class="border-glow" filter="url(#radarShadow)" />
  <line x1="16" y1="38" x2="404" y2="38" stroke="#1E293B" stroke-width="1" />

  <!-- Header Title -->
  <g transform="translate(18, 26)">
    <svg fill="#F97316" width="18" height="18" viewBox="0 0 24 24">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
    </svg>
    <text x="26" y="14" class="mono title">ENGINEERING DOMAIN RADAR</text>
  </g>

  <!-- Radar Diagram -->
  <g transform="translate(210, 148)">
    <polygon points="0,-18.75 16.2,-9.38 16.2,9.38 0,18.75 -16.2,9.38 -16.2,-9.38" class="grid-poly" />
    <polygon points="0,-37.5 32.5,-18.75 32.5,18.75 0,37.5 -32.5,18.75 -32.5,-18.75" class="grid-poly" />
    <polygon points="0,-56.25 48.7,-28.1 48.7,28.1 0,56.25 -48.7,28.1 -48.7,-28.1" class="grid-poly" />
    <polygon points="0,-75 64.95,-37.5 64.95,37.5 0,75 -64.95,37.5 -64.95,-37.5" class="grid-poly" stroke="#475569" stroke-dasharray="none" />

    <line x1="0" y1="0" x2="0" y2="-75" class="axis-line" />
    <line x1="0" y1="0" x2="64.95" y2="-37.5" class="axis-line" />
    <line x1="0" y1="0" x2="64.95" y2="37.5" class="axis-line" />
    <line x1="0" y1="0" x2="0" y2="75" class="axis-line" />
    <line x1="0" y1="0" x2="-64.95" y2="37.5" class="axis-line" />
    <line x1="0" y1="0" x2="-64.95" y2="-37.5" class="axis-line" />

    <polygon points="0,-71.25 63.65,-36.75 58.45,33.75 0,66 -59.75,34.5 -55.85,-32.25" class="data-poly" />

    <circle cx="0" cy="-71.25" r="3.5" class="data-node" />
    <circle cx="63.65" cy="-36.75" r="3.5" class="data-node" />
    <circle cx="58.45" cy="33.75" r="3.5" class="data-node" />
    <circle cx="0" cy="66" r="3.5" class="data-node" />
    <circle cx="-59.75" cy="34.5" r="3.5" class="data-node" />
    <circle cx="-55.85" cy="-32.25" r="3.5" class="data-node" />

    <text x="0" y="-84" class="mono axis-label">AI / DEEP LEARNING (95%)</text>
    <text x="75" y="-42" class="mono axis-label" style="text-anchor:start;">PATENTED IoT &amp; M2M (98%)</text>
    <text x="75" y="44" class="mono axis-label" style="text-anchor:start;">FULL-STACK SAAS (90%)</text>
    <text x="0" y="92" class="mono axis-label">DISTRIBUTED SYSTEMS (88%)</text>
    <text x="-75" y="44" class="mono axis-label" style="text-anchor:end;">DATABASE ENG (92%)</text>
    <text x="-75" y="-42" class="mono axis-label" style="text-anchor:end;">SECURITY &amp; ZT (86%)</text>
  </g>
</svg>'''
    with open(os.path.join(out_dir, "skill-radar.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_pipeline_telemetry(out_dir="profile"):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 260" width="100%" height="260">
  <defs>
    <linearGradient id="pipeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="60%" stop-color="#0B1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <filter id="pipeShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace; }
    .title { font-size: 15px; font-weight: 700; fill: #F97316; letter-spacing: 0.8px; }
    .telemetry-key { font-size: 12px; fill: #94A3B8; }
    .telemetry-val { font-size: 12px; font-weight: 700; fill: #F8FAFC; }
    .badge-green { fill: #064E3B; stroke: #10B981; stroke-width: 1; rx: 4px; }
    .badge-blue { fill: #0C4A6E; stroke: #38BDF8; stroke-width: 1; rx: 4px; }
    .badge-orange { fill: #7C2D12; stroke: #F97316; stroke-width: 1; rx: 4px; }
    .status-text-green { font-size: 10px; font-weight: 700; fill: #34D399; text-anchor: middle; }
    .status-text-blue { font-size: 10px; font-weight: 700; fill: #38BDF8; text-anchor: middle; }
    .status-text-orange { font-size: 10px; font-weight: 700; fill: #FB923C; text-anchor: middle; }
    .border-glow { stroke: #334155; stroke-width: 1.2; }
    .metric-bar-bg { fill: #1E293B; rx: 3px; }
    .metric-bar-fill { rx: 3px; }
  </style>

  <!-- Background -->
  <rect x="2" y="2" width="416" height="256" rx="12" fill="url(#pipeBg)" class="border-glow" filter="url(#pipeShadow)" />
  <line x1="16" y1="38" x2="404" y2="38" stroke="#1E293B" stroke-width="1" />

  <!-- Header Title -->
  <g transform="translate(18, 26)">
    <svg fill="#F97316" width="18" height="18" viewBox="0 0 24 24">
      <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"/>
    </svg>
    <text x="26" y="14" class="mono title">PIPELINE &amp; RUNTIME TELEMETRY</text>
  </g>

  <!-- Metrics Grid -->
  <g transform="translate(20, 52)">
    <!-- 1. M2M Telemetry Packet Fidelity -->
    <g transform="translate(0, 10)">
      <text x="0" y="10" class="mono telemetry-key">M2M Telemetry Packet Delivery</text>
      <text x="380" y="10" class="mono telemetry-val" text-anchor="end">99.98%</text>
      <rect x="0" y="16" width="380" height="5" class="metric-bar-bg" />
      <rect x="0" y="16" width="379.9" height="5" class="metric-bar-fill" fill="#10B981" />
    </g>

    <!-- 2. AI Inference Engine Availability -->
    <g transform="translate(0, 48)">
      <text x="0" y="10" class="mono telemetry-key">Model Inference Service Uptime</text>
      <text x="380" y="10" class="mono telemetry-val" text-anchor="end">100.0%</text>
      <rect x="0" y="16" width="380" height="5" class="metric-bar-bg" />
      <rect x="0" y="16" width="380" height="5" class="metric-bar-fill" fill="#38BDF8" />
    </g>

    <!-- 3. Zero-Deadlock Concurrency -->
    <g transform="translate(0, 86)">
      <text x="0" y="10" class="mono telemetry-key">Backend Thread Pool Efficiency</text>
      <text x="380" y="10" class="mono telemetry-val" text-anchor="end">0ms Latency Lock</text>
      <rect x="0" y="16" width="380" height="5" class="metric-bar-bg" />
      <rect x="0" y="16" width="365" height="5" class="metric-bar-fill" fill="#F97316" />
    </g>

    <!-- Operational Status Badges -->
    <g transform="translate(0, 128)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="118" height="26" class="badge-green" />
        <text x="59" y="16" class="mono status-text-green">● CI/CD PASSING</text>
      </g>
      <g transform="translate(130, 0)">
        <rect x="0" y="0" width="120" height="26" class="badge-blue" />
        <text x="60" y="16" class="mono status-text-blue">● WS STREAMING</text>
      </g>
      <g transform="translate(262, 0)">
        <rect x="0" y="0" width="118" height="26" class="badge-orange" />
        <text x="59" y="16" class="mono status-text-orange">★ PATENT ACTIVE</text>
      </g>
    </g>
  </g>
</svg>'''
    with open(os.path.join(out_dir, "pipeline-telemetry.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def main():
    os.makedirs("profile", exist_ok=True)
    metrics = fetch_github_data("YashwanthNavari")
    print(f"Generating telemetry for YashwanthNavari: {metrics}")
    generate_command_status_bar("profile")
    generate_stats_card(metrics, "profile")
    generate_top_langs("profile")
    generate_skill_radar("profile")
    generate_pipeline_telemetry("profile")
    print("All Command Center telemetry SVGs generated successfully.")

if __name__ == "__main__":
    main()
