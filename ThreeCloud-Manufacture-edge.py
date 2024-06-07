###Program Usage: Three Cloud Clicking for Manufacture
###Author: jiangweiguo
###2022/11/28

import time
import webbrowser
import os
import datetime
import random

MSEDGEPath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('MSEDGE', None, webbrowser.BackgroundBrowser(MSEDGEPath))

url0='https://threecloud.huawei.com/viewStory?storyId=story_8f525493-4e66-4495-b3fa-d8a40f9fc0c4&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/48d979d3-78cc-47f9-8966-6521e18996bc/@677278'
url1='https://threecloud.huawei.com/viewStory?storyId=story_058822a7-6380-46b5-be83-4f9ef794bf52&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/450e960a-a73d-4ca5-9e5d-a523c6aec85e/@677278'
url2='https://threecloud.huawei.com/viewStory?storyId=story_7cac1912-2d71-445e-a5c9-9b8b0da05ab4&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/b5ffc905-6ec7-4c8d-ae94-e36e1479911d/@677278'
url3='https://threecloud.huawei.com/viewStory?storyId=story_06751cd2-b7fa-4ef1-8d91-5371192648fc&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/bd7fa33d-f463-4995-88d7-f05c56c3414c/@677278'
url4='https://threecloud.huawei.com/viewStory?storyId=story_7d5d20c9-1dd7-46ae-b6c0-c903f374aab9&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/fd61f4ea-891d-40e1-a1fc-9cb933f753f6/@677278'
url5='https://threecloud.huawei.com/viewStory?storyId=story-4950c0c8-08dc-4c86-b5d8-5b646d5bc8e9&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/38fb9b1b-b37f-46bf-a9d8-00615e3bc001/@677278'
url6='https://threecloud.huawei.com/viewStory?storyId=story_c81c0117-43e4-45d8-a918-a780dc12a549&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/d380ad86-4c3e-48e9-a043-90436267dcff/@677278'
url7='https://threecloud.huawei.com/viewStory?storyId=story_a74fe24e-2796-4d4c-b87c-bce4b41cd864&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/7e653596-e972-439d-a465-49173c6fb13f/@677278'
url8='https://threecloud.huawei.com/viewStory?storyId=story_9d13b4f7-e004-4996-99ec-83bce9a4faaf&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/adfe31c0-01f1-41de-8ca9-f0b5178d6a79/@677278'
url9='https://threecloud.huawei.com/viewStory?storyId=story_70720673-f460-4fec-b99b-9dec66eabf52&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/d6b1246a-a33e-4390-9009-d3d53d4ad801/@677278'
url10='https://threecloud.huawei.com/viewStory?storyId=story_19d0ff46-2783-46cc-ac5b-ea54c4104b17&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/44b21e9f-d06a-4724-8881-357e27fb0b20/@677278'
url11='https://threecloud.huawei.com/viewStory?storyId=story_ab06d98a-e3db-457e-8972-efe2062f8493&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/60ab6753-3a47-44c1-b54b-153b7f69670f/@677278'
url12='https://threecloud.huawei.com/viewStory?storyId=story_5b096fff-eced-45a4-9b50-58a25cfa2f9c&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/c12b153a-c020-45e2-bc2a-ce0472620405/@677278'
url13='https://threecloud.huawei.com/viewStory?storyId=story_7f7b66df-4f18-42a1-a2c3-a021e5977093&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/0b82957e-65d9-4e5b-9f58-2cb8d3164143/@677278'
url14='https://threecloud.huawei.com/viewStory?storyId=story_08caabdf-736c-4219-9048-fb5c1169f6dd&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/36e8ae16-f97d-4c85-b56e-0ef91e9c069e/@677278'
url15='https://threecloud.huawei.com/viewStory?storyId=story_640b34e6-b052-4b58-958a-eacb15c05b47&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/3727c7d7-18bf-409f-8362-592029108db2/@677278'
url16='https://threecloud.huawei.com/viewStory?storyId=story_e8b137d4-cd0f-44b2-8110-22705b977ab5&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/f6dfd7a0-dd4d-42e5-af7f-47f50062133e/@677278'
url17='https://threecloud.huawei.com/viewStory?storyId=story_ffe91be7-5e5f-42a9-b02c-5862d2fa5650&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/41e45e11-9906-442b-bbf6-38c1e183bb18/@677278'
url18='https://threecloud.huawei.com/viewStory?storyId=story_18c9984b-e58d-490e-8a5f-fe4a1b1c2280&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/0b33db75-497c-4f8a-a4dc-bc4303b56c31/@677278'
url19='https://threecloud.huawei.com/viewStory?storyId=story-018456c5-112a-4bbd-9348-4b01eb0f0038&locale=zh_CN&zoneId=zone-0b7abb8f-2398-4568-9960-6731864ace6f&_dl=Y2hu#/83cff607-e872-4573-b52d-f6ae03dbe44d/@677278'

urllist = [url0, url1, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12, url13, url14, url15, url16, url17, url18, url19]

for t in range(100):                    ##运行100遍
    print (datetime.datetime.now(), 'This is the', t + 1, 'times runing')

    for i in range(len(urllist)):
        url = random.choice(urllist)    ##随机选取一个网址
        webbrowser.get('MSEDGE').open(url, new=1, autoraise=True)
        print ('open url', url)
        time.sleep(random.randint(5, 10))
            
    r = random.randint(300, 600)        ##随机休息5-10分钟
    print (datetime.datetime.now(),'...please waiting for', r, 'seconds')
    time.sleep(r)

    os.system('taskkill /F /IM msedge.exe /T')
