library("tidyr")


#Add column labeled StoryType and fill it with Fake:

  FakeNews$StoryType = "Fake"

#Remove the "when" column:
  
  FakeNews1 <- FakeNews[, 2:4]
  
#Separate the URL column 
#To see the website in one column and the domain in another:
  
  FakeNews2 <- separate(FakeNews1, url, c("Website", "Domain"), sep="_")
  
  
#Put the domain column back together:
  
  FakeNews3 <- unite(FakeNews2, FullSiteName, Website, Domain, sep = "_")
  
  
#Keep ONLY the first ten rows of data:
  
  FakeNews4 <- FakeNews3[1:10,]
  
  
  
  
