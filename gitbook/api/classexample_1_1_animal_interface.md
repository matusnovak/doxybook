---
search:
    keywords: ['example::AnimalInterface', 'get_num_of_limbs', 'get_num_of_eyes', 'has_tail']
---

# interface example::AnimalInterface

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**AnimalInterface**](classexample_1_1_animal_interface.md)




Inherited by the following classes: **[example::Animal](classexample_1_1_animal.md)**

## Public Functions

|Type|Name|
|-----|-----|
|virtual int|[**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#1adf3678fbed03da52a7bcbd3cd6a41d57) () const = 0<br>Returns the number of limbs. |
|virtual int|[**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#1a6111e1b914564c809ce7ef69fa8268a8) () const = 0<br>Returns the number of eyes. |
|virtual bool|[**has\_tail**](classexample_1_1_animal_interface.md#1a738f590b295f1ffb58054f609b931524) () const = 0<br>Returns true if the animal has a tail. |


## Public Functions Documentation

### function <a id="1adf3678fbed03da52a7bcbd3cd6a41d57" href="#1adf3678fbed03da52a7bcbd3cd6a41d57">get\_num\_of\_limbs</a>

```cpp
virtual int example::AnimalInterface::get_num_of_limbs () const = 0
```

Returns the number of limbs. 



**See also:** **[get\_num\_of\_eyes](classexample_1_1_animal_interface.md#1a6111e1b914564c809ce7ef69fa8268a8)** 


### function <a id="1a6111e1b914564c809ce7ef69fa8268a8" href="#1a6111e1b914564c809ce7ef69fa8268a8">get\_num\_of\_eyes</a>

```cpp
virtual int example::AnimalInterface::get_num_of_eyes () const = 0
```

Returns the number of eyes. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal_interface.md#1adf3678fbed03da52a7bcbd3cd6a41d57)** 


### function <a id="1a738f590b295f1ffb58054f609b931524" href="#1a738f590b295f1ffb58054f609b931524">has\_tail</a>

```cpp
virtual bool example::AnimalInterface::has_tail () const = 0
```

Returns true if the animal has a tail. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal_interface.md#1adf3678fbed03da52a7bcbd3cd6a41d57)** 


**Return value:**


* **true** Does have a tail 
* **false** Does not have a tail 





----------------------------------------
The documentation for this class was generated from the following file: `src/animal\_interface.h`
