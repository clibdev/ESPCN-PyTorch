# Usage

## Download datasets

### Download train dataset

#### T91

- Image format
    - [Google Driver](https://drive.google.com/drive/folders/1PYizfnKq-UtRCDoSy79PGA4FC5HqAqch?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1M0u-BPTdokxO452j7vxW4Q) access: `llot`

- LMDB format (train)
    - [Google Driver](https://drive.google.com/drive/folders/1BPqN08QHk_xFnMJWMS8grfh_vesVs8Jf?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1eqeORnKcTmGatx2kAG92-A) access: `llot`

- LMDB format (valid)
    - [Google Driver](https://drive.google.com/drive/folders/1bYqqKk6NJ9wUfxTH2t_LbdMTB04OUicc?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1W34MeEtLY0m-bOrnaveVmw) access: `llot`

### Download valid dataset

#### Set5

- Image format
    - [Google Driver](https://drive.google.com/file/d/1GtQuoEN78q3AIP8vkh-17X90thYp_FfU/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1dlPcpwRPUBOnxlfW5--S5g) access:`llot`

#### Set14

- Image format
    - [Google Driver](https://drive.google.com/file/d/1CzwwAtLSW9sog3acXj8s7Hg3S7kr2HiZ/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1KBS38UAjM7bJ_e6a54eHaA) access:`llot`

#### BSD200

- Image format
    - [Google Driver](https://drive.google.com/file/d/1cdMYTPr77RdOgyAvJPMQqaJHWrD5ma5n/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1xahPw4dNNc3XspMMOuw1Bw) access:`llot`

## Train dataset struct information

### Image format

```text
- T91
    - ESPCN
        - train
            - ...
        - valid
            - ...
```

### LMDB format

```text
- train_lmdb
    - ESPCN
      - T91_LRbicx3_lmdb
          - data.mdb
          - lock.mdb
      - T91_HR_lmdb
          - data.mdb
          - lock.mdb
- valid_lmdb
    - ESPCN
      - T91_LRbicx3_lmdb
          - data.mdb
          - lock.mdb
      - T91_HR_lmdb
          - data.mdb
          - lock.mdb
```

## Test dataset struct information

### Image format

```text
- Set5
    - GTmod12
        - baby.png
        - bird.png
        - ...
    - LRbicx4
        - baby.png
        - bird.png
        - ...
- Set14
    - GTmod12
        - baboon.png
        - barbara.png
        - ...
    - LRbicx4
        - baboon.png
        - barbara.png
        - ...
```