---
search:
    keywords: ['animal_interface.h', 'file']
---

# animal\_interface.h File Reference

**[Go to the documentation of this file.](animal__interface_8h.md)**
Source: `src/animal\_interface.h`

    
    
    
    
    
    
    
    
    
    
```cpp
#ifndef EXAMPLE_ANIMAL_INTERFACE_H
#define EXAMPLE_ANIMAL_INTERFACE_H

#include <string>

namespace example {
    class AnimalInterface {
    public:
        virtual int get_num_of_limbs() const = 0;

        virtual int get_num_of_eyes() const = 0;

        virtual bool has_tail() const = 0;
    };
}

#endif
```


    
  
