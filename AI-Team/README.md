# RedRosesDetector

# AI Development Team

## Overview

---

This software, which is an AI system, will be made with the objective of counting and detecting a type of roses, especifically explorer roses, that are in a given image. In order to do this, TensorFlow Lite is used, where files corresponding to the weights and architecture of the model will be exported. In this format which is tflite, the maximum number of objects detected is 25. Then, it will be used by other systems, specifically by a web platform and a mobile application.

## Dependencies

---

### Training

---

In order to train the model, we use Google Colaboratory. It is recommended to use, GPU hardware accelerator because it could take a lot of time depending on the amount of the training data, the number of epochs and the size of the model.

The only command we need for Google Colaboratory to install the required libraries is already in the first block of the notebook.

```bash
!pip install -q tflite-model-maker
```

Google Colaboratory uses Python version 3.7.12, and the other libraries needed are by default already installed.

- Matplotlib
- Tensorflow=2.7.0
- Numpy=1.19.2
- Pillow
- OpenCV

### Testing (Inference)

The archive **inference.py** is used for testing purpouses. So, in order to test our model, you must have install the following dependencies before use the model.

- Python3
- Matplotlib
- Tensorflow=2.7.0
- Numpy=1.21.4
- Pillow
- OpenCV
- Argparse

### Installation

---

1.- Create a python3 virtual environment. 

```bash
python3 -m venv inference_roses
```

2. Activate the virtual environment 

```bash
source inference_roses/bin/activate
```

3. Move to the directory that contains the **inference.py** file

```bash
cd Yachay-Tech-object-detection-projects/AI-Team/
```

4. Install dependencies

```bash
pip3 install -r requirements.txt 
```

5. You can download a custom Red Rose Image from any of your preferred sources.

# Usage

---

### Usage for training

---

For training we can change the number of epochs that by default is 50, the batch size, and the name of the model we will use. There are a list of models we can use depending on the performance we require. We use by default "efficientdet_lite2".

![screenshot.png](https://github.com/mateolomas/datasetRoses/blob/main/2.png)

- \* Size of the integer quantized models.
- ** Latency measured on Pixel 4 using 4 threads on CPU.
- *** Average Precision is the mAP (mean Average Precision) on the COCO 2017 validation dataset.

During Training it must take into account the following:

- In the training we use Pascal VOC format
- Training Images is into a folder with path is specified in the ImagesPath variable.
- Each image has a file with extension .xml, which are into a folder whose directory is in the LabelsPath variable.
- The Epochs are at 50 by default, however can be modified according to user preferences.

Once the training is finished:

- The original Tensorflow model Is evaluated on the test data with metrics same as COCO.
- A file named model.tflite will be exported, which contains the information about the model.
- The compressed Tensorflow Lite model is evaluated.

Optional:

- We can test our own image on the Tensorflow Lite model by changing the InputImagePath variable and the desired DETECTION_THRESHOLD that by default is 0.5.

### Usage for inference

---

```bash
python3 inference.py --help
```

![Screen Shot 2021-12-11 at 23.36.04.png](https://github.com/mateolomas/datasetRoses/blob/main/1.png)

Then, we are trying with an image called "rose1.jpg". We must use the flag **—image** in order to load an image in the current directory. 

```bash
python3 inference.py --image="red_rose.jpg" 
```

**Result**

![Screen Shot 2021-12-12 at 15.28.54.png](https://github.com/mateolomas/datasetRoses/blob/main/3.png)

In the console we can see the numbers of roses detected: 

```bash
Number of Red Roses: 8
```

We can use the flag **—threshold,** if we want to adjust the threshold parameter to improve our inference. A threshold of 0.5 is set by default. We're trying with 0.4.

```bash
python3 inference.py --image="red_rose.jpg" --threshold=0.4
```

![Screen Shot 2021-12-12 at 15.30.49.png](https://github.com/mateolomas/datasetRoses/blob/main/4.png)

In the console we can see the numbers of roses detected: 

```bash
Number of Red Roses: 10
```

After using the script and do all the testing needed we can deactivate the virtual environment.

```bash
deactivate 
```

## Authors

- Krishna Román. krishna.roman@yachaytech.edu.ec
- Mateo Sebastián Lomas. mateo.lomas@yachaytech.edu.ec
- Arianna Armijos. arianna.armijos@yachaytech.edu.ec
- Washington Pijal. washington.pijal@yachaytech.edu.ec

