#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np


# Function to calculate next predicted state:

# In[24]:


# All arguments must be type np.array
def nextPredictState(A, Xkp_prev, B, uk, wk):
    Xkp = A.dot(Xkp_prev) + B.dot(uk) + wk
    return Xkp


# Function to calculate process covariance matrix:

# In[25]:


# All arguments must be type np.array
def predictProcCovar(A, Pkp_prev, QR):
    Pkp = A.dot(Pkp_prev).dot(np.transpose(A)) + QR
    return Pkp


# Function to calculate Kalman Gain:

# In[26]:


# All arguments must be type np.array
def kalmanGain(Pkp, H, R):
    K_top = Pkp.dot(np.transpose(H))
    K_bottom = H.dot(Pkp).dot(np.transpose(H)) + R
    # Perform array division, element-wise.
    K = np.divide(K_top, K_bottom)
    return K


# Function to calculate new measurements to incorporate:

# In[27]:


# All arguments must be type np.array
def newMeas(C, Ykm, ZR):
    Yk = C.dot(Ykm) + ZR
    return Yk


# Filter equation - calculate new current state, combining estimate and measurements:

# In[ ]:


# All arguments must be type np.array
def filterEqn(Xkp, K, Yk, H):
    Xk = Xkp + K.dot(Yk - H.dot(Xkp))
    return Xk


# Function to update process covariance matrix:

# In[28]:


# All arguments must be type np.array
def updateProcCovar(I, K, H, Pkp):
    Pk = (I - K.dot(H)).dot(Pkp)
    return Pk

