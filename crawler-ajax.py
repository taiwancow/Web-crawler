#抓取OPGG的資料(ajax)
import urllib.request as req
src="https://op.gg/api/v1.0/internal/bypass/meta/champions?hl=zh_TW"
#建立一個request 物件，附加request headers資訊
request =req.Request(src,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")#根據觀察，取得JSON格式

#解析JSON格式的資料，取得每篇文章的標題
import json
data= json.loads(data)#把原始的 JSON 資料解析成字典/列表的表示形式
#取得JSON資料中的文章標題
# posts=data["data"][0]["skins"][16]["name"]
with open("LOL skin name.txt",mode="w",encoding="utf-8") as file:
    posts=data["data"]
    #print(posts)
#查全英雄造型
    # for post in posts:
    #     skins=(post["skins"]) 
    #     for skin in skins:
    #         names =(skin["name"])
    #         if names != "default":
    #             # print(names)             
    #             file.write(names + "\n")
                
    #             print(names)
#輸入英雄名稱查詢英雄造型
    name = input("請問需要查詢哪個英雄的造型?")
    for post in posts:
        hero=(post["name"])
        # print(names)  
        if name in hero:
            skins=(post["skins"])
            # print(skins)
            for skin in skins:
                skin_name =(skin["name"])
                if skin_name != "default":
                    print(skin_name)
                    file.write(skin_name + "\n")
            break            

    else:
        print("沒有此英雄")
