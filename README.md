modlib - For collecting modules the wrong way with less badness
=====

Overview
-----

This module simplifies importing dynamic modules. It exposes the Modstack class, which collects modules as you import them. If you need the same module again, it will return the existing module from the stack rather than reimporting it. It also supports getting a specific item from the modules rather than the full module

How to use
-----

    import modlib
    
    Stack = modlib.Modstack
    Names = ['foo.bar', 'alpha', 'hello.world']
    Modules = { x: Stack.get(x) for x in Names }

