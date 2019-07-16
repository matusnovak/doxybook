
# File bird.h

[**File List**](files.md) **>** [**src**](dir_68267d1309a1af8e8297ef4c3efbcdba.md) **>** [**bird.h**](bird_8h.md)

[Go to the documentation of this file.](bird_8h.md) 


````cpp
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
````

