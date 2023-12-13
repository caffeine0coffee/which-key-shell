# which-key-shell
*shell shortcut launcher inspired by spacemacs*

`alias` に登録する程でもないことを [Spacemacs](https://www.spacemacs.org) みたいに呼び出そう！<br/>
Let's call things like [Spacemacs](https://www.spacemacs.org) that aren't worth registering in `alias`!

<img height="600px" src="https://user-images.githubusercontent.com/48763656/206117409-76a4ee13-9f20-4d26-a87c-3d36a343340b.gif" />

連続したキーストロークを階層構造で定義することができます。([config.json](https://github.com/caffeine0coffee/space-shell-shortcut/blob/main/config.json)を参照)<br/>
Sequential keystrokes can be defined in a hierarchical structure. (See [config.json](https://github.com/caffeine0coffee/space-shell-shortcut/blob/main/config.json))

# Setup (for zsh)

requirement: python3

## 1. clone this repo

```
git clone git@github.com:caffeine0coffee/space-shell-shortcut.git
```

## 2. setup `.zshrc`

```bash
# space-shell-shortcut
function space-shell-shortcut() {
    BUFFER=`zsh <path-to-run.sh> < $TTY`
    if [ $? -eq 0 ]; then
        CURSOR=$#BUFFER
        zle accept-line
    else
        zle reset-prompt
    fi
}
zle -N space-shell-shortcut

bindkey <your-favorite-key> space-shell-shortcut
# e.g. bindkey '^G' space-shell-shortcut
```

# Customize

edit your [config.json](https://github.com/caffeine0coffee/space-shell-shortcut/blob/main/config.json)
