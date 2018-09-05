---
title: class example::Bird
meta:
  - name: keywords
    content: example::Bird Bird Bird Bird ~Bird swap move make_sound operator= operator=
---

# class example::Bird

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**Bird**](classexample_1_1_bird.md)




Inherits the following classes: **[example::Animal](classexample_1_1_animal.md)**



Inherited by the following classes: **[example::SpecialBird](classexample_1_1_special_bird.md)**

## Public Functions

|Type|Name|
|-----|-----|
||[**Bird**](classexample_1_1_bird.md#function-bird-1-3) (const std::string & name, **[Bird](classexample_1_1_bird.md)** \* mother = nullptr, **[Bird](classexample_1_1_bird.md)** \* father = nullptr) |
||[**Bird**](classexample_1_1_bird.md#function-bird-2-3) (const **[Bird](classexample_1_1_bird.md)** & other) = delete |
||[**Bird**](classexample_1_1_bird.md#function-bird-3-3) (**[Bird](classexample_1_1_bird.md)** && Bird) noexcept |
||[**~Bird**](classexample_1_1_bird.md#function-bird) () = default |
|void|[**swap**](classexample_1_1_bird.md#function-swap) (**[Bird](classexample_1_1_bird.md)** & other) noexcept |
|virtual void|[**move**](classexample_1_1_bird.md#function-move) () override |
|virtual void|[**make\_sound**](classexample_1_1_bird.md#function-make-sound) () override |
|**[Bird](classexample_1_1_bird.md)** &|[**operator=**](classexample_1_1_bird.md#function-operator-1-2) (const **[Bird](classexample_1_1_bird.md)** & other) = delete <br>Deleted copy operator. |
|**[Bird](classexample_1_1_bird.md)** &|[**operator=**](classexample_1_1_bird.md#function-operator-2-2) (**[Bird](classexample_1_1_bird.md)** && other) noexcept <br>Move operator. |


## Public Functions Documentation

### function Bird (1/3)

```cpp
example::Bird::Bird (
    const std::string & name,
    Bird * mother = nullptr,
    Bird * father = nullptr
)
```



### function Bird (2/3)

```cpp
example::Bird::Bird (
    const Bird & other
) = delete
```



### function Bird (3/3)

```cpp
example::Bird::Bird (
    Bird && Bird
) noexcept
```



### function ~Bird

```cpp
example::Bird::~Bird () = default
```



### function swap

```cpp
void example::Bird::swap (
    Bird & other
) noexcept
```



### function move

```cpp
virtual void example::Bird::move ()
```



Implements **[Animal::move](classexample_1_1_animal.md#function-move)**


### function make\_sound

```cpp
virtual void example::Bird::make_sound ()
```



Implements **[Animal::make\_sound](classexample_1_1_animal.md#function-make-sound)**


### function operator= (1/2)

```cpp
Bird & example::Bird::operator= (
    const Bird & other
) = delete
```

Deleted copy operator. 


### function operator= (2/2)

```cpp
Bird & example::Bird::operator= (
    Bird && other
) noexcept
```

Move operator. 




----------------------------------------
The documentation for this class was generated from the following file: `src/bird.h`
