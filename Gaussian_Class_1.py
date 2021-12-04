# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:01:25 2021

@author: madhawa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.api as sm
import os

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn import linear_model


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.naive_bayes import ComplementNB
#from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import metrics

from sklearn.decomposition import PCA


def NB_Classifires(X_train, X_test, y_train, y_test):
    
    clf_GNB = GaussianNB()
    clf_GNB.fit(X_train, y_train)
    y_pred = clf_GNB.predict(X_test) 
    M = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = M.ravel()  
    print ("Accuracy GNB ==1================= :",metrics.accuracy_score(y_test, y_pred))
    NB_Acc =metrics.accuracy_score(y_test, y_pred)
    
    clf_DT = tree.DecisionTreeClassifier(criterion="entropy", max_depth=5)
    clf_DT.fit(X_train, y_train)
    y_pred= clf_DT.predict(X_test)
    M = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = M.ravel() 
    print ("Accuracy DT  ==================== :", metrics.accuracy_score(y_test, y_pred))
    DT_Acc =metrics.accuracy_score(y_test, y_pred)
    
    
    clf_SVM = svm.SVC(kernel='linear') # Linear Kernel
    clf_SVM.fit(X_train, y_train)
    y_pred = clf_SVM.predict(X_test)
    M = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = M.ravel() 
    print ("Accuracy SVM ==================== :", metrics.accuracy_score(y_test, y_pred))
    SVM_Acc =metrics.accuracy_score(y_test, y_pred)
    
    
    clf_NB_DT = VotingClassifier(estimators=[('GNB', clf_GNB), ('DT', clf_DT)],voting='soft', weights=[2, 1])
    clf_NB_DT.fit(X_train, y_train)
    y_pred= clf_NB_DT.predict(X_test)
    M = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = M.ravel() 
    print ("Accuracy Voting (GNB + DT)======= :", metrics.accuracy_score(y_test, y_pred))
    NBDT_Acc   =metrics.accuracy_score(y_test, y_pred)



    clf_SVM_DT = VotingClassifier(estimators=[ ('SVM', clf_SVM), ('DT', clf_DT)], voting='hard')
    clf_SVM_DT.fit(X_train, y_train)
    y_pred= clf_SVM_DT.predict(X_test)
    M = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = M.ravel()   
    print ("Accuracy Voting (SVM + DT )====== :", metrics.accuracy_score(y_test, y_pred))
    DTSVM_Acc    =metrics.accuracy_score(y_test, y_pred) 

    clf_NB_SVM = VotingClassifier(estimators=[ ('SVM', clf_SVM), ('GNB', clf_GNB)], voting='hard')
    clf_NB_SVM.fit(X_train, y_train)
    y_pred= clf_NB_SVM.predict(X_test)
    M = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = M.ravel()   
    print ("Accuracy Voting (SVM + GNB)====== :", metrics.accuracy_score(y_test, y_pred))
    SVMNB_Acc     =metrics.accuracy_score(y_test, y_pred)
 
#    SVM_Acc   = 1.000
#    DTSVM_Acc = 2.000 
#    SVMNB_Acc = 3.000 
    
    ACCURACY_01 = [round(NB_Acc,4),round(DT_Acc,4),round(SVM_Acc,4),round(NBDT_Acc,4),round(DTSVM_Acc,4) ,round(SVMNB_Acc,4) ]
    
    return ([round(NB_Acc,4),round(DT_Acc,4),round(SVM_Acc,4),round(NBDT_Acc,4),round(DTSVM_Acc,4) ,round(SVMNB_Acc,4) ])
    # plotting the confusion matrix


