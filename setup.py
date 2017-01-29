'''
Created on Jan 29, 2017

@author: Daniel McMahon
'''
from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Daniel McMahon",
      author_email="daniel40392@gmail.com",
      license="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )