
# coding: utf-8

# In[17]:


import numpy as np
from math import exp


# In[18]:


#para redes linearmente separáveis 
def step_function(soma):

    if soma >= 1:
        return 1
    else:
        return 0
    
    


# ## Exemplo step function:
# 
# ![imagem](https://www.intmath.com/laplace-transformation/svg/svgphp-unit-step-functions-definition-1a-s0.svg)

# In[34]:


#ideal para classificações binárias
def sig_function(soma):
    
    return (1/(1+exp(-soma)))




# ## Exemplo sigmoid function:
# ![imagem](https://qph.fs.quoracdn.net/main-qimg-07066668c05a556f1ff25040414a32b7)

# In[22]:


#ideal para classificações binárias
def hyperbolic_tanget_function(soma):
    
    return ((exp(soma)-exp(-soma))/(exp(soma)-exp(-soma)))



# ## Exemplo hyperbolic function:
# ![imagem](http://mathworld.wolfram.com/images/interactive/TanhReal.gif)

# In[33]:


#função mais utilizada nas CNNs 
def RelU(soma):
    if soma >= 0:
        return soma
    else:
        return 0


# ## Exemplo RelU function:
# ![imagem](https://i.imgur.com/gKA4kA9.jpg)

# In[32]:


#nao muda os valores das somas(não faz nada)
def linear_function(soma):
    return soma
    


# ## Exemplo Linear function:
# ![imagem](https://d2gne97vdumgn3.cloudfront.net/api/file/WyB4Ik0S0CAE1fXAnzB5)
# 
# 

# In[45]:


#indicado para problemas com mais de uma classe(multiclass)
def softmax_function(x):
    
    exponencial = np.exp(x)
    return exponencial/exponencial.sum()

