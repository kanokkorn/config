import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

# Import qtile-extras popup tools
from qtile_extras.popup.toolkit import (
    PopupMenu,
    PopupMenuItem,
    PopupMenuSeparator,
    PopupRelativeLayout,
    PopupText,
)

# ---------------------------------------------------------------------------
# Colors & Style Settings
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

FOCUSED_BORDER   = colors["purple"]
NORMAL_BORDER    = colors["background"]
BORDER_WIDTH     = 1
WINDOW_GAP       = 0

mod = "mod4"          # Super key
alt = "mod1"          # Alt key
terminal = "xterm"
rofi_cmd = "rofi -modi drun -show drun"

# ---------------------------------------------------------------------------
# Groups (6 Workspaces with circle symbols)
# ---------------------------------------------------------------------------
groups = [Group(i, label="") for i in ["1", "2", "3", "4", "5", "6"]]

# ---------------------------------------------------------------------------
# Popups (System Menu, Volume, WiFi)
# ---------------------------------------------------------------------------

@lazy.function
def show_system_menu(qtile):
    """System menu popup on clicking power icon or launcher."""
    items = [
        PopupMenuItem(text="System Options", enabled=False),
        PopupMenuSeparator(),
        PopupMenuItem(text=" Reload Qtile", mouse_callbacks={"Button1": lazy.reload_config()}),
        PopupMenuItem(text=" Restart Qtile", mouse_callbacks={"Button1": lazy.restart()}),
        PopupMenuSeparator(),
        PopupMenuItem(text=" Lock Screen", mouse_callbacks={"Button1": lazy.spawn("slock")}),
        PopupMenuItem(text=" Power Off", mouse_callbacks={"Button1": lazy.spawn("poweroff")}),
    ]
    menu = PopupMenu.generate(qtile, menuitems=items, background=colors["bar_bg"], foreground=colors["foreground"])
    menu.show(centered=True)


@lazy.function
def show_volume_popup(qtile):
    """Volume control popup."""
    try:
        vol_output = subprocess.check_output(["amixer", "sget", "Master"]).decode("utf-8")
        vol_line = [line for line in vol_output.splitlines() if "Mono:" in line or "Left:" in line][0]
        vol = vol_line.split("[")[1].split("%]")[0] + "%"
    except Exception:
        vol = "N/A"

    controls = [
        PopupText(text=f"Volume: {vol}", pos_x=0.1, pos_y=0.15, width=0.8, height=0.3, h_align="center"),
        PopupText(
            text="[ Mute / Unmute ]",
            pos_x=0.1,
            pos_y=0.55,
            width=0.8,
            height=0.3,
            h_align="center",
            mouse_callbacks={"Button1": lambda: subprocess.run(["amixer", "set", "Master", "toggle"])},
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
    """Network popup showing status and connection."""
    try:
        ssid = subprocess.check_output(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"]).decode("utf-8")
        active_ssid = [line.split(":")[1] for line in ssid.splitlines() if line.startswith("yes")][0]
    except Exception:
        active_ssid = "Not Connected"

    controls = [
        PopupText(text=f"SSID: {active_ssid}", pos_x=0.1, pos_y=0.2, width=0.8, height=0.3, h_align="center"),
        PopupText(
            text="[ Network Settings ]",
            pos_x=0.1,
            pos_y=0.6,
            width=0.8,
            height=0.3,
            h_align="center",
            mouse_callbacks={"Button1": lambda: subprocess.run(["nm-connection-editor"])},
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
    # Launcher & Menus
    Key([alt], "space", lazy.spawn(rofi_cmd), desc="Rofi launcher"),
    Key([mod], "x", show_system_menu, desc="Show system popup menu"),

    # Window / Layout Controls
    Key([mod], "w", lazy.window.kill(), desc="Close window"),
    Key([mod], "m", lazy.next_layout(), desc="Toggle layout"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),

    # Focus navigation
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),

    # Qtile Controls
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, alt], "q", lazy.shutdown()),
]

# Group shortcuts
for i, group in enumerate(groups, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[group.name].toscreen()),
        Key([mod, "shift"], str(i), lazy.window.togroup(group.name, switch_group=True)),
    ])

# ---------------------------------------------------------------------------
# Layouts
# ---------------------------------------------------------------------------
layouts = [
    layout.Tile(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
        margin=WINDOW_GAP,
        ratio=0.55,
    ),
    layout.Max(),
    layout.Floating(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
    ),
]

# ---------------------------------------------------------------------------
# Helper Separator
# ---------------------------------------------------------------------------
def sep():
    return widget.TextBox(
        text="|",
        foreground=colors["sep"],
        padding=10,
        fontsize=12,
    )

# ---------------------------------------------------------------------------
# Screen Bar Configuration
# ---------------------------------------------------------------------------
widget_defaults = dict(
    font="Monospace",
    fontsize=12,
    padding=4,
    background=colors["bar_bg"],
    foreground=colors["foreground"],
)

screens = [
    Screen(
        top=bar.Bar(
            [
                # Left 1: Grid Launcher Icon
                widget.TextBox(
                    text=" 󰕮 ",
                    fontsize=14,
                    foreground=colors["purple"],
                    mouse_callbacks={"Button1": lazy.spawn(rofi_cmd)},
                    padding=6,
                ),
                sep(),

                # Left 2: Workspaces Circles
                widget.GroupBox(
                    font="Monospace",
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
                ),

                # Left Spacer (pushes Clock to center)
                widget.Spacer(),

                # Middle: Date & Time
                widget.Clock(
                    format="It's %A, %d %B %Y at %H:%M:%S",
                    foreground=colors["foreground"],
                    padding=6,
                ),

                # Right Spacer (pushes icons to right)
                widget.Spacer(),

                # Right 1: Keyboard Layout Indicator
                widget.KeyboardLayout(
                    configured_keyboards=["us", "th"],
                    display_map={"us": "us", "th": "th"},
                    foreground=colors["foreground"],
                    padding=6,
                ),
                sep(),

                # Right 2: WiFi Network Icon & SSID (Click opens WiFi popup)
                widget.TextBox(
                    text="󰤨",
                    foreground=colors["purple"],
                    fontsize=13,
                    padding=4,
                    mouse_callbacks={"Button1": show_wifi_popup},
                ),
                widget.Wlan(
                    format="{ssid}",
                    disconnected_message="Disconnected",
                    interface="wlan0",
                    foreground=colors["foreground"],
                    padding=4,
                    mouse_callbacks={"Button1": show_wifi_popup},
                ),
                sep(),

                # Right 3: Volume Icon & Meter (Click opens Volume popup)
                widget.TextBox(
                    text="󰕾",
                    foreground=colors["foreground"],
                    fontsize=13,
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

                # Right 4: Power Menu Button (Click opens System Menu popup)
                widget.TextBox(
                    text="󰐥 ",
                    foreground=colors["cyan"],
                    fontsize=14,
                    padding=6,
                    mouse_callbacks={"Button1": show_system_menu},
                ),
            ],
            size=26,
            background=colors["bar_bg"],
            margin=[0, 0, 0, 0],
        ),
    ),
]

# ---------------------------------------------------------------------------
# Mouse & Startup
# ---------------------------------------------------------------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["setxkbmap", "-layout", "us,th", "-option", "grp:caps_toggle"])

wmname = "LG3D"
