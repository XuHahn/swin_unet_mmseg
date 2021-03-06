# Swin-S Unet with multiple Losses in Cityscapes Dataset ðï¸


### * å¦ææ¨ä½¿ç¨äºæ¬ä»£ç ï¼å¯ä»¥ç¹å»ðæForkç»äºæé¼å±!è°¢è°¢ï¼ð
* ![Github stars](https://img.shields.io/github/stars/XuHahn/swin_unet_mmseg.svg) ![Github forks](https://img.shields.io/github/forks/XuHahn/swin_unet_mmseg.svg)


### * [ææé¢è§ ðï¸](demo/)
<img src="demo/pred_img_2.png" width="350px" height="200px"> <img src="demo/pred_img_3.png" width="350px" height="200px">
<img src="demo/pred_img.png" width="350px" height="200px"> <img src="demo/pred_img_1.png" width="350px" height="200px">




### * [ç¯å¢éç½® ðï¸](docs/get_started.md)

* ç¯å¢å®è£

  ```bash
  pip install requirements.txt
  
  ```

  æè

  ```bash
  conda create --name <env> --file requirements.txt
  ```
  
   æè

  ```bash
  sh environments.sh
  ```
  

### * [æ°æ®éä¸è½½ä¸é¢å¤ç ðï¸](docs/dataset_prepare.md)

1. é¦ååå»ºæ°æ®éç®å½æä»¶å¤¹ä¸è®¾ç½®ç®å½æä»¶

```shell
export PROJECT=$(pwd)
mkdir "$PROJECT/data"
mkdir "$PROJECT/data/cityscapes"
```

2. Cityscapesæ°æ®éå¯ä»¥å¨ [è¿é](https://www.cityscapes-dataset.com/downloads/) ä¸è½½ãæ¬é¡¹ç®ä½¿ç¨ç [è®­ç»é](https://www.cityscapes-dataset.com/file-handling/?packageID=3) å [æ ç­¾](https://www.cityscapes-dataset.com/file-handling/?packageID=1)
3. ä¸è½½å®æåè§£åæ°æ®é

```shell
unzip gtFine_trainvaltest.zip "gtFine" -d $PROJECT/data/cityscapes
unzip leftImg8bit_trainvaltest.zip "leftImg8bit" -d $PROJECT/data/cityscapes
```

4. å¨æ°æ®éä¸è½½å®æååºäº[cityscapesscripts](cityscapesscripts)å»éæ©æéè®­ç»çç±»å«ï¼å¨[è¿é](cityscapesscripts/helpers/labels.py)è®¾ç½®ï¼æ¬é¡¹ç®ä½¿ç¨19ç±»
5. è®¾ç½®å®è®­ç»ç±»å«åï¼è¿è¡

```shell
export CITYSCAPES_DATASET=data/cityscapes/
python cityscapesscripts/preparation/createTrainIdInstanceImgs.py
```

4. ä½¿ç¨æ­¤ [èæ¬](https://github.com/open-mmlab/mmsegmentation/blob/master/tools/convert_datasets/cityscapes.py) ,å»çæ `**labelTrainIds.png`ã

```shell
# --nproc 8 æå³çæ 8 ä¸ªè¿ç¨ç¨æ¥è½¬æ¢ï¼å®ä¹å¯ä»¥è¢«å¿½ç¥ã
python tools/convert_datasets/cityscapes.py data/cityscapes --nproc 8
```

### * [è®¾è®¡ç½ç» ðï¸](docs/config_model.md)

* æ¬é¡¹ç®ä½¿ç¨çæ¯Swin-Unet
  * åæå¤±å½æ°éç½®å¨ [è¿é](upernet_swin_small_patch4_window7_512x512_320000_cityscape.py)
  * å¤æå¤±å½æ°éç½®å¨ [è¿é](upernet_swin_small_patch4_window7_512x512_320000_multiple_loss_cityscape.py)

### * [å¼å§è®­ç» ðï¸](docs/train.md)

* é¢è®­ç»æ¨¡åå¨ [è¿é](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth) ä¸è½½
* ```shell
  cd $PROJECT/
  mkdir pretrain
  wget https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth
  python tools/model_converters/swin2mmseg.py swin_small_patch4_window7_224.pth pretrain/swin_small_patch4_window7_224.pth
  rm swin_small_patch4_window7_224.pth
  python tools/train.py upernet_swin_small_patch4_window7_512x512_320000_multiple_loss_cityscape.py --gpu-ids 0
  ```
  
### * [æéä¸è½½ ðï¸](https://github.com/XuHahn/swin_unet_mmseg/releases/)

#### * iter192000:
  | iter | mIoU | mAcc | ä¸è½½ |
  | ----- | ----- | ----- | -----|
  | 192000 | 80.34 | 86.99 | [â¬](https://github.com/XuHahn/swin_unet_mmseg/releases/tag/iter192000-miou80.34) |

  |     Class     |  IoU  |  Acc  |     Class     |  IoU  |  Acc  |
  |---------------|-------|-------|---------------|-------|-------|
  |      road     | 98.23 | 99.35 |      sky      | 95.34 | 98.45 |
  |    sidewalk   | 85.71 | 91.15 |     person    | 83.96 | 90.81 |
  |    building   | 92.92 | 96.99 |     rider     | 66.24 | 79.68 |
  |      wall     | 61.53 | 68.19 |      car      | 95.67 | 97.72 |
  |     fence     | 61.19 |  69.6 |     truck     | 84.17 | 89.94 |
  |      pole     | 66.97 | 77.55 |      bus      | 91.95 | 94.47 |
  | traffic light | 73.88 | 83.43 |     train     | 84.71 | 89.64 |
  |  traffic sign | 80.71 | 85.94 |   motorcycle  | 69.27 | 77.15 |
  |   vegetation  | 92.86 | 96.61 |    bicycle    | 74.55 | 91.92 |
  |    terrain    | 66.61 | 74.14 |    average    | 80.34 | 86.99 |


### * [éªè¯ ðï¸](docs/inference.md)

* ```shell
  python tools/test.py upernet_swin_small_patch4_window7_512x512_320000_multiple_loss_cityscape.py  work_dirs/iter_192000.pth --eval mIoU cityscapes
  ```

### * [å¶ä»å·¥å· ðï¸](docs/useful_tools.md)
