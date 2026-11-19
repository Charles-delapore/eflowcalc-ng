# Copyright (C) 2019-2021  Thibault Hallouin
from setuptools import setup


with open("README.rst", "r") as fh:
    long_desc = fh.read()

_version_ns = {}
with open('eflowcalc/version.py') as fv:
    exec(fv.read(), _version_ns)
__version__ = _version_ns['__version__']

setup(
    name='eflowcalc-ng',

    version=__version__,

    description='EFlowCalc: A Calculator of Streamflow Characteristics in Python',
    long_description=long_desc,
    long_description_content_type="text/x-rst",

    download_url="https://pypi.python.org/pypi/eflowcalc-ng",
    project_urls={
        "Bug Tracker": "https://github.com/Charles-delapore/eflowcalc-ng/issues",
        "Source Code": "https://github.com/Charles-delapore/eflowcalc-ng",
        "Documentation": "https://thibhlln.github.io/eflowcalc",
        "Original Repository": "https://github.com/ThibHlln/eflowcalc",
    },

    author='Thibault Hallouin',
    author_email='thibault.hallouin@ucdconnect.ie',

    license='GPLv3',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Natural Language :: English',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Hydrology',

        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython'
    ],

    python_requires='>=3.9',

    packages=['eflowcalc'],

    install_requires=[
        'numpy',
        'pandas'
    ],

    extras_require={
        'tests': ['netCDF4']
    }
)
