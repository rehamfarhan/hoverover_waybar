#!/usr/bin/env python3
import datetime
import json
import sys

def get_sleep_info():
    now = datetime.datetime.now()
    today = now.date()
    
    wakeup_time = datetime.time(7, 0)
    bedtime_start = datetime.time(22, 0)
    
    if now.time() < wakeup_time:
        wakeup_dt = datetime.datetime.combine(today, wakeup_time)
    else:
        wakeup_dt = datetime.datetime.combine(today + datetime.timedelta(days=1), wakeup_time)
    
    remaining = wakeup_dt - now
    remaining_seconds = max(0, int(remaining.total_seconds()))
    hours, remainder = divmod(remaining_seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    is_night = now.time() >= bedtime_start or now.time() < wakeup_time

    if is_night:
        if hours < 5:
            icon = "󰅶"
            status = "Critical Sleep Debt"
        elif hours < 7:
            icon = "󰒲"
            status = "Low Sleep Window"
        else:
            icon = "󰤄"
            status = "Bedtime Recommended"

        time_str = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"
        text = f"{icon} {time_str}"
        tooltip = (
            f"Sleep Schedule Monitor\n"
            f"Target Wake Time: 7:00 AM\n"
            f"Available Sleep: {time_str}\n"
            f"Status: {status}\n\n"
            f"Controls:\n"
            f"  LMB: Sleep Advice Toast\n"
            f"  MMB: Toggle Do Not Disturb"
        )

        return json.dumps({
            "text": text,
            "tooltip": tooltip,
            "class": "sleep"
        })
    
    return json.dumps({"text": "", "class": "hidden"})

if __name__ == "__main__":
    print(get_sleep_info())
