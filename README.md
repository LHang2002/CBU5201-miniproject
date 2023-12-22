# CBU5201-miniproject

&emsp;&emsp;This is a mini project about classification task in Machine Learning.It is also a final project of ML course in BUPT and QMUL.It was built by Yihang Lin and Rui Chen.

## Quick Start

We did following steps to config conda enviroment and train/test our model:
1. Run `conda create --name cbu5201 python=3.10` to create conda environment.
2. Run `conda activate cbu5201` to activate environment.
3. Run `pip install -r requirements.txt` to build your environment.
4. Run `python train.py` or `python train_advanced.py` to train basic task and advanced task,respectively.
5. Run `python test.py` or `python test_advanced.py` to test basic task and advanced task,respectively.
6. Run `python predict.py` or `python predict_advanced.py` to predict the classes of photos one by one,you can upload your photos to classify them.

## Project Structure

The repository consists of the following main components:
1. The dataset is located in `genki4k/files` and there are 3 other folders under `genki4k` which were named with suffix "(gender&color)","(preprocess)","(splitdata)",were represented as advanced task,files after preprocess and basic task,respectively.
2. We use ResNet to realize our tasks.ResNet was the most creative work in 2010s,which was proposed by Kaiming's team.In our repository,it is named as `resnet.py`.For training,pre trained model `resnet34-pre.pth` was downloaded from the pytorch org website.
3. Other components will be introduced in the next topic.

## Contributions

For realizing this mini project,we did following steps:
1. We first preprocess the dataset named `genki4k` which was downloaded from the UCSD website.We use `dlib`,`opencv`and `numpy` to preprocess the dataset.For preprocessing the dataset,we use shape predictor,which is a component in the `dlib` library and should be download from its org website,named as `shape_predictor_68_face_landmarks.dat`.If you want to try this step by yourself,just run `python preprocess.py`,we had completed the process file.
2. After preprocessing the dataset,we split the dataset into three parts,`train`,`test`and `val`.As their names,`train` for training,`test` for testing and `val` for validating.We seperated dataset in a 6:2:2 ratio.If you want to try this step by yourself,just run `python split_data.py` or `python split_data_advanced.py`,we had completed the split files.
3. Then,we use ResNet to realize our tasks.We selected the ResNet size of 34 blocks,which was named as ResNet34 by the authors.We download the pre trained model from the pytorch org website,which was named as `resnet34-pre.pth`.And then,we start training.If you want to try this step by yourself,just run `python train.py` or `python train_advanced.py`,we had completed the train files.
4. After training,two kind of files were generated,`class_indices.json`and `resNet34.pth`.The first one represent the classes for clarifying and the second one is the trained model.If you want to try this step by yourself,just run `python test.py` or `python test_advanced.py`,we had completed the test files.
5. We finished the two files for predicting,you can predict which classes your photos belong to and experience the power of machine learning. If you want to try this step by yourself,just run `python predict.py` or `python predict_advanced.py`,we had completed the predict files.Don't forget to change the relative path in the python files.

## Members

&emsp;&emsp;We have two members to finish this project.Yihang Lin,who is a senior undergraduate student at Soochow University,finished the coding part.Rui Chen,who is a third-year undergraduate student at Beijing University of Posts and Telecommunications,finished the essaying part.



