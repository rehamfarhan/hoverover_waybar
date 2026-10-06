# 🌊 Hoverover Waybar (Bottom Dock)

A fluid, bouncy, and highly interactive **Waybar** configuration designed as a bottom-dock status center for **Hyprland** on Arch Linux (Dusky Desktop Environment).

Featuring **60% Frosted Glass Transparency**, signature **Multi-Gradient Lava-Lamp Wax Hover Animations**, **Snappy Spring Arrival Transitions**, and a full suite of interactive power-user widgets.

---

## 🎮 Master Controls & Interactions Table

Every capsule is engineered for fast, intuitive access to system tools:

| Module | Icon / Display | LMB (Left Click) | RMB (Right Click) | MMB (Middle Click) | Scroll Up / Down | Hover Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Power Drawer** | `⏻` | Open **Wlogout** power menu | Lock screen (**Hyprlock**) | — | — | Expands drawer to reveal `Inhibit Suspend` |
| **Inhibit Suspend** | `󰌾` (Active) / `󰅶` (Paused) | Toggle **Hypridle** auto-suspend on/off | — | — | — | Child of Power Drawer |
| **Notifications** | `󰂚` (Count) | Open **Rofi** notification history panel | Toggle **Mako** Do Not Disturb (DND) | — | — | Liquid Lava-Lamp Glow |
| **Network Drawer** | `` (SSID) / `󰈀` (Ethernet) | Open **Dusky TUI Network Manager** in `foot` | Restart WiFi radio (off $\rightarrow$ on) + OSD toast | Turn WiFi radio **OFF** | — | Expands drawer to reveal `Bluetooth` |
| **Bluetooth** | `󰂯` / `󰂱` (Count) | Open **Blueman Manager** (GUI) | Open **Bluetui** (Terminal TUI) | Toggle Bluetooth Controller Power + OSD toast | — | Child of Network Drawer |
| **Uptime & Stopwatch** | `󰔛` / Time-of-Day Icon + Uptime | **Start / Stop Precision Stopwatch** (Displays elapsed time in 3.5s OSD toast) | — | — | — | Liquid Lava-Lamp Glow |
| **Friday Update** | `󰏓` / `󰑐` (Pulse) | Run mirrorlist ranking + `paru` upgrade + Dusky updates in terminal | — | — | — | **Auto-shows ONLY on Fridays** until updated |
| **Workspaces** | Number / Dynamic App Icon | Switch to clicked workspace | — | — | Cycle workspace (`e-1` / `e+1`) | Liquid Lava-Lamp Glow |
| **Active Window** | App Icon + Truncated Title | **Silently spawn `foot` terminal** on empty workspace & jump | **Close active window** (`window.close`) | Toggle **Special Scratchpad** (`magic`) | Cycle workspace (`e-1` / `e+1`) | Liquid Lava-Lamp Glow |
| **Sleep Monitor** | `󰒲` (Bedtime Status) | Send bedtime & circadian schedule analysis notification | — | Quick Toggle DND | — | Liquid Lava-Lamp Glow |
| **Media Player** | Brand Icon + Track Title | **Play / Pause** toggle | **Stop** playback | — | Next / Previous track (`playerctl`) | Auto-hides when idle; shows on active playback |
| **Audio Volume** | `` / Volume % | Open **Pavucontrol** volume mixer | Open **Cava** audio visualizer in terminal | **Restart Audio Server** (PipeWire + WirePlumber) | Adjust volume $\pm 5\%$ (`pactl`) | Liquid Lava-Lamp Glow |
| **System Tray** | Tray Icons | Standard Applet LMB action | Standard Applet RMB menu | — | — | Smooth Glass Capsule |
| **Clock Drawer** | `󰥔` (Time) | Open **GNOME Clocks** | Toggle calendar mode / view format | Open **Peaclock** terminal clock | Shift calendar month view up / down | Expands drawer to reveal `CPU` & `RAM` |
| **CPU Usage** | `` (Usage %) | Open **`btop`** monitor in terminal | Run **Sysbench CPU Benchmark** suite | — | Adjust Display Brightness $\pm 1\%$ | Child of Clock Drawer |
| **RAM Usage** | `` (Usage %) | Open **`btop`** monitor in terminal | Run **Dusky Disk I/O Monitor** | — | Adjust Display Brightness $\pm 1\%$ | Child of Clock Drawer |

---

## 🎨 Visual & Animation Architecture

### 1. The Lava-Lamp Wax Ooze (`@keyframes lava-ooze`)
When any capsule is hovered, its background morphs into a fluid multi-gradient linear wax flow (`180deg, @color1, @color2, @color3, @color5, @color7, @color2, @color1`) animated across an oversized `100% 400%` canvas over 4 seconds, accompanied by an inner layered glowing liquid drop-shadow.

```css
@keyframes lava-ooze {
    0%   { background-position: 0% 0%; }
    50%  { background-position: 50% 100%; }
    100% { background-position: 100% 0%; }
}
```

### 2. Snappy Spring Arrival & Clean Deceleration Return
- **Hover Entry (Snappy Spring)**: `transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);` creates an immediate, responsive pop.
- **Hover Exit (Zero-Jitter Deceleration)**: `transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);` smoothly settles the module back to resting dimensions with zero undershoot or jitter.

---

## 🧩 Custom Script Widgets

### ⏱️ Precision Stopwatch (`scripts/uptime.py`)
- Displays real-time session uptime with dynamic time-of-day icons (`󰖙` morning, `󰖝` evening, `󰖔` night) and active TTY.
- Left-clicking starts a background precision millisecond timer (`timer.json`).
- Clicking again stops the timer and immediately pops an OSD pill notification displaying the formatted duration (`00:02:14.382`).

### 🎵 Dynamic Media Player (`scripts/mediaplayer.py`)
- Automatically polls active MPRIS players (`Spotify`, `Firefox`, `Chromium`, `Brave`, `VLC`).
- Automatically hides the capsule when playback is idle and reveals on track play with branded icons (``, ``, ``, ``).

### 🧹 Friday Maintenance Checker (`scripts/friday_update.py`)
- Silently checks the day of the week. Remains completely invisible from Saturday through Thursday.
- On Fridays, pulses with a subtle maintenance badge (`󰏓 Friday Maintenance`) until clicked to execute mirrorlist optimization, `paru -Syu`, and Dusky desktop updates.

---

## 🚀 Installation & Switching

```bash
# Link to Dusky Waybar directory:
ln -s ~/waybarconf/hoverover ~/.config/waybar/21_hoverover

# Apply via Dusky TUI Switcher CLI:
python3 ~/user_scripts/waybar/tui_waybars.py --apply 21_hoverover
```
