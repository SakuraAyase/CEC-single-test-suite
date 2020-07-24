from setuptools import Extension
from distutils.core import setup
from setuptools.command.test import test as TestCommand
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import sys

# cython = Extension('ea.cbenchmarks',
#    sources = ['ea/cbenchmarks.pyx'],
##    include_dirs = ['include/']
#)
sourcefiles = ['cec2019comp100digit/cec2019comp100digit.pyx']

sourcefiles += ['cec2019comp100digit/eval_func.cpp', 'cec2019comp100digit/cec19_func.cpp']

cec2019comp100digit = Extension("cec2019comp100digit.cec2019comp100digit",
                        sourcefiles,
                        include_dirs=['cec2019comp100digit/'],
                        language="c++",
                        extra_compile_args=["-std=c++11"])  # Unix-like specific


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='cec2019comp100digit',
    version='0.8',
    author='Daniel Molina',
    author_email='dmolina@decsai.ugr.es',
    maintainer='Daniel Molina',
    description='Package for benchmark for the \
    100 digit competition on the IEEE \
    Congress on Evolutionary Computation CEC\'2019',
    long_description=open('README.rst').read(),
    license='GPL V3',
    url='https://github.com/dmolina/cec2019comp100digit',
    packages=['cec2019comp100digit'],
    install_requires=['cython', 'numpy'],
    ext_modules=[cec2019comp100digit],
    package_data={'cec2019comp100digit': ['input_data/*.txt'],
                  '': ['*.h']},
    tests_require=['pytest'],
    cmdclass={'build_ext': build_ext, 'test': PyTest},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ]
)
