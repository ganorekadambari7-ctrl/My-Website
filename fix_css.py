import re

with open('index.html', 'rb') as f:
    text = f.read().decode('utf-8')

new_css = """        /* ── Headline typewriter ───────────────────── */
        .headline-part1, .headline-part2 {
            font-family: "DM Serif Display", serif;
            font-size: clamp(2.8rem, 7vw, 4.2rem);
            color: var(--stone);
            line-height: 1.1;
            overflow: hidden;
            white-space: nowrap;
            width: 0;
            margin: 0;
        }
        .headline-part1 {
            border-right: 3px solid var(--teal);
            animation: typewriter1 .9s steps(9) .3s forwards,
                       hideCursor 0s 1.2s forwards;
        }
        .headline-part2 {
            border-right: 3px solid transparent;
            animation: showCursor 0s 1.2s forwards,
                       typewriter2 .6s steps(6) 1.2s forwards,
                       cursorBlink .75s step-end 1.2s infinite;
        }

        @keyframes typewriter1 {
            from { width: 0; }
            to   { width: 9.3ch; }
        }
        @keyframes typewriter2 {
            from { width: 0; }
            to   { width: 6.3ch; }
        }
        @keyframes hideCursor {
            to { border-right-color: transparent; }
        }
        @keyframes showCursor {
            to { border-right-color: var(--teal); }
        }
        @keyframes cursorBlink {
            50% { border-right-color: transparent; }
        }
"""

# The regex will match perfectly because .*? with DOTALL captures everything across lines.
text = re.sub(r'        /\* ── Headline typewriter ───────────────────── \*/.*?@keyframes cursorBlink \{.*?\}', new_css, text, flags=re.DOTALL)

with open('index.html', 'wb') as f:
    f.write(text.encode('utf-8'))
