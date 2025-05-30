import curses
import os

def load_file(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return "N/A"

def dashboard(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.border(0)

    scan = load_file("../reports/scan_report.txt")
    deploy = load_file("../reports/deploy_log.txt")

    stdscr.addstr(1, 2, "🔐 SecureCodeDock Dashboard", curses.A_BOLD)
    stdscr.addstr(3, 2, "Scan Report Summary:")
    stdscr.addstr(4, 4, scan[:200] + "..." if len(scan) > 200 else scan)
    stdscr.addstr(7, 2, "Last Deploy Log (truncated):")
    stdscr.addstr(8, 4, deploy[-200:] if len(deploy) > 200 else deploy)
    stdscr.addstr(12, 2, "Press any key to exit...")

    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(dashboard)

