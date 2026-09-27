# Qtile config – fixed & cleaned
# - Font: DejaVu Sans Mono (ships with virtually every Linux distro)
# - Style: minimal dwm-like (thin borders, zero gap, Tile layout, simple bar)
# - Keyboard: setxkbmap us,th + grp:caps_toggle (Caps Lock switches EN ↔ TH)
# - Only real APIs from Qtile + qtile-extras docs

import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

# qtile-extras popup toolkit (official import path from docs)
from qtile_extras.popup import (
    PopupMenu,
    PopupMenuItem,
    PopupMenuSeparator,
    PopupRelativeLayout,
    PopupText,
)

# ---------------------------------------------------------------------------
# Colors (dark, minimal)
# ---------------------------------------------------------------------------
colors = {
    "background": "#1A1B1E",
    "foreground": "#C4C7C5",
    "sep":        "#3F5360",
    "purple":     "#C084FC",
    "teal":       "#2DD4BF",
    "green":      "#34D399",
    "yellow":     "#FACC15",
    "cyan":       "#38BDF8",
    "red":        "#F87171",
    "dim_gray":   "#4B5563",
    "bar_bg":     "#111215",
}

FOCUSED_BORDER = colors["purple"]
NORMAL_BORDER  = colors["background"]
BORDER_WIDTH   = 1
WINDOW_GAP     = 0

mod = "mod4"
alt = "mod1"
terminal = "xterm"
rofi_cmd = "rofi -modi drun -show drun"

# Portable monospace font available on almost all distros
FONT = "DejaVu Sans Mono"

# ---------------------------------------------------------------------------
# Groups (plain numbers – dwm style, no Nerd Font required)
# ---------------------------------------------------------------------------
groups = [Group(i) for i in "123456"]

# ---------------------------------------------------------------------------
# Popups (verified against qtile-extras docs)
# ---------------------------------------------------------------------------

@lazy.function
def show_system_menu(qtile):
    items = [
        PopupMenuItem(text="System", enabled=False),
        PopupMenuSeparator(),
        PopupMenuItem(
            text="Reload config",
            mouse_callbacks={"Button1": lazy.reload_config()},
        ),
        PopupMenuItem(
            text="Restart Qtile",
            mouse_callbacks={"Button1": lazy.restart()},
        ),
        PopupMenuSeparator(),
        PopupMenuItem(
            text="Lock",
            mouse_callbacks={"Button1": lazy.spawn("slock")},
        ),
        PopupMenuItem(
            text="Power off",
            mouse_callbacks={"Button1": lazy.spawn("poweroff")},
        ),
    ]
    menu = PopupMenu.generate(
        qtile,
        menuitems=items,
        background=colors["bar_bg"],
        foreground=colors["foreground"],
    )
    menu.show(centered=True)


@lazy.function
def show_volume_popup(qtile):
    try:
        out = subprocess.check_output(["amixer", "sget", "Master"]).decode()
        line = next(l for l in out.splitlines() if "Mono:" in l or "Left:" in l)
        vol = line.split("[")[1].split("%]")[0] + "%"
    except Exception:
        vol = "N/A"

    controls = [
        PopupText(
            text=f"Volume: {vol}",
            pos_x=0.1,
            pos_y=0.15,
            width=0.8,
            height=0.3,
            h_align="center",
        ),
        PopupText(
            text="[ Mute / Unmute ]",
            pos_x=0.1,
            pos_y=0.55,
            width=0.8,
            height=0.3,
            h_align="center",
            mouse_callbacks={"Button1": lazy.spawn("amixer set Master toggle")},
        ),
    ]
    popup = PopupRelativeLayout(
        qtile,
        width=220,
        height=100,
        controls=controls,
        background=colors["bar_bg"],
        foreground=colors["foreground"],
        border=colors["sep"],
        border_width=1,
    )
    popup.show(centered=True)


@lazy.function
def show_wifi_popup(qtile):
    try:
        out = subprocess.check_output(
            ["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"]
        ).decode()
        active = [l.split(":")[1] for l in out.splitlines() if l.startswith("yes:")]
        ssid = active[0] if active else "Not connected"
    except Exception:
        ssid = "Not connected"

    controls = [
        PopupText(
            text=f"SSID: {ssid}",
            pos_x=0.1,
            pos_y=0.2,
            width=0.8,
            height=0.3,
            h_align="center",
        ),
        PopupText(
            text="[ Network settings ]",
            pos_x=0.1,
            pos_y=0.6,
            width=0.8,
            height=0.3,
            h_align="center",
            mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
        ),
    ]
    popup = PopupRelativeLayout(
        qtile,
        width=260,
        height=110,
        controls=controls,
        background=colors["bar_bg"],
        foreground=colors["foreground"],
        border=colors["sep"],
        border_width=1,
    )
    popup.show(centered=True)


# ---------------------------------------------------------------------------
# Keybindings
# ---------------------------------------------------------------------------
keys = [
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Launcher
    Key([alt], "space", lazy.spawn(rofi_cmd), desc="Rofi launcher"),
    Key([mod], "x", show_system_menu, desc="System menu"),

    # Window / layout
    Key([mod], "w", lazy.window.kill(), desc="Close window"),
    Key([mod], "m", lazy.next_layout(), desc="Next layout"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Floating"),

    # Focus (hjkl)
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),

    # Keyboard layout: Caps Lock toggles us ↔ th
    # (set via setxkbmap -option grp:caps_toggle in autostart)
    # Widget below still shows current layout; click it to cycle if desired.

    # Qtile
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, alt], "q", lazy.shutdown()),
]

# Group keys
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True)),
    ])

# ---------------------------------------------------------------------------
# Layouts (dwm-like master + stack)
# ---------------------------------------------------------------------------
layouts = [
    layout.Tile(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
        margin=WINDOW_GAP,
        ratio=0.55,
        master_length=1,
        expand=True,
    ),
    layout.Max(
        border_width=0,
        margin=0,
    ),
    layout.Floating(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
    ),
]

floating_layout = layout.Floating(
    border_focus=FOCUSED_BORDER,
    border_normal=NORMAL_BORDER,
    border_width=BORDER_WIDTH,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def sep():
    return widget.TextBox(
        text="|",
        foreground=colors["sep"],
        padding=8,
        fontsize=11,
    )

# ---------------------------------------------------------------------------
# Bar (minimal / dwm-inspired)
# ---------------------------------------------------------------------------
widget_defaults = dict(
    font=FONT,
    fontsize=12,
    padding=4,
    background=colors["bar_bg"],
    foreground=colors["foreground"],
)

screens = [
    Screen(
        top=bar.Bar(
            [
                # Launcher
                widget.TextBox(
                    text=" [apps] ",
                    fontsize=11,
                    foreground=colors["purple"],
                    mouse_callbacks={"Button1": lazy.spawn(rofi_cmd)},
                    padding=4,
                ),
                sep(),

                # Workspaces (plain numbers)
                widget.GroupBox(
                    font=FONT,
                    fontsize=12,
                    margin_y=0,
                    margin_x=0,
                    padding_y=0,
                    padding_x=6,
                    borderwidth=0,
                    active=colors["teal"],
                    inactive=colors["dim_gray"],
                    rounded=False,
                    highlight_method="text",
                    this_current_screen_border=colors["teal"],
                    disable_drag=True,
                    hide_unused=False,
                ),

                widget.Spacer(),

                # Center clock
                widget.Clock(
                    format="%a %d %b  %H:%M",
                    foreground=colors["foreground"],
                    padding=6,
                ),

                widget.Spacer(),

                # Keyboard layout indicator (Caps Lock toggles; click widget also cycles)
                widget.KeyboardLayout(
                    configured_keyboards=["us", "th"],
                    display_map={"us": "US", "th": "TH"},
                    foreground=colors["foreground"],
                    padding=6,
                ),
                sep(),

                # Wi-Fi (requires python-iwlib; falls back gracefully if missing)
                widget.TextBox(
                    text="net",
                    foreground=colors["purple"],
                    fontsize=11,
                    padding=4,
                    mouse_callbacks={"Button1": show_wifi_popup},
                ),
                widget.Wlan(
                    format="{essid}",
                    disconnected_message="down",
                    interface="wlan0",
                    foreground=colors["foreground"],
                    padding=4,
                    mouse_callbacks={"Button1": show_wifi_popup},
                ),
                sep(),

                # Volume
                widget.TextBox(
                    text="vol",
                    foreground=colors["foreground"],
                    fontsize=11,
                    padding=4,
                    mouse_callbacks={"Button1": show_volume_popup},
                ),
                widget.Volume(
                    emoji=False,
                    fmt="{}",
                    foreground=colors["yellow"],
                    padding=4,
                    mouse_callbacks={"Button1": show_volume_popup},
                ),
                sep(),

                # Power menu
                widget.TextBox(
                    text="pwr ",
                    foreground=colors["cyan"],
                    fontsize=11,
                    padding=4,
                    mouse_callbacks={"Button1": show_system_menu},
                ),
            ],
            size=24,
            background=colors["bar_bg"],
            margin=[0, 0, 0, 0],
        ),
    ),
]

# ---------------------------------------------------------------------------
# Mouse
# ---------------------------------------------------------------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------
@hook.subscribe.startup_once
def autostart():
    # Primary keyboard switch: Caps Lock toggles between us and th
    subprocess.Popen([
        "setxkbmap",
        "-layout", "us,th",
        "-option", "grp:caps_toggle",
    ])


# Java apps
wmname = "LG3D"
