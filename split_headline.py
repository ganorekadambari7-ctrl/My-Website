import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

# CSS Replacement
old_css = """        /* ── Headline typewriter ───────────────────── */
        .headline {
            font-family: "DM Serif Display", serif;
            font-size: clamp(2.0rem, 5vw, 4.2rem);
            color: var(--stone);
            line-height: 1.05;
            overflow: hidden;
            white-space: nowrap;
            border-right: 3px solid var(--teal);
            width: 0;
            animation: typewriter 1.6s steps(16) .3s forwards,
                       cursorBlink .75s step-end .3s 4;
        }

        @keyframes typewriter {
            from { width: 0; }
            to   { width: 16ch; }
        }
        @keyframes cursorBlink {
            50% { border-color: transparent; }
        }"""

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
            to   { width: 9.2ch; }
        }
        @keyframes typewriter2 {
            from { width: 0; }
            to   { width: 6.2ch; }
        }
        @keyframes hideCursor {
            to { border-right-color: transparent; }
        }
        @keyframes showCursor {
            to { border-right-color: var(--teal); }
        }
        @keyframes cursorBlink {
            50% { border-right-color: transparent; }
        }"""

if old_css not in text:
    print("WARNING: Old CSS not found exactly. Using string replacements on parts.")
    # Fallback to replace parts if Exact match fails
    pass
else:
    text = text.replace(old_css, new_css)
    print("Successfully replaced CSS.")

old_html = """                <h1 class="headline">Kadambari Ganore</h1>"""
new_html = """                <h1 class="headline-part1">Kadambari</h1>
                <h1 class="headline-part2">Ganore</h1>"""

if old_html in text:
    text = text.replace(old_html, new_html)
    print("Successfully replaced HTML.")
else:
    print("WARNING: Old HTML not found.")

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(text)
