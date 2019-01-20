---
search:
    keywords: ['example', 'Animal', 'AnimalInterface', 'Bird', 'CustomException', 'SpecialBird', 'CallbackType', 'Callback', 'some_namespace_function']
---

# namespace example

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md)


## Classes

|Type|Name|
|-----|-----|
|class|[**Animal**](classexample_1_1_animal.md)|
|class|[**AnimalInterface**](classexample_1_1_animal_interface.md)|
|class|[**Bird**](classexample_1_1_bird.md)|
|class|[**CustomException**](classexample_1_1_custom_exception.md)|
|class|[**SpecialBird**](classexample_1_1_special_bird.md)|


## Enums

|Type|Name|
|-----|-----|
|enum|[**CallbackType**](animal_8h.md#1a002d84037f2ef097ebb0504482fa893d) { **NONE** = 0, **EAT**, **SLEEP**, **ATTACK** } <br>Different types of an **[Animal](classexample_1_1_animal.md)** callback events. |


## Typedefs

|Type|Name|
|-----|-----|
|typedef std::function< void \*(**[Animal](classexample_1_1_animal.md)** \*)>|[**Callback**](animal_8h.md#1a02deaa75527d48da18f0959c46901bb7)<br>**[Animal](classexample_1_1_animal.md)** callback function definition. |


## Functions

|Type|Name|
|-----|-----|
|void|[**some\_namespace\_function**](animal_8h.md#1a766277c52d41af925d49bcd4f9bc7de0) (**[Animal](classexample_1_1_animal.md)** \* animal) <br>Some random namespace function that modifies **[Animal](classexample_1_1_animal.md)**. |


## Enums Documentation

### enum <a id="1a002d84037f2ef097ebb0504482fa893d" href="#1a002d84037f2ef097ebb0504482fa893d">CallbackType</a>

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

### typedef <a id="1a02deaa75527d48da18f0959c46901bb7" href="#1a02deaa75527d48da18f0959c46901bb7">Callback</a>

```cpp
typedef std::function<void*(Animal*)> example::Callback;
```

**[Animal](classexample_1_1_animal.md)** callback function definition. 


## Functions Documentation

### function <a id="1a766277c52d41af925d49bcd4f9bc7de0" href="#1a766277c52d41af925d49bcd4f9bc7de0">some\_namespace\_function</a>

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
