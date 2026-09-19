# Qtile configuration converted from bspwm + sxhkd + polybar forest theme
# Place this file at: ~/.config/qtile/config.py
#
# Original sources:
#   - bspwmrc (workspaces, borders, gaps)
#   - sxhkdrc (keybindings)
#   - polybar forest theme (adi1090x/polybar-themes)

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

# ---------------------------------------------------------------------------
# Colors (from polybar forest theme - colors.ini)
# ---------------------------------------------------------------------------
colors = {
    "background": "#212B30",
    "foreground": "#C4C7C5",
    "sep":        "#3F5360",
    "white":      "#FFFFFF",
    "black":      "#000000",
    "red":        "#EC7875",
    "pink":       "#EC407A",
    "purple":     "#BA68C8",
    "blue":       "#42A5F5",
    "cyan":       "#4DD0E1",
    "teal":       "#00B19F",
    "green":      "#61C766",
    "lime":       "#B9C244",
    "yellow":     "#FDD835",
    "amber":      "#FBC02D",
    "orange":     "#E57C46",
    "brown":      "#AC8476",
    "indigo":     "#6C77BB",
    "gray":       "#9E9E9E",
    "blue_gray":  "#6D8895",
}

# Border colors from original bspwmrc
FOCUSED_BORDER   = "#373737"
NORMAL_BORDER    = "#1B1A17"
BORDER_WIDTH     = 4
WINDOW_GAP       = 12

mod = "mod4"          # Super key
alt = "mod1"          # Alt key
terminal = "alacritty"
rofi_cmd = "rofi -modi drun -show drun"

# ---------------------------------------------------------------------------
# Groups (workspaces) – matches bspwm: I II III IV V VI
# ---------------------------------------------------------------------------
groups = [Group(i) for i in ["I", "II", "III", "IV", "V", "VI"]]

# ---------------------------------------------------------------------------
# Keybindings (converted from sxhkdrc + common qtile defaults)
# ---------------------------------------------------------------------------
keys = [
    # ---------- Terminal ----------
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # ---------- Language switcher (Thai / US) ----------
    Key([mod], "space", lazy.spawn("setxkbmap th"), desc="Switch to Thai"),
    # Note: original used super+@space to toggle. Here we use a simple toggle.
    # For proper toggle you can use a script; simple version below:
    Key([mod, "shift"], "space", lazy.spawn("setxkbmap us"), desc="Switch to US"),

    # ---------- Program launcher ----------
    Key([alt], "space", lazy.spawn(rofi_cmd), desc="Rofi launcher"),

    # ---------- Screenshots ----------
    Key([], "Print",
        lazy.spawn("scrot '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/shots/'"),
        desc="Fullscreen screenshot"),
    Key([mod, "shift"], "s",
        lazy.spawn("sleep 0.2; scrot -s '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/shots/'"),
        desc="Selection screenshot"),

    # ---------- Magnifier (boomer) ----------
    Key(["control", "shift"], "z", lazy.spawn("boomer"), desc="Screen magnifier"),

    # ---------- Reload / Quit ----------
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload Qtile config"),
    Key([mod, alt], "q", lazy.shutdown(), desc="Quit Qtile"),
    Key([mod, alt], "r", lazy.restart(), desc="Restart Qtile"),

    # ---------- Close / Kill window ----------
    Key([mod], "w", lazy.window.kill(), desc="Close window"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Force kill window"),

    # ---------- Layout toggle (tiled <-> monocle/max) ----------
    Key([mod], "m", lazy.next_layout(), desc="Toggle layout (monocle)"),

    # ---------- Window states ----------
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod, "shift"], "t", lazy.window.toggle_floating(), desc="Toggle floating (alt)"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "s", lazy.window.toggle_floating(), desc="Floating (s)"),

    # ---------- Focus / Swap (hjkl) ----------
    Key([mod], "h", lazy.layout.left(), desc="Focus left"),
    Key([mod], "j", lazy.layout.down(), desc="Focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Focus right"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Swap left"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Swap down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Swap up"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Swap right"),

    # ---------- Focus next/prev window ----------
    Key([mod], "c", lazy.layout.next(), desc="Focus next window"),
    Key([mod, "shift"], "c", lazy.layout.previous(), desc="Focus previous window"),

    # ---------- Focus next/prev group ----------
    Key([mod], "bracketleft", lazy.screen.prev_group(), desc="Previous group"),
    Key([mod], "bracketright", lazy.screen.next_group(), desc="Next group"),

    # ---------- Last window / group ----------
    Key([mod], "grave", lazy.screen.toggle_group(), desc="Last group"),
    Key([mod], "Tab", lazy.screen.toggle_group(), desc="Last group (Tab)"),

    # ---------- Grow / Shrink windows ----------
    Key([mod, alt], "h", lazy.layout.grow_left(), desc="Grow left"),
    Key([mod, alt], "j", lazy.layout.grow_down(), desc="Grow down"),
    Key([mod, alt], "k", lazy.layout.grow_up(), desc="Grow up"),
    Key([mod, alt], "l", lazy.layout.grow_right(), desc="Grow right"),

    Key([mod, alt, "shift"], "h", lazy.layout.shrink_left(), desc="Shrink left"),
    Key([mod, alt, "shift"], "j", lazy.layout.shrink_down(), desc="Shrink down"),
    Key([mod, alt, "shift"], "k", lazy.layout.shrink_up(), desc="Shrink up"),
    Key([mod, alt, "shift"], "l", lazy.layout.shrink_right(), desc="Shrink right"),

    # ---------- Move floating window ----------
    Key([mod], "Left",  lazy.window.move_floating(-20, 0), desc="Move floating left"),
    Key([mod], "Down",  lazy.window.move_floating(0, 20),  desc="Move floating down"),
    Key([mod], "Up",    lazy.window.move_floating(0, -20), desc="Move floating up"),
    Key([mod], "Right", lazy.window.move_floating(20, 0),  desc="Move floating right"),

    # ---------- Media keys ----------
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse sset Master 5%+ unmute"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse sset Master 5%- unmute"), desc="Volume down"),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"), desc="Mute"),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"), desc="Play/Pause"),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"), desc="Previous track"),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"), desc="Next track"),
]

# Group switching (super + 1-6 and super+shift + 1-6 to move)
for i, group in enumerate(groups, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"),
        Key([mod, "shift"], str(i),
            lazy.window.togroup(group.name, switch_group=True),
            desc=f"Move window to group {group.name}"),
    ])

# ---------------------------------------------------------------------------
# Layouts (inspired by bspwm: tiled + monocle)
# ---------------------------------------------------------------------------
layouts = [
    layout.Columns(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
        margin=WINDOW_GAP,
        border_on_single=True,
        insert_position=1,
    ),
    layout.Max(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=0,
        margin=0,
    ),
    layout.Floating(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
    ),
]

# ---------------------------------------------------------------------------
# Floating rules
# ---------------------------------------------------------------------------
floating_layout = layout.Floating(
    border_focus=FOCUSED_BORDER,
    border_normal=NORMAL_BORDER,
    border_width=BORDER_WIDTH,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="pinentry-gtk-2"),
        Match(wm_class="pinentry-qt"),
    ],
)

# ---------------------------------------------------------------------------
# Widgets / Bar  (polybar forest inspired)
# ---------------------------------------------------------------------------
widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=13,
    padding=6,
    background=colors["background"],
    foreground=colors["foreground"],
)
extension_defaults = widget_defaults.copy()


def sep():
    return widget.TextBox(
        text="|",
        foreground=colors["sep"],
        padding=8,
        fontsize=14,
    )


screens = [
    Screen(
        top=bar.Bar(
            [
                # Launcher hint
                widget.TextBox(
                    text=" 󰣇 ",          # Arch / apps icon
                    fontsize=16,
                    foreground=colors["green"],
                    mouse_callbacks={"Button1": lazy.spawn(rofi_cmd)},
                    padding=8,
                ),
                sep(),

                # Workspaces
                widget.GroupBox(
                    font="Iosevka Nerd Font",
                    fontsize=13,
                    margin_y=3,
                    margin_x=2,
                    padding_y=5,
                    padding_x=8,
                    borderwidth=2,
                    active=colors["foreground"],
                    inactive=colors["gray"],
                    rounded=False,
                    highlight_method="line",
                    this_current_screen_border=colors["green"],
                    this_screen_border=colors["blue_gray"],
                    other_current_screen_border=colors["orange"],
                    other_screen_border=colors["sep"],
                    urgent_border=colors["red"],
                    urgent_text=colors["red"],
                    disable_drag=True,
                    hide_unused=False,
                ),
                sep(),

                # Window name
                widget.WindowName(
                    foreground=colors["foreground"],
                    max_chars=60,
                    padding=8,
                ),

                # Spacer pushes everything else to the right
                widget.Spacer(),

                # CPU
                widget.TextBox(
                    text="󰻠",
                    foreground=colors["yellow"],
                    fontsize=14,
                    padding=4,
                ),
                widget.CPU(
                    format="{load_percent}%",
                    foreground=colors["foreground"],
                    update_interval=2.0,
                    padding=4,
                ),
                sep(),

                # Memory
                widget.TextBox(
                    text="󰍛",
                    foreground=colors["indigo"],
                    fontsize=14,
                    padding=4,
                ),
                widget.Memory(
                    format="{MemUsed:.0f}{mm}",
                    foreground=colors["foreground"],
                    update_interval=2.0,
                    padding=4,
                ),
                sep(),

                # Filesystem (root)
                widget.TextBox(
                    text="󰋊",
                    foreground=colors["orange"],
                    fontsize=14,
                    padding=4,
                ),
                widget.DF(
                    format="{uf}{m}",
                    visible_on_warn=False,
                    foreground=colors["foreground"],
                    update_interval=30,
                    padding=4,
                    partition="/",
                ),
                sep(),

                # Volume
                widget.TextBox(
                    text="󰕾",
                    foreground=colors["blue"],
                    fontsize=14,
                    padding=4,
                ),
                widget.Volume(
                    foreground=colors["foreground"],
                    padding=4,
                    update_interval=0.5,
                ),
                sep(),

                # Battery (if present)
                widget.Battery(
                    format="{char} {percent:2.0%}",
                    charge_char="󰂄",
                    discharge_char="󰁹",
                    full_char="󰁹",
                    unknown_char="󰂑",
                    empty_char="󰂎",
                    foreground=colors["pink"],
                    low_foreground=colors["red"],
                    low_percentage=0.2,
                    update_interval=30,
                    padding=6,
                    show_short_text=False,
                ),
                sep(),

                # Network
                widget.Net(
                    format="{down:.0f}↓ {up:.0f}↑",
                    foreground=colors["cyan"],
                    update_interval=2.0,
                    padding=6,
                ),
                sep(),

                # Clock / Date
                widget.TextBox(
                    text="󰥔",
                    foreground=colors["red"],
                    fontsize=14,
                    padding=4,
                ),
                widget.Clock(
                    format="%A, %d %B  %I:%M %p",
                    foreground=colors["foreground"],
                    padding=6,
                ),
                sep(),

                # System tray
                widget.Systray(
                    icon_size=18,
                    padding=6,
                ),
                widget.TextBox(text=" ", padding=4),
            ],
            size=34,                          # matches polybar height
            background=colors["background"],
            margin=[0, 0, 0, 0],
            border_width=[0, 0, 0, 0],
            opacity=1.0,
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
# Other settings
# ---------------------------------------------------------------------------
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

# Java apps fix
wmname = "LG3D"

# ---------------------------------------------------------------------------
# Autostart
# ---------------------------------------------------------------------------
@hook.subscribe.startup_once
def autostart():
    """Run once when Qtile starts."""
    home = os.path.expanduser("~")
    # Optional: set wallpaper (uncomment and adjust path)
    # subprocess.Popen(["feh", "--bg-fill", f"{home}/Pictures/grey.png"])
    # Optional: start compositor
    # subprocess.Popen(["picom", "--experimental-backends"])
    # Make sure sxhkd is NOT running (we use Qtile keys instead)
    # You can still keep sxhkd for extra media/extra keys if desired.
    pass


@hook.subscribe.startup
def restart_hook():
    """Run on every (re)start."""
    pass
