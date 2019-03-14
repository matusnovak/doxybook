
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


### <a href="#typedef-parents" id="typedef-parents">typedef Parents </a>


```cpp
typedef std::pair<Animal*, Animal*> example::Animal::Parents;
```



### <a href="#enum-type" id="enum-type">enum Type </a>


```cpp
enum example::Animal::Type {
    **NONE** = 0,
    **INSECT** = 1,
    **AMPHIBIAN** = 2,
    **BIRD** = 3,
    **FISH** = 4,
    **REPTILE** = 5,
    **MAMMAL** = 6
};
```


Lorem Ipsum Donor. 


        
## Public Functions Documentation


### <a href="#function-animal-1-3" id="function-animal-1-3">function Animal [1/3]</a>


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




        

### <a href="#function-animal-2-3" id="function-animal-2-3">function Animal [2/3]</a>


```cpp
example::Animal::Animal (
    const Animal & other
) = delete
```



### <a href="#function-animal-3-3" id="function-animal-3-3">function Animal [3/3]</a>


```cpp
example::Animal::Animal (
    Animal && animal
) noexcept
```



### <a href="#function-get-name" id="function-get-name">function get\_name </a>


```cpp
inline const std::string & example::Animal::get_name () const
```




**Returns:**

A constant reference to the name 





        

### <a href="#function-get-num-of-eyes" id="function-get-num-of-eyes">function get\_num\_of\_eyes </a>


```cpp
virtual int example::Animal::get_num_of_eyes () override const
```




**See also:** [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs), [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes) 



        
Implements [*example::AnimalInterface::get\_num\_of\_eyes*](classexample_1_1_animal_interface.md#function-get-num-of-eyes)


### <a href="#function-get-num-of-limbs" id="function-get-num-of-limbs">function get\_num\_of\_limbs </a>


```cpp
virtual int example::Animal::get_num_of_limbs () override const
```




**See also:** [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes), [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs) 



        
Implements [*example::AnimalInterface::get\_num\_of\_limbs*](classexample_1_1_animal_interface.md#function-get-num-of-limbs)


### <a href="#function-get-parents" id="function-get-parents">function get\_parents </a>


```cpp
inline Parents example::Animal::get_parents () const
```



### <a href="#function-has-tail" id="function-has-tail">function has\_tail </a>


```cpp
virtual bool example::Animal::has_tail () override const
```




**See also:** [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs), [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes) 


**Return value:**


* **true** Does have a tail 
* **false** Does not have a tail 




        
Implements [*example::AnimalInterface::has\_tail*](classexample_1_1_animal_interface.md#function-has-tail)


### <a href="#function-make-sound" id="function-make-sound">function make\_sound </a>


```cpp
virtual void example::Animal::make_sound () = 0
```



### <a href="#function-move" id="function-move">function move </a>


```cpp
virtual void example::Animal::move () 
```



### <a href="#function-operator-bool" id="function-operator-bool">function operator bool </a>


```cpp
example::Animal::operator bool () const
```


Lorem Ipsum returns true 


        

### <a href="#function-operator" id="function-operator">function operator= </a>


```cpp
Animal & example::Animal::operator= (
    const Animal & other
) = delete
```



### <a href="#function-operator-2" id="function-operator-2">function operator= </a>


```cpp
Animal & example::Animal::operator= (
    Animal && other
) noexcept
```



### <a href="#function-some-inline-member-function" id="function-some-inline-member-function">function some\_inline\_member\_function </a>


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





        

### <a href="#function-swap" id="function-swap">function swap </a>


```cpp
void example::Animal::swap (
    Animal & other
) noexcept
```



### <a href="#function-animal" id="function-animal">function ~Animal </a>


```cpp
virtual example::Animal::~Animal () = default
```


## Public Static Functions Documentation


### <a href="#function-find-child-by-name" id="function-find-child-by-name">function find\_child\_by\_name </a>


```cpp
static Animal * example::Animal::find_child_by_name (
    Animal * parent
) 
```



### <a href="#function-find-parent-by-name" id="function-find-parent-by-name">function find\_parent\_by\_name </a>


```cpp
static Animal * example::Animal::find_parent_by_name (
    Animal * child
) 
```


## Protected Attributes Documentation


### <a href="#variable-father" id="variable-father">variable father </a>


```cpp
Animal* example::Animal::father;
```


Can be null! 


        

### <a href="#variable-mother" id="variable-mother">variable mother </a>


```cpp
Animal* example::Animal::mother;
```


Can be null! 


        

### <a href="#variable-name" id="variable-name">variable name </a>


```cpp
std::string example::Animal::name;
```

## Friends Documentation



### <a href="#friend-some-global-function" id="friend-some-global-function">friend some\_global\_function </a>


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