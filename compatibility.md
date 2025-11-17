# Compatibility

Most of the programs in this repository will work on every Python version 2.x and 3.x.

However, some programs use certain functions and syntax that is not compatible with all versions of Python.

For example, the walrus operator `:=` that allows for assignment within list comprehension was only introduced in Python 3.8 (Oct 2019), and the `reduce()` function in Python 2.X was [removed in Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html#builtins) (but can still be accessed via an import of `functools.reduce()`).

Programs that use version-specific syntax will likely have a comment in the solution denoting this. Regardless, here's a list of all the programs that are version-dependent : 

| Problem Number        | Version Requirement | Reason     | Alternative? |
|-----------------------|---------------------|------------|--------------|
| [0268](codes/0268.py) | <= 2.7              | `reduce()` | `functools`  |
| [0898](codes/0898.py) | <= 2.7              | `reduce()` | `functools`  |
| [0922](codes/0922.py) | <= 2.7              | `reduce()` | `functools`  |
| [1221](codes/1221.py) | >= 3.2              | `accumulate()` | No Alternative  |
| [1423](codes/1423.py) | >= 3.8              | `:=`       | No Alternative |
| [1486](codes/1486.py) | <= 2.7              | `reduce()` | `functools`  |
| [1835](codes/1835.py) | <= 2.7              | `reduce()` | `functools`  |
| [2248](codes/2248.py) | <= 2.7              | `reduce()` | `functools`  |
| [2708](codes/2708.py) | <= 2.7              | `reduce()` | `functools`  |
| [2788](codes/2788.py) | <= 2.7              | `reduce()` | `functools`  |
| [3622](codes/3622.py) | <= 2.7              | `reduce()` | `functools`  |
| [3688](codes/3688.py) | <= 2.7              | `reduce()` | `functools`  |