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
}

#endif