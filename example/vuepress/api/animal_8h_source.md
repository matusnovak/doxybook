---
title: animal.h File Reference
meta:
  - name: keywords
    content: animal.h file
---

# animal.h File Reference

**[Go to the documentation of this file.](animal_8h.md)**
Source: `src/animal.h`

    
    
    
    
    
    
    
    
    
    
      
    
    
    
```cpp
#ifndef EXAMPLE_ANIMAL_H
#define EXAMPLE_ANIMAL_H

#include <functional>
#include "animal_interface.h"

namespace example {
    class Animal: public AnimalInterface {
    public:
        enum Type {
            NONE = 0,
            INSECT = 1,
            AMPHIBIAN = 2,
            BIRD = 3,
            FISH = 4,
            REPTILE = 5,
            MAMMAL = 6
        };

        typedef std::pair<Animal*, Animal*> Parents;
        struct Result {
            const Type type = Type::NONE;
            const std::string name;
            const Animal* mother = nullptr;
            const Animal* father = nullptr;
        };

        static Animal* find_parent_by_name(Animal* child);
        static Animal* find_child_by_name(Animal* parent);

        Animal(Type type, const std::string& name, Animal* mother = nullptr, Animal* father = nullptr);
        Animal(const Animal& other) = delete;
        Animal(Animal&& animal) noexcept;
        virtual ~Animal() = default;

        operator bool() const;

        void swap(Animal& other) noexcept;

        int get_num_of_limbs() const override;

        int get_num_of_eyes() const override;

        bool has_tail() const override;

        virtual void move();
        virtual void make_sound() = 0;

        inline Parents get_parents() const {
            return Parents(mother, father);
        }

        inline const std::string& get_name() const {
            return name;
        }
        Animal& operator = (const Animal& other) = delete;
        Animal& operator = (Animal&& other) noexcept;

        friend void some_global_function(Animal* animal);

    protected:
        Animal* mother;
        Animal* father;
        std::string name;
    };

    void some_namespace_function(Animal* animal);
    typedef std::function<void*(Animal*)> Callback;
    enum class CallbackType {
        NONE = 0,
        EAT,
        SLEEP,
        ATTACK
    };
}

extern void some_global_function(example::Animal* animal);

#endif
```


    
  
