from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.0',
      description='',
      url='https://github.com/Andriiok/clean_folder',
      author='Andriiok',
      author_email='',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']})