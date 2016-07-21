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
        - [Putting it All Together](#markdown-header-putting-it-all-together)

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

### Putting it All Together

[Example](code/strings-and-collections.py)

## Modularity

### Creating, Running, and Importing a Module
