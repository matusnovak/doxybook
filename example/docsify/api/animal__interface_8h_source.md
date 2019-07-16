
# File animal\_interface.h

[**File List**](files.md) **>** [**src**](dir_68267d1309a1af8e8297ef4c3efbcdba.md) **>** [**animal\_interface.h**](animal__interface_8h.md)

[Go to the documentation of this file.](animal__interface_8h.md) 


````cpp
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
````

