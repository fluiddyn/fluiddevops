from setuptools import setup, find_packages
from runpy import run_path

d = run_path('fluiddevops/_version.py')
__version__ = d['__version__']

# Get the development status from the version string
if 'a' in __version__:
    devstatus = 'Development Status :: 3 - Alpha'
elif 'b' in __version__:
    devstatus = 'Development Status :: 4 - Beta'
else:
    devstatus = 'Development Status :: 5 - Production/Stable'

setup(
    name="fluiddevops",
    version=__version__,
    packages=find_packages(exclude=['docker', 'examples']),
    install_requires=['mercurial', 'hg-git', 'configparser'],
    entry_points={
        'console_scripts':
        ['fluidmirror = fluiddevops.mirror:main',
         ]},
    author='Ashwin Vishnu Mohanan',
    author_email='avmo@kth.se',
    description="Console scripts to make DevOps easier.",
    license="CeCILL",
    keywords='DevOps, continuous integration, testing',
    url="http://bitbucket.org/gfdyn/fluiddevops",
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        devstatus,
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        # actually CeCILL License (GPL compatible license for French laws)
        #
        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2,
        # Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'],
)
