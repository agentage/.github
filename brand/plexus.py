#!/usr/bin/env python3
"""Branded plexus/network banner generator (dark-galaxy: near-black + amber).
Recreates the blue constellation banner in agentage brand colors.
Reproducible via fixed seed. Output = SVG on stdout."""
import random, math, sys

W, H = 1774, 444            # recommended banner size; rescalable
SEED = 7
random.seed(SEED)
LEFT_INSET = W * 0.06       # keep the far-left from over-crowding (the ~5-10% crop)

AMBER = "#f5a623"          # brand primary (nodes/lines, left = bright)
BLUE  = "#5b9bef"          # dark-galaxy workhorse accent (a few cool nodes)
BG_A, BG_B = "#0b1220", "#05070d"

N = 46                     # node count
LINK_DIST = 250            # connect nodes closer than this (scaled to canvas)

# Density weighted to the left (like the reference) but eased so the far-left
# no longer over-crowds; nodes start at LEFT_INSET (the ~5-10% the user cropped).
nodes = []
for _ in range(N):
    x = LEFT_INSET + (random.random() ** 1.4) * (W - LEFT_INSET)
    y = random.random() * H
    r = random.uniform(2.0, 4.2)
    nodes.append((x, y, r))

def brightness(x):
    # 1.0 at left edge -> ~0.12 at right edge (matches fade)
    t = max(0.0, min(1.0, x / W))
    return 0.12 + (1.0 - t) ** 1.6 * 0.9

svg = []
svg.append(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
svg.append('<defs>')
svg.append(f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
           f'<stop offset="0" stop-color="{BG_A}"/><stop offset="1" stop-color="{BG_B}"/></linearGradient>')
svg.append('<radialGradient id="glow" cx="8%" cy="30%" r="60%">'
           f'<stop offset="0" stop-color="{AMBER}" stop-opacity="0.16"/>'
           f'<stop offset="55%" stop-color="{AMBER}" stop-opacity="0.03"/>'
           '<stop offset="100%" stop-color="#000" stop-opacity="0"/></radialGradient>')
svg.append('<filter id="soft"><feGaussianBlur stdDeviation="2.2"/></filter>')
svg.append('</defs>')
svg.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
svg.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')

# edges
for i in range(N):
    for j in range(i + 1, N):
        x1, y1, _ = nodes[i]
        x2, y2, _ = nodes[j]
        d = math.hypot(x1 - x2, y1 - y2)
        if d < LINK_DIST:
            b = brightness((x1 + x2) / 2) * (1 - d / LINK_DIST)
            op = round(b * 0.55, 3)
            if op < 0.015:
                continue
            svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                       f'stroke="{AMBER}" stroke-width="0.9" stroke-opacity="{op}"/>')

# nodes
for idx, (x, y, r) in enumerate(nodes):
    b = brightness(x)
    col = BLUE if idx % 9 == 0 else AMBER   # sprinkle a few cool nodes for depth
    op = round(min(1.0, b * 1.05), 3)
    if b > 0.62:  # bright hubs get a bloom
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r*2.6:.1f}" fill="{col}" '
                   f'fill-opacity="{round(op*0.28,3)}" filter="url(#soft)"/>')
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}" fill-opacity="{op}"/>')

svg.append('</svg>')
sys.stdout.write("\n".join(svg))
