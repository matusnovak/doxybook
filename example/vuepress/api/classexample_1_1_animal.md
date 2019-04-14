
# Class example::Animal


[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **>** [**Animal**](classexample_1_1_animal.md)



_Base class for all animals from which_ [_**Bird**_](classexample_1_1_bird.md) _derives._[More...](#detailed-description)

* `#include <animal.h>`



Inherits the following classes: [example::AnimalInterface](classexample_1_1_animal_interface.md)


Inherited by the following classes: [example::Bird](classexample_1_1_bird.md)





## Classes

| Type | Name |
| ---: | :--- |
| struct | [**Result**](structexample_1_1_animal_1_1_result.md) <br>_Some random inner class of_ [_**Animal**_](classexample_1_1_animal.md) _._ |

## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::pair&lt; [**Animal**](classexample_1_1_animal.md) \*, [**Animal**](classexample_1_1_animal.md) \* &gt; | [**Parents**](classexample_1_1_animal.md#typedef-parents)  <br> |
| enum  | [**Type**](classexample_1_1_animal.md#enum-type)  <br>_The 6 classes of animal kingdom._  |








## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Animal**](classexample_1_1_animal.md#function-animal-1-3) ([**Type**](classexample_1_1_animal.md#enum-type) type, const std::string & name, [**Animal**](classexample_1_1_animal.md) \* mother=nullptr, [**Animal**](classexample_1_1_animal.md) \* father=nullptr) <br>_The main constructor._  |
|   | [**Animal**](classexample_1_1_animal.md#function-animal-2-3) (const [**Animal**](classexample_1_1_animal.md) & other) = delete<br> |
|   | [**Animal**](classexample_1_1_animal.md#function-animal-3-3) ([**Animal**](classexample_1_1_animal.md) && animal) noexcept<br> |
|  const std::string & | [**get\_name**](classexample_1_1_animal.md#function-get-name) () const<br>_Get the name of the animal._  |
| virtual int | [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes) () override const<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs) () override const<br>_Returns the number of limbs._  |
|  [**Parents**](classexample_1_1_animal.md#typedef-parents) | [**get\_parents**](classexample_1_1_animal.md#function-get-parents) () const<br> |
| virtual bool | [**has\_tail**](classexample_1_1_animal.md#function-has-tail) () override const<br>_Returns true if the animal has a tail._  |
| virtual void | [**make\_sound**](classexample_1_1_animal.md#function-make-sound) () = 0<br> |
| virtual void | [**move**](classexample_1_1_animal.md#function-move) () <br> |
|   | [**operator bool**](classexample_1_1_animal.md#function-operator-bool) () const<br>_Returns true if this is an valid animal._  |
|  [**Animal**](classexample_1_1_animal.md) & | [**operator=**](classexample_1_1_animal.md#function-operator) (const [**Animal**](classexample_1_1_animal.md) & other) = delete<br>_Deleted copy operator._  |
|  [**Animal**](classexample_1_1_animal.md) & | [**operator=**](classexample_1_1_animal.md#function-operator-2) ([**Animal**](classexample_1_1_animal.md) && other) noexcept<br>_Move operator._  |
|  void | [**some\_inline\_member\_function**](classexample_1_1_animal.md#function-some-inline-member-function) ([**Animal**](classexample_1_1_animal.md) \* animal) <br>_Lorem Ipsum._  |
|  void | [**swap**](classexample_1_1_animal.md#function-swap) ([**Animal**](classexample_1_1_animal.md) & other) noexcept<br> |
| virtual  | [**~Animal**](classexample_1_1_animal.md#function-animal) () = default<br> |

## Public Functions inherited from [example::AnimalInterface](classexample_1_1_animal_interface.md)

| Type | Name |
| ---: | :--- |
| virtual int | [**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#function-get-num-of-eyes) () const = 0<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#function-get-num-of-limbs) () const = 0<br>_Returns the number of limbs._  |
| virtual bool | [**has\_tail**](classexample_1_1_animal_interface.md#function-has-tail) () const = 0<br>_Returns true if the animal has a tail._  |

## Public Static Functions

| Type | Name |
| ---: | :--- |
|  [**Animal**](classexample_1_1_animal.md) \* | [**find\_child\_by\_name**](classexample_1_1_animal.md#function-find-child-by-name) ([**Animal**](classexample_1_1_animal.md) \* parent) <br> |
|  [**Animal**](classexample_1_1_animal.md) \* | [**find\_parent\_by\_name**](classexample_1_1_animal.md#function-find-parent-by-name) ([**Animal**](classexample_1_1_animal.md) \* child) <br> |






## Protected Attributes

| Type | Name |
| ---: | :--- |
|  [**Animal**](classexample_1_1_animal.md) \* | [**father**](classexample_1_1_animal.md#variable-father)  <br>_The pointer to the father._  |
|  [**Animal**](classexample_1_1_animal.md) \* | [**mother**](classexample_1_1_animal.md#variable-mother)  <br>_The pointer to the mother._  |
|  std::string | [**name**](classexample_1_1_animal.md#variable-name)  <br> |








## Public Types Documentation


### typedef Parents 


```cpp
typedef std::pair<Animal*, Animal*> example::Animal::Parents;
```



### enum Type 


```cpp
enum example::Animal::Type {
    NONE = 0,
    INSECT = 1,
    AMPHIBIAN = 2,
    BIRD = 3,
    FISH = 4,
    REPTILE = 5,
    MAMMAL = 6
};
```


Lorem Ipsum Donor. 


        
## Public Functions Documentation


### function Animal [1/3]


```cpp
example::Animal::Animal (
    Type type,
    const std::string & name,
    Animal * mother=nullptr,
    Animal * father=nullptr
) 
```


Use this constructor to allocate a new instance of [**Animal**](classexample_1_1_animal.md) 

**Parameters:**


* **type** The type of the animal that matches [**Animal::Type**](classexample_1_1_animal.md#enum-type) 
* **name** Any name to associate the animal with 



**Exception:**


* **[**CustomException**](classexample_1_1_custom_exception.md)** If either only mother or father is assigned 




        

### function Animal [2/3]


```cpp
example::Animal::Animal (
    const Animal & other
) = delete
```



### function Animal [3/3]


```cpp
example::Animal::Animal (
    Animal && animal
) noexcept
```



### function get\_name 


```cpp
inline const std::string & example::Animal::get_name () const
```




**Returns:**

A constant reference to the name 





        

### function get\_num\_of\_eyes 


```cpp
virtual int example::Animal::get_num_of_eyes () override const
```




**See also:** [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs), [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes) 



        
Implements [*example::AnimalInterface::get\_num\_of\_eyes*](classexample_1_1_animal_interface.md#function-get-num-of-eyes)


### function get\_num\_of\_limbs 


```cpp
virtual int example::Animal::get_num_of_limbs () override const
```




**See also:** [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes), [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs) 



        
Implements [*example::AnimalInterface::get\_num\_of\_limbs*](classexample_1_1_animal_interface.md#function-get-num-of-limbs)


### function get\_parents 


```cpp
inline Parents example::Animal::get_parents () const
```



### function has\_tail 


```cpp
virtual bool example::Animal::has_tail () override const
```




**See also:** [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs), [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes) 


**Return value:**


* **true** Does have a tail 
* **false** Does not have a tail 




        
Implements [*example::AnimalInterface::has\_tail*](classexample_1_1_animal_interface.md#function-has-tail)


### function make\_sound 


```cpp
virtual void example::Animal::make_sound () = 0
```



### function move 


```cpp
virtual void example::Animal::move () 
```



### function operator bool 


```cpp
example::Animal::operator bool () const
```


Lorem Ipsum returns true 


        

### function operator= 


```cpp
Animal & example::Animal::operator= (
    const Animal & other
) = delete
```



### function operator= 


```cpp
Animal & example::Animal::operator= (
    Animal && other
) noexcept
```



### function some\_inline\_member\_function 


```cpp
inline void example::Animal::some_inline_member_function (
    Animal * animal
) 
```




**See also:** [**Animal**](classexample_1_1_animal.md) 


**Parameters:**


* **animal** The pointer to the animal instance

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.


### Implementation:





        

### function swap 


```cpp
void example::Animal::swap (
    Animal & other
) noexcept
```



### function ~Animal 


```cpp
virtual example::Animal::~Animal () = default
```


## Public Static Functions Documentation


### function find\_child\_by\_name 


```cpp
static Animal * example::Animal::find_child_by_name (
    Animal * parent
) 
```



### function find\_parent\_by\_name 


```cpp
static Animal * example::Animal::find_parent_by_name (
    Animal * child
) 
```


## Protected Attributes Documentation


### variable father 


```cpp
Animal* example::Animal::father;
```


Can be null! 


        

### variable mother 


```cpp
Animal* example::Animal::mother;
```


Can be null! 


        

### variable name 


```cpp
std::string example::Animal::name;
```

## Friends Documentation



### friend some\_global\_function 


```cpp
friend void example::Animal::some_global_function (
    Animal * animal
) 
```




**See also:** [**Animal**](classexample_1_1_animal.md) 


**Parameters:**


* **animal** The pointer to the animal instance 




        

------------------------------
The documentation for this class was generated from the following file `src/animal.h`