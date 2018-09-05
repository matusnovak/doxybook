---
title: interface example::AnimalInterface
meta:
  - name: keywords
    content: example::AnimalInterface get_num_of_limbs get_num_of_eyes has_tail
---

# interface example::AnimalInterface

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**AnimalInterface**](classexample_1_1_animal_interface.md)




Inherited by the following classes: **[example::Animal](classexample_1_1_animal.md)**

## Public Functions

|Type|Name|
|-----|-----|
|virtual int|[**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#function-get-num-of-limbs) () const = 0<br>Returns the number of limbs. |
|virtual int|[**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#function-get-num-of-eyes) () const = 0<br>Returns the number of eyes. |
|virtual bool|[**has\_tail**](classexample_1_1_animal_interface.md#function-has-tail) () const = 0<br>Returns true if the animal has a tail. |


## Public Functions Documentation

### function get\_num\_of\_limbs

```cpp
virtual int example::AnimalInterface::get_num_of_limbs () const = 0
```

Returns the number of limbs. 



**See also:** **[get\_num\_of\_eyes](classexample_1_1_animal_interface.md#function-get-num-of-eyes)** 


### function get\_num\_of\_eyes

```cpp
virtual int example::AnimalInterface::get_num_of_eyes () const = 0
```

Returns the number of eyes. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal_interface.md#function-get-num-of-limbs)** 


### function has\_tail

```cpp
virtual bool example::AnimalInterface::has_tail () const = 0
```

Returns true if the animal has a tail. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal_interface.md#function-get-num-of-limbs)** 


**Return value:**


* **true** Does have a tail 
* **false** Does not have a tail 





----------------------------------------
The documentation for this class was generated from the following file: `src/animal\_interface.h`
