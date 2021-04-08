// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_msg:msg/Vn300.idl
// generated code does not contain a copyright notice
#include "custom_msg/msg/detail/vn300__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/string_functions.h"

bool
custom_msg__msg__Vn300__init(custom_msg__msg__Vn300 * msg)
{
  if (!msg) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__init(&msg->data)) {
    custom_msg__msg__Vn300__fini(msg);
    return false;
  }
  return true;
}

void
custom_msg__msg__Vn300__fini(custom_msg__msg__Vn300 * msg)
{
  if (!msg) {
    return;
  }
  // data
  rosidl_runtime_c__String__fini(&msg->data);
}

custom_msg__msg__Vn300 *
custom_msg__msg__Vn300__create()
{
  custom_msg__msg__Vn300 * msg = (custom_msg__msg__Vn300 *)malloc(sizeof(custom_msg__msg__Vn300));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_msg__msg__Vn300));
  bool success = custom_msg__msg__Vn300__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
custom_msg__msg__Vn300__destroy(custom_msg__msg__Vn300 * msg)
{
  if (msg) {
    custom_msg__msg__Vn300__fini(msg);
  }
  free(msg);
}


bool
custom_msg__msg__Vn300__Sequence__init(custom_msg__msg__Vn300__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  custom_msg__msg__Vn300 * data = NULL;
  if (size) {
    data = (custom_msg__msg__Vn300 *)calloc(size, sizeof(custom_msg__msg__Vn300));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_msg__msg__Vn300__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_msg__msg__Vn300__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_msg__msg__Vn300__Sequence__fini(custom_msg__msg__Vn300__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_msg__msg__Vn300__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_msg__msg__Vn300__Sequence *
custom_msg__msg__Vn300__Sequence__create(size_t size)
{
  custom_msg__msg__Vn300__Sequence * array = (custom_msg__msg__Vn300__Sequence *)malloc(sizeof(custom_msg__msg__Vn300__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = custom_msg__msg__Vn300__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
custom_msg__msg__Vn300__Sequence__destroy(custom_msg__msg__Vn300__Sequence * array)
{
  if (array) {
    custom_msg__msg__Vn300__Sequence__fini(array);
  }
  free(array);
}
