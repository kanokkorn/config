# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;; esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
# PS1='${debian_chroot:+($debian_chroot)}\[\033[00;32m\]\u@\[\033[01;31m\]\h:\[\033[01;34m\]\w\[\033[00m\]\$ '
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[01;36m\]@\h:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}$

# some more ls aliases
alias ll='exa -lgb'
alias la='ls -A'
alias l='ls -CF'

alias neofetch='neofetch --ascii ~/.config/neofetch/ascii/weeb'
alias nvi='nxvi'


# `ef` for `edit file`
# alias ef='find . -type f 2>/dev/null | fzf --preview "batcat -n --color=always {}" --height 40% --layout=reverse --border | xargs -r -o vi'
# alias ef="find . -type f ! -path '*.var*' ! -path '*.rustup*' 2>/dev/null |fzf-tmux --header-first --header $'Edit File\n───────\n' --layout=reverse  -p | xargs -r -o vi"
# alias ef="find . -type f ! -path '*.var*' ! -path '*.rustup*' 2>/dev/null |fzf-tmux --header-first --header $'Edit File\n───────\n' --layout=reverse  -p | xargs -r -o vi"
# alias ef="fd --type file --hidden --no-ignore |fzf-tmux --header-first --header $'Edit File\n───────\n' --layout=reverse  -p | xargs -r -o vi"

# `sd` for `switch directory`
# alias sd='cd $(find * -type d 2>/dev/null | fzf --height 40% --layout=reverse --border)'
# alias sd='cd $(find ~ -type d ! -path "*.var*" ! -path "*.rustup*" 2>/dev/null | fzf-tmux --header-first --header "search directory" --layout=reverse -p)'

f() {
  file=$(find . -type f ! -path '*.var*' ! -path '*.rustup*' 2>/dev/null |fzf-tmux --header-first --header $'Edit File\n───────\n' --layout=reverse -p)
  if [ -z "$file" ]; then
    cd .
  else
    vi "$file"
  fi
}

d() {
  dir=$(find ~ -type d ! -path "*.var*" ! -path "*.rustup*" 2>/dev/null | fzf-tmux --header-first --header 'search directory' --layout=reverse -p)
  if [ -z "$dir" ]; then
    cd .
  else
    cd "$dir"
  fi
}

dl() {
  dir=$(find * -type d ! -path "*.var*" ! -path "*.rustup*" 2>/dev/null | fzf-tmux --header-first --header 'search directory [local]' --layout=reverse -p)
  if [ -z "$dir" ]; then
    cd .
  else
    cd "$dir"
  fi
}
# alias sd='cd $(fd --type directory --hidden . /home/mitsuha | fzf-tmux --header-first --header "search directory" --layout=reverse -p)'
# alias sd=''

# alias gsc='git show $(git log --oneline 2>/dev/null | head -n1 | cut -d " " -f1 | fzf --height 40 --layout=reverse --border)'
alias gsc='git show $(git log --oneline 2>/dev/null | fzf --height 40 --layout=reverse --border | head -n1 | cut -d " " -f1)'

# cat to batcat
alias cat='bsdcat'
alias fd='fdfind'
alias less='bat'

# screenshot & terminal clock
scrot '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/shots/'
alias peaclock='peaclock --config "~/.config/peaclock/config/binary"'

# file explorer
BLK="0B" CHR="0B" DIR="04" EXE="06" REG="00" HARDLINK="06" SYMLINK="06" MISSING="00" ORPHAN="09" FIFO="06" SOCK="0B" OTHER="06"
export NNN_FCOLORS="$BLK$CHR$DIR$EXE$REG$HARDLINK$SYMLINK$MISSING$ORPHAN$FIFO$SOCK$OTHER"
export NNN_TMPFILE=/tmp/.lastd 
alias nnn='nnn -d -e -H -r'

# QR-code generator
alias qr='qrencode -t UTF8'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

export PATH="$PATH:$HOME/.spicetify"
. "$HOME/.cargo/env"


# nim lang executable
export PATH=/home/mitsuha/.nimble/bin:$PATH

# deno
export DENO_INSTALL="/home/mitsuha/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH=$BUN_INSTALL/bin:$PATH
export PATH=$PATH:/usr/local/go/bin

# ollama
export OLLAMA_MODELS="/media/mitsuha/wdc-ext/llm_model/"

# export FZF_DEFAULT_OPTS=$FZF_DEFAULT_OPTS'
# --color=fg:#d0d0d0,fg+:#d0d0d0,bg:#121212,bg+:#262626
# --color=hl:#5faf5f,hl+:#00ff5f,info:#afaf87,marker:#87ff00
# --color=prompt:#00ff5f,spinner:#d7d7ff,pointer:#5f00ff,header:#87afaf
# --color=border:#262626,query:#d9d9d9'

# export FZF_DEFAULT_OPTS=$FZF_DEFAULT_OPTS'
# --color=fg:#d0d0d0,fg+:#d0d0d0,bg:#121212,bg+:#262626
# --color=hl:#836FFF,hl+:#15F5BA,info:#afaf87,marker:#211951
# --color=prompt:#d7005f,spinner:#af5fff,pointer:#211951,header:#87afaf
# --color=border:#262626,query:#d9d9d9'

# export FZF_DEFAULT_OPTS=" \
#          --color=bg+:#313244,bg:#1e1e2e,spinner:#f5e0dc,hl:#f38ba8 \
#          --color=fg:#cdd6f4,header:#f38ba8,info:#cba6f7,pointer:#f5e0dc \
#          --color=marker:#f5e0dc,fg+:#cdd6f4,prompt:#cba6f7,hl+:#f38ba8"
. "/home/mitsuha/.deno/env"
