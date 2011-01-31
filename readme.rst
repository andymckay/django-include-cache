django-include-cache
------------------

If you've got a large number of includes in your Django urls.py, then there
can be a performance hit in accessing urls at the bottom of the includes as
Django searches through multiple url patterns to find the match.

This monkey patches URLResolvers so that when the right pattern is found we
cache that pattern and move it to the top of the url pattern stack so it will
be found quicker.

In completely unscientific tests on one site, before:

Requests per second:    438.49 [#/sec] (mean)

After:

Requests per second:    585.39 [#/sec] (mean)

Installation
=================

1. Install from pypi::

   pip install django-include-cache

2. In manage.py (or your wsgi script) add::

    import include_cache
    include_cache.patch()

Author: Andy McKay
