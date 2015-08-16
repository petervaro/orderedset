orderedset
==========

*Pure Python OrderedSet implementation built on top of collections.OrderedDict*


Description
-----------

`OrderedSet` is a collection of hashable objects, which also remembers the
injection order. This implementation is a bit dirty and quick hack to create a
pure python object based on `collections.OrderedDict`. It is very light, and
has absolutely no dependencies. All functions and *operators* defined on the
built-in `set` object are also available on `OrderedSet`.


Dependencies
------------

None.


Installation
------------

On Linux and Macintosh:

```
$ git clone https://github.com/petervaro/orderedset.git
$ cd orderedset
$ sudo python3 setup.py install
```

Usage
-----

Create an `OrderedSet` of various items and print it:

```python
from orderedset import OrderedSet

s = OrderedSet(['hello', True, None, 1, 3.14])
print(s)
for i, item in enumerate(s):
    print(i, '=>', item)
```

And the output is:

```
OrderedSet(['hello', True, None, 3.14])
0 => hello
1 => True
2 => None
3 => 3.14
```

> ***NOTE:*** One very important difference is, that an `OrderedSet` can only
> be compared to another `OrderedSet` via the `==` and `!=` operators. Also
> two `OrderedSet`s are equal if and only if both have the exact same items and
> their orders are the same as well.
