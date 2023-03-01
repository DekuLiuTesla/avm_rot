# AVM 

## 环境

### 最佳实践（推荐，已测试可行）

1. 第一步 使用 MIM 安装 MMCV
```bash
pip install -U openmim
mim install mmcv-full
```

2. 第二步 安装 MMRotate
```bash
pip install mmrotate
```

3. 第三步下载配置文件(可选)

```bash
mim download mmrotate --config oriented_rcnn_r50_fpn_1x_dota_le90 --dest .
```

## 训练

在当前目录下建立软连接
```bash
ln -s AVM_DATA_ROOT avm
```

其中AVM原始数据集目录需调整为如下结构
```python
avm
 │
 ├─ images
 │   ├─ b2_left
 │   │   └─ avm
 │   │       ├─ 0.jpg
 │   │       └─ 20.jpg
 │   │       ... 
 │   ├─ b2_right
 │   ├─ b2_to_b3
 │   └─ b3_to_b2
 │   
 └─ det_annotations
     ├─ b2_left
     │   ├─ 0.json
     │   └─ 20.json
     │   ... 
     ├─ b2_right
     ├─ b2_to_b3
     └─ b3_to_b2
```

将原数据集格式转换为DOTA格式
```python
python create_data.py --avm-dir ./data/avm --output-dir ./data/avm_dota_format
```

转换过后文件结构如下：
```python
avm_cs_format
 │
 └─ train
     ├─ annfiles
     │   ├─ b2_left_0.txt
     │   └─ b2_left_1000.txt
     │       ... 
     └─ images
         ├─ b2_left_0.png
         └─ b2_left_1000.png
         ... 
 
```


## 推理

```bash
python inference.py --config=configs/rotated_retinanet_obb_r50_fpn_1x_avm_le90.py --checkpoint=checkpoints/epoch_3.pth --image_path=demo.png
```
结果将保存为bin文件，读取后reshape成(-1, 7)，则7个维度分别对应 (x, y, w, h, theta, score, label)。