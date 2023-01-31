from shopee_funs import mouse_roll_and_crawl , shopee
my_item   = str(input('請輸入要爬取的物件(ex:包包):'))
save_path = str(input('請輸入要存取的路徑以及檔名(ex:./bag.txt):'))
#調用上述的class
S = shopee() #此調用動作已經包含了 init 裡面開啟chrome的功能
crawl_list = S.page_crawl(item=my_item)
crawl_list

output_file = open(save_path,'w',encoding = 'utf8')
for each_title in crawl_list:
    output_file.write(str(each_title)+'\n')
output_file.close()