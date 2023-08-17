#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints information about a Python list.
 * @p: Pointer to a PyObject representing a list.
 */
void print_python_list(PyObject *p)
{
    if (PyList_Check(p))
    {
        Py_ssize_t size = PyList_Size(p);

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (Py_ssize_t i = 0; i < size; i++)
        {
            PyObject *item = PyList_GetItem(p, i);
            const char *typeName = Py_TYPE(item)->tp_name;
            printf("Element %ld: %s\n", i, typeName);
        }
    }
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to a PyObject representing a bytes object.
 */
void print_python_bytes(PyObject *p)
{
    if (PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [.] size: %ld\n", PyBytes_Size(p));
        printf("  [.] trying string: %s\n", PyBytes_AsString(p));
        printf("  [.] first bytes: ");
        for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; i++)
        {
            printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
            if (i + 1 < PyBytes_Size(p) && i + 1 < 10)
                printf(" ");
        }
        printf("\n");
    }
}
