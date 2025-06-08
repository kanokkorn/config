. "$HOME/.cargo/env"

export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
export PATH=$PATH:$HOME/go/bin
export PATH=$PATH:$HOME/.bun/bin

autoload -U colors && colors
PS1="%{$fg[green]%}%n@%m%{$reset_color%}:%{$fg[cyan]%}%1~%{$reset_color%} %% "
PROMPT='%F{208}%n%f in %F{226}%~%f -> '

eval "$(fzf --zsh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

# more alias
alias ll='ls -lah'
alias l='ls'
alias lua='luajit'
# alias nv='nvim'

# `ef` for `edit file`
alias f='find . -type f -maxdepth 4 ! -path "./Library*" | fzf-tmux -p --layout=reverse | xargs -ro vi'

# `sd` for `switch directory`
alias d='cd $(find ~ -type d -maxdepth 4 ! -path "./Library*" | fzf-tmux -p --layout=reverse )'

# `gsc` for `git search commit`
alias gsc='git show $(git log --oneline 2>/dev/null | fzf --height 40 --layout=reverse | head -n1 | cut -d " " -f1)'

# find manual topics from keywords
alias mans='find $(man -k | fzf --height 40% --layout=reverse --border)'

eval "$(/opt/homebrew/bin/brew shellenv)"

export FZF_DEFAULT_OPTS=$FZF_DEFAULT_OPTS'
  --color=fg:#d0d0d0,fg+:#d0d0d0,bg:#121212,bg+:#262626
  --color=hl:#5faf5f,hl+:#00ff5f,info:#afaf87,marker:#87ff00
  --color=prompt:#00ff5f,spinner:#d7d7ff,pointer:#5f00ff,header:#87afaf
  --color=border:#262626,label:#aeaeae,query:#d9d9d9'

# bun completions
[ -s "/Users/kano/.bun/_bun" ] && source "/Users/kano/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"


# If you need to have mysql@8.0 first in your PATH, run:
echo 'export PATH="/opt/homebrew/opt/mysql@8.0/bin:$PATH"' >> ~/.zshrc

# For compilers to find mysql@8.0 you may need to set:
export LDFLAGS="-L/opt/homebrew/opt/mysql@8.0/lib"
export CPPFLAGS="-I/opt/homebrew/opt/mysql@8.0/include"
export PATH="/opt/homebrew/opt/mysql@8.0/bin:$PATH"
