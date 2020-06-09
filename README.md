# libplf

library for multidimensional piecewise linear function

# usage

```python
from libplf import *

f = plf(
    piece(
        point(
            vector(1, 1),
            vector(8),
        ),
        point(
            vector(2, 3),
            vector(5),
        ),
        point(
            vector(3, 2),
            vector(5),
        ),
    ),
)

f(1.5, 1.5)
```