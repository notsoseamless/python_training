
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.5** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 3 - More Pandas
# This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%)
# Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, 
# 
# e.g. 
# 
# `'Bolivia (Plurinational State of)'` should be `'Bolivia'`, 
# 
# `'Switzerland17'` should be `'Switzerland'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[24]:

import pandas as pd
import numpy as np
 

#def get_dataframes():




def answer_one():
    # get energy data from Energy Indicators.xl
    energy_excel_file = pd.ExcelFile('Energy Indicators.xls')
    energy = energy_excel_file.parse('Energy')
    # get rid of first two columns
    energy = energy.drop('Unnamed: 0', 1)
    energy = energy.drop('Unnamed: 1', 1)
    # get rid of footer
    energy = energy.drop(energy.index[243:])
    # get rid of header
    energy = energy.drop(energy.index[0:16])    
    # change the column labels
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    # For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
    energy = energy.replace('...', np.NaN)   
    # Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). 
    gj = 1000000
    energy['Energy Supply'] = energy['Energy Supply'].apply(lambda x: x*gj)
    # Rename list of countries (for use in later questions):
    energy = energy.replace('Republic of Korea', 'South Korea')
    energy = energy.replace("United States of America", "United States")
    energy = energy.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy = energy.replace("China, Hong Kong Special Administrative Region", "Hong Kong")
    energy = energy.replace("China2", "China") 
    energy = energy.replace('Bolivia (Plurinational State of)', 'Bolivia')
    energy = energy.replace('Switzerland17', 'Switzerland')
    energy = energy.replace('Japan10', 'Japan')
    energy = energy.replace('France6', 'France')
    energy = energy.replace('Italy9', 'Italy')
    energy = energy.replace('Spain16', 'Spain')
    energy = energy.replace('Iran (Islamic Republic of)', 'Iran')
    energy = energy.replace('Australia1', 'Australia')
    energy = energy.replace('United States of America20', 'United States')
    energy = energy.replace('Switzerland17', 'Switzerland')
    energy = energy.replace('United Kingdom of Great Britain and Northern Ireland19', 'United Kingdom')
    
    
    # get GDP data from the file world_bank.csv
    GDP = pd.read_csv('world_bank.csv')
    # get rid of footer
    #GDP = GDP.drop(df_GDP.index[243:])
    # get rid of header
    GDP = GDP.drop(GDP.index[0:4])  
    # rename list of countries:
    GDP = GDP.replace("Korea, Rep.", "South Korea") 
    GDP = GDP.replace("Iran, Islamic Rep.", "Iran")
    GDP = GDP.replace("Hong Kong SAR, China", "Hong Kong")   
    # Use only the last 10 years (2006-2015) of GDP data, and rid other unwanted columbs 
    GDP = GDP.drop(GDP.ix[:,'Unnamed: 2':'Unnamed: 49'].head(0).columns, axis=1)
    GDP = GDP.drop('World Development Indicators', 1)

    # change the column labels
    GDP.columns = ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    
    # get the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology
    ScimEn_excel_file = pd.ExcelFile('scimagojr-3.xlsx')
    ScimEn = ScimEn_excel_file.parse('Sheet1')   
    
    # Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). 
    df = pd.merge(ScimEn, energy, on = ['Country'])
    df = pd.merge(df, GDP, on = ['Country'])
    df = df.set_index('Country')
    # use only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).  
    df = df[df.Rank < 16]
   
    #return ScimEn
    #return energy
    #return GDP
    return df
    
    #get_dataframes()


    
    
    
    

#answer_one()







# ### Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[2]:

get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[82]:


import numpy as np

def get_dataframes():
    # get energy data from Energy Indicators.xl
    energy_excel_file = pd.ExcelFile('Energy Indicators.xls')
    energy = energy_excel_file.parse('Energy')
    # get rid of first two columns
    energy = energy.drop('Unnamed: 0', 1)
    energy = energy.drop('Unnamed: 1', 1)
    # get rid of footer
    energy = energy.drop(energy.index[243:])
    # get rid of header
    energy = energy.drop(energy.index[0:16])    
    # change the column labels
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    # For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
    energy = energy.replace('...', np.NaN)   
    # Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). 
    gj = 1000000
    energy['Energy Supply'] = energy['Energy Supply'].apply(lambda x: x*gj)

    #note that column C has the country names with footnote numbers while column B has no footnotes
    # if you read the C column in 1 then remove any digits in the country column   
    energy['Country'] = energy['Country'].str.strip('0123456789')    
    
    # Rename list of countries (for use in later questions):    
    energy = energy.replace('Republic of Korea', 'South Korea')
    energy = energy.replace("United States of America", "United States")
    energy = energy.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy = energy.replace("China, Hong Kong Special Administrative Region", "Hong Kong")   
         
    # remove the part ' (...)' form all countries that have paranthesis, make 
    # sure the result has no trailing space
    energy['Country'] = energy['Country'].str.replace(r"\(.*\)","")    
    energy['Country'] = energy['Country'].str.strip()    
        
    # get GDP data from the file world_bank.csv
    GDP = pd.read_csv('world_bank.csv')
    # get rid of header
    GDP = GDP.drop(GDP.index[0:4])
    GDP = GDP.drop(GDP.ix[:,'Unnamed: 2':'Unnamed: 49'].head(0).columns, axis=1)
    GDP = GDP.drop('World Development Indicators', 1)
    # change the column labels
    GDP.columns = ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']    

    GDP = GDP.replace("Korea, Rep.", "South Korea")
    GDP = GDP.replace("Iran, Islamic Rep.", "Iran")
    GDP = GDP.replace("Hong Kong SAR, China", "Hong Kong")
    
    # get the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology
    ScimEn_excel_file = pd.ExcelFile('scimagojr-3.xlsx')
    ScimEn = ScimEn_excel_file.parse('Sheet1')

    return energy, GDP, ScimEn 



def answer_two():    
    Energy, GDP, ScimEn = get_dataframes()   
    # outer
    outer = pd.merge(Energy, ScimEn, how='outer', on = ['Country'])
    outer = pd.merge(outer,  GDP,    how='outer', on = ['Country'])
    # inner
    inner = pd.merge(ScimEn, Energy, how='inner', on = ['Country'])
    inner = pd.merge(inner,  GDP,    how='inner', on = ['Country'])

    #return 153
    return len(outer) - len(inner)


answer_two()



# <br>
# 
# Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[4]:

def answer_three():
    Top15 = answer_one()    
    avgGDP = Top15[["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]].mean(axis=1)
    return avgGDP

answer_three()


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[5]:

def answer_four():
    Top15 = answer_one()
    
    # from answer three, sort and get 6th largest
    sixth = answer_three().sort_values(ascending=False).index[5]
    
    # find how much the GDP changed over the 10 year span
    return Top15.loc[sixth, '2015'] - Top15.loc[sixth, '2006']


answer_four()


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[6]:

def answer_five():
    Top15 = answer_one()    
    meanEnergy = Top15['Energy Supply per Capita'].mean(axis=0)
    #meanEnergy = Top15['Energy Supply per Capita']
    return meanEnergy

answer_five()


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[7]:

def answer_six():
    Top15 = answer_one()
    ren = [Top15['% Renewable'].sort_values(ascending=False).index[0], Top15['% Renewable'].sort_values(ascending=False)[0]]  
    return tuple(ren)

answer_six()


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[8]:

def answer_seven():
    Top15 = answer_one()
    ratio = Top15[['Self-citations', 'Citations']]
    ratio['Ratio'] = ratio['Self-citations'] / ratio['Citations'] 
    ratio = (ratio['Ratio'].sort_values(ascending=False).index[0] , ratio['Ratio'].sort_values(ascending=False)[0] )
    return tuple(ratio)

answer_seven()


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[9]:

def answer_eight():
    Top15 = answer_one()
    Top15['Est_Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15 = Top15['Est_Population'].sort_values(ascending=False).index[2]
    
    
    return Top15

answer_eight()


# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[10]:

def answer_nine():
    Top15 = answer_one()
    
    # Create Population Estimate from Energy Supply / Energy Supply per Capita: 
    Top15['Population Estimate'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita'] 
    
    # Create Documents per Capita from  Citable documents and Population Estimate
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['Population Estimate'] 

    # Perform pearson correlation
    Top15 = Top15['Energy Supply per Capita'].corr(Top15['Citable docs per Capita'])
    
    return Top15


answer_nine()


# In[11]:

def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[12]:

#plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[13]:

def answer_ten():
    Top15 = answer_one()
    
    # get the median % Renewable value for all countries in the top 15
    median = Top15['% Renewable'].mean(axis=0)

    Top15['Median'] = np.where(Top15['% Renewable'] > median, 1, 0)
    
    #return median
    HighRenew = Top15[['% Renewable', 'Median']]
    
    HighRenew =  (HighRenew.sort_values(by= '% Renewable', ascending=False))
    return HighRenew['% Renewable']

answer_ten()


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[14]:

import pandas as pd
import numpy as np


def answer_eleven():
    Top15 = answer_one()
    
    # get population estimate like before
    Top15['Est_Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    
    # reset index so we can use Counrty
    Top15 = Top15.reset_index()
    
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}  
    # this with help from forums:    
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Continent_Populations = Top15.set_index('Continent').groupby(level=0)['Est_Population'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    Continent_Populations = Continent_Populations[['size', 'sum', 'mean', 'std']]
    return Continent_Populations


answer_eleven()


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[15]:

import pandas as pd
import numpy as np


def answer_twelve():
    Top15 = answer_one()
    
    # reset index so we can use Counrty
    Top15 = Top15.reset_index()
    
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}    

    # this with help from forums:    
    Top15['% Renewable'] = [ContinentDict[country] for country in Top15['Country']]
    #MultiIndex_of_Continents = Top15.set_index('Continent').groupby(level=0)['Est_Population'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    #MultiIndex_of_Continents = MultiIndex_of_Continents[['size', 'sum', 'mean', 'std']]
    
#    return MultiIndex_of_Continents
    return Top15




answer_twelve()


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[16]:

import pandas as pd
import numpy as np
import locale

def answer_thirteen():
    Top15 = answer_one()
    
    # get population estimate like before
    Top15['Est_Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    #Top15['Est_Population'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype(float)
    
    #locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    # sz = "{:0,}".format(1.2345)

    map_str = []
    for num in Top15['Est_Population']:
        #"{0:,f}".format(num)
        map_str.append(locale.format('%.7f', num, grouping=True).rstrip('0').rstrip('.'))
        #map_str.append(locale.format('%,F', num, grouping=True))
        #map_str = "{:0,}".format(map_str)
        
    Top15['Est_Population_str'] = map_str  


    return Top15['Est_Population_str']  
    
answer_thirteen()

# 1,367,645,161.2903225


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[17]:

def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[18]:

#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!


# In[ ]:



