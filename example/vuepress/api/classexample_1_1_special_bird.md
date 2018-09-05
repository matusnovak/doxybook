---
title: class example::SpecialBird
meta:
  - name: keywords
    content: example::SpecialBird SpecialBird SpecialBird SpecialBird ~SpecialBird swap do_something_special operator= operator=
---

# class example::SpecialBird

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**SpecialBird**](classexample_1_1_special_bird.md)




Inherits the following classes: **[example::Bird](classexample_1_1_bird.md)**

## Public Functions

|Type|Name|
|-----|-----|
||[**SpecialBird**](classexample_1_1_special_bird.md#function-specialbird-1-3) (const std::string & name, **[SpecialBird](classexample_1_1_special_bird.md)** \* mother = nullptr, **[SpecialBird](classexample_1_1_special_bird.md)** \* father = nullptr) |
||[**SpecialBird**](classexample_1_1_special_bird.md#function-specialbird-2-3) (const **[SpecialBird](classexample_1_1_special_bird.md)** & other) = delete |
||[**SpecialBird**](classexample_1_1_special_bird.md#function-specialbird-3-3) (**[SpecialBird](classexample_1_1_special_bird.md)** && SpecialBird) noexcept |
||[**~SpecialBird**](classexample_1_1_special_bird.md#function-specialbird) () = default |
|void|[**swap**](classexample_1_1_special_bird.md#function-swap) (**[SpecialBird](classexample_1_1_special_bird.md)** & other) noexcept |
|void|[**do\_something\_special**](classexample_1_1_special_bird.md#function-do-something-special) () |
|**[SpecialBird](classexample_1_1_special_bird.md)** &|[**operator=**](classexample_1_1_special_bird.md#function-operator-1-2) (const **[SpecialBird](classexample_1_1_special_bird.md)** & other) = delete |
|**[SpecialBird](classexample_1_1_special_bird.md)** &|[**operator=**](classexample_1_1_special_bird.md#function-operator-2-2) (**[SpecialBird](classexample_1_1_special_bird.md)** && other) noexcept |


## Public Functions Documentation

### function SpecialBird (1/3)

```cpp
example::SpecialBird::SpecialBird (
    const std::string & name,
    SpecialBird * mother = nullptr,
    SpecialBird * father = nullptr
)
```



### function SpecialBird (2/3)

```cpp
example::SpecialBird::SpecialBird (
    const SpecialBird & other
) = delete
```



### function SpecialBird (3/3)

```cpp
example::SpecialBird::SpecialBird (
    SpecialBird && SpecialBird
) noexcept
```



### function ~SpecialBird

```cpp
example::SpecialBird::~SpecialBird () = default
```



### function swap

```cpp
void example::SpecialBird::swap (
    SpecialBird & other
) noexcept
```



### function do\_something\_special

```cpp
void example::SpecialBird::do_something_special ()
```



### function operator= (1/2)

```cpp
SpecialBird & example::SpecialBird::operator= (
    const SpecialBird & other
) = delete
```



### function operator= (2/2)

```cpp
SpecialBird & example::SpecialBird::operator= (
    SpecialBird && other
) noexcept
```





----------------------------------------
The documentation for this class was generated from the following file: `src/special\_bird.h`
