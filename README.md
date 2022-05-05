# Swin-S Unet with multiple Losses in Cityscapes Dataset 🚀️

### * [效果预览 🎉️](demo/)
<img src="demo/pred_img_2.png" width="450px" height="250px"> <img src="demo/pred_img_3.png" width="450px" height="250px">
<img src="demo/pred_img.png" width="450px" height="250px"> <img src="demo/pred_img_1.png" width="450px" height="250px">

### * [环境配置 🎉️](docs/get_started.md)

* 环境安装

  ```bash
  pip install requirements.txt
  ```

  或者

  ```bash
  conda create --name <env> --file requirements.txt
  ```

### * [数据集下载与预处理 🎉️](docs/dataset_prepare.md)

1. 首先创建数据集目录文件夹与设置目录文件

```shell
export PROJECT=$(pwd)
mkdir "$PROJECT/data"
mkdir "$PROJECT/data/cityscapes"
```

2. Cityscapes数据集可以在 [这里](https://www.cityscapes-dataset.com/downloads/) 下载。本项目使用 [训练集](https://www.cityscapes-dataset.com/file-handling/?packageID=3) 和 [标签](https://www.cityscapes-dataset.com/file-handling/?packageID=1)
3. 下载完成后解压数据集

```shell
unzip gtFine_trainvaltest.zip "gtFine" -d $PROJECT/data/cityscapes
unzip leftImg8bit_trainvaltest.zip "leftImg8bit" -d $PROJECT/data/cityscapes
```

4. 在数据集下载完成后基于[cityscapesscripts](cityscapesscripts)去选择所需训练的类别，在[这里](cityscapesscripts/helpers/labels.py)设置（本项目使用19类
5. 设置完训练类别后，运行

```shell
export CITYSCAPES_DATASET=data/cityscapes/
python cityscapesscripts/preparation/createTrainIdInstanceImgs.py
```

4. 使用此 [脚本](https://github.com/open-mmlab/mmsegmentation/blob/master/tools/convert_datasets/cityscapes.py) ,去生成 `**labelTrainIds.png`。

```shell
# --nproc 8 意味着有 8 个进程用来转换，它也可以被忽略。
python tools/convert_datasets/cityscapes.py data/cityscapes --nproc 8
```

### * [设计网络 🎉️](docs/config_model.md)

* 本项目使用的是Swin-Unet
  * 单损失函数配置在 [这里](upernet_swin_small_patch4_window7_512x512_320000_cityscape.py)
  * 多损失函数配置在 [这里](upernet_swin_small_patch4_window7_512x512_320000_multiple_loss_cityscape.py)

### * [开始训练 🎉️](docs/train.md)

* 预训练模型在 [这里](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth) 下载
* ```shell
  cd $PROJECT/
  mkdir pretrain
  wget https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth
  python tools/model_converters/swin2mmseg.py swin_small_patch4_window7_224.pth pretrain/swin_small_patch4_window7_224.pth
  rm swin_small_patch4_window7_224.pth
  python tools/train.py upernet_swin_small_patch4_window7_512x512_320000_multiple_loss_cityscape.py --gpu-ids 0
  ```

### * [验证 🎉️](docs/inference.md)

* ```shell
  python tools/test.py upernet_swin_small_patch4_window7_512x512_320000_multiple_loss_cityscape.py  work_dirs/iter_192000.pth --eval mIoU cityscapes
  ```

### * [其他工具 🎉️](docs/useful_tools.md)
