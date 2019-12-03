#include "swig_example.h"

int add_vector(int * p_a, int * p_b, int * p_c, int len){
    if (len <= 0) {
        return 0;
    }
    for (int i=0; i<len; ++i) {
        p_c[i] = p_a[i] + p_b[i];
    }
    return len;
}
