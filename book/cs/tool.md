# Tool

## Git

* uses sha-1 to compare hash

> Convention

* Uses present tense for commit message

> Terms

* branch
  * simply a lightweight movable pointer to one of these commits
  * ^(n) : previous branch (nth parent)
  * ~n : n previous branch

* conflict
  * Option 1 ("Accept Incoming changes") would ignore completely what you had, and keep what you merge.
  * Option 2 ("Accept current changes") would ignore completely what you merge, and keep what you had.

* main (master before 2020.10)
  * default name for the first branch in convention, this contains the local development

* stage
  * a cache of files that you want to commit

* HEAD
  * pointer to the current branch

* origin
  * alias on your system for a particular remote repository

* workspace
  * where actual files are

* index (staging area)
  * where commits are prepared

* Merge
  * independent lines of development created by git branch and integrate them into a single branch

* fast-forwarding
  * try to merge C1 with a C2 that can be reached by following commit history, just move pointer forward

* squash
  * technique that helps you to take a series of commits and condense it to a few commits

* Repository
  * container that tracks the changes to your project files

* Bare repository
  * Repository without workspace
  * Can be used in a shared folder

* Issue
  * "fix \#33" commit messages closes issue

> Files

* .git

```sh
cat .git/HEAD        # see head
rm -rf .git          # Delete git repository

# Accidentally removed .git
git init
git remote add origin <remote_address>.git
git pull
got reset --hard origin/main
```

* .gitignore

{% tabs %}
{% tab title='.gitignore' %}

```sh
*                    # Ignore everything
!*.py                # But not these files...

# For home file
*

!.ssh/**
!*.vimrc
!*.vim
!*.bashrc
!.gitignore
```

{% endtab %}
{% endtabs %}

* .gitconfig

{% tabs %}
{% tab title='.gitconfig' %}

```sh
[user]
  name = Gyuseung Hwang
  email = sean@remote.host
[credential]
  helper = cache --timeout=360000        # timeout for password

[alias]
  s = status -s
  co = checkout
  ci = commit
  br = branch
  l = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%C(bold blue)<%an>%Creset' --abbrev-commit
  backup = "!git branch backup-`git b0`"
  cleanbranch = "!git branch -d $(git branch --merged | grep -v '^\\*\\|\\<master$')"
```

{% endtab %}
{% endtabs %}

* .gitcredentials

{% tabs %}
{% tab title='.gitcredentials' %}

```sh
Username: sean
Password: ss
```

{% endtab %}
{% endtabs %}

* .gitmodules
  * config file that stores mapping between project’s URL and local subdir

{% tabs %}
{% tab title='.gitmodules' %}

```sh
[submodule "DbConnector"]
	path = DbConnector
	url = https://github.com/chaconinc/DbConnector
```

{% endtab %}
{% endtabs %}

* .gitmessage
  * default commit message

```sh
Fix Issue #{number}: {description}
R+: {reviewer}
```

> Hooks

```sh
.git/hooks directory
/usr/share/git-core/templates                         # Linux Template
C:\Program Files\Git\mingw64\share\git-core\templates # Window template
```

* prehook
  * static code checking (linting, codestyle)
  * exit non 0 doesn't get run
  * --no-verify         # make executable
* posthook only for notifying

```sh
chmod +x pre-commit
```

{% tabs %}

{% tab title='install.sh' %}

```sh
#!/bin/bash
# https://gist.github.com/clbarnes/3b521f81b0f30f2db4df390dcd12ac8d

# cd [path-of-the-script]
# . install.sh
#
# Folders usecase
# /.git
# /.git/hooks
# /hooks/install.sh <- this script
# /hooks <- path of your hooks

set -e

# list of hooks the script will look for
HOOK_NAMES="applypatch-msg pre-applypatch post-applypatch pre-commit prepare-commit-msg commit-msg post-commit pre-rebase post-checkout post-merge pre-receive update post-receive post-update pre-auto-gc"
PROJECT_ROOT_DIR=`git rev-parse --show-toplevel`

TGT_DIR=$PROJECT_ROOT_DIR/.git/hooks # absolute folder path of directory into which hooks should be installed
SRC_DIR=$PROJECT_ROOT_DIR/hooks      # absolute folder path of the custom hooks to deploy / current script
LNS_RELATIVE_PATH=../../hooks        # relative folder path from the target dir to the source dir

echo "Install project git hooks"

for hook in $HOOK_NAMES; do
  if [ -f $SRC_DIR/$hook ]; then     # if we have a custom hook to set
    echo "> Hook $hook"
    if [ ! -x $SRC_DIR/$hook ]; then
      echo " > Not executable, skipping"
      continue
    fi
    # If hook exists, executable, not a symlink
    if [ ! -h $TGT_DIR/$hook -a -x $TGT_DIR/$hook ]; then
      echo " > Old git hook $hook disabled"
      mv $TGT_DIR/$hook $TGT_DIR/$hook.old      # append .old to disable it
    fi

    echo " > Enable project git hook"           # create the symlink, overwriting the file if it exists
    ln -s -f $LNS_RELATIVE_PATH/$hook $TGT_DIR/$hook
  fi
done
```

{% endtab %}
{% tab title='email_check.sh' %}

```sh
if ["$useremail" != "seanhwang@github.com" ]; then
  cat <<\EOF
ERROR: user.email not set to "seanhwangg@github.com"
EOF
  exit 1
fi
```

{% endtab %}
{% tab title='git-commit-message' %}

```sh
#!/bin/bash
################################################################################
# Store this file as .git/hooks/commit-msg in your repository in order to
# enforce checking for proper commit message format before actual commits. You
# may need to make the script executable by 'chmod +x .git/hooks/commit-msg'.
################################################################################
filename="$1"
copy=$(tempfile -p gitco)
cat $filename >> $copy
lineno=0

error() {
  echo  "CHECKIN STOPPED DUE TO INAPPROPRIATE LOG MESSAGE FORMATTING!"
  echo "$1!"
  echo ""
  echo "Original checkin message has been stored in '_gitmsg.saved.txt'"
  mv $copy '_gitmsg.saved.txt'
  exit 1
}

while read -r line
do
  # Ignore comment lines (don't count line number either)
  [[ "$line" =~ ^#.* ]] && continue

  let lineno+=1
  length=${#line}

  # Subject line tests
  if [[ $lineno -eq 1 ]]; then
  [[ $length -gt 60 ]] && error "Limit the subject line to 60 characters"
  [[ ! "$line" =~ ^[A-Z].*$ ]] && error "Capitalise the subject line"
  [[ "$line" == *. ]] && error "Do not end the subject line with a period"
  fi

  # Rules related to the commit message body
  [[ $lineno -eq 2 ]] && [[ -n $line ]] && error "Separate subject from body with a blank line"
  [[ $lineno -gt 1 ]] && [[ $length -gt 72 ]] && error "Wrap the body at 72 characters"
done < "$filename"
rm -f $copy
exit 0
```

{% endtab %}
{% endtabs %}

### GIT CLI

![alt](images/20210206_115537.png)

* git

```sh
-V / --version                            # Print git version
--no-pager                                # Print unicode
svn export <github_url>|trunk|codes       # Download some files from github
```

> Error

* error: cannot lock ref 'refs/remotes/origin/working/sample': 'refs/remotes/origin/working' exists; cannot create 'refs/remotes/origin/working/sample'
  From [https://github.com/sample/repo](https://github.com/sample/repo)
  ! \[new branch\] working/hojae -&gt; origin/working/hojae \(unable to update local ref\)

```sh
sean@ip-172-31-61-87:~/EnkorBackend$ git update-ref -d refs/remotes/origin/working
git update-ref -d refs/remotes/origin/development
```

* error: external filter 'git-lfs filter-process' failed
  * lfs install --skip-smudge

* modified content, untracked content
  * git rm -rf --cached

> Config

* init
  * initialize git repository, create .git file

* config
  * --list : Print current configuration
  * --global --edit : Configure user name, email
  * core.editor "nano" : change default editor to vim
  * --bool core.bare true : Create bare repository
  * credential.helper store : save id / pw in .gitcredentials
  * --global diff.submodule log : show changes in submodule
  * --global commit.template ~/.gitmessage : set git commit message
  * --global credential.helper 'cache --timeout=2628000' : timeout password for month

> submodule

* add
  * URL
  * path `https://github.com/pybind/pybind11`

* deinit
  * -f path/to/submodule Remove the submodule entry from .git/config

* init
  * initialize your local configuration file

* foreach
  * git push origin master : push each submodule

* update
  * fetch all data from that project and check out appropriate commit
  * --init
  * --remote : go into your submodules and fetch and update

* lfs (large file storage)
  * do not use for faster cloning and fetching
  * --skip-smudge : ignore lfs when cloning
  * track *.bin : Track all binary files
  * install : setup lfs
  * env : show env
  * clone : Does not prompt for every large objects

> Inspect

* show
  * Show current and see what has been changed
  * --shortstat : only show stat

* status
  * Show changes between commits, commit and working tree, etc

```sh
[<options>] [<commit>] [--] [<path>…​]
[<options>] --cached [<commit>] [--] [<path>…​]
[<options>] <commit> <commit> [--] [<path>…​]
[<options>] <blob> <blob>
[<options>] --no-index [--] <path> <path>
<>                  # changes between working directory and index
HEAD                # all changes between working directory and HEAD
--cached            # changes between index and HEAD | see added files
--name-only         # name only
--porcelain         # output in an easy-to-parse format for scripts
--staged            # show changed between working directory and staged
--submodule         # show lines in submodules
```

* rev-parse
  * --short HEAD : show current commit
  * --abbrev-ref HEAD : show current branch

* blame
  * show file history

* log
  * master : local commit history
  * master.. : branch commit history
  * origin : server commit history
  * -n : limit search to n
  * --reflog : show all commits
  * --oneline : show abbreviated version
  * --graph : In graph form
  * --author="sean" : limit author
  * --grep = "init" : search for message
  * -p `file` : show changes over time for a `file`
  * --since/until=2020-01-01 : from time
  * -1 --stat -- `file` : Generate a diffstat (show file | 2 ++)
  * --graph --decorate --pretty=oneline --abbrev-commit --all : git lola

* reflog
  * View all ref updates (checkout, reset, commit, merge)

* revlist
  * Lists commit objects in reverse chronological order

* revparse
  * --short HEAD : show first 7 strings

* ls-files
  * show all files
  * --stage ls-tree -r -t -l --full-name HEAD | sort -n -k 4 | tail -n 10 : show largest files

* ls-tree
  * --name-only -r HEAD : List all files on the branch

* diff
  * -U n : allows you to customize the number of lines to show around a change
  * --stat : modified_file.txt    | 100 +-
  * --name-status : A / M / D  new_file.txt
  * HEAD:path/to/foo bar : diff over two commits
  * --name-only --diff-filter=U : show all unmerged files/

![alt](images/20210215_235720.png)

* diff-index
  * diff against the index or working tree / same as diff HEAD

{% tabs %}
{% tab title='precommit.sh' %}

```sh
if git rev-parse --verify HEAD >/dev/null 2>&1
then
  against=HEAD
else
  # Initial commit: diff against an empty tree object
  against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
  # Note that the use of brackets around a tr range is ok here, (it's
  # even required, for portability to Solaris 10's /usr/bin/tr), since
  # the square bracket bytes happen to fall in the designated range.
  test $(git diff --cached --name-only --diff-filter=A -z $against |
    LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
  cat <<\EOF
Error: Attempt to add a non-ASCII file name.
This can cause problems if you want to work with people on other platforms.
To be portable it is advisable to rename the file.
If you know what you are doing you can disable this check using:
  git config hooks.allownonascii true
EOF
  exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
```

{% endtab %}
{% endtabs %}

> Operation

* mv
  * <> src dest : move src to dest
  * -t dest src1 scr2 : move multiple item at once
  * -n : Do not overwrite an existing file

* rm
  * <> fn : rm fn and add to stage area
  * --cached : only remove from the index
  * rm -r --cached . : remove everything from index

* clean
  * Remove untracked files from the working tree
  * -n : see what will be removed
  * -d : recurse directory
  * -f : force

* format-patch
  * Prepare patches for e-mail submission

* apply
  * Apply a patch to files and/or to the index

* stash
  * pop ( -- filename) : reapply all conflict (only filename)
  * show (-p) : To show files changed in the last stash (content of the stashed files)
  * show -p stash@{1} : Show specific stash
  * clear : clear stashed files
  * list : see lists of stashed files
  * git checkout stash -- . : overwrite current file
  * git checkout stash@{0} -- fn : stash pop certain files

![stash](images/20210220_021545.png)

* remote
  * <> : Find current repository
  * -r : List remote branches
  * -v : List all currently configured remotes
  * add `name` `url` : Adds a remote `name` for repository at `url` / add origin for new
  * rm origin : remove existing origin
  * get-url :
  * set-url name new_url : Changes URL remote points to

* filter-branch
  * --tree-filter : delete accidentally added file

* log
  * logs last
  * --all : search by commit message
  * --pretty=oneline : line only

* show
  * all : show all lfs files

* ls-files
  * Show all

> Forward

* add [filename]
  * add files to staging area
  * -A : Add, delete updated codes (git add . + git add -u)
  * -a : Adds only files that changed since the last commit before committing
  * -p : add some parts of files
  * -u : Update or remove previously tracked files from the entire working tree

* commit
  * move files in staging area to local repository
  * -a : automatically stage files that have been modified and deleted (add -u)
  * -m msg : given msg as the commit message
  * --signoff : certifies who is the author of the commit
  * --amend -m "new" : change previous commit message
  * git reset --soft HEAD@{1} && git commit -C HEAD@{1} : undo git commit --amend
  * close, closes, closed, fix, fixes, fixed, resolve, resolves, resolved : with following message close issue

![alt](images/20210206_115808.png)

* push
  * [repo] [ref] : first push
  * -u / --set-upstream : every successfully pushed, add upstream
  * remote local_br(:remote_br) : (omit one if identical)
  * origin branch : push only one specific branch
  * origin --delete master : delete branch
  * -f origin HEAD:master : push detached head
  * -f origin commit:branch : undo push

![alt](images/20210218_015049.png)

> Backward

![alt](images/20210218_015026.png)

* Clone
  * --bare : clone bare repository
  * folder : get a local copy of an existing repository (default cwd) (. for current directory)
  * --depth 1 : shallow clone
  * -b / --branch : clone branch
  * -j n : number of submodules fetched at the same time.
  * --recurse-submodules : initialize, update each submodule in repository
  * git://host.xz[:port]/path/to/repo.git/ : does no authentication
  * ssh://[user@]host.xz[:port]/path/to/repo.git/
  * http[s]://host.xz[:port]/path/to/repo.git/
  * native transport (i.e. git:// URL) and should be used with caution on unsecured networks.

* Fetch
  * downloads commits that remote has but missing from local repository and updates remote branches point
  * does not change anything about your local state
  * Before Fetch (left : Local, right : Remote with new bugFix)
  * --unshallow : fetch all older commits from shallow clone
  * --all && git reset --hard origin/master : Download from remote and discard all

![Before fetch](images/20210206_120406.png)
![After Fetch](images/20210206_120442.png)

* pull
  * Before & After pull
  * [repo] [ref] : fetch + merge
  * --allow-unrelated-histories : merge different git repository
  * origin master : update local copy with commits from remote repo
  * -C git-working-directory pull `git_remote` : pull in other directory

![alt](images/20210206_120545.png)
![alt](images/20210206_120616.png)

* Checkout
  * will also update HEAD to set the specified branch as the current branch
  * branch : switch to branch
  * commit : update HEAD
  * filename : Discard changes in the working directory (enclose with ' to use wildcard '*.ext')
  * origin/master : check out remote
  * -b `branch` : create a `branch`, and use it (git branch -f branch [<start_point>] + git checkout branch)
  * -f branch commit : Reset `branch` to commit, even if branch exists

![alt](images/20210206_115843.png)

* Reset
  * file : Unstage a file
  * tree path : Unstage all changes in one file
  * HEAD filename : Discard all changes from previous commit
  * --hard branch : throws away all uncommitted changes

![alt](images/20210206_115937.png)

* Revert
  * forward-moving undo
  * branch : Creates new commit of existing commit
  * commit : Undo commits in a public branch

![alt](images/20210206_120017.png)

### Branch

![alt](images/20210218_015121.png)

* the starred branch is your current branch

* branch
  * <> : show branch
  * `branch` : create name `branch`
  * -d / -D name : Delete merged branch / not merged in upstream branch
  * -f b1 b2 : Move b1 to b2
  * -m A B : Rename branch (current to A (A to B)
  * -u o/master (branch) : set branch to track o/master (current branch)
  * -vv : Show all the local branches of your rep
  * -mc branch2 : branch2 will be created
  * --merged | egrep -v "(^\*|master|main|dev)" | xargs git branch -d : delete merged branches

* cherry-pick
  * C1 C2 : copy C1, C2, … to our current HEAD
  * C1...C2 : copy commit from C1 to C2 to our current HEAD

* Merge
  * On feature branch
  * Left : git merge master
  * Right : git rebase master
  * branch_name : merge with another branch
  * --unset-upstream main : unset upstream branch
  * -s ours branch1 branch2 branchN : merge result is always that of the current branch HEAD

![alt](images/20210206_120704.png)

* mergetool
  * <> : run left

* git config merge.conflictstyle diff3

```sh
<<<<<<<
This is the branch that I have currently checked out (i.e. HEAD).
|||||||
The common ancestor version.
=======
Changes made on the branch that is being merged in. This is often a feature branch
.>>>>>>>
```

* Rebase
  * integrating changes from one branch onto another
  * pastes feature branch to the end of the master branch
  * a (b) : a → b (current if omitted)
  * -i --root : Interactive rebase / from root
  * fetch && origin/master : Merge remote master to the local branc

> Github cli

* gh gist create filename : push to gist
  * ?file=afile : only one file in gist

## Vim

* -o * : Open with horizontal split
* -o * : Open with vertical split
* -p * : Open with each tab
* -r .swp : recover swp file
* --version : Show version

> Files

* .vimrc
  * Located in home\(~\) directory, get run every time when open vim

{% tabs %}
{% tab title='.vimrc' %}

```text
:so ~/.vimrc            # apply vimrc

set num                 # show line number
syntax on               # coloring
set tabstop=4           # Change Tab into 4 spaces
set shiftwidth=4        # Change >> length to 4
set et                  # Convert tab to space
set hlsearch            # highlight all matches in a file when perform a search,
set incsearch           # highlight next match while you're still typing search pattern
verbose                 # where setting is from

set encoding=utf-8      # Korean support
set fileencodings=utf-8,cp949

# AUTOCOMPLETE RELATED
func! AutoClose(...)
  let cur = getline(".")[col(".")]
  if cur != a:1
  if a:1 == "'" || a:1 == '"'
    execute "normal!a".a:1.a:1
  else
    execute "normal!a".a:1
  endif
  execute "normal!h"
  else
  execute "normal!l"
  endif
endfunc

inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap ) <ESC>:call AutoClose(')') <CR>a
inoremap ] <ESC>:call AutoClose(']') <CR>a
inoremap } <ESC>:call AutoClose('}') <CR>a
inoremap " <ESC>:call AutoClose('"') <CR>a
inoremap ' <ESC>:call AutoClose("'") <CR>a
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

" COMMAND RUN related
func! RunScript(...)
  execute ":wa"
  let fileName = a:1
  let fileType = a:2

  if fileType == 'cpp'
  execute ":!g++ -std=c++11 -o ".fileName fileName.".cpp && cat ".fileName.".txt 2> /dev/null | ./".fileName
  elseif fileType == 'py'
  execute ":!cat input.txt 2> /dev/null |" "python3" fileName.".py"
  endif
endfunc

nnoremap <C-l> :call RunScript(expand('%<'), expand('%:e')) <CR>

""autocmd *.py nnoremap <F5> :w <CR> :!cat input.txt 2> /dev/null | python % <CR>

"" SYNTAX
syntax on
colorscheme evening
se nu tabstop=4 shiftwidth=4 softtabstop=4 smarttab expandtab autoindent
set hlsearch  " highlight search and search while typing
set incsearch

"" SCREEN
noremap <Left> <C-w><Left>
noremap <Right> <C-w><Right>
```

{% endtab %}
{% endtabs %}

> Navigation

```sh
0 | $          # begin | end of the line
^              # first non-blank character
( | )          # begin | end of the current paragraph
zt | z. | zb   # cursor top | middle | bottom
H | M | L      # move to top | middle | low of the page
ctrl-f | b     # scroll full screen forward | backward
ctrl-d | u     # scroll half screen forward | backward
* / #          # Search current word forward / backward
/copy\C / \c   # Case sensitive / insensitive
```

> search

```sh
:g/pattern/d        # delete all line matching patterns
:g!/pattern/d
:g/^\s*$/d          # delete all blank lines
:g/^$/d             # Delete empty line
\c                  # ignore case
:s/sunny/(&)/       # & is matched text
:g/pattern/m$       # Move all lines matching a pattern to end of file
```

> Mark

```sh
`a             # goto position of mark a
ma             # mark a
:marks         # list all marks
:delmarks a    # delete mark
```

### Action

* map
  * map / imap : normal, visual mode / insert mode
  * unmap : cancel mapping
  * inoremap : insert mode non recursive
  * n / i : normal / insert mode
  * v / s / x : visual select mode / select mode / visual mode only
  * c : command-line
  * l : lang-arg o pending
  * <D- : mac command
  * `<CR>` : carriage return usually the Enter on your keyboard
  * :map : see current mapping
  * remap : makes mappings work recursively
  * nnoremap : one that works in normal mode
  * `<silent>` : show no message when this key sequence is used
  * `<leader>` : let mapleader = autocmd

```sh
map <C-l> <Esc>:w<CR>:!clear;python %<CR>    # run python script
filetype cpp nnoremap <F5> :w <bar> exec '!g++ -g -O2 -std=gnu++17 -static %'<CR>
```

* Copy
  * yy : yank line
  * dd : delete and copy current line
  * ggyG : yank entire file
  * :d : delete current line
  * :m0 : move current line to line 0
  * :wqa : write close all
  * :%w !pbcopy : copy to clipboard
  * :r !pbpaste : paste from the clipboard
  * :w !sudo tee % : without permission

* visual
  * ctrl + v | shift + i # enter : python multiline comment

* macro
  * :reg : Show all current macro
  * "" : unnamed | default register
  * “+ : clipboard
  * "kyy : copy current line to register k
  * “kp : paste k register

> Register

```sh
q[a-z][command]q
@a
```

### File

* expand
  * ("%") : path/file.txt
  * ("%:t") : file.txt
  * ("%:r") : path/file
  * ("%:e") : txt
  * ("%:p:h") : /home/you/path/file.txt

```sh
:e []/file        # Reload current file | Open new file

! : ignore vimrc mapping configure
execute "normal! ihello my name is sean"

startinsert
strftime("%c")
type(var) ==   type(0) / type(function("tr")) / type([]) / type({}) / type(0.0)

%              # current file name
q:             # history
:saveas        # save file as
```

> split

* :tabe file : in a new tab
* Ctrl+w+r : vsplit swap window
* Ctrl+w+= : vsplit resize equal dimension
* :vs file : in a split mode
* :Sex / Vex : split and open file explore
* :tabnew file : open as a new tap

> Lastline

* :![cmd] : run terminal command
* :history : Last command
* :help key-notation : man page
* :retab : Repace tab to spaces
* :3,5y : copy from line 3 to 5

* command Gb :normal i {% tabs %} <CR> {% tab title=""} <CR> {% endtab %} <CR> {% endtabs %} <ESC>

### Vimscript

> Data

* Primitive

```vim
str2float("2.3")
str2nr("3")
float2nr("3.14")
```

* String

```vim
len(str)
split("one.two.three", '.')    # ['one', 'two', 'three']
tolower('Hello')
'hello ' . name
```

* Dictionary
  * count(dict, 'x')
  * empty(dict)
  * get(dict, "apple")
  * has_key(dict, 'foo')
  * keys(dict)
  * len(dict)
  * max(dict)
  * min(dict)
  * remove(dict, "apple")

{% tabs %}
{% tab title='print_every_pair.vim' %}

```vim
# Construct
let colors = {
  \ "apple": "red",
  \ "banana": "yellow"
}

# Access
echo colors["a"]

for key in keys(dict)
  echo key . ': ' . dict(key)
endfor
```

{% endtab %}
{% endtabs %}

> Logical

{% tabs %}
{% tab title='compare' %}

```sh
if name ==# 'John'    # case-sensitive
if name ==? 'John'    # case-insensitive
if name == 'John'     # depends on :set ignorecase
"hello" =~ '/x/'      # regex match
"hello" !~ '/x/'

&&    # and
||    # or

if

let char = getchar()
if char == "\<LeftMouse>"
  " …
elseif char == "\<RightMouse>"
  " …
else
  " …
endif
```

{% endtab %}
{% endtabs %}

> Flows

* For

```vim
for s in list
  echo s
  continue  " jump to start of loop
  break     " breaks out of a loop
endfor
```

* List

```vim
let longlist = mylist + [5, 6]
let mylist += [7, 8]
mylist[2:]
let alist = add(mylist, 4)
```

* while

```vim
while x < 5
endwhile
```

* Function
  * Vimscript functions must start with a capital letter if they are unscoped

```vim
let temp = @@
let @@ = temp  : prevent overwriting current register

function Varg(...)
a:000    # a list containing all the extra arguments that were passed
a:0      # number of argument
a:1      # first argument
```

{% tabs %}
{% tab title='C_prototype.vim' %}

```vim
func! CPrototypeFunction()
let temp = @@
  exe "normal! mayy"
  exe "normal! /Prototypes\<CR>"
  exe "normal! )kpA;\<ESC>"
  exe "normal@ 'a"
let @@ = temp
endfunc
```

{% endtab %}
{% endtabs %}

## VScode

* [enter without key](https://code.visualstudio.com/docs/remote/troubleshooting)
* github1s.com : show github in vscode

> Terms

* workspace
  * override user settings
  * specific to a project and can be shared across developers on a project

* Icons

![img](images/20210214_173530.png)

> shortcut

* Edit
  * ⌘ d : edit multiple variables
  * option up / down : move current code up / down
  * ⌃ Space : trigger IntelliSense Suggestions
  * ⇧ ⌥ a : toggle comment

* Navigation
  * ⌘ o : Open file or folder
  * ⌘ shift f / h : find / replace words in all files
  * ⌘ shift o : find symbol / move to method
  * ⌘ shift . : See all methods
  * ⌘ option click : Open Side
  * ⌘ click : Replace / Click again to go back
  * ⌃ (⇧) - : Navigate back (forward)

* Replace
  * uses () and refernce with $1 for capture group

* Select
  * ⌘ click : Multi-line cursor
  * ⇧ ⌥ drag : Multi-line cursor
  * ⌃⇧⌘←/→ : expand / shrink select

* Screen
  * ⌘ E : Find given word
  * ⌘ B : Toggle Sidebar
  * ⌘ k : zenmode
  * ctrl 1 : Focus on editor
  * ⌘ K ⌘ / : Fold all block comments
  * ⌘ shift B : Build and debug
  * shift ⌘ M : jump to errors and warnings in the project
  * option ⌘ [ : Code folding
  * ⌘ k ⌘ 0 / j : Fold / unfold all codes

* Terminal
  * ⌃ ` : Focus on terminal
  * ⌃ shift ` : New terminal
  * ⌘ ⌥ ← / → / ↑ / ↓ : Toggle between pane / terminal

> Files

{% tabs %}
{% tab title='Settings.json' %}

```json
// ${workspaceFolder} workspace forder

{
  // General
  "editor.wordWrapColumn": 120,
  "editor.formatOnSave": true,
  "files.exclude": {                   // don't show in file explorer
  ".vscode/launch.json": true,
  "env/windows/*.sh": true,
  "env/osx/dmg.applescript": true,
  "bin/": true,
  "build/": true,

  // Use environment variable ${env:Name}
  "args": ["${env:USERNAME}"]

  // Python related
  "python.formatting.autopep8Args": [
    "--max-line-length=200"
  ],
  "python.linting.pylintArgs": ["--generate-members"],           // disable cv2 warning
  "python.pythonPath": "${workspaceFolder}/env/bin/python3",     // python3 -m venv env
  "python.linting.pylintArgs": ["--load-plugins=pylint_django"], // for django

  // c++ related
  "C_Cpp.clang_format_style": "file",                            // use .clang-format in current / home directory
  "C_Cpp.default.configurationProvider": "ms-vscode.cmake-tools", // use CMakeLists.txt for linting
  "editor.wordWrapColumn": 120,
}
```

{% endtab %}
{% tab title='launch.json' %}

```json
{
  "configurations": [
  {
    "console": "integratedTerminal",     // use integrated terminal for console.log
    "sudo" : true,  // must be  used with "console": "externalTerminal"
    // add environment variable
    "env": {"API_BASE":"https://"}  ,
    "envFile": "${workspaceFolder}/.env" ,
    "preLaunchTask": "myShellCommand", // run before
    "justMyCode"  // When omitted / set true (default), restricts debugging to user-written code only
  }
  // Run module
  {
    "name": "Tests",
    "type": "python",
    "request": "launch",
    "module": "page.test",
    "cwd": "${workspaceFolder}",
    "envFile": "${workspaceFolder}/.env"
  },

  // Flask app
  {
    "name": "Main Server",
    "type": "python",
    "request": "launch",
    "module": "flask",
    "env": { "FLASK_APP": "page.app:create_app()", "FLASK_ENV": "development",
        "FLASK_RUN_PORT": "8080", "FLASK_RUN_HOST": "localhost", },
    "args": [ "run", "--cert", "adhoc" ],
    "jinja": true
  }

  // Django app
  {
    "name":"Django",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/manage.py",
    "args": [
      "runserver",
    ],
    "django": true
  }
  ]
}
```

{% endtab %}
{% tab title='task.json' %}

```json
{
  "version": "2.0.0",
  "windows": {
  "options": {
    "env": { "Path": "${config:terminal.integrated.env.windows.Path}" }
  }
  },
  "linux": {
  "options": {
    "env": { "PATH": "${config:terminal.integrated.env.linux.PATH}" }
  }
  },
  "osx": {
  "options": {
    "env": { "PATH": "${config:terminal.integrated.env.osx.PATH}" }
  }
  },
  "presentation": {
  "echo": false,
  "reveal": "always",
  "focus": true,
  "panel": "shared",
  "clear": false,
  "showReuseMessage": true
  },
  "tasks": [
  {
    "label": "Build & Run: Release",
    "command": "bash ./build.sh buildrun Release vscode",
    "type": "shell",
    "group": { "kind": "build", "isDefault": true },
    "problemMatcher": [ "$gcc" ],
  },
  {
    "label": "Build: Release",
    "command": "bash ./build.sh build Release vscode",
    "type": "shell",
    "group": { "kind": "build", "isDefault": true },
    "problemMatcher": [ "$gcc" ]
  },
  {
    "label": "Run: Release",
    "command": "bash ./build.sh run Release vscode",
    "type": "shell",
    "group": { "kind": "build", "isDefault": true },
    "problemMatcher": [ "$gcc" ]
  },
  ]
}
```

{% endtab %}
{% tab title='c_cpp_properties.json' %}

```json
{
  "configurations": [
  {
    "name": "Linux",
    "intelliSenseMode": "gcc-x64",
    "includePath": [
    "${workspaceFolder}/src",
    "${workspaceFolder}/lib",
    "${workspaceFolder}/test",
    "~/SFML-2.5.1/include",
    "/usr/local/include/**",
    "/usr/include/**"
    ],
    "defines": [ "_DEBUG" ],
    "cStandard": "c11",
    "cppStandard": "c++17",
    "forcedInclude": [ "${workspaceFolder}/src/PCH.hpp" ]
  },
  {
    "name": "Mac",
    "intelliSenseMode": "${default}",
    "compilerPath": "/usr/bin/clang",
    "macFrameworkPath": [
    "/Library/Frameworks",
    "/System/Library/Frameworks"
    ],
    "includePath": [
    "${workspaceFolder}/src",
    "${workspaceFolder}/lib",
    "${workspaceFolder}/test",
    "/usr/local/include/**"
    ],
    "defines": [ "_DEBUG" ],
    "cStandard": "c11",
    "cppStandard": "c++17",
    "forcedInclude": [ "${workspaceFolder}/src/PCH.hpp" ]
  },
  {
    "name": "Win32",
    "intelliSenseMode": "gcc-x64",
    "compilerPath": "C:/mingw32/bin/gcc.exe",
    "includePath": [
    "${workspaceFolder}/src",
    "${workspaceFolder}/lib",
    "${workspaceFolder}/test",
    "C:/SFML-2.5.1/include"
    ],
    "defines": [
    "_DEBUG",
    "UNICODE",
    "_UNICODE"
    ],
    "cStandard": "c11",
    "cppStandard": "c++17",
    "forcedInclude": [ "${workspaceFolder}/src/PCH.hpp" ]
  }
  ],
  "version": 4
}
```

{% endtab %}
{% tab title='keybindings.json' %}

```json
{
  "key": "cmd+1",
  "command": "type",
  "args": {
    "text": "{% tabs %}\n{% tab title='' %}\n{% endtab %}\n{% endtabs %}"
  },
  "when": "editorTextFocus"
}
```

{% endtab %}
{% endtabs %}

> Install

* Lagging -> Renderer Type dom

* Window
  * https://docs.microsoft.com/en-us/windows/wsl/install-win10

* Mac
  * $HOME/Library/Application Support/Code/User/settings.json

### Extension

> code runner

* Shortcut to run different codes

{% tabs %}
{% tab title='settings.json' %}

```sh
{
  "code-runner.ignoreSelection": true,       # don't create tempCodeRunnerFile
  "code-runner.saveAllFilesBeforeRun": true,
  "code-runner.runInTerminal": true,
  "code-runner.executorMapByGlob" : {
    "complicated.cpp" : "cd $dir && bash run_complicated.sh"
  }
}
```

{% endtab %}
{% endtabs %}

> vim

* Well integrated with vscode (:vs)

> docker

* show all images and containers

> Remote - Containers

{% tabs %}
{% tab title='code_cli_inside_conatiner.sh' %}

```sh
export PATH="$PATH:$HOME/.vscode-server/bin/<directory with a hash-like name>/bin/"
```

{% endtab %}
{% tab title='.devcontainer/devcontainer.json' %}

```json
{
  "image": "mcr.microsoft.com/vscode/devcontainers/typescript-node:0-12",
  "forwardPorts": [3000],
  "extensions": ["dbaeumer.vscode-eslint"]
}
```

{% endtab %}
{% endtabs %}

> git

* Given featrue branch rebase from master

![](images/20210303_215312.png)

> gitlens

![file diff](images/20210220_013415.png)

> Paste Image

* sudo apt-get update
* sudo apt-get install -y xclip

{% tabs %}
{% tab title='save_image_path.sh' %}

```text
Paste Image:Path ${currentFileDir}/images
```

{% endtab %}
{% endtabs %}

> Prettier

{% tabs %}
{% tab title='.vscode/settings.json' %}

```json
"[typescript]": {
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

{% endtab %}
{% tab title='.prettierrc' %}

```json
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": false,
  "printWidth": 80,
  "tabWidth": 4,
  "arrowParens": "avoid"
}
```

{% endtab %}
{% endtabs %}

> Cmake

* Cmake: Reset CMake Tools Extension State
* configure

```json
// An object containing key : value pairs, which will be passed onto CMake when configuring. It does the same thing as passing -DVAR_NAME=ON via cmake.configureArgs.
{
  "cmake.configureSettings": {"KEY" : "{env:VAR}"}
}
```

## CI (Continuous Integration)

> Terms

* artifact
  * output generated at the end of each build exists beyond build step
  * stored and stacked in registries
  * Authentication is required to upload artifacts

> Docker

* Benefit
  * reduces deployment into small pieces, horizontally scalable
  * same build system, libraries across developer, test, production

* Docker workflow

![](images/20210321_134042.png)

### Jenkins

![img](images/20210214_174049.png)

* 1GB RAM, 10 GB disk → docker community Edition
* stability / extensible / free / visibility using pipelines
* test production like environment quality assurance
* Automate delivery : continuous delivery
* "Archive the artifacts" option in "Post Build Actions" section is specify exact files to archive for build

> Terms

* folder
  * group things together containing jobs views and other folders
  * provides separate namespace, deleting folder delete all contents

* view
  * display jobs that meet a criteria, like a filter

* workspace
  * dedicated directory on the Jenkins server where each job is given and store generated files

* build steps
  * define the actions that Jenkins will take during a build

{% tabs %}
{% tab title='Hello_world' %}

```js
pipeline {
  agent any
  stages {
    stage('Hello') {
      steps {
        echo 'Hello World'
      }
    }
    stage('Bye') {
      steps {
        echo 'Bye World'
      }
    }
  }
}
```

{% endtab %}
{% tab title='cron' %}

```sh
@overnight @hourly @midnight @daily
pipeline {
  agent any
  parameters {
    string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
  }
  stages {
    stage('Example') {
      steps {
        echo "${params.Greeting} World!"
      }
    }
  }
}
```

{% endtab %}
{% endtabs %}

### GitLab

![gitlab](images/20210221_023453.png)

> Variable

* CI_PROJECT_NAME : name of repository
* CI_COMMIT_REF_NAME : name of branch
* token_realm : authentication endpoint, usually GitLab URL. needs to be reachable by the user
* http_secret : random string to sign state that may be stored with client to protect tampering
* internal_key : automatically generated. Contents of key that GitLab uses to sign the tokens.
* registry_http_addr : Needs to be reachable by web server (or LB).

> register

* stage,qa,build,deploy

> File

* .gitlab-ci.yml
  * CI_PIPELINE_SOURCE : push / schedule /web

{% tabs %}
{% tab title='hello_world.yml' %}

```yml
stages:
  - build
  - test

build:
  stage: build
  script:
  - echo "Building"
  - mkdir build
  - touch build/info.txt
  artifacts:
  paths:
  - build/

test:
  stage: test
  script:
  - echo "Testind"
  - test -f "build/info.txt"
```

{% endtab %}
{% tab title='with_docker.yml' %}

```yml
# docker run --rm -it  ubuntu:latest --privileged=true
# [inside docker]
# apt update
# apt install -y apt-transport-https software-properties-common
# apt install curl
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" # docker repository
# apt install docker-ce
# docker run -d --name gitlab-runner --restart always -v /srv/gitlab-runner/config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-runner:latest
image: busybox:latest

before_script:
  - echo "Run an update here or install a build dependency or print out some debugging details"

after_script:
  - echo "do some cleanup here"

build1:
  tags:
    - docker
  stage: build
  script:
    - echo "Do your build here"

test1:
  tags:
    - docker
  stage: test
  script:
    - echo "For example run a test suite"

test2:
  tags:
    - docker
  stage: test
  script:
    - echo "Do another parallel test here"
  only:
  variables:
    - $TEST_LINUX == "true"

deploy1:
  tags:
    - docker
  stage: deploy
  script:
    - echo "Do your deploy here"
```

{% endtab %}
{% endtabs %}

### Github

* Easy setup, same tool

> module

* [avto-dev/markdown-lint@v1](https://github.com/marketplace/actions/markdown-linting-action)
  * rules: '/lint/rules/changelog.js'
  * config: '/lint/config/changelog.yml'
  * args: './CHANGELOG.md'
  * ignore: './one_file.md ./another_file.md'
* actions/setup-python@v1
  * python-version : "3.x"
* [ad-m/github-push-action@master](https://github.com/marketplace/actions/docker-build-push-action)
  * github_token : Token (save in secretes)
  * branch : branch to push
  * username
    * _json_key for GCP
  * password
    * service account json for GCP
* [GoogleCloudPlatform/github-actions/setup-gcloud@master](https://github.com/google-github-actions/setup-gcloud)
  * enable gcloud cli

> Variable

* GITHUB_TOKEN
  * automatically creates a secret to use in your workflow
  * You can use the GITHUB_TOKEN to authenticate in a workflow run
* GITHUB_SHA
  * The commit SHA that triggered the workflow. For example, ffac537e6cbbf934b08745a378932722df287a5d3
  * SHA12: ${GITHUB_SHA::12}
* GITHUB_WORKSPACE
* GITHUB_ACTION
* GITHUB_ACTOR

> Environment variable

* $VARIABLE_NAME
* $Env:VARIABLE_NAME
  * variable is read from the shell
* ${{ env.VARIABLE_NAME }}
  * variable is read from the workflow (can be used for other flow configuration)
  * cannot use environment defined in same step

> artifacts

* Can only be uploaded by a workflow
  * actions/upload-artifact

> yml

* jobs
  * must have identifier with alphanumeric

* name
  * workflow name GitHub displays on your repository's actions page.
  * If omit name, GitHub sets it to workflow file path relative to root of the repository

* on
  * [required] : trigger worflow
  * webhooks, schedule

* action
  * standalone commands that are combined into steps to create a job
  * smallest portable building block of a workflow

* events
  * specific activity that triggers a workflow

* workflow
  * an automated procedure that you add to your repository.
  * made up of one or more jobs and can be scheduled or triggered by an event.

* defaults
  * A map of default settings that will apply to all jobs in the workflow

* defaults.run
  * provide default shell and working-directory options for all run steps in a workflow

* jobs.<job_id>.runs-on
  * Required. The type of machine to run the job on

* jobs.<job_id>.name
  * The name of the job displayed on GitHub

* jobs.<job_id>.needs
  * job1 / [job1, job2] : only jobs that must complete successfully before this job will run
  * If a job fails, all jobs that need it are skipped unless a conditional expression that causes the job to continue.

* run
  * run commands in the virtual environment's shell

* secret
  * stored encrypted environment variable that can't be viewed or edited
  * up to 100 secrets, 64 KB
  * can be accessed with `${{ secrets.STAGING_DB_HOST }}`

![github secret](images/20210220_012131.png)

* on push | [push, pull]
  * Specify the event that automatically triggers the workflow file

* uses
  * identifies an action to use, defines location of that action

{% tabs %}
{% tab title='hello_world.yml' %}

```yml
name: CI
on:         # Controls when the action will run.
  push:     # Triggers the workflow on push or pull request events but only for the main branch
  branches: [ main ]
  pull_request:
  branches: [ main ]
    workflow_dispatch:  # Allows you to run this workflow manually from the Actions tab
jobs:                   # workflow run is made up of 1+ jobs that can run sequentially or in parallel
  build:                # This workflow contains a single job called "build"
  runs-on: ubuntu-latest        # type of runner that the job will run on
  steps:                        # represent a sequence of tasks that will be executed as part of job
  - uses: actions/checkout@v2   # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
  - name: Run a onescript       # Runs a single command using the runners shell
    run: echo Hello, world!
  - name: Run a multi script    # Runs a set of commands using the runners shell
    run: |
      echo Add other actions to build,
      echo test, and deploy your project.
```

{% endtab %}
{% tab title='push_again.yml' %}

```yml
name: Update index.html
on: push
jobs:
  run:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v1
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        dir
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        python update.py
        dir

    - name: Commit files
      id: commit
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "github-actions"
        git add --all
        if [-z "$(git status --porcelain)"]; then
           echo "::set-output name=push::false"
        else
           git commit -m "Add changes" -a
           echo "::set-output name=push::true"
        fi
      shell: bash
    - name: Push changes
      if: steps.commit.outputs.push == 'true'
      uses: ad-m/github-push-action@master
      with:
         github_token: ${{ secrets.GITHUB_TOKEN }}
```

{% endtab %}
{% tab title='deploy.yml' %}

```yml
name: hosting
on:
  push:
    branches: [main]
  schedule:
    - cron: "0 17 * * *"
  workflow_dispatch:
jobs:
  setup-build-deploy:
    name: Setup, Build, and Deploy
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - uses: google-github-actions/setup-gcloud@master
        with:
          version: "290.0.1"
          project_id: seansdevnote
          service_account_key: ${{ secrets.SERVICE_ACCOUNT_JSON }}
      - name: Authorize Docker push
        run: gcloud auth configure-docker
      - name: create .env file
        uses: SpicyPizza/create-envfile@v1
        with:
          envkey_GIT: ${{ secrets.GIT }}
          envkey_OAUTH: ${{ secrets.OAUTH }}
          envkey_SERVICE_ACCOUNT: ${{ secrets.SERVICE_ACCOUNT }}
      - name: Build
        run: |-
          docker-compose build
          docker-compose push
      - name: Deploy
        run: |-
          gcloud run deploy page \
            --image gcr.io/seansdevnote/page \
            --region us-central1 \
            --platform "managed" \
            --service-account firebase-adminsdk-h70pe@seansdevnote.iam.gserviceaccount.com
```

{% endtab %}
{% endtabs %}

## Mac

* disable accented key for long press

```sh
defaults write -g ApplePressAndHoldEnabled -bool false
```

### Shortcut

* Screen shot
  * ⌘ ⇧ 3 / 4 : captures a screenshot of your entire screen / drag to select a portion of your screen
  * ⌘ ⇧ 6 : captures number pad
  * (⌃) ⌘ shift 4 / 5 : Screen shot (saved to clipboard)

* Shortcut
  * ⌘ ⇧ / : Help
  * ⌘ space : Search files
  * ⌥ ⌘ v : Ctrl x for files
  * ⇧ ⌘ . : See Hidden files
  * ⌃ ⌘ space : See special characters
  * ⌘ ⇧ G : Go to specific file path
  * ⌘ ⌃ f : Full screen
  * System Preferences -> Sharing -> Computer Name:

## Google

* search
  * &tbs=qdr:X : n h d w m y
  * past 6 month : `http://www.google.com/search?q=local+seo&tbs=qdr:m6`

### Drive

* Free storage
* Version Control
* Shareable link with different permission
* drive API for automation (fetching, writing)

* Shortcut
  * ⌃ ⌥ f : File
  * ⌃ ⌥ e : Edit
  * ⌥ / : Search menu
  * ⌘ / : Search shortcut

### Docs

* [Equation](http://www.notuom.com/google-docs-equation-shortcuts.html)

* Shortcut
  * ⌥ ⌘ x : Spell check
  * ⇧ ⌘ c : page info
  * ⌘ ⌥ 1~6 : Heading
  * ⌘ ⌥ c / v : style copy / paste

### Form

* make quiz -> put answer

### Sheet

* Shortcut
  * option ↑ ↓ : Change sheet

### Chrome

* Shortcut
  * ⌘  d : bookmark
  * ⌘  l : search tab
  * ⌘  ` : change window
  * ⌘  ⇧  t : reopen closed tab
  * ⌘  ⇧  c : page inspection

> Extension

* stylish
  * Customize css for any website

{% tabs %}
{% tab title='gitbook.css' %}

```css
/* Increase Center */
.reset-3c756112--pageContainer-544d6e9c {
  max-width: 1800px;
}

/* Hide left navigation */
.reset-3c756112--body-324a5898 {
  margin: 0;
}

.reset-3c756112--contentNavigation-dd3370a4 {
  min-width: 0px;
}

/* Hide except edit on github */
.reset-3c756112--menuItem-aa02f6ec--menuItemLight-757d5235--menuItemInline-173bdf97--pageSideMenuItem-22949732:not(:first-child) {
  display: none;
}

/* reduce right navigation */
.reset-3c756112--contentNavigation-dd3370a4 {
  padding-left: 0;
  width: calc((100% - 1448px) / 5);
}

.reset-3c756112--pageSide-ad9fed26 {
  width: 180px;
}

/* Hide admin option */
.reset-3c756112--sidebarNav-1270f224 {
  display: none;
}

.reset-3c756112--body-324a5898 {
  width: 100%;
}
```

{% endtab %}
{% endtabs %}

## Latex

![alt](images/20210214_175128.png)

* Starts From 0

```text
\setcounter{section}{-1}
```

* Put string before section

```text
\usepackage{titlesec}
\titleformat{\subsection}{\normalfont\large\bfseries}{Task \thesubsection}{1em}{}
```

* Change sub sections to arabic

```latex
\renewcommand{\thesubsection}{\thesection.\alph{subsection}}
\renewcommand\thesubsection{\thesection.\arabic{subsection}}

\arabic (1, 2, 3, ...)
\alph (a, b, c, ...)
\Alph (A, B, C, ...)
\roman (i, ii, iii, ...)
\Roman (I, II, III, ...)
\fnsymbol (∗, †, ‡, §, ¶, ...)
```

> Number

* Fraction

```latex
\over{1}{2}
```

> Figure

* Multiple Figures

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}[b]{0.45\textwidth}
  \includegraphics[width=\textwidth]{images_new/d1.png}
  \caption{Loss for 0.0001 L2}
  \label{pca_vectors}
  \end{minipage}
  \hfill
  \centering
  \begin{minipage}[b]{0.45\textwidth}
  \includegraphics[width=\textwidth]{images_new/d1_2.png}
  \caption{Accuracy for 0.0001 L2}
  \label{pca_vectors}
  \end{minipage}
\end{figure}
```

* Ordered, unordered

```txt
\begin{itemize/enumerate}
  \item One entry in the list
  \item Another entry in the list
\end{itemize/enumerate}
```

* Spacing

```sh
\!        # -3 mu
\quad     # 18 mu
\qquad    # 36 mu
```

* Vector

```latex
\left[\begin{array}{c} 1\\0\\1\end{array}\right]
```

* Every Grid

```latex
\begin{center}
\begin{tabular}{ | m{5em} | m{1cm}| m{1cm} | }
\hline
cell1 dummy text dummy text dummy text & cell2 & cell3 \\
\hline
cell1 dummy text dummy text dummy text & cell5 & cell6 \\
\hline
cell7 & cell8 & cell9 \\
\hline
\end{tabular}
\end{center}

\begin{table}[]
\begin{tabular}{lllll}
 &  &  &  &  \\
 &  &  &  &  \\
 &  &  &  &  \\
 &  &  &  &
\end{tabular}
\end{table}

> Matrix
\documentclass{article}
\usepackage{amsmath}
\begin{document}
\[
\begin{bmatrix}
  x_{11}       & x_{12} & x_{13} & \dots & x_{1n} \\
  x_{21}       & x_{22} & x_{23} & \dots & x_{2n} \\
  \hdotsfor{5} \\
  x_{d1}       & x_{d2} & x_{d3} & \dots & x_{dn}
\end{bmatrix}
=
\begin{bmatrix}
  x_{11} & x_{12} & x_{13} & \dots  & x_{1n} \\
  x_{21} & x_{22} & x_{23} & \dots  & x_{2n} \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  x_{d1} & x_{d2} & x_{d3} & \dots  & x_{dn}
\end{bmatrix}
\]
\end{document}
```

## Markdown

* a lightweight markup language for creating formatted text using a plain-text editor
* [Syntax Highlight](https://support.codebasehq.com/articles/tips-tricks/syntax-highlighting-in-markdown)

* Two table side by side

```html
<table>
<tr><th> Orders </th><th> Employees </th></tr>
<tr><td>

| OrderID | CustomerID |
| ------- | ---------- |
| 10308   | 2          |
| 10309   | 37         |
| 10310   | 77         |

</td><td>


| EmployeeID | LastName  | FirstName | BirthDate | Photo      |
| ---------- | --------- | --------- | --------- | ---------- |
| 1          | Davolio   | Nancy     | 12/8/1968 | EmpID1.pic |
| 2          | Fuller    | Andrew    | 2/19/1952 | EmpID2.pic |
| 3          | Leverling | Janet     | 8/30/1963 | EmpID3.pic |

</td></tr> </table>
```

* basic

```text
#n                   # headers
** bold    **        # Bold
 > backquote         #
* / + / -            # list (add spaces to make sublist)
1. / 2.              # unordered list
![sample](/assets/images/tux.png)        # images> Code Snipet
```

* table

```text
|     | name | score | rank |
| --- | ---- | ----- | ---- |
| A   |      |       |      |
| B   |      |       |      |
```

> footnote

* Here's a simple footnote,[^1] and here's a longer one.[^bignote]

```text
[^1]: This is the first footnote.
[^bignote]: Here's one with multiple paragraphs and code.
  Indent paragraphs to include them in the footnote.
  `{ my code }`
  Add as many paragraphs as you like
```

> Distribution

* Pandoc’s
  * the most comprehensive one to our knowledge.

* Rmarkdown
  * Datavisualization in R

> Syntax

* Images

```md
![test](a.png)
```

> Size

```md
![test](a.png =192x102)        # Not supported in gitbook
<img src="a.png" width="640" height=360 />
```

> Math

![alt](https://github.com/SeanHwangG/tool/tree/ced6d494fa4e440252b0041e1debf3dc75a94eaf/book/images/2021-02-05-16-34-50.png)

```sh
$$
\int_{-\infty}^\infty g(x) dx
$$
```

> Presentation

```sh
pandoc -t beamer presentation_example.md -o output.pdf
```

{% tabs %}
{% tab title='vim' %}

```md
% Title of talk
% Speaker Name
% Date of Talk

# Title of Slide 1

* Item of list

$$ \sum..{a,b} + x y \infty $$

# Title of Slide 2

1. *Italic*
2. **Bold**
3. ~~line through~~
```

{% endtabs %}

### Gitbook

* For full functionality, use app.gitbook.com web ui

> Pros

* Free hosting, easy setup
* h1 based text search
* full markdown \(push github automatically updates\)
* math equation latex
* images \(using paste image vscode extension\)

> Cons

* Dynamic contents (API Support in new version)
* Customizing (Stylish extension)

> _Error

* TypeError: cb.apply is not a function inside graceful-fs

```sh
cd /usr/local/lib/node_modules/gitbook-cli/node_modules/npm/node_modules/
npm install graceful-fs@4.2.0 --save
```

* TypeError: Cannot read property 'pipesCount' of undefined

```sh
npm install gitbook-cli@2.1.2 --global
```

* Wrong codeblock output
  * Codeblock \(\`\`\`\) must has new line before starting
  * sub list must be preceded by at least 4 space

> New version

* [https://{username}.gitbook.io/](https://{username}.gitbook.io/)
* demo / document : [https://docs.gitbook.com/](https://docs.gitbook.com/)
* Change of UI \(contents navigation\)
* Add full space search \(prermium\)

```sh
https://app.gitbook.com/{username}/spaces
integration on left tab -> github

# Add Summary
https://github.com/GitbookIO/gitbook/blob/master/docs/SUMMARY.md

# Contents
https://github.com/GitbookIO/gitbook/tree/master/docs
```

> Old version

* gitbook cli
  * ls : Show version installed
  * serve : Run locally
  * update : Update version
  * install : Install required plugins

* [https://{username}.github.io/](https://{username}.github.io/)
* demo / document : [https://gitbookio.gitbooks.io/documentation/content/](https://gitbookio.gitbooks.io/documentation/content/)
* Setup

```sh
# Setup PC
git --version               # git version 2.17.1
node --version
npm --version

npm install -g gulp         # provides a way to sequence commands that execute steps in local Operating System
gulp --version              # 2.3.0
npm install -g gitbook-cli  # gitbook-cli

# Main Homepage
git pull [username].github.io
echo "<h1> Main </h1>" > index.html
git

# Setup per repository
git clone https://github.com/rebeccapeltz/gitbook-publishable-template.git
mv gitbook-publishable-template/* .
echo "{}" > book.json
grep -qxF '_book' .gitignore || echo '._book' >> .gitignore
grep -qxF 'node_modules' .gitignore || echo '._book' >> .gitignore
rm -rf gitbook-publishable-template
echo "Successfully Setup"

# Publish to Github pages
# alias gbp="gitbook install && gitbook build && rm -rf docs && mkdir -p docs && cp -R _book/* docs && git clean -fx node_modules && git clean -fx _book && git add -A && git commit --amend --no-edit && git push --force"
gitbook install && gitbook build
rm -rf docs
mkdir -p docs
cp -R _book/* docs

git clean -fx node_modules
git clean -fx _book

git add -A && git commit --amend --no-edit && git push --force
```
