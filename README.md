# Fork of [Lornatang/ESPCN-PyTorch](https://github.com/Lornatang/ESPCN-PyTorch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.8. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/ESPCN-PyTorch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* The following deprecations, warnings and errors has been fixed:
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.
  * FutureWarning: 'torch.cuda.amp.GradScaler(args...)' is deprecated.
  * AttributeError: 'Namespace' object has no attribute 'gt_image_size'.
  * WARN imwrite_ Unsupported depth image for selected encoder is fallbacked to CV_8U.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Name     | Model Size (MB) | Link                                                                                                                                                                                   | SHA-256                                                                                                                              |
|----------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ESPCN_x2 | 0.1<br>0.1      | [PyTorch](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/espcn-x2.pth.tar), [ONNX](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/espcn-x2.onnx) | 67321a870da341c15a92f5dcea31bcb21b7fa30165b0ac445662d4364048595b<br>6c806349be7f963f3d0895050a771a5de15e9950361e2a2f92624e4b1f675044 |
| ESPCN_x3 | 0.1<br>0.1      | [PyTorch](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/espcn-x3.pth.tar), [ONNX](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/espcn-x3.onnx) | 242ab640f79fa1e005f5d495debf6c1e385209c8b81f14f5692ba7ed51ec2f5d<br>77aea5de0ba9628566ef9519de06a18ff5c25b32b0743d3e49a808c539c5445f |
| ESPCN_x4 | 0.1<br>0.1      | [PyTorch](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/espcn-x4.pth.tar), [ONNX](https://github.com/clibdev/ESPCN-PyTorch/releases/latest/download/espcn-x4.onnx) | 756564c1b4103cad1170479bbce665b2b58163444d5170dcc1db37ba143694f8<br>2b421d032afd5737c8cc0f1145214d78c35dbc46e3c7cb45913da80304b8aa8e |

* Evaluation results:

| Name     | Scale | Set5 (PSNR) | Set14 (PSNR) |
|----------|-------|-------------|--------------|
| ESPCN_x2 | 2     | 36.64       | 32.35        |
| ESPCN_x3 | 3     | 32.55       | 29.20        |
| ESPCN_x4 | 4     | 30.26       | 27.41        |

# Inference

```shell
python inference.py --model_arch_name espcn_x2 --upscale_factor 2 --model_weights_path espcn-x2.pth.tar --inputs_path figure/comic.png --output_path figure/sr_comic_x2.png
python inference.py --model_arch_name espcn_x3 --upscale_factor 3 --model_weights_path espcn-x3.pth.tar --inputs_path figure/comic.png --output_path figure/sr_comic_x3.png
python inference.py --model_arch_name espcn_x4 --upscale_factor 4 --model_weights_path espcn-x4.pth.tar --inputs_path figure/comic.png --output_path figure/sr_comic_x4.png
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --model_arch_name espcn_x2 --model_weights_path espcn-x2.pth.tar
python export.py --model_arch_name espcn_x3 --model_weights_path espcn-x3.pth.tar
python export.py --model_arch_name espcn_x4 --model_weights_path espcn-x4.pth.tar
```
