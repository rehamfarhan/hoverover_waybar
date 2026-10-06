# 🎯 BKCCDots Waybar (Vertical Right Dock)

A sleek, ultra-thin **Vertical Right-Edge Status Bar** for **Waybar** on **Hyprland** (Dusky Desktop Environment).

Designed for minimal screen footprint with a vertical orientation (width: 30px), stacked multi-line clock format, interactive workspaces, grouped connections, media controls, theme switcher, and power action buttons.

---

## 🌟 Layout & Key Features

- **Orientation**: Vertical on right screen edge (`"position": "right"`, `"width": 30`).
- **Clock**: Stacked Arch Linux badge + Hours / Minutes layout (`\n%I\n%M`) with rich calendar popups and scroll navigation.
- **Active App Icon**: Dynamic SVG/Nerd Font active application icon tracking.
- **Grouped Controls**:
  - `group/media`: Media player controls tucked vertically.
  - `group/connections`: Network and Bluetooth quick toggles.
  - `custom/theme`: Direct wallpaper & Matugen color palette switcher.
  - `custom/power`: Quick access to Wlogout and screen lock.

---

## 🚀 Installation & Switching

```bash
# Link to Dusky Waybar directory:
ln -s ~/waybarconf/bkcddots ~/.config/waybar/20_bkcddots

# Apply via Dusky TUI Switcher CLI:
python3 ~/user_scripts/waybar/tui_waybars.py --apply 20_bkcddots
```
