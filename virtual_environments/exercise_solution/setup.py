


from distutils.core import setup

setup(name='somePackageName',
      version='1.0',
      description='My package for doing something',
      author='Your Name',
      author_email='username@uio.no',
      py_modules=['sequence_matcher'],
      install_requires=["pyfaidx"]
      )

