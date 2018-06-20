---
search:
    keywords: ['example::SpecialBird', 'SpecialBird', 'SpecialBird', 'SpecialBird', '~SpecialBird', 'swap', 'do_something_special', 'operator=', 'operator=', 'Bird', 'Bird', 'Bird', '~Bird', 'swap', 'move', 'make_sound', 'operator=', 'operator=', 'Animal', 'Animal', 'Animal', '~Animal', 'swap', 'get_num_of_limbs', 'get_num_of_eyes', 'has_tail', 'move', 'make_sound', 'get_parents', 'get_name', 'operator=', 'operator=', 'get_num_of_limbs', 'get_num_of_eyes', 'has_tail']
---

# class example::SpecialBird



Inherits the following classes: **[example::Bird](classexample_1_1_bird.md)**

## Public Functions

|Type|Name|
|-----|-----|
||[**SpecialBird**](classexample_1_1_special_bird.md#1a3ac69244c03c5f9d84e86ffccd6e61c7) (const std::string & name, **[SpecialBird](classexample_1_1_special_bird.md)** \* mother = nullptr, **[SpecialBird](classexample_1_1_special_bird.md)** \* father = nullptr) |
||[**SpecialBird**](classexample_1_1_special_bird.md#1a672562a57b5a563b79029838fe3f5788) (const **[SpecialBird](classexample_1_1_special_bird.md)** & other) = delete |
||[**SpecialBird**](classexample_1_1_special_bird.md#1ae31b01cb260d88b3f414b35e1fefad19) (**[SpecialBird](classexample_1_1_special_bird.md)** && SpecialBird) noexcept |
||[**~SpecialBird**](classexample_1_1_special_bird.md#1aa870cc323a87e2cf7df2b6bb44948ccd) () = default |
|void|[**swap**](classexample_1_1_special_bird.md#1a6a33c839c2c4afb1cc6ac95923828f8f) (**[SpecialBird](classexample_1_1_special_bird.md)** & other) noexcept |
|void|[**do\_something\_special**](classexample_1_1_special_bird.md#1af3b69e60317cd3d537a2c0bebfeb4ea2) () |
|**[SpecialBird](classexample_1_1_special_bird.md)** &|[**operator=**](classexample_1_1_special_bird.md#1a842108e610d4378d96d82d5d1d3b2328) (const **[SpecialBird](classexample_1_1_special_bird.md)** & other) = delete |
|**[SpecialBird](classexample_1_1_special_bird.md)** &|[**operator=**](classexample_1_1_special_bird.md#1a8bb5e5570615362ef8f725bc83759c5d) (**[SpecialBird](classexample_1_1_special_bird.md)** && other) noexcept |


#### Public Functions inherited from [example::Bird](classexample_1_1_bird.md)

|Type|Name|
|-----|-----|
||[**Bird**](classexample_1_1_bird.md#1a3e9a914edb8db0a5ecb68f1a8230a671) (const std::string & name, **[Bird](classexample_1_1_bird.md)** \* mother = nullptr, **[Bird](classexample_1_1_bird.md)** \* father = nullptr) |
||[**Bird**](classexample_1_1_bird.md#1a0cca7cb1f27a09fc21f763eb6a5be07f) (const **[Bird](classexample_1_1_bird.md)** & other) = delete |
||[**Bird**](classexample_1_1_bird.md#1a183101969ac7abd593f41a0197bd9c68) (**[Bird](classexample_1_1_bird.md)** && Bird) noexcept |
||[**~Bird**](classexample_1_1_bird.md#1a3209f795942057f0da73316dda7b4c39) () = default |
|void|[**swap**](classexample_1_1_bird.md#1ae9c126dd4739755af505cd5a43c9f1de) (**[Bird](classexample_1_1_bird.md)** & other) noexcept |
|virtual void|[**move**](classexample_1_1_bird.md#1aa3877f1e70aba0d25ef757c248f69d13) () override |
|virtual void|[**make\_sound**](classexample_1_1_bird.md#1ae61379b32b53508e9a2398305826667a) () override |
|**[Bird](classexample_1_1_bird.md)** &|[**operator=**](classexample_1_1_bird.md#1a14c736790bab9fdcad79095ec7e43e83) (const **[Bird](classexample_1_1_bird.md)** & other) = delete |
|**[Bird](classexample_1_1_bird.md)** &|[**operator=**](classexample_1_1_bird.md#1a5f431ca5c2a97f9c62ae688078a5a8a0) (**[Bird](classexample_1_1_bird.md)** && other) noexcept |


#### Public Functions inherited from [example::Animal](classexample_1_1_animal.md)

|Type|Name|
|-----|-----|
||[**Animal**](classexample_1_1_animal.md#1acef1db6802de001a01c403afeca90c86) (**[Type](classexample_1_1_animal.md#1adc9e490a8ea5390fbcaf6ffa24c3ec69)** type, const std::string & name, **[Animal](classexample_1_1_animal.md)** \* mother = nullptr, **[Animal](classexample_1_1_animal.md)** \* father = nullptr) <br>The main constructor. |
||[**Animal**](classexample_1_1_animal.md#1a612d7d2e9631e6f241e871b3785f4cdf) (const **[Animal](classexample_1_1_animal.md)** & other) = delete |
||[**Animal**](classexample_1_1_animal.md#1a29db85a24acf4fd5fb353c871eb086ed) (**[Animal](classexample_1_1_animal.md)** && animal) noexcept |
|virtual |[**~Animal**](classexample_1_1_animal.md#1a7b633f0bc3834108ca024d0c73dc135e) () = default |
|void|[**swap**](classexample_1_1_animal.md#1affec460d5bc2fb8d650fcf5b7b8cf396) (**[Animal](classexample_1_1_animal.md)** & other) noexcept |
|virtual int|[**get\_num\_of\_limbs**](classexample_1_1_animal.md#1a77ea3286e2b43830a5443be76eec4c5f) () override const <br>Returns the number of limbs. |
|virtual int|[**get\_num\_of\_eyes**](classexample_1_1_animal.md#1afc4972484d411d75bdc829be3502bb60) () override const <br>Returns the number of eyes. |
|virtual bool|[**has\_tail**](classexample_1_1_animal.md#1a80c789f01a9e211b821cfa57c27792fa) () override const <br>Returns true if the animal has a tail. |
|Parents|[**get\_parents**](classexample_1_1_animal.md#1a93c61aed16aeb0b52631961e17251b0f) () const |
|const std::string &|[**get\_name**](classexample_1_1_animal.md#1ab4e7a34b9637acc89c55eec9405f1f6e) () const <br>Get the name of the animal. |
|**[Animal](classexample_1_1_animal.md)** &|[**operator=**](classexample_1_1_animal.md#1a021864d5b75ff00550cd4ffe65f4014d) (const **[Animal](classexample_1_1_animal.md)** & other) = delete |
|**[Animal](classexample_1_1_animal.md)** &|[**operator=**](classexample_1_1_animal.md#1a055b1b5d5ffaa302068e7000b1b9f4f7) (**[Animal](classexample_1_1_animal.md)** && other) noexcept |


## Additional Inherited Members

#### Public Types inherited from [example::Animal](classexample_1_1_animal.md)

|Type|Name|
|-----|-----|
|enum|[**Type**](classexample_1_1_animal.md#1adc9e490a8ea5390fbcaf6ffa24c3ec69) { **NONE** = 0, **INSECT** = 1, **AMPHIBIAN** = 2, **BIRD** = 3, **FISH** = 4, **REPTILE** = 5, **MAMMAL** = 6 } <br>The 6 classes of animal kingdom. |
|typedef std::pair< **[Animal](classexample_1_1_animal.md)** \*, **[Animal](classexample_1_1_animal.md)** \* >|[**Parents**](classexample_1_1_animal.md#1a3fc3e692a61c2e21080fef955df099d5)|


#### Protected Attributes inherited from [example::Animal](classexample_1_1_animal.md)

|Type|Name|
|-----|-----|
|**[Animal](classexample_1_1_animal.md)** \*|[**mother**](classexample_1_1_animal.md#1a77ebfd8268da42527748bc17f458c02c)<br>The pointer to the mother. |
|**[Animal](classexample_1_1_animal.md)** \*|[**father**](classexample_1_1_animal.md#1aeaabef8bc7cd869f09db725e0fcc5092)<br>The pointer to the father. |
|std::string|[**name**](classexample_1_1_animal.md#1a9362efc813ef23964f7f6f57640a12e7)|


#### Public Static Functions inherited from [example::Animal](classexample_1_1_animal.md)

|Type|Name|
|-----|-----|
|static **[Animal](classexample_1_1_animal.md)** \*|[**find\_parent\_by\_name**](classexample_1_1_animal.md#1a7ff2cbf990657553d95f6d15fb0f4568) (**[Animal](classexample_1_1_animal.md)** \* child) |
|static **[Animal](classexample_1_1_animal.md)** \*|[**find\_child\_by\_name**](classexample_1_1_animal.md#1a1d509e63586d5fe3edc86d393f88910b) (**[Animal](classexample_1_1_animal.md)** \* parent) |


#### Friends inherited from [example::Animal](classexample_1_1_animal.md)

|Type|Name|
|-----|-----|
|friend void|[**some\_global\_function**](classexample_1_1_animal.md#1aa7ca55f69abe84eade027036327d6f34)<br>Some random global function that modifies **[Animal](classexample_1_1_animal.md)**. |


## Public Functions Documentation

### function <a id="1a3ac69244c03c5f9d84e86ffccd6e61c7" href="#1a3ac69244c03c5f9d84e86ffccd6e61c7">SpecialBird</a>

```cpp
example::SpecialBird::SpecialBird (
    const std::string & name,
    SpecialBird * mother = nullptr,
    SpecialBird * father = nullptr
)
```



### function <a id="1a672562a57b5a563b79029838fe3f5788" href="#1a672562a57b5a563b79029838fe3f5788">SpecialBird</a>

```cpp
example::SpecialBird::SpecialBird (
    const SpecialBird & other
) = delete
```



### function <a id="1ae31b01cb260d88b3f414b35e1fefad19" href="#1ae31b01cb260d88b3f414b35e1fefad19">SpecialBird</a>

```cpp
example::SpecialBird::SpecialBird (
    SpecialBird && SpecialBird
) noexcept
```



### function <a id="1aa870cc323a87e2cf7df2b6bb44948ccd" href="#1aa870cc323a87e2cf7df2b6bb44948ccd">~SpecialBird</a>

```cpp
example::SpecialBird::~SpecialBird () = default
```



### function <a id="1a6a33c839c2c4afb1cc6ac95923828f8f" href="#1a6a33c839c2c4afb1cc6ac95923828f8f">swap</a>

```cpp
void example::SpecialBird::swap (
    SpecialBird & other
) noexcept
```



### function <a id="1af3b69e60317cd3d537a2c0bebfeb4ea2" href="#1af3b69e60317cd3d537a2c0bebfeb4ea2">do\_something\_special</a>

```cpp
void example::SpecialBird::do_something_special ()
```



### function <a id="1a842108e610d4378d96d82d5d1d3b2328" href="#1a842108e610d4378d96d82d5d1d3b2328">operator=</a>

```cpp
SpecialBird & example::SpecialBird::operator= (
    const SpecialBird & other
) = delete
```



### function <a id="1a8bb5e5570615362ef8f725bc83759c5d" href="#1a8bb5e5570615362ef8f725bc83759c5d">operator=</a>

```cpp
SpecialBird & example::SpecialBird::operator= (
    SpecialBird && other
) noexcept
```





----------------------------------------
The documentation for this class was generated from the following file: `src/special\_bird.h`
