from distutils.core import setup, Extension

setup(
    name='swig_example',
    version='0.0.1',
    author='Blue Geek',
    description="example for swig python",
    ext_modules=[
        Extension(
            '_swig_example', 
            sources=['swig_example_wrap.c', 'swig_example.c'])],
    py_modules=['swig_example']
)