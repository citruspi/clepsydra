#!/usr/bin/env python
# -*- coding: utf8 -*-

from threading import Timer
try:
    import _thread
except ImportError:
    import thread as _thread


def run(task, timeout, *args, **kwargs):
    kwargs['_state'] = {
        'timer_triggered': False
    }

    timer_ = Timer(timeout, lambda: _thread.interrupt_main())
    timer_.start()

    try:
        task(*args, **kwargs)
        timer_.cancel()
    except KeyboardInterrupt:
        kwargs['_state']['timer_triggered'] = True

    return kwargs['_state']
