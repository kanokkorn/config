# handful of alias use with .bashrc
# required:
#   - tmux 
#   - fzf 
#   - vim 
#   - git 
#   - batcat 

# `ef` for `edit file`
alias ef='find . -type f 2>/dev/null | fzf --bind "enter:become(vim {1})" --preview "batcat -n --color=always {}" --height 40% --layout=reverse --border'

# `sd` for `switch directory`
alias sd='cd $(find * -type d 2>/dev/null | fzf --height 40% --layout=reverse --border)'

# `gsc` for `git search commit`
alias gsc='git show $(git log --oneline 2>/dev/null | fzf --height 40 --layout=reverse --border | head -n1 | cut -d " " -f1)'
