"""Single-key input (Windows / Linux / macOS) and screen clearing."""
import os
import sys
import time

if os.name == "nt":
    import msvcrt
    os.system("")

    def getkey(timeout=None):
        end = None if timeout is None else time.time() + timeout
        while True:
            if msvcrt.kbhit():
                c = msvcrt.getwch()
                if c in ("\x00", "\xe0"):
                    return {"H": "up", "P": "down", "K": "left", "M": "right"}.get(msvcrt.getwch(), "")
                if c == "\x03":
                    raise KeyboardInterrupt
                return c.lower()
            if end is not None and time.time() >= end:
                return None
            time.sleep(0.01)
else:
    import select
    import termios
    import tty

    def getkey(timeout=None):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            if not select.select([fd], [], [], timeout)[0]:
                return None
            data = os.read(fd, 8).decode(errors="ignore")
            if data.startswith("\x1b["):
                return {"A": "up", "B": "down", "D": "left", "C": "right"}.get(data[2:3], "")
            return "esc" if data.startswith("\x1b") else data[:1].lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def clear():
    sys.stdout.write("\x1b[2J\x1b[H")


def show(text):
    clear()
    print(text)
    sys.stdout.flush()
