#!/usr/bin/env python

from distutils.core import setup

setup(name='salt_grain_vultr',
      version='0.0.3',
      description='Vultr VPS metadata grain for SaltStack',
      author='Iggy',
      author_email='iggy@theiggy.com',
      url='https://github.com/saltstack-contrib/grains-vultr',
      py_modules=['_grains/vultr'],
     )
