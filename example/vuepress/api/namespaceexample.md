---
title: namespace example
meta:
  - name: keywords
    content: example Animal AnimalInterface Bird CustomException SpecialBird CallbackType Callback some_namespace_function
---

# namespace example

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md)


## Classes

|Type|Name|
|-----|-----|
|class|[**Animal**](classexample_1_1_animal.md)<br>Base class for all animals from which **[Bird](classexample_1_1_bird.md)** derives. |
|class|[**AnimalInterface**](classexample_1_1_animal_interface.md)|
|class|[**Bird**](classexample_1_1_bird.md)|
|class|[**CustomException**](classexample_1_1_custom_exception.md)|
|class|[**SpecialBird**](classexample_1_1_special_bird.md)|


## Enums

|Type|Name|
|-----|-----|
|enum|[**CallbackType**](animal_8h.md#enum-callbacktype) { **NONE** = 0, **EAT**, **SLEEP**, **ATTACK** } <br>Different types of an **[Animal](classexample_1_1_animal.md)** callback events. |


## Typedefs

|Type|Name|
|-----|-----|
|typedef std::function< void \*(**[Animal](classexample_1_1_animal.md)** \*)>|[**Callback**](animal_8h.md#typedef-callback)<br>**[Animal](classexample_1_1_animal.md)** callback function definition. |


## Functions

|Type|Name|
|-----|-----|
|void|[**some\_namespace\_function**](animal_8h.md#function-some-namespace-function) (**[Animal](classexample_1_1_animal.md)** \* animal) <br>Some random namespace function that modifies **[Animal](classexample_1_1_animal.md)**. |


## Enums Documentation

### enum CallbackType

```cpp
enum example::CallbackType {
    NONE = 0,
    EAT,
    SLEEP,
    ATTACK,
};
```

Different types of an **[Animal](classexample_1_1_animal.md)** callback events. 


## Typedefs Documentation

### typedef Callback

```cpp
typedef std::function<void*(Animal*)> example::Callback;
```

**[Animal](classexample_1_1_animal.md)** callback function definition. 


## Functions Documentation

### function some\_namespace\_function

```cpp
void example::some_namespace_function (
    Animal * animal
)
```

Some random namespace function that modifies **[Animal](classexample_1_1_animal.md)**. 



**See also:** **[Animal](classexample_1_1_animal.md)** 


**Parameters:**


* **animal** The pointer to the animal instance 





----------------------------------------
The documentation for this class was generated from the following file: `src/animal.h`
