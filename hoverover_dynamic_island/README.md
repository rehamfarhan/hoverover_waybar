# 🏝️ Hoverover Dynamic Island (Top Bar)

A minimal, floating **Top Bar Dynamic Island** configuration for **Waybar** on **Hyprland** (Dusky Desktop Environment).

Featuring a **Permanently Visible Centered Workspace Island**, **Tucked-Up Side Modules** that reveal on hover with liquid multi-gradient lava-lamp animations, and the complete suite of interactive Dusky widgets.

---

## 🌟 Dynamic Island Concept

- **Resting State**: Only the centered `hyprland/workspaces` capsule is visible like an isolated floating pill. All side modules (drawers, notifications, network, uptime, audio, tray, clock) are tucked into the top bezel (`opacity: 0.01; margin-top: -10px; margin-bottom: 22px;`).
- **Hover Reveal**: Moving your cursor near the top edge smoothly drops the modules down (`opacity: 1; margin-top: 4px; margin-bottom: 4px;`) with fluid animated wax lava-lamp gradients and bouncy spring arrival.

---

## 🎮 Master Controls & Interactions Table

| Module | Icon / Display | LMB (Left Click) | RMB (Right Click) | MMB (Middle Click) | Scroll Up / Down | Hover Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Power Drawer** | `⏻` | Open **Wlogout** power menu | Lock screen (**Hyprlock**) | — | — | Expands drawer to reveal `Inhibit Suspend` |
| **Inhibit Suspend** | `󰌾` / `󰅶` | Toggle **Hypridle** auto-suspend | — | — | — | Child of Power Drawer |
| **Notifications** | `󰂚` (Count) | Open **Rofi** notification history | Toggle **Mako** DND mode | — | — | Reveals with Lava-Lamp Glow |
| **Network Drawer** | `` / `󰈀` | Open **Dusky TUI Network Manager** | Restart WiFi (off $\rightarrow$ on) + OSD toast | Turn WiFi **OFF** | — | Expands drawer to reveal `Bluetooth` |
| **Bluetooth** | `󰂯` / `󰂱` | Open **Blueman Manager** (GUI) | Open **Bluetui** (Terminal TUI) | Toggle Bluetooth Power + OSD toast | — | Child of Network Drawer |
| **Uptime & Stopwatch** | `󰔛` / Uptime | **Start / Stop Precision Stopwatch** (OSD duration toast) | — | — | Adjust Display Brightness $\pm 5\%$ | Reveals with Lava-Lamp Glow |
| **Friday Update** | `󰏓` / `󰑐` | Run mirrorlist ranking + `paru` + Dusky updates | — | — | — | **Auto-shows ONLY on Fridays** |
| **Workspaces (Island)** | Numbers / Icons | Switch to clicked workspace | — | — | Cycle workspace (`e-1` / `e+1`) | Permanent Island; glows on hover |
| **Active Window** | Title | Spawn `foot` on empty workspace & jump | Close window (`window.close`) | Toggle Scratchpad (`magic`) | Cycle workspace (`e-1` / `e+1`) | Reveals with Lava-Lamp Glow |
| **Sleep Monitor** | `󰒲` | Bedtime analysis OSD notification | — | Toggle DND | — | Reveals with Lava-Lamp Glow |
| **Media Player** | Track Title | **Play / Pause** toggle | **Stop** playback | — | Next / Previous track (`playerctl`) | Auto-hides when idle |
| **Audio Volume** | `` / Volume % | Open **Pavucontrol** mixer | Open **Cava** visualizer | **Restart Audio Server** (PipeWire) | Adjust volume $\pm 5\%$ (`pactl`) | Reveals with Lava-Lamp Glow |
| **System Tray** | Tray Icons | Standard Applet LMB action | Standard Applet RMB menu | — | — | Drops down into view |
| **Clock Drawer** | `󰥔` (Time) | Open **GNOME Clocks** | Toggle calendar mode / format | Open **Peaclock** terminal clock | Shift calendar month up / down | Expands to reveal `CPU` & `RAM` |
| **CPU Usage** | `` (Usage %) | Open **`btop`** monitor | Run **Sysbench CPU Benchmark** | — | Adjust Brightness $\pm 1\%$ | Child of Clock Drawer |
| **RAM Usage** | `` (Usage %) | Open **`btop`** monitor | Run **Dusky Disk I/O Monitor** | — | Adjust Brightness $\pm 1\%$ | Child of Clock Drawer |

---

## 🚀 Installation & Switching

```bash
# Link to Dusky Waybar directory:
ln -s ~/waybarconf/hoverover_dynamic_island ~/.config/waybar/22_hoverover_dynamic_island

# Apply via Dusky TUI Switcher CLI:
python3 ~/user_scripts/waybar/tui_waybars.py --apply 22_hoverover_dynamic_island
```
