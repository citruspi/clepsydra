#!/usr/bin/env python
# -*- coding: utf8 -*-

import clepsydra


def task(_state, name):
    _state['message'] = 'hello {}'.format(name)


class Dog(object):
    def talk(self, _state, count):
        _state['message'] = 'woof'*count


def test_function():
    state = clepsydra.run(task, timeout=2, name='world')

    assert state['message'] == 'hello world'
    assert not(state['timer_triggered'])


def test_method():
    state = clepsydra.run(Dog().talk, timeout=2, count=5)

    assert state['message'] == 'woofwoofwoofwoofwoof'
    assert not(state['timer_triggered'])
