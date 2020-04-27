from operator import mul
from functools import partial


dir(mul)
double = partial(mul, 2)

print(double(5))