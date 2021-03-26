# Module

> Term

* multifile module
  * module to reference each other using __init__.py

## Util

> ast

* literal_eval(str) : only accept str, num, tuples, lists, dicts, booleans, None ("rm -rf" error)

> copy

{% tabs %}
{% tab title='copy.py' %}

```py
a = [1,2]
b = copy.copy(a) # equivalent to [e for e in a], a[:]

# deepcopy()     preserve the graphical structure of the original compound data
a = [1,2]
b = [a,a]        # there's only 1 object a
c = copy.deepcopy(b)

c[0] is a        # return False, a new object a' is created
c[0] is c[1]     # return True, c is [a',a'] not [a',a'module.md']
```

{% endtab %}
{% endtabs %}

> mmh3

* mmh3.hash('aaaa', -1756908916) : hash string based on value

> platform

* processor() : (real) processor name, e.g. 'amdk6'
* python_implementation() : Get one of 'thon’, ‘Irothon’, ‘Jython’, Py’
* python_version() : python version as string 'major.minor.patchlevel
* system() : system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'

> functool

* reduce(lambda a,b : a if a > b else b, [1,5,3]) : get maximum
* lru_cache(maxsize=32) : decorator
* cache_clear() / cache_info() : clear / print cache info for decorated function

> itertools

* number of iterator building blocks inspired by constructs from APL, Haskell, and SML
* Each has been recast in a form suitable for Python

* accumulate(iterable, func, *, initial) : accumulate([1,2,3,4,5]) → 1 3 6 10 15
* chain(*iterables) : chain('ABC', 'DEF') → A B C D E F
* combinations(iterable, r) : combinations('ABCD', 2) → AB AC AD BC BD CD
* compress(data, selectors)
  * compress('ABCDEF', [1,0,1,0,1,1]) → A C E F
* count(start=0, step=1)
  * count(2.5, 0.5) : 2.5 3.0 3.5 ...
* cycle(iterable) : ('ABCD') → A B C D A B C
* dropwhile(predicate, iterable)
  * dropwhile(lambda x: x<5, [1,4,6,4,1]) → 6 4 1
* islice(iterable, start, stop, [step]) : ('ABCDEFG', 2, None) → C D E F G
* groupby(iterable, key=None) : [(k, g) for k, g in groupby('AAABB')] → (A, AAA), (B, BB)
* permutations(iterable) : permutations(range(3)) → 012 021 102 120 201 210
* product(*iterables, repeat=1)
  * product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
* repeat(object[, times])
  * repeat(10, 3) → 10 10 10

> operators

* lt / le / eq / ne / ge / gt(a, b) : comparators

> textwrap

* dedent(multiline_string) : start with correct indentation in the source

> unicodedata

* unicodedata.name('/') : SOLIDUS
* unicodedata.decimal('9') : 9
* unicodedata.category('A') : Lu
* unicodedata.bidirectional('한') : L
* unicodedata.lookup('LEFT CURLY BRACKET') : {
* unicodedata.normalize('NFD', u'\u00C7') : decompose: convert Ç to "C + ̧"
* unicodedata.normalize('NFC', u'C\u0327') : compose: convert "C + ̧" to Ç

> typing

* Type[CustomClass] : class CustomClass itself (or a subtype)

{% tabs %}
{% tab title='Hello_typing.py' %}

```py
import itertools
import argparse
from tqdm import tqdm
from math import ceil, sqrt
from typing import List, Dict, Set, Optional, Tuple, Union
from collections import defaultdict, Counter
class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point({self.x}, {self.y})"

  def distance_from(self, other: "Point") -> int:
    return ceil(sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))


class Obj:
  def __init__(self, id: int):
    self._id = id

  def __repr__(self):
    return f"{self.__class__.__name__} {self._id}"

  @property
  def id(self):
    return self._id


class Product(Obj):
  def __init__(self, id: int, weight: int):
    super().__init__(id)
    self._weight = weight

  @property
  def weight(self):
    return self._weight


class PositionObj(Obj):
  def __init__(self, id: int, position: Point):
    super().__init__(id)
    self._position = position

  def __repr__(self):
    return f"{self.__class__.__name__} {self._id} at {self._position}"

  @property
  def position(self):
    return self._position

  def distance_from(self, _other: "PositionObj") -> int:
    return self._position.distance_from(_other.position)

  def find_nearest_object(self, _others: List["PositionObj"]) -> Tuple["PositionObj", int]:
    nearest = _others[0]
    distance = self.distance_from(nearest)
    for other in _others[1:]:
      d = self.distance_from(other)
      if d < distance:
      nearest, distance = other, d
    return nearest, distance


class ProductHolder(PositionObj):
  def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs)
  self._products: Dict[Product, int] = {}

  @property
  def products(self):
  return self._products

  def add_products(self, products: Dict[Product, int]):
  for product, quantity in products.items():
    if product in self._products:
    self._products[product] += quantity
    else:
    self._products[product] = quantity

  def remove_products(self, products: Dict[Product, int]):
  for product, quantity in products.items():
    self._products[product] -= quantity
    if self._products[product] == 0:
    self._products.pop(product)

  @property
  def product_weight(self):
  return sum(p.weight * q for p, q in self._products.items())

  def remove_all_products(self):
  self._products = {}
```

{% endtab %}
{% endtabs %}

### Debug

> Logging

* getLogger() : returns logging.Logger
* logging.Logger
  * setLevel(logging.INFO) : Messages less severe than level will be ignored
  * add / removeFilter(filter) : Adds / remove specified filter filter to this handler
  filter(record)
  * lineno, funcName, message : line number, function name, message
  * debug / info / warning / error / critical(msg)

{% tabs %}
{% tab title='logger_class.py' %}

```py
# NOTSET | 0 < DEBUG | 10 < INFOR | 20 < WARNING | 30 < ERROR | 40 < CRITICAL | 50
basicConfig(filename="newfile.log", level=logging.DEBUG)
log(level, msg, *args, **kwargs)  # Logs a message with integer level level on this logger
logging.getLogger("imported_module").setLevel(logging.WARNING)    # disable imported logger
(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')

# Simple logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')

# Disable unexpected logging in python interactive
logging.getLogger('parso.python.diff').disabled = True

# logger class
import logging
import logging.config

def get_logger(name, level=logging.DEBUG):
  # ignore warning from other module
  logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True
  })

  logger = logging.getLogger(name)

  # remove exsiting handlers -> prevents logged twice
  for hdlr in logger.handlers[:]:
  logger.removeHandler(hdlr)

  # set output to file
  sh = logging.StreamHandler()
  sh.setFormatter(logging.Formatter('%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'))
  logger.addHandler(sh)
  logger.setLevel(level)


  return logger

log = get_logger(__name__)
log.info("hi")
```

{% endtab %}
{% endtabs %}

> rlcompleter

{% tabs %}
{% tab title='django_debug.py' %}

```py
import rlcompleter
import readline
readline.parse_and_bind("tab: complete")
```

{% endtab %}
{% endtabs %}

> tqdm

{% tabs %}
{% tab title='tqdm.py' %}

```py
from tqdm import tqdm_notebook as tqdm

text = ""
bar = tqdm(total=4)
for i, char in enumerate(["a", "b", "c", "d"]):
  time.sleep(0.5)
  bar.update(1)

for i in tqdm.tqdm(range(10000)):
  time.sleep(0.5)
```

{% endtab %}
{% endtabs %}

> warnings

* filterwarnings('ignore') : action='once'
* warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

> dis

* dis() : Return a formatted view of the bytecode operations

> pdb

{% tabs %}
{% tab title='pdb.py' %}

```py
pdb.set_trace()
python -m pdb
```

{% endtab %}
{% endtabs %}

> cprofile

* python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)

{% tabs %}
{% tab title='cprofile.py' %}

```py
def create_array():
  arr=[]
  for i in range(0,400000):
  arr.append(i)

def print_statement():
  print('Array created successfully')

def main():
  create_array()
  print_statement()

if __name__ == '__main__':
  import cProfile, pstats
  profiler = cProfile.Profile()
  profiler.enable()
  main()
  profiler.disable()
  stats = pstats.Stats(profiler).sort_stats('ncalls')
  stats.print_stats()
```

{% endtab %}
{% endtabs %}

> pstats

* ncalls (actual calls / primitive calls)
  * if not recurse, two values are the same

{% tabs %}
{% tab title='pstats.py' %}

```py
import pstats

# after running python3 -m cprofile -o output main.py
p = pstats.Stats("output")
p.sort_stats("cumulative").print_stats(30)        # 30 longest in descending
p.sort_stats("cumulative").print_stats("main.py") # functions in main.py
```

{% endtab %}
{% endtabs %}

> line_profiler

{% tabs %}
{% tab title='line_profiler.py' %}

```py
from line_profiler import LineProfiler
import random

def do_other_stuff(numbers):
  s = sum(numbers)


def do_stuff(numbers):
  do_other_stuff(numbers)
  l = [numbers[i]/43 for i in range(len(numbers))]
  m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

numbers = [random.randint(1, 100) for i in range(1000)]

lp = LineProfiler()
lp_wrapper = lp(do_stuff)
lp_wrapper(numbers)
lp.print_stats()
"""
Timer unit: 1e-06 s

Total time: 0.000768 s
File: <ipython-input-1-d026e2ddfa6e>
Function: do_stuff at line 9

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   9                                           def do_stuff(numbers):
  10         1         16.0     16.0      2.1    do_other_stuff(numbers)
  11         1        228.0    228.0     29.7    l = [numbers[i]/43 for i in range(len(numbers))]
  12         1        524.0    524.0     68.2    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]
"""
```

{% endtab %}
{% endtabs %}

### Path

> fileinput

{% tabs %}
{% tab title="inplace_modify.py" %}

```py
import fileinput

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
  for line in file:
    print(line.replace(text_to_search, replacement_text), end='module.py')
```

{% endtab %}
{% endtabs %}

> dotenv

* pip install python-dotenv
* load_dotenv(dotenv_path=PATH.ENV)

> glob

{% tabs %}
{% tab title='glob.py' %}

```py
import glob, os
os.chdir("/mydir")
for file in glob.glob("*.txt"):
  print(file)
```

{% endtab %}
{% endtabs %}

> pathlib

![Class Diagram](images/20210219_123346.png)

* Path
  * parents
    * MODEL_ROOT = Path(__file__).resolve().parents[2] / 'models'
  * chmod(0o444)
  * name : 'my/setup.py.zip' -> 'setup'
  * stem : setup
  * suffix / suffixes : .py / ['.py', '.zip']
  * as_posix() / as_uri() : win → linux / uri
  * glob('*.py') : get all matched files
  * match('*.py') : patterns
  * stat() : information about this path (st_size, st_mtime)
  * resolve(strict=False) : make absolute
  * is_dir / is_file () : check if directory or file
  * is_absolute() / is_relative_to(*other)
  * mkdir(mode=0o777, parents=F, exist_ok=F)
  * read_bytes() / read_text()
  * write_text(data, encoding=None, errors=None)

> os

* python3 -c 'import sys; print(64 if sys.maxsize > 2 ** 32 else 32)')

* environ : mapping object representing string environment (environ['HOME'])
* close(fd) : Close file descriptor fd
* ctermid() : filename corresponding to the controlling terminal of the process
* chdir(path) : change directory
* getcwd() : current working directory
* getuid() : current process’s real user id
* getpid() : current process id
* getlogin() : name of the user logged in on the controlling terminal of the process
* listdir(path='.') : List containing the names of the entries in the directory given by path
* rename('old,'new) : rename
* system(command) : Execute the command (a string) in a subshell
* times() : current global process times
* rmdir(path, *, dir_fd=None) : Remove directory path
* mkdir(path, mode=0o777, exists_ok=True) : Create a directory named path
* os.path.exists('/usr/local/bin/') : check if path exists

{% tabs %}
{% tab title='recur_size.py' %}

```py
import os

def get_recur_size(path='.'):
  total = 0
  if os.path.isfile(path):
    return os.path.getsize(path)
  else:
    return sum(get_recur_size(fn) for fn in os.scandir(path))
  return total

def human(size):
  for u in ['B', 'KB', 'MB', 'GB']:
    if size < 1024 :
      return f"{size:.1f} {u}"
    size /= 1024
  return f"{size:.1f} {'TB'}"

print(f"In {os.path.abspath('.')} \t {human(get_recur_size())}")
for fn in sorted(os.listdir('.'), key = get_recur_size, reverse=True):
  print(f"{fn} \t {human(get_recur_size('./' + fn))}")
```

{% endtab %}
{% endtabs %}

* os.path
  * basename : data/item.csv → item.csv
  * isabs() : check if absolute path
  * abspath(path) : Get absolute path
  * isfile(fn) / isdir(dn) : Check file / directory exists

* os.sys
  * argv : List of command line arguments passed to a Python script
  * builtin_module_names : names of all modules that are compiled into this Python interpreter
  * byteorder : big vs little endian
  * executable : absolute path of the executable binary for the Python interpreter
  * flags
  * path : All path that is being search by python
  * version_info : assert sys.version_info[0]==3 and assert sys.version_info[1] >= 5
  * exit([arg])
  * cd()

> shutil

* copyfile(src, dst)
* copy2(src,dst)
  * dst can be a directory, in which case the basename of src is used for creating the new file
  * it preserves the mtime and atime in the file metadata

> sysconfig

* get_paths() : dictionary of key-paths
* get_config_var()

### CLI

> argparse

* ArgumentParser() : create parser
  * add_argument("--input", type=str) : add arguments
    * args.myArg is not None : check argument
    * required=False : whether this argument is needed
    * nargs='+' : Accepts multiple argument(python arg.py 1234 2345)
    * nargs='?' : At most one argument or default value will be consumed from the command line if possible
    * nargs=argparse.REMAINDER : parse all leftover
    * choices=['rock', 'paper', 'scissors']
  * parse_args()
  * parse_known_args() : Only parse predefined options

> fire

{% tabs %}
{% tab title='fire.py' %}

```py
import fire

class ParseClass:
  def __init__(self, offset):
    self.offset = 3

  # python fire_class.py ParseClass add 10 20 --offset=0
  def add(self, x, y):
    return self.offset + x + y

  def add_list(self, li):
    return sum(li)

if __name__ == "__main__":
  fire.Fire(ParseClass)

# python fire_class.py add --x 1 --y 2
# python fire_class.py add_list "[1,2,6,54]"
```

{% endtab %}
{% endtabs %}

### Package

> pkg_resources

{% tabs %}
{% tab title='update_packages.py' %}

```py
from subprocess import call
packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip3 install --upgrade " + ' '.join(packages), shell=True)
```

{% endtab %}
{% endtabs %}

> setuptools

{% tabs %}
{% tab title='publish.py' %}

```py
from setuptools import setup

def readme():
  with open('README.md') as f:
    README = f.read()
  return README

setup(
  name="robotcar",
  version="1.0.0",
  description="robotcar simulator package for education",
  long_description=readme(),
  author="UCSD Robotic Lab",
  author_email="g5hwang@ucsd.edu",
  license="MIT",
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
  ],
  packages=["robotcar"],    # which file should be imported
  include_package_data=True,
  install_requires=["cv2"],
)

# Publish
packages=[package for package in find_packages() if package.startswith('gym')],

# python3 setup.py sdist bdist_wheel
# twine upload --repository-url https://test.pypi.org|legacy| dist|* --skip-existing
# twine upload --repository-url https://upload.pypi.org|legacy| dist|* -r https://www.python.org/pypi
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title='main.py' %}

```py
# python3 setup.py build && python3 setup.py install
# python3 main.py

from threading import Thread
import spam

groups = []
for i in range(5):
  groups.append([str(val) for val in range(i)])

threads = [Thread(target=spam.print_list, args=(group,)) for group in groups]
[t.start() for t in threads]
[t.join() for t in threads]
```

{% endtab %}
{% tab title='setup.py' %}

```py
import os
from setuptools import setup, Extension

module = Extension('spam', sources=['spammodule.cpp', 'cprint_list.cpp'], include_dirs=['.'], language='c++')

setup(name='spam', ext_modules=[module])
```

{% endtab %}
{% tab title='spammodule.cpp' %}

```cpp
#include <Python.h>
#include <cprint_list.hpp>

static PyObject *print_list(PyObject *self, PyObject *args)
{
  PyObject *lobj;
  /* Verify that the argument is a list. */
  if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &lobj))
    return NULL;

  /* Verify that each member of the list is of type str. */
  for (unsigned int i = 0; i < PyList_Size(lobj); ++i)
  {
    if (!PyUnicode_Check(PyList_GetItem(lobj, i)))
    {
      PyErr_SetString(PyExc_TypeError, "must pass in list of str");
      return NULL;
    }
  }
  /* Convert python object to a "natural C++ object" */
  std::vector<std::string> strings;
  for (unsigned int i = 0; i < PyList_Size(lobj); ++i)
    strings.push_back(PyUnicode_AsUTF8(PyList_GetItem(lobj, i)));

  Py_BEGIN_ALLOW_THREADS /* <-------- HERE WE RELEASE THE GIL */
    cprint_list(strings);
  Py_END_ALLOW_THREADS /* <---------- HERE WE ACQUIRE THE GIL */
    Py_RETURN_NONE;
}

static PyMethodDef SpamMethods[] = {
  {"print_list", print_list, METH_VARARGS,
    "A function that prints a list of strings."},
  {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef spammodule = {
  PyModuleDef_HEAD_INIT,
  "spam",        /* name of module */
  "spam module", /* module documentation */
  -1,
  SpamMethods};

PyMODINIT_FUNC
PyInit_spam(void) {
  PyObject *m = PyModule_Create(&spammodule);
  if (m == NULL)
    return NULL;
  return m;
}
```

{% endtab %}
{% tab title='cprint_list.cpp' %}

```cpp
#include <cprint_list.hpp>

#include <iostream>

#include <unistd.h>
#include <pthread.h>

pthread_mutex_t lock; /* <----------------- HERE IS OUR LOCK! */

void cprint_list(const std::vector<std::string> &strings) {
  sleep(1);
  pthread_mutex_lock(&lock); /* <-------- HERE WE ACQUIRE THE LOCK */
  for (const auto &str : strings)
    std::cout << str << " ";
  std::cout << "\n";
  pthread_mutex_unlock(&lock); /* <------ HERE WE RELEASE THE LOCK */
}
```

{% endtab %}
{% endtabs %}

> disutil

* MANIFEST.in
  * text files that contain a series of “commands” in a Distutils-defined format

* setup()
  * [Required]
  * url : the home page of your project. (can be PyPI package page)
  * name : the name of the package.
  * author : your full name.
  * version : the version number of the package.
  * author_email : your email address.
  * [Optional]
  * description : one-line summary of the project.
  * long_description : multi-line string in reStructuredText format. (PyPI converts to html and displays in package page)
  * classifiers : a list of specially-formatted strings

{% tabs %}
{% tab title='classifier' %}

```txt
Programming Language :: Python
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Development Status :: 5 - Production/Stable
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Dynamic Content
Topic :: Internet :: WWW/HTTP :: WSGI
Topic :: Software Development :: Libraries :: Python Modules
```

{% endtab %}
{% endtabs %}

> importlib

* reload(module) : previously imported module
* find_loader(name, path=None) : sys.modules[name].__loader__ is returned
* import_module(name, package=None)

* > js2py

{% tabs %}
{% tab title='js2py.py' %}

```py
import js2py

code = " function test(a, b) { return a + b; } "
js_func = js2py.eval_js(code)
print(js_func(1, 2))
```

{% endtab %}
{% endtabs %}

> pipreqs

* Auto generate requirements.txt file for any project based on imports

{% tabs %}
{% tab title='cli.sh' %}

```text
$ pipreqs /home/project/location

Usage:
  pipreqs [options] <path>

Options:
  --use-local           Use ONLY local package info instead of querying PyPI
  --pypi-server <url>   Use custom PyPi server
  --proxy <url>         Use Proxy, parameter will be passed to requests library. or environments parameter in your terminal:
              $ export HTTP_PROXY="http://10.10.1.10:3128" HTTPS_PROXY="https://10.10.1.10:1080"
  --debug               Print debug information
  --ignore <dirs>...    Ignore extra directories
  --encoding <charset>  Use encoding parameter for file open
  --savepath <file>     Save the list of requirements in the given file
  --print               Output the list of requirements in the standard output
  --force               Overwrite existing requirements.txt
  --diff <file>         Compare modules in requirements.txt to project imports.
  --clean <file>        Clean up requirements.txt by removing modules that are not imported in project.
  --no-pin              Omit version of output packages.
```

{% endtab %}
{% endtabs %}

### Time

> datetime

{% tabs %}
{% tab title='datetime.py' %}
```py
from datetime import date, datetime, timedelta

print(f"strftime \t {d.}")
print(f"timedelta \t {d - timedelta(days=1, hours=0, minutes=50)}")
```

{% endtab %}
{% endtabs %}

* DateTime
  * datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
  * end_date = date_1 + datetime.timedelta(days=10) : add date to datetime

* date
  * date(2002, 12, 31)
  * isocalendar() / isoformat() / strftime('%d/%m/%y') : (y, m, d) / (2002-12-31) / (31/12/02)
  * replace(day=26) : replace
  * weekday() : Monday is 0 and Sunday is 6.
  * timedelta(days=1, hours=0, minutes=50) : date - timedelta

* Time
  * replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])
  * strftime("%H:%M:%S %Z")
  * min : time(0, 0, 0, 0)
  * max : time(23, 59, 59, 999999)

> time

* time.perf_counter() / _ns : clock with highest available resolution to measure a short duration
* tm_zone : EDT, EST
* time() / time_ns() / ctime() : time in ms / nice format
* gmtime() / localtime() : 0 is struct_time(1970, 1, 1), and none is current time

{% tabs %}
{% tab title="date.py" %}

```py
from datetime import date, datetime

today = date.today()
print(today.strftime("%d/%m/%Y"))  # dd/mm/YY
print(today.strftime("%B %d, %Y")) # Textual month, day and year
print(today.strftime("%m/%d/%y"))  # mm/dd/y
print(today.strftime("%b-%d-%Y"))  # Month abbreviation, day and year
print(datetime.now())              # datetime object containing current date and time
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))   # dd/mm/YY H:M:S
```

{% endtab %}
{% tab title="timer_context.py" %}

```py
class Time:
  def __init__(self, f):
  self.func = f

  def __call__(self, *args, **kwargs):
  cur = time.perf_counter()
  print(cur)   # 185.006554938
  self.func(*args, **kwargs)
  print(f"Took {time.perf_counter() - cur:.3f}s")

@Time
def complex():
  li = []
  for i in range(1000000):
  li.append(i)
  li.sort()

complex()       # Took 0.111s
```

{% endtab %}
{% endtabs %}

### Network

> `<socket>`

{% tabs %}
{% tab title="ip_address.py" %}

```py
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
```

{% endtab %}
{% tab title="tcp_client.py" %}

```py
import socket

host = '127.0.0.1'
port = 5000

def tcp_client():
  s = socket.socket()
  s.connect((host, port))

  while (message := input("->").encode()) != 'q':
  s.send(message)
  data = s.recv(1024)
  print(f"Recieved from server {data}")
  s.close()

def tcp_server():
  s = socket.socket()
  s.bind((host, port))

  s.listen(1)
  c, addr = s.accept()
  print(f"Connection from {addr}")

  while True:
  data = c.recv(1024)
  if not data:
    break
  print(f"message {data} recieved, sending back {data.upper()}")
  c.send(data.upper())
  c.close()
```

{% endtab %}
{% tab title="udp_client.py" %}

```py
import socket

host, port = '127.0.0.1', 5001
server = ('127.0.0.1',5000)

def udp_client():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((host, port))

  while (message := input("-> ").encode()) != 'q':
  s.sendto(message, server)
  data, addr = s.recvfrom(1024)
  print(f'Received from server:{data}')
  s.close()

def udp_server():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((host,port))

  print("Server Started.")
  while True:
  data, addr = s.recvfrom(1024)
  print(f"message {data} recieved from {addr}, sending back {data.upper()}")
  s.sendto(data.upper(), addr)
  c.close()
```

{% endtab %}
{% endtabs %}

> cgi

* dynamically generating web pages that respond to user input

> http.server.HTTPServer

```sh
python3 -m http.server
serve_forever()
```

> urllib

* Request
  * urllib2.Request("www.example.com")
  * add_header('Referer', 'http://www.python.org/')
  * urlopen(url) : string / Request object.  For HTTP, returns http.client.HTTPResponse object

* parse
  * unquote(str) : decode urlencoded bytes

* HTTPResponse
  * content = resp.read()

{% tabs %}
{% tab title='multithreading_image.py' %}

```py
import time
import urllib.request
import multiprocessing as mp
import concurrent.futures

""" Returns: total bytes from downloading all images in image_numbers list """
def seq_download_images(image_numbers):
  total_bytes = 0
  for num in image_numbers:
  total_bytes += _download_image(num)
  return total_bytes

def _download_image(image_number):
  image_number = (abs(image_number) % 50) + 1  # force between 1 and 50
  image_url = 'http://699340.youcanlearnit.net/image{:03d}.jpg'.format(image_number)
  try:
  with urllib.request.urlopen(image_url, timeout=60) as conn:
    return len(conn.read())  # number of bytes in downloaded image
  except Exception as e:
  print(e)

def par_download_images(image_numbers):
  total_bytes = 0
  with concurrent.futures.ThreadPoolExecutor() as pool:
  futures = [pool.submit(_download_image, num) for num in image_numbers]
  for f in concurrent.futures.as_completed(futures):
    total_bytes += f.result()
  return total_bytes

if __name__ == '__main__':
  IMAGE_NUMBERS = list(range(1, 50))

  print('Evaluating Sequential Implementation...')
  sequential_result = seq_download_images(IMAGE_NUMBERS)
  sequential_time = 0
  start = time.perf_counter()
  seq_download_images(IMAGE_NUMBERS)
  sequential_time += time.perf_counter() - start

  print('Evaluating Parallel Implementation...')
  parallel_result = par_download_images(IMAGE_NUMBERS)
  parallel_time = 0
  start = time.perf_counter()
  par_download_images(IMAGE_NUMBERS)
  parallel_time += time.perf_counter() - start

  if sequential_result != parallel_result:
  raise Exception('sequential_result and parallel_result do not match.')
  print('Average Sequential Time: {:.2f} ms'.format(sequential_time*1000))
  print('Average Parallel Time: {:.2f} ms'.format(parallel_time*1000))
  print('Speedup: {:.2f}'.format(sequential_time | parallel_time))
  print('Efficiency: {:.2f}%'.format(100*(sequential_time | parallel_time) | mp.cpu_count()))
```

{% endtab %}
{% tab title='coco.py' %}

```py
import sys, getopt
import fire
import json
import requests

def download_factory(all = False, *, coco2014 = None, coco2017 = None):
  if all or coco2014:
    url = "http://images.cocodataset.org/annotations/annotations_trainval2014.zip"
    download(url)

  if all or coco2017:
    url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
    download(url)

def download(url):
  response = requests.get(url, stream=True)
  total_bytes = int(response.headers.get('content-length', 0))
  with open('test.dat', 'wb') as file:
    with tqdm(total=total_bytes / (32*1024.0), unit='B', unit_scale=True, unit_divisor=1024) as pbar:
      for data in response.iter_content(1024):
        pbar.update(len(data))
        file.write(data)
```

{% endtab %}
{% endtabs %}

### Automation

> python-pptx

{% tabs %}
{% tab title='PPT_class.py' %}

```py
class PPT:

  def __init__(self, layout=[12192000, 6858000]):     # 13.33, 7.5 inches
    self.layout = layout
    if os.path.exists('template.pptx'):
      self.prs = Presentation('template.pptx')    # template file with "browsed by individual window" turned on
      rId = self.prs.slides._sldIdLst[0].rId
      self.prs.part.drop_rel(rId)
      del self.prs.slides._sldIdLst[0]
    else:
      self.prs = Presentation()                   # starting from default settings
    self.prs.slide_width, self.prs.slide_height = layout

  def create_verse(self, sermon):     # Bible.pptx format (verses and hyperlinks)
    self.add_slide()                # create title slide
    if '"' in sermon.title:
      self.add_textbox(sermon.title, [1.67, 0.08, 10, 1.2], 26, spacing=1.1)
    else:
      self.add_textbox('"' + sermon.title + '"', [1.67, 0.08, 10, 1.2], 26, spacing=1.1)
    self.add_paragraph('(' + sermon.passages_raw[0] + '/ ' + sermon.preacher + ')', 24)

    p = self.add_verse_slides(sermon.passages_ext, 'p')     # add verses in main passage
    q = self.add_verse_slides(sermon.quotes_ext, 'q')       # add verses to quote

    for slide in self.prs.slides:
      self.slide = slide
      self.add_link_table(p + q)  # add hyperlink table

  def create_large(self, sermon):     # Large.pptx format
    self.add_large_slides(sermon, sermon.passages_ext, 7)

  def add_slide(self):                # create new blank slide
    self.slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
```

{% endtab %}
{% endtabs %}

> pyautogui

* pyautogui.mouseInfo() : get RGB from mouse
* pyautogui.pixel(28, 18) : get RGB from pixel

* Box
  * left, top, width, height

* locateOnScreen
  * region=(x, y, width, height)
  * greyscale=True
  * confidence=0.9 (pip install opencv-python)

{% tabs %}
{% tab title='locate.py' %}

```py
file_loc = pyautogui.locateOnScreen("file_menu.png") # Get location on certain image, None if not exists
pyautogui.moveTo(file_loc)
pyautogui.click(file_loc)

# Multiple images
for file_loc in pyautogui.locateAllOnScreen("file_menu.png"):
  pyautogui.click(i, duration=0.25)

# With timeout
file_location = None
while not file_location:
  file_location = pyautogui.locateOnScreen("file_menu.png")
  end = time.time()
  if end - start > timeout:
  print("timout")
  sys.exit()
```

{% endtab %}
{% endtabs %}

### Test

> coverage

* pip install coverage
* coverage CLI
  * run --source="." manage.py test : for django
  * report

> unittest

* @skip

* setUp(self) : Executed before each test
* tearDown(self) : Executed after each test method
* test_name(self) : test_* will run sequentially

* assertIn : Check string in string
* fail : Fails test

{% tabs %}
{% tab title='hello.py' %}

```py
import unittest

class TestAll(unittest.TestCase):
  def setUp(self):
    pass

  def test_doc(self):
    self.assertIsNotNone("1")

  def tearDown(cls):
    pass  # use line_profile

if __name__ == "__main__":
  # run single test
  suite = unittest.TestSuite()
  suite.addTest(PageTester("test_doc"))
  runner = unittest.TextTestRunner()
  runner.run(suite)

  # run whole test
  unittest.main()
```

{% endtab %}
{% tab title='connection.py' %}

```py
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # She is invited to enter a to-do item straight away
    # [...rest of comments as before]

if __name__ == '__main__':
  unittest.main()
```

{% endtab %}
{% endtabs %}

### Web

> http.server

* python -m http.server --cgi 8000

> httpie

* http http://127.0.0.1:8000/test

> jinja

* string
  * capfirst
  * {{ var | default(5) }} : 5 if not set
  * {{ var | isnan }}
  * {{ var | log }}
  * {{ var | pow(2) }}
  * {{ var | root }}
  * {{ var | ipaddr }} : check if var is ipaddr
  * {{ var | ipv6 }} : check if
  * {{ "C style" | comment('c') }}
  * {% |reverse %}

* load
  * {% load A %}
  * {% A 'images/logo.png' %}
  * {% extends "base.html" %} : substitute A block in base.html

{% tabs %}
{% tab title='conditional.html' %}

```py
{% if title %} {% else %} {% endif %}
{% if ( (foo == 'foo' or bar == 'bar') and (fo == 'fo' or ba == 'ba') ) %}
```

{% endtab %}
{% endtabs %}

* list
  * {{ value|last }} : last element

* set
  * {{ list1 | unique }} : To get a unique set from a list:
  * {{ list1 | union(list2) }} : To get a union of two lists
  * {{ list1 | intersect(list2) }} : unique list of all items in both
  * {{ list1 | difference(list2) }} : items in 1 that don’t exist in 2
  * {{ list1 | symmetric_difference(list2) }} : list1 - list2

{% tabs %}
{% tab title='login_check.html' %}

```html
{% if current_user and current_user.id %}
  <a class="btn" style="display:inline">Hi {{ current_user.id }} </a>
  <a class="btn content-login-link" href="/signout">Sign out</a>
{% if current_user.class_id == "" %}
  <a class="btn content-login-link" href="/premium">Premium</a>
{% endif %}
{% else %}
  <a class="btn content-login-link" href="{{ url_for('signin') }}">Sign in</a>
{% endif %}
```

{% endtab %}
{% endtabs %}

* {% csrf_token %} : in django

> bs4

* from bs4 import BeautifulSoup

* name : tagname
* text, attrs : inside text, attribute object
* next / previous_elements : next / previous tags generator
* next / previous_siblings : next sibling tags generator
* original_encoding

* bs4.element.Tag
  * string
  * text
  * clear() : removes the contents of a tag:
  * decompose() : remove tag
  * extract() : hide element
  * find_all(tag, href=None, limit=None) → [Tags] : find all matching tags
  * find("span") : find tags inside
  * get_text() :
  * insert(pos, tag) : insert tag to position
  * insert_before() / after() : immediately before
  * prettify()
  * wrap(soup.new_tag("b")) : wrap around new tags
  * new_button = soup.new_tag('a')
  * new_button.attrs["onclick"] = "toggle()"
  * new_button.append('This is a new button!')

{% tabs %}
{% tab title='multifile_gist_toggle.py' %}

```py
import requests
import re
from ..common import PATH, logger, git_credential
from bs4 import BeautifulSoup
from itertools import islice
from concurrent.futures import ThreadPoolExecutor, as_completed

class Gist:
  def __init__(self, gist_id="", h1="", h2='', h3='', li='', link='', file_names=None, html='', problem_id=''):
  self.gist_id = gist_id
  self.h1 = h1
  self.h2 = h2
  self.h3 = h3
  self.li = li
  self.link = link
  self.file_names = file_names or []
  self.html = html
  self.problem_id = problem_id

  def __repr__(self):
  return f"{self.__dict__}"

  @classmethod
  def get_gist(cls, gist_id, h1="", h2="", h3="", li=""):
  gist = cls(gist_id, h1, h2, h3, li, f"<a href=https://gist.github.com/SeanHwangG/{gist_id}>{gist_id}</a>")
  result = requests.get(f'https://gist.github.com/{gist_id}.js', headers=git_credential)

  if result.text.startswith("<!DOCTYPE html>"):
    return None
  # update with regex
  result = result.text.replace("\\\\n", "[NEW_LINE]").replace("\\n", "\n").replace("[NEW_LINE]", "\\n")
  result = re.sub(r"\\(/|&|\$|<|`|\"|\\|')", r"\1", result)
  result = result.split("document.write('")[-1][:-3]

  bs = BeautifulSoup(result, "html.parser")

  for tag in bs.find_all(class_="gist"):
    file_box = tag.find(class_="file-box")
    root = tag.find(class_="file-box")
    toggle_div = bs.new_tag('div', attrs={"class": "gist-meta"})

    for i, d in enumerate(tag.find_all(class_="file")):
    d["class"] = f"file gist-id-{gist_id}"
    if i != 0:
      file_box.append(d)  # combine to first table

    for d in tag.find_all(class_="gist-meta"):
    siblings = list(d.next_elements)
    file_id, file_name = siblings[4].attrs["href"].split("#")[-1], siblings[5]
    toggle_a = bs.new_tag('a', attrs={"id": file_id, "class": f"gist-toggler gist-id-{gist_id}", "onclick": f"toggle('gist-id-{gist_id}', '{file_id}')", "style": "padding: 0 18px"})
    toggle_a.append(file_name)
    toggle_div.append(toggle_a)
    d.extract()  # remove bottom nav
    edit_gist = bs.new_tag('a', attrs={"class": f"edit-gist", "href": f"https://gist.github.com/{gist_id}", "style": "float: right"})
    edit_gist.append("edit")
    toggle_div.append(edit_gist)

    root.insert(0, toggle_div)
    for d in islice(tag.find_all(class_="gist-file"), 1, None):
    d.extract()  # remove except first
  gist.html = str(bs)

  return gist

  @staticmethod
  def get_all_gist(gist_ids, h1="", h2="", h3="", li=""):
  logger.debug(f"get_all_gist({h1}, {h2}, {h3}, {li})")
  futures = []
  with ThreadPoolExecutor() as ex:
    futures.extend([ex.submit(Gist.get_gist, gist_id, h1, h2, h3, li) for gist_id in gist_ids])
  gists = [future.result() for future in as_completed(futures)]
  return [gist for gist in gists if gist != None]
```

{% endtab %}
{% endtabs %}

> requests

* json() : convert back to

{% tabs %}
{% tab title='clone_gist_process.py' %}

```py
import json
import subprocess as sp
import requests
import os
from itertools import islice
from math import ceil

def clone_all(username='seanhwangg', clone_path):
  current_count, total_count = 0, 1000
  git_cred = get_git_credential()

  for i in range(ceil(total_count / 100)):
  pid2popen = {}
  result = requests.get(f'https://api.github.com/users/{username}/gists?page={i}&per_page={100}', headers=git_cred)
  gists = json.loads(result.content)

  loop_count = min(total_count - current_count, len(gists))
  current_count += loop_count

  for g in islice(gists, loop_count):
    url, gist_path = f"https://gist.github.com/{g['id']}.git", f"{clone_path}/{g['id']}"
    if os.path.isdir(gist_path):
    p = sp.Popen(['git', '-C', gist_path, 'pull', url], stdout=sp.PIPE, stderr=sp.PIPE)
    else:
    p = sp.Popen(['git', 'clone', url, f"{clone_path}/{g['id']}"], stdout=sp.PIPE, stderr=sp.PIPE)
    pid2popen[gist_path] = p
  for gist_path, p in pid2popen.items():
    out, err = p.communicate()
    file2content = {}
    for file in os.listdir(gist_path):
    if not os.path.isdir(f"{gist_path}/{file}"):
      with open(f"{gist_path}/{file}", 'r') as f:
      file2content[file] = f.read().split('\n')
  return file2content
```

{% endtab %}
{% endtabs %}

> selenium

{% tabs %}
{% tab title='baekjoon.py' %}

```py
import multithreading as mt
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def update_problems(*, update_page=None, update_level=None):
  if update_level:
  with mt.Pool(16) as pool:
    levels = pool.map(get_problems_level, range(0, 31))
  problems = [problem for level in levels for problem in level]
  else:
  with open(f"{PATH.DATA}/problems.json", 'r') as f:
    problems = json.load(f)

  with open(f"{PATH.DATA}/problems.json", 'w') as f:
  json.dump(problems, f, ensure_ascii=False)


def get_problems_level(level):
  problems = []
  chrome_options = Options()
  chrome_options.add_argument('headless')
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
  try:
  level_problems = []
  for page in range(1, 100):
    driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
    lines = driver.find_element_by_class_name('contents').text
    if '해당하는 문제가 없습니다' in lines:
    break
    for line in lines.split('\n'):
    level_problems.extend(re.findall(r'^ (\d+)', line))
  for problem in level_problems:
    problems.append({'id': f"BJ_{problem}", 'level': level})
  except Exception:
  driver.quit()
  else:
  driver.quit()
  return problems
```

{% endtab %}
{% tab title='leetcode_solvedac.py' %}

```py
import json
import re
import os
from ..common import PATH, logger,  get_chrome_driver
from itertools import islice, chain
from firebase_admin import credentials, firestore, initialize_app
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class Problem():
  def __init__(self, problem_id="", title="", level="", link="", category_id="", solution_link=""):
    self.problem_id = problem_id
    self.title = title
    self.level = level
    self.link = link
    self.category_id = category_id
    self.solution_link = solution_link

  def __repr__(self):
    return f"{self.problem_id}"

  @classmethod
  def get_baekjoon_problems_level(cls, level):
    logger.debug(f"get_baekjoon_problems_level({level})")
    driver = get_chrome_driver()
    problems = []
    try:
      id_title = []
      for page in range(1, 100):
        driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
        logger.debug(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
        lines = driver.find_element_by_class_name('contents').text
        if '해당하는 문제가 없습니다' in lines:
          break
        for line in lines.split("\n"):                      # ex)
          line = line.strip("STANDARD").strip()             # 10430 나머지 계산 STANDARD -> 10430 나머지 계산
          id_title = line.split(' ', 1)                     # 10430 나머지 계산 -> [10430, 나머지 계산]
          if id_title[0].isdigit() and len(id_title) == 2:
            id, title = id_title
            problem_id = f"BJ_{id}"
            link = f'<a href="http://acmicpc.net/problem/{id}" style="color:blue;">{problem_id} {title} ({level})</a>'
            problem = cls(problem_id, title, level, link)
            problems.append(problem)
    except Exception as e:
      logger.warn(e)
    finally:
      driver.quit()
    return problems

  @classmethod
  def get_baekjoon_problems(cls, lo=0, hi=31):
    logger.debug(f"update_baekjoon_problems({lo}, {hi})")
    problems = []
    with ThreadPoolExecutor() as ex:
      future2level = {ex.submit(Problem.get_baekjoon_problems_level, level): level for level in range(lo, hi)}
      for future in as_completed(future2level):
        problems.extend(future.result())
    return problems

  @classmethod
  def get_leetcode_problems(cls, total_count=10000):
    logger.debug(f"update_leetcode({total_count})")
    driver = get_chrome_driver()
    problems = []
    try:
      driver.get(f"https://leetcode.com/problemset/all/")

      select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'select'))))
      select.select_by_visible_text('all')
      WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

      data = driver.find_element_by_class_name("reactable-data").find_elements_by_tag_name("tr")
      for prob in islice(data, total_count):
        id, title, level = prob.text.split('\n')
        level = {"Easy": 1, "Medium": 2, "Hard": 3}[level[level.find(' ') + 1:]]
        link = prob.find_element_by_css_selector("a").get_attribute('href')
        link = f'<a href="{link}" style="color:blue;">{title} ({level})</a>'
        problem = cls(f"LC_{id}", title, level, link)
        logger.debug(f"{id} {title}")
        problems.append(problem)
    except Exception as e:
      logger.error(e)
    finally:
      driver.quit()
    return problems
```

{% endtab %}
{% endtabs %}

> Errors

* DevToolsActivePort file doesn't exist
  * chrome_options.add_argument("--single-process")

> livereload

* gh repo clone nathanwright1242/flask_livereload_example

> algolia

* full-text search

* client
  * SearchClient.create('key', 'cred') : create client

* index
  * client.init_index('page') : create index
  * clear_objects() : remove all objects
  * save_objects()

> eb

* pip install awsebcli
* eb cli
  * creathttps://github.com/SeanHwangG/notee
  * init : Create new application

## Algorithm

> bisect

* bisect_left(`nums`, `x`) : first insert point for x in `nums` to maintain sorted order
* bisect_right(`nums`, `x`) : last insert point for x in `nums` to maintain sorted order
  * lo=0, hi=len(a) : set where to start, end in array

> decimal

{% tabs %}
{% tab title='concise.py' %}

```py
import decimal
decimal.getcontext().prec = 5000
decimal.Decimal(0.999592935235).sqrt()
```

{% endtab %}
{% endtabs %}

> heapq

* smallest element is always the root
* If you want to use max heap, multiply by -1
* heappush(heap, item)
* heappop(heap)
* heapify(x) : Transform list x into a heap, in-place, in linear time
* merge(*iterables, key=N, reverse=F) : Merge sorted inputs into a single sorted output
* nlargest(n, iterable, key=N) : return n th largest index and number
* nsmallest(n, iterable, key=N)

{% tabs %}
{% tab title='print_order.py' %}

```py
heapify lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
heapify(lst)    # [0, 1, 3, 2, 5, 4, 7, 9, 6, 8]
heappush(lst, 10)
for i in range(k):
  ans = heapq.heappop(lst)
```

{% endtab %}
{% endtabs %}

> io

* StringIO()

> math

* [round](https://docs.google.com/forms/d/19Hzj2ohcfL9cT4QnrDVvd89YTPj_a8z53KNOM-55ZlE/edit)
* [combination](https://docs.google.com/forms/d/1AeV7i1ky3EHT0ap8SStwHDkQiBmrlG8w2hXDEOQrh_c/edit)

* ceil(x)
  * ceiling of x, smallest integer greater than or equal to x. If x is not a float, use x.__ceil__(), which should return int.
* comb(n, k)
  * number of ways to choose k items from n items without repetition and without order.

> traceback

* print_exc()
* format_exc()

{% tabs %}
{% tab title='error_stack.py' %}

```py
import traceback
try:
  raise TypeError("Oups!")
except Exception, err:
  try:
    raise TypeError("Again !?!")
  except:
    pass
  traceback.print_exc()
  var = traceback.format_exc()
  print(var)
```

{% endtab %}
{% endtabs %}

### Collections

* Search and insert
  * O(N) due to insert
  * bisect.insort(a, x, lo=0, hi=len(a))

>  collections.Counter

* subclass of dict
* [Counter](https://docs.google.com/forms/d/1m1F3h8PzaSuVO6rqFZko9amMXTo_-NNj1UdfiD5ihGU/edit)
  * elements() : iterator over elements repeating count | ignore if less than one
  * most_common([k]) : Return k most common key value pair in order in O(n log k)
  * subtract([iterable-or-mapping]) : Subtract another mapping
  * update([iterable-or-mapping]) : Add another mapping

{% tabs %}
{% tab title='Counter.py' %}

```py
from collections import Counter

# Create
Counter()
Counter('gallahad')            # new counter from an iterable
Counter({'red': 4, 'blue': 2}) # new counter from a mapping
Counter(cats=4, dogs=8)        # keyword args

co['a'] += 1      # update
del c['sausage']  # remove
```

{% endtab %}
{% endtabs %}

> collections.defaultdict

* subclass of dict
* vs setdefault: When look up a missing key, do you want an empty list, or a KeyError

> collections.ordereddict

* popitem(last=True)
* move_to_end(key, last=True)

{% tabs %}
{% tab title='ordereddict.py' %}

```py
OrderedDict(sorted(dictitems(), key=lambda t: t[0]))  # LRU

from collections import OrderedDict
def align_with_list(dic, li):
  print(OrderedDict([(el, dic[el]) for el in li]))    # OrderedDict([('sandwich', 'C'), ('potato', 'A'), ('tomato', 'B')])
align_with_list({'potato':'A', 'tomato':'B', 'sandwich':'C'}, ['sandwich', 'potato', 'tomato'])
```

{% endtab %}
{% endtabs %}

> collections.deque

* [deque](https://docs.google.com/forms/d/12yDxm3jPOLbyR8Fc9dJ-6yOGz9arfs-iVIiA1s_mTlM/edit)
* deque([iterable[, maxlen]]) : if deque is full and item added, item is discarded on other side
  * append(`x`) : Add `x` to the right side of the deque
  * appendleft(`x`) : Add `x` to the left side of the deque
  * clear() : Remove all elements from the deque leaving it with length 0
  * copy() : Shallow copy of the deque
  * count(`x`) : Number of deque elements equal to `x`
  * extendleft(`iterable`) : insert multiple `iterable` into left
  * full() : Return True if the queue is full
  * index(`x`[, start[, stop]]) : Position of `x` in the deque
  * insert(i, x) : Index error if full
  * pop() : Remove and return an element from the right
  * popleft() : Remove and return an element from the left
  * remove(value) : Remove the first occurrence of value
  * reverse() : Reverse elements of the deque in-place
  * rotate(n=1) : Rotate the deque n steps to the right
  * extend(iterable) : Extendleft(iterable)

{% tabs %}
{% tab title='deque.py' %}

```py
# linux tail
def tail(filename, n=10):
  with open(filename) as f:
    return deque(f, n)
```

{% endtab %}
{% endtabs %}

### Concurrency

* Global Interpreter Lock is a mutex that allows one thread to hold the control of Python interprete
* Does GIL have a negative impact on multi-threaded, I|O-bound programs?
  * IO-bound tasks spend most of their time waiting on external actions - network operations or user input
  * Which doesn’t require GIL while waiting, so the GIL has a minimal impact on IO-intensive application

> concurrent.futures

* ProcessPoolExecutor(initializer=init_globals, initargs=(counter,))
* submit(fn) : returns Future object
* shutdown(wait=True) : free using resources when currently pending futures are done executing
* cancel()
* cancelled()
* running()
* done()
* result() : returns the value returned by the call

* concurrent.futures.ThreadPoolExecutor
  * Useful for IO-bound tasks
  * reuse threads to reduce required overhead to create a new, separate thread for every concurrent task
  * default ThreadPoolExecutor creates up to five times as many threads as processors in the system
  * shutdown(wait=True) : Free up ThreadPoolExecutor resources after pending tasks finish

{% tabs %}
{% tab title='parallel_sum.py' %}

```py
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp
import time

def seq_sum(lo, hi):
    return sum(range(lo, hi))

def par_sum(lo, hi, pool=None):
    if not pool:
        with ProcessPoolExecutor() as executor:
            futures = par_sum(lo, hi, pool=executor)
            return sum(f.result() for f in as_completed(futures))
    else:
        if hi - lo <= 1000000:
            return [pool.submit(sum, range(lo,hi))]
        else:
            mi = (hi + lo) // 2
            lo = par_sum(lo, mi, pool=pool)
            hi = par_sum(mi, hi, pool=pool)
            return lo + hi

if __name__ == '__main__':
    NUM_EVAL_RUNS = 1
    SUM_VALUE = 100000000

    print('Evaluating Sequential Implementation...')
    sequential_result = seq_sum(1, SUM_VALUE) # "warm up"
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_sum(1, SUM_VALUE)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print(f'Evaluating Parallel Implementation... {mp.cpu_count()}')
    parallel_result = par_sum(1, SUM_VALUE)   # "warm up"
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_sum(1, SUM_VALUE)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    assert sequential_result == parallel_result, 'sequential_result and parallel_result do not match.'
    print(f'Average Sequential Time: {sequential_time*1000:.2f} ms')
    print(f'Average Parallel Time: {parallel_time*1000:.2f} ms')
    print(f'Speedup: {sequential_time / parallel_time:.2f}')
    print(f'Efficiency: {(sequential_time / parallel_time) / mp.cpu_count():.2%}')
Evaluating Sequential Implementation...
Evaluating Parallel Implementation... 16
Average Sequential Time: 2069.46 ms
Average Parallel Time: 561.73 ms
Speedup: 3.68
Efficiency: 23.03%
```

{% endtab %}
{% endtabs %}

> psutil

* cpu_count()
* ps.memory_info()[0] / 1024 / 1024)

> shlex

* split(command_line) : split command line into list

> signal

{% tabs %}
{% tab title="timeout_signal.py" %}

```py
import sys
import signal

count = 0

def handler(signum, frame):
  print(f"1 sec passed \t {count}")
  sys.exit(0)

signal.signal(signal.SIGINT, lambda sn, f: print("CTRL+C Pressed"))
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
while True:
  count += 1
print(count)
```

{% endtab %}
{% tab title="timeout_decorator.py" %}

```py
import signal
import os
import errno
import time
from functools import wraps

def timeout(seconds, error_message=os.strerror(errno.ETIME)):
  def decorator(func):
    def _handle_timeout(signum, frame):
      raise Exception(f"Took longer than {seconds}s")

    def wrapper(*args, **kwargs):
      signal.signal(signal.SIGALRM, _handle_timeout)
      signal.alarm(seconds)
      try:
      result = func(*args, **kwargs)
      finally:
      signal.alarm(0)
      return result

    return wraps(func)(wrapper)
  return decorator

@timeout(1)
def fast_function():
  time.sleep(0.5)
  print("hello")


@timeout(1)
def slow_function():
  time.sleep(2)
  print("heeeeeeello")
```

{% endtab %}
{% tab title="timeout_context.py" %}

```py
import contextlib
import errno
import os
import signal
import time

class timeout(contextlib.ContextDecorator):
  def __init__(self, seconds, *, timeout_message=os.strerror(errno.ETIME), suppress_error=False):
  self.seconds = seconds
  self.timeout_message = timeout_message
  self.suppress_error = suppress_error

  def _timeout_handler(self, signum, frame):
  raise TimeoutError(self.timeout_message)

  def __enter__(self):
  signal.signal(signal.SIGALRM, self._timeout_handler)
  signal.alarm(self.seconds)

  def __exit__(self, exc_type, exc_val, exc_tb):
  signal.alarm(0)
  if self.suppress_error and exc_type is TimeoutError:
    return True


with timeout(1):
  time.sleep(0.5)
  print("hello")

with timeout(1):
  time.sleep(2)
  print("heeeello")
```

{% endtab %}
{% endtabs %}

> Multiprocessing

* new process has __mp_main__
* used for CPU intensive tasks

* cpu_count() : total number of cpu
* join() : Wait worker processes to exit, must call close|terminate()
* imap / map(func, iterable[, chunksize]) : use imap to lower memory usage for long iterables
* starmap(func, iterable[, chunksize]) : [(1,2), (3, 4)] ⇒ [func(1,2), func(3,4)]

* Process
  * pid : Return the process ID.
  * Process(target=f)
  * start()
  * join([timeout]) : method blocks until the process whose join() method is called terminates

* RawArray
  * Raw cannot be synchronized
  * from multiprocessing.sharedctypes import Value, Array

{% tabs %}
{% tab title="matrix_multiply.py" %}

```py
import random
import multiprocessing as mp
import math


def par_matrix_multiply(M1, M2):
  # Multiply two 2d array (Efficient after 300 x 300)
  n1, m1, n2, m2 = len(M1), len(M1[0]), len(M2), len(M2[0])

  num_workers = mp.cpu_count()
  chunk_size = math.ceil(n1 / num_workers)
  C_1D = mp.RawArray('d', n1 * m2)  # flat version of matrix C
  workers = []
  for w in range(num_workers):
  row_start_C = min(w * chunk_size, n1)
  row_end_C = min((w + 1) * chunk_size, n1)
  workers.append(mp.Process(target=_par_worker, args=(M1, M2, C_1D, row_start_C, row_end_C)))
  for w in workers:
  w.start()
  for w in workers:
  w.join()

  C_2D = [[0] * m2 for i in range(n1)]
  for i in range(n1):
  for j in range(m2):
    C_2D[i][j] = C_1D[i*m2 + j]
  return C_2D


def _par_worker(M1, M2, C_1D, row_start_C, row_end_C):
  for i in range(row_start_C, row_end_C):  # subset of rows in M1
  for j in range(len(M2[0])):
    for k in range(len(M1[0])):
    C_1D[i*len(M2[0]) + j] += M1[i][k] * M2[k][j]


if __name__ == '__main__':
  A = [[random.random() for i in range(200)] for j in range(200)]
  B = [[random.random() for i in range(200)] for j in range(200)]
  par_matrix_multiply(A, B)
```

{% endtab %}
{% tab title="mergesort.py" %}

```py
import math
import multiprocessing
import random
import sys
import time

def merge(*args):
  # Support explicit left/right args, as well as a two-item tuple which works more cleanly with multiprocessing.
  left, right = args[0] if len(args) == 1 else args
  left_length, right_length = len(left), len(right)
  left_index, right_index = 0, 0
  merged = []
  while left_index < left_length and right_index < right_length:
  if left[left_index] <= right[right_index]:
    merged.append(left[left_index])
    left_index += 1
  else:
    merged.append(right[right_index])
    right_index += 1
  if left_index == left_length:
  merged.extend(right[right_index:])
  else:
  merged.extend(left[left_index:])
  return merged


def merge_sort(data):
  length = len(data)
  if length <= 1:
  return data
  middle = length // 2
  left = merge_sort(data[:middle])
  right = merge_sort(data[middle:])
  return merge(left, right)


def merge_sort_parallel(data):
  # Split the initial data into partitions, sized equally per worker, and perform a regular merge sort across each partition.
  processes = multiprocessing.cpu_count()
  pool = multiprocessing.Pool(processes=processes)
  size = int(math.ceil(float(len(data)) / processes))
  data = [data[i * size:(i + 1) * size] for i in range(processes)]
  data = pool.map(merge_sort, data)
  # Each partition is now sorted - merge pairs of these together using worker pool, until partitions are reduced down to a single sorted result.
  while len(data) > 1:
  # If partitions remaining is odd, pop off last one and append it back after one iteration of this loop, since pairs need to merge.
  extra = data.pop() if len(data) % 2 == 1 else None
  data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
  data = pool.map(merge, data) + ([extra] if extra else [])
  return data[0]


if __name__ == "__main__":
  size = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 1000
  data_unsorted = [random.randint(0, size) for _ in range(size)]
  for sort in merge_sort, merge_sort_parallel:
  start = time.time()
  data_sorted = sort(data_unsorted)
  end = time.time() - start
  print(sort.__name__, sorted(data_unsorted) == data_sorted)
```

{% endtab %}
{% endtabs %}

> asyncio

* async await → good for IO bound application

{% tabs %}
{% tab title='async_request.py' %}

```py
import aiohttp
import asyncio
import sys
import json
import time
from random import randint

async def worker(n, session):
  url = f"https://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16"
  response = await session.request(method='GET', url=url)
  value = await response.text()
  value = json.loads(value)
  return sum(value['data'])


async def main():
  async with aiohttp.ClientSession() as session:
    sums = await asyncio.gather(*(worker(5, session) for _ in range(20)))
    print(sums)

if __name__ == "__main__":
  start = time.perf_counter()
  asyncio.run(main())
  print(f'Took {time.perf_counter() - start}s')
```

{% endtab %}
{% tab title='async_sleep.py' %}

```py
import asyncio
import sys
import fire
import time
from random import randint


async def db_query(delay):
  await asyncio.sleep(delay)
  return randint(1, 10)


async def main():
  task1 = asyncio.create_task(db_query(1))
  task2 = asyncio.create_task(db_query(2))

  start = time.perf_counter()
  await task1
  await task2
  print(f"{time.perf_counter() - start:.2f} s")

  start = time.perf_counter()
  r = await asyncio.gather(*(db_query(2) for _ in range(1000)))
  print(f"{time.perf_counter() - start:.2f} s") # takes roughly 2 seconds
  print(f"finished at {time.strftime('%X')}")

if __name__ == "__main__":
  asyncio.run(main())
```

{% endtab %}
{% endtabs %}

![](images/20210306_180325.png)

> threading

* Create threads with function or inherit from subclass Thread (__init__, run)
* new threads will inherit daemon status from their parent
* Python thread cannot be turned into a daemon thread after it has been started

* enumerate() : list of all Thread objects currently alive
* current_thread() / main_thread() : current / main Thread (Python interpreter was started)

> Thread class

* Thread(target=f, kwargs={'x': 1}) : kwargs
* is_alive() / isDaemon()
* get_native_id() : Native integral TID of the current thread assigned by kernel
* join(timeout=None) : Wait until thread terminates
* start() : must be called at most once per thread object
* daemon : whether this thread is a daemon
* name : A string used for identification purposes only
* native_id : The native integral thread ID of this thread

{% tabs %}
{% tab title='thread_class.py' %}

```py
import threading
import time

class MyThread(threading.Thread):
  def __init__(self, name, counter):
    threading.Thread.__init__(self)
    self.name = name
    self.counter = counter

  def run(self):
    print("Starting " + self.name)
    while self.counter:
      time.sleep(1)
      print(f"{self.name} {time.ctime(time.time())}")
      self.counter -= 1
    print("Exiting " + self.name)


if __name__ == "__main__":
  thread1 = MyThread("Thread-1", 2)
  thread2 = MyThread("Thread-2", 3)
  thread1.start()
  thread2.start()
  print("Exiting Main Thread")
```

{% endtab %}
{% endtabs %}

* daemon : setting true make it demon

* Lock
  * acquire(blocking=True, timeout=-1)
  * release() : Can be called from any thread, not only thread acquired the lock.
  * locked() : Return true if the lock is acquired

{% tabs %}
{% tab title='buy_list.py' %}

```py
import time
import threading

pencil = threading.Lock()
items_on_notepad = 0

def shopper():
  global items_on_notepad
  name = threading.current_thread().getName()
  items_to_add = 0
  while items_on_notepad <= 20:
    if items_to_add and pencil.acquire(blocking=False): # if blocking is True one write everytime
      print(f"{name} write {items_to_add}, so total become {items_on_notepad}")
      items_on_notepad += items_to_add
      items_to_add = 0
      time.sleep(0.3)
      pencil.release()
    else:
      time.sleep(0.1)
      items_to_add += 1

if __name__ == '__main__':
  sean = threading.Thread(target=shopper, name='sean')
  tom = threading.Thread(target=shopper, name='tom')
  start_time = time.perf_counter()
  sean.start()
  tom.start()
  sean.join()
  tom.join()
  print(f'Elapsed time: {time.perf_counter() - start_time} seconds')
  """
  sean write 1, so total become 0
  tom write 4, so total become 1
  sean write 4, so total become 5
  tom write 4, so total become 9
  sean write 4, so total become 13
  tom write 4, so total become 17
  Elapsed time: 2.104485642630607 seconds
  """
```

{% endtab %}
{% endtabs %}

* semaphore
  * Track the availability of a limited resource.
  * Not thread-safe

```py
Semaphore (counter=1)                # initial value for the internal counter
acquire(blocking=True, timeout=None) # if counter is positive, decrement, otherwise wait
release()                            # increment counter and signal waiting thread

sem = asyncio.Semaphore(10)          # context
async with sem:
which is equivalent to:
await sem.acquire()                  # Equivalent to above
try:
  # work with shared resource
finally:
  sem.release()
```

* Barrier
  * Barrier(parties, action=None, timeout=None)
  * broken
  * parties : n_threads required to pass the barrier
  * n_waiting : n_threads currently waiting in the barrier
  * abort() : Put the barrier into a broken state
  * reset() : Return the barrier to the default
  * wait(timeout=None) : Pass the barrier

{% tabs %}
{% tab title='cpu_waster.py' %}

```py
import os
import threading

def cpu_waster():
  while True:
    pass

print('\n  Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
  print(thread)

for i in range(12):
  threading.Thread(target=cpu_waster).start()

print('\n  Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
  print(thread)

class ThreadSessionFactory:
  def __init__(self, exit_stack):
    self._lock = threading.Lock()
    self._thread_local = threading.local()
    self._exit_stack = exit_stack

  def __call__(self):
    try:
      session = self._thread_local.session
    except AttributeError:
      with self._lock: # ExitStack might not be thread-safe either
        session = self._exit_stack.enter_context(requests.Session())
      self._thread_local.session = session
    return session
```

{% endtab %}
{% endtabs %}

* RLock
  * RWLockFair : fair priority for readers|writers
  * RWLockRead : readers get priority
  * RWLockWrite : writers get priority

{% tabs %}
{% tab title='calender.py' %}

```py
import threading
from readerwriterlock import rwlock

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
marker = rwlock.RWLockFair()

def calendar_reader(id):
  global today
  read_marker = marker.gen_rlock()
  while today < len(DAYS)-1:
    read_marker.acquire()
    print(f"Reader {id} sees {DAYS[today]}, read count: {read_marker.c_rw_lock.v_read_count}")
    read_marker.release()

def calendar_writer(id):
  global today
  write_marker = marker.gen_wlock()
  while today < len(DAYS) - 1:
    write_marker.acquire()
    today = (today + 1) % 7
    print(f"Writer {id} updated date to {DAYS[today]}")
    write_marker.release()

if __name__ == '__main__':
  for i in range(3):
    threading.Thread(target=calendar_reader, args=(i,)).start()
  for i in range(2):
    threading.Thread(target=calendar_writer, args=(i,)).start()

  """
  Reader0 sees Sunday, read count: 1
  Reader0 sees Sunday, read count: 1
  Reader1 sees Sunday, read count: 2
  Reader0 sees Sunday, read count: 2
  Reader1 sees Sunday, read count: 3
  Reader2 sees Sunday, read count: 3
  Writer 0 updated date to Monday
  Writer 0 updated date to Tuesday
  Writer 0 updated date to Wednesday
  Writer 0 updated date to Thursday
  Reader2 sees Thursday, read count: 1
  Reader0 sees Thursday, read count: 1
  Reader1 sees Thursday, read count: 1
  Writer 1 updated date to Friday
  Writer 1 updated date to Saturday
  Writer 0 updated date to Sunday
  Writer 0 updated date to Monday
  Writer 0 updated date to Tuesday
  Writer 0 updated date to Wednesday
  Writer 0 updated date to Thursday
  Writer 0 updated date to Friday
  Writer 0 updated date to Saturday
  Reader0 sees Saturday, read count: 1
  Reader2 sees Saturday, read count: 2
  Reader1 sees Saturday, read count: 3
  """
```

{% endtab %}
{% tab title='nested.py' %}

```py
import threading
from contextlib import nullcontext

total = 0
lock = threading.RLock()  # RLock should be used for nested lock


def count(is_lock):
  global total
  # acquire and release
  with lock if is_lock else nullcontext():
    with lock if is_lock else nullcontext():
      for _ in range(1000000):
        total += 1


if __name__ == '__main__':
  td1 = threading.Thread(target=count, args=(False,))
  td2 = threading.Thread(target=count, args=(False,))

  td1.start()
  td2.start()
  td1.join()
  td2.join()
  print(total)  # 1362632 -> setting is_lock = True prints 2000000
```

{% endtab %}
{% endtabs %}

* Condition

```py
Condition(lock=None)
acquire(*args)
release()
wait(timeout=None)
wait_for(predicate, timeout=None)
notify(n=1)
notify_all()
```

{% tabs %}
{% tab title='eat_turn.py' %}

```py
import threading

slowcooker_lid = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid)

def hungry_person(person_id):
  global soup_servings
  while soup_servings > 0:
    with slowcooker_lid:
      while (person_id != (soup_servings % 5)) and (soup_servings > 0):
        print(f'Person {person_id} checked... then put the lid back.')
        soup_taken.wait()
      if soup_servings > 0:
        soup_servings -= 1
        print(f'Person {person_id} took soup!, Servings left: {soup_servings}')
        soup_taken.notify_all()

if __name__ == '__main__':
  for person in range(5):
    threading.Thread(target=hungry_person, args=(person,)).start()
  """
  Person 0 checked... then put the lid back.
  Person 1 took soup!, Servings left: 10
  Person 1 checked... then put the lid back.
  Person 2 checked... then put the lid back.
  Person 0 took soup!, Servings left: 9
  Person 0 checked... then put the lid back.
  Person 1 checked... then put the lid back.
  Person 3 checked... then put the lid back.
  Person 2 checked... then put the lid back.
  Person 4 took soup!, Servings left: 8
  Person 4 checked... then put the lid back.
  Person 0 checked... then put the lid back.
  Person 1 checked... then put the lid back.
  Person 3 took soup!, Servings left: 7
  Person 3 checked... then put the lid back.
  Person 2 took soup!, Servings left: 6
  Person 2 checked... then put the lid back.
  Person 0 checked... then put the lid back.
  Person 1 took soup!, Servings left: 5
  Person 1 checked... then put the lid back.
  Person 3 checked... then put the lid back.
  Person 4 checked... then put the lid back.
  Person 2 checked... then put the lid back.
  Person 0 took soup!, Servings left: 4
  Person 0 checked... then put the lid back.
  Person 1 checked... then put the lid back.
  Person 3 checked... then put the lid back.
  Person 4 took soup!, Servings left: 3
  Person 4 checked... then put the lid back.
  Person 2 checked... then put the lid back.
  Person 0 checked... then put the lid back.
  Person 1 checked... then put the lid back.
  Person 3 took soup!, Servings left: 2
  Person 3 checked... then put the lid back.
  Person 4 checked... then put the lid back.
  Person 2 took soup!, Servings left: 1
  Person 2 checked... then put the lid back.
  Person 1 took soup!, Servings left: 0
  """
```

{% endtab %}
{% endtabs %}

> queue

* thread safe

```py
Queue(maxsize=0)
empty()
get(block=True, timeout=None)
put(item, block=True, timeout=None)
qsize()

from queue import PriorityQueue

pq = PriorityQueue(maxsize=3)
pq.put((8, 'top'))
pq.put((1, 'sean'))
pq.put((3, 'top'))
while pq.size():
  print(pq.get())
```

> subprocess

```py
run(["ls", "-l"], capture_output=True, text=True)    # simplified Popen, execute and wait

# Popen
Popen(args)           # Execute a child program in a new process
universal_newlines=False      # input/output is accepted as bytes, not Unicode
p = subprocess.Popen("ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()    # out is byte -> must be encoded
```

{% tabs %}
{% tab title='linux.py' %}

```py
import os
import subprocess
import time
from collections import deque

def ls():
  commands = "ls -a"

  process = subprocess.Popen(commands.split(), stdout=subprocess.PIPE)
  out, err = process.communicate()

  print(out)
  print(err)

def top():
  cpu_usages = [1]
  while True:
  process = subprocess.Popen("ps -a -o %cpu,%mem,cmd".split(), stdout=subprocess.PIPE)
  out, _ = process.communicate()
  try:
    cpu_usages.append(int([line.split()[0] for line in out.decode('utf-8').split('\n') if "_type_" in line][0]))
    print(cpu_usages)
    time.sleep(0.1)
  except Exception as e:
    return sum(cpu_usages) / len(cpu_usages)

def cpu_usage():
  p = subprocess.Popen(['/usr/bin/time'] + ["ls"], stdout=open(os.devnull, 'wb', 0), stderr=subprocess.PIPE)
  with p.stderr:
  q = deque(iter(p.stderr.readline, b''), maxlen=2)
  rc = p.wait()
  return b''.join(q).decode().strip()
```

{% endtab %}
{% endtabs %}

### Random

> random

* randrange(0, 10) : random integer between
* uniform(0, 10) : random float between

## Database

### Local

> csv

```py
import csv

data = ['4', '5', '6']

with open('data1d.csv', 'w') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(data)

csvFile.close()

with open('data1d.csv') as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  for row in csvReader:
    print(row)

# write | read 2d file
data = [['height','weight','age'],
    [155,66,27],
    [177,82,34],
    [155,66,27],
    [175,70,32],
    [195,99,21],
    [157,52,17],
    ["",52,17]]

with open("data2d.csv","w") as my_csv:
  writer = csv.writer(my_csv, delimiter=',')
  writer.writerows(data)

with open('data2d.csv') as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  for row in csvReader:
    print(row)
```

> pickle

* dump(obj, file)
* load(file)

> psycopg2

* mac
  * pip install psycopg2-binary
  * import psycopg

{% tabs %}
{% tab title='run_query.py' %}

```py
# Connect to your postgres DB
conn = psycopg.connect("dbname=test user=postgres")
# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a query
cur.execute("SELECT * FROM my_data")
# Retrieve query results
records = cur.fetchall()
```

{% endtab %}
{% endtabs %}

> panflute

* make pandoc filters

> pypandoc

* serialize markdown

```py
import io
import pypandoc
import panflute

def action(elem, doc):
  if isinstance(elem, panflute.Header):
    doc.header.append(elem)

if __name__ == '__main__':
  raw_doc = pypandoc.convert_file('book/cpp/cpp.md', 'json')
  doc = panflute.load(io.StringIO(raw_doc))
  doc.header = []
  doc = panflute.run_filter(action, doc=doc)

  for image in doc.header:
    print(image)
```

> json

* encoding Python Objects into JSON is called Serialization

```py
python -m json.tool file.json  # validate file.json
dumps()    # encode JSON Data into native Python String
dump()     # encode and store JSON Data into a file
load(s)    # read from json

json.dumps(parsed, indent=4, sort_keys=True)    # pretty print json
```

{% tabs %}
{% tab title='basic_crud.py' %}

```py
# read write
import json
data = [{
  'name' : '영수',
  'age' : 16
}]
with open("data_file.json", "w") as write_file:
  json.dump(data, write_file, indent=4, ensure_ascii=False)  # ensure_ascii for korean character

with open("data_file.json", "r") as read_file:
  data = json.load(read_file)
print(data)

# Recursive print
def pprint(obj):          # recursively decode all lists
  import json
  if isinstance(obj, list):
    return repr(obj).decode('string-escape')
  elif isinstance(obj, dict):
    return json.dumps(self.__dict__, indent=4, ensure_ascii=False)
```

{% endtab %}
{% tab title='json_db.py' %}

```py
import os
import json
import pathlib
import functools

class JsonDB():
  def add(self, collection_id, documents, overwrite=True):
    if not isinstance(documents, list):
      documents = [documents]

    pathlib.Path(f"{PATH.DB}/{collection_id}").mkdir(parents=True, exist_ok=True)
    for document in documents:
      document_id = document.__dict__[collection_id + "_id"]
      document_path = PATH.DB / collection_id / f"{document_id}.json"
      if os.path.exists(document_path) and not overwrite:
        return False
      with open(document_path, "w") as f:
        json.dump(document.__dict__, f, ensure_ascii=False)
    return True

  def delete(self, collection_id, document_id, ignore_missing=True):
    logger.debug(f"delete({collection_id}, {document_id})")
    document_path = PATH.DB / collection_id / f"{document_id}.json"
    if document_path.exists:
      os.remove(document_path)
    elif not ignore_missing:
      return False
    return True

  @functools.lru_cache
  def get_all(self, collection_id):
    logger.debug(f"get_all({collection_id})")
    collection_path = PATH.DB / collection_id
    document_id2obj = {}
    for document_path in collection_path.iterdir():
      with open(document_path, "r") as f:
        document_id2obj[document_path.name[:-5]] = dict2class(collection_id, json.load(f))
    return document_id2obj

  def get(self, collection_id, document_ids):
    document_id2obj = self.get_all(collection_id)
    if not isinstance(document_ids, list):
      document_ids = [document_ids]
    documents = []
    for document_id in document_ids:
      documents.append(document_id2obj[document_id])
    return documents[0] if len(documents) == 1 else documents


local_db = JsonDB()
```

{% endtab %}
{% endtabs %}

> spark

{% tabs %}
{% tab title='spark.py' %}

```py
import pyspark
from operator import add
sc = pyspark.SparkContext.getOrCreate()
data = sc.parallelize (["scala", "hadoop", "spark", "akka", "spark vs hadoop", "pyspark", "pyspark and spark"])
print(data.count())
print("data.collect()")
filtered = data.filter(lambda x: 'spark' in x).collect()
print(filtered)
print(data.reduce(add))
file = sc.textFile('00_keywords.py')
print(f"{file.count()}")
print(f"{file.take(3)}")
print(f"{file.filter(lambda s: 'print' in s.lower()).count()}")
spark = pyspark.sql.SparkSession(sc)
files = sc.wholeTextFiles('.')
pprint(f"{files.count()}")
df = files.toDF(['name', 'data'])
print(f"{df.select('name').toPandas().head()}")
spark.read.csv('competition_vision/mnist/data/mnist_train.csv').toPandas()
spark.read.load('competition_vision/mnist/data/mnist_train.csv').head()
```

{% endtab %}
{% endtabs %}

> yaml

* safe_load()

{% tabs %}
{% tab title='yaml.py' %}

```py
import yaml
import io

# Define data
data = {
  'a list': [1, 42, 3.141, 1337, 'help', u'€'],
  'a string': 'bla',
  'another dict': {
      'foo': 'bar',
      'key': 'value',
      'the answer': 42
  }
}

# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
  yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

# Read YAML file
with open("data.yaml", 'r') as stream:
  data_loaded = yaml.safe_load(stream)

print(data == data_loaded)
```

{% endtab %}
{% endtabs %}

### Remote

> faker

```py
'add_provider', 'address', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number', 'cache_pattern', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color', 'color_name', 'company', 'company_email', 'company_suffix', 'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 'cryptocurrency_name', 'csv', 'currency', 'currency_code', 'currency_name', 'currency_symbol', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'del_arguments', 'dga', 'domain_name', 'domain_word', 'dsv', 'ean', 'ean13', 'ean8', 'ein', 'email', 'factories', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'first_name_nonbinary', 'fixed_width', 'format', 'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'generator_attrs', 'get_arguments', 'get_formatter', 'get_providers', 'hex_color', 'hexify', 'hostname', 'http_method', 'iban', 'image_url', 'internet_explorer', 'invalid_ssn', 'ios_platform_token', 'ipv4', 'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'items', 'itin', 'job', 'json', 'language_code', 'language_name', 'last_name', 'last_name_female', 'last_name_male', 'last_name_nonbinary', 'latitude', 'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 'locales', 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'name_nonbinary', 'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 'phone_number', 'port_number', 'postalcode', 'postalcode_in_state', 'postalcode_plus4', 'postcode', 'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male', 'prefix_nonbinary', 'pricetag', 'profile', 'provider', 'providers', 'psv', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random', 'random_choices', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter', 'random_letters', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'safari', 'safe_color_name', 'safe_domain_name', 'safe_email', 'safe_hex_color', 'secondary_address', 'seed', 'seed_instance', 'seed_locale', 'sentence', 'sentences', 'set_arguments', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift', 'swift11', 'swift8', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'tsv', 'unique', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'weights', 'windows_platform_token', 'word', 'words', 'year', 'zip', 'zipcode', 'zipcode_in_state', 'zipcode_plus4'
```

* fake data generator

```py
import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
fake = Faker()
fake_data = defaultdict(list)

for _ in range(1000):
  fake_data["first_name"].append( fake.first_name() )
  fake_data["last_name"].append( fake.last_name() )
  fake_data["occupation"].append( fake.job() )
  fake_data["dob"].append( fake.date_of_birth() )
  fake_data["country"].append( fake.country() )

df_fake_data = pd.DataFrame(fake_data)
df_fake_data

fake.factories
```

```py
from faker import Faker

faker.name()
faker.job()
faker.text()

# in Czech language
faker = Faker('cz_CZ')

for i in range(3):
  name = faker.name()
  address = faker.address()
  phone = faker.phone_number()
  print(f'{name}, {address}, {phone}')
```

> sqlfaker

```py
from faker import Faker
from sqlfaker.database import Database
from collections import defaultdict
from sqlalchemy import create_engine

# add database
my_db = Database(db_name="housing")

# add tables
my_db.add_table(table_name="User", n_rows=500)
my_db.tables["studyprogram"].add_primary_key(column_name="studyprogram_id")
my_db.tables["studyprogram"].add_column(column_name="shortname", data_type="varchar(50)", data_target="name")
my_db.tables["studyprogram"].add_column(column_name="startdate", data_type="date", data_target="date")

my_db.tables["student"].add_primary_key(column_name="student_id")
my_db.tables["student"].add_column(column_name="firstname", data_type="varchar(50)", data_target="first_name")
my_db.tables["student"].add_column(column_name="lastname", data_type="varchar(50)", data_target="last_name")
my_db.tables["student"].add_foreign_key(column_name="studiengang_id", target_table="studiengang", target_column="studiengang_id")
# data_types : password, email, date_time

my_db
```

> sqlite

{% tabs %}
{% tab title="wrapper.py" %}

```py
import sqlite3
"""singleton class to deal with db"""

class DBConnection:
  instance = None

  def __new__(cls, *args, **kwargs):
  if cls.instance is None:
    cls.instance = super().__new__(DBConnection)
    return cls.instance
  return cls.instance

  def __init__(self, db_name='you-db-name'):
  self.name = db_name
  # connect takes url, dbname, user-id, password
  self.conn = self.connect(db_name)
  self.cursor = self.conn.cursor()

  def connect(self):
  try:
    return sqlite3.connect(self.name)
  except sqlite3.Error as e:
    pass

  def __del__(self):
  self.cursor.close()
  self.conn.close()
```

{% endtab %}
{% tab title="dataframe.py" %}

```py
import sqlite3
import json
import pandas as pd

conn = sqlite3.connect('data/sample.db') # sqlite3.connect(":memory:")
c = conn.cursor()

def db2dicts(db_path):
  db = bsddb3.btopen(db_path, 'r')
  for id in db:
  try:
    dic = json.loads(db[id])
    assert isinstance(dic, dict)
  except:
    dic = {'raw': db[id].decode('utf-8')}
  yield({'_' + k: v for k, v in dic.items()})

def json2server(db_path, sqlite_path=None):
  conn = sqlite3.connect(sqlite_path)
  try:
  conn.execute(f"DROP TABLE {cate}")
  except:
  pass

  conn.execute(f"CREATE TABLE IF NOT EXISTS {cate} (_id object PRIMARY KEY)")

  for dic in db2dicts(db_path):
  columns = set(e[1] for e in conn.execute(f"PRAGMA table_info('{cate}')").fetchall())
  for key in dic.keys():
    if key not in columns:
    conn.execute(f"ALTER TABLE {cate} ADD COLUMN {key}")
    columns.add(key)
  try:
    conn.execute(f"INSERT INTO {cate}({', '.join(dic.keys())}) VALUES ({', '.join('?' * len(dic.keys()))})", tuple(repr(e) for e in dic.values()))
  except:
    logger.warn("invalid" + str(sys.exc_info()[0]))

  conn.commit()

def query2df(sqlite_path, query):
  print("\n", query)
  conn = sqlite3.connect(sqlite_path)
  cursor = conn.execute(query)
  return pd.DataFrame(data=cursor.fetchall(), columns=[c[0] for c in cursor.description])

def flatten(obj):
  if isinstance(obj, str):
  return "'" + obj + "'"
  else:
  return "'" + repr(obj) + "'"

c.execute("DROP TABLE students")
c.execute("CREATE TABLE IF NOT EXISTS students (id object PRIMARY KEY, date text)")
c.execute("INSERT INTO students(date) VALUES ('2006-01-05')")

c.execute("CREATE INDEX idx_id ON students(id)")

display(query2df('data/sample.db', "PRAGMA index_list('students')"))
display(query2df('data/sample.db', "PRAGMA table_info('students')"))
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
  display(query2df('data/sample.db', "SELECT name as table_name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"))

dic = {'new' : [1, 2, 4], 'date' : '2006-02-22', 'raw' : 'afd, (),'}
for key in dic.keys():
  try:
  c.execute(f"ALTER TABLE students ADD COLUMN {key}")
  except:
  pass


c.execute(f"INSERT INTO students({', '.join(dic.keys())}) VALUES ({', '.join('?' * len(dic.keys()))})", tuple(flatten(e) for e in dic.values()))

conn.commit()

for row in c.execute('SELECT * FROM students ORDER BY date'):
  print(row)
```

{% endtab %}
{% endtabs" %}

> sqlalchemy

```sh
detached      # Object, states which an object can have within a session
dialect       # Object, allows DB operations on a particular DB backend
DBAPI         # Python Database API Specification
metadata      # generally refers to "data that describes data"
create_engine('DB', echo=True)     # echo for logging
```

* sqlalchemy.engine
  * not thread-safe (underlying DBAPI connection may not support shared access between threads)

```sh
begin()       # Transaction Instance
```

* sqlalchemy.engine.Engine
  * Connects a Pool and Dialect together

```sh
begin()       # Return a context manager delivering a Connection
connect()     # Return a new Connection object
```

* sqlalchemy.engine.Connection
  * not thread-safe

```sh
execute()     # Executes SQL statement construct, returns ResultProxy
```

* sqlalchemy.engine.Transaction
  * not thread safe

```sh
close()
commit()
rollback()
```

* sqlalchemy.schema
* sqlalchemy.schema.column

```sh
Column(name, type, primary_key=F)        # Column in a database table
```

* sqlalchemy.schema.Table

```py
Table()
drop(engine)
columns
```

* sqlalchemy.schema.MetaData

```py
MetaData()       # Thread-safe container object for read
create_all()     # check existence of each individual table. CREATE if not
```

> pymongo

* Namespace is the concatenation of the database name and collection name
* MongoDB does not support foreign key constraints
* not support default multi-document ACID transactions atomic operation on a single document
* indexes are stored in RAM
* Can’t use index Regex or negation operators ($nin, $not). Arithmetic operators ($mod). $where

* pymongo.Client

```py
drop_database(name_or_database)  # drop database
list_database_names()            # show all database
```

* pymongo.Database

```py
drop_collection(collection_name)    # remove matching document
list_collections_names()            # show all collections
db[collection_name] || db.collection_name  # get collection
```

* pymongo.Collection

```py
count_documents({})     # counts documents
create_index(keys)      # create index on keys
delete_one()            # drop one document
insert_one()            # insert one document
insert_many()
rename(new_name)        # rename this collection

find({ "key" : { "$exists" : false } })        # find if key doesn’t exists
db.collection.update(
  {},
  [{ $set: { a: { $concat: [ "$a", "World" ] } } }],
  { multi: true }
)
update_one({}, {"$set": {"a": 1}}, upsert=F)    # update field
update_many({}, {'old' : 'new'})        # rename field "old" to "new" in all documents
cl.create_index([( "_kowiki_id_v0", 1 )],partialFilterExpression = {'_kowiki_id_v0' : {'$exists': True }}
```

```py
# aggregate
db.COL.update_many({}, [{ "$set": { '_id': { '$concat': [ "COL", "$_id" ] } } }])
db.zipcodes.aggregate( [            # Average population by state
   { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },
   { $group: { _id: "$_id.state", avgCityPop: { $avg: "$pop" } } }
] )
db.zipcodes.aggregate( [            # States with Populations above 10 Million
   { $group: { _id: "$state", totalPop: { $sum: "$pop" } } },
   { $match: { totalPop: { $gte: 10*1000*1000 } } }
] )

# operator
"$eq"              # equal to a specified value.
"$gt"              # greater than a specified value.
"$gte"             # greater than or equal to a specified value.
"$lt"              # less than a specified value.
"$lte"             # less than or equal to a specified value.
"$ne"              # not equal to a specified value.
"$exists"          # exists in documents
"$in"              # any of the values specified in an array.
"$nin"             # none of the values specified in an array.
"$or"              # Joins query clauses with a logical OR.
"$not"             # Inverts the effect of a query expression.
"$nor"             # Joins query clauses with a logical NOR.
'{ "$and": [ {"sex": "male"}, {"age": "26"}]}' # Joins query clauses with a logical AND.
"{'$regex':'^File'}"
cl.updateMany({}, {$rename: {'orig: "new"}}    # rename entire field name

# compound
db.collection.createIndex( { <field1>: <type>, <field2>: <type2>, ... } )
```

> text

```py
db.stores.createIndex( { name: "text", description: "text" } )
# tokenize the search string using whitespace and most punctuation as delimiters
cl.find({ $text:{ $search: "java -coffee" }})    # Exclude query
```

> Firestore

```py
Transactions       # a set of read and write operations on one or more documents.
Batched Writes     # a set of write operations on one or more documents (max 500)
firestore.Increment(50) # if current isn’t numeric value, sets field to the given value
doc_ref.update({'id': firestore.DELETE_FIELD})  # delete field
city_ref.update({u'regions': firestore.ArrayRemove([u'east_coast'])})    # delete from array
```

* Client

```py
collection("user") # CollectionReference
document("doc")    # DocumentReference
```

* WriteBatch

```py
batch = db.batch()

# Set the data for NYC
nyc_ref = db.collection(u'cities').document(u'NYC')
batch.set(nyc_ref, {u'name': u'New York City'})

# Update the population for SF
sf_ref = db.collection(u'cities').document(u'SF')
batch.update(sf_ref, {u'population': 1000000})

# Delete DEN
den_ref = db.collection(u'cities').document(u'DEN')
batch.delete(den_ref)

batch.commit()    # Commit the batch

# Example 2
for member_ref in db.collection("member").list_documents():
  member = member_ref.get().to_dict()
  member_ref.update({'solved_problem_ids': member["solved"], 'solved': firestore.DELETE_FIELD})
```

* CollectionReference

```py
db.collection("problem")             # get reference
list_documents() → Generator[DocRef] # list documents
stream()  → Generator[DocSnap]       # list streams
get()   # get all documents in collection
delete()
```

* DocumentReference

```py
id                            # id
document("rbtmd1010")
get() → DocumentSnapShot()    # get_document
delete()                      # delete document
update({"kr_name": '황규승'})   # update document
```

* DocumentSnapshot

```py
to_dict()      # convert to dictioanry
```

{% tabs %}
{% tab title='usage.py' %}

```py
from collections import defaultdict
from functools import lru_cache
from itertools import islice

class Team:
  def __init__(self, team_id="", admin_ids=None, member_ids=None):
    self.team_id = team_id
    self.admin_ids = admin_ids or []
    self.member_ids = member_ids or []

  @staticmethod
  @lru_cache
  def show_progress(team_id):
    from ..database import local_db, remote_db
    member_ids = remote_db.get("team", team_id).member_ids
    members = remote_db.get("member", member_ids)
    members.sort(key=lambda member: len(member.solved_problem_ids))
    html = '<div id="search-problem" onchange=toggle_visibility()>'
    html += 'bj_range=<input type="number" class="min_bj_level" value="1">~<input type="number" class="max_bj_level" value="10"><br>'

    for i, member in enumerate(reversed(members)):
      html += f'<input id="{member.id}" class="show_member_id" type="checkbox">{member.kr_name} {len(member.solved_problem_ids)} {member.baekjoon_id}</input><br>'
      member.solved_problem_ids = set(member.solved_problem_ids)

    problems = local_db.get_all("problem")
    problems = problems.values()
    cate2problems = defaultdict(list)
    for problem in problems:    # cache headers to problem for effeciency
      if problem.solution_link != "" and problem.problem_id.startswith("BJ"):
        cate2problems[f"{problem.category_id}"].append(problem)
    for category in categories:
      html += f"<h1>{category}</h1>"
      for problem in sorted(cate2problems[f"{category}"], key=lambda problem: problem.level):
        html += f'<table style="table-layout:fixed;">'
        html += f"<tr id='{problem.level}' class='bj_level'>"
        html += f"<td style='width:400px;'>{problem.link}</td>"
        html += f"<td style='width:70px;'>{problem.solution_link}</td>"
        html += " ".join([f"<td> <span id={member.id} class='{'' if problem.problem_id in member.solved_problem_ids else 'member_id'}' style='display:none;'>{member.kr_name}</span></td>" for member in members])
        html += f"</tr>"
      html += f"</table>"
    html += "</div>"
    return html
```

{% endtab %}
{% tab title='firebase_db.py' %}

```py
from firebase_admin import credentials, firestore, initialize_app

class FirebaseDB():
  def __init__(self):
    cred = credentials.Certificate(service_account_credential)
    try:
      initialize_app(cred)
    except Exception as e:
      logger.error(e)
      return
    self._db = firestore.client()

  def add(self, collection_id, document, overwrite=True):
    document_id = document.__dict__[collection_id + "_id"]
    document_ref = self._db.collection(collection_id).document(document_id)

    if not overwrite and document_ref.get().exists:
      return False
    document_ref.set(document.__dict__)
    return True

  def delete(self, collection_id, document_id, ignore_missing=True):
    logger.debug(f"delete({collection_id}, {document_id})")

    document_ref = self._db.collection(collection_id).document(document_id)
    if not ignore_missing and not document_ref.get().exists:
      return False
    document_ref.delete()
    return True

  @functools.lru_cache
  def get_all(self, collection_id):
    logger.debug(f"get_all({collection_id})")
    return {doc_ref.id: dict2class(collection_id, doc_ref.to_dict()) for doc_ref in self._db.collection(collection_id).get()}

  def get(self, collection_id, document_ids):
    document_id2obj = self.get_all(collection_id)
    documents = []
    if not isinstance(document_ids, list):
      document_ids = [document_ids]
    for document_id in document_ids:
      documents.append(document_id2obj[document_id])
    return documents[0] if len(documents) == 1 else documents


remote_db = FirebaseDB()
```

{% endtab %}
{% endtabs %}

> redis

{% tabs %}
{% tab title="app.py" %}

```py
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
  redis.incr('hits')
  return f'Compose/Flask demo has been viewed {redis.get("hits")} time(s).'


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
```

{% endtab %}
{% tab title="docker-compose.yml" %}

```yaml
version: '2'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    depends_on:
      - redis
  redis:
    image: redis
```

{% endtab %}
{% tab title="Dockerfile" %}

```sh
FROM python:3
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
requirements.txt

# run command
# docker build -t compose-flask .
# docker-compose up
```

{% endtab %}
{% endtabs %}

> sys

* path : a list of strings that determines the interpreter’s search path for modules
* setswitchinterval() : set time slice
* exc_info()
  * This function returns a tuple of three values that give information about the exception
* read() : sys.stdin Read all input at once
* write() : sys.stderr
* getsitepackages() : see sitepackages

```sh
ps1 / ps2             # used for interactive mode string
```

{% tabs %}
{% tab title='inputs.py' %}

```py
# Fast IO (when TC > 50000)
import sys
input = sys.stdin.readline

# Read entire file
files = sys.stdin.read()
for line in files.split("\n"):
  print(line)
```

{% endtab %}
{% endtabs %}

## ML

### Traditional

> scipy

```py
spatial.distance.cosine(outputs[i], outputs[j]) # Cosine similarity
scipy.signal.convolve(I, filter, mode='same')   # # convolve
```

{% tabs %}
{% tab title='pairwise_distance.py' %}

```py
import numpy as np
from scipy.spatial import distance
a = np.array([[0, 0, 0]])
b = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])

distance.cdist(a, b, 'euclidean')   # [[1.73205081 1.41421356 1.]]
np.argmin(distance.cdist(a, b, 'euclidean')[0]) # 2th
distance.pdist(b, 'euclidean') # [1. 1.41421356 1.]
```

{% endtab %}
{% tab title='convex_haul.py' %}

![](images/20210301_195331.png)

```py
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt
import numpy as np

points = np.random.rand(30, 2)   # 30 random points in 2-D
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
plt.show()
```

{% endtab %}
{% endtabs %}

* scipy.sparse
  * [+] CSR fast arithmetic operations (CSR + CSR, CSR * CSR), row slicing, matrix vector products
  * [-] CSR slow column slicing (than CSC), changes to sparsity structure (than LIL| DOK)
  * nnz : Number of stored values
  * bsr_matrix(arg1[, shape, dtype, copy, blocksize]) : Block Sparse Row matrix
  * coo_matrix(arg1[, shape, dtype, copy]) : Coordinate format.
  * csc_matrix(arg1[, shape, dtype, copy]) : Compressed Sparse Column matrix
  * csr_matrix(arg1[, shape, dtype, copy]) : Compressed Sparse Row matrix
  * dia_matrix(arg1[, shape, dtype, copy]) : Sparse matrix with DIAgonal storage
  * dok_matrix(arg1[, shape, dtype, copy]) : Dictionary Of Keys based sparse matrix.
  * lil_matrix(arg1[, shape, dtype, copy]) : Row-based list of lists sparse matrix
  * getrow(i) : copy (1 x n) CSR matrix
  * get_shape() : get shape of a matrix
  * nonzero() : tuple of arrays (row,col)
  * getnnz([axis]) : stored values, including explicit zeros
  * multiply(other) : Pointwise multiplication by another matrix
  * power(n[, dtype]) : Element-wise power
  * todense([, order, out]) : Return a dense matrix representation of this matrix

> sklearn

{% tabs %}
{% tab title='visualize_word.py' %}

```py
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
word_10d = np.random.random((10, 10))

tsne_model = TSNE()
word_2d = tsne_model.fit_transform(word_10d)
for i, (x, y) in enumerate(word_2d):
  plt.scatter(x, y)
  plt.annotate(i, xy=(x, y), ha='right', va='bottom')
```

{% endtab %}
{% tab title='sentence_similarity.py' %}

```py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
train = ['call you tonight', 'Call me a cab', 'Please call me... PLEASE!']

count_vect = CountVectorizer()
ngram_vect = CountVectorizer(ngram_range=(2,2))
tfidf_vect = TfidfVectorizer()

count_vect.fit(train)
tfidf_vect.fit(train)
ngram_vect.fit(train)

print(f"unigram get_feature_names \t {count_vect.get_feature_names()}")
# unigram get_feature_names ['cab', 'call', 'me', 'please', 'tonight', 'you']
# bigram get_feature_names   ['call me', 'call you', 'me cab', 'me please', 'please call', 'you tonight']
print(f"bigram get_feature_names \t {ngram_vect.get_feature_names()}")

count_dtm = count_vect.transform(train)
ngram_dtm = ngram_vect.transform(train)
tfidf_dtm = tfidf_vect.transform(train)

print(pd.DataFrame(count_dtm.toarray(), columns=count_vect.get_feature_names()))  # one row per document and one column per token
print(pd.DataFrame(ngram_dtm.toarray(), columns=ngram_vect.get_feature_names()))
print(pd.DataFrame(tfidf_dtm.toarray(), columns=tfidf_vect.get_feature_names()))
"""
| cab | call | me  | please | tonight | you |
| --- | ---- | --- | ------ | ------- | --- |
| 0   | 1    | 0   | 0      | 1       | 1   |
| 1   | 1    | 1   | 0      | 0       | 0   |
| 0   | 1    | 1   | 2      | 0       | 0   |

| call me | call you | me cab | me please | please call | you tonight |
| ------- | -------- | ------ | --------- | ----------- | ----------- |
| 0       | 1        | 0      | 0         | 0           | 1           |
| 1       | 0        | 1      | 0         | 0           | 0           |
| 1       | 0        | 0      | 1         | 1           | 0           |

| cab   | call  | me       | please | tonight | you   |
| ----- | ----- | -------- | ------ | ------- | ----- |
| 0.000 | 0.385 | 0.000000 | 0.000  | 0.652   | 0.652 |
| 0.720 | 0.425 | 0.547832 | 0.000  | 0.000   | 0.000 |
| 0.000 | 0.266 | 0.342620 | 0.901  | 0.000   | 0.000 |
"""
```

{% endtab %}
{% endtabs %}

[bayes_recsys.ipynb](https://gist.github.com/SeanHwangG/b91b282540c3eec4b3cfd91c0a8d2d68)
[Iris_decision_tree.ipynb](https://gist.github.com/SeanHwangG/aa0514cab9d7c383d9e92fb5e673034d)
[boost_titanic.ipynb](https://gist.github.com/SeanHwangG/f940014736119f5859109de0f16695bd)

### NLP

> nltk

* PorterStemmer

```py
ps = nltk.PorterStemmer()
ps.stem('grows')
```

* WordNetLemmatizer

```py
wn = nltk.WordNetLemmatizer()
print(wn.lemmatize('geese'))
```

* corpus

```py
corpus.stopwords.words('english')    # stopwords
```

{% tabs %}
{% tab title='synonyms.py' %}

```py
poses = {'n':'noun', 'v':'verb', 's','adj (s)', 'a':'adj', 'r', 'adv'}
for synset in corpus.wordnet.synsets('good'):
  print(f'{poses[synset.pos()]} {', '.join([l.name() for l in synset.lemmas()])}')
```

{% endtab %}

{% tab title='hypernyms.py' %}

```py
panda = corpus.wordnet.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
list(pandas.closure(hyper)
```

{% endtab %}

{% endtabs %}

### Media

> Pygame

```py
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First game")
x, y = 50, 50
width, height, vel = 30, 30, 5
run = True
while run:
  pygame.time.delay(100)
  for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
  x -= vel
  if keys[pygame.K_RIGHT]:
  x += vel
  if keys[pygame.K_UP]:
  y -= vel
  if keys[pygame.K_DOWN]:
  y += vel

  win.fill((0, 0, 0))
  pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
  pygame.display.update()
```

> PIL

* RGB

{% tabs %}
{% tab title='insepect.py' %}

```py
from PIL import Image

def getSize(size) :
  return str(size[0]) + ' columns x ' + str(size[1]) + ' rows'

def getMode(mode) :
  if(mode == 'RGB'):
    return '3x8-bit pixels, true colour'
  elif(mode == 'RGBA') :
    return '4x8-bit pixels, true colour with transparency mask'
  elif(mode == 'CMYK') :
    return '4x8-bit pixels, colour separation'
  elif(mode == 'L') :
    return '8-bit pixels, black and white'
  elif(mode == 'P') :
    return '8-bit pixels, mapped to any other mode using a colour palette'
  elif(mode == 'YCbCr') :
    return '3x8-bit pixels, colour video format'
  elif(mode == 'RGBA') :
    return '1-bit pixels, black and white, stored with one pixel per byte'
  elif(mode == 'I') :
    return '32-bit signed integer pixels'
  elif(mode == 'F') :
    return '32-bit floating point pixels'
  else :
    return 'Unknown'

im = Image.open("/Users/sean/github/data/images/dining_table.jpg")
pix = im.load()
print(f'color at [w, h] \t {pix[10, 20]}')          # color at [w, h]    (140, 141, 133)
print(f'size \t {getSize(im.size)}')                # size    500 columns x 500 rows
print(f'mode \t {str(im.mode)} {getMode(im.mode)}') # mode    RGB 3x8-bit pixels, true colour
```

{% endtab %}
{% tab title='convert_to_video.py' %}

```py
import numpy as np
from PIL import Image, ImageDraw
import cv2

videodims = (100,100)
fourcc = cv2.VideoWriter_fourcc(*'avc1')
video = cv2.VideoWriter("test.mp4",fourcc, 60,videodims)
img = Image.new('RGB', videodims, color = 'darkred')
for i in range(0,60*60): #draw stuff that goes on every frame here
  imtemp = img.copy()
  video.write(cv2.cvtColor(np.array(imtemp), cv2.COLOR_RGB2BGR))
video.release()
```

{% endtab %}
{% endtabs %}

### opencv

* sudo apt-get install python3-opencv
* pip install opencv-python
* height, width, channel, BGR color
* OpenCV time: frame decoding + time to render the bounding boxes, labels, and to display the results

> Version

* 2009 Opencv 2.0 : convert to c++, mat class
* 2011 Opencv 2.3 : import cv2
* 2015 Opencv 3.0 : GPU(T-API)
* 2017 Opencv 3.3 : DNN

* opencv : core, widely used (highgui, imgproc ...)
* opencv_contirb : brand new, non-free, HW dependency (datasets, cnn_3dobj …)

> GUI

* moveWindow(wn, x, y) : only works if WINDOW_NORMAL, ignore header
* imshow(filename, img) → None : if int32 // 255, if float * 255, create namedWindow()
* setWindowProperty("slides")
* namedWindow(wn, WINDOW_AUTOSIZE) : WINDOW_NORMAL (video → window)
* destroyWindow(wn) / destroyAllWindows() : Destroy window
* waitKey(delay=None) → -1 | ord(key') : 27 (ESC), 13(ENTER), 9(TAB), ← (123), delay=-1 ∞
* WND_PROP_FULLSCREEN, WINDOW_FULLSCREEN : Full size

> Images

* copy() → np.ndarray
* cvtColor(img, type)
  * type : COLOR_BGR2RGB, COLOR_BGR2GRAY)
* imread(filename, parames)     np.ndarray : (IMREAD_COLOR/GRAYSCALE/UNCHANGED (PNG)
* imwrite(fn, img, params = N) → if Success : [IMWRITE_JPEG_QUALITY, 90] compression rate of 90
* CV_8U / S : np.uint8 /  np.int8
* CV_16U / S / F : np.uint16 / np.int16 /  np.float16
* CV_8UC1 / CV_8UC3 : np.uint8, shape (h, w) (Grey scale video) / (h, w, 3) (Color scale video)
* rectangle(img,(38,0),(51,12),(0,255,0),3)
  * image, top_left, bottom_right, color, thickness

* sobel(src, ddepth, dx, dy, ksize) : first, second, third, or mixed image derivatives
* cv.blur(src, ksize, dst, anchor, borderType) : blurs image using box filter

{% tabs %}
{% tab title="images.py" %}

```py
import cv2
import numpy as np
import fire
import math
import glob
import itertools
import matplotlib.pyplot as plt

def slide_show():
  img = np.zeros((255, 255, 3))
  cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 10)
  cv2.rectangle(img, (10, 10), (50, 50), 5)
  cv2.circle(img, (100, 100), 10, (1, 255, 1), -1)
  cv2.putText(img, 'OpenCv', (10, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 10, cv2.LINE_AA)

  imgs = [img] + [cv2.imread(f) for f in glob.glob('data/*.jpg')]

  # cv2.setWindowProperty("slides", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
  i, mx = 0, len(imgs)
  while True:
    cv2.imshow("slides", imgs[i])
    try:
      for (p, c) in zip(cv2.split(imgs[i]), ['b', 'g', 'r']):
        hist = cv2.calcHist([p], [0], None, [256], [0, 256])
        plt.plot(hist, color=c)
    except:
      pass
    key = cv2.waitKey(-1)
    if key == 123:
      i = (i + mx - 1) % mx
    elif key == 124:
      i = (i + 1) % mx
    elif key == ord('b'):
      imgs[i] = cv2.add(imgs[i], (50, 50, 50, 0))
    elif key == ord('d'):
      imgs[i] = cv2.add(imgs[i], (-50, -50, -50, 0))
    elif key == ord('q'):
      break

def combine():
  messi = cv2.imread('data/combine/messi.jpg')
  b, g, r = cv2.split(messi)
  messi = cv2.merge((r, g, b))
  ball = messi[290:340, 340:390]
  messi[0:50, 0:50] = ball

  logo = cv2.imread('data/combine/logo.png')
  logo = cv2.resize(logo, (messi.shape[1], messi.shape[0]))
  combined = cv2.addWeighted(messi, .9, logo, .1, 2)

  plane_bg = cv2.imread('data/combine/airplane.bmp')
  mask = cv2.imread('data/combine/mask_plane.bmp')
  field = cv2.imread('data/combine/field.bmp')
  plane = cv2.copyTo(plane_bg, mask)
  field[mask > 0] = plane_bg[mask > 0]

  imgs = [messi, logo, combined, plane, field]

  i, mx = 0, len(imgs)
  while True:
    cv2.imshow("slides", imgs[i])
    key = cv2.waitKey(-1)
    if key == 123:
      i = (i + mx - 1) % mx
    elif key == 124:
      i = (i + 1) % mx
    elif key == ord('q'):
      break
```

{% endtab %}
{% tab title="mouse_image.py" %}

```py
class Pallete:
  def __init__(self):
    self.ix = -1
    self.iy = -1
    # HEIGHT/y: 200, WIDTH/x: 300
    self.img = np.ones((200, 300, 3), np.uint8) * 255
    self.mode = "RECTANGLE"
    self.points = []

  def draw_shape(self, event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
      self.drawing = True
      (self.ix, self.iy) = x, y
    elif event == cv2.EVENT_LBUTTONUP:
      self.drawing = False
      cv2.rectangle(self.img, (self.ix, self.iy), (x, y), (0, 0, 0), -1)

  def draw_line(self, event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
      # OpenCV uses BGR
      cv2.circle(self.img, (x, y), 3, (0, 0, 255), -1)
      self.points.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
      if len(self.points) > 1:
        self.img = cv2.line(
          self.img, self.points[-1], self.points[-2], (255, 0, 0), 5)

  def start(self):
    windowName = 'Drawing Demo'
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, self.draw_line)
    while(True):
      cv2.imshow(windowName, self.img)

      k = cv2.waitKey(1)
      if k == 27:
        break

    cv2.destroyAllWindows()

def grep_cut():
  src = cv2.imread('data/messi.jpg')

  mask = np.zeros(src.shape[:2], np.uint8)
  bgdModel = np.zeros((1, 65), np.float64)
  fgdModel = np.zeros((1, 65), np.float64)
  rc = cv2.selectROI(src)
  cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
  mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
  dst = src * mask2[:, :, np.newaxis]

  cv2.imshow('dst', dst)

  def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
      cv2.circle(dst, (x, y), 3, (255, 0, 0), -1)
      cv2.circle(mask, (x, y), 3, cv2.GC_FGD, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
      cv2.circle(dst, (x, y), 3, (0, 0, 255), -1)
      cv2.circle(mask, (x, y), 3, cv2.GC_BGD, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
      if flags & cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(dst, (x, y), 3, (255, 0, 0), -1)
        cv2.circle(mask, (x, y), 3, cv2.GC_FGD, -1)
      elif flags & cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(dst, (x, y), 3, (0, 0, 255), -1)
        cv2.circle(mask, (x, y), 3, cv2.GC_BGD, -1)
    cv2.imshow('dst', dst)

  cv2.setMouseCallback('dst', on_mouse)

  while True:
    key = cv2.waitKey()
    if key == 13:
      cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
      mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
      dst = src * mask2[:, :, np.newaxis]
      cv2.imshow('dst', dst)
    elif key == 27:
      break

  cv2.destroyAllWindows()
```

{% endtab %}
{% endtabs %}

> video

* isOpened() → bool
* open()
* get()
* CAP_FRAME_WIDTH  / HEIGHT
* CAP_PROP_FPS / FRAME_COUNT    # Frame per count
* CAP_PROP_POS_MSEC / EXPOSURE    # current milisecond
* set() / read()
* grab() / retrieve()/ release()
* VideoCapture(fname, apiPreference) → retval

{% tabs %}
{% tab title="capture_video.py" %}

```py
import cv2
import fire


def check_video(path):
  cap = cv2.VideoCapture(path)
  frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
  fps = cap.get(cv2.CAP_PROP_FPS)
  length = -1 if fps == 0 else frame / fps
  width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
  print(f"FRAME \t {frame}")
  print(f"FPS \t {fps}")
  print(f"LENGTH \t {length}")
  print(f"SIZE \t {width} x {height}")


def open_video(path):
  cap = cv2.VideoCapture(path)

  while cap.isOpened():
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
      break

def capture_video():
  cap = cv2.VideoCapture(0)
  #fourcc = cv2.VideoWriter_fourcc(*'XVID')
  #out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

  print(f'HEIGHT \t {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
  print(f'WIDTH \t {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}')
  while cap.isOpened():
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
      break
    elif key == ord('s'):
      cv2.imwrite('data/result/capture.jpg', frame)
    elif key == ord('g'):
      cv2.imwrite('data/result/capture.jpg', gray)

  cap.release()
  cv2.destroyAllWindows()
```

{% endtab %}
{% tab title="tracker.py" %}

```py
import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[2]

if tracker_type == 'BOOSTING':
  tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
  tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF':
  tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD':
  tracker = cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
  tracker = cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
  tracker = cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
  tracker = cv2.TrackerMOSSE_create()
if tracker_type == "CSRT":
  tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture(0)
if not video.isOpened():
  print("Could not open video")
  sys.exit()

ok, frame = video.read()
if not ok:
  print('Cannot read video file')
  sys.exit()

# Define an initial bounding box
bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)  # Initialize tracker with first frame and bounding box

while True:
  ok, frame = video.read()
  if not ok:
    break

  timer = cv2.getTickCount()
  ok, bbox = tracker.update(frame)
  fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
  if ok:
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
  else:  # Tracking failure
    cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

  cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
  cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
  cv2.imshow("Tracking", frame)
  k = cv2.waitKey(1) & 0xff
  if k == 27:
    break
```

{% endtab %}
{% tab title="blur_thread.py" %}

```py
from collections import deque
from multiprocessing.pool import ThreadPool

import cv2

VIDEO_PATH = "/Users/sean/github/data/video"

def process_frame(frame):
  frame = cv2.medianBlur(frame, 19)
  return frame

cap = cv2.VideoCapture(f"{VIDEO_PATH}/sd_sample_03.mp4")
thread_num = cv2.getNumberOfCPUs()
pool = ThreadPool(processes=thread_num)
pending_task = deque()

while True:
  while len(pending_task) > 0 and pending_task[0].ready():
    res = pending_task.popleft().get()
    cv2.imshow('threaded video', res)

  if len(pending_task) < thread_num:
    frame_got, frame = cap.read()
    if frame_got:
      task = pool.apply_async(process_frame, (frame.copy(),))
      pending_task.append(task)

  if cv2.waitKey(1) == 27 or not frame_got:
    break

cv2.destroyAllWindows()
```

{% endtab %}
{% endtabs %}

> dnn

* size : output image size (default 0, 0)
* mean : subtract from input image (default 0, 0, 0)
* retval) : numpy.ndarray. shape=(N,C,H,W). dtype=numpy.float32
* readNet(model, config, framework : trained weight, network, cv2.dnn_Net
* blobFromImage(image, scalefactor=1.0 : multiply to image (default 1)
* NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)

### Numpy

> Array

* Create
  * arange() : same to range
  * array()
    * ([[1], [2]]) : 2d arry
  * eye() : n * n identity matrix
  * empty_like(<matrix>) : same dimension empty array
  * full((3,3), True, dtype=bool) : 3*3 true
  * linspace(1, 2, 5) : (5, 1) [1, 1.25, 1.5, 1.75, 2]
  * ones()
    * ([2, 3]) : 2x3 array of zeros
  * repeat(a, n, axis) : Repeat a, n times (same shape as a, except along given axis)
  * zeros()

* Access

![](images/20210316_153208.png)

* Operation
  * \* n : scalar multiplication
  * \/ n : scalar division
  * a @ b : Equivalent to a.matmul(b)
  * a + b : element wise sum
  * a - b : element wise difference
  * a * b : element wise product
  * a / b : element wise division
  * array2string(x, precision=2, separator=',', suppress_small=True) : [0.  ,1.24,2.  ]
  * array2string(x, formatter={'float_kind':lambda x: "%.2f" % x}) : [0.00 1.24 2.00]
  * a.dot(b) : cannot use scalars. matrices are broadcast together as if matrices were elements
  * a.multiply(b) : Element-wise multiplication
  * invert(x)
  * lexsort((b,a))                     # Sort by a, then by b → array([2, 0, 4, 6, 5, 3, 1])
  * log() : elementwise log
  * logical_not(x)
  * logical_and|or|xor(x1, x2)
  * mean(a) : sum of all array elements
  * np.flip(temp, axis = 1) : flip horizontally
  * power() : elementwise power
  * round() : round matrix
  * split(ary, sections) : Split an array into n+1 sections (if sections is int, equal size)
  * sum(a) : sum of all array elements
    * axis=0 : for each column
    * axis=1 : for each row
  * unravel_index()
  * where(a < 3, a, 10*a) : array([0, 1, 2, 3, 4, 5]) -> array([ 0,  1,  2, 30, 40])

![](images/20210316_153045.png)

* arraysplit()

![](images/20210316_153106.png)

* meshgrid()

![](images/20210316_151654.png)

* File
  * load('data.npy')
  * loadtxt("file_name", dtype=np.float32)
  * save('data.npy', num_arr)

{% tabs %}
{% tab title='read_save.py' %}

```py
# read | save file using numpy

# Shape
a = np.random.rand(10,11,12,2,3)
b = np.random.rand(10,11,12,3,4)
print(a.dot(b).shape) # (10, 11, 12, 2, 10, 11, 12, 4)
print((a @ b).shape)  # (10, 11, 12, 2, 4)

to_homog = lambda p: p[:-1] / p[-1]  # Homogeneous to euclidean

np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True) # softmax
```

{% endtab %}
{% tab title='gaussian_filter.py' %}

```py

def gaussian2d(filter_size=7, sig=1.0):
  """ Creates 2D Gaussian kernel with side length `filter_size` and a sigma of `sig`. """
  ax = np.arange(-filter_size // 2 + 1., filter_size // 2 + 1.)
  xx, yy = np.meshgrid(ax, ax)
  kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sig))
  return kernel / np.sum(kernel)
```

{% endtab %}
{% tab title='line_intersect.py' %}

```py
import numpy as np
def get_intersect(a1, a2, b1, b2):
  """
  Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
  a1: [x, y] a point on the first line
  a2: [x, y] another point on the first line
  b1: [x, y] a point on the second line
  b2: [x, y] another point on the second line
  """
  s = np.vstack([a1,a2,b1,b2])        # s for stacked
  h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
  l1 = np.cross(h[0], h[1])  # get first line
  l2 = np.cross(h[2], h[3])  # get second line
  x, y, z = np.cross(l1, l2) # point of intersection
  if z == 0:                 # lines are parallel
    return (float('inf'), float('inf'))
  return (x/z, y/z)
print(get_intersect((0, 0), (1, 1), (1, 0), (0, 1)))
print(get_intersect((0, 0), (1, 1), (1, 1), (2, 2)))
```

{% endtab %}
{% endtabs %}

* Gven a and b are both (3, 2)
  * np.stack((a, b)) : (2, 3, 2)
  * np.array((a, b))
  * np.vstack((a, b)) : (6, 2)
  * np.hstack((a, b)) : (3, 4)
  * np.dstack((a, b)) : (3, 2, 2) = np.concatenate(a[..., None], b[..., None]), axis=2)

![](images/20210301_194725.png)

> linalg

* dot(a, b) : if both scalars, 1D arrays then a scalar is returned; otherwise an array is returned
* eig(np.diag((1, 2, 3))) : get eigenvalue
* lstsq(a, b) : a = (M, N), b= (M,) or (M, K), returns x, sum residuals, rank, singular
* norm(a)


{% tabs %}
{% tab title='polynomial_regression.py' %}

```py
# Polyfit and draw
x = [0, 2000]
f = np.poly1d(np.polyfit([2, 7], [3, 5], 1))
plt.plot(x, f(x), '-')

data = [d for d in data if 'user|ageInSeconds' in d and d['user|ageInSeconds'] < 60*60*24*365*100]
X = [[1, d['user|ageInSeconds'], d['beer|ABV']] for d in data] # two feature
X = [[1, d['beer|ABV'], d['beer|ABV'] ** 2] for d in data]     # polynomial
y = [d['review|overall'] for d in data]
theta, residuals, rank, s = np.linalg.lstsq(X, y)
```

{% endtab %}
{% endtabs %}

> Random

* rand(d0, d1, …, dn) : Random values in a given shape
* randn(d0, d1, …, dn) : Standard normal distribution
* randint(low[, high, size, dtype]) : Random integers from [low, high)
* shuffle(x) : Modify sequence in-place by shuffling its contents
* seed([seed]) : Seed the generator
* beta(a, b[, size]) : Draw samples from a Beta distribution
* geometric(p[, size]) : Draw samples from the geometric distribution
* uniform(-1,0,1000) : Generate 1000 uniform number
* randint(2, size=10) : array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])

> sort

* a[a[:,1].argsort()] : Sort array by first column
* np.argpartition(a, -4)[-4:] : get unsorted top 4
* arr[(-arr).argsort()[:4]] : get sorted top 4
* z = np.maximum(0, z) : Relu using numpy

### Pandas

* Panel Data library

* concat(axis=0) : if contains at least one DataFrame, return df
* read_json(typ=’frame’)
* unique(values) : Uniques are returned in order of appearance
* display.max_rows | columns
* display.max_colwidth

> DataFrame

* Dataframe is multiple series that share the same index
* DataFrame(data=None)
* axes : list representing the axes of the DataFrame
* columns, index : column|row labels of the DataFrame
* dtypes : types of columns in the DataFrame
* shape : tuple representing dimensionality of DataFrame
* values : Numpy representation of the DataFrame

* access
  * [colname] : return Series corresponding to colname
  * describe() : quick statistic
  * duplicated([col], keep=First) : Mark duplicates as True except for first
  * head(n) : first n rows
  * iloc(r_index) : select a single row or list of row (starting from 0)
  * isin(values) : True at a location if all the labels match
  * isna(df1) : boolean mask where values are nan
  * iterrows() : iter(idx, row_sr), ignore dtypes across rows
  * itertuples() : iter(row_df)
  * iloc(row) : return Series
  * isin(lists) : filter only in lists
  * loc(r_name) : select a single row or list of rows
  * tail(n) : last n rows
  * value_counts()

![](images/20210301_194925.png)

```py
options.display.float_format = '{:,100f}'.format
read_csv()

# Modify
append(other)      # Append column and return new dataframe
apply(axis=0}      # Apply function to each columnl or row(axis=1)
drop('row', axis=0, inplace=True) # Remove row (axis=0), col (axis=1)
dropna(how='any')                 # Drop any rows that have missing data
drop_duplicates(subsets)          #
fillna(value=None)                # Fill missing data with value
insert(loc, column, value)        # Insert column in DataFrame at specified location
reset_index(drop=False)           # Convert index to column
sort_values(by='col')             # Sort dataframe by 'col' column
to_numpy()                        # Axes labels will be removed
rename(index=None, columns=None, inplace=F)    # Alter axes labels
set_axis(labels, axis=0, inplace=False)        # Assign desired index to given axis
to_csv(index=True) / to_sql(name, conn)        # Save as csv / sql file

> Example
dp.loc[‘tom’] == dp.iloc[0]
dp.loc[[‘tom’, ‘nick’], [‘score’]]
df[(df['score'] > 70) & (df['age'] < 20)] # multiple condition
df.rename(index={0: "x", 1: "y", 2: "z"}) # rename index
df.rename(columns={"A": "a", "B": "c"})   # rename columns
df.groupby('age').max()

# to_sql
engine = sqlalchemy.create_engine("postgresql://user:password@host:port|database")

# preprocess
data['clean'] = data['text'].apply(lambda x: "".join([ch for ch in x if ch not in string.punctuation]))
data['tokens'] = data['clean'].apply(lambda x: re.split('\W+', x))
data['stops'] = data['tokens'].apply(lambda x: [w for w in x if w not in stopwords])
ps = nltk.PorterStemmer()
data['stem'] = data['stops'].apply(lambda x: [ps.stem(w) for w in x])
```

{% tabs %}
{% tab title='display_side.py' %}

```py
import pandas as pd

def display_side(*args):
  from IPython.display import display_html
  html_str = ''
  for df in args:
    if isinstance(df, pd.Series):
      df = pd.DataFrame(df)
    if not isinstance(df, pd.DataFrame):
      html_str += df.render(index= False)
    else:
      html_str += df.to_html(index= False)
  display_html(html_str.replace('table', 'table style="display:inline"'), raw=True)

display_side(pd.DataFrame([1,2,3]), pd.DataFrame([2,3,4]))
```

{% endtab %}
{% endtabs %}

> Series

* built on top of a numpy array and have a named index
* arithmetic converts to float

* Acesss
  * head(n) : first n rows
  * to_list() : return list ignoring all index
  * tail(n) : last n rows

* Function
  * T : Return the transpose, which is by definition self.
  * array : The ExtensionArray of the data backing this Series or Index.
  * at : Access a single value for a row/column label pair.
  * attrs : Dictionary of global attributes on this object.
  * axes : Return a list of the row axis labels.
  * dtype : Return the dtype object of the underlying data.
  * hasnans : Return if I have any nans; enables various perf speedups.
  * iat : Access a single value for a row/column pair by integer position.
  * iloc : Purely integer-location based indexing for selection by position.
  * index : The index (axis labels) of the Series.
  * is_monotonic_decreasing() : Return boolean if values in the object are monotonic_decreasing.
  * is_monotonic_increasing() : Return boolean if values in the object are monotonic_increasing.
  * isna(self) : Detect missing values
  * is_unique : Return boolean if values in the object are unique.
  * loc : Access a group of rows and columns by label(s) or a boolean array.
  * nbytes : Return the number of bytes in the underlying data.
  * ndim : Number of dimensions of the underlying data, by definition 1.
  * shape : Return a tuple of the shape of the underlying data.
  * size : Return the number of elements in the underlying data.
  * values : Return Series as ndarray of ndarray-like depending on the dtype.

* Modify
  * apply(func) : apply function in every element
  * get(key, default=N)
  * mean(axis=N, skipna=N, level=N, numeric_only=N)

### Plot

> matplot

* 0 is black 1 is white
* Matplotlib only supports PNG images
* float32 and uint8 (only float32 greyscale)
* axis('off') : Remove axis
* imshow(img, cmap) → None        # Display Image ('gray')
* fig.colorbar(im, ax=ax)

![](images/20210309_003050.png)

{% tabs %}
{% tab title='types.py' %}

```py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, axs = plt.subplots(2, 3)
axs[0, 0].set_title('1 : scatter')
axs[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

axs[0, 1].set_title('2 : line')
axs[0, 1].plot([1, 2, 3, 4], [1, 4, 9, 16])

axs[0, 2].set_title('3 : heatmap')
axs[0, 2].imshow(np.random.random((16, 16)), cmap='hot', interpolation='nearest')

axs[1, 0].set_title('4 : bar')
axs[1, 0].bar(['A', 'B', 'C'], [1, 5, 3])

axs[1, 1].set_title('5 : curve')
axs[1, 1].plot(np.linspace(0, 2 * np.pi, 400), np.sin(np.linspace(0, 2 * np.pi, 400) ** 2))

X, Y = np.meshgrid(np.arange(-5,6,1), np.arange(-5,6,1))
u, v = X|5, -Y|5
axs[1, 2].quiver(X,Y,u,v)

plt.show()

for ax in axs.flat:
  ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
  ax.label_outer()
```

{% endtab %}
{% tab title='types.py' %}

![](images/20210309_010526.png)

```py
from cv2 import cv2
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 5)

dog_np = cv2.cvtColor(cv2.imread('data/dog.jpg'), cv2.COLOR_BGR2RGB)
axs[0].imshow(dog_np)
axs[0].axis('off')

axs[1].imshow(cv2.imread('data/dog.jpg', cv2.IMREAD_GRAYSCALE))
axs[1].axis('off')

axs[2].imshow(cv2.resize(dog_np,(300, 600)))
axs[2].axis('off')

axs[3].imshow(cv2.resize(dog_np, (0,0), dog_np, 1, 0.5))
axs[3].axis('off')

axs[4].imshow(cv2.flip(dog_np, -1))
axs[4].axis('off')

cv2.imwrite("data/dog_np.jpg", dog_np)
```

{% endtab %}
{% endtabs %}

> seaborn

* seaborn.countplot(Y_train)
  * Y_train = [1,2,3,4,5,6,7,5,7,4,58,45,2,4,53,45,2]

![](images/20210309_002938.png)

### Deep Learning

> pytorch

![](images/20210301_195612.png)

* [Transfer](https://gist.github.com/SeanHwangG/f16bbb0beba182251d2b6c147a5c7b9a)
* [Backward](https://gist.github.com/SeanHwangG/cfd2ff68f7f2e5b086cde701b35f8e18)

vector is 1d tensor

module    # Base class for all neural network modules. models should also subclass this class
parameter    # A kind of Tensor that is to be considered a module parameter
tensor        # multi-dimensional matrix containing elements of a single data type

```py
# save | load only the model parameters
torch.save(the_model.state_dict(), PATH)
the_model = TheModelClass(*args, **kwargs)
the_model.load_state_dict(torch.load(PATH))

# Save | load entire model
torch.save(the_model, PATH)
the_model = torch.load(PATH)

# Tensors
matrix-like data structures for deep learning libraries and efficient computation
Graphical Processing Units (GPUs) are especially effective at calculating operations between tensors

arr = np.array([1, 2, 3, 4, 5]) # shallow copy
torch.from_numpy(arr)           # share same memory as numpy
torch.as_tensor(arr)

torch.tensor(arr)               # deep copy + same dtype
torch.Tensor(arr)               # FloatTensor

torch.empty(4,2)                # zeros, ones, (_like)
torch.arange(1, 10)             # linspace

x.view(2, 5)                    # share same memory

# Random
torch.manual_seed(42)
torch.rand(2, 3)                # randn, randint
torch = torch.type(torch.int32) # change dtype

# operation
torch.add(a, b) | a + b
a.add_(b)                # in-place
a.mul(b)                 # element wise operation
a.dot(b)                 # dot product
torch.mm(a, b) | a @ b   # matrix multiplication

x.norm()
x.numel()

# loss
CrossEntropyLoss()
L1Loss(reduction='mean')        # measures MAE between each element in input xx and target yy
MSELoss(reduction='mean')        # squared L2 norm
```

* Variable
  * Variable class wraps a tensor, and allows automatic gradient computation on the tensor

> torchvision

[MNIST_KNN_PCA_CNN.ipynb](https://gist.github.com/SeanHwangG/13714cbe18c3a379397dc35c52da9cbe)

> torchtext

* Fields
  * Specify how preprocessing should be done
  * vocab.stoi : str2index information
  build_vocab()

* Dataset
  * load data
  * fields : information of dataset
  * vars(trainset[0]) : get inside content

* BucketIterator
  * batching and padding

[hello_rnn.ipynb](https://gist.github.com/SeanHwangG/90c8434a8f53cdac9561cdd6624a101e)
[lstm_music.ipynb](https://gist.github.com/SeanHwangG/b6044b7e1142f866551af4a4e230f94a)