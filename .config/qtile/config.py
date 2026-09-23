# Qtile configuration updated for dwm styling, universal fonts, and bidirectional layout toggling
# Place this file at: ~/.config/qtile/config.py

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os

# ---------------------------------------------------------------------------
# Colors (dwm color scheme)
# ---------------------------------------------------------------------------
colors = {
    "norm_bg":     "#222222",
    "norm_fg":     "#bbbbbb",
    "norm_border": "#444444",
    "sel_bg":      "#005577",
    "sel_fg":      "#eeeeee",
    "sel_border":  "#005577",
}

FOCUSED_BORDER   = colors["sel_border"]
NORMAL_BORDER    = colors["norm_border"]
BORDER_WIDTH     = 1
WINDOW_GAP       = 0

mod = "mod4"          # Super key
alt = "mod1"          # Alt key
terminal = "xterm"
rofi_cmd = "rofi -modi drun -show drun"

# ---------------------------------------------------------------------------
# Groups (workspaces) – standard 1-9 numbering matching dwm
# ---------------------------------------------------------------------------
groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

# ---------------------------------------------------------------------------
# Keybindings
# ---------------------------------------------------------------------------
keys = [
    # ---------- Terminal ----------
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # ---------- Language switcher (Toggle between US and TH) ----------
    Key([mod], "space", lazy.spawn("setxkbmap -query | grep -q 'th' && setxkbmap us || setxkbmap us,th -option grp:toggle,grp_led:scroll th"), desc="Toggle US / Thai layout"),

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

    # ---------- Layout toggle ----------
    Key([mod], "m", lazy.next_layout(), desc="Toggle layout"),

    # ---------- Window states ----------
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod, "shift"], "t", lazy.window.toggle_floating(), desc="Toggle floating (alt)"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

    # ---------- Focus / Swap ----------
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

    # ---------- Last group ----------
    Key([mod], "Tab", lazy.screen.toggle_group(), desc="Last group"),

    # ---------- Media keys ----------
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse sset Master 5%+ unmute"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse sset Master 5%- unmute"), desc="Volume down"),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"), desc="Mute"),
]

# Group switching (super + 1-9 and super+shift + 1-9 to move)
for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"),
        Key([mod, "shift"], group.name,
            lazy.window.togroup(group.name, switch_group=True),
            desc=f"Move window to group {group.name}"),
    ])

# ---------------------------------------------------------------------------
# Layouts (dwm tile standard: no gap, 1px border)
# ---------------------------------------------------------------------------
layouts = [
    layout.Tile(
        border_focus=FOCUSED_BORDER,
        border_normal=NORMAL_BORDER,
        border_width=BORDER_WIDTH,
        margin=WINDOW_GAP,
        ratio=0.55,
        add_after_last=True,
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
# Widgets / Bar (dwm style)
# ---------------------------------------------------------------------------
widget_defaults = dict(
    font="Monospace",
    fontsize=11,
    padding=6,
    background=colors["norm_bg"],
    foreground=colors["norm_fg"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # Workspaces block (dwm tags style)
                widget.GroupBox(
                    font="Monospace",
                    fontsize=11,
                    margin_y=0,
                    margin_x=0,
                    padding_y=2,
                    padding_x=6,
                    borderwidth=0,
                    active=colors["norm_fg"],
                    inactive="#666666",
                    rounded=False,
                    highlight_method="block",
                    this_current_screen_border=colors["sel_bg"],
                    this_screen_border=colors["norm_bg"],
                    other_current_screen_border=colors["sel_bg"],
                    other_screen_border=colors["norm_bg"],
                    disable_drag=True,
                    hide_unused=False,
                ),
                # Layout indicator [[]], [M], etc.
                widget.CurrentLayout(
                    foreground=colors["sel_fg"],
                    background=colors["sel_bg"],
                    padding=6,
                ),
                # Window title
                widget.WindowName(
                    foreground=colors["norm_fg"],
                    max_chars=50,
                    padding=6,
                ),
                widget.Spacer(),
                # Status indicators in simple textual dwm block format
                widget.CPU(
                    format="CPU {load_percent}%",
                    padding=6,
                ),
                widget.Memory(
                    format="MEM {MemUsed:.0f}{mm}",
                    padding=6,
                ),
                widget.Volume(
                    fmt="VOL {}",
                    padding=6,
                ),
                widget.Clock(
                    format="%Y-%m-%d %H:%M",
                    background=colors["sel_bg"],
                    foreground=colors["sel_fg"],
                    padding=8,
                ),
                widget.Systray(
                    icon_size=14,
                    padding=4,
                ),
            ],
            size=18,
            background=colors["norm_bg"],
            margin=[0, 0, 0, 0],
            border_width=[0, 0, 0, 0],
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

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    pass
