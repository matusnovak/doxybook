---
search:
    keywords: ['example::Animal', 'Result', 'Type', 'Parents', 'mother', 'father', 'name', 'find_parent_by_name', 'find_child_by_name', 'Animal', 'Animal', 'Animal', '~Animal', 'operator bool', 'swap', 'get_num_of_limbs', 'get_num_of_eyes', 'has_tail', 'move', 'make_sound', 'get_parents', 'get_name', 'operator=', 'operator=', 'some_global_function']
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
|enum|[**Type**](classexample_1_1_animal.md#1adc9e490a8ea5390fbcaf6ffa24c3ec69) { **NONE** = 0, **INSECT** = 1, **AMPHIBIAN** = 2, **BIRD** = 3, **FISH** = 4, **REPTILE** = 5, **MAMMAL** = 6 } <br>The 6 classes of animal kingdom. |
|typedef std::pair< **[Animal](classexample_1_1_animal.md)** \*, **[Animal](classexample_1_1_animal.md)** \* >|[**Parents**](classexample_1_1_animal.md#1a3fc3e692a61c2e21080fef955df099d5)|


## Protected Attributes

|Type|Name|
|-----|-----|
|**[Animal](classexample_1_1_animal.md)** \*|[**mother**](classexample_1_1_animal.md#1a77ebfd8268da42527748bc17f458c02c)<br>The pointer to the mother. |
|**[Animal](classexample_1_1_animal.md)** \*|[**father**](classexample_1_1_animal.md#1aeaabef8bc7cd869f09db725e0fcc5092)<br>The pointer to the father. |
|std::string|[**name**](classexample_1_1_animal.md#1a9362efc813ef23964f7f6f57640a12e7)|


## Public Static Functions

|Type|Name|
|-----|-----|
|static **[Animal](classexample_1_1_animal.md)** \*|[**find\_parent\_by\_name**](classexample_1_1_animal.md#1a7ff2cbf990657553d95f6d15fb0f4568) (**[Animal](classexample_1_1_animal.md)** \* child) |
|static **[Animal](classexample_1_1_animal.md)** \*|[**find\_child\_by\_name**](classexample_1_1_animal.md#1a1d509e63586d5fe3edc86d393f88910b) (**[Animal](classexample_1_1_animal.md)** \* parent) |


## Public Functions

|Type|Name|
|-----|-----|
||[**Animal**](classexample_1_1_animal.md#1acef1db6802de001a01c403afeca90c86) (**[Type](classexample_1_1_animal.md#1adc9e490a8ea5390fbcaf6ffa24c3ec69)** type, const std::string & name, **[Animal](classexample_1_1_animal.md)** \* mother = nullptr, **[Animal](classexample_1_1_animal.md)** \* father = nullptr) <br>The main constructor. |
||[**Animal**](classexample_1_1_animal.md#1a612d7d2e9631e6f241e871b3785f4cdf) (const **[Animal](classexample_1_1_animal.md)** & other) = delete |
||[**Animal**](classexample_1_1_animal.md#1a29db85a24acf4fd5fb353c871eb086ed) (**[Animal](classexample_1_1_animal.md)** && animal) noexcept |
|virtual |[**~Animal**](classexample_1_1_animal.md#1a7b633f0bc3834108ca024d0c73dc135e) () = default |
||[**operator bool**](classexample_1_1_animal.md#1aba77090c59b9c50d026032ed998c862d) () const <br>Returns true if this is an valid animal. |
|void|[**swap**](classexample_1_1_animal.md#1affec460d5bc2fb8d650fcf5b7b8cf396) (**[Animal](classexample_1_1_animal.md)** & other) noexcept |
|virtual int|[**get\_num\_of\_limbs**](classexample_1_1_animal.md#1a77ea3286e2b43830a5443be76eec4c5f) () override const <br>Returns the number of limbs. |
|virtual int|[**get\_num\_of\_eyes**](classexample_1_1_animal.md#1afc4972484d411d75bdc829be3502bb60) () override const <br>Returns the number of eyes. |
|virtual bool|[**has\_tail**](classexample_1_1_animal.md#1a80c789f01a9e211b821cfa57c27792fa) () override const <br>Returns true if the animal has a tail. |
|virtual void|[**move**](classexample_1_1_animal.md#1aaee0d759d18beaca18670d2a794b1445) () |
|virtual void|[**make\_sound**](classexample_1_1_animal.md#1a6939f9fed1a387b128d3947afc239873) () = 0|
|Parents|[**get\_parents**](classexample_1_1_animal.md#1a93c61aed16aeb0b52631961e17251b0f) () const |
|const std::string &|[**get\_name**](classexample_1_1_animal.md#1ab4e7a34b9637acc89c55eec9405f1f6e) () const <br>Get the name of the animal. |
|**[Animal](classexample_1_1_animal.md)** &|[**operator=**](classexample_1_1_animal.md#1a021864d5b75ff00550cd4ffe65f4014d) (const **[Animal](classexample_1_1_animal.md)** & other) = delete <br>Deleted copy operator. |
|**[Animal](classexample_1_1_animal.md)** &|[**operator=**](classexample_1_1_animal.md#1a055b1b5d5ffaa302068e7000b1b9f4f7) (**[Animal](classexample_1_1_animal.md)** && other) noexcept <br>Move operator. |


## Friends

|Type|Name|
|-----|-----|
|friend void|[**some\_global\_function**](classexample_1_1_animal.md#1aa7ca55f69abe84eade027036327d6f34)<br>Some random global function that modifies **[Animal](classexample_1_1_animal.md)**. |


## Detailed Description

Lorem Ipsum Donor. Some [Random link with **bold** and _italics_](http://github.com) And the following is a `typewritter` font.
Example code:

```cpp
Animal animal = Animal("Hello World", nullptr, nullptr);
std::cout << animal.get_name() << std::endl;
```

 

**See also:** **[Bird](classexample_1_1_bird.md)** 


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

### enum <a id="1adc9e490a8ea5390fbcaf6ffa24c3ec69" href="#1adc9e490a8ea5390fbcaf6ffa24c3ec69">Type</a>

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

### typedef <a id="1a3fc3e692a61c2e21080fef955df099d5" href="#1a3fc3e692a61c2e21080fef955df099d5">Parents</a>

```cpp
typedef std::pair<Animal*, Animal*> example::Animal::Parents;
```



## Protected Attributes Documentation

### variable <a id="1a77ebfd8268da42527748bc17f458c02c" href="#1a77ebfd8268da42527748bc17f458c02c">mother</a>

```cpp
Animal* example::Animal::mother;
```

The pointer to the mother. 

Can be null! 

### variable <a id="1aeaabef8bc7cd869f09db725e0fcc5092" href="#1aeaabef8bc7cd869f09db725e0fcc5092">father</a>

```cpp
Animal* example::Animal::father;
```

The pointer to the father. 

Can be null! 

### variable <a id="1a9362efc813ef23964f7f6f57640a12e7" href="#1a9362efc813ef23964f7f6f57640a12e7">name</a>

```cpp
std::string example::Animal::name;
```



## Public Static Functions Documentation

### function <a id="1a7ff2cbf990657553d95f6d15fb0f4568" href="#1a7ff2cbf990657553d95f6d15fb0f4568">find\_parent\_by\_name</a>

```cpp
static Animal * example::Animal::find_parent_by_name (
    Animal * child
)
```



### function <a id="1a1d509e63586d5fe3edc86d393f88910b" href="#1a1d509e63586d5fe3edc86d393f88910b">find\_child\_by\_name</a>

```cpp
static Animal * example::Animal::find_child_by_name (
    Animal * parent
)
```



## Public Functions Documentation

### function <a id="1acef1db6802de001a01c403afeca90c86" href="#1acef1db6802de001a01c403afeca90c86">Animal (1/3)</a>

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


* **type** The type of the animal that matches **[Animal::Type](classexample_1_1_animal.md#1adc9e490a8ea5390fbcaf6ffa24c3ec69)** 
* **name** Any name to associate the animal with 



**Exception:**


* ****[CustomException](classexample_1_1_custom_exception.md)**** If either only mother or father is assigned 



### function <a id="1a612d7d2e9631e6f241e871b3785f4cdf" href="#1a612d7d2e9631e6f241e871b3785f4cdf">Animal (2/3)</a>

```cpp
example::Animal::Animal (
    const Animal & other
) = delete
```



### function <a id="1a29db85a24acf4fd5fb353c871eb086ed" href="#1a29db85a24acf4fd5fb353c871eb086ed">Animal (3/3)</a>

```cpp
example::Animal::Animal (
    Animal && animal
) noexcept
```



### function <a id="1a7b633f0bc3834108ca024d0c73dc135e" href="#1a7b633f0bc3834108ca024d0c73dc135e">~Animal</a>

```cpp
virtual example::Animal::~Animal () = default
```



### function <a id="1aba77090c59b9c50d026032ed998c862d" href="#1aba77090c59b9c50d026032ed998c862d">operator bool</a>

```cpp
example::Animal::operator bool () const
```

Returns true if this is an valid animal. 

Lorem Ipsum returns true 

### function <a id="1affec460d5bc2fb8d650fcf5b7b8cf396" href="#1affec460d5bc2fb8d650fcf5b7b8cf396">swap</a>

```cpp
void example::Animal::swap (
    Animal & other
) noexcept
```



### function <a id="1a77ea3286e2b43830a5443be76eec4c5f" href="#1a77ea3286e2b43830a5443be76eec4c5f">get\_num\_of\_limbs</a>

```cpp
virtual int example::Animal::get_num_of_limbs () const
```

Returns the number of limbs. 



**See also:** **[get\_num\_of\_eyes](classexample_1_1_animal.md#1afc4972484d411d75bdc829be3502bb60)**, **[get\_num\_of\_limbs](classexample_1_1_animal.md#1a77ea3286e2b43830a5443be76eec4c5f)** 


Implements **[AnimalInterface::get\_num\_of\_limbs](classexample_1_1_animal_interface.md#1a0300198be5798cfa0350fbb2fde4295e)**


### function <a id="1afc4972484d411d75bdc829be3502bb60" href="#1afc4972484d411d75bdc829be3502bb60">get\_num\_of\_eyes</a>

```cpp
virtual int example::Animal::get_num_of_eyes () const
```

Returns the number of eyes. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal.md#1a77ea3286e2b43830a5443be76eec4c5f)**, **[get\_num\_of\_eyes](classexample_1_1_animal.md#1afc4972484d411d75bdc829be3502bb60)** 


Implements **[AnimalInterface::get\_num\_of\_eyes](classexample_1_1_animal_interface.md#1a63c32ae61aa4ee35b3666b08ce3378f9)**


### function <a id="1a80c789f01a9e211b821cfa57c27792fa" href="#1a80c789f01a9e211b821cfa57c27792fa">has\_tail</a>

```cpp
virtual bool example::Animal::has_tail () const
```

Returns true if the animal has a tail. 



**See also:** **[get\_num\_of\_limbs](classexample_1_1_animal.md#1a77ea3286e2b43830a5443be76eec4c5f)**, **[get\_num\_of\_eyes](classexample_1_1_animal.md#1afc4972484d411d75bdc829be3502bb60)** 


**Return value:**


* **true** Does have a tail 
* **false** Does not have a tail 



Implements **[AnimalInterface::has\_tail](classexample_1_1_animal_interface.md#1af994135a8e875998808ca7f11f12a6b3)**


### function <a id="1aaee0d759d18beaca18670d2a794b1445" href="#1aaee0d759d18beaca18670d2a794b1445">move</a>

```cpp
virtual void example::Animal::move ()
```



### function <a id="1a6939f9fed1a387b128d3947afc239873" href="#1a6939f9fed1a387b128d3947afc239873">make\_sound</a>

```cpp
virtual void example::Animal::make_sound () = 0
```



### function <a id="1a93c61aed16aeb0b52631961e17251b0f" href="#1a93c61aed16aeb0b52631961e17251b0f">get\_parents</a>

```cpp
Parents example::Animal::get_parents () const
```



### function <a id="1ab4e7a34b9637acc89c55eec9405f1f6e" href="#1ab4e7a34b9637acc89c55eec9405f1f6e">get\_name</a>

```cpp
const std::string & example::Animal::get_name () const
```

Get the name of the animal. 



**Returns:**

A constant reference to the name 




### function <a id="1a021864d5b75ff00550cd4ffe65f4014d" href="#1a021864d5b75ff00550cd4ffe65f4014d">operator= (1/2)</a>

```cpp
Animal & example::Animal::operator= (
    const Animal & other
) = delete
```

Deleted copy operator. 


### function <a id="1a055b1b5d5ffaa302068e7000b1b9f4f7" href="#1a055b1b5d5ffaa302068e7000b1b9f4f7">operator= (2/2)</a>

```cpp
Animal & example::Animal::operator= (
    Animal && other
) noexcept
```

Move operator. 


## Friends Documentation

### friend <a id="1aa7ca55f69abe84eade027036327d6f34" href="#1aa7ca55f69abe84eade027036327d6f34">some\_global\_function</a>

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
