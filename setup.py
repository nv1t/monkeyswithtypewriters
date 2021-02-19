# -*- coding: utf-8 -*-
import setuptools
import os

setuptools.setup(name='monkeyswithtypewriters',
      version='0.1',
      description='Tool for AutoType from String or File',
      url='https://github.com/nv1t/pyautotype',
      author='Jan Hoersch',
      author_email='jan.hoersch@securesystems.de',
      license='MIT',
      packages=['monkeyswithtypewriters'], 
      setup_requires=[
          'wheel',
      ],
      install_requires=[
          'pynput'
      ],
      entry_points = {'console_scripts': ['monkeyswithtypewriters = monkeyswithtypewriters.main:main']},
      zip_safe=False)
