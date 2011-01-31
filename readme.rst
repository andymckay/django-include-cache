django-cronjobs
------------------

This provide a @cron decorator to mark cronjob methods and
a namespace for managei.

Installation
=================

::
  pip install cronjobs

Add 'cronjobs' to your INSTALLED_APPS.

Usage
=================

Methods can be added to anywhere, but if you put them in a file called cron.py,
they will be automatically imported.

Register you method by decorating it with @register for example::
  from cronjobs import register
  @register
  def some_function():
      pass

You can then run::
  manage.py cron some_function


License: Mozilla Public License
Authors:  originally by Jeff Balogh, packaged and broken by Andy McKay
