def gettiebalist(name): #获取贴吧前15页的链接
    tiebalist = []
    for i in range(15): #页数
        tiebalist.append("http://tieba.baidu.com/f?kw=" + name + "&pn=" + str(i * 50))
    return tiebalist


def gettiebatitle(pageurl):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib.request.Request(pageurl, headers=headers)
    # request.add_header("Connection", "keep-alive")
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

    restr = "<div class=\"threadlist_title pull_left j_th_tit \">([\s\S]*?)</div>"#取帖子标题
    regex = re.compile(restr,re.IGNORECASE)
    templist = regex.findall(data)

    str = ""
    for line in templist:
        #取帖子标题
        str += line
    restr = "<a rel=\"noreferrer\"([\s\S]*?)</a>"
    regex = re.compile(restr,re.IGNORECASE)
    templist1 = regex.findall(str)
    # print(templist1)

    str = ""
    for line in templist1:
       #取帖子标题
        str += line
    restr = "title=\"([\s\S]*?)\" target=\"_blank\" class=\"j_th_tit \">"
    regex = re.compile(restr,re.IGNORECASE)
    titlelist = regex.findall(str)

    str = ""
    for line in titlelist:
        str += line

    fo = open("title.txt", "a", encoding='utf-8')
    fo.write(str)
    fo.close()



name = ""#  贴吧名字
for i in gettiebalist(name):
    gettiebatitle(i)
