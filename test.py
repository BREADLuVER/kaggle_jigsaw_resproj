import torch
import collections

print(collections)
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"Devices:")
for i in range(torch.cuda.device_count()):
    print(f"  Device {i}: {torch.cuda.get_device_name(i)}")
