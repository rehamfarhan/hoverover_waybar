#!/usr/bin/env python3
import os
import sys
import time
import json
import datetime
import subprocess
from pathlib import Path

TIMER_CACHE = Path.home() / ".cache" / "waybar_uptime_timer_start.txt"

def toggle_timer():
    now = time.time()
    if not TIMER_CACHE.exists():
        TIMER_CACHE.write_text(str(now))
        now_dt = datetime.datetime.now().strftime("%I:%M:%S %p")
        subprocess.run([
            "notify-send",
            "-a", "OSD",
            "-i", "chronometer",
            "-h", "string:x-canonical-private-synchronous:uptime-timer",
            "-t", "3500",
            "⏱ Timer Started",
            f"Precision timer started at {now_dt}\nClick Uptime module again to stop."
        ])
    else:
        try:
            start_time = float(TIMER_CACHE.read_text().strip())
            elapsed = now - start_time
            TIMER_CACHE.unlink(missing_ok=True)
            
            hours, rem = divmod(elapsed, 3600)
            minutes, seconds = divmod(rem, 60)
            
            if hours > 0:
                elapsed_str = f"{int(hours)}h {int(minutes)}m {seconds:.3f}s"
            elif minutes > 0:
                elapsed_str = f"{int(minutes)}m {seconds:.3f}s"
            else:
                elapsed_str = f"{seconds:.3f}s"

            subprocess.run([
                "notify-send",
                "-a", "OSD",
                "-i", "chronometer",
                "-h", "string:x-canonical-private-synchronous:uptime-timer",
                "-t", "5000",
                f"⏱ Elapsed: {elapsed_str}",
                f"Duration: {elapsed_str}"
            ])
        except Exception:
            TIMER_CACHE.unlink(missing_ok=True)
            subprocess.run([
                "notify-send",
                "-a", "OSD",
                "-i", "chronometer",
                "-h", "string:x-canonical-private-synchronous:uptime-timer",
                "-t", "3500",
                "⏱ Timer Reset",
                "Timer reset."
            ])

def get_uptime_info():
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        
        days, rem = divmod(int(uptime_seconds), 86400)
        hours, rem = divmod(rem, 3600)
        minutes, _ = divmod(rem, 60)
        
        boot_time = datetime.datetime.now() - datetime.timedelta(seconds=uptime_seconds)
        boot_str = boot_time.strftime("%I:%M %p, %b %d")

        if days > 0:
            uptime_text = f"{days}d {hours}h {minutes}m"
        elif hours > 0:
            uptime_text = f"{hours}h {minutes}m"
        else:
            uptime_text = f"{minutes}m"

        tty_num = os.environ.get("XDG_VTNR", "")
        if tty_num:
            tty_str = f"tty{tty_num}"
        else:
            try:
                res = subprocess.check_output(["tty"], text=True, stderr=subprocess.DEVNULL).strip()
                tty_str = os.path.basename(res) if "tty" in res else "Wayland/Hyprland"
            except Exception:
                tty_str = "tty1 (Hyprland)"

        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            tod_icon = "󰖙"
            tod_name = "Morning"
        elif 12 <= hour < 17:
            tod_icon = "󰖨"
            tod_name = "Afternoon"
        elif 17 <= hour < 21:
            tod_icon = "󰖔"
            tod_name = "Evening"
        else:
            tod_icon = "󰽥"
            tod_name = "Night"

        timer_status = "Running (Click to Stop)" if TIMER_CACHE.exists() else "Idle (Click to Start)"

        tooltip = (
            f"Session Uptime: {uptime_text}\n"
            f"Booted: {boot_str}\n"
            f"Session TTY: {tty_str}\n"
            f"Time of Day: {tod_name}\n\n"
            f"Stopwatch: {timer_status}\n"
            f"LMB: Start / Stop Precision Timer"
        )

        return json.dumps({
            "text": f"{tod_icon} {uptime_text}",
            "tooltip": tooltip,
            "class": "uptime"
        })

    except Exception as e:
        return json.dumps({
            "text": "󰖨 Uptime",
            "tooltip": f"Error: {str(e)}",
            "class": "uptime"
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--toggle-timer":
        toggle_timer()
    else:
        print(get_uptime_info())
