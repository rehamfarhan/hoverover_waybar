#!/bin/bash

# Dusky Gamemode Toggle for Hyprland
HYPR_STATE=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')

if [ "$HYPR_STATE" = "1" ]; then
    # Disable animations, shadows, blur, and borders for maximum gaming performance
    hyprctl --batch "
        keyword animations:enabled 0;
        keyword decoration:drop_shadow 0;
        keyword decoration:blur:enabled 0;
        keyword general:gaps_in 0;
        keyword general:gaps_out 0;
        keyword general:border_size 1;
        keyword decoration:rounding 0"
    
    notify-send -a "OSD" -i "input-gaming" -h string:x-canonical-private-synchronous:"gamemode" "Gamemode Enabled" "High performance profile active (animations/blur off)"
    echo '{"text": "󰓓", "class": "enabled", "tooltip": "Gamemode: ON (Performance Mode)"}'
else
    # Re-enable standard settings
    hyprctl --batch "
        keyword animations:enabled 1;
        keyword decoration:drop_shadow 1;
        keyword decoration:blur:enabled 1;
        keyword general:gaps_in 4;
        keyword general:gaps_out 8;
        keyword general:border_size 2;
        keyword decoration:rounding 10"
        
    notify-send -a "OSD" -i "input-gaming" -h string:x-canonical-private-synchronous:"gamemode" "Gamemode Disabled" "Standard desktop profile restored"
    echo '{"text": "󰓓", "class": "disabled", "tooltip": "Gamemode: OFF"}'
fi
