from setuptools import setup
from subprocess import Popen, PIPE


def git_describe_abbrev():
    try:
        p = Popen(['git', 'describe', '--abbrev=0'],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return line.strip().decode('utf-8')[1:]

    except:
        return None


README = """
DoxyBook
========

Please follow the information provided on GitHub here: https://github.com/matusnovak/doxybook
"""

setup(
    name='doxybook',
    version=git_describe_abbrev(),
    description='Convert Doxygen XML to GitBook or Vuepress markdown files',
    long_description=README,
    long_description_content_type='text/x-rst',
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
