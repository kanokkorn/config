export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
export PATH=$PATH:$HOME/go/bin
export PATH=$PATH:$HOME/.bun/bin

autoload -U colors && colors
PS1="%{$fg[green]%}%n@%m%{$reset_color%}:%{$fg[cyan]%}%1~%{$reset_color%} %% "
# PROMPT='%F{208}%n%f in %F{226}%~%f -> '
# PROMPT='%{\033[1;32m%}%n%{\033[1;30m%}\@%{\033[0;34m%}%m%{\033[1;30m%} (%?) : %{\033[1;33m%}%B%c%B%{\033[1;30m%}\$%{\033[0m%} '
PROMPT="%{$fg_bold[green]%}%n%{$fg_bold[black]%}@%T%{$fg[blue]%}%m%{$fg_bold[black]%} (%?) : %{$fg_bold[yellow]%}%B%~%b%{$fg_bold[black]%}%# %{$reset_color%}"

eval "$(fzf --zsh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

# more alias
alias ll='ls -lha'
alias l='ls'
alias lua='luajit'
alias sc='sc-im'
alias grep='grep --color=auto'
# alias nv='nvim'

# `ef` for `edit file`
alias f='find . -type f -maxdepth 4 ! -path "./Library*" 2>/dev/null | fzf-tmux -p --layout=reverse | xargs -ro vi'

# `sd` for `switch directory`
alias d='cd $(find ~ -type d -maxdepth 4 ! -path "./Library*" 2>/dev/null | fzf-tmux -p --layout=reverse )'

# `gsc` for `git search commit`
alias gsc='git show $(git log --oneline 2>/dev/null | fzf --height 40 --layout=reverse | head -n1 | cut -d " " -f1)'

# find manual topics from keywords
alias mans="man -k . 2>/dev/null | fzf --height 40% --layout=reverse --border | sed -E 's/^([^ ]+)\(([^)]+)\).*/\2 \1/' | xargs -r man"

eval "$(/opt/homebrew/bin/brew shellenv)"

# custom fzf theme
# export FZF_DEFAULT_OPTS=$FZF_DEFAULT_OPTS'
#   --color=fg:#d0d0d0,fg+:#d0d0d0,bg:#121212,bg+:#262626
#   --color=hl:#5faf5f,hl+:#00ff5f,info:#afaf87,marker:#87ff00
#   --color=prompt:#00ff5f,spinner:#d7d7ff,pointer:#5f00ff,header:#87afaf
#   --color=border:#262626,label:#aeaeae,query:#d9d9d9'

# fzf catpucchi theme
export FZF_DEFAULT_OPTS=" \
--color=bg+:#313244,bg:#1E1E2E,spinner:#F5E0DC,hl:#F38BA8 \
--color=fg:#CDD6F4,header:#F38BA8,info:#CBA6F7,pointer:#F5E0DC \
--color=marker:#B4BEFE,fg+:#CDD6F4,prompt:#CBA6F7,hl+:#F38BA8 \
--color=selected-bg:#45475A \
--color=border:#6C7086,label:#CDD6F4"

# bun completions
[ -s "/Users/kano/.bun/_bun" ] && source "/Users/kano/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"

# if [ -r ~/.zshrc ]; then echo -e '\nexport GPG_TTY=$(tty)' >> ~/.zshrc; \
#   else echo -e '\nexport GPG_TTY=$(tty)' >> ~/.zprofile; fi
# For compilers to find mysql@8.0 you may need to set:
export LDFLAGS="-L/opt/homebrew/opt/mysql@8.0/lib"
export CPPFLAGS="-I/opt/homebrew/opt/mysql@8.0/include"
export PATH="/opt/homebrew/opt/mysql@8.0/bin:$PATH"

export GPG_TTY=$(tty)
export COLORTERM=truecolor

. "$HOME/.cargo/env"

# `uv run` autocomplete fix
eval "$(uv generate-shell-completion zsh)"
_uv_run_mod() {
    if [[ "$words[2]" == "run" && "$words[CURRENT]" != -* ]]; then
        _arguments '*:filename:_files'
    else
        _uv "$@"
    fi
}
compdef _uv_run_mod uv

# f() {
#   find . -type f ! -path '*/.var/*' ! -path '*/.rustup/*' 2>/dev/null | fzf-tmux --header-first --header $'Edit File\n───────\n' --layout=reverse --bind 'enter:become(vi {})'
# }
# 
# d() {
#   find ~ -type d ! -path '*/.var/*' ! -path '*/.rustup/*' 2>/dev/null | fzf-tmux --header-first --header 'search directory' --layout=reverse --bind 'enter:become(cd {})'
# }
# 
# dl() {
#   find . -maxdepth 1 -type d ! -path '*/.var/*' ! -path '*/.rustup/*' 2>/dev/null | fzf-tmux --header-first --header 'search directory [local]' --layout=reverse --bind 'enter:become(cd {})'
# }

alias ddg="w3m -cookie -t 2 ddg.gg/lite"
alias www="w3m -cookie -t 2 "
alias less='bat'

alias spotify="killall Spotify 2>/dev/null; open -a /Applications/Spotify.app --args --disable-gpu --disable-software-rasterizer --disable-background-timer-throttling"

. "$HOME/.local/bin/env"
