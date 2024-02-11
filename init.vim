" visual customise
" keep it minimal & match with vim config
syntax enable
set fillchars+=vert:│
hi StatusLine   ctermbg=233   ctermfg=48
hi StatusLineNC ctermbg=233   ctermfg=240
hi VertSplit    ctermfg=236   ctermbg=NONE
" hi Search       ctermfg=48    ctermbg=233
" hi Visual       ctermfg=48    ctermbg=233
hi TabLineFill  ctermfg=236   ctermbg=233
hi TabLineSel   ctermfg=233   ctermbg=48
hi TabLine      ctermfg=15    ctermbg=236

" awkward keymap for term
" CTRL+x is more egonomic than CTRL+\ CTRL+n
tnoremap <C-x> <C-\><C-n>

" underline paste
tnoremap P pu<CR>

" font for Neovim QT
" GuiFont {font_name}:h{size}

set number
set linebreak
set showbreak=+++
set textwidth=100
set showmatch
set visualbell
set hlsearch
set smartcase
set ignorecase
set incsearch
set autoindent
set cindent
set expandtab
set shiftwidth=2
set smartindent
set smarttab
set softtabstop=2
set ruler
set undolevels=1000
set backspace=indent,eol,start
