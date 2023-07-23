import argparse
from pathlib import Path
import model
import torch
import os
from utils import load_state_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_arch_name', type=str, default='espcn_x4')
    parser.add_argument('--model_weights_path',
                        type=str,
                        default='./results/pretrained_models/ESPCN_x4-T91-64bf5ee4.pth.tar',
                        help='Model weights file path.')
    parser.add_argument('--device_type', type=str, default='cpu', choices=['cpu', 'cuda'])
    args = parser.parse_args()

    device = torch.device(args.device_type)

    sr_model = model.__dict__[args.model_arch_name](in_channels=1, out_channels=1, channels=64)
    sr_model = sr_model.to(device)
    sr_model = load_state_dict(sr_model, args.model_weights_path)
    sr_model.eval()

    model_path = Path(args.model_weights_path).with_suffix('')
    model_path = os.path.join(model_path.parent, model_path.stem + '.onnx')

    dummy_input = torch.randn(1, 1, 224, 224).to(device)
    torch.onnx.export(
        sr_model,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {2: '?', 3: '?'}, 'output': {2: '?', 3: '?'}},
        opset_version=17
    )
