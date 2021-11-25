# Handmade Neural Network
Implementation of a configurable neural network from scratch exclusively in python.

## Table of contents
* [General](#general)
* [Project Overview](#project-overview)
* [Learning Task Overview](#learning-task-overview)
* [Technologies](#technologies)

## General
This project is a simple neural network mapping a polynomial function.

## Project Overview
Inspiration of this project lies in the fact that neural network, at its core, is simply a function estimator that, given enough data, can accurately map features (x) to target variables (y). So, here we have tried to map a fairly complex polynomial function so as to showcase the ability of a neural network to achieve that task using simple activation units like sigmoid, rectified linear and linear.

 Also, this project tries to explore and clarify what really goes on under the hood in a neural network. The choice of a polynomial function tries to mirror the functions a neural network tries to learn while performing tasks like image recognition or text classification. Clearly, we have chosen a much simpler task than the tasks mentioned above. This is done deliberately so as to serve the purpose of analysing the mechanics of neural network itself instead of dealing with the intricacies of a typical deep learning task.

Once cut open and clearly understood, we can explore numerous ways to experiment with the basic form of the network to create variations. The project is at its nascent stage and the code is largely inspired by Deep Learning Specialization from deeplearning.ai. Full specialization can be found out at - https://www.coursera.org/specializations/deep-learning.







## Learning Task Overview
Here we have chosen a fairly complex 2-dimensional polynomial function for the network to learn.

The chosen function is as follows:

$y = (x+3)(x-2)^2(x+1)^3$

As training data we have given our network equidistant but randomly permutated 1000 x-values and corresponding y-values. The domain of x-values of the function for training is [-3, 2.5]. The network is trained for 100,000 iterations.

Whereas, as validation data we use 100 equidistant x-values and corresponding y-values. The domain for validation data is [-4, 4].

We do not have test data because the purpose is to explore with the form of the network rather than to perform an actual learning task.


## Technologies
Project is created with:
* Python version: 3.10.0
* Numpy version: 1.21.4
* Matplotlib version: 3.4.3
