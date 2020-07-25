from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

#cython = Extension('ea.cbenchmarks',
#    sources = ['ea/cbenchmarks.pyx'],
##    include_dirs = ['include/']
#)
#
cec2013single = Extension("cec2013single.cec2013",
              ["cec2013single/cec2013.pyx", "cec2013single/cec2013_func.c"]) # Unix-like specific

setup(
	name='cec2013single',
        version='0.1',
        author='Daniel Molina',
        author_email='daniel.molina@uca.es',
        description='Package for benchmark for the Real Single Objective Optimization session on IEEE Congress on Evolutionary Computation CEC\'2013',
        long_description=open('README.rst').read(),
        license='GPL V3',
        packages=['cec2013single'],
        install_requires=['cython', 'numpy'],
        ext_modules=cythonize(cec2013single),
#	ext_modules=cythonize('benchmarks.pyx', annotated=True),
        cmdclass={'build_ext': build_ext},
	# Packaging options.
	#include_package_data = True,
	# Tests
	#tests_require=['pytest'],
)
