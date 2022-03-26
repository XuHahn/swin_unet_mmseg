conda create -n swin python=3.8
conda activate swin
conda install pytorch=1.11.0 torchvision cudatoolkit=11.3 -c pytorch
pip install mmcv-full==1.4.7 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html
pip install mmsegmentation \
            seaborn\
            onnxruntime-tools\
            tensorboardX

