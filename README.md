modlib
=========

[![Latest Version](https://img.shields.io/pypi/v/modlib.svg)](https://pypi.python.org/pypi/modlib/)
[![Coverage Status](https://img.shields.io/coveralls/akerl/modlib.svg)](https://coveralls.io/r/akerl/modlib)
[![Build Status](https://img.shields.io/travis/akerl/modlib.svg)](https://travis-ci.org/akerl/modlib)
[![MIT Licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://tldrlegal.com/license/mit-license)

Simplifies importing dynamic modules. It exposes the Modstack class, which collects modules as you import them. If you need the same module again, it will return the existing module from the stack rather than reimporting it. It also supports getting a specific item from the modules rather than the full module

## Usage

    import modlib

    Stack = modlib.Modstack
    Names = ['foo.bar', 'alpha', 'hello.world']
    Modules = { x: Stack.get(x) for x in Names }

## Installation

    pip install modlib

## License

modlib is released under the MIT License. See the bundled LICENSE file for details.

