
# Class example::SpecialBird


[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **>** [**SpecialBird**](classexample_1_1_special_bird.md)





* `#include <special_bird.h>`



Inherits the following classes: [example::Bird](classexample_1_1_bird.md)










## Public Types inherited from [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
| typedef std::pair&lt; [**Animal**](classexample_1_1_animal.md) \*, [**Animal**](classexample_1_1_animal.md) \* &gt; | [**Parents**](classexample_1_1_animal.md#typedef-parents)  <br> |
| enum  | [**Type**](classexample_1_1_animal.md#enum-type)  <br>_The 6 classes of animal kingdom._  |














## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SpecialBird**](classexample_1_1_special_bird.md#function-specialbird-1-3) (const std::string & name, [**SpecialBird**](classexample_1_1_special_bird.md) \* mother=nullptr, [**SpecialBird**](classexample_1_1_special_bird.md) \* father=nullptr) <br> |
|   | [**SpecialBird**](classexample_1_1_special_bird.md#function-specialbird-2-3) (const [**SpecialBird**](classexample_1_1_special_bird.md) & other) = delete<br> |
|   | [**SpecialBird**](classexample_1_1_special_bird.md#function-specialbird-3-3) ([**SpecialBird**](classexample_1_1_special_bird.md) && SpecialBird) noexcept<br> |
|  void | [**do\_something\_special**](classexample_1_1_special_bird.md#function-do-something-special) () <br> |
|  [**SpecialBird**](classexample_1_1_special_bird.md) & | [**operator=**](classexample_1_1_special_bird.md#function-operator) (const [**SpecialBird**](classexample_1_1_special_bird.md) & other) = delete<br> |
|  [**SpecialBird**](classexample_1_1_special_bird.md) & | [**operator=**](classexample_1_1_special_bird.md#function-operator-2) ([**SpecialBird**](classexample_1_1_special_bird.md) && other) noexcept<br> |
|  void | [**swap**](classexample_1_1_special_bird.md#function-swap) ([**SpecialBird**](classexample_1_1_special_bird.md) & other) noexcept<br> |
|   | [**~SpecialBird**](classexample_1_1_special_bird.md#function-specialbird) () = default<br> |

## Public Functions inherited from [example::Bird](classexample_1_1_bird.md)

| Type | Name |
| ---: | :--- |
|   | [**Bird**](classexample_1_1_bird.md#function-bird-1-3) (const std::string & name, [**Bird**](classexample_1_1_bird.md) \* mother=nullptr, [**Bird**](classexample_1_1_bird.md) \* father=nullptr) <br> |
|   | [**Bird**](classexample_1_1_bird.md#function-bird-2-3) (const [**Bird**](classexample_1_1_bird.md) & other) = delete<br> |
|   | [**Bird**](classexample_1_1_bird.md#function-bird-3-3) ([**Bird**](classexample_1_1_bird.md) && Bird) noexcept<br> |
| virtual void | [**make\_sound**](classexample_1_1_bird.md#function-make-sound) () override<br> |
| virtual void | [**move**](classexample_1_1_bird.md#function-move) () override<br> |
|  [**Bird**](classexample_1_1_bird.md) & | [**operator=**](classexample_1_1_bird.md#function-operator) (const [**Bird**](classexample_1_1_bird.md) & other) = delete<br>_Deleted copy operator._  |
|  [**Bird**](classexample_1_1_bird.md) & | [**operator=**](classexample_1_1_bird.md#function-operator-2) ([**Bird**](classexample_1_1_bird.md) && other) noexcept<br>_Move operator._  |
|  void | [**swap**](classexample_1_1_bird.md#function-swap) ([**Bird**](classexample_1_1_bird.md) & other) noexcept<br> |
|   | [**~Bird**](classexample_1_1_bird.md#function-bird) () = default<br> |

## Public Functions inherited from [example::Animal](classexample_1_1_animal.md)

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



## Public Static Functions inherited from [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
|  [**Animal**](classexample_1_1_animal.md) \* | [**find\_child\_by\_name**](classexample_1_1_animal.md#function-find-child-by-name) ([**Animal**](classexample_1_1_animal.md) \* parent) <br> |
|  [**Animal**](classexample_1_1_animal.md) \* | [**find\_parent\_by\_name**](classexample_1_1_animal.md#function-find-parent-by-name) ([**Animal**](classexample_1_1_animal.md) \* child) <br> |












## Protected Attributes inherited from [example::Animal](classexample_1_1_animal.md)

| Type | Name |
| ---: | :--- |
|  [**Animal**](classexample_1_1_animal.md) \* | [**father**](classexample_1_1_animal.md#variable-father)  <br>_The pointer to the father._  |
|  [**Animal**](classexample_1_1_animal.md) \* | [**mother**](classexample_1_1_animal.md#variable-mother)  <br>_The pointer to the mother._  |
|  std::string | [**name**](classexample_1_1_animal.md#variable-name)  <br> |














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