def _c(code, text):
    return f"\x1b[{code}m{text}\x1b[0m"


TERRAIN = {"#": "90", ".": "32", ":": "33", "~": "34"}


def render_grid(g, visited=(), path=()):
    left, lines = g.remaining(), []
    for r, row in enumerate(g.grid):
        out = []
        for c, ch in enumerate(row):
            u = (r, c)
            if u == g.player:
                out.append(_c("1;97", "@"))
            elif u in left:
                out.append(_c("1;93", "$"))
            elif u == g.exit:
                out.append(_c("1;92", "E") if g.exit_open else _c("1;91", "X"))
            elif u in path:
                out.append(_c("1;91", "*"))
            elif u in visited:
                out.append(_c("36", "o"))
            else:
                out.append(_c(TERRAIN[ch], ch))
        lines.append(" ".join(out))
    return "\n".join(lines)
