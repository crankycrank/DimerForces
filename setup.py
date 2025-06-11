from setuptools import setup, Extension
import numpy as np

ext1 = Extension('_wordcount', sources = ['wordcountmodule.c'], 
    include_dirs = [np.get_include()],
    extra_compile_args=["-O3"])

setup (name = 'wordcount',
    scripts = ['compute_sliding_window_force.py',
        'compute_force_from_regions.py', 'compute_force_for_fasta.py'],
    py_modules = ['wordcount'],
    ext_modules = [ext1])
