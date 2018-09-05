---
search:
    keywords: ['example::SpecialBird', 'SpecialBird', 'SpecialBird', 'SpecialBird', '~SpecialBird', 'swap', 'do_something_special', 'operator=', 'operator=']
---

# class example::SpecialBird

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**SpecialBird**](classexample_1_1_special_bird.md)




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


## Public Functions Documentation

### function <a id="1a3ac69244c03c5f9d84e86ffccd6e61c7" href="#1a3ac69244c03c5f9d84e86ffccd6e61c7">SpecialBird (1/3)</a>

```cpp
example::SpecialBird::SpecialBird (
    const std::string & name,
    SpecialBird * mother = nullptr,
    SpecialBird * father = nullptr
)
```



### function <a id="1a672562a57b5a563b79029838fe3f5788" href="#1a672562a57b5a563b79029838fe3f5788">SpecialBird (2/3)</a>

```cpp
example::SpecialBird::SpecialBird (
    const SpecialBird & other
) = delete
```



### function <a id="1ae31b01cb260d88b3f414b35e1fefad19" href="#1ae31b01cb260d88b3f414b35e1fefad19">SpecialBird (3/3)</a>

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



### function <a id="1a842108e610d4378d96d82d5d1d3b2328" href="#1a842108e610d4378d96d82d5d1d3b2328">operator= (1/2)</a>

```cpp
SpecialBird & example::SpecialBird::operator= (
    const SpecialBird & other
) = delete
```



### function <a id="1a8bb5e5570615362ef8f725bc83759c5d" href="#1a8bb5e5570615362ef8f725bc83759c5d">operator= (2/2)</a>

```cpp
SpecialBird & example::SpecialBird::operator= (
    SpecialBird && other
) noexcept
```





----------------------------------------
The documentation for this class was generated from the following file: `src/special\_bird.h`
