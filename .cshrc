# My prompt
set prompt='%{\033[1;32m%}%n%{\033[1;30m%}\@%{\033[0;34m%}%m%{\033[1;30m%} (%?) : %{\033[1;33m%}%B%c%B%{\033[1;30m%}\$%{\033[0m%} '

# History settings
set history=1000    
set savehist=2000   # command history saved after shell exits
set time=1          # show run-time stats of long-running processes

# Bind up/down keys to search history
bindkey -k down history-search-forward
bindkey -k up history-search-backward
bindkey '\e[1;5D' backward-word
bindkey '\e[1;5C' forward-word

alias ll ls -l
alias lf ls -F
alias lr ls -R
alias vi vi
alias ls 'ls -G --color=always'
alias ll 'ls -lahG --color=always'
alias l 'ls -laG --color=always'
alias mcd 'mkdir -p \!* && cd \!*'
#alias tree='tree -puhDC'
alias tree 'tree -C'
alias tl 'tree -d'
alias grep 'grep --color'
alias egrep 'egrep --color=auto'
alias fgrep 'fgrep --color=auto'
alias df 'df -h'
alias du 'du -h'
alias du- 'du -h --max-depth=0'
# Add an "alert" alias for long running commands.  Use like so: 'sleep 10; alert'
alias alert 'notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias neofetch  'neofetch --ascii ~/.config/neofetch/ascii/weeb'
alias nvi 'nxvi'

# Alias f: Find file, edit if selected
alias f '\
  set file = `sh -c "find . -type f ! -path '\''*.var*'\'' ! -path '\''*.rustup*'\'' 2>/dev/null | fzf-tmux --header-first --header '\''Edit File\n───────\n'\'' --layout=reverse -p"` ; \
  if ( "$file" != "" ) vi "$file" \
'

# Alias d: Find directory globally (~), cd if selected
alias d '\
  set dir = `sh -c "find ~ -type d ! -path '\''*.var*'\'' ! -path '\''*.rustup*'\'' 2>/dev/null | fzf-tmux --header-first --header '\''search directory'\'' --layout=reverse -p"` ; \
  if ( "$dir" != "" ) cd "$dir" \
'

# Alias dl: Find directory locally (.), cd if selected
alias dl '\
  set dir = `sh -c "find . -type d ! -path '\''*.var*'\'' ! -path '\''*.rustup*'\'' 2>/dev/null | fzf-tmux --header-first --header '\''search directory [local]'\'' --layout=reverse -p"` ; \
  if ( "$dir" != "" ) cd "$dir" \
'
