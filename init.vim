call plug#begin('~')

Plug 'junegunn/vim-easy-align'
Plug 'joshdick/onedark.vim'
Plug 'iCyMind/NeoSolarized'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/nerdtree'

call plug#end()

colo onedark
set guifont=Cascadia_Code\ Code:h12

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
