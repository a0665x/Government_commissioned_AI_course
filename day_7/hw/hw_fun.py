from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import  urlopen


class rest_crawl_fun:
    def __init__(self,):
        self.name_list =  []
        self.link_list =  []
#==============================================================================
    def rest_crawl(self,page = 1): # page:從哪一頁開始爬
        while True:
            url = 'https://tabelog.com/tw/rstLst/'+str(page)+'/?maxLat=34.24365355481369&minLat=34.05243392843337&maxLon=134.74502128375389&minLon=134.43946403277732&lat=34.148097849244536&lon=134.5922426582656&zoom=12&RdoCosTp=2&LstCos=0&LstSitu=0&LstRev=0&LstReserve=0&ChkParking=0&LstSmoking=0&LstCatD=RC0101&LstCat=RC01&Cat=RC'
            res = urlopen(url)
            res
            html = BeautifulSoup(res)
            restaurants = html.find_all('li',class_ = 'list-rst')
            print('看一下餐廳盒子群的個數',len(restaurants))
            if len(restaurants)==0:
                break
            for each_rest in restaurants:
                rest_name = each_rest.find('div',class_ = 'list-rst__header').find('a',class_ = 'list-rst__name-main').text
                rest_link = each_rest.find('div',class_ = 'list-rst__header').find('a',class_ = 'list-rst__name-main').get('href')
                self.name_list.append(rest_name)
                self.link_list.append(rest_link)
            print(f'===========爬完了{page}頁=================')
            page += 1

        df = pd.DataFrame(columns = ['rest_name','link'])
        df['rest_name'] = self.name_list
        df['link']      = self.link_list
        return df