# fzf alias like .bashrc but for windows 
# requires :
#   - nvim    (Neovim.Neovim)
#   - fdfind  (sharkdp.fd)
#   - fzf     (junegunn.fzf)
# all program can be install via winget

function searchDir {
  $directories = fd --type directory -H .
  $selectedDirectory = $directories | fzf --reverse --border --header-first --header 'Search directory'
  if ($selectedDirectory) {
    cd $selectedDirectory
  } else {
      Write-Host "No directory selected."
  }
}

function editFile {
  $directories = fd --type file -H .
  $selectedDirectory = $directories | fzf --reverse --border --header-first --header 'Edit target file'
  if ($selectedDirectory) {
    nvim $selectedDirectory
  } else {
      Write-Host "No file selected."
  }
}

Set-Alias sd searchDir
Set-Alias ef editFile
