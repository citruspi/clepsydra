#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import clepsydra


def multisecond_task(_state):
    _state['count'] = 0

    while True:
        _state['count'] += 1
        time.sleep(1)


def subsecond_task(_state):
    _state['count'] = 0

    while True:
        _state['count'] += 0.01
        time.sleep(0.01)


def test_multisecond_timer():
    state = clepsydra.run(multisecond_task, timeout=5)

    assert (4 <= state['count'] <= 5)
    assert state['timer_triggered']


def test_subsecond_timer():
    state = clepsydra.run(subsecond_task, timeout=0.08)

    assert (0.07 <= state['count'] <= 0.08)
    assert state['timer_triggered']
