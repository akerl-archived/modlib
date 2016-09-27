modlib
=========

[![Latest Version](https://img.shields.io/pypi/v/modlib.svg?style=flat)](https://pypi.python.org/pypi/modlib/)
[![Build Status](https://img.shields.io/circleci/project/akerl/modlib/master.svg)](https://circleci.com/gh/akerl/modlib)
[![Dependency Status](https://img.shields.io/gemnasium/akerl/modlib.svg)](https://gemnasium.com/akerl/modlib)
[![Coverage Status](https://img.shields.io/codecov/c/github/akerl/modlib.svg)](https://codecov.io/github/akerl/modlib)
[![Code Quality](https://img.shields.io/codacy/a34888f436a94926bd65f8e20210a9d1.svg)](https://www.codacy.com/app/akerl/modlib)
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

The module's object is returned by .get(), so `my_module = modlib.Modstack.get('foobar')` is equivalent to `import foobar as my_module`: if foobar.py has a "say_something" function, you'd call it with `my_module.say_something()`

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

When specifying a target object, .get() returns that object. So if you have foobar.py that defines say_something(), loading the module with `my_method = modlib.Modstack(target='say_something').get('foobar')` would let you run say_something as `my_method()`

## Installation

    pip install modlib

## License

modlib is released under the MIT License. See the bundled LICENSE file for details.

