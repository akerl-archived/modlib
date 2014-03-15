import unittest
import modlib
import sys
import os


class TestModlib:
    def test_modstack(self):
        stack = modlib.Modstack()
        names = ['apple', 'orange', 'tomato']
        for i in [1, 2]:
            modules = {x: stack.get('mock.' + x) for x in names}
            for x in names:
                assert modules[x].name() == x

    def test_formula(self):
        stack = modlib.Modstack(formula='mock.{name}')
        names = ['apple', 'orange', 'tomato']
        modules = {x: stack.get(name=x) for x in names}
        for x in names:
            assert modules[x].name() == x

    def test_target(self):
        stack = modlib.Modstack(target='name')
        names = ['apple', 'orange', 'tomato']
        modules = {x: stack.get('mock.' + x) for x in names}
        for x in names:
            assert modules[x]() == x
