# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 08:07:30 2021

@author: madhawa
"""

# =============================================================================================
""" This module is toload the Data Set and 

 """ 
# ===============================================================================================


import numpy as np
import pandas as pd


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn import linear_model


from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif

def Anova_Feature_selction (df,Ratio,No_of_Variable):
    X = df.iloc[:,1:-1]  #independent columns
    y = df.iloc[:,-1]    #target column i.e price range
#    print("x----\n\n",X.head())
#    print("y----\n\n",y.head())
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Ratio, random_state=0)

    bestfeatures = SelectKBest(score_func=f_classif, k=No_of_Variable)
    fit = bestfeatures.fit(X_train,y_train)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(X_train.columns)
    #concat two dataframes for better visualization 
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    featureScores.columns = ['Specs','Score']  #naming the dataframe columns
    return (featureScores.nlargest(No_of_Variable,'Score'))  #print 10 best features


def Chi_Feature_selction (df,Ratio,No_of_Variable):
    X = df.iloc[:,1:-1]  #independent columns
    y = df.iloc[:,-1]    #target column i.e price range
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Ratio, random_state=0)

    bestfeatures = SelectKBest(score_func=chi2, k=No_of_Variable)
    fit = bestfeatures.fit(X_train,y_train)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(X_train.columns)
    #concat two dataframes for better visualization 
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    featureScores.columns = ['Specs','Score']  #naming the dataframe columns
    df=featureScores.nlargest(No_of_Variable,'Score')
    df=df[df.Specs != "churn"]
    print ("*****************************************\n",df)
    return (df)  #print 10 best features

