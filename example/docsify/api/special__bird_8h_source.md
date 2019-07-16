
# File special\_bird.h

[**File List**](files.md) **>** [**src**](dir_68267d1309a1af8e8297ef4c3efbcdba.md) **>** [**special\_bird.h**](special__bird_8h.md)

[Go to the documentation of this file.](special__bird_8h.md) 


````cpp
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
````

