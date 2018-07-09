# ros_np_multiarray

## Usage

```
import ros_np_multiarray as rnm
import numpy as np

print(rnm.to_multiarray_f32(np.array([1.0, 2.0], dtype=np.float32)))
```

```
layout: 
  dim: 
    - 
      label: "dim0"
      size: 2
      stride: 8
  data_offset: 0
data: [1.0, 2.0]
```