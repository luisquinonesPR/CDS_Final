from setuptools import setup, find_packages
#######
# Only needed if the version is imported from the library
# import os
# import sys

# base_dir = os.path.dirname(__file__)
# src_dir = os.path.join(base_dir, 'src')
# sys.path.insert(0, src_dir)

# import library_example
#######

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

# for the version you can either put here a string with the version number
__version__ = "0.1.0"
# or you can create a variable called __version__ inside the __init__.py from
# the src/your_library folder that has a string with the version as a string.

setup(
    name= 'library',
    version='0.1.0',
    description='Flights Data Prediction package',
    author='Luis Quiñones, Giovanna Chaves, Daniela de los Santos, Margherita Philipp',
    url='https://github.com/luisquinonesPR/CDS_HW5',
    packages=find_packages(where='src', exclude=['test']),
    package_dir={'': 'src'},
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    package_data={'Flights_Data': ['Flights_Data.csv']
                  }
)
