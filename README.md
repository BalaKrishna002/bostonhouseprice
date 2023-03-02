## Boston House Price Prediction

### Software and Tool Requirements

1. [Github Account](https://github.com/)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Render Account](https://render.com)
4. [GitCLI](https://git-scm.com/)

Create a new environment

```
conda create -p venv python==3.7 -y
```
## DataSet
Boston house prices dataset
---------------------------

**Data Set Characteristics:**  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

    :Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's
**Dataset can be download from [UCI repositeroy](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/)**
**or can be used from scikit-learn library datasets**
```
from sklearn.datasets import load_boston
boston = load_boston()
dataset = pd.DataFrame(boston.data,columns=boston.feature_names)
dataset["Price"]=boston.target
```


## Website link
```
https://house-price-prediction-dilh.onrender.com
```
