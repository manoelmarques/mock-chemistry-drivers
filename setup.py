# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import atexit

long_description="""Mock Chemistry Drivers"""
    
requirements = [
    "qiskit-aqua-chemistry>=0.2.0"
]

def _post_install():
    from qiskit_aqua_chemistry.preferences import Preferences
    preferences = Preferences()
    preferences.add_package(Preferences.PACKAGE_TYPE_DRIVERS,'mock_chemistry_drivers')
    preferences.save()
    
class CustomInstallCommand(install):
    def run(self):
        atexit.register(_post_install)
        install.run(self)
        
class CustomDevelopCommand(develop):
    def run(self):
        atexit.register(_post_install)
        develop.run(self)
        
class CustomEggInfoCommand(egg_info):
    def run(self):
        atexit.register(_post_install)
        egg_info.run(self)
    

setuptools.setup(
    name='mock-chemistry-drivers',
    version="0.1.0",  # this should match __init__.__version__
    description='Mock Chemistry Drivers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/QISKit/qiskit-aqua-chemistry',
    author='QISKit AQUA Chemistry Development Team',
    author_email='qiskit@us.ibm.com',
    license='Apache-2.0',
    classifiers=(
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering"
    ),
    keywords='qiskit sdk quantum aqua chemistry',
    packages=setuptools.find_packages(exclude=['test*']),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand
    }
)