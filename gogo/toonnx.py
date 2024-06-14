import torch

# Load your model
path='C:/Users/Lenovo/yolov5/yolov5s.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path)  # path to your .pt file
model.eval()

# Input to the model
dummy_input = torch.randn(1, 3, 640, 640)  # adjust according to your model's input size

# Export the model
torch.onnx.export(model, dummy_input, "model.onnx", opset_version=11, export_params=True, do_constant_folding=True, input_names = ['input'], output_names = ['output'])
