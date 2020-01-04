from distutils.core import setup, Extension
MOD = 'cext_example'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['cext_example.c'])])
