# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re
from setuptools import setup

#import sys
#if not sys.version_info[0] == 3:
#    print("\n \
#    sys.exit("\n \
#              ****************************************************************\n \
#              * The CLI has only been tested with Python 3+ at this time.    *\n \
#              * Report any issues with Python 2 by emailing help@pipeline.io *\n \
#              ****************************************************************\n")

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pipeline_runtime/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the relevant file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = [line.rstrip() for line in f.readlines()]

#Classifier: Development Status :: 3 - Alpha
#Classifier: Environment :: Console
#Classifier: Intended Audience :: Developers
#Classifier: Intended Audience :: Education
#Classifier: Intended Audience :: Information Technology
#Classifier: Intended Audience :: Science/Research
#Classifier: License :: OSI Approved :: Apache Software License
#Classifier: Natural Language :: English
#Classifier: Operating System :: POSIX :: Linux
#Classifier: Operating System :: MacOS :: MacOS X
#Classifier: Programming Language :: Python :: 2.7
#Classifier: Programming Language :: Python :: 3
#Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
#Classifier: Topic :: Scientific/Engineering :: Image Recognition
#Classifier: Topic :: Scientific/Engineering :: Information Analysis
#Classifier: Topic :: Scientific/Engineering :: Mathematics
#Classifier: Topic :: Scientific/Engineering :: Visualization
#Classifier: Topic :: Software Development :: Libraries
#Classifier: Topic :: Software Development :: Libraries :: Python Modules
#Classifier: Topic :: Utilities

setup(
    name = "pipeline-runtime",
    packages = ["pipeline_runtime"],
    version = version,
    description = "PipelineAI Runtime",
    long_description = "%s\n\nRequirements:\n%s" % (long_description, requirements),
    author = "Chris Fregly",
    author_email = "github@pipeline.ai",
    url = "https://github.pipeline.ai",
    install_requires=requirements,
    dependency_links=[
    ]
)
