" visual customise
" keep it minimal & match with vim config
syntax enable
set fillchars+=vert:│
hi StatusLine ctermbg=105 ctermfg=236
hi StatusLineNC ctermbg=240 ctermfg=236
hi VertSplit ctermfg=236
hi VertSplit cterm=NONE
hi Search ctermfg=141 ctermbg=238
hi Visual ctermfg=36 ctermbg=238

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
