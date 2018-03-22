from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='doxybook',
    version='2.0.0',
    description='Doxygen XML to GitBook markdown',
    long_description=long_description,
    url='https://github.com/matusnovak/doxybook',
    author='Matus Novak',
    author_email='matusnov@gmail.com',
    license='MIT',
    keywords='doxygen gitbook markdown generator',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'doxybook=doxybook:main',
        ],
    },
)
