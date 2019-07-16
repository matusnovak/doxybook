
# Namespace example


[**Class List**](annotated.md) **>** [**example**](namespaceexample.md)














## Namespaces

| Type | Name |
| ---: | :--- |
| namespace | [**inner\_namespace**](namespaceexample_1_1inner__namespace.md) <br> |

## Classes

| Type | Name |
| ---: | :--- |
| class | [**Animal**](classexample_1_1_animal.md) <br>_Base class for all animals from which_ [_**Bird**_](classexample_1_1_bird.md) _derives._ |
| interface | [**AnimalInterface**](classexample_1_1_animal_interface.md) <br> |
| class | [**Bird**](classexample_1_1_bird.md) <br> |
| class | [**CustomException**](classexample_1_1_custom_exception.md) <br> |
| class | [**NumericException**](classexample_1_1_numeric_exception.md) <br> |
| class | [**SpecialBird**](classexample_1_1_special_bird.md) <br> |

## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::function&lt; void \*([**Animal**](classexample_1_1_animal.md) \*)&gt; | [**Callback**](namespaceexample.md#typedef-callback)  <br>[_**Animal**_](classexample_1_1_animal.md) _callback function definition._ |
| enum  | [**CallbackType**](namespaceexample.md#enum-callbacktype)  <br>_Different types of an_ [_**Animal**_](classexample_1_1_animal.md) _callback events._ |




## Public Functions

| Type | Name |
| ---: | :--- |
|  void | [**some\_namespace\_function**](namespaceexample.md#function-some_namespace_function) ([**Animal**](classexample_1_1_animal.md) \* animal) <br>_Some random namespace function that modifies_ [_**Animal**_](classexample_1_1_animal.md) _._ |








## Public Types Documentation


### typedef Callback 


```cpp
typedef std::function<void*(Animal*)> example::Callback;
```



### enum CallbackType 


```cpp
enum example::CallbackType {
    NONE = 0,
    EAT,
    SLEEP,
    ATTACK
};
```


## Public Functions Documentation


### function some\_namespace\_function 


```cpp
void example::some_namespace_function (
    Animal * animal
) 
```




**See also:** [**Animal**](classexample_1_1_animal.md) 


**Parameters:**


* animal The pointer to the animal instance 




        

------------------------------
The documentation for this class was generated from the following file `src/animal.h`