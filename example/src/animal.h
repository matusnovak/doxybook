#ifndef EXAMPLE_ANIMAL_H
#define EXAMPLE_ANIMAL_H

#include <string>

namespace example {
    class Animal {
    public:
        /*!
         * @brief The 6 classes of animal kingdom
         */
        enum Type {
            NONE,
            INSECT,
            AMPHIBIAN,
            BIRD,
            FISH,
            REPTILE,
            MAMMAL
        };

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
        ~Animal() = default;

        void swap(Animal& other) noexcept;

        /*!
         * @brief Returns the number of limbs
         * @see get_num_of_eyes
         */
        int get_num_of_limbs() const;

        /*!
         * @brief Returns the number of eyes
         * @see get_num_of_limbs
         */
        int get_num_of_eyes() const;

        /*!
         * @brief Returns true if the animal has a tail
         * @see get_num_of_limbs
         */
        bool has_tail() const;

        virtual void move();
        virtual void make_sound() = 0;

        inline std::pair<Animal*, Animal*> get_parents() const {
            return std::pair<Animal*, Animal*>(mother, father);
        }

        inline const std::string& get_name() const {
            return name;
        }

        Animal& operator = (const Animal& other) = delete;
        Animal& operator = (Animal&& other) noexcept;

    protected:
        Animal* mother;
        Animal* father;
        std::string name;
    };

    /*!
     * @brief Some random global function that modifies Animal
     * @see Animal
     * @param animal The pointer to the animal instance
     */
    void some_global_function(Animal* animal);
}

#endif