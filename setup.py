from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='doxybook',
    version='3.0.0',
    description='Convert Doxygen XML to GitBook or Vuepress markdown files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/matusnovak/doxybook',
    author='Matus Novak',
    author_email='matusnov@gmail.com',
    license='MIT',
    keywords='doxygen gitbook vuepress markdown generator',
    packages=['doxybook', 'doxybook.templates'],
    install_requires=['Jinja2'],
    entry_points={
        'console_scripts': [
            'doxybook=doxybook:main',
        ],
    },
)
