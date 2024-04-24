export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
export PATH=$PATH:$HOME/go/bin

. "$HOME/.cargo/env"

autoload -U colors && colors
PS1="%{$fg[green]%}%n@%m%{$reset_color%}:%{$fg[cyan]%}%1~%{$reset_color%} %% "
PROMPT='%F{208}%n%f in %F{226}%~%f -> '

eval "$(fzf --zsh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

alias ll='ls -lah'
alias ef='find . -type f -maxdepth 4 ! -path "./Library*" | fzf --height 40% --layout=reverse --border | xargs -ro vi'

# `sd` for `switch directory`
alias sd='cd $(find ~ -type d -maxdepth 4 ! -path "./Library*" | fzf --height 40% --layout=reverse --border)'

# `gsc` for `git search commit`
alias gsc='git show $(git log --oneline 2>/dev/null | fzf --height 40 --layout=reverse --border | head -n1 | cut -d " " -f1)'

eval "$(/opt/homebrew/bin/brew shellenv)"
