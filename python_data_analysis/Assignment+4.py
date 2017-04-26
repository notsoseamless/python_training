
# coding: utf-8

# In[ ]:

---

_You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._

---


# In[1]:

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


# # Assignment 4 - Hypothesis Testing
# This assignment requires more individual learning than previous assignments - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.
# 
# Definitions:
# * A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
# * A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# * A _recession bottom_ is the quarter within a recession which had the lowest GDP.
# * A _university town_ is a city which has a high percentage of university students compared to the total population of the city.
# 
# **Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)
# 
# The following data files are available for this assignment:
# * From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
# * From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
# * From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```. For this assignment, only look at GDP data from the first quarter of 2000 onward.
# 
# Each function in this assignment below is worth 10%, with the exception of ```run_ttest()```, which is worth 50%.

# In[2]:

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


# In[3]:

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
        
    # import university_towns
    in_file = open('university_towns.txt', 'r')
    towns = []
    index = 0
    
    for line in in_file:
        if "[edit]" in line:
            # we are at start of state section
            current_state = line.split("[")[0]
        else:
            # now we are in town section, append state and town
            town = line.split("(")[0].strip()
            towns.append([current_state, town])

    df = pd.DataFrame(towns)
    df.columns = ["State", "RegionName"]
    return df


get_list_of_university_towns()


def test_get_list_of_university_towns():
    '''
    output should be in both cases
    Empty DataFrame
    Columns: [State, RegionName]
    Index: []
    '''
    df = get_list_of_university_towns()
    print (df[df['State'].str.contains('\n') | df['RegionName'].str.contains('\n')])
    print(df[df['State'].str.contains('\s$',regex=True) | df['RegionName'].str.contains('\s$',regex=True)])

#test_get_list_of_university_towns()



# In[4]:

def get_gdp():
    gdp_excel = pd.ExcelFile('gdplev.xls')
    gdp = gdp_excel.parse('Sheet1')
    # get rid of footer
    gdp = gdp.drop(gdp.index[288:])
    # get rid of header
    # only look at GDP data from the first quarter of 2000 onward.
    gdp = gdp.drop(gdp.index[0:219])    
    # get rid of unwanted columns
    gdp = gdp.drop('Current-Dollar and "Real" Gross Domestic Product', 1)
    gdp = gdp.drop('Unnamed: 5', 1)
    gdp = gdp.drop(gdp.ix[:,'Unnamed: 1':'Unnamed: 3'].head(0).columns, axis=1)
    # change the column labels
    gdp.columns = ['Quater', 'GDP', 'Temp']
    gdp = gdp.drop('Temp', 1)
    #gdp.reset_index()
    return gdp




def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    
    gdp = get_gdp()
    
    gdp_prev_1 = pd.Series(['', 0.0], index=['Quater', 'GDP'])
    gdp_prev_2 = pd.Series(['', 0.0], index=['Quater', 'GDP'])
    
    # step through quarters to find resession
    for index, row in gdp.iterrows():
        if (row['GDP'] < gdp_prev_1['GDP']) and (gdp_prev_1['GDP'] < gdp_prev_2['GDP']):
           return gdp_prev_1['Quater']
        # set history
        gdp_prev_2 = gdp_prev_1
        gdp_prev_1 = row
    
    return 'ERROR'
                 

get_recession_start()


# In[5]:

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    gdp = get_gdp()
    
    gdp_prev_1 = pd.Series(['', 0.0], index=['Quater', 'GDP'])
    gdp_prev_2 = pd.Series(['', 0.0], index=['Quater', 'GDP'])
    
    in_ressession = False
    
    # step through quarters to find resession start and end
    for index, row in gdp.iterrows():
        if in_ressession == False:
            if (row['GDP'] < gdp_prev_1['GDP']) and (gdp_prev_1['GDP'] < gdp_prev_2['GDP']):
               in_ressession = True
        else:
            # now we are in ressession
            if (row['GDP'] > gdp_prev_1['GDP']) and (gdp_prev_1['GDP'] > gdp_prev_2['GDP']):
                return row['Quater'] 
            
        # set history
        gdp_prev_2 = gdp_prev_1
        gdp_prev_1 = row
    
    return 'ERROR'


get_recession_end()    


# In[6]:

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''

    gdp = get_gdp()
    #gdp = gdp.set_index('Quater')
    
    r_start = get_recession_start()
    r_end   = get_recession_end()
    
    gdp = gdp.set_index('Quater')
    
    resession = gdp.loc[r_start : r_end]
    resession = resession['GDP'].sort_values(ascending=True).index[0]
    
    return resession
    


get_recession_bottom()


# In[7]:

import pandas as pd
import numpy as np

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    
    # import housing data
    houses = pd.read_csv('City_Zhvi_AllHomes.csv')  
    
    # remove unwanted columns
    cols = [c for c in houses.columns if c.lower()[:3] != '199']    
    houses = houses[cols]
    
    
    #houses.index = pd.to_datetime(houses.index)
    #return houses.head()
    
    
    cols = [c for c in houses.columns if c.lower()[:2] == '20']  
    tdf = houses[cols]
    
    #tdf.index = pd.to_datetime(tdf.index)
    
    tdf = pd.to_datetime('2008-06-12')
    
    #mdf = tdf.T.resample('Q').mean().T  
    
    #return tdf
    

    
    #THIS IS TERRIBLE CODE:
    
    # set up quaters data  
    houses['2000q1'] = houses[['2000-01', '2000-02', '2000-03']].mean(axis=1)
    houses['2000q2'] = houses[['2000-04', '2000-05', '2000-06']].mean(axis=1)
    houses['2000q3'] = houses[['2000-07', '2000-08', '2000-09']].mean(axis=1)
    houses['2000q4'] = houses[['2000-10', '2000-11', '2000-12']].mean(axis=1)

    houses['2001q1'] = houses[['2001-01', '2001-02', '2001-03']].mean(axis=1)
    houses['2001q2'] = houses[['2001-04', '2001-05', '2001-06']].mean(axis=1)
    houses['2001q3'] = houses[['2001-07', '2001-08', '2001-09']].mean(axis=1)
    houses['2001q4'] = houses[['2001-10', '2001-11', '2001-12']].mean(axis=1)

    houses['2002q1'] = houses[['2002-01', '2002-02', '2002-03']].mean(axis=1)
    houses['2002q2'] = houses[['2002-04', '2002-05', '2002-06']].mean(axis=1)
    houses['2002q3'] = houses[['2002-07', '2002-08', '2002-09']].mean(axis=1)
    houses['2002q4'] = houses[['2002-10', '2002-11', '2002-12']].mean(axis=1)

    houses['2003q1'] = houses[['2003-01', '2003-02', '2003-03']].mean(axis=1)
    houses['2003q2'] = houses[['2003-04', '2003-05', '2003-06']].mean(axis=1)
    houses['2003q3'] = houses[['2003-07', '2003-08', '2003-09']].mean(axis=1)
    houses['2003q4'] = houses[['2003-10', '2003-11', '2003-12']].mean(axis=1)

    houses['2004q1'] = houses[['2004-01', '2004-02', '2004-03']].mean(axis=1)
    houses['2004q2'] = houses[['2004-04', '2004-05', '2004-06']].mean(axis=1)
    houses['2004q3'] = houses[['2004-07', '2004-08', '2004-09']].mean(axis=1)
    houses['2004q4'] = houses[['2004-10', '2004-11', '2004-12']].mean(axis=1)

    houses['2005q1'] = houses[['2005-01', '2005-02', '2005-03']].mean(axis=1)
    houses['2005q2'] = houses[['2005-04', '2005-05', '2005-06']].mean(axis=1)
    houses['2005q3'] = houses[['2005-07', '2005-08', '2005-09']].mean(axis=1)
    houses['2005q4'] = houses[['2005-10', '2005-11', '2005-12']].mean(axis=1)

    houses['2006q1'] = houses[['2006-01', '2006-02', '2006-03']].mean(axis=1)
    houses['2006q2'] = houses[['2006-04', '2006-05', '2006-06']].mean(axis=1)
    houses['2006q3'] = houses[['2006-07', '2006-08', '2006-09']].mean(axis=1)
    houses['2006q4'] = houses[['2006-10', '2006-11', '2006-12']].mean(axis=1)

    houses['2007q1'] = houses[['2007-01', '2007-02', '2007-03']].mean(axis=1)
    houses['2007q2'] = houses[['2007-04', '2007-05', '2007-06']].mean(axis=1)
    houses['2007q3'] = houses[['2007-07', '2007-08', '2007-09']].mean(axis=1)
    houses['2007q4'] = houses[['2007-10', '2007-11', '2007-12']].mean(axis=1)

    houses['2008q1'] = houses[['2008-01', '2008-02', '2008-03']].mean(axis=1)
    houses['2008q2'] = houses[['2008-04', '2008-05', '2008-06']].mean(axis=1)
    houses['2008q3'] = houses[['2008-07', '2008-08', '2008-09']].mean(axis=1)
    houses['2008q4'] = houses[['2008-10', '2008-11', '2008-12']].mean(axis=1)

    houses['2009q1'] = houses[['2009-01', '2009-02', '2009-03']].mean(axis=1)
    houses['2009q2'] = houses[['2009-04', '2009-05', '2009-06']].mean(axis=1)
    houses['2009q3'] = houses[['2009-07', '2009-08', '2009-09']].mean(axis=1)
    houses['2009q4'] = houses[['2009-10', '2009-11', '2009-12']].mean(axis=1)
    
    houses['2010q1'] = houses[['2010-01', '2010-02', '2010-03']].mean(axis=1)
    houses['2010q2'] = houses[['2010-04', '2010-05', '2010-06']].mean(axis=1)   
    houses['2010q3'] = houses[['2010-07', '2010-08', '2010-09']].mean(axis=1)
    houses['2010q4'] = houses[['2010-10', '2010-11', '2010-12']].mean(axis=1)

    houses['2011q1'] = houses[['2011-01', '2011-02', '2011-03']].mean(axis=1)
    houses['2011q2'] = houses[['2011-04', '2011-05', '2011-06']].mean(axis=1)
    houses['2011q3'] = houses[['2011-07', '2011-08', '2011-09']].mean(axis=1)
    houses['2011q4'] = houses[['2011-10', '2011-11', '2011-12']].mean(axis=1)

    houses['2012q1'] = houses[['2012-01', '2012-02', '2012-03']].mean(axis=1)
    houses['2012q2'] = houses[['2012-04', '2012-05', '2012-06']].mean(axis=1)
    houses['2012q3'] = houses[['2012-07', '2012-08', '2012-09']].mean(axis=1)
    houses['2012q4'] = houses[['2012-10', '2012-11', '2012-12']].mean(axis=1)

    houses['2013q1'] = houses[['2013-01', '2013-02', '2013-03']].mean(axis=1)
    houses['2013q2'] = houses[['2013-04', '2013-05', '2013-06']].mean(axis=1)
    houses['2013q3'] = houses[['2013-07', '2013-08', '2013-09']].mean(axis=1)
    houses['2013q4'] = houses[['2013-10', '2013-11', '2013-12']].mean(axis=1)

    houses['2014q1'] = houses[['2014-01', '2014-02', '2014-03']].mean(axis=1)
    houses['2014q2'] = houses[['2014-04', '2014-05', '2014-06']].mean(axis=1)
    houses['2014q3'] = houses[['2014-07', '2014-08', '2014-09']].mean(axis=1)
    houses['2014q4'] = houses[['2014-10', '2014-11', '2014-12']].mean(axis=1)

    houses['2015q1'] = houses[['2015-01', '2015-02', '2015-03']].mean(axis=1)
    houses['2015q2'] = houses[['2015-04', '2015-05', '2015-06']].mean(axis=1)
    houses['2015q3'] = houses[['2015-07', '2015-08', '2015-09']].mean(axis=1)
    houses['2015q4'] = houses[['2015-10', '2015-11', '2015-12']].mean(axis=1)

    houses['2016q1'] = houses[['2016-01', '2016-02', '2016-03']].mean(axis=1)
    houses['2016q2'] = houses[['2016-04', '2016-05', '2016-06']].mean(axis=1)
    houses['2016q3'] = houses[['2016-07', '2016-08'           ]].mean(axis=1)
    
    # get rid of monthly data
    month_cols = [col for col in houses.columns if '-' in col]
    houses = houses.drop(month_cols, axis=1)
    
    #del_cols = ['RegionID', 'Metro', 'SizeRank', 'CountyName']
    del_cols = ['RegionID', 'CountyName', 'SizeRank', 'CountyName', 'Metro']
    houses = houses.drop(del_cols, axis=1)    

    # rename 
    houses['State'] = [states[state] for state in houses['State']]
    houses = houses.set_index(['State', 'RegionName'])
    
    return houses





convert_housing_data_to_quarters().head()


# In[48]:

from scipy import stats
import numpy as np

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).''' 
        
    # get housing data in ressession
    r_start  = get_recession_start()
    r_bottom = get_recession_bottom()

    # get housing data
    hdf = convert_housing_data_to_quarters()
    
    col_names = list(hdf)
    r_start_idx = col_names.index(r_start)
    r_bottom_idx = col_names.index(r_bottom)
    
    hdfr = hdf.ix[ : , r_start_idx:r_bottom_idx+1]
    # get decline or growth of housing prices
    hdfr['Decline'] = hdfr['2008q3'] - hdfr['2009q2']
    
    # get university towns
    un_towns = get_list_of_university_towns()
    un_towns['HasUni'] = True
    un_towns = un_towns.set_index(['State', 'RegionName'])
    un_towns = un_towns.reset_index()  
    
    hdfr = hdfr.reset_index()
#    hdfr_u = pd.merge(un_towns, hdfr, how='left', right_on=['State','RegionName'], left_on=['State','RegionName'])
#    hdfr_u = hdfr_u.set_index(['State', 'RegionName'])
    
    hdfr = pd.merge(un_towns, hdfr, how='right', right_on=['State','RegionName'], left_on=['State','RegionName'])
    hdfr = hdfr.set_index(['State', 'RegionName'])
    
    # remove rows where HasUni is True
    nouni = hdfr[hdfr.HasUni != True]
    
    #  remove rows where HasUni is not True
    withini = hdfr[hdfr.HasUni == True]

    # calculate ttest
    eval = stats.ttest_ind(nouni['Decline'], withini['Decline'], nan_policy='omit')      
    
    if eval.pvalue < 0.01:
        p = True
    else:
        p = False
    
    return (np.bool_(p), eval.pvalue, "university town")
    
    
    
    
    
#the auto-grader expects [bool, numpy.float64, str]

#res= run_ttest()
#correctTypes = ', '.join(str(type(v)) for v in res) == "<class 'numpy.bool_'>, <class 'numpy.float64'>, <class 'str'>"
#if correctTypes:
#    print("Data types test passed")
#else:
#    print("Data types test failed")

    
    



run_ttest()








# In[ ]:



