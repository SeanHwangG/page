# ML

![Roles](images/20210220_193151.png)

![Types](images/20210220_193132.png)

* The field of study that gives computers the ability to learn without being explicitly programmed (Arthur Samuel 1959)
* A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience (E. Tom mitchell, 1998)
* Algorithms that can figure out how to perform important tasks by generalizing from examples (UW, 2012)
* Practice of using algorithms to parse data, learn from it, and then make a determination or prediction about something in the world (NVIDIA, 2016)

> Notation

* a: acitvation value
* J : cost function
* L : number of layer in the network

> Terms

* Augmentation
  * scale, translation, rotation

* Bias
  * difference between average prediction of our model and correct value which we are trying to predict

* End to End
  * [+] Less hand-designing of components needed
  * [-] Face recognition → large data for subproblems (face detection, face classification)
  * [-] Not enough data → excludes potential useful hand-designed components

* Training
  * Static : You can verify the model before applying it in production
  * Dynamic : model stays up to date as new data arrives

* Unsupervised Learning
  * unlabeled data that the algorithm tries to make sense of by extracting features and patterns on its own
  * [ex] market segmentation, organize computing cluster, social network analysis, astronomical data analysis
  * [+] spectral classes do not always correspond to informational classes

* Variance
  * Model with high variance pays a lot of attention to training data and does not generalize on data


> Feature

* Some set value -1, NaN      → linear, net model can suffer
* Mean, approximate         → weather data

* make range
  * power transformation
  * log transformation

* Finding
  * length of text field
  * percentage of characters that are punctuation in the text
  * percentage of character that are capitalize

* Nominal
  * One hot encoding → sparse matrix

* Ordinal
  * Special categorical feature where sorted in some meaningful order
  * Education (undergraduate, graduate), Grade (A, B, C)
  * Label (sorted) | Frequency | Rank encoding

* Coordinate
  * distance from Interesting places from data
  * center of clusters
  * Aggregated statistics

* Datetime
  * periodicity | time since row-independent | dependent event | difference between dates

* Numerical
  * Non tree-based models depend on scaling
  * Feature generation : fraction part in money (human perception), interval (human vs bot)
  * winsorization to remove outlier

## Engineering

> Terms

* Feature Selection

![Feature Selection](images/20210220_193357.png)

* Negative Sampling
  * train models that generally have several order of magnitudes more negative than positive one

> Learning

* Offline
  * [+] Make all possible predictions in a batch, using a mapreduce or similar.
  * [+] Write to a table, then feed these to a cache|lookup table
  * [-] long tail → can only predict things we know tail
  * [-] update latency likely measured in hours or days

* Online
  * Predict on demand, using a server
  * [+] can predict any new item as it comes
  * [-] monitoring needs are more intensive

> Dynamic Sampling

* Minlong Lin, 2013

$$
P\left(X^{!}\right)=1.0-P\left(\frac{X}{\text { Sum of Candidates }}^{0.7}\right)
$$

### Metric

> Cosine Similarity

$$ \frac{A \cdot B}{\|A\|\|B\|} $$

* Euclidean
  * Favor small sets

$$ \left|U_{i} \backslash U_{j}\right|+\left|U_{i} \backslash U_{j}\right|=\left\|R_{i}-R_{j}\right\| $$

> softmax

{% tabs %}
{% tab title='softmax.py' %}

```py
import numpy as np

def softmax(x):
  """ Args    : input value [N, dim]
      Returns : softmax [N, dim]
  """
  m = np.amax(x, axis=(0, 1))
  ret = np.exp(x - m) / np.sum(np.exp(x - m), axis=1, keepdims=True)
  return ret
```

{% endtab %}
{% endtabs %}

> Cross Entropy

* used for mutually exclusive classes (male vs female, grayscale vs color)
* probability distribution of the event over k different events

$$
g(z)_{i}=\frac{e^{z_{i}}}{\sum_{j=1}^{K} e^{z_{j}}}
$$

$$
\begin{array}{ll}
J(W)=-(y \log (\hat{y})+(1-y) \log (1-\hat{y})) & \text { binary } \\
J(W)=-\frac{1}{N} \sum_{n=1}^{N} y_{n} \log \hat{y}_{n}+\left(1-y_{n}\right) \log \left(1-\hat{y}_{n}\right) & \text { multi class }
\end{array}
$$

> Similarity

* Cosine
  * Useful for positive | negative feedback
  * independent of vector length → commonly used measure for high-dimensional spaces

* Jaccard
  * [-] Cannot use if the input is binary (ex. Recsys thumbs up vs thumbs down)

$$
J \operatorname{accard}\left(U_{i}, U_{j}\right)=\frac{\left|U_{i} \cap U_{j}\right|}{\left|U_{i} \cup U_{j}\right|}
$$

{% tabs %}
{% tab title='jaccard.py' %}

```py
import gzip
import numpy
import random
import requests
from collections import defaultdict

# Data
"""
{'marketplace': 'US',
 'customer_id': '45610553',
 'review_id': 'RMDCHWD0Y5OZ9',
 'product_id': 'B00HH62VB6',
 'product_parent': '618218723',
 'product_title': 'AGPtek® 10 Isolated Output 9V 12V 18V Guitar Pedal Board Power Supply Effect Pedals with Isolated Short Cricuit / Overcurrent Protection',
 'product_category': 'Musical Instruments',
 'star_rating': 3,
 'helpful_votes': 0,
 'total_votes': 1,
 'vine': 'N',
 'verified_purchase': 'N',
 'review_headline': 'Three Stars',
 'review_body': 'Works very good, but induces ALOT of noise.',
 'review_date': '2015-08-31'}
"""
def jaccard(s1, s2):
  numer = len(s1 & s2)
  denom = len(s1 | s2)
  return numer / denom

def most_similar(i):
  similarities = []
  users = item2user[i]

  candidate_items = set()
  for u in users:
    candidate_items |= user2item[u]

  for i2 in candidate_items:
    if i == i2: continue
    sim = jaccard(users, item2user[i2])
    similarities.append((sim, i2))
  similarities.sort(reverse=True)
  return similarities[:10]

user2item, item2user = defaultdict(set), defaultdict(set)

item_name = {}
for d in data:
  u, i = d['customer_id'], d['product_id']
  item2user[i].add(u)
  user2item[u].add(i)
  item_name[i] = d['product_title']

display(data[2])
for sim, iid in most_similar(data[2]['product_id']):
  print(f"{item_name[iid][:55]:<60} has {sim:.3f} most similar item")
```

{% endtab %}
{% endtabs %}

> Pearson Correlation

* Subtract by normalized value → Useful for numerical rating

$$
\frac{\sum_{j}\left(r_{i j}-\bar{r}_{i}\right)\left(r_{k j}-\bar{r}_{k}\right)}{\sqrt{\sum_{j}\left(r_{i j}-\bar{r}_{i}\right)^{2} \sum_{j}\left(r_{k j}-\bar{r}_{k}\right)^{2}}}
$$

> F1

* gives a larger weight to lower numbers
* macro-F1 arithmetic mean of our per-class F1-scores
* weighted-F1, weight each class by the number of samples from that class
* micro-averaged F1, micro-F1 = micro-precision = micro-recall = accuracy

$$
2 \cdot \frac{\text { Prec } \cdot \text { recall }}{\text { Prec }+\text { recall }}=\frac{2 T P}{2 T P+F P+F N}
$$

* Fb
  * Low beta: precision is more important.
  * High beta: recall is more important

$$
\left(1+\beta^{2}\right) \cdot \frac{\text { prec } \cdot \text { recall }}{\beta^{2} \cdot \text { prec }+\text { recall }}
$$

> Triplet Loss


| Notation | Meaning            |
| -------- | ------------------ |
| $A$      | Anchor             |
| $P, N$   | Positive, Negative |
| $\alpha$ | Margin             |

$$L(A, P, N)=\max \left(\|f(A)-f(P)\|^{2}-\|f(A)-f(N)\|^{2}+\alpha, 0\right)$$
$$\frac{\|f(A)-f(p)\|^{2}}{d(A, P)}-\frac{\|f(A)-f(N)\|^{2}}{d(A, N)}+\alpha \leq 0 $$

## Traditional

### Feature

> PCA (Principal component analysis)

| Notation                        | Meaning             |
| ------------------------------- | ------------------- |
| $x_{i}$                         | Original Point      |
| $y_{i}=\varphi_{i} \cdot x_{i}$ | Rotated Point       |
| $\varphi$                       | Rotation            |
| $\varphi_{i}^{T} \varphi_{j}$   | 1 iff i = j, else 0 |

| Equation                                                                                                                                                             | Meaning                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| $x_{i} \simeq \sum_{j=1}^{K} \varphi_{j} y_{j}+\sum_{j=K+1}^{M} \varphi_{j} b_{j}$                                                                                   | Discard K+1 ~ M dimension |
| $\min _{\varphi, b} \frac{1}{N} \sum_{y}\left\|\sum_{j=1}^{K} \varphi_{j} y_{j}+\sum_{j=K+1}^{M} \varphi_{j} b_{j}-\sum_{j=1}^{M} \varphi_{j} y_{j}\right\|_{2}^{2}$ |                           | MSE of lost information |
| $\min _{\varphi, b} \frac{1}{N} \sum_{y}\left\|\sum_{j=k+1}^{M} \varphi_{j}\left(y_{j}-b_{j}\right)\right\|_{2}^{2}$                                                 | Simplify                  |
| $\min _{\varphi} \frac{1}{N} \sum_{j=K+1}^{M} \varphi_{j}(X-\bar{X})(X-\bar{X})^{T} \varphi_{j}^{T}$                                                                 | Expand in terms of X      |
| $\min _{\varphi} \frac{1}{N} \sum_{j=K+1}^{M} \varphi_{j} \operatorname{Cov}(X) \varphi_{j}^{T}-\lambda_{j}\left(\varphi_{j} \varphi_{j}^{T}-1\right)$               | Lagrange multiplier       |

* discovers latent feature
* Ranked in order of their explained variance
* first principal component (PC1) explains the most variance in your dataset

> SVD (Singular Value Decomposition)

$$A=U \Sigma V^{T}$$
$$A^{T} A=\left(V \Sigma^{T} U^{T}\right) U \Sigma V^{T}=V\left(\Sigma^{T} \Sigma\right) V^{T}$$

$U$ | m * m orthonormal matrix
$\Sigma$ | m * n diagonal matrix
$\sigma$ | singular values of A $\gamma_1 >= \gamma_2 >= ... >= 0$
$V^{T}$ | an n × n orthonormal matrix

* Any matrix A (m × n) can be written as the product of three matrices

> t-SNE

* a nonlinear dimensionality reduction technique well-suited for embedding high-dimensional data for visualization in a low-dimensional space of two or three dimensions

> UV Decomposition

* PCA, SVD not defined for partially observed matrices , doesn't work for huge matrix ⇒ UV
* Used in large sparse matrix where element can be empty (not 0)


### Classification

* supervised learning / categorical
* Output variable in the regression is numerical|continuous
* Useful for sparse high-dimensional data
* Split space into 2 subspaces
* Not work for non-linear transformations of parameters (θ0 + θ12 · X)
  * use Neural network instead

![Classification](images/20210314_005720.png)

> Term

* Confusion matrix

![Confusion matrix](images/20210305_201340.png)


> True Positive

![True Postive](images/20210305_201438.png)

| Equation                          | Meaning                                                                |
| --------------------------------- | ---------------------------------------------------------------------- |
| $\frac{T P+T N}{T P+F P+T N+F N}$ | Accuracy                                                               |
| $\frac{1}{2}(FPR + FNR)$          | Balanced Error rate                                                    |
| $\frac{T P}{T P+F N}$             | True Positive Rate (Sensitivity, True positive rate, Recall, Hit rate) |
| $\frac{TN}{FN+FP}$                | True Negative Weight (Specificity, Selectivity)                        |
| $\frac{FP}{FP+TN}$                | False positive rate                                                    |
| $\frac{FN}{FN+TP}$                | False negative rate (miss rate)                                        |
| $\frac{T P}{T P+F P}$             | Precision                                                              |

{% tabs %}
{% tab title='multiclass_acc_prec.py' %}

```py
TP, FP, TN, FN = [0 for i in range(202)], [0 for i in range(202)], [0 for i in range(202)], [0 for i in range(202)]
classes = []

for p, l in zip(preds, labels):
  if p == l:
    TP[pred] += 1
    for i in range (len(TP)):
      TN[i] += 1
    TN[pred] -= 1
  else:
    FP[pred] += 1
    FN[label] += 1
    for i in range (len(TN)):
      TN[i] += 1
    TN[pred] -= 1
    TN[label] -= 1

for tp, fp, tn, fn in zip(TP, FP, TN, FN):
  accuracy = (tp + tn) / (tp + fp + tn + fn)
  precision if fp + tp == 0 else tp / (fp + tp)
  recall = 0 if tp + fn == 0 else tp / (tp + fn)
  bcr = (precision + recall) / 2
  classes.append({"Class": i, "Precision": precision, "Accuracy": accuracy, "Recall": recall, "BCR": bcr})
```

{% endtab %}
{% endtabs %}


### Regression

* Discrete

![Regession](images/20210314_005741.png)

> Logistic Regression

* logistic regression is based on statistical approaches

| Term         | Value                            | Meaning                                       |
| ------------ | -------------------------------- | --------------------------------------------- |
| odds         | $\frac{p}{1-p}$                  |                                               |
| logit        | $\ln \left(\frac{p}{1-p}\right)$ |                                               |
| $logit^{-1}$ | $\frac{1}{1+e^{-x}}$             | probability of being in the event occur group |


> Mean absolute error

$$\frac{\sum_{i=1}^{n}\left|y_{i}-x_{i}\right|}{n}$$

> Mean biased error

$$\frac{\sum_{i=1}^{n} y_{i}-x_{i}}{n}$$

> Mean squared error

| Equation                      | Meaning                                          |
| ----------------------------- | ------------------------------------------------ |
| $\frac{M S E(f)}{V A R(y)}$   | Fraction of Variance (1 means perfect predictor) |
| $1-\frac{M S E(f)}{V A R(y)}$ | Coefficient of determination                     |

* Based on the assumption that error is normally distributed
* If we predict mean value, that is variance
* coefficient of determination

> RMSE (Root Means Sequared Error)

* more useful when large errors are particularly undesirable
* expects that the all sample data is measured exactly, or observed without error
* Metric used for netflix prize

$$ \sqrt{\frac{\sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}}{n}} $$

> Total Least Square

![Total Least Square](images/20210324_145214.png)

$\frac{1}{2 n} \sum_{x}\|y(x)-\hat{y}(x)\|^{2}$

### Clustering

| Notation  | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| cut(c, c) | number of edges that separate c from the rest of the network |

* Four types of clustering methods are 1) Exclusive 2) Agglomerative 3) Overlapping 4) Probabilistic

> Hierarchical Clustering

* Iteratively merge closest points which constructs dendrogram
* Useful for geographic location

![Hierarchical Clustering](images/20210324_000002.png)

> K-mean

* Soft K-means
  * replace hard memberships to each cluster by a proportional membership to each cluster

$C_{k}=\frac{\sum_{i} \delta\left(y_{i}=k\right) X_{i}}{\sum_{i} \delta\left(y_{i}=k\right)}$

> K-median

* replace mean with median to minimize 1-norm distance

$$ y_{i}=\min _{C, y} \sum_{i}\left\|X_{i}-C_{y i}\right\|_{2}^{2} $$

> Normalized cut

![Normalized Cut](images/20210324_143607.png)

$$\frac{1}{|C|} \sum_{c \in C} \frac{\operatorname{cut}(c, \bar{c})}{d e g r e e s \operatorname{in} c}$$

> Ratio Cut

![Ratio Cut](images/20210324_143644.png)

$$\frac{1}{|C|} \sum_{c \in C} \frac{\operatorname{cut}(c, \bar{c})}{|c|}$$

### Linear

![Decision map](images/20210322_184729.png)

> SVM

![Support vector machine](images/20210305_201646.png)

* SVM is based on geometrical properties of the data
* [+] Risk overfitting is less in SVM, while Logistic regression is vulnerable to overfitting
* Kernel
  * mapping the non-linear separable data-set into a higher dimensional to find a separable hyperplane

* Optimization function

$$ \arg \min _{\theta, \alpha} \frac{1}{2}\|\theta\|_{2}^{2} \text { such that } \forall_{i} y_{i}\left(\theta \cdot X_{i}-\alpha\right) \geq 1 $$

* Decision rule

$$ w \cdot u+b \geq 0, \text { then }+ $$

> KNN (K nearest neighbors)

* transformed into a fast indexing structure such as a Ball Tree or KD Tree

> Linear Discriminant Analysis

* Maximizes the separability between classes
* maximize distance between means | minimize variation within each category
* LD1 accounts for the most variation between categories

> Principal Component Analysis

![Limitation](images/20210322_193043.png)

### Tree

![Random Forest vs Boosting](images/20210222_225347.png)

* Useful for tabular data
* avoid overfitting in two ways: to add a stopping criteria, or to use tree pruning

> Gradient Boosting Decision Tree

* ensemble that takes an iteratively combine weak learners to create a strong learner
* focus on mistakes of prior iterations
* [+] powerful, accepts various inputs, used for classification / regression, outputs feature importance
* [-] longer to train, likely to overfit, difficult to tune
* Overfit
  * max_depth (7), subsample, colsample_bytree, colsample_bylevel, eta, num_rounds
* Under fit
  * min_child_weight (0, 5, 15, 500), lambda alpha

> Random Forest

* each decision tree gets a random sample | columns of the training data to be sent to each tree
  * [+] does not increase generalization error when more trees are added to the model
  * [-] don’t train well on smaller datasets
  * [-] problem of interpretability with random forest
  * [-] Random forests do not handle large numbers of irrelevant features
  * [-] models requires O(NK) memory storage, (N - # of base, K - # of trees)

> Extra Tree

* Split of each selected feature is random → less computationally expensive than a random forest
* Extra Trees show low variance

### Ensemble

![Types](images/20210324_000215.png)

![Bagging vs Boosting](images/20210324_143414.png)

* technique that creates multiple models and then combines them to produce better results

* Bagging
  * combine them using some model averaging techniques (e.g. weighted average, majority vote)
  * Random Forest models

* Boosting
  * takes less time|iterations to reach close to actual predictions
  * Adaptive Gradient Boosting
    * machine learning meta-algorithm formulated by Yoav Freund and Robert Schapire

* Cascading
  * reject if any of the classifier doesn’t match




## Deep Learning

![ML vs Deep Learning](images/20210220_193500.png)

* Neural networks become deep neural networks if it contains two or more hidden layers
* Zhou, Boris proved Neural Network can approximate any convex continuous function

* If a model has low loss in the training data but poor on test, what should you do?
  * implement L2 regularization on the weights
  * decrease the number of hidden units in the model

* Overfitting?
  * a network is learning features in the train data not useful in generalizing predictions to the holdout set

* Which activation functions for the hidden units might cause vanishing gradients?
  * Tanh, sigmoid (Not relu)

* Why should bias be added?
  * Without b the line always goes through the origin (0, 0) and you may get a poorer fit. When x = 0.

> Notation

![Notation](images/20210220_193309.png)

| Notation                                               | Meaning                                                |
| ------------------------------------------------------ | ------------------------------------------------------ |
| $b^{[l]}$                                              | # Bias vector in $I^{th}$ Layer                        |
| $g^{[l]}$                                              | $I^{th}$ layer activation function                     |
| $h(x)$                                                 | hypothesis                                             |
| $m$                                                    | Number of examples in datasets                         |
| $n_{x} / n_{y}$                                        | input / output size                                    |
| $n_{h}^{[l]}$                                          | number of hidden units of $I^{th}$ layer               |
| $W^{[l]}$                                              | Weight matrix in $I^{th}$ layer                        |
| $x \mid X$                                             | input / input matrix ($n_x$, m)                        |
| $x^{(i)}$                                              | $i^{th}$ example represented as a column of ($n_x$, 1) |
| $\hat{y}$                                              | predicted output vector                                |
| $Y$                                                    | label matrix ($n_y$, m)                                |
| $z$                                                    | weighted sum input                                     |
| $a=\sum_{j=0}^{d} w_{j} x_{j}=w^{T} x$                 | Weighted Sum Output                                    |
| $\delta_{j}^{p}=\frac{\delta J^{P}}{\delta a_{j}^{p}}$ | Delta                                                  |
| $L=\prod_{n=1}^{N} P\left(X^{n}\right)$                | Likelihood                                             |
| $-\ln L=-\ln \prod_{n=1}^{N} P\left(X^{n}\right)$      | Error                                                  |

> Terms

* Auto-encoder
  * denoise auto-encoder to make robust
  * learn efficient data encodings in an unsupervised manner

* Epoch
  * one forward pass and one backward pass of all the training examples

* Batch
  * number of training examples in one forward/backward pass. higher batch size needs more memory space

* Iteration
  * Number of passes each pass using number of examples

* Normalization
  * inputs and each hidden unit throughout the network, on a per-unit basis, over each minibatch

* Fine-tuning
  * process in which the parameters of a trained model must be adjusted very precisely
  * to validate that model taking into account a small data set that does not belong to the train set.

* Inception
  * CNN uses convolutions kernels of multiple sizes as well as pooling within one layer

* Internal representation (Rumelhart, 87)

![alt](images/20210210_183904.png)

* Graph Neural Netwrok (GNN)

![alt](images/20210210_183847.png)

### Activation Function

* non-linear, differentiable
* multi-class situation vs binary situation
* One hot encoding

* non-exclusive vs mutually exclusive
  * sum of all probabilities will be equal to one

* dendrites : input
* soma : summation function
* axon : activation function

![Human brain](images/20210316_153624.png)

> Linear

![Linear](images/20210210_184041.png)

$$
g(a) = a
$$

* no matter how many layers it had, it will behave just like a single-layer perceptron

> Perception

![](images/20210316_153550.png)

$$
g(z)=1(z \geq \theta), 0
$$

> Relu

![ReLu](images/20210222_225423.png)

* good performance especially when dealing with vanishing gradient

$$
g(z)=max(0,z) \\
g'(z)=1 (z>0), 0
$$

> Leaky Relu

![Leaky Relu](images/20210316_153436.png)

$$
g(z)=x<0 ? 0.01 x: x \\
g^{\prime}(z)=x<0 ? 0.01: 1
$$

> Sigmoid

* binary classification
* used for multiple non-exclusive classes (beach, night, boat)

$$
g(z)=\frac{1}{1+e^{-x}} \\
g^{\prime}(z)=\sigma(z)(1-\sigma(z))
$$

> TanH

![tanh](images/20210316_153806.png)

$$
\begin{array}{l}
g(x)=\tanh (x) \\
g^{\prime}(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}
\end{array}
$$


### Gradient Descent

> Delta Rule

$$
\Delta w_{ij}^p = \eta \delta_j^p a_i^p%0
$$

$$
\delta_{j}^{p}=\frac{\partial J^{p}}{\partial a_{j}^{p}}=\sum_{k} \frac{\partial J^{p}}{\partial a_{k}^{p}} \frac{\partial a_{k}^{p}}{\partial a_{j}^{p}}=\sum_{k} \delta_{k}^{p} w_{j k}
$$

> Deep Learning

$\frac{\partial E}{\partial a_{j}}=\sum_{k} \frac{\partial E}{\partial a_{k}} \frac{\partial a_{k}}{\partial a_{j}}$

$$
=-\sum_{k} \delta_{k} \frac{\partial a_{k}}{\partial z_{j}} \frac{\partial z_{j}}{\partial a_{j}}
$$

$$
=-\frac{\partial z_{j}}{\partial a_{j}} \sum_{k} \delta_{k} \sum_{i} \frac{\partial w_{i k} z_{i}}{\partial z_{j}}
$$

$$
=-g^{\prime}\left(a_{j}\right) \sum_{k} \delta_{k} w_{j k}
$$


> Adaptive learning rate

* Increase local gain if the gradient for that weight doesn't change the sign
* Limit the gains to lie in some reasonable range
* Use full batch learning or big mini-batches

> Momentum

* The magnitudes of the gradients can be different for different layers, especially if small initial weights

* Standard
  * standard momentum method first computes the gradient at the current location
  * then takes a big jump in the direction of the updated accumulated gradient.
* Nesterov
  * Nesterov momentum first makes a big jump in the direction of the previously accumulated gradient.
  * Then measure the gradient where you end up and make corrections.

> L1 Normalization

$$
L 1(W)=\sum_{k} \sum_{l}\left|W_{k, l}\right|
$$

> L2 Normalization

$$
L 2(W)=\sum_{k} \sum_{l} W_{k, l}^{2}
$$

### Training

> Analyze datao

* look for class imbalance, misclassified labels, duplicate data.
* spatial position matter

> Visualize features

![alt](images/20210214_013159.png)

* Feature maps need to be uncorrelated and have high variance.
* Hidden units are sparse across samples and across features.

> Starts with simple baseline

* Fix random seed → stable.
* Simplify - turn off data augmentation.
* Add significant digits to your eval, verify loss @ init.
* human baseline → annotate label and prediction
* Overfit one batch to see if you can achieve 0 loss.
* Measure error on both training and validation set.
* use backprop to chart dependencies

> Overfit

* Pick a known model
* Adam is safe → try with 3e-4

> Regularize

* Get more data. Data augmentation
* Pretrain data.
* Decrease batch size.
* Dropout, weight decay, early stop
* Try a larger model → early stopped performance of larger often be better.

### RNN

> Map time into space

* Auto regressive model
  * Linear model
  * Predict the next term in a sequence from a fixed number of previous terms using delay taps.

![alt](images/20210214_014206.png)

* Feed-Forward neural network
  * generalized autoregressive models by using one or more layers of non-linear hidden units.
  * Transformer networks use identical networks over every location in the input (up to 256 locations)
  * The networks then interact via attention mechanisms

![alt](images/20210214_014302.png)



> Map time into state

* Jordan network

![alt](images/20210214_014033.png)

* One time step back

* Elman network

![alt](images/20210214_014048.png)


### LSTM

![alt](images/20210214_013941.png)

* preserve data for a long time in the activities of an RNN, use a circuit that implements an memory cell.
* A linear unit that has a self-link with a weight of 1 will maintain its state.
* Information is stored in the cell by activating its write gate.
* Information is retrieved by activating its read gate
* We can backpropagate through this circuit because logistic units have nice derivatives.

$$
\begin{aligned}
\boldsymbol{g}^{(t)} &=\phi\left(W_{g x} \boldsymbol{x}^{(t)}+W_{i h} \boldsymbol{h}^{(t-1)}+\boldsymbol{b}_{g}\right) \\
\boldsymbol{i}^{(t)} &=\sigma\left(W_{i x} \boldsymbol{x}^{(t)}+W_{i h} \boldsymbol{h}^{(t-1)}+\boldsymbol{b}_{i}\right) \\
\boldsymbol{f}^{(t)} &=\sigma\left(W_{f x} \boldsymbol{x}^{(t)}+W_{f h} \boldsymbol{h}^{(t-1)}+\boldsymbol{b}_{f}\right) \\
\boldsymbol{o}^{(t)} &=\sigma\left(W_{o x} \boldsymbol{x}^{(t)}+W_{o h} \boldsymbol{h}^{(t-1)}+\boldsymbol{b}_{o}\right) \\
\boldsymbol{s}^{(t)} &=\boldsymbol{g}^{(t)} \odot \boldsymbol{i}^{(i)}+\boldsymbol{s}^{(t-1)} \odot \boldsymbol{f}^{(t)} \\
\boldsymbol{h}^{(t)} &=\boldsymbol{s}^{(t)} \odot \boldsymbol{o}^{(t)}
\end{aligned}
$$

### Style Transfer

* [Gatys, 2015](https://arxiv.org/abs/1508.06576)

* Style matrix

$$ G_{k k^{\prime}}^{[l]}=\sum_{i=1}^{n_{H}} \sum_{j=1}^{n_{W}} a_{i j k}^{[l]} \cdot a_{i j k^{\prime}}^{[l]} $$

* Initialize G randomly and keep minimize above cost function
* Style cost function

$$ J(G)=\alpha \cdot J_{\text {content }}(C, G)+\beta \cdot J_{\text {style }}(S, G) $$
$$ J_{s t y l e}^{[l]}(S, G)=\frac{1}{\left(2 n_{H}^{[l]} n_{W}^{[l]} n_{C}^{[l]}\right)^{2}} \sum_{k} \sum_{k^{\prime}}\left(G_{k k^{\prime}}^{[l](S)}-G_{k k^{\prime}}^{[l](G)}\right)^{2} $$

* Content Cost function

$$ J_{\text {content }}(C, G)=\frac{1}{2}\left\|a^{[l](c)}-a^{[l](G)}\right\|^{2} $$

## NLP

* an automated way to understand or analyze the natural languages and extract the required information from such data by applying machine learning Algorithms
* Used in Semantic Analysis, Automatic summarization, Text classification, Question answering

> Terms

* Dependency Parsing
  * Aka Syntactic Parsing, the task of recognizing a sentence and assigning a syntactic structure to it.

* Entity (Words of interest)
  * names of persons, locations and companies

* Entity Linking
  * Name variations (New York, NY, neuyork)
  * Ambiguity (Paris Hilton vs Paris in France)
  * Absence (Domain specific knowledge base)
  * Scalability (Chatbot, Search)
  * Evolving Information (Recent news articles in which there are mentions)
  * Multiple Languages (Support queries performed in multiple languages)

* Knowledge base
  * words of interest are mapped from input text to corresponding unique entities in target knowledge base

* Hypernym
  * Is a Relation | a word of less specific meaning
  * chiroptophobia and phobia
  * opera and music

![alt](images/20210213_232247.png)

* Hyponym
  * Subclass of
  * If X is a hyponym of Y, and Y is a hyponym of Z, then X is a hyponym of Z
  * pigeon, eagle and seagull are hyponyms of bird

* Latent Semantic Indexing
  * LSI, aka Latent semantic analysis, is a mathematical method developed to increase the accuracy of retrieving
  * It helps to find out the hidden relation between the words by producing a set of various concepts related to the terms of a sentence to improve the information understanding.
  * technique used for the purpose is called Singular value decomposition, useful for working on small sets of a static document

* LDA
  * Latent Dirichlet Allocation

* Meronym
  * Part of

```sh
a 'tire' is part of a 'car'             # Part meronym
a 'car' is a member of a 'traffic jam'  # Member meronym
a 'wheel' is made from 'rubber'"​        # Substance (stuff) meronym
```

* Named entity disambiguation
  * ambiguity of entity names tends to be much higher (e.g., mentions of common last | first name-only).

![](images/20210305_195400.png)

* POS tagging
  * PoS Tagger is a piece of software that reads a text in some language and assigns PoS to each word
  * make more complex categories than those defined as basic PoS (ex noun-plural)

* Pragmatic Analysis
  * It deals with outside word knowledge, which means knowledge that is external to the documents|queries.
  * Pragmatic analysis that focuses on what was described is reinterpreted by what is actually meant, deriving the various aspects of language that require real-world knowledge

* Lemmatization
  * do the things properly with the use of vocabulary and morphological analysis of words
  * lemmatizing is more accurate as it uses more informed analysis to create groups of words
  * democracy, democratic, democratization → democracy
  * saw → s


* Pragmatic analysis
  * Can be defined as the words which have multiple interpretations
  * Pragmatic Analysis is part of the process of extracting information from text.

* Stemming
  * stemming is faster as it simply chops off the end of a word using heuristics
  * democracy, democratic, democratization → democr
  * saw → see | saw (meaning)

* Synonym
  * Similar words

* Syntactic analysis
  * a sentence may be interpreted in more than one way due to ambiguous sentence structure
  * proper ordering of words.

* Tokenization
  * Methods of dividing the text into various tokens. (in the form of the word)

* Word sense disambiguation
  * mapping con- tent words to a predefined inventory of word senses

### Embedding

| Notation | Term                |
| -------- | ------------------- |
| $u_{w}$  | Context word        |
| $v_{w}$  | Center word         |
| $b_{i}$  | Biases of i         |
| $X$      | Co-occurence matrix |

* Intrinsic evaluation
  * Fast to compute
  * Evaluation on a specific / intermediate subtask
  * Dataset : wordsim353

* Extrinsic evaluation
  * Evaluation on a real task
  * can take a long time to compute accuracy
  * Unclear if the subsystem is the problem or its interaction or other subsystems

> A mathematical theory of communication (Shannon, 1948)

* understand context within sentence → hang out
* [-] a very large vector → meaning of each value in the vector is known
* [-] disregarding grammar and even word order

![ngram](images/20210314_004152.png)

> Distributed representations (Hinton, 1986)

* one-hot vector
* [-] hotel and model are orthogonal

> Producing high-dimensional semantic spaces from lexical co-occurrence (Lund, 96)

* [+] Fast Training / Efficient usage of statistics
* [-] Primarily used to capture word similarity
* [-] Disproportionate importance given to large counts

> Improved Method for Deriving Word Meaning from Lexical Co-Occurrence (Rohde, 04)

* [+] Add threshold, manual tuning for distant word

> Efficient Estimation of Word Representations in Vector Space (Mikolov, 2013)

* word2vec(Continuous Bag of Words (CBOW)) predict center word from context words
* can be trained with a specific corpus to find pseudo-algebraic operations between words
* mimics human logic, focusing on word senses and connections between real-world entities
* [+] Generate improved performance, capture complex patterns
* [-] Scales with corpus size / Inefficient usage of statistics
* [-] Can't compute accurate word similarity
* [-] Miss nuance (proficient, good), new meanings of words (ninja)
* [-] Same vector for synonyms

| Equation | Meaning |
| -------- | ------- |
$P(o \mid c)=\frac{\exp \left(u_{o}^{T} \cdot v_{c}\right)}{\sum_{w=1}^{v} \exp \left(u_{w}^{T} \cdot v_{c}\right)}$
$\frac{\delta}{\delta v_{c}} J(\theta)=u_{0}-\sum_{x=1}^{v} p(x \mid c) \cdot u_{x}$ | Used Chain Rule
$J_{n e g}\left(o, v_{c}, U\right)=-\log \left(\sigma\left(u_{o}^{T} v_{c}\right)\right)-\sum_{k=1}^{K} \log \left(\sigma\left(-u_{k}^{T} v_{c}\right)\right)$ | Negative Sampling

* Prediction function

$$ P(o \mid c)=\frac{\exp \left(u_{o}^{T} v_{c}\right)}{\sum_{w \in V} \exp \left(u_{w}^{T} v_{c}\right)} $$

* Likelihood

$$ L(\theta)=\prod_{t=1}^{T} \prod_{m \leq j \leq m} P\left(w_{t+j} \mid w_{t} ; \theta\right) $$

* Objective

$$ J(\theta)=-\frac{1}{T} \log L(\theta) $$

> Distributed Representations of Words and Phrases and their Compositionality (Mikolov, 2013)

* Skip-grams (SG) predict context words given center words

> GloVe: Global Vectors for Word Representation (Pennington, 14)

* local statistics (local context information of words) + global statistics (word co-occurrence) for vector
* training only on the nonzero elements in a word-word co occurrence matrix
* [+] Fast training, scalable to huge corpora
* [+] good performance with small corpus and small vectors

| Equation                                                                                                       | Meaning                |
| -------------------------------------------------------------------------------------------------------------- | ---------------------- |
| $w_{i} \cdot w_{j}=\log P(i \mid j)$                                                                           | Log-bilinear model     |
| $w_{x} \cdot\left(w_{a}-w_{b}\right)=\log \frac{P(x \mid a)}{P(x \mid b)}$                                     | with vector difference |
| $\sum_{i, j=1}^{V} f\left(X_{i j}\right)\left(w_{i}^{T} \bar{w}_{j}+b_{i}+\bar{b}_{j}-\log X_{i j}\right)^{2}$ | Loss Function          |

> TFIDF

* Term Frequency: How often a word occurs in a document
* Inverse Document Frequency : How often a word occurs in an entire set of documents
* Weight higher the more a word appears in doc and not in corpus

| Notation     | Meaning                     |
| ------------ | --------------------------- |
| N            | total # of documents        |
| $tf_{i . j}$ | $ of times i occurs in j    |
| $d f_{i}$    | $ of documents containing i |

$$ w_{i, j}=tf_{i . j} \times \log \left(\frac{N}{df_{i}}\right) $$

### Named Entity Disambiguation

> Term

* Context : All words in the input text except stopwords and entity
* Entity  : Disambiguated thing    (ex. Wiki article, Yago, NLU)
* Mention : Not disambiguated thing    (ex. Stanford NER)

> Context (Milne08)

* cosine similarity, weighted Jaccard distance, KL divergence
* [+] work well for long, clean input texts such as predicting the link target of Wikipedia anchor text
* [-] similarity have been developed for common nouns and verbs (Thater 10) / short text
* [-] IU played guitar in Paris. (Paris might be a guitarist, but IU ↔ Paris not relation)
* Inlink share

$$
M W(e, f)=1-\frac{\log \left(\max \left\{\left|I_{e}\right|,\left|I_{f}\right|\right\}\right)-\log \left(\left|I_{e} \cap I_{f}\right|\right)}{\log (N)-\log \left(\min \left\{\left|I_{e}\right|,\left|I_{f}\right|\right\}\right)}
$$

* Collective assignment (Kulkarni 09)
  * coherence of the resulting entities, in the sense of semantic relatedness
  * [-] Manchester and Barcelona that takes place in Madrid

> Robust NED (Hoffart, 12)

* Density : # total weight of subgraph edges / minimum weighted degree in sub-graph
* Coherence  : Entity-Entity (ex. # inlinks Wikipedia articles share)
* Prior      : Mention-Entity (ex. Number of inlinks)
* Similarity : Context-Entity (ex. CosSim)
* simplest heuristics for name resolution is to choose the most prominent entity for a given name
* (ex) place with the most inhabitants or largest area / largest number of incoming links in Wikipedia
* [-] Non popular entities will never be identified

* Coherence

$$ u(E, T)=2 \cdot \frac{H(E)+H(T)-H(E, T)}{H(E)+H(T)} $$

* Entropy

$$ H(X)=-\sum_{x \in X} p(x) \log p(x) $$

* Phrase overlap

$$ P O(p, q)=\frac{\sum_{w \in \eta \cap q} \min \left\{\gamma_{e}(w), \gamma_{f}(w)\right\}}{\sum_{w \in p \cup q} \max \left\{\gamma_{e}(w), \gamma_{f}(w)\right\}} $$

* Phrase overlap with Norm

$$ \operatorname{KORE}(e, f)=\frac{\sum_{p \in P_{e}, q \in P_{f}} P O(p, q)^{2} \cdot \min \left\{\phi_{e}(p), \phi_{f}(q)\right\}}{\sum_{p \in P_{e}} \phi_{e}(p)+\sum_{q \in P_{f}} \phi_{f}(q)} $$

* Locality-sensitive hashing
  * Bucketize all highly similar keyphrases.
  * Group entities together that have sufficiently high overlap in terms of keyphrase bucket identifiers.

> KORE (Nguyen, 2014)

* KORELSH-G , a reasonably fast approximation of KORE which has nearly the same quality as KORE

> Zeroshot (Logeswaran, 19)

* End to end entity linking

## Recommender System

* Information retrieval
* static content base → invect time in indexing content
* dynamic information need → queries presented in real time
* common approach TFIDF → rank documents by term overlap

* Implicit data : purchase | video viewing | click data
* explicit data : star reviews
* candidate generation | filtering | ranking # What are components of Top-N recommender
* Because people have to search for them.    # Why are older movies rated higher?

> Term

* Context Aware
  * User may have different preferences under different contexts
  * Users, items, context and user-item interaction data
  * [+] Incorporating more information and fitting the real-world cases better
  * [-] Data availability and sparsity issue

* Session Based
  * User preference changes along with the corresponding session context
  * [+] Considering the user preference evolution, which fits the real-world cases better
  * [-] Ignoring user’s general and long-term preference

> Metrics

* AB Test
  * Ultimate metric

* Churn
  * How quickly does new user behavior influence your recommendations?

* DCG (Discounted Cumulative Gain)
  * NDCG means Normalized Discounted Cumulative Gain
  * penalize lower rank

$$ DCG_{k}=\sum_{r=1}^{k} \frac{rel_{r}}{\log (r+1)}A $$

* Responsiveness
  * How often do recommendations change?

* Coverage
  * % of <user, item> pairs that can be predicted
  * balance between coverage and accuracy

* Diversity
  * avg similarity between recommendation pairs

* Hit rate
  * hits show users something they found interesting enough to watch on their own already

$$ \frac{hits}{users} $$

* Mean Average Precision

$$ \frac{1}{k} \sum_{i=1}^{k} P_{i}=\frac{1}{k} \sum_{r=1}^{k} r e l_{r} \log \frac{k}{r} $$

* Novelty
  * mean popularity rank of recommended items
  * how popular the items that you are recommending
  * more obscure items that may lead to serendipitous discovery from the users

* Ranking
  * Used in ranking algorithm
  * discontinuous and thus non-differentiable

![alt](images/20210213_232628.png)

> Notation

| notaion          | meaning                           |
| ---------------- | --------------------------------- |
| $\Omega_{j}$     | set of all users who rated item j |
| $r_{i j}$        | rating user i gave item j         |
| $R_{N \times M}$ | user-item rating matrix           |

### Models

> Item | User Vector

* Doesn’t have personalized recommendation

| Term      | Meaning                                            |
| --------- | -------------------------------------------------- |
| $\alpha$  | average                                            |
| $\beta_i$ | Does this item receive higher ratings than average |


* Objective

$$ \arg \min _{\alpha, \beta} \sum_{i, u}\left(\alpha+\beta_{i}+\beta_{u}-R_{u, i}\right)^{2}+\lambda\left[\sum_{i} \beta_{i}^{2}+\sum_{u} \beta_{u}^{2}\right] $$

> Item-item collaborative filtering

![alt](images/20210213_232711.png)

* Good amount of information of items’ own features, rather than using users’ interactions and feedbacks
* Genre, year, director, actor, textual content of articles extracted by applying NLP

> Latent Factor

| Notation    | Meaning                                         |
| ----------- | ----------------------------------------------- |
| $\beta_{u}$ | Does this user give higher ratings than average |
| $I_{u}$     | List of items rated by u                        |
| $U_{i}$     | List of users who rated i                       |

![Latent Factor](images/20210324_142324.png)

* Multiple solutions by permuting $γ_u, γ_i$
* [+] as we add data, latent-factor model automatically discover any useful dimensions
* [-] Cannot use with small datasets → Fix i, u alternatively

> User-User collaborative filtering

![alt](images/20210213_232744.png)

* Select top X similar users, take weighted average of ratings from X users with similarities as weights
* Explicit Rating → a rate given by a user to an item on a sliding scale
* Implicit Rating → indirect users preference, such as page views, clicks, purchase records
* [-] If one user purchases one item, this changes ranking of every other item that was purchased
* [-] No use for new users and new items
* [-] Won't necessarily encourage diverse results

> One-class recommendation

* maximize difference in predictions between positive and negative items


| equation                                                                                                                                                        | meaning                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| $\max \ln \sigma\left(\gamma_{u} \cdot \gamma_{i}-\gamma_{u} \cdot \gamma_{j}\right)$                                                                           | User who likes i and dislikes j            |
| $\sum_{u, i, j}-\ln \left(1+e^{\gamma_{u} \cdot \gamma_{i}-\gamma_{u} \cdot \gamma_{j}}\right)$                                                                 | Objective                                  |
| $-\frac{\left(\gamma_{j k}-\gamma_{i k}\right) e^{\gamma_{u} \cdot \gamma_{j}-\gamma_{u} \cdot \gamma_{i}}}{1+e^{\gamma_{u} \gamma_{j}-\gamma_{u} \gamma_{i}}}$ | $\frac{\delta o b j}{\delta \gamma_{u k}}$ |

## Reinforcement Learning

> Terms

* Tasks

```sh
Episodic Tasks    # Interaction breaks into episodes, which end with a terminal state.
Continuing Tasks  # Interaction goes on continually without terminal state.
```

* Policy
  * Target : One we are learning
  * Behavior : One we are choosing action from

* Generalized policy iteration (GPI)
  * interaction between policy-evaluation and policy improvement

* Planning
  * any process that takes input model, and improves a policy

* Backup Diagram

| Notation | Term                                                                         |
| -------- | ---------------------------------------------------------------------------- |
| K        | Number of actions                                                            |
| t        | Discrete time step                                                           |
| qk(a)    | Expected value of action a                                                   |
| Qt(a)    | Estimate at time t of q*(a)                                                  |
| πt(a)    | Probability of selecting action a at time t                                  |
| ρt       | importance sampling ratio for time t                                         |
| δt       | TD Error at time t Rt+1 γV(St+1) - V(St)                                     |
| d        | dimensionality—the number of components of w                                 |
| v̂(s, w)  | approximate value of state s given weight vector w (Σwixi(s), or neural net) |
| b(a      | s)                                                                           | Behavior policy used to select actions while learning about target policy π |

![](images/20210301_193635.png)

### Model

![Models](images/20210222_225900.png)

* Actor critic

```text
Input:
  Differentiable policy parameterization π(a | s, θ)
  Differentiable state-value function parameterization v̂(s, w)
Initialize:
  R̄ ∈ R to 0
  State-value weights w ∈ Rd and policy parameter θ ∈ Rd (e.g. to 0)
  Algorithm parameters: αw > 0, αθ > 0, αR̄ > 0
  S ∈ S
Loop:
  A ~ π( · | S, θ)
  Take action A, observe S’, R
  δ ← R - R̄ + v̂(S’, w) - v̂(S, w)
  R̄ ← R̄ + αR̄δ
  w ← w + αw δ ∇ v̂(S, w)
  θ ← θ + αθ δ ∇ln π(A | S, θ)
  S ← S’
```

* Dyna

```text
# Q+
Initialize:
  Q(s, a) and Model(s, a) for all s 2 S and a 2 A(s)
Loop forever:
  S ← current (nonterminal) state
  A ← e-greedy(S, Q)
  Take action A: observe resultant reward, R, and state, S'
  Q(S, A) ← Q(S, A) + α [R + γ maxaQ(S', a) - Q(S, A)]
  Model(S, A) ← R, S'
  Loop repeat n times:
    S ← random previously observed state
    A ← random action previously taken in S
    R, S' ← Model(S, A)
    Q(S, A) ← Q(S, A) + α[(R + κτ0.5) + R + γ maxaQ(S', a) - Q(S, A)]
```

* Monte Carlo

```text
# e-soft
Input : a policy π to be evaluated, ε > 0
Initialize:
  π ← an arbitrary ε-soft policy
  Q(s, a) ∈ R (arbitrarily) for all s ∈ S, a ∈ A(s)
  Returns(s, a) ← an empty list, for all s ∈ S, a ∈ A(s).
Loop:
  Generate an episode from S0, A0, following π : S0, A0, R1, …, ST-1, AT-1, RT
  G ← 0
  Loop for each step of episode, t = T - 1, T - 2, ..., 0:
    G ← γG + Rt+1
    Append G to Returns(St, At)
    Q(St, At) ← average(Returns(St, At))
    A* ← argmaxa Q(St, a)
    For all a ∈ A(St):


# Exploring start
Initialize:
  π(s) ∈ A(s)  (arbitrarily), for all s ∈ S.
  Q(s, a) ∈ R (arbitrarily), for all s ∈ S, a ∈ A(s).
  Returns(s, a) ← an empty list, for all s ∈ S, a ∈ A(s).
Loop:
  Choose S0 ∈ S, A0 ∈ A(S0) randomly s.t. all pairs have probability > 0
  Generate an episode from S0, A0, following π : S0, A0, R1, …, ST-1, AT-1, RT
    G ← return that follows the first occurence of s, a
    Append G to Returns(s, a)
    Q(s, a) ← average(Returns(s, a))
    For each s in the episode:
      π(s) ← argmaxa Q(s, a)

# Off-policy
Input:
  an arbitrary target policy π
Initialize, for all s ∈ S, a ∈ A(s):
  Q(s, a) ← arbitrary
  C(s, a) ← 0
Repeat:
  b ← any policy with coverage of π
  Generate an episode using b:
  S0, A0, R1, …, ST - 1, AT - 1, RT, ST
  G ← 0
  W ← 1
  For t = T - 1, T - 2, … down to 0:
    G ← γG + Rt+1
    C(St, At) ← C(St, At) + W
    Q(St, At) ← Q(St, At) + W | C(St, At) [G - Q(St, At)]
    W ← W π(At|St) | b(At|St)
    If W = 0 then exit For loop

# Prediction
Initialize:
  π ← policy to be evaluated
  V ← an arbitrary state-value function
  Returns(s) ← an empty list, for all s ∈ S
Repeat forever:
  Generate an episode using π
  For each state s appearing in the episode:
    G ← the return that follows the first occurrence of s
    Append G to Returns(s)
    V (s) ← average(Returns(s))
```

* Policy Iteration

![](images/20210301_193452.png)

* SARSA

```text
# Differential Semi-G
Initialize state S, and action A
Loop for each step:
  Take action A, observe R, S’
  Choose A’ as a function of q̂(S’, ·, w) (e.g. ε-greedy)
  δ ← R - R̄+ q̂(S’, A’, w) - q̂(S, A, w)
  R̄ ← R̄ + β δ
  w ← w + αδ ∇q̂(S, A, w)
  S ← S’
  A ← A’

# Expected
Loop for each episode:
  Initialize S
  Choose A from S using policy derived from Q (e.g. ε-greedy)
  Loop for each step of episode:
    Take action A, observe R, S’
    Choose A’ from S’ using policy derived Q (e.g. ε-greedy)
    Q(S, A) ← Q(S, A) + α[R + γQ(S’, A’) - Q(S, A)]
    Q(S, A) ← Q(S, A) + α[R + γΣaπ(a | St+1)Q(St+1, a) - Q(St, At)]
    S ← S’; A ← A’;
  until S is terminal
```

* Q Learning

```text
Initialize:
  Q(s, a) = random, for all s ∈ S, a ∈ A(s)
  Q(terminal, *) = 0
Loop:
  Initialize S
  Loop for each step of episode:
    Choose A from S using policy derived from Q (e.g. e-greedy)
    Take action A, observe R, S'
    Q(S, A) ← Q(S, A) + α [R + γ maxa Q(S', a) - Q(S, A)]
    S ← S'
  until S is terminal
```

* Q planning

```text
Loop:
  Select a state, S ∈ S, and an action, a ∈ A(s) at random
  Send s, a to a sample model, and obtain a sample next reward, R, and a sample next state, S'
  Apply one-step tabular Q-learning to S, A, R, S'
    Q(S, A) ← Q(S, A) + α[ R + γmaxaQ(S', a) - Q(S, A)]
```

* TD0

```text
Input:
  policy π to be evaluated, step size α
Initialize:
  V(s), for all s ∈ S+, arbitrarily except that V(terminal) = 0
Loop for each episode:
  Initialize S
  Loop for each step of episode:
    A ← action given by π for S
    Take action A, observer R, S'
    V(S) ← V(S) + α[R + γV(s') - V(S)]
    S ← S'
  until S is terminal

# Semi-Gradient
Loop for each episode:
  Initialize S
  Loop for each step of episode:
    Choose A ~ π(*|S)
    Take action A, observe R, S'
    w ← w + α[R + γ v̂(S', w) - v̂(S, w)] Δv̂(S, w)
    S ← S'
until S is terminal
```

* Policy Iteration

![](images/20210301_193519.png)

## Computer vision

* Extracting descriptions of the world from pictures or sequences of pictures
* ambiguous Interpretations: Changing viewpoint, moving light source, deforming the shape
* forward (graphics) well-posed, inverse (vision)
* Should computer vision follow from our understanding of human vision?

* How to solve
  * craft a solution using established methods and tailor them
  * build a math/physical model of the problem and implement algorithms with provably correct properties
  * gather image data, label it, and use machine learning to provide the solution

> Terms

* Filter

![](images/20210309_010213.png)

* Throughput
  * count / second

* Non maximal suppression

![alt](images/20210213_232105.png)

```text
while select bounding box with some threshold
  discard any remaining box with IoU >= 0.5 with the box output in previous step
```

* background substitution
  * subtract from previous frame

* Noise
  * Impulsive noise randomly pick a pixel and randomly set to a value
  * saturated version is called salt and pepper noise
  * Median filters - completely discard the spike, linear filter always responds to all aspects
  * Quantization effects - often called noise although it is not statistical
  * Unanticipated image structures - also often called noise although it is a real repeatable signal

* Eight point algorithm
  * Set $$ E_33 $$ to 0 and use 8 points to calculate $$ E_11 $$, $$ E_32 $$

$$
[u, v, 1]\left[\begin{array}{ccc}
E_{11} & E_{12} & E_{13} \\
E_{21} & E_{22} & E_{23} \\
E_{31} & E_{32} & E_{33}
\end{array}\right]\left[\begin{array}{c}
u^{\prime} \\
v^{\prime} \\
1
\end{array}\right]=0
$$

* Perspective
  * distant objects appear smaller than nearer objects.
  * lines parallel in nature meet at the point at infinity
  * Most realistic because it’s the same way as photographic lenses and the human eye works.
  * 1/2/3-point, based on the orientation of the projection plane towards the axes of the depicted object

![strong, weak perspective](images/20210322_214730.png)

* Projective geometry
  * provides an elegant means for handling these different situations in a unified way.

* Point at Infinity
  * Where w is 0, with homogeneous coordinates

* Projective plane
  * = Euclidean plane ∪ Line at Infinity

> Features

* Anchor
  * object is assigned to grid cell that contains object's midpoint, anchor box for grid cell with highest IoU

![alt](images/20210213_232016.png)
![alt](images/20210213_231959.png)

* Harris
  * large difference with nearby pixel

* Good Features to Track
  * sorted by value, suppress non-max

* FAST
  * use nearby 16 pixels, fast than above two

* Feature Pyramid

![alt](images/20210213_232138.png)

* viola-jones algorithm (Paul Viola and Michael Jones, 2001)
  * trained to detect a variety of object classes, it was motivated primarily by the problem of face detection
  * [+] robust: high detection rate (true-positive rate) & low false-positive rate always
  * [+] Real time: For practical applications at least 2 frames per second must be processed.
  * Face detection only (not recognition) - The goal is to distinguish faces from non-faces

```text
Haar Feature Selection (eye, nose)
Creating an Integral Image
Adaboost Training
Cascading Classifiers
```

* haar-like features (Rapid Object Detection using a Boosted Cascade of Simple Features, 2001)
  * edge features, line features, four-rectangle features
  * uses integral of image and adaboost (Cascade of Classifiers) for faster computation

* integral
  * integral image enables you to rapidly calculate summations over image subregions

![alt](images/20210213_231506.png)

> Eye

* 1604 Kepler eye as an optical instrument, which image is inverted on retina
* 1625 Scheiner experimented by this idea

* Color is precieved differently by
  * previously seen color
  * neighborhood colors
  * state of mind

* Camera vs Human

![alt](images/20210210_185040.png)

| Camera        | Human              |
| ------------- | ------------------ |
| curved retina | wide range of view |
| hard lense    | soft lense         |

![alt](images/20210210_185112.png)

| rods                   | cones           |
| ---------------------- | --------------- |
| night (a lot of light) | day             |
| many                   | few             |
| one                    | three(color)    |
| low resolution         | high resolution |

> Epipolar

![alt](images/20210214_020403.png)

* Baseline: line connecting two center of projection O and O'
* Epipoles (e, e'): Two intersection points of baseline with image planes
* Epipolar plane: Any plain that contains the baseline
* Epipolar lines: Pair of lines from intersection of an epipolar plane with two image plane

![alt](images/20210210_184754.png)

> Public Datasets

* Coco
  * 80 labels (people, bicycles, cars and trucks, airplanes, stop signs and fire hydrants, animals, kitchens)
  * object detection, segmentation
  * https://gist.github.com/50e1deaec61bbd28b60bb96cb10ab74d

* MOT
  * https://motchallenge.net/results/MOT17

> Shadow

![alt](images/20210214_020943.png)

* hard shadow is generated by point source while soft shadow generated by extended source
* Stereo
  * shape from shading (single image, known direction, known BRDF)
  * Photometric stereo (single viewpoint, multiple images under different lighting)
* Multi-view stereo
  * Multiple images, dynamic scene, multiple viewpoints, fixed lighting, correspondence hard

> CNN

* Pixel depend on nearby pixels(locality)             # small receptive fields
* Statistics of visual inputs are invariant across image     # replicate receptive fields across images
* Objects don't change based on location             # translation invariance, spatial pooling
* Objects are made of parts                     # get larger in the net

* convolutional layer of replicated feature maps
* Depth allows features of features to be learned which tend to get more abstract in deeper layers
* Deeper networks are better as long as they allow the gradient to pass backwards easily
* Reuse a pre-trained network and then add a softmax for categorization or logistic units for tagging

$$
W_{\text {out }}=\text { floor }\left(\frac{W_{\text {in }}+2 \times \text { padding }-\text { dilation } \times(k-1)-1}{\text { stride }}\right)+1
$$

> Mixture of Gaussian (improved adaptive gaussian mixture model for background subtraction, 2004)

* Moving average
* Save memory
  * $$ \alpha $$ weight for current frame (0.01)

$$ B(x, y, t)=\alpha \cdot I(x, y, t)+(1-\alpha) \cdot B(x, y, t-1) $$

### Colors

* gray
  * 0 Black - 255 White
  * 1Byte → unsigned char in c++, numpy.uint8 in python

* HSL, HSV

* YUV 4:2:0
  * This format requires 4×8+8+8=48 bits per 4 pixels, so its depth is 12 bits per pixel
  * I420 is by far the most common format in VLC.

* NV12
  * commonly found as the native format from various machine vision, and other, video cameras
  * another variant where colour information is stored at a lower resolution than the intensity data
  * intensity (Y) data is stored as 8 bit samples, and colour (Cr, Cb) information as 2x2 subsampled image, known as 4:2:0.

* I420
  * identical to YV12 except that the U and V plane order is reversed

### Sensor

* Digital Cameras
  * Photons hit a detector the detector becomes charged the charge is read out as brightness

* CCD (charge-coupled device)
  * High sensitivity/power
  * Cannot be individually addressed
  * Blooming

* CMOS (Complementary metal–oxide–semiconductor)
  * Lower sensitivity/power
  * Can be individually addressed
  * Simple to fabricate (cheap)
  * The vast majority of camera

> proprioceptive Sensor

* measure values internal to the robot (motor speed, robot arm joint angles, battery)

* Accelerometer
  * device that measures all external forces acting upon it
  * Modern accelerometers are MEMS deflection measured via capacitive or piezoelectric effects
* Compass
  * absolute encoders and incremental encoders
* Encoder
  * absolute encoders and incremental encoders

* Inertia measurement unit
  * uses gyroscopes and accelerometers to estimate the relative pos, ori, vel, and accel of a robot

![](images/20210304_003757.png)

* Gyroscope
  * heading sensor that preserves its orientation relative to a fixed reference frame
  * Provides an absolute measurement for heading of a robot
  * mechanical and optical gyroscope

> Exteroceptive Sensor

* acquire information about the environment (distance measurements, light intensity)

* IR sensors
  * linear camera
* Laser rangefinders
  * emits a laser beam to detect the distance to an object
* Satellite-based sensors / GPS
  * These are a type of beacon which are signalling devices with precise known positions.
* Sonar
  * emits an ultrasonic wave to measure the time of flight from the robot location to an obstacle
* Structured light
  * structured light using CCDs and CMOS
  * a light is emitted and the reflection is captured by the CCDs and CMOS
* Tactile
  * detect objects in the environment upon contacting them
* Visual sensors
  * single monocular, stereo camera, 360 cameras
  * features are detected in the image with filtering algorithms applied on the image signal

### Robotics

> Motion planning

* the ability for an agent to compute its own motions in order to achieve high-level goals

* Kinematic Solution
  * Compute the sequence of translation/rotations that achieve this
  * Come up with another one that respects the mechanical limitations of the robot
* Dynamic Solution
  * Compute controls (e.g. thrusts) that make the robot follow the path
  * must pay attention to velocity control

> Map

* Where am I in the world? (localization)
  * Assumes perfect map
  * Computes location relative to map

* What is the world around me? (coverage and mapping)
  * Assumes perfectly known position of robot
  * Creates a map of the environment
  * The combined problem is called SLAM

* Deterministic
  * Sense a bit → Plan → Move a bit
  * Bug algorithm, simple algorithms for point robots
  * Roadmaps and planning over graphs for points robot
  * Configuration spaces : planning for more sophisticated robots
  * Free configuration space representations
  * Sampling Based Planning

* Probabilistic
  * Maintain probabilistic hypotheses about the environment
  * Recursive estimation, histogram filters
  * Probabilistic motion models
  * Sensor measurement models
  * Simple particle filters

### Tasks

* Video classification
* Activity recognition
* Activity detection
* Video segmentation

| Stage                   | Example                                              | Buffering                                             | Latency (1080p30) |
| ----------------------- | ---------------------------------------------------- | ----------------------------------------------------- | ----------------- |
| Capture Post-processing | Bayer Filter <br/> chroma resampling                 | few lines (eg. 8)                                     | < 0.5ms           |
| Video Compression       | Motion Jpeg, MPEG-1/2/4 <br/> H.264 with single-pass | 8 lines <br/> few thousand pixels on encoder piepline | 0.25ms            |
| Network Processing      | RTP / UDP / IP encapsualtion                         | A few Kbytes                                          | < 0.01ms          |
| Decoder Stream Buffer   | From number of frames (more than 30)                 | 16-1 ms                                               |
| Decompression           | Motion Jpeg, MPEG-1/2/4 <br/> H.264 with single-pass | 8 lines <br/> few thousand pixels on encoder piepline | 0.25ms            |
| Display Pre-processinsg | Scaling, Chroma Resampling                           | Few lines (e.g. 8)                                    | < 0.5ms           |

> Random Sample Consensus

* estimating parameters of models in the presence of outlier data points

```text
repeat n times:
  select two points at random
  determine line equation from two points count number of points that are within distance τ from line
  (called support of line which is # of inliers)
  line with the greatest support wins
```

> Autmonomous vehicle

* Driving task
  * Perceiving the environment
  * Planning how to reach from point A to B
* Controlling the vehicle
  * Operational Design Domain / Environmental
  * Time of day

* Lateral Control steering
* Longitudinal control braking accelerating
* Object and Event Detection and Response detection, reaction
* Inertial measurement unit
  * Measures a vehicle’s three linear acceleration and rotational rate components

* Level of automation
  * 1: Assistance either, but not both longitudinal control or lateral (e.g. cruise, lane keeping)
  * 2: Both longitudinal control and lateral
  * 3: Includes automated object and event detection and response. Alert in case of failure.
  * 4: Can handle emergencies autonomously.
  * 5: Unlimited ODD

* Perception
  * Static objects
  * Dynamic objects
  * Ego localization

* Planning
  * Predictive : Make predictions about other vehicles and how they are moving
  * Rule based : Take into account the current state of ego and other objects and give decisions
  * Long term : How to navigate from NY to LA?
  * Short Term : Can I change my lane to lane right? Can I pass this intersection and join the left road?
  * Immediate : Accelerate, brake

> Segmentation

![alt](images/20210210_190100.png)

* mask-RCNN (Mask R-CNN, He 2017)
  * Faster R-CNN + FCN

![alt](images/20210210_190110.png)

* Single short multibox detector
  * 74.3 mAP, 59 FPS

* Faster R-CNN
  * 73.2 mAP, 7 FPS

* Darknet
  * 19 convolutional layers and 5 maxpooling layers

* Tiny Yolo
  * 23.7mAP, 244FPS

* YOLO1
  * 74.3mAP, 59FPS
  * 49 objects / Relatively high localization error

* Yolo v2
  * Classification and prediction in a single framework
  * Batch Normalization
  * classiﬁer network at 224×224, Increase in image size 448*448
  * divides into 13 * 13 grid cells → finegrand feature
  * Multi-scale training
  * Anchor boxes

* Yolo v3 (J Redmon, 2018)
  * 0 normalized 416 (320, 608) RGB input → [(507, 85), (2028, 85), (8112, 85)]

![alt](images/20210210_190347.png)

### Graphics

> Terms

* Interactive
  * Produces images within milliseconds.
  * Using specialized hardware, graphic processing units.
  * Standardized APIs (OpenGL, DriectX, Vulkan)
  * Tries to be as photorealistic as possible.
  * Hard shadows, only single bounce of light.
  * Used in games, technical design.

> Rendering

* Synthesis of a 2D image from a 3D scene description
* 2D image is an array of pixels
* Algorithm interprets data structures that represent scene in terms of geometric primitives, textures, and lights
* Objective / Interactive

> Photorealistic

* Physically-based simulation of light, camera Shadows, global illumination, multiple bounces of light
* Slow, used in movies, animation

> Light

* Quadratic attenuation
  * Most computationally expensive, most physically correct
$$ k*(p-v)^2 $$
* Linear attenuation
  * Less expensive, less accurate
$$ k*(p-v) $$
* Constant attenuation
  * Fastest computation, least accurate
    $$ k $$

### OpenGL

* Open Graphics Library
* Render 3D graphics efficiently
* Cross-language and cross-platform.
* Extension Wrangler Library
* High-quality color images composed of geometric and image primitives.
* Window / Operating system independent.

> Terms

* Shader
  * shaders are small programs that rest on the GPU.
  * These programs are run for each specific section of the graphics pipeline.
  * In a basic sense, shaders are nothing more than programs transforming inputs to outputs
  * Shaders are also isolated programs in that they're not allowed to communicate with each other
  * the only communication they have is via their inputs and outputs.

* GLU
  * part of OpenGL that supports more complex shapesL
