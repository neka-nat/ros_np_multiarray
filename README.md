# ros_np_multiarray

Convert between numpy ndarray and ros multiarray message.

## Usage

This is a simple example.

```py
import ros_np_multiarray as rnm
import numpy as np

print(rnm.to_multiarray_f32(np.array([[[1.0, 2.0], [3.0, 4.0]]], dtype=np.float32)))
```

We get the data converted to 'std_msgs/Float32MultiArray'.

```
layout: 
  dim: 
    - 
      label: "dim0"
      size: 1
      stride: 4
    - 
      label: "dim1"
      size: 2
      stride: 8
    - 
      label: "dim2"
      size: 2
      stride: 8
  data_offset: 0
data: [1.0, 2.0, 3.0, 4.0]
```