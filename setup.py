import os
import sys
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext

# Read Long Description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Helper class to build pybind11 extension
class get_pybind_include(object):
    def __str__(self):
        import pybind11
        return pybind11.get_include()

ext_modules = [
    Extension(
        'uhk.uhk_core',
        ['sdk/bindings.cpp'],
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
            'src'
        ],
        language='c++'
    ),
]

setup(
    name='uhk-kernel',  # Package name on PyPI
    version='1.0.0',
    author='UHK Team',
    author_email='contact@uhk-project.org', # Placeholder
    description='Universal Heterogeneous Kernel (UHK) Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uhk-project/uhk", # Placeholder
    packages=['uhk'],
    package_dir={'uhk': 'sdk/uhk'},
    ext_modules=ext_modules,
    install_requires=[
        'pybind11>=2.5.0',
        'numpy>=1.19.0',
        'brainflow',
        'qiskit',
        'qiskit-aer',
        'flask'
    ],
    setup_requires=['pybind11>=2.5.0'],
    cmdclass={'build_ext': build_ext},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
    zip_safe=False,
)
