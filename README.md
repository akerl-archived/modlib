modlib
=========

[![Latest Version](https://img.shields.io/pypi/v/modlib.svg?style=flat)](https://pypi.python.org/pypi/modlib/)
[![Coverage Status](https://img.shields.io/coveralls/akerl/modlib.svg?style=flat)](https://coveralls.io/r/akerl/modlib)
[![Build Status](https://img.shields.io/travis/akerl/modlib.svg?style=flat)](https://travis-ci.org/akerl/modlib)
[![MIT Licensed](https://img.shields.io/badge/license-MIT-green.svg?style=flat)](https://tldrlegal.com/license/mit-license)

Simplifies importing dynamic modules. It exposes the Modstack class, which collects modules as you import them. If you need the same module again, it will return the existing module from the stack rather than reimporting it. It also supports getting a specific item from the modules rather than the full module

## Usage

The basic usage is pretty straightforward:

```
import modlib

stack = modlib.Modstack
names = ['foo.bar', 'alpha', 'hello.world']
modules = { x: stack.get(x) for x in names }
```

It's possible to use a custom formula for your module path. The default is `'{0}'`, which takes the name you pass to `.get()` directly. This is useful if your modules follow a common pattern. For instance, if your modules are stored in `./modules/{kind}/{name}`, you can pass that parameter to Modstack:

```
import modlib

stack = modlib.Modstack(formula='modules.{kind}.{name}')
fruits = ['apple', 'orange', 'tomato']
fruit_modules = { x: stack.get(kind='fruit', name=x) for x in fruits }
```

You can also specify a target object, and only that object will be pulled from the module. For instance, if you want to pull the run() method from each of your modules:

```
import modlib

stack = modlib.Modstack(target='run')
actions = ['jump', 'swim', 'bike']
action_methods = { x: stack.get(x) for x in names }
```

## Installation

    pip install modlib

## License

modlib is released under the MIT License. See the bundled LICENSE file for details.

