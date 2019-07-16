
# Interface example::AnimalInterface


[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **>** [**AnimalInterface**](classexample_1_1_animal_interface.md)





* `#include <animal_interface.h>`





Inherited by the following classes: [example::Animal](classexample_1_1_animal.md)










## Public Functions

| Type | Name |
| ---: | :--- |
| virtual int | [**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#function-get_num_of_eyes) () const = 0<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#function-get_num_of_limbs) () const = 0<br>_Returns the number of limbs._  |
| virtual bool | [**has\_tail**](classexample_1_1_animal_interface.md#function-has_tail) () const = 0<br>_Returns true if the animal has a tail._  |








## Public Functions Documentation


### function get\_num\_of\_eyes 


```cpp
virtual int example::AnimalInterface::get_num_of_eyes () const = 0
```




**See also:** [**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#function-get_num_of_limbs) 



        

### function get\_num\_of\_limbs 


```cpp
virtual int example::AnimalInterface::get_num_of_limbs () const = 0
```




**See also:** [**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#function-get_num_of_eyes) 



        

### function has\_tail 


```cpp
virtual bool example::AnimalInterface::has_tail () const = 0
```




**See also:** [**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#function-get_num_of_limbs) 


**Return value:**


* true Does have a tail 
* false Does not have a tail 




        

------------------------------
The documentation for this class was generated from the following file `src/animal_interface.h`