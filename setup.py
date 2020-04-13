from setuptools import setup

setup(name='psi_dataset_creator',
      version='0.1.0',
      packages=['psi_dataset_creator'],
      entry_points={
          'console_scripts':
          ['psi_dataset_creator = psi_dataset_creator.__main__:main']
      })
