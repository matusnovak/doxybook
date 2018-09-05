---
title: bird.h File Reference
meta:
  - name: keywords
    content: bird.h file
---

# bird.h File Reference

**[Go to the documentation of this file.](bird_8h.md)**
Source: `src/bird.h`

    
    
    
    
    
    
    
    
    
    
    
```cpp
#ifndef EXAMPLE_BIRD_H
#define EXAMPLE_BIRD_H

#include "animal.h"

namespace example {
    class Bird: public Animal {
    public:
        Bird(const std::string& name, Bird* mother = nullptr, Bird* father = nullptr);
        Bird(const Bird& other) = delete;
        Bird(Bird&& Bird) noexcept;
        ~Bird() = default;

        void swap(Bird& other) noexcept;

        void move() override;
        void make_sound() override;
        Bird& operator = (const Bird& other) = delete;
        Bird& operator = (Bird&& other) noexcept;
    };
}

#endif
```


    
  
