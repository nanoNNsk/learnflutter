import onnx
from onnx_tf.backend import prepare

# Load the ONNX model
onnx_model = onnx.load('model.onnx')

# Convert to TensorFlow
tf_rep = prepare(onnx_model)
tf_rep.export_graph('model.pb')
