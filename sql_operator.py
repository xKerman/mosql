#!/usr/bin/env python
# -*- coding: utf-8 -*-

EMPTY = object()

def to_keyword(key):
    '''It converts the attribute name to the SQL keyword.

    Examples:

        from_    -> form
        order_by -> order by
        values_  -> values
    '''
    return key.replace('_', ' ').rstrip()

def flat(obj):
    '''It flats an object.

    Examples:

        'str'      -> 'str'
        1          -> '1'
        ('x', 'y') -> 'x, y'
        callable   -> flat(callable())
    '''

    if isinstance(obj, basestring):
        return obj
    elif callable(obj):
        return flat(obj())
    elif hasattr(obj, '__iter__'):
        return ', '.join(flat(item) for item in obj)

    return str(obj)

def param(key):
    return '?'

def eq(key, value=EMPTY):
    if value is EMPTY:
        value = param(key)
    else:
        value = "'%s'" % value.replace("'", "''")
    return '%s=%s' % (key, value)
