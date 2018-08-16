
# coding: utf-8

# In[1]:

name="superman"
name = "mu"
age = 99


# In[2]:


print(age)


# In[3]:


print(name)


# In[7]:


print(age);


# In[11]:


print("my name is")


# In[13]:


print("my name is",name)


# In[14]:


print("abc")


# In[15]:


print("sdf")


# In[16]:


print("my name is",name, "and my age is",age)


# In[17]:


clear


# In[18]:


newage = age - 50


# In[19]:


print("newage
      ")


# In[20]:


print("newage")


# In[21]:


print(newage)


# In[22]:


newage=age-5


# In[23]:


print(newage)


# In[24]:


newage=age*2


# In[25]:


print(newage)


# In[26]:


sequence="CTAGCTAGaaaaa"


# In[27]:


print(sequence)


# In[28]:


print(sequence)


# In[29]:


print(sequence(0))


# In[30]:


print(sequence[0])


# In[31]:


print(sequence[0-3])


# In[32]:


print(sequence[0:3])


# In[33]:


print(sequence[3])


# In[34]:


print(sequence[1:4])


# In[35]:


len(sequence)


# In[36]:


sequence(0:3)


# In[37]:


sequence(0)


# In[38]:


sequence[0:3]


# In[39]:


sequence[1:3]


# In[40]:


type(sequence)


# In[41]:


type(age)


# In[42]:


COX2='TACG'


# In[43]:


COX1="CTAG"


# In[44]:


COX1-COX2


# In[45]:


COX1+COX2


# In[46]:


firstname="aanuj"


# In[47]:


lastname="guru"


# In[48]:


firstname+lastname


# In[49]:


firstname+" "+lastname


# In[50]:


len(age)


# In[51]:


name+age


# In[52]:


print(name, "is",age)


# In[53]:


5^2


# In[54]:


5**2


# In[55]:


5/2


# In[56]:


5/3


# In[57]:


5%2


# In[58]:


6%3


# In[59]:


7%5


# In[60]:


8%5


# In[61]:


9%5


# In[62]:


10%5


# In[63]:


#this is a comment


# In[64]:


test=(1,2,3,4,5)


# In[65]:


test


# In[66]:


test(2)


# In[67]:


test=[1,2,3,4,5]


# In[68]:


test


# In[69]:


test(2)


# In[70]:


test[2]


# In[71]:


test=(1,2,3,4)


# In[72]:


test[2]


# In[73]:


max(test)


# In[74]:


min(test)


# In[75]:


sum(test)


# In[76]:


average(test)


# In[77]:


mean(test)


# In[78]:


round(3.1415926)


# In[79]:


round(4.8)


# In[80]:


round(3.14159,2)


# In[81]:


round(3.14159,3)


# In[82]:


test=[21,32,45]


# In[83]:


test


# In[84]:


max(test)+min(min)


# In[85]:


max(test)


# In[86]:


min(test)


# In[87]:


max(test)+min(test)


# In[88]:


hundred_C="c"*100


# In[89]:


hundred_C


# In[90]:


COX1


# In[91]:


COX1+hundred_C


# In[92]:


len(hundred_C)


# In[93]:


len(COX1+hundred_C)


# In[94]:


import math


# In[95]:


math.cos(180)


# In[96]:


math.sin(30)


# In[97]:


math.sin(90)


# In[98]:


round(math.sin(90),2)


# In[99]:


math.pi


# In[100]:


math.e


# In[101]:


help(math)


# In[102]:


log(10)


# In[103]:


math.log(100)


# In[104]:


math.log2(8)


# In[105]:


from math import cos


# In[106]:


cos(1)


# In[107]:


import math as m


# In[108]:


m.cos(1)


# In[109]:


import(math)


# In[110]:


import math


# In[111]:


from math import sin,pi


# In[112]:


print("sin(pi/2) =",sin(pi/2))


# In[113]:


sin(pi/3)


# In[114]:


sin(pi/2)


# In[115]:


sin(pi/6)


# In[116]:


2*sin(pi/4)


# In[117]:


sin(pi)


# In[118]:


sin(2*pi)


# In[119]:


from math import *


# In[120]:


angle = degrees(pi / 2)
print(angle)


# In[121]:


import pandas


# In[122]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[123]:


pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[124]:


data=pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[125]:


data(1,:)


# In[126]:


print(data)


# In[127]:


data=pandas.read_csv("data/gapminder_gdp_americas.csv", index_col="country")


# In[128]:


data


# In[129]:


data.info()


# In[130]:


data.T


# In[131]:


data.describe


# In[132]:


data.describe()


# In[133]:


americas=pandas.read_csv(gapminder_gdp_americas.csv)


# In[134]:


americas=pandas.read_csv(data/gapminder_gdp_americas.csv)


# In[135]:


americas=pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[136]:


data.describe()


# In[137]:


data.describe(americas)


# In[138]:


data.describe --help


# In[139]:


data.describe()


# In[140]:


data.T.describe


# In[141]:


americas.describe()


# In[142]:


americas.columns


# In[143]:


americas.rows


# In[144]:


data.{loc[1,2]}


# In[145]:


data.iloc[1,2]


# In[146]:


data


# In[147]:


data.loc["Haiti,:"]


# In[148]:


data.loc["Haiti",:]


# In[149]:


data.loc[:,"gdpPercap_1957"]


# In[150]:


data.loc["Haiti","gdpPercap_1952":"gdpPercap_1962"]


# In[151]:


help pandas


# In[152]:


help(pandas)


# In[153]:


subset=data.loc[:,"gdpPercap_1957"]


# In[154]:


print(subset>11000)


# In[155]:


subset[subset>11000]


# In[156]:


subset[subset>11000].describe()


# In[161]:


Europe=pandas.read_csv("data/gapminder_gdp_europe.csv",index_col="country")


# In[162]:


Europe


# In[163]:


Europe.loc["Serbia","gdpPercap_2007"]


# In[164]:


dataset=Europe.loc["Italy":"Norway","gdpPercap_1962":"gdpPercap_1972"]


# In[165]:


dataset[dataset<15000].describe()


# In[166]:


dataset<15000

