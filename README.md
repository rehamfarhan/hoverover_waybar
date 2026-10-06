# 🚀 Waybar Configurations Monorepo (`waybarconf`)

A central repository of custom, highly interactive, and beautifully styled **Waybar** configurations crafted for **Hyprland** on Arch Linux (Dusky Desktop Environment).

---

## 📂 Configurations Index

| Configuration | Layout | Orientation | Highlights | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **[`hoverover`](./hoverover)** | **Bottom Dock** | Horizontal | 60% Frosted glass dock with 3 expanding hover drawers, fluid lava-lamp multi-gradient wax animations, and precision stopwatch. | [**View Docs ➔**](./hoverover/README.md) |
| **[`hoverover_dynamic_island`](./hoverover_dynamic_island)** | **Top Bar** | Horizontal | Floating centered workspace island with tucked side modules that smoothly drop down on hover. | [**View Docs ➔**](./hoverover_dynamic_island/README.md) |
| **[`bkcddots`](./bkcddots)** | **Right Dock** | Vertical (30px) | Ultra-compact vertical right dock with stacked clock, active app tracker, theme switcher, and grouped controls. | [**View Docs ➔**](./bkcddots/README.md) |

---

## 🛠️ Quick Start & Dusky TUI Integration

### 1. Clone or Place Repository
```bash
git clone https://github.com/rehamfarhan/waybarconf.git ~/waybarconf
```

### 2. Symlink into Dusky Waybar Directory
Link the configurations into `~/.config/waybar/` for automatic discovery by Dusky's TUI Switcher:

```bash
# Hoverover (Bottom Dock) -> 21_hoverover
ln -s ~/waybarconf/hoverover ~/.config/waybar/21_hoverover

# Dynamic Island (Top Bar) -> 22_hoverover_dynamic_island
ln -s ~/waybarconf/hoverover_dynamic_island ~/.config/waybar/22_hoverover_dynamic_island

# BKCCDots (Vertical Right Dock) -> 20_bkcddots
ln -s ~/waybarconf/bkcddots ~/.config/waybar/20_bkcddots
```

### 3. Switch Live via Dusky CLI
```bash
# Switch to Hoverover:
python3 ~/user_scripts/waybar/tui_waybars.py --apply 21_hoverover

# Switch to Dynamic Island:
python3 ~/user_scripts/waybar/tui_waybars.py --apply 22_hoverover_dynamic_island

# Switch to BKCCDots:
python3 ~/user_scripts/waybar/tui_waybars.py --apply 20_bkcddots
```

---

## ➕ Adding New Configurations to this Repo

To add a new custom Waybar configuration to `waybarconf`:

1. Create a new directory inside `~/waybarconf/` (e.g. `~/waybarconf/my_new_bar/`).
2. Add your `config.jsonc`, `modules.jsonc`, `style.css`, and `scripts/`.
3. Symlink it to `~/.config/waybar/<prefix>_my_new_bar`:
   ```bash
   ln -s ~/waybarconf/my_new_bar ~/.config/waybar/23_my_new_bar
   ```
4. Commit and push from `~/waybarconf`:
   ```bash
   cd ~/waybarconf
   git add .
   git commit -m "feat: add my_new_bar configuration"
   git push origin master
   ```

---

## 📦 Core Dependencies

- **Wayland / Compositor**: `hyprland`, `waybar`
- **Notifications**: `mako` (`makoctl`), `rofi`
- **Media & Audio**: `playerctl`, `pulseaudio-utils` (`pactl`), `pavucontrol`, `cava`
- **Connectivity**: `blueman`, `bluez-utils`, `networkmanager`
- **Terminals & System**: `foot`, `kitty`, `btop`, `wlogout`, `hyprlock`, `hypridle`
