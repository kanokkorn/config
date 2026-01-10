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

" netrw
let g:netrw_altv=1
let g:netrw_liststyle=3
let g:netrw_banner=0
let g:netrw_keepdir=0
let g:netrw_winsize=20
let g:netrw_browse_split=3

" awkward keymap for term
" CTRL+x is more egonomic than CTRL+\ CTRL+n
tnoremap <C-x> <C-\><C-n>

" underline paste
tnoremap P pu<CR>
" ergonomic keymap
map <Space> <leader>
" paste underline
tnoremap P pu<CR>
" switch to textmode in terminal
tnoremap <C-x> <C-w>N
" open newtab
nnoremap <leader>t :tabnew 
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

" font for Neovim QT
" GuiFont {font_name}:h{size}

" autoload view
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview 

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
