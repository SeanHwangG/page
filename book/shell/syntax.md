# Syntax

> globbing

* \* : expands to all the files (except .) in the current working directory unless quoted
  * ls * : lists all files in a directory
* ? : matches any single characte
* [a-d] : matches any character from a, b, c or d

{% tabs %}
{% tab title='globbing.sh' %}

```sh
MYGLOB=*        # No quotes around the glob
echo $MYGLOB    # Glob is interpreted
MYGLOB="*"      # Double / single quotes around the glob
echo "$MYGLOB"  # *
echo '$MYGLOB'  # $MYGLOB
echo $MYGLOB    # Glob is interpreted
```

{% endtab %}
{% endtabs %}

> Error

* script.sh: line 100: syntax error: unexpected end of file
  * close do done / if fi / case esac / { } / ( )?
* Unexpected end of file while looking for matching ...
  * double-quote pairs, single-quote pairs (also $'string'!)
  * missing a closing } with parameter expansion syntax
* Too many arguments
  * likely forgot to quote a variable expansion somewhere
* syntax error near unexpected token `('
  * have an alias defined with the same name as the function.
  * Alias expansion happens before the real language interpretion, so expanded and makes your function definition invalid

## IO

### builtIns

```sh
!, %, ., :, @, {, }

alias, alloc, bg, bind, bindkey, break, breaksw, builtins, case, cd, chdir, command, complete, continue, default, dirs, do, done, echo, echotc, elif, else, end, endif, endsw, esac,
eval, exec, exit, false, fc, fg, filetest, fi, for, foreach, getopts, glob, goto, hash, hashstat, history, hup, if, jobid, jobs, kill, limit, local, log, login, logout, ls-F, nice, nohup, notify,
onintr, popd, printenv, pushd, pwd, read, readonly, rehash, repeat, return, sched, set, setenv, settc, setty, setvar, shift, source, stop, suspend, switch, telltc, test, then, time, times, trap, true, type,
ulimit, umask, unalias, uncomplete, unhash, unlimit, unset, unsetenv, until, wait, where, which

echo `ls` wolrd     # print inside
```

> keywords

* Special parameters
  * $ : Escape to variable
  * $- : option flags enabled in current shell using set
  * $_ : previous last parameter or command if none (mkdir -p foo/bar/zoo && cp myfile $_)
  * $$ : PID of the current instance of shell (same in subshell)
  * $# : Number of arguments supplied to a script
  * $n : arguments with which a script was invoked ($1)
  * $0 : name of the shell or / current script
  * $@ : All the arguments are individually double quoted
  * $? : Exit status of the last command executed
  * $! : Process number of the last background command (using * or |)

* Shell Variable : cannot be overwritten
  * BASH : Expands to the full file name used to invoke this instance of bash.
  * UID / EUID : numeric real / effective user id of the current user
  * GROUPS : array containing list of groups of which the current user is a member
  * LANG : setting for all that are not directly set by a LC_* variable.
  * LANGUAGE : set LC_MESSAGES to a multi-valued value
  * LC_ALL : Takes precedence over all LC_*, LANG, LANGUAGE
  * LC_NUMERIC : Determines locale category for numeric formatting
  * LC_TIME : determines the locale category used for data and time formatting
  * LINENO : line number in script or shell function currently executing
  * OLDPWD : previous working directory
  * PPID (readonly) : The process ID of the shell’s parent process
  * RANDOM : Each time referenced, expands to a random integer 0 ~ 32767.
  * PS4 : denotes the value is the prompt printed before the command line

## Input

> Command line

{% tabs %}
{% tab title='defulat_arg.sh' %}

```sh
grep -r -- "-n"        # using '--' declare '-n' is not an option

# Optional Argument
ARG1=${1:-foo}
ARG2=${2:-bar}

echo "$ARG1"
echo "$ARG2"

# Check envrionment is set
if [[ -z $REPO_PATH ]]; then
  echo "REPO_PATH not set"
  exit 1
fi
```

{% endtab %}
{% tab title='shift.sh' %}

```sh
# shift.sh a b c d
echo "Total arguments passed are: $#"
echo "The arguments are: $*"      # $* is used to show the command line arguments
echo "The First Argument is: $1"  # a

echo "The First Argument After Shift 2 is: $1"  # c
shift
echo "The First Argument After Shift is: $1"    # d
```

{% endtab %}
{% endtabs %}

## Data

* doesn’t have data types → used as string in string operation / int in int operation

* Single quote
  * No string is escaped
  * added with $'' to use escape characters

* double quote
  * make string separated by space, prevents globbing

{% tabs %}
{% tab title='single_quote.sh' %}

```sh
AA=100
sh -c "AA=200; echo $AA"    # 100 -> variable is expanded first
sh -c 'AA=200; echo $AA'    # 200 -> variable is not expanded

# I love
# you
echo $'I love\n\'you\''
```

{% endtab %}
{% tab title='double_quote.sh' %}

```sh
echo "I
Love you"        # prints in multiline
AA="I
Love you"
echo $AA         # prints in single line unless quoted "$AA" (in bash)

$(( 0377 ))      # expand oct
$(( 0xff ))      # expand hex
```

{% endtab %}
{% endtabs %}

* Meta char
  * can be used without space
  * () : create subshell
  * ; : two commands in a line

* string
  * multiple spaces and tab is replaced by space (" preserves space and new line)
  * \ to use multiline string
  * -z / -n : if string is empty / filled
  * -d : if directory exists
  * ${#PARAMETER} : length of string
  * ${parameter:+word}
  * ${parameter:offset}
  * ${parameter:offset:length}
  * string=01234567890abcdefgh
  * echo ${string:7/-7} : 7890abcdefgh / bcdefgh
  * echo ${string:7:2/-2} : 78 / 7890abcdef

## Operation

* redirection
  * >> : append
  * >1 | > : stdout
  * &> | >& : standard output and error (&> preferred)
  * >&0 : redirect same as stdin
  * >&1 : redirect same as stdout
  * >&2 : redirect same as stderr
  * 2>&1 : redirect stderr to whatever value is set to stdout

> Expansion

* Arithmetics
  * $(( )) : $(( 1 + 2 )) ...

* brace expansion
  * echo a{d,c,b}e : ade ace abe
  * mkdir /usr/local/{old,new} : create multiple

* Tilde
  * ~ is expanded ONLY if it is the first character of a word AND it is unquoted
  * ~- : old pwd
  * ~-/+ n : same as dirs -/+ n
  * -fred : home directory of the user fred

* Parameter
  * ${param:-word} : If param is unset, substitute expansion of word, else param
  * ${parameter:=word} : If param is unset, expansion of word is assigned to parameter
  * ${param:?word} : if param is unset, expansion of word to stdout (stderr if unset)

* process substitution
  * allows a process’s input or output to be referred to using a filename
  * <(list) : input
  * >(list) : output

> Substitution

* ${ }
  * variable  $AA, ${AA}, ${AA:-5}, ${AA%.*} ...

* $( )
  * Modern way of backtick, enable nested
  * $( echo "1.3 + 2.5" | bc )

* Backtick
  * echo `time` : escape command

### Conditional

* doesn’t have data types → used as string in string operation / int in int operation

* Operation
  * : : True
  * && / || : and / or
  * -R name : True if shell variable name is set and is name reference
  * -z string : True if the length of string is zero.
  * -n : string not empty

* Files
  * -a / e / f / s / L FILE : Exists / regular file / non-empty / symbolic link
  * -r / w / x FILE aa : readable / writable / executable
  * file1 -ef file2 : if file1 and file2 refer to the same device and inode numbers
  * file1 -nt file2 : file1 modification date is newer than file2 (file1 exists not file2)
  * file1 -ot file2 : file1 modification date is older than file2 (file2 exists not file1)

> if

* space between braces
* == and = is equivalent
* ~= for regex match

{% tabs %}
{% tab title='if.sh' %}

```sh
cd ~/tempdir && rm -rf *     # only remove if cd success
if [[ -z $ENV ]]; then       # check environment variable is set
  echo "Please set ENV"
  exit 1
fi

if [[ "a" == "$1" ]]; then
  echo 1
elif [[ "b" == "$1" ]]; then
  echo 2
else
  echo "0"
fi

# Contains check
string='My long string'
if [[ $string == *"My long"* ]]; then
  echo "It's there!"
fi
```

{% endtab %}
{% tab title='case.sh' %}

```sh
case $- in
  *i*) ;;
    *) return;;
esac
```

{% endtab %}
{% endtabs %}

> For

{% tabs %}
{% tab title='update_repo.sh' %}

```sh
for d in */ ; do
  cd $d
  echo $d
  git add -A && git commit --amend --no-edit && git push --force
  cd ..
done
```

{% endtab %}
{% tab title='infinite_loop.sh' %}

```sh
for (( ; ; ))
do
  echo "infinite loops [ hit CTRL+C to stop]"
done
```

{% endtab %}
{% tab title='multiplication.sh' %}

```sh
read x
read y
for i in {+,-,"*",/}
do
  var=$(((x)$i(y)))
  echo $var
done
```

{% endtab %}
{% tab title='rename_multi.sh' %}

```sh
for file in Picture*.jpg
do
  mv "$file" "vacation-$file"
done
```

{% endtab %}
{% endtabs %}

### String

{% tabs %}
{% tab title='substring.sh' %}

```sh
Str="Learn Linux from LinuxHint"
subStr=${Str:6:5}
echo $subStr
```

{% endtab %}
{% tab title='regex.sh' %}

```sh
case "$(uname -s)" in
  Linux*)   machine=Linux;;
  Darwin*)  machine=Mac;;
  CYGWIN*)  machine=Cygwin;;
  MINGW*)   machine=MinGw;;
  *)        machine="UNKNOWN:${unameOut}"
esac
echo ${machine}
```

{% endtab %}
{% endtabs %}

## Iterable

{% tabs %}
{% tab title='sleep.sh' %}

```sh
echo "pid is $$"

while (( COUNT < 10 ))
do
  sleep 10
  (( COUNT ++ ))
  echo $COUNT
done
exit 0

# keep input key
valid=true
while [ $valid ]
  do
  echo "press q to quit"
  read key
  if [[ $key = "q" ]] || [[ $key = "Q" ]]; then
    break
  fi
done
```

{% endtab %}
{% tab title='' %}

```sh
while [[ $# -gt 0 ]];
do
  key="$1"
  case "$key" in
    -s|--source-dir)
    source_dir=$(realpath $2)
    shift
    shift
    ;;
    -r|--resource-dir)
    resource_dir=$(realpath $2)
    shift
    shift
    ;;
    -m|--mode)
    mode="$2"
    shift
    shift
    ;;
    *)
  esac
done
```

{% endtab %}
{% tab title='getopts.sh' %}

```sh
DEBUG=0
CLEAN=0
while getopts cfd option
do
case $option in
c) CLEAN=1
  ;;
d) DEBUG=1
  ;;
esac
done
```

{% endtab %}
{% endtabs %}

### Array

* a=($(cat))
* echo ${a[@]}
* echo {10..1..2} : similar to range
* echo two{apple,banana}s : prefix suffix

## OOP

### Function

{% tabs %}
{% tab title='cli.sh' %}

```sh
function e {
    echo $1
}
e Hello

# default argument
echo_and_run() { echo "\$ $*" ; "$@" ; }

FOO="${VARIABLE:-default}"
```

{% endtab %}
{% endtabs %}
