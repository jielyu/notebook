#include "Python.h"

int add_vector(int * p_a, int * p_b, int * p_c, int len){
    if (len <= 0) {
        return 0;
    }
    for (int i=0; i<len; ++i) {
        p_c[i] = p_a[i] + p_b[i];
    }
    return len;
}

// 包装python调用接口
static PyObject * cext_add_vector(PyObject *self, PyObject *args){
    PyObject * py_list_a = NULL;
    PyObject * py_list_b = NULL;
    PyObject * py_list_c = NULL;
    if (!PyArg_ParseTuple(args, "OOO", &py_list_a, &py_list_b, &py_list_c)) {
        return NULL;
    }
    // 申请存储空间
    int len = PyList_Size(py_list_a);
    int * pa = (int *)malloc(sizeof(int)*len);
    int * pb = (int *)malloc(sizeof(int)*len);
    int * pc = (int *)malloc(sizeof(int)*len);
    // 拷贝输入参数
    int count = len;
    while(count--){
        if(!PyArg_Parse(PyList_GetItem(py_list_a, count), "i", pa+count)){return NULL;}
        if(!PyArg_Parse(PyList_GetItem(py_list_b, count), "i", pb+count)){return NULL;}
    }
    // 执行计算任务
    int ret = add_vector(pa, pb, pc, len);
    // 拷贝输出结果
    count = len;
    while(count--){
        PyList_SetItem(py_list_c, count, Py_BuildValue("i", pc[count]));
    }
    // 释放内存
    free(pa);free(pb);free(pc);
    // 返回
    return (PyObject *)Py_BuildValue("i", ret);
}

// 罗列提供接口的方法列表
static PyMethodDef cextMethods[] = {
    {"add_vector", cext_add_vector, METH_VARARGS},
    {NULL, NULL},
};

static struct  PyModuleDef cModDef = {
    PyModuleDef_HEAD_INIT,
    "cext_example",               // 模块名
    "just test for c extension",  // 文档
    -1,                           
    cextMethods                   // 模块提供的方法
};


PyMODINIT_FUNC PyInit_cext_example(void)
{
    return PyModule_Create(&cModDef);
}