# Fork of [Lornatang/ESPCN-PyTorch](https://github.com/Lornatang/ESPCN-PyTorch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/ESPCN-PyTorch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name     | Scale | Set5 (PSNR) | Set14 (PSNR) | Link                                                                                                                                                                                                             |
|----------|-------|-------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ESPCN_x2 | 2     | 36.64       | 32.35        | [PyTorch](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/ESPCN_x2-T91-da809cd7.pth.tar), [ONNX](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/ESPCN_x2-T91-da809cd7.onnx) |
| ESPCN_x3 | 3     | 32.55       | 29.20        | [PyTorch](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/ESPCN_x3-T91-647e91f3.pth.tar), [ONNX](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/ESPCN_x3-T91-647e91f3.onnx) |
| ESPCN_x4 | 4     | 30.26       | 27.41        | [PyTorch](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/ESPCN_x4-T91-64bf5ee4.pth.tar), [ONNX](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/ESPCN_x4-T91-64bf5ee4.onnx) |

# Inference

```shell
python inference.py --model_arch_name espcn_x2 --upscale_factor 2 --model_weights_path results/pretrained_models/ESPCN_x2-T91-da809cd7.pth.tar --inputs_path figure/comic.png --output_path figure/sr_comic_x2.png
python inference.py --model_arch_name espcn_x3 --upscale_factor 3 --model_weights_path results/pretrained_models/ESPCN_x3-T91-647e91f3.pth.tar --inputs_path figure/comic.png --output_path figure/sr_comic_x3.png
python inference.py --model_arch_name espcn_x4 --upscale_factor 4 --model_weights_path results/pretrained_models/ESPCN_x4-T91-64bf5ee4.pth.tar --inputs_path figure/comic.png --output_path figure/sr_comic_x4.png
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --model_arch_name espcn_x2 --model_weights_path results/pretrained_models/ESPCN_x2-T91-da809cd7.pth.tar
python export.py --model_arch_name espcn_x3 --model_weights_path results/pretrained_models/ESPCN_x3-T91-647e91f3.pth.tar
python export.py --model_arch_name espcn_x4 --model_weights_path results/pretrained_models/ESPCN_x4-T91-64bf5ee4.pth.tar
```
