from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


def home (request):
    global search
    search=request.GET.get('search')
    print(search)
    if type(search) != 'NoneType':
        search=str(search)
        search= search.replace(' ','+')
    print(search)
    url=f"https://www.amazon.co.uk/s?k={search}&ref=nb_sb_noss"
    url2=f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search}&_sacat=0"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    page= requests.get(url,headers=headers)
    page2= requests.get(url2,headers=headers)
    soup= BeautifulSoup(page.content,'html.parser')
    soup2= BeautifulSoup(page2.content,'html.parser')
    title= soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"})
    title2= soup2.find_all("h3", {"class": "s-item__title"})
    price= soup.find_all("span", {"class": "a-offscreen"})
    price2= soup2.find_all("span", {"class": "s-item__price"})
    img= soup.find_all("img", {"class": "s-image"})
    img2= soup2.find_all("img", {"class": "s-item__image-img"})
    new_title=[]
    new_title2=[]
    new_price=[]
    new_price2=[]
    new_img=[]
    new_img2=[]
    for i in title:
        i= i.getText()
        new_title.append(i)
    for i in title2:
        title= i.getText()
        new_title2.append(title)
    for i in price:
        price= i.getText()
        new_price.append(price)
    for i in price2:
        price= i.getText()
        new_price2.append(price)
    for i in img:
        image= i['src']
        new_img.append(image)
    for i in img2:
        image= i['src']
        new_img2.append(image)
    new_title2=new_title2[1:12]
    new_price2=new_price2[:12]
    new_img2=new_img2[:12]
    mylist=zip(new_title2,new_price2,new_img2)
    mylist2=zip(new_title,new_price,new_img)
    print(new_title2)
    detail={"mylist":mylist,"mylist2":mylist2}
    return render(request,'index.html',detail)