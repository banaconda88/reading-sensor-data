#!/usr/bin/env python
# coding: utf-8

# In[2]:


file = open("sensordata.txt")
data = file.read().split()


# In[18]:


final = []
for d in data:
    if int(d) >= 200 or int(d)<= -200:
        continue
    else:
        final.append(int(d))
print(final)
a = sum(final)/len(final)
print(a)
final = []
for d in data:
    if int(d) > a or int(d)<= -200:
        continue
    else:
        final.append(int(d))
print("The number of numbers above the average is", len(final))
final = []
for d in data:
    if int(d) >= 200 or int(d) < a:
        continue
    else:
        final.append(int(d))
print("The number of number below the average is", len(final))

