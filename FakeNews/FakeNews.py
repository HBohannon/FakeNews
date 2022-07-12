import pandas as pd

FakeNews = pd.read_excel('C:/User/Hanna B/Documents/python_course/Practice HandsOn L1/FakeNews.xlsx')
FakeNews.head()

#Add a column labeled StoryType and fill it with Fake

FakeNews['StoryType'] = "Fake"
FakeNews.head()

#Remove the when column

FakeNews.drop(['when'], axis=1, inplace=True)
FakeNews.head()




#Separate the URL column into Website and Domain

FakeNews1 = FakeNews['url'].str.split('_', expand=True).rename(columns = lambda x: "URL"+str(x+1))
FakeNews1.head()

FakeNews2 = pd.concat([FakeNews, FakeNews1], axis=1)
FakeNews2.head()

FakeNews2.drop(['url'], axis=1, inplace=True)
FakeNews2.head()



#Put the domain column back together:

FakeNews2['url'] = FakeNews2["URL1"] + "_" + FakeNews2["URL2"].map(str)
FakeNews2.head()

FakeNews2.drop(['URL1', 'URL2'], axis=1, inplace=True)
FakeNews2.head()

#Keep ONLY the first ten rows of the data


FakeNews3 = FakeNews2[:10]
FakeNews3