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
bindkey "^R" i-search-back

alias ll ls -l
alias lf ls -F
alias lr ls -R
alias vi vi
alias sc 'sc-im'
alias ls 'ls -G --color=always'
alias ll 'ls -lahG --color=always'
alias l 'ls -laG --color=always'
alias mcd 'mkdir -p \!* && cd \!*'
#alias tree='tree -puhDC'
alias cd 'cd \!* && ls'

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
# cat to batcat
alias cal 'ncal -C'
alias cat 'bsdcat'
alias fd  'fdfind'
alias less  'bat'
alias qr  'qrencode -t UTF8'
alias peaclock  'peaclock --config "~/.config/peaclock/config/binary"'

# Alias f: Find file, edit if selected
alias f '\
        set file = `sh -c "find . -type f ! -path '\''*.var*'\'' ! -path '\''*.rustup*'\'' ! -path '\''*.cache*'\'' 2>/dev/null | fzf-tmux --header-first --header '\''edit file'\'' --layout=reverse -p"` ; \
        if ( "$file" != "" ) vi "$file" \
        '

# Alias d: Find directory globally (~), cd if selected
alias d '\
        set dir = `sh -c "find ~ -type d ! -path '\''*.c*'\'' ! -path '\''*.z*'\'' ! -path '\''*pkg*'\'' ! -path '\''*.l*'\'' ! -path '\''*.t*'\'' ! -path '\''*gradle*'\'' !  -path '\''*snap*'\'' ! -path '\''*android*'\'' ! -path '\''*.r*'\'' ! -path '\''*.n*'\''  2>/dev/null | fzf-tmux --header-first --header '\''search directory'\'' --layout=reverse -p"` ; \
        if ( "$dir" != "" ) cd "$dir" \
        '
# optimise version of find directory script
# set excluded_search_dirs = ("android" ".rustup" ".theme" ".cache" "snap");
# alias d '\
#         set find_cmd = "find ~ -type d"; \
#         foreach excl ($excluded_search_dirs) \
#                 set find_cmd = "$find_cmd ! -path '\''*$excl*'\''"; \
#         end; \
#         set find_cmd = "$find_cmd 2>/dev/null | fzf-tmux --header-first --header '\''Search Directory'\'' --layout=reverse -p"; \
#         set dir = `sh -c "$find_cmd"`; \
#         if ( "$dir" != "" ) then; \
#                 cd "$dir"; \
#         endif \
# '

# Alias dl: Find directory locally (.), cd if selected
alias dl '\
  set dir = `sh -c "find . -type d ! -path '\''*.var*'\'' ! -path '\''*.rustup*'\'' ! -path '\''*.cache*'\'' 2>/dev/null | fzf-tmux --header-first --header '\''search directory [local]'\'' --layout=reverse -p"` ; \
  if ( "$dir" != "" ) cd "$dir" \
'
