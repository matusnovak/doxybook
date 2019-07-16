
# Class example::Animal


[**Class List**](api/annotated.md) **>** [**example**](api/namespaceexample.md) **>** [**Animal**](api/classexample_1_1Animal.md)



_Base class for all animals from which_ [_**Bird**_](api/classexample_1_1Bird.md) _derives._[More...](#detailed-description)

* `#include <animal.h>`



Inherits the following classes: [example::AnimalInterface](api/classexample_1_1AnimalInterface.md)


Inherited by the following classes: [example::Bird](api/classexample_1_1Bird.md)





## Classes

| Type | Name |
| ---: | :--- |
| struct | [**Result**](api/structexample_1_1Animal_1_1Result.md) <br>_Some random inner class of_ [_**Animal**_](api/classexample_1_1Animal.md) _._ |

## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::pair&lt; [**Animal**](api/classexample_1_1Animal.md) \*, [**Animal**](api/classexample_1_1Animal.md) \* &gt; | [**Parents**](api/classexample_1_1Animal.md#typedef-parents)  <br> |
| enum  | [**Type**](api/classexample_1_1Animal.md#enum-type)  <br>_The 6 classes of animal kingdom._  |








## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Animal**](api/classexample_1_1Animal.md#function-animal-13) ([**Type**](api/classexample_1_1Animal.md#enum-type) type, const std::string & name, [**Animal**](api/classexample_1_1Animal.md) \* mother=nullptr, [**Animal**](api/classexample_1_1Animal.md) \* father=nullptr) <br>_The main constructor._  |
|   | [**Animal**](api/classexample_1_1Animal.md#function-animal-23) (const [**Animal**](api/classexample_1_1Animal.md) & other) = delete<br> |
|   | [**Animal**](api/classexample_1_1Animal.md#function-animal-33) ([**Animal**](api/classexample_1_1Animal.md) && animal) noexcept<br> |
|  const std::string & | [**get\_name**](api/classexample_1_1Animal.md#function-get_name) () const<br>_Get the name of the animal._  |
| virtual int | [**get\_num\_of\_eyes**](api/classexample_1_1Animal.md#function-get_num_of_eyes) () override const<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](api/classexample_1_1Animal.md#function-get_num_of_limbs) () override const<br>_Returns the number of limbs._  |
|  [**Parents**](api/classexample_1_1Animal.md#typedef-parents) | [**get\_parents**](api/classexample_1_1Animal.md#function-get_parents) () const<br> |
| virtual bool | [**has\_tail**](api/classexample_1_1Animal.md#function-has_tail) () override const<br>_Returns true if the animal has a tail._  |
| virtual void | [**make\_sound**](api/classexample_1_1Animal.md#function-make_sound) () = 0<br> |
| virtual void | [**move**](api/classexample_1_1Animal.md#function-move) () <br> |
|   | [**operator bool**](api/classexample_1_1Animal.md#function-operator-bool) () const<br>_Returns true if this is an valid animal._  |
|  [**Animal**](api/classexample_1_1Animal.md) & | [**operator=**](api/classexample_1_1Animal.md#function-operator) (const [**Animal**](api/classexample_1_1Animal.md) & other) = delete<br>_Deleted copy operator._  |
|  [**Animal**](api/classexample_1_1Animal.md) & | [**operator=**](api/classexample_1_1Animal.md#function-operator-1) ([**Animal**](api/classexample_1_1Animal.md) && other) noexcept<br>_Move operator._  |
|  void | [**some\_inline\_member\_function**](api/classexample_1_1Animal.md#function-some_inline_member_function) ([**Animal**](api/classexample_1_1Animal.md) \* animal) <br>_Lorem Ipsum._  |
|  void | [**swap**](api/classexample_1_1Animal.md#function-swap) ([**Animal**](api/classexample_1_1Animal.md) & other) noexcept<br> |
| virtual  | [**~Animal**](api/classexample_1_1Animal.md#function-animal) () = default<br> |

## Public Functions inherited from example::AnimalInterface

See [example::AnimalInterface](api/classexample_1_1AnimalInterface.md)

| Type | Name |
| ---: | :--- |
| virtual int | [**get\_num\_of\_eyes**](api/classexample_1_1AnimalInterface.md#function-get_num_of_eyes) () const = 0<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](api/classexample_1_1AnimalInterface.md#function-get_num_of_limbs) () const = 0<br>_Returns the number of limbs._  |
| virtual bool | [**has\_tail**](api/classexample_1_1AnimalInterface.md#function-has_tail) () const = 0<br>_Returns true if the animal has a tail._  |

## Public Static Functions

| Type | Name |
| ---: | :--- |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**find\_child\_by\_name**](api/classexample_1_1Animal.md#function-find_child_by_name) ([**Animal**](api/classexample_1_1Animal.md) \* parent) <br> |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**find\_parent\_by\_name**](api/classexample_1_1Animal.md#function-find_parent_by_name) ([**Animal**](api/classexample_1_1Animal.md) \* child) <br> |






## Protected Attributes

| Type | Name |
| ---: | :--- |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**father**](api/classexample_1_1Animal.md#variable-father)  <br>_The pointer to the father._  |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**mother**](api/classexample_1_1Animal.md#variable-mother)  <br>_The pointer to the mother._  |
|  std::string | [**name**](api/classexample_1_1Animal.md#variable-name)  <br> |








# Detailed Description


Lorem Ipsum Donor. Some [Random link with **bold** and _italics_](http://github.com) And the following is a `typewritter` font.

Example code:


````cpp
Animal animal = Animal("Hello World", nullptr, nullptr);
std::cout << animal.get_name() << std::endl;
````

 

**See also:** [**Bird**](api/classexample_1_1Bird.md) 


**Bug**

Some random bug 



**Note:**

Some random note 




**Warning:**

Some random warning 




**Test**

Some random test description 



**Todo**

Some random todo 



**Template parameters:**


* T Some random template paramater description which actually does not exist in the code! 



**Precondition:**

First initialize the system. 




**Date:**

2017-2018 




**Author:**

Matus Novak 




**Author:**

Hello World 




    
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


Use this constructor to allocate a new instance of [**Animal**](api/classexample_1_1Animal.md) 

**Parameters:**


* type The type of the animal that matches [**Animal::Type**](api/classexample_1_1Animal.md#enum-type) 
* name Any name to associate the animal with 



**Exception:**


* [**CustomException**](api/classexample_1_1CustomException.md) If either only mother or father is assigned 



        

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




**See also:** [**get\_num\_of\_limbs**](api/classexample_1_1Animal.md#function-get_num_of_limbs), [**get\_num\_of\_eyes**](api/classexample_1_1Animal.md#function-get_num_of_eyes) 


        
Implements [*example::AnimalInterface::get\_num\_of\_eyes*](api/classexample_1_1AnimalInterface.md#function-get_num_of_eyes)


### function get\_num\_of\_limbs 


```cpp
virtual int example::Animal::get_num_of_limbs () override const
```




**See also:** [**get\_num\_of\_eyes**](api/classexample_1_1Animal.md#function-get_num_of_eyes), [**get\_num\_of\_limbs**](api/classexample_1_1Animal.md#function-get_num_of_limbs) 


        
Implements [*example::AnimalInterface::get\_num\_of\_limbs*](api/classexample_1_1AnimalInterface.md#function-get_num_of_limbs)


### function get\_parents 


```cpp
inline Parents example::Animal::get_parents () const
```



### function has\_tail 


```cpp
virtual bool example::Animal::has_tail () override const
```




**See also:** [**get\_num\_of\_limbs**](api/classexample_1_1Animal.md#function-get_num_of_limbs), [**get\_num\_of\_eyes**](api/classexample_1_1Animal.md#function-get_num_of_eyes) 


**Return value:**


* true Does have a tail 
* false Does not have a tail 



        
Implements [*example::AnimalInterface::has\_tail*](api/classexample_1_1AnimalInterface.md#function-has_tail)


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




**See also:** [**Animal**](api/classexample_1_1Animal.md) 


**Parameters:**


* animal The pointer to the animal instance

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




**See also:** [**Animal**](api/classexample_1_1Animal.md) 


**Parameters:**


* animal The pointer to the animal instance 



        

------------------------------
The documentation for this class was generated from the following file `src/animal.h`