import requests
import json
def getCommodityComments(url):
    if url[url.find('id=')+14] != '&':
        id = url[url.find('id=')+3:url.find('id=')+15]
    else:
        id = url[url.find('id=')+3:url.find('id=')+14]
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+id+'&currentPageNum=1'
    res = requests.get(url)
    jc = json.loads(res.text.strip().strip('()'))
    max = jc['total']
    users = []
    comments = []
    count = 0
    page = 1
    while count<max:
        res = requests.get(url[:-1]+str(page))
        page = page + 1
        jc = json.loads(res.text.strip().strip('()'))
        jc = jc['comments']
        print('该商品共有评论'+str(count)+'条,具体如下:')
        for j in jc:
            users.append(j['user']['nick'])
            comments.append( j['content'])
            print(count+1,'>>',users[count],'\n        ',comments[count])
            count = count + 1

getCommodityComments('https://detail.tmall.com/item.htm?spm=a222t.7786574.firstTime.1.QCTYbW&acm=lb-zebra-21014-573575.1003.4.789038&id=537743006671&scm=1003.4.lb-zebra-21014-573575.ITEM_537743006671_789038&skuId=3423032242596')

