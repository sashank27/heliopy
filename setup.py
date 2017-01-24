from setuptools import setup

setup(name='heliopy',
      version='0.1',
      description='Python for Space Physics',
      url='https://github.com/dstansby/heliopy',
      author='David Stansby',
      author_email='dstansby@gmail.com',
      license='GPL-3.0',
      include_package_data=True,
      install_requires=['numpy',
                        'scipy',
                        'matplotlib',
                        'pandas',
                        'spacepy'],
      packages=['heliopy',
                'heliopy.bodies',
                'heliopy.data',
                'heliopy.plot',
                'heliopy.vector',
                'heliopy.util'],
      data_files=[('heliopy', ['README.md', 'heliopy/heliopyrc'])])
