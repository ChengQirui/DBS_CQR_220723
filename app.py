#!/usr/bin/env python
# coding: utf-8

# In[11]:


from flask import Flask, request, render_template
import joblib


# In[12]:


app = Flask(__name__)


# In[6]:


'''model0 = joblib.load('LinearRegression')
model1 = joblib.load('DecisionTree')
model2 = joblib.load('GradientBoosting')
model3 = joblib.load('RandomForest')'''


# In[ ]:


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model0 = joblib.load('LinearRegression')
        r0 = model0.predict([[rates]])
        model1 = joblib.load('DecisionTree')
        r1 = model1.predict([[rates]])
        model2 = joblib.load('GradientBoosting')
        r2 = model2.predict([[rates]])
        model3 = joblib.load('RandomForest')
        r3 = model3.predict([[rates]])
        return(render_template("index.html", result0 = r0, result1 = r1, result2 = r2, result3 = r3))
    else:
        return(render_template("index.html", result0 = "WAITING", result3 = "WAITING"result1 = "WAITING", result2 = "WAITING"))


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




