---
title: class example::Animal
meta:
  - name: keywords
    content: example::Animal Result Type Parents mother father name find_parent_by_name find_child_by_name Animal Animal Animal ~Animal operator bool swap get_num_of_limbs get_num_of_eyes has_tail move make_sound get_parents get_name operator= operator= some_global_function
---

# class example::Animal

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**Animal**](classexample_1_1_animal.md)


Base class for all animals from which **[Bird](classexample_1_1_bird.md)** derives. [More...](#detailed-description)


Inherits the following classes: **[example::AnimalInterface](classexample_1_1_animal_interface.md)**



Inherited by the following classes: **[example::Bird](classexample_1_1_bird.md)**

## Classes

|Type|Name|
|-----|-----|
|struct|[**Result**](structexample_1_1_animal_1_1_result.md)|


## Public Types

|Type|Name|
|-----|-----|
|enum|[**Type**](classexample_1_1_animal.md#enum-type) { **NONE** = 0, **INSECT** = 1, **AMPHIBIAN** = 2, **BIRD** = 3, **FISH** = 4, **REPTILE** = 5, **MAMMAL** = 6 } <br>The 6 classes of animal kingdom. |
|typedef std::pair< **[Animal](classexample_1_1_animal.md)** \*, **[Animal](classexample_1_1_animal.md)** \* >|[**Parents**](classexample_1_1_animal.md#typedef-parents)|


## Protected Attributes

|Type|Name|
|-----|-----|
|**[Animal](classexample_1_1_animal.md)** \*|[**mother**](classexample_1_1_animal.md#variable-mother)<br>The pointer to the mother. |
|**[Animal](classexample_1_1_animal.md)** \*|[**father**](classexample_1_1_animal.md#variable-father)<br>The pointer to the father. |
|std::string|[**name**](classexample_1_1_animal.md#variable-name)|


## Public Static Functions

|Type|Name|
|-----|-----|
|static **[Animal](classexample_1_1_animal.md)** \*|[**find\_parent\_by\_name**](classexample_1_1_animal.md#function-find-parent-by-name) (**[Animal](classexample_1_1_animal.md)** \* child) |
|static **[Animal](classexample_1_1_animal.md)** \*|[**find\_child\_by\_name**](classexample_1_1_animal.md#function-find-child-by-name) (**[Animal](classexample_1_1_animal.md)** \* parent) |


## Public Functions

|Type|Name|
|-----|-----|
||[**Animal**](classexample_1_1_animal.md#function-animal-1-3) (**[Type](classexample_1_1_animal.md#enum-type)** type, const std::string & name, **[Animal](classexample_1_1_animal.md)** \* mother = nullptr, **[Animal](classexample_1_1_animal.md)** \* father = nullptr) <br>The main constructor. |
||[**Animal**](classexample_1_1_animal.md#function-animal-2-3) (const **[Animal](classexample_1_1_animal.md)** & other) = delete |
||[**Animal**](classexample_1_1_animal.md#function-animal-3-3) (**[Animal](classexample_1_1_animal.md)** && animal) noexcept |
|virtual |[**~Animal**](classexample_1_1_animal.md#function-animal) () = default |
||[**operator bool**](classexample_1_1_animal.md#function-operator-bool) () const <br>Returns true if this is an valid animal. |
|void|[**swap**](classexample_1_1_animal.md#function-swap) (**[Animal](classexample_1_1_animal.md)** & other) noexcept |
|virtual int|[**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get-num-of-limbs) () override const <br>Returns the number of limbs. |
|virtual int|[**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get-num-of-eyes) () override const <br>Returns the number of eyes. |
|virtual bool|[**has\_tail**](classexample_1_1_animal.md#function-has-tail) () override const <br>Returns true if the animal has a tail. |
|virtual void|[**move**](classexample_1_1_animal.md#function-move) () |
|virtual void|[**make\_sound**](classexample_1_1_animal.md#function-make-sound) () = 0|
|Parents|[**get\_parents**](classexample_1_1_animal.md#function-get-parents) () const |
|const std::string &|[**get\_name**](classexample_1_1_animal.md#function-get-name) () const <br>Get the name of the animal. |
|**[Animal](classexample_1_1_animal.md)** &|[**operator=**](classexample_1_1_animal.md#function-operator-1-2) (const **[Animal](classexample_1_1_animal.md)** & other) = delete <br>Deleted copy operator. |
|**[Animal](classexample_1_1_animal.md)** &|[**operator=**](classexample_1_1_animal.md#function-operator-2-2) (**[Animal](classexample_1_1_animal.md)** && other) noexcept <br>Move operator. |


## Friends

|Type|Name|
|-----|-----|
|friend void|[**some\_global\_function**](classexample_1_1_animal.md#friend-some-global-function)<br>Some random global function that modifies **[Animal](classexample_1_1_animal.md)**. |


## Detailed Description

Lorem Ipsum Donor. Some [Random link with **bold** and _italics_](http://github.com) And the following is a `typewritter` font.
Example code:

```cpp
Animal animal = Animal("Hello World", nullptr, nullptr);
std::cout << animal.get_name() << std::endl;
```

 

**See also:** **[Bird](classexample_1_1_bird.md)** 
::: danger Bug:
Some random bug 

:::

::: tip Note:
Some random note 

:::


::: warning Warning:
Some random warning 

:::


**Test**

Some random test description 



**Todo**

Some random todo 



**Template parameters:**


* **T** Some random template paramater description which actually does not exist in the code! 



**Precondition:**

First initialize the system. 




**Date:**

2017-2018 




**Author:**

Matus Novak 




**Author:**

Hello World 



## Public Types Documentation

### enum Type

```cpp
enum example::Animal::Type {
    NONE = 0,
    INSECT = 1,
    AMPHIBIAN = 2,
    BIRD = 3,
    FISH = 4,
    REPTILE = 5,
    MAMMAL = 6,
};
```

The 6 classes of animal kingdom. 

Lorem Ipsum Donor. 

### typedef Parents

```cpp
typedef std::pair<Animal*, Animal*> example::Animal::Parents;
```



## Protected Attributes Documentation

### variable mother

```cpp
Animal* example::Animal::mother;
```

The pointer to the mother. 

Can be null! 

### variable father

```cpp
Animal* example::Animal::father;
```

The pointer to the father. 

Can be null! 

### variable name

```cpp
std::string example::Animal::name;
```



## Public Static Functions Documentation

### function find\_parent\_by\_name

```cpp
static Animal * example::Animal::find_parent_by_name (
    Animal * child
)
```



### function find\_child\_by\_name

```cpp
static Animal * example::Animal::find_child_by_name (
    Animal * parent
)
```



## Public Functions Documentation

### function Animal (1/3)

```cpp
example::Animal::Animal (
    Type type,
    const std::string & name,
    Animal * mother = nullptr,
    Animal * father = nullptr
)
```

The main constructor. 

Use this constructor to allocate a new instance of **[Animal](classexample_1_1_animal.md)** 

**Parameters:**


* **type** The type of the animal that matches **[Animal::Type](classexample_1_1_animal.md#enum-type)** 
* **name** Any name to associate the animal with 



**Exception:**


* ****[CustomException](classexample_1_1_custom_exception.md)**** If either only mother or father is assigned 



### function Animal (2/3)

```cpp
example::Animal::Animal (
    const Animal & other
) = delete
```



### function Animal (3/3)

```cpp
example::Animal::Animal (
    Animal && animal
) noexcept
```



### function ~Animal

```cpp
virtual example::Animal::~Animal () = default
```



### function operator bool

```cpp
example::Animal::operator bool () const
```

Returns true if this is an valid animal. 

Lorem Ipsum returns true 

### function swap

```cpp
void example::Animal::swap (
    Animal & other
) noexcept
```



### function get\_num\_of\_limbs

```cpp
virtual int example::Animal::get_num_of_limbs () const
```

Returns the number of limbs. 



**See also:** **[get\_num\_of\_eyes](classexample_1_1_animal.md#function-get-num-of-eyes)**, **[get\_num\_of\_limbs](classexample_1_1_animal.md#function-get-num-of-limbs)** 


Implements **[AnimalInterface::get\_num\_of\_limbs](classexample_1_1_animal_interface.md#function-get-num-of-limbs)**


### function get\_num\_of\_eyes

```cpp
virtual int example::Animal::get_num_of_eyes () const
```

Returns the number of eyes. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal.md#function-get-num-of-limbs)**, **[get\_num\_of\_eyes](classexample_1_1_animal.md#function-get-num-of-eyes)** 


Implements **[AnimalInterface::get\_num\_of\_eyes](classexample_1_1_animal_interface.md#function-get-num-of-eyes)**


### function has\_tail

```cpp
virtual bool example::Animal::has_tail () const
```

Returns true if the animal has a tail. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal.md#function-get-num-of-limbs)**, **[get\_num\_of\_eyes](classexample_1_1_animal.md#function-get-num-of-eyes)** 


**Return value:**


* **true** Does have a tail 
* **false** Does not have a tail 



Implements **[AnimalInterface::has\_tail](classexample_1_1_animal_interface.md#function-has-tail)**


### function move

```cpp
virtual void example::Animal::move ()
```



### function make\_sound

```cpp
virtual void example::Animal::make_sound () = 0
```



### function get\_parents

```cpp
Parents example::Animal::get_parents () const
```



### function get\_name

```cpp
const std::string & example::Animal::get_name () const
```

Get the name of the animal. 



**Returns:**

A constant reference to the name 




### function operator= (1/2)

```cpp
Animal & example::Animal::operator= (
    const Animal & other
) = delete
```

Deleted copy operator. 


### function operator= (2/2)

```cpp
Animal & example::Animal::operator= (
    Animal && other
) noexcept
```

Move operator. 


## Friends Documentation

### friend some\_global\_function

```cpp
friend void example::Animal::some_global_function (
    Animal * animal
)
```

Some random global function that modifies **[Animal](classexample_1_1_animal.md)**. 



**See also:** **[Animal](classexample_1_1_animal.md)** 


**Parameters:**


* **animal** The pointer to the animal instance 





----------------------------------------
The documentation for this class was generated from the following file: `src/animal.h`
