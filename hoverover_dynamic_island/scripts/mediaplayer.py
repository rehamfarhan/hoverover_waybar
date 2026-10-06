#!/usr/bin/env python3
import gi
gi.require_version("Playerctl", "2.0")
from gi.repository import Playerctl, GLib
from gi.repository.Playerctl import Player
import argparse
import logging
import sys
import signal
import json
import os
from typing import List

logger = logging.getLogger(__name__)

def signal_handler(sig, frame):
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.exit(0)

class PlayerManager:
    def __init__(self, selected_player=None, excluded_player=None):
        self.manager = Playerctl.PlayerManager()
        self.loop = GLib.MainLoop()
        self.manager.connect("name-appeared", lambda *args: self.on_player_appeared(*args))
        self.manager.connect("player-vanished", lambda *args: self.on_player_vanished(*args))

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGPIPE, signal_handler)
        
        self.selected_player = selected_player
        self.excluded_player = excluded_player.split(",") if excluded_player else []

        self.init_players()

    def init_players(self):
        for player in self.manager.props.player_names:
            if player.name in self.excluded_player:
                continue
            if self.selected_player is not None and self.selected_player != player.name:
                continue
            self.init_player(player)
        
        if not self.manager.props.players:
            self.clear_output()

    def run(self):
        self.loop.run()

    def init_player(self, player):
        p = Playerctl.Player.new_from_name(player)
        p.connect("playback-status", self.on_playback_status_changed, None)
        p.connect("metadata", self.on_metadata_changed, None)
        self.manager.manage_player(p)
        self.on_metadata_changed(p, p.props.metadata)

    def get_players(self) -> List[Player]:
        return self.manager.props.players

    def write_output(self, text, tooltip, css_class="media"):
        output = {
            "text": text,
            "tooltip": tooltip,
            "class": css_class
        }
        sys.stdout.write(json.dumps(output) + "\n")
        sys.stdout.flush()

    def clear_output(self):
        sys.stdout.write(json.dumps({"text": "", "class": "hidden"}) + "\n")
        sys.stdout.flush()

    def on_playback_status_changed(self, player, status, _=None):
        self.on_metadata_changed(player, player.props.metadata)

    def get_first_playing_player(self):
        players = self.get_players()
        if players:
            for player in reversed(players):
                if player.props.status == "Playing":
                    return player
            # If any are paused, return the first paused player
            for player in reversed(players):
                if player.props.status == "Paused":
                    return player
        return None

    def show_most_important_player(self):
        current_player = self.get_first_playing_player()
        if current_player is not None:
            self.on_metadata_changed(current_player, current_player.props.metadata)
        else:
            self.clear_output()

    def on_metadata_changed(self, player, metadata, _=None):
        # Hide if player is stopped
        if player.props.status not in ["Playing", "Paused"]:
            self.clear_output()
            return

        player_name = (player.props.player_name or "").lower()
        artist = player.get_artist() or ""
        title = player.get_title() or ""
        album = metadata.get("xesam:album", "") or ""

        # Clean HTML characters
        title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        artist = artist.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        album = album.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        if "spotify" in player_name and "mpris:trackid" in metadata and ":ad:" in str(metadata.get("mpris:trackid")):
            track_text = "Spotify Ad"
        elif artist and title:
            track_text = f"{artist} - {title}"
        elif title:
            track_text = title
        else:
            track_text = f"{player.props.player_name.capitalize()}"

        # Brand Icon
        if "spotify" in player_name:
            brand_icon = ""
        elif "firefox" in player_name or "zen" in player_name:
            brand_icon = ""
        elif "chromium" in player_name or "chrome" in player_name or "brave" in player_name:
            brand_icon = ""
        elif "mpv" in player_name:
            brand_icon = ""
        elif "vlc" in player_name:
            brand_icon = "󰕼"
        else:
            brand_icon = ""

        # Status icon
        status_icon = "" if player.props.status == "Playing" else ""
        formatted_text = f"{status_icon} {brand_icon} {track_text}"

        tooltip_lines = [
            f"Player: {player.props.player_name.capitalize()}",
            f"Status: {player.props.status}",
            f"Title: {title or 'Unknown'}"
        ]
        if artist:
            tooltip_lines.append(f"Artist: {artist}")
        if album:
            tooltip_lines.append(f"Album: {album}")
        
        tooltip_lines.append("\nControls:\n  LMB: Play/Pause\n  RMB: Stop\n  Scroll: Next/Prev Track")
        tooltip = "\n".join(tooltip_lines)

        current_playing = self.get_first_playing_player()
        if current_playing is None or current_playing.props.player_name == player.props.player_name:
            self.write_output(formatted_text, tooltip, f"custom-{player.props.player_name}")

    def on_player_appeared(self, _, player):
        if player.name in self.excluded_player:
            return
        if self.selected_player is None or player.name == self.selected_player:
            self.init_player(player)

    def on_player_vanished(self, _, player):
        self.show_most_important_player()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-x", "--exclude", help="Comma-separated list of excluded players")
    parser.add_argument("--player", help="Player to listen to")
    return parser.parse_args()

def main():
    args = parse_arguments()
    logger.setLevel(max((3 - args.verbose) * 10, 0))
    player = PlayerManager(args.player, args.exclude)
    player.run()

if __name__ == "__main__":
    main()