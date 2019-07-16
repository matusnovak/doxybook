
# File exception.h

[**File List**](files.md) **>** [**src**](dir_68267d1309a1af8e8297ef4c3efbcdba.md) **>** [**utils**](dir_313caf1132e152dd9b58bea13a4052ca.md) **>** [**exception.h**](exception_8h.md)

[Go to the documentation of this file.](exception_8h.md) 


````cpp
#ifndef EXAMPLE_EXCEPTION_H
#define EXAMPLE_EXCEPTION_H

#include <exception>
#include <string>

namespace example {
    class CustomException : public std::exception {
    public:
        CustomException(const std::string& msg):std::exception(),msg(msg){

        }

        virtual const char* what() const throw() {
            return msg.c_str();
        }

    private:
        std::string msg;
    };

    class NumericException : public std::exception {
    public:
        NumericException(const std::string& msg):std::exception(),msg(msg){

        }

        virtual const char* what() const throw() {
            return msg.c_str();
        }

    private:
        std::string msg;
    };
}

#endif
````

