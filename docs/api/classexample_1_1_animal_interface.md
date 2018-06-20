---
search:
    keywords: ['example::AnimalInterface', 'get_num_of_limbs', 'get_num_of_eyes', 'has_tail']
---

# interface example::AnimalInterface



Inherited by the following classes: **[example::Animal](classexample_1_1_animal.md)**

## Public Functions

|Type|Name|
|-----|-----|
|virtual int|[**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#1a0300198be5798cfa0350fbb2fde4295e) () const = 0<br>Returns the number of limbs. |
|virtual int|[**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#1a63c32ae61aa4ee35b3666b08ce3378f9) () const = 0<br>Returns the number of eyes. |
|virtual bool|[**has\_tail**](classexample_1_1_animal_interface.md#1af994135a8e875998808ca7f11f12a6b3) () const = 0<br>Returns true if the animal has a tail. |


## Public Functions Documentation

### function <a id="1a0300198be5798cfa0350fbb2fde4295e" href="#1a0300198be5798cfa0350fbb2fde4295e">get\_num\_of\_limbs</a>

```cpp
virtual int example::AnimalInterface::get_num_of_limbs () const = 0
```

Returns the number of limbs. 



**See also:**

**[get\_num\_of\_eyes](classexample_1_1_animal_interface.md#1a63c32ae61aa4ee35b3666b08ce3378f9)** 




### function <a id="1a63c32ae61aa4ee35b3666b08ce3378f9" href="#1a63c32ae61aa4ee35b3666b08ce3378f9">get\_num\_of\_eyes</a>

```cpp
virtual int example::AnimalInterface::get_num_of_eyes () const = 0
```

Returns the number of eyes. 



**See also:**

**[get\_num\_of\_limbs](classexample_1_1_animal_interface.md#1a0300198be5798cfa0350fbb2fde4295e)** 




### function <a id="1af994135a8e875998808ca7f11f12a6b3" href="#1af994135a8e875998808ca7f11f12a6b3">has\_tail</a>

```cpp
virtual bool example::AnimalInterface::has_tail () const = 0
```

Returns true if the animal has a tail. 



**See also:**

**[get\_num\_of\_limbs](classexample_1_1_animal_interface.md#1a0300198be5798cfa0350fbb2fde4295e)** 




**Return value:**


* _true_ Does have a tail 
* _false_ Does not have a tail 





----------------------------------------
The documentation for this class was generated from the following file: `src/animal\_interface.h`
