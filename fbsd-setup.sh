!#/bin/sh


# create dir for wm dotfiles
mkdir ~/.config
mkdir ~/.config/bspwm && mkdir ~/.config/sxhkd

# copy to target dir
cp .Xresources .vimrc .tmux.conf ~
cp ~/.config/bspwm/bspwmrc ~/.config/bspwm/
cp ~/.config/bspwm/sxhkd ~/.config/sxhkd/
