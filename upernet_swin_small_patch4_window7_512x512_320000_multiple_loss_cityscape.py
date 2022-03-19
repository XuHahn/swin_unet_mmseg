_base_ = [
    'upernet_swin_small_patch4_window7_512x512_320000_cityscape.py'
]

model = dict(
     decode_head=dict(loss_decode=[dict(type='CrossEntropyLoss', loss_weight=1.0),
             dict(type='DiceLoss', loss_weight=3.0)]),
    auxiliary_head=dict(loss_decode=[dict(type='CrossEntropyLoss', loss_weight=1.0),
                                     dict(type='DiceLoss', loss_weight=3.0)]),
)