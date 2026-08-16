-- the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices

-- For example, changing the color scheme:
-- config.color_scheme = 'Catppuccin Latte'
config.color_scheme = 'Catppuccin Mocha'
-- config.color_scheme = 'rose-pine'
-- config.color_scheme = 'rose-pine-dawn'

config.enable_tab_bar = false
config.font_size = 12.0
config.default_cursor_style = "SteadyBlock"

-- and finally, return the configuration to wezterm
return config
