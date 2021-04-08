// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msg:msg/Vn300.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__VN300__BUILDER_HPP_
#define CUSTOM_MSG__MSG__DETAIL__VN300__BUILDER_HPP_

#include "custom_msg/msg/detail/vn300__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msg
{

namespace msg
{

namespace builder
{

class Init_Vn300_data
{
public:
  Init_Vn300_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_msg::msg::Vn300 data(::custom_msg::msg::Vn300::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::msg::Vn300 msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::msg::Vn300>()
{
  return custom_msg::msg::builder::Init_Vn300_data();
}

}  // namespace custom_msg

#endif  // CUSTOM_MSG__MSG__DETAIL__VN300__BUILDER_HPP_
