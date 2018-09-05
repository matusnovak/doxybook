---
search:
    keywords: ['special_bird.h', 'file']
---

# special\_bird.h File Reference

**[Go to the documentation of this file.](special__bird_8h.md)**
Source: `src/special\_bird.h`

    
    
    
    
    
    
    
    
```cpp
#ifndef EXAMPLE_SPECIAL_BIRD_H
#define EXAMPLE_SPECIAL_BIRD_H

#include "bird.h"

namespace example {
    class SpecialBird: public Bird {
    public:
        SpecialBird(const std::string& name, SpecialBird* mother = nullptr, SpecialBird* father = nullptr);
        SpecialBird(const SpecialBird& other) = delete;
        SpecialBird(SpecialBird&& SpecialBird) noexcept;
        ~SpecialBird() = default;

        void swap(SpecialBird& other) noexcept;
        void do_something_special();

        SpecialBird& operator = (const SpecialBird& other) = delete;
        SpecialBird& operator = (SpecialBird&& other) noexcept;
    };
}

#endif
```


    
  
