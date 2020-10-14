# use command "pwd" to see where to put the csv ,json or text files so that you can read them



# 1st part
import numpy as np
import pandas as pd
import plotly.plotly as pl
import plotly.offline as po   # these need to be run offline which is why we need to import offline lib
import cufflinks as cf

po.init_nootebook_mode(connected = True)  # to connect the offline plotly with our system
cf.go_offline()                           # to load cufflinks go_offline


# 3rd part
def createdata(data):
    if data == 1 :

        x = np.random.rand(100,5)        # a numpy function that generates random matrix of numbers having 100 rows and 5 columns

        a = pd.Dataframe(x , columns = ['A','B','C','D','E'])  #  a pandas function that will give you kinda box of values of x having columns as defined ie (a matrix)
        # think of Data frame as creating an excel file ie having a table with columns A B C D
    elif data == 2:
        x =  [0,0,0,0,0]                 # examplry matrix of 5 empty columns
        r1 = [0,0,0,0,0]
        r2 = [0,0,0,0,0]
        r3 = [0,0,0,0,0]
        r4 = [0,0,0,0,0]

        print("Enter the values of columns")

        i = 0        # initializing for loop variable
        for i in [0,1,2,3,4]:
            x[i] = input()           # take values from user as column and then update the list of x
            i = i + 1

        print("Enter the values for 1st row")

        i = 0
        for i in [0,1,2,3,4]:
            r1[i] = input()
            i = i + 1
        print("Enter the values for 2nd row")

        i = 0
        for i in [0,1,2,3,4]:
            r2[i] = input()
            i = i + 1

        print("Enter the values for 3rd row")

        i = 0
        for i in [0,1,2,3,4]:
            r3[i] = input()
            i = i + 1

        print("Enter the values for 4th row")

        i = 0
        for i in [0,1,2,3,4]:
            r4[i] = input()
            i = i + 1

        a = np.Dataframe([r1,r2,r3,r4], columns = x )


    elif data == 3 :

        file = input("Enter the name of the file (csv file)")

        x = pd.read_csv(file)        # reading or kind of loading the csv file via pandas to variable x

        a = pd.Dataframe(x)

    else :
        print("Please enter a valid number from 1 2 or 3 ")


    return a

# 7th part
def main(b):
    if b==1:
        print('Select the type of plot you need to plot by writing 1 to 6')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')      #  a box plot shows you min , max , 25% quartile , 75% quartile and median of the data
        print('6.Surface plot') #Surface plots are diagrams of three-dimensional data. Rather than showing the individual data points, surface plots
        # show a functional relationship between a designated dependent variable (Y), and two independent variables (X and Z).

        c = int(input())   # let user select one from above

        output = plotter1(c)

    elif b==2:
        print('Select the type of plot you need to plot by writing 1 to 7')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot') # displays 3 dimensions of data.Bubble charts can facilitate the understanding of social, economical, medical, and other scientific relationships.
        # Bubble charts can be considered a variation of the scatter plot

        c = int(input())

        output = plotter2(c)

    else :
        print("Please Enter 1 or 2 or try again")


# 8th part
def plotter1(c):

    if c == 1:
        d = a.iplot(kind = 'scatter')  #  a new variable d which will store plots . ie will get dataframe a apply method iplot of cufflinks with Scatter

    elif c == 2:
        d = a.iplot(kind='scatter',mode='markers' ,symbol='x',colorscale='paired') # mode markers will disconnect lines and will display dots, symbol will
        #replace dots with X and paired colorscale will merge colors ie diminished

    elif(c == 3):
        d = a.iplot(kind='bar')

    elif(c == 4):
        d = a.iplot(kind='hist')

    elif(c == 5):
        d = a.iplot(kind='box')

    elif(c == 6):
        d = a.iplot(kind='surface')

    else:
        d = print('Select only between 1 to 7')

    return d

# 9th part
def plotter2(c):
    e = int(input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3'))  # takes or selects number of columns to plots

    if(e==1):
        f = input('Enter the column you want to plot by selecting any column from dataframe head') # that column which user selects from the dataframe

        if(c==1):
            d = a[f].iplot(kind='scatter')

        elif(c==2):
            d = a[f].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')

        elif(c==3):
            d = a[f].iplot(kind='bar')

        elif(c==4):
            d = a[f].iplot(kind='hist')

        elif(c==5):
            d = a[f].iplot(kind='box')

        elif(c==6 or c==7):
            d = print('Bubble plot and surface plot require more than one column arguments')

        else:
            d = print('Select only between 1 to 7')

    if(e==2):
        f = input('Enter the column you want to plot by selecting any column from dataframe head') # that column which user selects from the dataframe
        x = input("First column")
        y = input("Second column")     # as now he has to enter two columns

        # now we give our dataframe two columns ie by list of x and y
        if(c==1):
            d = a[[x,y]].iplot(kind='scatter')

        elif(c==2):
            d = a[[x,y]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')

        elif(c==3):
            d = a[[x,y]].iplot(kind='bar')

        elif(c==4):
            d = a[[x,y]].iplot(kind='hist')

        elif(c==5):
            d = a[[x,y]].iplot(kind='box')

        elif(c==6):
            d = a[[x,y]].iplot(kind='surface')

        elif(c==7):
            size = input('Please enter the size column for bubble plot')
            d = a.iplot(kind='bubble' , x=x,y=y,size=size)                     # two columns x and y which are x and y  ,

        else:
            d = print('Select only between 1 to 7')


    elif(e==3):
        print('Enter the columns you want to plot')
        x=input('First column')
        y=input('Second column')
        z=input('Third column')

        # now we give our dataframe three columns ie by list of x y and z

        if(c==1):
            d = a[[x,y,z]].iplot(kind='scatter')

        elif(c==2):
            d = a[[x,y,z]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')

        elif(c==3):
            d = a[[x,y,z]].iplot(kind='bar')

        elif(c==4):
            d = a[[x,y,z]].iplot(kind='hist')

        elif(c==5):
            d = a[[x,y,z]].iplot(kind='box')

        elif(c==6):
            d = a[[x,y,z]].iplot(kind='surface')

        elif(c==7):
            size = input('Please enter the size column for bubble plot')
            d = a.iplot(kind='bubble' , x=x,y=y,z=z,size=size )

        else:
            d = print('Select only between 1 to 7')

    else:
        d = print('Please enter only 1 , 2 or 3')

    return d






#  2nd part
print("Select the type of data you need to plot (by selecting 1 2 or 3  below)")
print("1. Random data with 100 rows and 5 eumns")
print("2. Customize dataframe with 5 columns and 4 rows")
print("3. Upload csv/json/txt file ")

data = int(input())                      # saved the selection of user

a = createdata(data)                     #function defined above



# 4th part
print("Your Dataframe head is given below check the columns to plot using cufflinks")

a.head()                   # head is a method which simplys shows the sample compacted dataframe ie it will show 4 to 5 rows n columns

# 5th part
print("What kind of plot do you want , the complete data plot or columns plot")   # ie plot all or give certain columns to plot only them

b = int(input("Press 1 for plotting all columns and 2 for specifying columns to plot"))

#6th part
main(b)
