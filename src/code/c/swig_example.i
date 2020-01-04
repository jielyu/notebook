%module swig_example


%{
#include "swig_example.h"
%}

%include "carrays.i"
%array_class(int, intp);

int add_vector(int * p_a, int * p_b, int * p_c, int len);