---
search:
    keywords: ['example::Bird', 'Bird', 'Bird', 'Bird', '~Bird', 'swap', 'move', 'make_sound', 'operator=', 'operator=']
---

# class example::Bird

[**Class List**](annotated.md) **>** [**example**](namespaceexample.md) **::** [**Bird**](classexample_1_1_bird.md)




Inherits the following classes: **[example::Animal](classexample_1_1_animal.md)**



Inherited by the following classes: **[example::SpecialBird](classexample_1_1_special_bird.md)**

## Public Functions

|Type|Name|
|-----|-----|
||[**Bird**](classexample_1_1_bird.md#1a3e9a914edb8db0a5ecb68f1a8230a671) (const std::string & name, **[Bird](classexample_1_1_bird.md)** \* mother = nullptr, **[Bird](classexample_1_1_bird.md)** \* father = nullptr) |
||[**Bird**](classexample_1_1_bird.md#1a0cca7cb1f27a09fc21f763eb6a5be07f) (const **[Bird](classexample_1_1_bird.md)** & other) = delete |
||[**Bird**](classexample_1_1_bird.md#1a183101969ac7abd593f41a0197bd9c68) (**[Bird](classexample_1_1_bird.md)** && Bird) noexcept |
||[**~Bird**](classexample_1_1_bird.md#1a3209f795942057f0da73316dda7b4c39) () = default |
|void|[**swap**](classexample_1_1_bird.md#1ae9c126dd4739755af505cd5a43c9f1de) (**[Bird](classexample_1_1_bird.md)** & other) noexcept |
|virtual void|[**move**](classexample_1_1_bird.md#1aa3877f1e70aba0d25ef757c248f69d13) () override |
|virtual void|[**make\_sound**](classexample_1_1_bird.md#1ae61379b32b53508e9a2398305826667a) () override |
|**[Bird](classexample_1_1_bird.md)** &|[**operator=**](classexample_1_1_bird.md#1a14c736790bab9fdcad79095ec7e43e83) (const **[Bird](classexample_1_1_bird.md)** & other) = delete <br>Deleted copy operator. |
|**[Bird](classexample_1_1_bird.md)** &|[**operator=**](classexample_1_1_bird.md#1a5f431ca5c2a97f9c62ae688078a5a8a0) (**[Bird](classexample_1_1_bird.md)** && other) noexcept <br>Move operator. |


## Public Functions Documentation

### function <a id="1a3e9a914edb8db0a5ecb68f1a8230a671" href="#1a3e9a914edb8db0a5ecb68f1a8230a671">Bird (1/3)</a>

```cpp
example::Bird::Bird (
    const std::string & name,
    Bird * mother = nullptr,
    Bird * father = nullptr
)
```



### function <a id="1a0cca7cb1f27a09fc21f763eb6a5be07f" href="#1a0cca7cb1f27a09fc21f763eb6a5be07f">Bird (2/3)</a>

```cpp
example::Bird::Bird (
    const Bird & other
) = delete
```



### function <a id="1a183101969ac7abd593f41a0197bd9c68" href="#1a183101969ac7abd593f41a0197bd9c68">Bird (3/3)</a>

```cpp
example::Bird::Bird (
    Bird && Bird
) noexcept
```



### function <a id="1a3209f795942057f0da73316dda7b4c39" href="#1a3209f795942057f0da73316dda7b4c39">~Bird</a>

```cpp
example::Bird::~Bird () = default
```



### function <a id="1ae9c126dd4739755af505cd5a43c9f1de" href="#1ae9c126dd4739755af505cd5a43c9f1de">swap</a>

```cpp
void example::Bird::swap (
    Bird & other
) noexcept
```



### function <a id="1aa3877f1e70aba0d25ef757c248f69d13" href="#1aa3877f1e70aba0d25ef757c248f69d13">move</a>

```cpp
virtual void example::Bird::move ()
```



Implements **[Animal::move](classexample_1_1_animal.md#1aaee0d759d18beaca18670d2a794b1445)**


### function <a id="1ae61379b32b53508e9a2398305826667a" href="#1ae61379b32b53508e9a2398305826667a">make\_sound</a>

```cpp
virtual void example::Bird::make_sound ()
```



Implements **[Animal::make\_sound](classexample_1_1_animal.md#1a6939f9fed1a387b128d3947afc239873)**


### function <a id="1a14c736790bab9fdcad79095ec7e43e83" href="#1a14c736790bab9fdcad79095ec7e43e83">operator= (1/2)</a>

```cpp
Bird & example::Bird::operator= (
    const Bird & other
) = delete
```

Deleted copy operator. 


### function <a id="1a5f431ca5c2a97f9c62ae688078a5a8a0" href="#1a5f431ca5c2a97f9c62ae688078a5a8a0">operator= (2/2)</a>

```cpp
Bird & example::Bird::operator= (
    Bird && other
) noexcept
```

Move operator. 




----------------------------------------
The documentation for this class was generated from the following file: `src/bird.h`
