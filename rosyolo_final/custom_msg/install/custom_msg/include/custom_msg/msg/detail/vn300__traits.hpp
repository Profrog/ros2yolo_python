// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_msg:msg/Vn300.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__VN300__TRAITS_HPP_
#define CUSTOM_MSG__MSG__DETAIL__VN300__TRAITS_HPP_

#include "custom_msg/msg/detail/vn300__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_msg::msg::Vn300>()
{
  return "custom_msg::msg::Vn300";
}

template<>
inline const char * name<custom_msg::msg::Vn300>()
{
  return "custom_msg/msg/Vn300";
}

template<>
struct has_fixed_size<custom_msg::msg::Vn300>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_msg::msg::Vn300>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_msg::msg::Vn300>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MSG__MSG__DETAIL__VN300__TRAITS_HPP_
