# Jinzhan-Cafeteria-AI
## Introduction
This project is the final project of the course, "Introduction to Machine Learning", in National Tsinghua University.
We modify YOLOv7 to detect the food image from the cafeteria in our campus, "Jinzhan", and also use regression model to predict the price based on the detection result from YOLOv7 model, since the price is not only based on number of each food classes but also its combination and food amount.
For more detail, we encourage you to refer to Campus Cafeteria Recognition and Billing System - Based on YOLOv7 and Regression Models.pdf

credit: https://github.com/WongKinYiu/yolov7
## Environment Setup
Our system is built upon the YOLOv7 architecture with principal alterations aimed at enhancing its capability to handle regression models. These modifications are summarized as follows:

A new directory for regression models has been integrated into the existing model structure for dedicated regression model training.
Adjustments to model/detect.py allow for the visualization of price information directly on the images.
Environment Setup
To utilize our custom implementation, you may set up your environment using one of the two following methods:

Method 1: Clone Our Repository
bash
Copy code

```shell
git clone https://github.com/lazumo/Jinzhan-Cafeteria-AI
pip install -r /path/to/requirements.txt
```

Method 2: Modify Original YOLOv7 Implementation
Download the original YOLOv7 implementation from its official webpage.
Replace the original detect.py with our modified version.
Add the regression model folder to the corresponding location within the YOLOv7 directory structure.

## Performance
### Yolov7 Model
### Regression Model
|   model  | exact accuracy |+-5 dollars accuracy |
| -------- | ------- |------- |
| Regression Model | 34.3%    | 86.6%    |
| concatenated system(Throuput) | 30.9%    | 80.2%    |

+-5 dollars accuracy means the accuracy with 5 NT dollars error margin.

## Dataset
There are two kinds of data:
### Image:
It contains both raw image and .txt file of label data. There are total 52 classes, we added a python script which can reduce class number to 9.
The decreased list is: ['plate', 'box', 'white rice', 'brown rice', 'purple rice', 'side dish', 'main_dish_25', 'main_dish_30', 'main_dish_40']

The Image dataset is packaged by Roboflow with Yolov7 format.
### Price
It contains ground truth price of each image. There is a column called fair price which is culculated only depends on number of each class and price of each class.
The corresponding image is also recorded in the Table. 

## Model
### Yolov7
The weight is Jinzhan.pt.
### Regression
It is in Model-> Regression.

## Training
### yolov7 model
* Train with 52 classes:
``` python
python train.py --workers 8 --device 0 --batch-size 32 --data Jinzhan-Cafeteria-AI/dataset/image_data
/data.yaml --img 640 640
```
* Train with 9 classes:
1. run decrease_label.py
``` shell
python decrease_label.py
```
2. modify the .yaml file
``` yaml
nc:9
names:['plate', 'box', 'white rice', 'brown rice', 'purple rice', 'side dish', 'main_dish_25', 'main_dish_30', 'main_dish_40']
```
3. Run
```python
python train.py --workers 8 --device 0 --batch-size 32 --data Jinzhan-Cafeteria-AI/dataset/image_data
/data.yaml --img 640 640
```
### Regresssion Model

## Inference
### Overall system
Go to file model.
``` shell
python detect.py --weights Jinzhan.pt --conf 0.25 --img-size 640 --source 0
```
To access camera
``` shell
python detect.py --weights Jinzhan.pt --conf 0.25 --img-size 640 --source -1
```
### Regresssion Model

## Generated Result
<div align="center">
    <a href="./">
        <img src="./example.png" width="39%"/>
    </a>
</div>

## Use of right
This is open to anyone who is interested.
