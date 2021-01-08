import zipfile
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from high_order_framework_requests_python import utils_class

class Chrome_auto():
    def __init__(self,os,isLoadImage,isHeadless,folder_save='', proxy=''):
        self.os=os
        self.isLoadImage=isLoadImage
        self.isHeadless=isHeadless
        self.folder_save=folder_save
        self.proxy=proxy
        
    def initDriver(self):
        chrome_options = webdriver.ChromeOptions()
        if self.isHeadless:
            chrome_options.add_argument("--headless")

        if self.proxy:
            chrome_options.add_argument('--proxy-server=%s' % self.proxy)

        prefs={}
        if not self.isLoadImage:
            prefs['profile.managed_default_content_settings.images']=2
        #disable notification
        prefs['profile.default_content_setting_values.notifications']=2
        chrome_options.add_experimental_option("prefs", prefs)
        
        
        # chrome_options.add_argument('start-maximized')
        if self.folder_save !='':
            chrome_options.add_argument("user-data-dir=%s"%self.folder_save)

        WINDOW_SIZE = "1920,1080"
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

        if self.os=='windows':
            driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        
        if self.os=='linux':
            CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
            chrome_options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                    chrome_options=chrome_options
                                    )        
        return driver

    def initDriverPrivateProxy(self, PROXY_HOST,PROXY_PORT,PROXY_USER,PROXY_PASS,use_proxy=True, user_agent=None):
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)





        path = os.path.dirname(os.path.abspath(__file__))
        chrome_options = webdriver.ChromeOptions()
        if use_proxy:
            pluginfile = 'proxy_auth_plugin.zip'

            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            chrome_options.add_extension(pluginfile)
        if user_agent:
            chrome_options.add_argument('--user-agent=%s' % user_agent)
        driver = webdriver.Chrome(
            os.path.join(path, 'chromedriver'),
            chrome_options=chrome_options)
        return driver



    def check_curent_ip(self,driver):
        driver.get('https://api6.ipify.org?format=json')
        text=driver.find_element_by_css_selector('body').text
        # print(text)
        return text

    
    def wait_element_can_click(self,driver,css_element):
        return WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_element)))
    
    def wait_element_can_located(self,driver,css_element):
        return WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, css_element)))

    def upload_file(self, driver, file_path):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(file_path)
    
    def get_html_from_css_selector(self, driver,css_selector):
        return driver.find_element_by_css_selector(css_selector).get_attribute('innerHTML')

    def login(self, driver,url, css_user, user, css_pass , password,css_submit):
        driver.get(url)
        time.sleep(5)



        #wait until element located
        self.wait_element_can_located(driver,css_user)
        print('css_user', css_user)
        print('user', user)

        driver.find_element_by_css_selector(css_user).send_keys(user)
        time.sleep(1)
        driver.find_element_by_css_selector(css_pass).send_keys(password)
        time.sleep(1)
        driver.find_element_by_css_selector(css_submit).click()
        time.sleep(10)

        
        list_err=driver.find_elements_by_css_selector('#login_error')
        print(len(list_err))

        if len(list_err):
            driver.find_element_by_css_selector(css_user).send_keys(user)
            time.sleep(1)
            driver.find_element_by_css_selector(css_pass).send_keys(password)
            time.sleep(1)
            driver.find_element_by_css_selector(css_submit).click()
            time.sleep(10)



    def post_anhAll_wp(self,driver, url, list_image_locals):
        driver.get(url)
        time.sleep(5)
        dem = 0
        for filePath in list_image_locals:
            try:
                time.sleep(2)
                file_ip = WebDriverWait(driver, 10).until(
                    ec.invisibility_of_element_located((By.CSS_SELECTOR, "input[type=file]")))
                file_ip.send_keys(filePath)
                dem += 1
            except:
                print("err")

        #wait until all upload success
        eles = driver.find_elements_by_css_selector('.edit-attachment')
        demtimeout = 0
        timeout = 60
        while(len(eles) < dem):
            print('len(eles)', len(eles))
            eles = driver.find_elements_by_css_selector('.edit-attachment')
            time.sleep(2)

            demtimeout += 1
            if demtimeout > timeout:
                break

        print('dem', dem)
        time.sleep(10)
        print("upload done")

    def remove_ext(self, link_image):
        string_Interact1=utils_class.String_Interact()
        ext = string_Interact1.regex_one_value(r'(-\d{3}x\d{3})', link_image)
        return link_image.replace(ext,'')
    
    def get_list_link_after_upload_all_wp(self,driver1):
        list_link_image = driver1.find_elements_by_css_selector('.pinkynail')
        list_link_image = [link_image.get_attribute('src') for link_image in list_link_image]
        list_link_image = [self.remove_ext(link_image) for link_image in list_link_image]

        list_file_name=driver1.find_elements_by_css_selector('.title')
        list_file_name=[file_name.text for file_name in list_file_name]

        return list_link_image,list_file_name

    def post_bai(self, driver, url, title, ndung,description='',id_wp=''):
        driver.get(url)
        time.sleep(0.5)
        driver.get(url)
        time.sleep(5)
        
        html_btn = self.wait_element_can_click(driver, '#content-html')
        html_btn.click()

        ndung = ndung.replace("'", '')
        try:
            driver.execute_script("document.querySelector('#content').value=`"+ndung+"`")
        except:
            return 'err_post'

        title_input = self.wait_element_can_located(driver, '#title')
        title_input.send_keys(title)

        if description:
            driver.find_element_by_css_selector('[name="aiosp_description"]').send_keys(description)
        if id_wp:
            js="document.querySelector('#category-"+'%s'%id_wp+" label').click()"
            driver.execute_script(js)


        driver.find_element_by_css_selector('#set-post-thumbnail.thickbox').click()
        #chuyen tab chon anh
        # menu_item_browse = self.wait_element_can_click(driver, '#menu-item-browse')
        # menu_item_browse.click()

        thumbnail_btn = self.wait_element_can_click(driver, '.thumbnail')
        thumbnail_btn.click()

        set_thumnail_btn = self.wait_element_can_click(driver, '.search-form button')
        set_thumnail_btn.click()

        #public_btn = self.wait_element_can_click(driver, '#publish')
        #public_btn.click()
        time.sleep(10)
        driver.execute_script("document.querySelector('#publish').click()")
        
        link_post=self.wait_element_can_located(driver,'#sample-permalink a')
        link_post = link_post.get_attribute('href')
        time.sleep(5)
        return link_post
    
    def downnload_image_from_gg_anh(self,driver1,image_path, nb_image,keyword):
        # idx_keyword=0
        # keyword='leo messi'
        nb_scroll=nb_image//35

        string_Interact1=utils_class.String_Interact()
        slug=string_Interact1.gen_slug(keyword)
        

        #b1; GET list link anh
        driver1.get('https://www.google.com/')

        url='https://www.google.com/search?tbm=isch&q=' + keyword.replace(" ", "+")
        driver1.get(url)
        time.sleep(5)


        #click cong cu
        driver1.find_elements_by_css_selector('[tabindex="0"] div')[2].click()
        time.sleep(3)
        #click vao size
        driver1.find_element_by_css_selector('div[data-index="0"] div').click()
        time.sleep(3)
        #click vao medium size
        driver1.find_element_by_css_selector('a[aria-label="Medium"]').click()
        time.sleep(3)


        for i in range(nb_scroll):
            driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)

        # #get link truc tiep cua anh
        list_elements = driver1.find_elements_by_css_selector('#islrg div a.islib')
        list_href = []

        para2=len(list_elements)
        if nb_image<para2:
            para2=nb_image
        
        for i in range(para2):
            element=list_elements[i]
            element.click()
            time.sleep(1)
            href = element.get_attribute('href')
            # print(href)
            list_href.append(href)

        #b2; DECODE url anh
        list_link_image=[]
        for href in list_href:
            try:
                o=string_Interact1.url_decode(href)
                link_image=o['https://www.google.com/imgres?imgurl']
                list_link_image.append(link_image[0])
            except:
                pass

        #b3; DOWNLOAD anh
        image_Interact1=utils_class.Image_Interact()
        for index,link_image in enumerate(list_link_image):
            image_Interact1.downloadImg(link_image,'%s-%s'%(slug,index),image_path)

    def get_list_suggest_keys(self,driver1,keyword):
        driver1.get('https://keywordtool.io/')
        time.sleep(30)

        #send keyword
        self.wait_element_can_located(driver1,'#edit-keyword').send_keys(keyword)
        js="document.querySelector('.glyphicon-search').click()"
        driver1.execute_script(js)
        time.sleep(30)

        #wait for result
        self.wait_element_can_located(driver1,'.text-normal.search-results-title')
        time.sleep(10)

        #get list_suggest_keys
        list_eles=driver1.find_elements_by_css_selector('.col-keywords')
        list_suggest_keys=[ele.text for ele in list_eles if ele.text!='']
        list_suggest_keys=list_suggest_keys[1:]

        print(list_suggest_keys)
        return list_suggest_keys

    
    def open_new_tab(self, driver1):
        driver1.execute_script("window.open('https://www.google.com');")

    def switch_tab(self, driver1, idx_tab):
        driver1.switch_to.window(driver1.window_handles[idx_tab])

    def filter_element_has_inner_text(self,driver1,css_selector, text):
        index=0
        list_eles=driver1.find_elements_by_css_selector(css_selector)
        for i,ele in enumerate(list_eles):
            if text.lower() in ele.text.strip().lower():
                index=i
                break
        return list_eles[index]

def get_proxy_tinsoft(api_key):
    #nghiahsgs
    # api_key='TL2x4XaVk8fDXECie3U2sZnChS6ZTbw4ARdiuQ'
    url = 'http://proxy.tinsoftsv.com/api/changeProxy.php?key=%s&location=1'%api_key
    data = requests.get(url).json()

    if data['success']:
        return data['proxy']
    else:
        url='http://proxy.tinsoftsv.com/api/getProxy.php?key=%s'%api_key
        data = requests.get(url).json()
        return data['proxy']

#get_proxy_tinsoft2
def get_new_proxy(api_key='TL2x4XaVk8fDXECie3U2sZnChS6ZTbw4ARdiuQ'):
    url = 'http://proxy.tinsoftsv.com/api/changeProxy.php?key=%s&location=1'%api_key
    data = requests.get(url).json()
    print(data)
    return data['proxy']

def get_proxy_tinsoft2(api_key='TL2x4XaVk8fDXECie3U2sZnChS6ZTbw4ARdiuQ'):
    url='http://proxy.tinsoftsv.com/api/getProxy.php?key=%s'%api_key
    data = requests.get(url).json()
    print(data)
    if data['success']:
        # print(data)
        #proxy song lau hon 5phut thi dung
        if(data['timeout']>400):
            proxy = data['proxy']
        else:
            time.sleep(data['next_change'])
            proxy=get_new_proxy(api_key)
    else:
        #ko co proxy thi tao moi
        proxy=get_new_proxy(api_key)
    return proxy

def spawn_chrome_win(isHeadless):
    proxy = get_proxy_tinsoft('')
    chrome_auto1 = Chrome_auto(os='windows',isLoadImage=True,isHeadless=isHeadless,folder_save='', proxy=proxy)
    driver1 = chrome_auto1.initDriver()
    return chrome_auto1,driver1

def spawn_chrome_linux(isHeadless):
    proxy = get_proxy_tinsoft('')
    chrome_auto1 = Chrome_auto(os='linux',isLoadImage=True,isHeadless=isHeadless,folder_save='', proxy=proxy)
    driver1 = chrome_auto1.initDriver()
    return chrome_auto1,driver1

def check_current_ip():
    data=requests.get('https://api6.ipify.org/?format=json').text
    return data

if __name__=='__main__':
    chrome_auto1=Chrome_auto('windows',True,True, proxy=get_proxy_tinsoft(''))
    driver1=chrome_auto1.initDriver()

    ip=chrome_auto1.check_curent_ip(driver1)
    print(ip)

    driver1.quit()


