---
search:
    keywords: ['exception.h', 'file']
---

# exception.h File Reference

**[Go to the documentation of this file.](exception_8h.md)**
Source: `src/utils/exception.h`

    
    
    
    
    
    
    
    
    
    
    
```cpp
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
```


    
  
