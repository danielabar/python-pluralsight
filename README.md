<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python Fundamentals](#markdown-header-python-fundamentals)
    - [Getting Started With Python 3](#markdown-header-getting-started-with-python-3)
        - [Scalar Types](#markdown-header-scalar-types)
        - [Relational Operators](#markdown-header-relational-operators)
        - [Conditional Statements](#markdown-header-conditional-statements)
        - [While Loops](#markdown-header-while-loops)
    - [Strings and Collections](#markdown-header-strings-and-collections)
        - [Strings](#markdown-header-strings)
        - [Bytes](#markdown-header-bytes)
        - [Lists](#markdown-header-lists)
        - [Dictionaries](#markdown-header-dictionaries)
        - [For Loops](#markdown-header-for-loops)
        - [Putting it all together](#markdown-header-putting-it-all-together)
    - [Modularity](#markdown-header-modularity)
        - [Creating, Running, and Importing a Module](#markdown-header-creating-running-and-importing-a-module)
        - [Defining Functions and Returning Values](#markdown-header-defining-functions-and-returning-values)
        - [Distinguishing Between Module Import and Module Execution](#markdown-header-distinguishing-between-module-import-and-module-execution)
        - [The Python Execution Model](#markdown-header-the-python-execution-model)
        - [Main Functions and Command Line Arguments](#markdown-header-main-functions-and-command-line-arguments)
        - [Sparse is better than Dense](#markdown-header-sparse-is-better-than-dense)
        - [Documenting Using Docstrings](#markdown-header-documenting-using-docstrings)
        - [Documenting With Comments](#markdown-header-documenting-with-comments)
        - [The Whole Shebang](#markdown-header-the-whole-shebang)
    - [Objects](#markdown-header-objects)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Python Fundamentals

> My course notes from [Python Fundamentals](https://app.pluralsight.com/library/courses/python-fundamentals/table-of-contents) course on Pluralsight.

## Getting Started With Python 3

### Scalar Types

__int__

signed, arbitrary precision integer, eg `42`, specified in decimal but also can be binary with `0b` prefix, octal with `0o` prefix, or hex with `0x` prefix. Can also use constructor to convert other numeric types to int, for example `int(3.5)` returns `3` (rounds down). Strings can be converted to ints `int("496")` returns 496.

__float__

64-bit floating point numbers, implemented as IEEE-754 double precision floating point numbers with 53 bits of binary precision, which is around 15 to 16 bits of decimal precision.

any literla number containing a decimal point or `E` is interpreted as a float.

Can use scientific notation, for example `3e8`, which is 3 x 10 to power of 8, `1.616e-35` is 1.616 x 10 to power of negative 35.

`float` constructor can be used to convert other tyoes to float, for example int `float(7)` returns `7.0`, `float("1.618")` returns 1.618.

Can also create "not a number", and positive/negative infinity `float("nan")`, `float("inf")`, `float("-inf")`

Any calculation involving int and float is promoted to float, `3.0 + 1` is `4.0`.

__None__

The null object. The solve value of NoneType, used to represent absence of a value, not displayed by REPL.

Can be assigned to a variable `a = None`. Can test whether a variable is null `a is None` returns true.

__bool__

Boolean logical value, either `True` or `False`.

bool constructor can be used to convert other types. For integers, `bool(0)` is falsey, and all other int values are truthy.
Same behaviour with floats `bool(0.0)` is falsey, any other float is truthy.

Empty list is falsey `bool([])`, populated list is truthy `bool([1, 3, 5])`.

Empty string is falsey `bool("")`, any other non empty string is truthy.

### Relational Operators

Two objects are _equivalent_ if one could be used in place of the other.

`==` value equality / equivalence

`!=` value inequality / inequivalence

`<` less than

`>` greater than

`<=` less than or equal to

`>=` greater than or equal to

### Conditional Statements

```python
if expr:
  print("expr is True")
```

`expr` is converted to bool as if by the `bool()` constructor. So this evaluates to `True`

```python
if "eggs":
  print("Yes please!")
```

Optional else clause:

```python
h = 42
if h > 50:
  print("Greater than 50")
else:
  print("Less than 50")
```

Rather than nesting an `if` block in an `else` block, use `elif` keyword, because "zen of python" - "flat is better than nested"

### While Loops

`while` statment terminated by a colon because it introduces a new block. `expr` is converted to `bool` as if by the `bool()` constructor.

```python
while expr:
  print("loop while expr is True")
```

```python
c = 5
# equivalent would be: while c:, but more idiomatic python to be explicit as below:
while c != 0:
  print(c)
  c -= 1
```

`break` keyword terminates innermost loop and transfers execution to the first statement after the loop.

```python
while True:
  if expr:
    break
print("Go here on break")
```

## Strings and Collections

### Strings

data type `str`. Immutable sequences of Unicode codepoints. Codepoints are roughly like characters though not strictly equivalent.
Once a string is constructed, cannot modify its contents.

Literal strings are delimited by either single or double quotes, but must be consistent within a single string:

```python
'This is a string'
"This is also a string"
```

Adjacent strings are concatenated into a single string

```python
>>> "first" "second"
'firstsecond'
```

Newline options:

__Multiline strings__ - delimited by three quote characters (can be double or single quotes)

```python
>>>"""This is
a multiline
string"""
'This is\na multiline\nstring'
```

__Escape sequences__

Embed the newline control character right in the string

```python
>>> m = 'This string\nspans multiple\nlines'
```

Note Python 3 gas _Universal Newlines_, so no need on Windows to specify carriage return `\r\n`,
rather `\n` is translated to the native newline sequence on whatever platform the code is running on.

__Raw Strings__

"what you see is what you get". To avoid ugly escape sequences, especially useful with Windows paths.
To use it, precede string with `r'`

```python
>>> path = r'C:\Users\Merlin\Documents\Spells'
>>> path
'C:\\Users\\Merlin\\Documents\\Spells'
```

Strings are _sequence types_, which means they support common operations for querying sequences.

Can access certain characters in string using square brackets:

```python
>>> s = 'parrot'
>>> s[4]
'o'
>>> type(s[4])
<class 'str'>
```

There is no separate character type from string type. Characters are simply one element strings.

String objects support many operations, type `help(str)` in repl. For example:

```python
>>> c = 'oslo'
>>> c.capitalize()
'Oslo '
```

__Unicode__

Python strings are unicode, unicode characters can be used in string literals because default soruce encoding is UTF-8.

### Bytes

Immutable sequences of bytes. Used for raw binary data and fixed width single byte character encoding such as ASCII.

Byte literals `b'data'` or `b"data"`.

Support many of same operations that strings do such as indexing and splitting.

To convert between strings and bytes, must know the encoding of the byte sequence used to represent the strings unicode codepoints as bytes.

encode: str to bytes
decode: bytes to str

### Lists

Mutable sequence of objects. List literals delimited by square brackets: `[a, b, c, d]`.

Items can be retrieved with square brackets and zero-based index:

```python
>>> a = ["apple", "orange", "pear"]
>>> a[1]
'orange'
```

Elements can be replaced by assigning to a specific element `a[1] = 7`.

Lists can contain different types.

To create an empty list `b = []`. To add an item `b.append(1.6)`.

List constructor can be used to create a list from another collection such as a string:

```python
>>> list("abcd")
['a', 'b', 'c', 'd']
```

### Dictionaries

Mutable mappings of keys to values.

Dict literals `{k1: v1, k2: v2}`. Items can be retrieved and assigned by key using square brackets:

```python
>>> d = {'alice': '123', 'bob': '456'}
>>> d['alice']
'123'
>>> d['bob'] = 999
```

If assign to a key that doesn't exist yet, a new entry will be added.

Entries are not stored in any particular order.

To create an empty dictionary `e = {}`

### For Loops

Visit each item in an iterable series. General form is:

```python
for item in iterable:
  ...body...
```

```python
cities = ["London", "New York", "Paris"]
for city in cities:
  print(city)
```

Can also iterate over dictionary, which gets keys:

```python
colors = {'crimson': 0xdc143c, 'coral': 0xff7f50}
for color in colors:
  print(color, colors[color])
```

Outputs:
```
coral 16744272
crimson 14423100
```

### Putting it all together

[Example](code/strings-and-collections.py)

## Modularity

### Creating, Running, and Importing a Module

Module like [words.py](code/words.py) can be imported into the REPL, omit the file extension:

```python
>>> import words
... program output...
```

When importing a module, code in it is executed immediately. To have more control over when code is executed and reuse, move code into a function.

### Defining Functions and Returning Values

Functions are defined with `def` keyword, followed by function name, and arguments in parenthesis.

```python
def square(x):
  return x * x

// invoke square
square(5)  // 25
```

Functions don't need to return a value and can produce side effects. Can return early from a function by using `return` keyword with no parameter.

### Distinguishing Between Module Import and Module Execution

When all the code in the module is organized into functions, then importing it will not execute anything right away (besides just defining the functions):

```python
>>> import words
>>> words.fetch_words()
```

Can also import just a specific function:

```python
>>> from words import fetch_words()
>>> fetch_words()
```

Notice that running the module now from OS cli `python words.py` will not do anything, because all executing it now does is define a function then immediately exit.

To make a module with useful functions AND which can be run as a script, need to use _special attributes_, which are delimited by __double underscores__.

`__name__` - evalutes to `__main__` or the actual module name depending on how the enclosing module is being used. Used to detect whether module is being run as a script or being imported into another module or the REPL.

[Example](code/words_special.py)

For example, add `print(__name__)` as last line in module, then when imported into the REPL, will print out the module name, for example "words-special".

Note if module is imported a second time in the same session, print statement will NOT run again, because module code is only executed once on first import (singleton?).

Now running the script at OS cli `python words_special.py` outputs `__main__`.

Module can use this behaviour to detect how its being used.

### The Python Execution Model

`def <some_function>()` is not a declaration, its a statement that when used in sequence with top level module scope code, causes the code within the function to be bound to the name of the function.

When modules are imported or run, all of the top level statements are run, this is how functions within the module namespace are defined.

By `.py` file is a Python module. But modules can be written for convenience import, convenience execution, or using the `if __name__ == '__main__'` idiom, both import and execution.

__Python module__ - Conveninet import with API.

__Python script__ - Conveninet execution from command line.

__Python program__ - Possibly composed of many modules.

Recommend making even simple scripts importable, to make development and testing easier.

### Main Functions and Command Line Arguments

[Example](code/words_cli.py)

This refactor supports testing the individual functions and all together from the REPL. Note multiple functions can be imported from a module with a single import statement:

```python
>>> from words_cli import (fetch_words, print_items)
>>> print_items(fetch_words())
```

Can also import _everything_ from a module, but not generally recommended because you can't control what gets imported, which can cause namespace collisions:

```python
>>> from words_cli import *
>>> fetch_words()
```

To accept command line arguments, use the `argv` attribute of the `sys` module, which is a list of strings:

```python
import sys
...

def main():
  url = sys.argv[1]
  words = fetch_words(url)
  print_items(words)
```

Issue with above is `main()` can no longer be tested from REPL because `sys.argv[1]` does not have a useful value in that environment.

Solution is to have `url` be a parameter to the `main` function, and pass in `sys.argv[1]` from the __main__ check.

More sophisticated cli parsing: `argparse`, also third party options such as `docopt`.

### Sparse is better than Dense

Top level functions have 2 blank lines between them. This is a convention for modern Python. (PEP 8 recommendation).

### Documenting Using Docstrings

API documentation in Python uses _docstrings_. Literal strings which occur as the first statement in a named block such as a function or module.

Use triple quoted strings even for a single line because it can easily be expanded to add more details later.
Recommend using Google's Python Style Guide, it can be machine parsed to generate html api docs, but still human readable.

Begin with short description of function, followed by list of arguments to function, and the return value.

After docstring is added, can access it via `help` in REPL:

```python
>>> from words-cli import fetch_words
>>> help(fetch_words)
```

Module docstrings are placed at the beginning of the module, before any statements. Then can request help on the module as a whole:

```python
>>> import words_cli
>>> help(words_cli)
```

### Documenting With Comments

Generally recommended to use docstrings, which explain how to _consume_ your code. And code should be clean enough not to require additional explanation of how it works, but sometimes this is needed. For example:

```python
if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
```

### The Whole Shebang

To allow program to be run as a shell script, add at beginning of file, the shebang line which tells the OS which interpreter to use to run the program -  `#!/usr/bin/env python`

## Objects
