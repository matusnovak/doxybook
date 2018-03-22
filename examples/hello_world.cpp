#include "bird.h"

auto mother = example::Bird("Mom");
auto father = example::Bird("Dad");
auto child = example::Bird("Junior", &mother, &father);
