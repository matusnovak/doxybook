
# Class example::Bird


[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **>** [**Bird**](classexample_1_1_bird.md)





* `#include <bird.h>`



Inherits the following classes: [example::Animal](classexample_1_1_animal.md)


Inherited by the following classes: [example::SpecialBird](classexample_1_1_special_bird.md)







## Public Types inherited from example::Animal

See [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
| typedef std::pair&lt; [**Animal**](classexample_1_1_animal.md) \*, [**Animal**](classexample_1_1_animal.md) \* &gt; | [**Parents**](classexample_1_1_animal.md#typedef-parents)  <br> |
| enum  | [**Type**](classexample_1_1_animal.md#enum-type)  <br>_The 6 classes of animal kingdom._  |











## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Bird**](classexample_1_1_bird.md#function-bird-13) (const std::string & name, [**Bird**](classexample_1_1_bird.md) \* mother=nullptr, [**Bird**](classexample_1_1_bird.md) \* father=nullptr) <br> |
|   | [**Bird**](classexample_1_1_bird.md#function-bird-23) (const [**Bird**](classexample_1_1_bird.md) & other) = delete<br> |
|   | [**Bird**](classexample_1_1_bird.md#function-bird-33) ([**Bird**](classexample_1_1_bird.md) && Bird) noexcept<br> |
| virtual void | [**make\_sound**](classexample_1_1_bird.md#function-make_sound) () override<br> |
| virtual void | [**move**](classexample_1_1_bird.md#function-move) () override<br> |
|  [**Bird**](classexample_1_1_bird.md) & | [**operator=**](classexample_1_1_bird.md#function-operator) (const [**Bird**](classexample_1_1_bird.md) & other) = delete<br>_Deleted copy operator._  |
|  [**Bird**](classexample_1_1_bird.md) & | [**operator=**](classexample_1_1_bird.md#function-operator-1) ([**Bird**](classexample_1_1_bird.md) && other) noexcept<br>_Move operator._  |
|  void | [**swap**](classexample_1_1_bird.md#function-swap) ([**Bird**](classexample_1_1_bird.md) & other) noexcept<br> |
|   | [**~Bird**](classexample_1_1_bird.md#function-bird) () = default<br> |

## Public Functions inherited from example::Animal

See [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
|   | [**Animal**](classexample_1_1_animal.md#function-animal-13) ([**Type**](classexample_1_1_animal.md#enum-type) type, const std::string & name, [**Animal**](classexample_1_1_animal.md) \* mother=nullptr, [**Animal**](classexample_1_1_animal.md) \* father=nullptr) <br>_The main constructor._  |
|   | [**Animal**](classexample_1_1_animal.md#function-animal-23) (const [**Animal**](classexample_1_1_animal.md) & other) = delete<br> |
|   | [**Animal**](classexample_1_1_animal.md#function-animal-33) ([**Animal**](classexample_1_1_animal.md) && animal) noexcept<br> |
|  const std::string & | [**get\_name**](classexample_1_1_animal.md#function-get_name) () const<br>_Get the name of the animal._  |
| virtual int | [**get\_num\_of\_eyes**](classexample_1_1_animal.md#function-get_num_of_eyes) () override const<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](classexample_1_1_animal.md#function-get_num_of_limbs) () override const<br>_Returns the number of limbs._  |
|  [**Parents**](classexample_1_1_animal.md#typedef-parents) | [**get\_parents**](classexample_1_1_animal.md#function-get_parents) () const<br> |
| virtual bool | [**has\_tail**](classexample_1_1_animal.md#function-has_tail) () override const<br>_Returns true if the animal has a tail._  |
| virtual void | [**make\_sound**](classexample_1_1_animal.md#function-make_sound) () = 0<br> |
| virtual void | [**move**](classexample_1_1_animal.md#function-move) () <br> |
|   | [**operator bool**](classexample_1_1_animal.md#function-operator-bool) () const<br>_Returns true if this is an valid animal._  |
|  [**Animal**](classexample_1_1_animal.md) & | [**operator=**](classexample_1_1_animal.md#function-operator) (const [**Animal**](classexample_1_1_animal.md) & other) = delete<br>_Deleted copy operator._  |
|  [**Animal**](classexample_1_1_animal.md) & | [**operator=**](classexample_1_1_animal.md#function-operator-1) ([**Animal**](classexample_1_1_animal.md) && other) noexcept<br>_Move operator._  |
|  void | [**some\_inline\_member\_function**](classexample_1_1_animal.md#function-some_inline_member_function) ([**Animal**](classexample_1_1_animal.md) \* animal) <br>_Lorem Ipsum._  |
|  void | [**swap**](classexample_1_1_animal.md#function-swap) ([**Animal**](classexample_1_1_animal.md) & other) noexcept<br> |
| virtual  | [**~Animal**](classexample_1_1_animal.md#function-animal) () = default<br> |

## Public Functions inherited from example::AnimalInterface

See [example::AnimalInterface](classexample_1_1_animal_interface.md)

| Type | Name |
| ---: | :--- |
| virtual int | [**get\_num\_of\_eyes**](classexample_1_1_animal_interface.md#function-get_num_of_eyes) () const = 0<br>_Returns the number of eyes._  |
| virtual int | [**get\_num\_of\_limbs**](classexample_1_1_animal_interface.md#function-get_num_of_limbs) () const = 0<br>_Returns the number of limbs._  |
| virtual bool | [**has\_tail**](classexample_1_1_animal_interface.md#function-has_tail) () const = 0<br>_Returns true if the animal has a tail._  |


## Public Static Functions inherited from example::Animal

See [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
|  [**Animal**](classexample_1_1_animal.md) \* | [**find\_child\_by\_name**](classexample_1_1_animal.md#function-find_child_by_name) ([**Animal**](classexample_1_1_animal.md) \* parent) <br> |
|  [**Animal**](classexample_1_1_animal.md) \* | [**find\_parent\_by\_name**](classexample_1_1_animal.md#function-find_parent_by_name) ([**Animal**](classexample_1_1_animal.md) \* child) <br> |









## Protected Attributes inherited from example::Animal

See [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
|  [**Animal**](classexample_1_1_animal.md) \* | [**father**](classexample_1_1_animal.md#variable-father)  <br>_The pointer to the father._  |
|  [**Animal**](classexample_1_1_animal.md) \* | [**mother**](classexample_1_1_animal.md#variable-mother)  <br>_The pointer to the mother._  |
|  std::string | [**name**](classexample_1_1_animal.md#variable-name)  <br> |











## Public Functions Documentation


### function Bird [1/3]


```cpp
example::Bird::Bird (
    const std::string & name,
    Bird * mother=nullptr,
    Bird * father=nullptr
) 
```



### function Bird [2/3]


```cpp
example::Bird::Bird (
    const Bird & other
) = delete
```



### function Bird [3/3]


```cpp
example::Bird::Bird (
    Bird && Bird
) noexcept
```



### function make\_sound 


```cpp
virtual void example::Bird::make_sound () override
```


Implements [*example::Animal::make\_sound*](classexample_1_1_animal.md#function-make_sound)


### function move 


```cpp
virtual void example::Bird::move () override
```


Implements [*example::Animal::move*](classexample_1_1_animal.md#function-move)


### function operator= 


```cpp
Bird & example::Bird::operator= (
    const Bird & other
) = delete
```



### function operator= 


```cpp
Bird & example::Bird::operator= (
    Bird && other
) noexcept
```



### function swap 


```cpp
void example::Bird::swap (
    Bird & other
) noexcept
```



### function ~Bird 


```cpp
example::Bird::~Bird () = default
```



------------------------------
The documentation for this class was generated from the following file `src/bird.h`