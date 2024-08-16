from itertools import zip_longest
from bs4 import BeautifulSoup
import requests
import csv



title= []
links = []
about_1 = []
aboutMovie = []
result = requests.get("https://mydramalist.com/movies/top")
sr = result.content 
sp = BeautifulSoup(sr, "lxml")

titles = sp.find_all("h6", {"class":"text-primary title"})

for i in range(len(titles)):
    # title.append(titles[i].text)
     title.append(titles[i].find("a").text) 
     links.append(titles[i].find("a").attrs['href']) 

for link in links: 
    s = f"https://mydramalist.com/{link}"
    result = requests.get(s)
    sr = result.content 
    sp = BeautifulSoup(sr, "lxml")
    about = sp.find("b", {"class":"inline"})
    about_1.append(about.text)
    aboutM = sp.find("ul",{"class":"list m-a-0 hidden-md-up"})
    about_txt = ""
    for li in aboutM.find_all("li"):
        about_txt += li.text +  " | " 
        about_txt = about_txt[:-2].replace("#","^^") # replaced 

    aboutMovie.append(about_txt) 
    
file_list = [title, links, about_1, aboutMovie]
exported = zip_longest(*file_list)
with open(r"C:\Users\Admin\Documents\title.cvs", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Movie titles"," Movie links", "test", "About Movie"])
    wr.writerows(exported)


      