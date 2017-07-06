from setuptools import setup, find_packages


setup(
    name="fluiddevops",
    version="0.0.0",
    author='Ashwin Vishnu Mohanan',
    author_email='avmo@kth.se',
    packages=find_packages(exclude=['docker', 'examples']),
    install_requires=['mercurial', 'hg-git'],
    entry_points={'console_scripts':
                  ['fluidmirror = fluiddevops.mirror.__init__: main',
                   ]
                  }
)
