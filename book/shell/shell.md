# Shell

* Shell is a program which processes commands and returns output , like bash in Linux

  Distribution

> Terminal

* program that run a shell

> Error

* getcwd() failed: No such file or directory
  * execute a command from a path that doesn't exists (deleted by other terminal)

## Shortcut

```sh
ctrl + a / e       # Move to the beginning / end of the line
ctrl + r            # Search history
ctrl + u | k        # Delete to the beginning / end of the line
ctrl + w            # Delete a word
ctrl + l            # Clear screen
option + ← / →      # Navigate left / right

command + t         # Create new tab
command + n          # Create new window
ctrl + (shift) + tab    # Navigate tabs
command + (shift) + d    # Split terminal
defaults write com.apple.finder AppleShowAllFiles TRUE    # Show hidden folder on Mac
```

## .rc

```sh
/etc/skel/.bashrc   # reset rc files to original
#!/bin/bash -e      # set which shell to run
```

* Setup

```sh
# Mac
brew install ag         # recursively search text in folder
brew install htop       # advanced top
brew install vim        # text editor
brew install git && gh  # version control
brew install binutils   # readelf equivalent 'export PATH="/usr/local/opt/binutils/bin:$PATH"' >> ~/.zshrc
```

* bashrc

```sh
# Shell
case $- in
  *i*) ;;
    *) return;;
esac

parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "   # show branch in shell
export PS4='+(${BASH_SOURCE}:${LINENO}): ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'
alias ..='cd ..'
cdl() {
  cd"$@";
  ls -al;
}
alias fn="find . -name "
alias fr="find . -regex "
alias ipe='ipconfig getifaddr en0'
alias ipi='curl ipinfo.io/ip'
alias ll="ls -la"
mkcdir ()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}
alias mount='mount |column -t'
alias ports='netstat -tulanp'  # TCP / UDP
alias sshhosts="sed -n 's/^\s*Host\s+(.*)\s*/\1/ip' ~/.ssh/config"
alias speed='speedtest-cli --server 2406 --simple'
alias untar='tar -zxvf '
alias psm='ps aux | sort -nr -k 4 | head -3'
alias psm10='ps aux | sort -nr -k 4 | head -10'
alias psc='ps aux | sort -nr -k 3 | head -3'
alias psc10='ps aux | sort -nr -k 3 | head -10'
export VISUAL=vim
export EDITOR="$VISUAL"

# Bash
alias ag="ag --hidden -U"

# C
source ~/github/opencv/build/setup_vars.sh
export PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" # CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv4) LDFLAGS += $(shell pkg-config --libs --static opencv4)
export CMAKE_PREFIX_PATH=~/github/opencv/build    # PATH searched by CMake FIND_XXX()
export CPPFLAGS="-I/usr/local/opt/libffi/include"
export LDFLAGS="-L/usr/local/opt/libffi/lib"

# PYTHON
export FLASK_APP="server"

# MAC
defaults write -g ApplePressAndHoldEnabled -bool false # disable accentuate
alias ldd="otool -L"
alias xclip="pbcopy"
alias xargs="gxargs"

# Git Related
alias gacp="git add -A && git commit --amend --no-edit && git push --force"
alias gaA="git add -A"
alias gau="git add -u"
alias gauca="git add -u && git commit --amend"
alias gb="git branch -vv"
alias gca="git commit --amend"
alias gd="git diff"
alias gdc="git diff --cached"
alias gfa="git fetch --all"
alias gl="git log"
alias gml="git log --stat --color --decorate --all --oneline"
alias gog="git log --abbrev-commit --name-status --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"
alias gs="git status"
```

## Distribution

> Linux

* Kernel interacts with computer hardwares to allow software \| hardware to exchange information
* Tries to make the distribution more user-friendly with more convenient features
* Four categories based on original distribution - Arch, Debian, Red Hat, and Slackware

> WSL

compatibility layer for running Linux binary executables natively on Windows 10

> Red Hat

CentOS, Fedora, and Red Hat Enterprise Linux are derived

> BSD

Linux : MacOS

> Ubuntu

* Desktop based Linux distribution

> window

* Win+R shell:startup \(current user\) shell:common \(all user\)

```sh
systeminfo            # checks 32, 64 bitness
new-alias vi notepad  # use vi to replace notepad
```

> type

* like cat in linux

```text
C:\>echo hi > a.txt
C:\>echo bye > b.txt
C:\>type a.txt b.txt > c.txt
C:\>type c.txt
```