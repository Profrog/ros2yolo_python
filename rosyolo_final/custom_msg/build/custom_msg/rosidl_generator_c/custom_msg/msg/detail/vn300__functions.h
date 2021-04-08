// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from custom_msg:msg/Vn300.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__VN300__FUNCTIONS_H_
#define CUSTOM_MSG__MSG__DETAIL__VN300__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "custom_msg/msg/rosidl_generator_c__visibility_control.h"

#include "custom_msg/msg/detail/vn300__struct.h"

/// Initialize msg/Vn300 message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * custom_msg__msg__Vn300
 * )) before or use
 * custom_msg__msg__Vn300__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
bool
custom_msg__msg__Vn300__init(custom_msg__msg__Vn300 * msg);

/// Finalize msg/Vn300 message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
void
custom_msg__msg__Vn300__fini(custom_msg__msg__Vn300 * msg);

/// Create msg/Vn300 message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * custom_msg__msg__Vn300__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
custom_msg__msg__Vn300 *
custom_msg__msg__Vn300__create();

/// Destroy msg/Vn300 message.
/**
 * It calls
 * custom_msg__msg__Vn300__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
void
custom_msg__msg__Vn300__destroy(custom_msg__msg__Vn300 * msg);


/// Initialize array of msg/Vn300 messages.
/**
 * It allocates the memory for the number of elements and calls
 * custom_msg__msg__Vn300__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
bool
custom_msg__msg__Vn300__Sequence__init(custom_msg__msg__Vn300__Sequence * array, size_t size);

/// Finalize array of msg/Vn300 messages.
/**
 * It calls
 * custom_msg__msg__Vn300__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
void
custom_msg__msg__Vn300__Sequence__fini(custom_msg__msg__Vn300__Sequence * array);

/// Create array of msg/Vn300 messages.
/**
 * It allocates the memory for the array and calls
 * custom_msg__msg__Vn300__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
custom_msg__msg__Vn300__Sequence *
custom_msg__msg__Vn300__Sequence__create(size_t size);

/// Destroy array of msg/Vn300 messages.
/**
 * It calls
 * custom_msg__msg__Vn300__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_custom_msg
void
custom_msg__msg__Vn300__Sequence__destroy(custom_msg__msg__Vn300__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MSG__MSG__DETAIL__VN300__FUNCTIONS_H_
