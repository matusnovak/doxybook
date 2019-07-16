
# Interface example::AnimalInterface


[**Class List**](api/annotated.md) **>** [**example**](api/namespaceexample.md) **>** [**AnimalInterface**](api/classexample_1_1AnimalInterface.md)





* `#include <animal_interface.h>`





Inherited by the following classes: [example::Animal](api/classexample_1_1Animal.md)










## Public Functions

| Type | Name |
| ---: | :--- |
| virtual int | [**get\_num\_of\_eyes**](api/classexample_1_1AnimalInterface.md#function-get_num_of_eyes) () const = 0<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](api/classexample_1_1AnimalInterface.md#function-get_num_of_limbs) () const = 0<br>_Returns the number of limbs._  |
| virtual bool | [**has\_tail**](api/classexample_1_1AnimalInterface.md#function-has_tail) () const = 0<br>_Returns true if the animal has a tail._  |








## Public Functions Documentation


### function get\_num\_of\_eyes 


```cpp
virtual int example::AnimalInterface::get_num_of_eyes () const = 0
```




**See also:** [**get\_num\_of\_limbs**](api/classexample_1_1AnimalInterface.md#function-get_num_of_limbs) 


        

### function get\_num\_of\_limbs 


```cpp
virtual int example::AnimalInterface::get_num_of_limbs () const = 0
```




**See also:** [**get\_num\_of\_eyes**](api/classexample_1_1AnimalInterface.md#function-get_num_of_eyes) 


        

### function has\_tail 


```cpp
virtual bool example::AnimalInterface::has_tail () const = 0
```




**See also:** [**get\_num\_of\_limbs**](api/classexample_1_1AnimalInterface.md#function-get_num_of_limbs) 


**Return value:**


* true Does have a tail 
* false Does not have a tail 



        

------------------------------
The documentation for this class was generated from the following file `src/animal_interface.h`