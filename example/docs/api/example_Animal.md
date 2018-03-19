# Animal class Reference

Base class for all animals from which **[Bird](example_Bird.md)** derives. 
## Public Types

|Type|Name|
|-----|-----|
|enum|[**Type**](#1adc9e490a8ea5390fbcaf6ffa24c3ec69) { **NONE**, **INSECT**, **AMPHIBIAN**, **BIRD**, **FISH**, **REPTILE**, **MAMMAL**,  } |


## Protected Attributes

|Type|Name|
|-----|-----|
|**[Animal](example_Animal.md)** \*|[**mother**](#1a77ebfd8268da42527748bc17f458c02c)|
|**[Animal](example_Animal.md)** \*|[**father**](#1aeaabef8bc7cd869f09db725e0fcc5092)|
|std::string|[**name**](#1a9362efc813ef23964f7f6f57640a12e7)|


## Public Static Functions

|Type|Name|
|-----|-----|
|static **[Animal](example_Animal.md)** \*|[**find\_parent\_by\_name**](#1a7ff2cbf990657553d95f6d15fb0f4568) (**[Animal](example_Animal.md)** \* child)|
|static **[Animal](example_Animal.md)** \*|[**find\_child\_by\_name**](#1a1d509e63586d5fe3edc86d393f88910b) (**[Animal](example_Animal.md)** \* parent)|


## Public Functions

|Type|Name|
|-----|-----|
||[**Animal**](#1acef1db6802de001a01c403afeca90c86) (**[Type](example_Animal.md#b5abe031)** type, const std::string & name, **[Animal](example_Animal.md)** \* mother = nullptr, **[Animal](example_Animal.md)** \* father = nullptr)|
||[**Animal**](#1a612d7d2e9631e6f241e871b3785f4cdf) (const **[Animal](example_Animal.md)** & other)|
||[**Animal**](#1a29db85a24acf4fd5fb353c871eb086ed) (**[Animal](example_Animal.md)** && animal)|
||[**~Animal**](#1a3f655bd72ea96eba32d8332a1b44e70b) ()|
|void|[**swap**](#1affec460d5bc2fb8d650fcf5b7b8cf396) (**[Animal](example_Animal.md)** & other)|
|int|[**get\_num\_of\_limbs**](#1ad6aee00ea8d457d2bd7becbe107f2d9a) ()|
|int|[**get\_num\_of\_eyes**](#1a7558cb43e67bc800961b451dd546db74) ()|
|bool|[**has\_tail**](#1a71d036f82dfe3e7dbefb334a92f91275) ()|
|void|[**move**](#1aaee0d759d18beaca18670d2a794b1445) ()|
|void|[**make\_sound**](#1a6939f9fed1a387b128d3947afc239873) ()|
|std::pair< **[Animal](example_Animal.md)** \*, **[Animal](example_Animal.md)** \* >|[**get\_parents**](#1ab985ec14c22d9f3b80c1a4a911300062) ()|
|const std::string &|[**get\_name**](#1ab4e7a34b9637acc89c55eec9405f1f6e) ()|
|**[Animal](example_Animal.md)** &|[**operator=**](#1a021864d5b75ff00550cd4ffe65f4014d) (const **[Animal](example_Animal.md)** & other)|
|**[Animal](example_Animal.md)** &|[**operator=**](#1a055b1b5d5ffaa302068e7000b1b9f4f7) (**[Animal](example_Animal.md)** && other)|


## Detailed Description

Lorem Ipsum Donor. Some [Random link with **bold** and _italics_](http://github.com) 

**See also**

**[Bird](example_Bird.md)** 



----------------------------------------
The documentation for this class was generated from the following file: [src/animal.h](file.md)
