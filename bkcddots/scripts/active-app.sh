#!/usr/bin/env bash

class=$(hyprctl activewindow -j | jq -r '.class')

case "$class" in
    kitty) echo "  Kitty" ;;
    firefox) echo "  Firefox" ;;
    microsoft-edge) echo "󰇩  Microsoft Edge" ;;
    google-chrome) echo "  Google Chrome" ;;
    code) echo "󰨞  VS Code" ;;
    codium) echo "󰨞  VSCodium" ;;
    org.gnome.Nautilus) echo "󰉋  Files" ;;
    thunar) echo "󰉋  Thunar" ;;
    discord) echo "  Discord" ;;
    Spotify) echo "  Spotify" ;;
    steam) echo "  Steam" ;;
    obsidian) echo "󱓧  Obsidian" ;;
    pavucontrol) echo "  Audio" ;;
    btop) echo "  Btop" ;;

    *)
        name=$(echo "$class" | sed \
            -e 's/^org\.[^.]*\.//' \
            -e 's/-/ /g' \
            -e 's/\b\(.\)/\u\1/g')

        if [ -z "$name" ] || [ "$name" = "null" ] || [ "$name" = "Null" ]; then
            echo "  Arch"
        else
            echo "󰣆  $name"
        fi
        ;;
esac
