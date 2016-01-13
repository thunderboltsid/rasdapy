
from setuptools import setup

setup(name='raspy',
      version='0.1',
      description='Python interface to rasdaman',
      author='Siddharth Shukla',
      author_email='s.shukla@jacobs-university.de',
      license='MIT',
      packages=['raspy'],
      install_requires=['grpcio', 'protobuf', 'numpy', 'scipy'],
      zip_safe=False)