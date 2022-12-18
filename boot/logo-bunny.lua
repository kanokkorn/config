-- boot logo for FreeBSD
-- from https://forums.FreeBSD.org/threads/customize-boot-loader-logo.72903/post-482703
-- Name this file logo-bunnyfacebw.lua
-- Make sure it has read permissions
-- Place in /boot/lua
-- In /boot/loader.conf, change or add the loader_logo option to read:
-- loader_logo="bunnyfacebw"

local drawer = require("drawer")

local bunnyface_bw = {
  [[     / \                ]],
  [[    / _ \               ]],
  [[   | / \ |              ]],
  [[   ||   || _______      ]],
  [[   ||   || |\     \     ]],
  [[   ||   || ||\     \    ]],
  [[   ||   || || \    |    ]],
  [[   ||   || ||  \__/     ]],
  [[   ||   || ||   ||      ]],
  [[    \\_/ \_/ \_//       ]],
  [[   /   _     _   \      ]],
  [[  /               \     ]],
  [[  |    O     O    |     ]],
  [[  |   \  ___  /   |     ]],
  [[ /     \ \_/ /     \    ]],
  [[/  -----  |  -----  \   ]],
  [[|     \__/|\__/     |   ]],
  [[\       |_|_|       /   ]],
  [[ \_____       _____/    ]],
  [[       \     /          ]],
  [[       |     |          ]]
}

drawer.addLogo("bunnyfacebw", {
    graphic = bunnyface_bw,
    shift = {x = 2, y = -3},
  })
