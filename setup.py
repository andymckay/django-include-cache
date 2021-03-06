from setuptools import setup

version = '0.1'

setup(name='django-include-cache',
      version=version,
      description="Include Cache for Django",
      long_description=open("readme.rst").read() + "\n",
      classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        ],
      keywords='',
      packages=['include_cache'],
      author='Mozilla',
      author_email='andym@mozilla.com',
      url='http://mozilla.com',
      license='MPL',
      zip_safe=True,
      )
