from selenium import webdriver  # 啟動控制我們的driver
from selenium.webdriver.common.keys import Keys  # 模擬使用鍵盤
from selenium.webdriver.chrome.options import Options  # 可以對網頁開啟時,做一些篩選,例如關閉開啟網頁的自動翻譯/詢問
import time
# ==================Explicit Waits=====(等待driver運作,直到某個特徵出現為止)========================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def mouse_roll_and_crawl(title_list, driver, pix=500, run_time=10):
    global imgs
    # 偷偷寫一下,輸入(添加名稱的籃子, driver , 每次向下滑多少像素, 總共滾幾次)
    for each_move in range(run_time):
        js = f'window.scrollBy(0,{pix})'
        driver.execute_script(js)
        print('滑鼠滾動一次~')
        time.sleep(1)
        prods = driver.find_elements_by_class_name('_10Wbs-')
        imgs = driver.find_elements_by_class_name('_3-N5L6')
        #         print(imgs)
        # prods 就是當下畫面有的盒子資訊
        for p in prods:
            t = p.text
            if t not in title_list:
                # 每次滾動 會有重複的內容, 做一個判斷,如果有重複的文字在已經append的籃子, 那就不要走這個判斷式
                title_list.append(t)
        for img in imgs:
            link = img.get_attribute('src')  # 類似bs4 裡面的get()
        #             print(link)
        time.sleep(1)
        print('每次滾完滑鼠,看一下籃子裡面的數量:', len(title_list))
    print('已經滾完所有頁面了,為了確保畫面有頁碼,所以滾輪網上滾一點點')


#     js = f'window.scrollBy(0,-300)'
#     driver.execute_script(js)


class shopee:
    def __init__(self, ):
        self.chrom_driver_path = './chromedriver.exe'
        self.opt = Options()
        self.opt.add_argument('--disable-notifications')  # 禁止彈出詢問視窗
        self.driver = webdriver.Chrome(self.chrom_driver_path, chrome_options=self.opt)

        self.pix = 500
        self.run_time = 8
        self.title_list = []

    def page_crawl(self, item='包包'):
        url = 'https://shopee.tw/'
        self.driver.get(url)  # 得到url資訊
        # 放大全螢幕
        self.driver.maximize_window()

        # 做一個彈性的等待(因為driver在處理時要時間,不想用sleep去固定時間等待)
        # 最多等10秒, 直到畫面有'stardust-popover__target' 出現後才會繼續走程式碼
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'stardust-popover__target')))

        # 找搜尋欄位 並且輸入我們想要的搜尋物件
        # search = driver.find_element_by_class_name('shopee-searchbar-input__input') #類似bs4 find
        search = self.driver.find_elements_by_class_name('shopee-searchbar-input__input')  # 類似bs4 find_all
        keyin_bar = search[0]
        keyin_bar.send_keys(item)
        keyin_bar.send_keys(Keys.ENTER)

        # 等待盒子的class出現,最多等10秒
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'col-xs-2-4')))
        print('已經搜尋完畢..')

        mouse_roll_and_crawl(self.title_list, self.driver, pix=self.pix, run_time=self.run_time)
        time.sleep(1)
        for page in range(2, 3):
            buttom_xpath = f'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[3]/div/button[{page + 1}]'
            self.driver.find_element_by_xpath(buttom_xpath).click()  # 用畫面的絕對位置,去找按鈕,並且點擊
            # 進入下一頁
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_10Wbs-')))
            # 成功跳轉到下一頁
            mouse_roll_and_crawl(self.title_list, self.driver, pix=self.pix, run_time=self.run_time)
            print(f'==========第{page}頁完成爬取===========')
        self.driver.quit()
        return self.title_list