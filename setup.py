from setuptools import setup, find_packages

setup(name='nbparameterise',
      version='0.3',
      url='https://github.com/takluyver/nbparameterise',
      license='MIT',
      packages=find_packages(),
      install_requires=['nbconvert', 'astsearch'])
