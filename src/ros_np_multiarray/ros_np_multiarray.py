import numpy as np
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import (Float32MultiArray, Float64MultiArray,
                          Int8MultiArray, Int16MultiArray,
                          Int32MultiArray, Int64MultiArray,
                          UInt8MultiArray, UInt16MultiArray,
                          UInt32MultiArray, UInt64MultiArray)

def _numpy_to_multiarray(multiarray_type, np_array):
    multiarray = multiarray_type()
    multiarray.layout.dim = [MultiArrayDimension('dim%d' % i,
                                                 np_array.shape[i],
                                                 np_array.shape[i] * np_array.dtype.itemsize) for i in range(np_array.ndim)];
    multiarray.data = np_array.reshape([1, -1])[0].tolist();
    return multiarray

def _multiarray_to_numpy(pytype, dtype, multiarray):
    dims = tuple(map(lambda x: x.size, multiarray.layout.dim))
    return np.array(multiarray.data, dtype=pytype).reshape(dims).astype(dtype)


from functools import partial

to_multiarray_f32 = partial(_numpy_to_multiarray, Float32MultiArray)
to_numpy_f32 = partial(_multiarray_to_numpy, float, np.float32)
to_multiarray_f64 = partial(_numpy_to_multiarray, Float64MultiArray)
to_numpy_f64 = partial(_multiarray_to_numpy, float, np.float64)
to_multiarray_i8 = partial(_numpy_to_multiarray, Int8MultiArray)
to_numpy_i8 = partial(_multiarray_to_numpy, int, np.int8)
to_multiarray_i16 = partial(_numpy_to_multiarray, Int16MultiArray)
to_numpy_i16 = partial(_multiarray_to_numpy, int, np.int16)
to_multiarray_i32 = partial(_numpy_to_multiarray, Int32MultiArray)
to_numpy_i32 = partial(_multiarray_to_numpy, int, np.int32)
to_multiarray_i64 = partial(_numpy_to_multiarray, Int64MultiArray)
to_numpy_i64 = partial(_multiarray_to_numpy, int, np.int64)
to_multiarray_u8 = partial(_numpy_to_multiarray, UInt8MultiArray)
to_numpy_u8 = partial(_multiarray_to_numpy, int, np.uint8)
to_multiarray_u16 = partial(_numpy_to_multiarray, UInt16MultiArray)
to_numpy_u16 = partial(_multiarray_to_numpy, int, np.uint16)
to_multiarray_u32 = partial(_numpy_to_multiarray, UInt32MultiArray)
to_numpy_u32 = partial(_multiarray_to_numpy, int, np.uint32)
to_multiarray_u64 = partial(_numpy_to_multiarray, UInt64MultiArray)
to_numpy_u64 = partial(_multiarray_to_numpy, int, np.uint64)
