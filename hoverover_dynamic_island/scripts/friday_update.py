#!/usr/bin/env python3
import os
import sys
import json
import datetime
import subprocess
from pathlib import Path

def check_friday_maintenance():
    today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")
    
    # State file to track dismissal/execution for today
    cache_dir = Path.home() / ".cache" / "waybar_friday_update"
    cache_dir.mkdir(parents=True, exist_ok=True)
    dismiss_file = cache_dir / f"dismissed_{today_str}"

    # Handle action flag when clicked
    if len(sys.argv) > 1 and sys.argv[1] == "--run":
        # Mark as dismissed for today
        dismiss_file.touch()
        
        # Trigger terminal update
        cmd = (
            "foot --app-id=system_update -T 'Friday System Maintenance' "
            "bash -c 'echo -e \"\\033[1;36m==> Running Friday System Maintenance...\\033[0m\\n\"; "
            "~/user_scripts/arch_iso_scripts/offline_iso/050_mirrorlist.sh && "
            "paru -Syu --noconfirm && "
            "python3 /home/directpass/user_scripts/update_dusky/python/update_dusky.py; "
            "echo -e \"\\n\\033[1;32m==> Maintenance Complete! Press Enter to close.\\033[0m\"; "
            "read'"
        )
        subprocess.Popen(cmd, shell=True)
        
        # Signal Waybar to refresh and hide module
        subprocess.run(["pkill", "-RTMIN+9", "waybar"], stderr=subprocess.DEVNULL)
        sys.exit(0)

    # 4 = Friday (0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday)
    is_friday = today.weekday() == 4

    # If it is Friday and hasn't been dismissed today, display the update notification
    if is_friday and not dismiss_file.exists():
        return json.dumps({
            "text": "󰮯 Update Available",
            "tooltip": (
                "Weekly System Maintenance (Friday)\n\n"
                "Click to run:\n"
                "  • 050_mirrorlist.sh (Mirrors)\n"
                "  • paru -Syu (Packages)\n"
                "  • update_dusky.py (Dusky Distro)"
            ),
            "class": "pending"
        })
    
    # Otherwise, return empty/hidden
    return json.dumps({"text": "", "class": "hidden"})

if __name__ == "__main__":
    print(check_friday_maintenance())
