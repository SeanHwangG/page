# Python

* Created by Guido van Rossum
* object-oriented language (represented by objects or relations between objects), dynamic typing
* [+] Community. (Don’t reinvent the wheel: github.com/nuno-faria/tetris-ai)
* [+] Resource (Machine learning, Web scraping)
* [+] Easy (shorter code)
* [-] Scope confusion → inner scope can see not modify the outer scope
* [-] untyped → slow
* [-] Python wasn’t made with mobile in mind → javascript, android studio, Swift C
* [Reference 1](https://wikidocs.net/book/536)
* [Reference 2](https://docs.python.org/3/)

* Download

```sh
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
```

## Error

> Class

* TypeError: Cannot create a consistent method resolution

```py
class Player:
    pass

class Enemy(Player):
    pass

class GameObject(Player, Enemy):
    pass

g = GameObject()
```

* GameObject is inheriting from Player and Enemy. Because Enemy already inherits from Player

> Module

* Command '['/path/to/env/bin/python3.7', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
  * sudo apt-get install python3.9-venv

* Cannot be found
  * python3 -c "import sys;print(sys.path)"
  * Add to PYTHONPATH

* zsh: command not found: pipreqs
  * When running a module as cli
  * export `PATH="/Users/<my-username>/Library/Python/<python-edition>/bin:$PATH"`

* RuntimeWarning: 'module.api' found in sys.modules after import of package 'module', but prior to execution of 'module.api'; this may result in unpredictable behaviour
  * python3 -m module.a

* python command not found
  * `/usr/local/opt/python@3.8/bin:$PATH`

```py
# module/api.py
constant = 5

# module/__init__.py
from .api import constant
```

* circular import

```py
# a.py
import b

def function_a():
    print('function_a')
    return b.function_b()

function_a()

# b.py
import a
def function_b():
    print('function_b')

def function_c():
    print('function_c')
    return a.function_a()
```

> Syntax

* NameError: name 'prin' is not defined
  * try to use a variable or a function name that is not valid
  * print(1)

```py
prin(1)
```

* SyntaxError: unexpected EOF while parsing
  * print(1)

```py
print(1
```

* AttributeError: 'builtin_function_or_method' object has no attribute 'split'

```py
a = input.split()
```

* IndentationError: expected an indented block
  * for must be indented by some space

```py
for i in range(3):
print(1)
```

* TypeError 'float' object cannot be interpreted as an integer
  * range function takes int

```py
range(11 / 2)
```

* TypeError 'int' object is not iterable
  * min function takes iterable

```py
min(1)
```

* UnboundLocalError: local variable 's' referenced before assignment
  * variable can't be both local and global inside a function

```py
def f(): 
  # global s    # Solution
  print(s)      # Error
  s = "I love London!"
  print(s)
 
s = "I love Paris!"
f()
```

* AttributeError: <'classmethod' or 'staticmethod'>,  object has no attribute '__name__'
  * apply classmethod and staticmethod last when using multiple decorators

```py
class My_class(object):
    @classmethod
    @print_function_name

class GameObject(Enemy):
    pass
```

> Terms

* Expression
  * If you can print it, or assign it to a variable, it’s an expression. 
  * Atoms is the most basic element of expressions → identifiers, literals, forms enclosed in parentheses

* Statement
  * If you can’t print it, or assign it to a variable, it’s a statement

* Identifier
  * unlimited in length. Case is significant 

* GIL
  * None python created thread doesn’t have thread state structure
  * PyGILState_Ensure() / PyGILState_Release()  # create thread data structure and free

## Packaging

> PYTHONPATH

* environment variable which you can set to add additional directories where python will look for modules and packages

> Namespace

* mapping from names to objects → most are currently implemented as Python dictionaries

```sh
parent/
  __init__.py
  one/
    __init__.py
  two/
    __init__.py
```

* importing parent.one will implicitly execute parent/__init__.py and parent/one/__init__.py
* subsequent imports of parent.two will execute parent/__init__.py and parent/two/__init__.py
* composite of various portions, where each portion contributes a subpackage to the parent package
* __path__ attribute : custom iterable type which automatically perform a new search for portions 

> Potions

* A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package

> Module

* a file containing Python definitions and statements. 
* file name is the module name with the suffix .py
* each module is only imported once per interpreter session
* when module changes, restart interpreter – or use importlib.reload(), 

> Package

* structuring Python’s module namespace by using “dotted module names”.
* special module that helps organize modules, provide naming hierarchy (directories on a file system)
* All packages are modules
* Create isolated Python environments

> from <module_name> import *

* imports all names except those beginning with an underscore
* bad since it introduces an unknown set of names into interpreter, hiding some important things 

> import foo.bar.baz 

* first tries to import foo, then foo.bar, and finally foo.bar.baz

```sh
python3 -m reader          # run package / library module (__main__)
```
## Convention

* a blank line group import
* Standard library | third party | Local application/library specific

> Variable

```sh
_single_leading     # from M import * doesn’t import these objects
single_trailing_    # avoid conflicts with Python keyword (ex. class_, id_)
CONSTANT_VAR        # all capital letters with underscores separating words
ClassName           # capwords 
function_name, var_name
```

> @classmethod vs @staticmethod

* cls for the first argument to class methods used for constructor overloading
* staticmethod can have no parameters at all

```py
if foo is not None:     # Wrong: if not foo is None:
def f(x): return 2*x    # Wrong: f = lambda x: 2*x
if greeting:            # Wrong: if greeting == True:
```

> if __name__ == "__main__": 

* module’s name (as a string) is available as the value of the global variable __name__
* convenient UI to module, or for testing purposes

```py
# a.py
print(1)
if __name__ == "__main__": 
  print(2)

# b.py
import a
python b.py             # prints 1
```

> Interpreters

* Cpython
  * Default and most widely used python interpreter written in C and Python 
  * uses GIL for thread-safe operation
  * each thread owns PyThreadState  and only thread created it can acquire GIL

* Jython
  * as a scripting language for Java applications
  * tests for Java libraries | create applications using the Java class libraries 

* Pypy
  * faster than CPython because PyPy is a just-in-time compiler while CPython is an interpreter
  * easier to modify the interpreter

> Files

* __pycache__
  * caches the compiled version of each module in the __pycache__
  * directory to put  bytecode which interpreter compiled
  * PYTHONDONTWRITEBYTECODE to any non blank string to disable bytecode 
  * .pyc files is the speed with which they are loaded

* __init__.py
  * __init__.py code defines a list named __all__ (default None)
  * taken to be list of module names that should be imported when from package import * 

## Tools

### Style

> Linter

* Styles PEP Python Enhancement Proposals
* A code linter is a program that analyses your source code for potential errors → pylint

```sh
[MASTER]
jobs=1                         # Use multiple processes to speed up Pylint. Specifying 0 will auto-detect the number of processors available to use.
#ignore=CVS                    # Add files or directories to the blacklist. They should be base names, not paths.
unsafe-load-any-extension=yes  # Allow loading of any C extensions. They are imported into active Python interpreter and may run arbitrary code.


# A comma-separated packages, module names from where C extensions may be loaded. 
# Extensions loads into  active Python interpreter and may run arbitrary code.
extension-pkg-whitelist=cv2

max-line-length=1024  # single line.
# run only  classes checker, but have no Warning level messages displayed
# --disable=all --enable=classes --disable=W
disable=
    C0114, # missing-module-docstring
    C0115, # missing-class-docstring
    C0116, # missing-function-docstring
    W0703, # Catching too general exception Exception (broad-except)
    R0801, # Similar lines in 2 files (duplicate-code)
    R1705, # Unnecessary "elif" after "return" (no-else-return)
    E0401, # (import-error)
    W0401, # (wildcard-import)

argument-naming-style=any    # Naming style matching correct argument names.
variable-naming-style=any    # snake_case, camelCase, PascalCase, UPPER_CASE
#argument-rgx=               # Regular expression matching correct variable names. Overrides variable-naming-style.
const-naming-style=camelCase # Naming style matching correct constant names.
```

> Autopep

* autopep8 automatically formats Python code to conform to the PEP 8 style guide

### Environment

> conda

* https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf 

```sh
-V               # show conda version
env list         # get all environments (* is activated)
list             # show installed packages

list --revision                  # history of each change to current environment
info                             # get all the current environment details
search PACKAGE_NAME              # use conda to search for a package
create --clone py35 name py35-2  # make copy of an environment
source /Users/sean/anaconda3/bin/activate  # Activate conda
rm -rf ~/.condarc ~/.conda ~/.continuum    # Uninstall conda
create --name py35 python=3.5              # Create new environment py35 install Python 3.5
create --clone py35 --name py35-2          # Make exact copy of an environment 
source activate py35                       # activate environment
deactivate                                 # Exit from conda
update conda                               # update version
install -y -c <anaconda> bsddb             # Install (anaconda.org 에서 <owner > 수정)
```

> venv

* Prefered as it is official

```py
python3 -m venv env
source env/bin/activate
```

## Installer

> Pypi (Python Package Index)

* a repository of software for the Python programming language

> Easy install

* Python-only system for install Python libraries → libraries installed in system Python's site-packages

### pip

* Python package-management system
* homebrew automatically download pip: brew install python

```sh
list                        # List pip packages
show -f cv2                 # See details of the package
freeze > requirements.txt   # save | download all required packages
```

> pip install

```sh
--without-pip
-r requirements.txt         # install everything in requirements
-verbose <my_package>       # verbose
--no-cache-dir --upgrade <package>  # ignore local file
--upgrade pip                       # Update
--force-reinstall                   # downgrade

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  # reinstall pip
python3 get-pip.py --force-reinstall
python3 -m pip install                                   # pip doesn’t work
rm -rf ~/.local/lib/python3.6/site-packages/numpy
pip3 install livereload==2.5.1
```

> config

* change default location for pip

```sh
# Unix

$ cat $HOME/.pip/pip.conf

# windows

$ type %HOME%\pip\pip.ini

[global]
target=C:\Users\Bob\Desktop
```

### Interactive

> Ipython

```sh
ipython3 -i file_name.py
```

> Jupyter

```sh
jupyter notebook .      # Open
python3 -m notebook .

from IPython.display import display   # print in nicer form
_ih[-5:]                              # code of the 5 most recently run cells

from IPython.core.debugger import set_trace

c     # continue until the next breakpoint
n    # next line of code (→ shows current position)
q     # quits
```

* shortcut

```sh
ctrl + enter            # Run cell
shift + enter           # Run cell and move
alt + enter             # Create cell below
dd                      # Delete current cell
command + shift + C     # command palette
```

* magic

```sh
%load_ext autoreload
%autoreload 2                   # Reload modules (except %aimport) automatically 
%debug                          # Run pdb
%reset_selective <regular_expression>
%reset -f
%who                            # List all variable
%whos                           # Some extra information about each variable
%matplotlib                     # Set up matplotlib to work interactively

%%time                          # Information about a single run of the code
%%bash                          # Run bash script (bash, HTML, latex, markdown)
%%writefile name                # Write the contents of the cell to a fill
```
