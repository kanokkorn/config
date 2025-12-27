" visual customise
colo habamax
syntax enable
set fillchars+=vert:│
hi StatusLine   ctermbg=233   ctermfg=48
hi StatusLineNC ctermbg=233   ctermfg=240
hi VertSplit    ctermfg=236   ctermbg=NONE
hi Search       ctermfg=48    ctermbg=233
hi Visual       ctermfg=48    ctermbg=233
hi TabLineFill  ctermfg=236   ctermbg=233 
hi TabLineSel   ctermfg=233   ctermbg=48
hi TabLine      ctermfg=15    ctermbg=236

" netrw
let g:netrw_altv=1
let g:netrw_liststyle=3
let g:netrw_banner=0
let g:netrw_keepdir=0
let g:netrw_winsize=20
let g:netrw_browse_split = 3

" ergonomic keymap
map <Space> <leader>
" paste underline
tnoremap P pu<CR>
" switch to textmode in terminal
tnoremap <C-x> <C-w>N
" file explorer
nnoremap <leader>f :Lexplore %:p:h<CR>
" run command & paste stdout
nnoremap <leader>c :r!
" substitution
nnoremap <leader>r :%s/
" force close buffer
nnoremap <leader>x :bd! <CR>
" no highlight
nnoremap <leader>nh :noh <CR>
" check spell on
nnoremap <leader>g :set spell <CR>
" check spell off
nnoremap <leader>gn :set nospell <CR>
" horizontal terminal
nnoremap <leader>h :below term <CR>
" vertical terminal
nnoremap <leader>v :rightb vert term <CR>

" find old
" nnoremap <leader>fo :browse oldfiles<CR>
set path=**
set wildoptions=pum

" keymap
vmap y ygv<Esc>

" autoload view
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview 


" set number
" set relativenumber
set splitright
set nocompatible
set ttymouse=xterm
set linebreak
set expandtab
set showmatch
set smartindent
set smarttab
set hlsearch
set incsearch
set ignorecase
set autoindent
set cindent
set expandtab
set tabstop=2
set scrolloff=8
set shiftwidth=2
set ruler
set undolevels=1000
set backspace=indent,eol,start
