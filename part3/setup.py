


from distutils.core import setup

setup(name='DnaAnalyser',
      version='1.0',
      description='A package for various DNA-analyses',
      author='Your Name',
      author_email='username@uio.no',
      py_modules=['gc_content'],
      install_requires=["pyfaidx"],
      entry_points = {
            'console_scripts': ['gc_content=gc_content:main'],
        }
)