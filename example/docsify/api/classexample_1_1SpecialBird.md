
# Class example::SpecialBird


[**Class List**](api/annotated.md) **>** [**example**](api/namespaceexample.md) **>** [**SpecialBird**](api/classexample_1_1SpecialBird.md)





* `#include <special_bird.h>`



Inherits the following classes: [example::Bird](api/classexample_1_1Bird.md)










## Public Types inherited from example::Animal

See [example::Animal](api/classexample_1_1Animal.md)

| Type | Name |
| ---: | :--- |
| typedef std::pair&lt; [**Animal**](api/classexample_1_1Animal.md) \*, [**Animal**](api/classexample_1_1Animal.md) \* &gt; | [**Parents**](api/classexample_1_1Animal.md#typedef-parents)  <br> |
| enum  | [**Type**](api/classexample_1_1Animal.md#enum-type)  <br>_The 6 classes of animal kingdom._  |














## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SpecialBird**](api/classexample_1_1SpecialBird.md#function-specialbird-13) (const std::string & name, [**SpecialBird**](api/classexample_1_1SpecialBird.md) \* mother=nullptr, [**SpecialBird**](api/classexample_1_1SpecialBird.md) \* father=nullptr) <br> |
|   | [**SpecialBird**](api/classexample_1_1SpecialBird.md#function-specialbird-23) (const [**SpecialBird**](api/classexample_1_1SpecialBird.md) & other) = delete<br> |
|   | [**SpecialBird**](api/classexample_1_1SpecialBird.md#function-specialbird-33) ([**SpecialBird**](api/classexample_1_1SpecialBird.md) && SpecialBird) noexcept<br> |
|  void | [**do\_something\_special**](api/classexample_1_1SpecialBird.md#function-do_something_special) () <br> |
|  [**SpecialBird**](api/classexample_1_1SpecialBird.md) & | [**operator=**](api/classexample_1_1SpecialBird.md#function-operator) (const [**SpecialBird**](api/classexample_1_1SpecialBird.md) & other) = delete<br> |
|  [**SpecialBird**](api/classexample_1_1SpecialBird.md) & | [**operator=**](api/classexample_1_1SpecialBird.md#function-operator-1) ([**SpecialBird**](api/classexample_1_1SpecialBird.md) && other) noexcept<br> |
|  void | [**swap**](api/classexample_1_1SpecialBird.md#function-swap) ([**SpecialBird**](api/classexample_1_1SpecialBird.md) & other) noexcept<br> |
|   | [**~SpecialBird**](api/classexample_1_1SpecialBird.md#function-specialbird) () = default<br> |

## Public Functions inherited from example::Bird

See [example::Bird](api/classexample_1_1Bird.md)

| Type | Name |
| ---: | :--- |
|   | [**Bird**](api/classexample_1_1Bird.md#function-bird-13) (const std::string & name, [**Bird**](api/classexample_1_1Bird.md) \* mother=nullptr, [**Bird**](api/classexample_1_1Bird.md) \* father=nullptr) <br> |
|   | [**Bird**](api/classexample_1_1Bird.md#function-bird-23) (const [**Bird**](api/classexample_1_1Bird.md) & other) = delete<br> |
|   | [**Bird**](api/classexample_1_1Bird.md#function-bird-33) ([**Bird**](api/classexample_1_1Bird.md) && Bird) noexcept<br> |
| virtual void | [**make\_sound**](api/classexample_1_1Bird.md#function-make_sound) () override<br> |
| virtual void | [**move**](api/classexample_1_1Bird.md#function-move) () override<br> |
|  [**Bird**](api/classexample_1_1Bird.md) & | [**operator=**](api/classexample_1_1Bird.md#function-operator) (const [**Bird**](api/classexample_1_1Bird.md) & other) = delete<br>_Deleted copy operator._  |
|  [**Bird**](api/classexample_1_1Bird.md) & | [**operator=**](api/classexample_1_1Bird.md#function-operator-1) ([**Bird**](api/classexample_1_1Bird.md) && other) noexcept<br>_Move operator._  |
|  void | [**swap**](api/classexample_1_1Bird.md#function-swap) ([**Bird**](api/classexample_1_1Bird.md) & other) noexcept<br> |
|   | [**~Bird**](api/classexample_1_1Bird.md#function-bird) () = default<br> |

## Public Functions inherited from example::Animal

See [example::Animal](api/classexample_1_1Animal.md)

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



## Public Static Functions inherited from example::Animal

See [example::Animal](api/classexample_1_1Animal.md)

| Type | Name |
| ---: | :--- |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**find\_child\_by\_name**](api/classexample_1_1Animal.md#function-find_child_by_name) ([**Animal**](api/classexample_1_1Animal.md) \* parent) <br> |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**find\_parent\_by\_name**](api/classexample_1_1Animal.md#function-find_parent_by_name) ([**Animal**](api/classexample_1_1Animal.md) \* child) <br> |












## Protected Attributes inherited from example::Animal

See [example::Animal](api/classexample_1_1Animal.md)

| Type | Name |
| ---: | :--- |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**father**](api/classexample_1_1Animal.md#variable-father)  <br>_The pointer to the father._  |
|  [**Animal**](api/classexample_1_1Animal.md) \* | [**mother**](api/classexample_1_1Animal.md#variable-mother)  <br>_The pointer to the mother._  |
|  std::string | [**name**](api/classexample_1_1Animal.md#variable-name)  <br> |














## Public Functions Documentation


### function SpecialBird [1/3]


```cpp
example::SpecialBird::SpecialBird (
    const std::string & name,
    SpecialBird * mother=nullptr,
    SpecialBird * father=nullptr
) 
```



### function SpecialBird [2/3]


```cpp
example::SpecialBird::SpecialBird (
    const SpecialBird & other
) = delete
```



### function SpecialBird [3/3]


```cpp
example::SpecialBird::SpecialBird (
    SpecialBird && SpecialBird
) noexcept
```



### function do\_something\_special 


```cpp
void example::SpecialBird::do_something_special () 
```



### function operator= 


```cpp
SpecialBird & example::SpecialBird::operator= (
    const SpecialBird & other
) = delete
```



### function operator= 


```cpp
SpecialBird & example::SpecialBird::operator= (
    SpecialBird && other
) noexcept
```



### function swap 


```cpp
void example::SpecialBird::swap (
    SpecialBird & other
) noexcept
```



### function ~SpecialBird 


```cpp
example::SpecialBird::~SpecialBird () = default
```



------------------------------
The documentation for this class was generated from the following file `src/special_bird.h`