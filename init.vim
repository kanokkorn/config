syntax on

" plug
call plug#begin('~')
Plug 'junegunn/vim-easy-align'
Plug 'iCyMind/NeoSolarized'
Plug 'joshdick/onedark.vim'
Plug 'tomasr/molokai'
Plug 'sainnhe/sonokai'
Plug 'iCyMind/NeoSolarized'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/nerdtree'
call plug#end()

" air-line
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif

" unicode symbols
let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

" airline symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''

" color and font
colo onedark
set guifont=Cascadia \Code:h12

hi StatusLine ctermbg=105 ctermfg=236
hi StatusLineNC ctermbg=240 ctermfg=236
hi VertSplit ctermfg=236
hi Search ctermfg=141 ctermbg=238

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
