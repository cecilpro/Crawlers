import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')


for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(time,h2,a)

'''
3月15日 11:39 科学家发现抗寨卡病毒蛋白质 有望抑制艾滋病毒 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6649952.shtml
3月15日 11:38 体育总局局长:中超老板有钱任性 需严格整肃 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6649878.shtml
3月15日 11:23 李克强谈中美关系:虽经历风风雨雨但一直前行 http://news.sina.com.cn/c/2017-03-15/doc-ifycnikk0705650.shtml
3月15日 11:11 重庆新确诊1例人感染H7N9病例 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6645815.shtml
3月15日 11:05 赣州成江西房产限购第二城 本市居民限购1套 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4643474.shtml
3月15日 10:58 李克强：增长6.5%这个速度不低了 也很不容易 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1404173.shtml
3月15日 10:52 民进党党内争台南市长提名 台媒:1图看清这些人 http://news.sina.com.cn/c/2017-03-15/doc-ifycnikk0700152.shtml
3月15日 10:50 台湾“观光局”:游览车上导游必须进行安全解说 http://news.sina.com.cn/o/2017-03-15/doc-ifycnikk0699676.shtml
3月15日 10:39 中消协:微商付费游戏等网络消费不满意率突出 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6639580.shtml
3月15日 10:28 部长通道回答问题创新高 46部门共回答95个问题 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6637866.shtml
3月15日 10:23 剁手党注意 今起7类商品不适用七日无理由退货 http://news.sina.com.cn/o/2017-03-15/doc-ifychavf2849234.shtml
3月15日 10:12 第十二届全国人民代表大会第五次会议(全文) http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4638516.shtml
3月15日 09:51 第十二届全国人民代表大会第五次会议闭幕 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4636094.shtml
3月15日 09:50 官方:决不让一个达不到安全条件煤矿复工复产 http://news.sina.com.cn/o/2017-03-15/doc-ifychavf2840952.shtml
3月15日 09:43 徐显明辞去全国人大常委会委员表决通过 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1396619.shtml
3月15日 09:40 全国人大闭幕会表决通过最高法最高检报告 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4635032.shtml
3月15日 09:40 气象局长:今年气象灾害重于往年 台风影响更大 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4634995.shtml
3月15日 09:38 海洋局副局长:超35%大陆岸线纳入红线管控范围 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6626848.shtml
3月15日 09:25 全国人大闭幕会表决通过港澳人大选举草案 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1394644.shtml
3月15日 11:39 科学家发现抗寨卡病毒蛋白质 有望抑制艾滋病毒 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6649952.shtml
3月15日 11:38 体育总局局长:中超老板有钱任性 需严格整肃 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6649878.shtml
3月15日 11:23 李克强谈中美关系:虽经历风风雨雨但一直前行 http://news.sina.com.cn/c/2017-03-15/doc-ifycnikk0705650.shtml
3月15日 11:11 重庆新确诊1例人感染H7N9病例 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6645815.shtml
3月15日 11:05 赣州成江西房产限购第二城 本市居民限购1套 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4643474.shtml
3月15日 10:58 李克强：增长6.5%这个速度不低了 也很不容易 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1404173.shtml
3月15日 10:39 中消协:微商付费游戏等网络消费不满意率突出 http://news.sina.com.cn/o/2017-03-15/doc-ifychihc6639580.shtml
3月15日 10:28 部长通道回答问题创新高 46部门共回答95个问题 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6637866.shtml
3月15日 10:23 剁手党注意 今起7类商品不适用七日无理由退货 http://news.sina.com.cn/o/2017-03-15/doc-ifychavf2849234.shtml
3月15日 10:12 第十二届全国人民代表大会第五次会议(全文) http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4638516.shtml
3月15日 09:51 第十二届全国人民代表大会第五次会议闭幕 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4636094.shtml
3月15日 09:50 官方:决不让一个达不到安全条件煤矿复工复产 http://news.sina.com.cn/o/2017-03-15/doc-ifychavf2840952.shtml
3月15日 09:43 徐显明辞去全国人大常委会委员表决通过 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1396619.shtml
3月15日 09:40 全国人大闭幕会表决通过最高法最高检报告 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4635032.shtml
3月15日 09:40 气象局长:今年气象灾害重于往年 台风影响更大 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4634995.shtml
3月15日 09:38 海洋局副局长:超35%大陆岸线纳入红线管控范围 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6626848.shtml
3月15日 09:33 全国人大表决通过政府工作报告 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4634040.shtml
3月15日 09:25 全国人大闭幕会表决通过港澳人大选举草案 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1394644.shtml
3月15日 09:22 专家:个人信息泄露 几乎是当下电商行业通病 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1394335.shtml
3月15日 09:20 全国人大五次会议闭幕会表决通过民法总则 http://news.sina.com.cn/2017-03-15/doc-ifychhuq4632931.shtml
3月15日 09:18 刘亚宁任陕西延安政协党组副书记(图/简历) http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhus1393998.shtml
3月15日 09:14 人大代表包景岭:坚信三五年后能看到治霾成效 http://news.sina.com.cn/c/nd/2017-03-15/doc-ifychhuq4631782.shtml
3月15日 10:52 民进党党内争台南市长提名 台媒:1图看清这些人 http://news.sina.com.cn/c/2017-03-15/doc-ifycnikk0700152.shtml
3月15日 10:50 台湾“观光局”:游览车上导游必须进行安全解说 http://news.sina.com.cn/o/2017-03-15/doc-ifycnikk0699676.shtml
3月15日 05:48 人民日报海外版:“五千共谍在台湾”？鬼扯 http://news.sina.com.cn/c/gat/2017-03-15/doc-ifychhuq4619617.shtml
3月15日 02:08 “陆生共谍案”岛内持续延烧 台媒:莫吓跑陆生 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6589499.shtml
3月15日 02:08 马英九遭人告发教唆泄密被起诉 回应：公理何在 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6589496.shtml
3月15日 02:08 蔡当局拟推“反渗透法”被批“绿色恐怖” http://news.sina.com.cn/c/2017-03-15/doc-ifychavf2801729.shtml
3月15日 02:02 台媒:马耳他骑士团有望成台“外交新盟友” http://news.sina.com.cn/c/2017-03-15/doc-ifychavf2801590.shtml
3月15日 02:02 台北故宫拒绝本地合作却联手日本办展览被批 http://news.sina.com.cn/c/2017-03-15/doc-ifychihc6589341.shtml
3月14日 18:04 赌王儿子坐经济舱遭冷待 香港航空发文回应 http://news.sina.com.cn/c/gat/2017-03-14/doc-ifychhuq4566591.shtml
3月14日 16:58 大陆对台进口审核更严？检验检疫总局:一视同仁 http://news.sina.com.cn/o/2017-03-14/doc-ifychihc6546769.shtml
3月14日 16:53 台当局未见世卫大会邀请函 喊话世卫组织求门票 http://news.sina.com.cn/c/gat/2017-03-14/doc-ifychhus1313321.shtml
3月14日 16:09 台大学生称“中华民国国歌”应消失遭网友怒喷 http://news.sina.com.cn/c/2017-03-14/doc-ifychavf2753029.shtml
3月14日 14:44 曾荫权余罪9月底将重审 法官下令限制报道内容 http://news.sina.com.cn/c/gat/2017-03-14/doc-ifychhuq4508708.shtml
3月14日 13:36 马英九涉嫌泄密罪被台检方起诉 马办:公道何在 http://news.sina.com.cn/c/2017-03-14/doc-ifychihc6520462.shtml
3月14日 12:39 台北地检署起诉马英九教唆泄密 马全盘否认犯罪 http://news.sina.com.cn/c/gat/2017-03-14/doc-ifychhus1241691.shtml
3月14日 11:46 “立委”批文物盗版猖獗“台故宫”:已要求下架 http://news.sina.com.cn/c/2017-03-14/doc-ifychavf2722645.shtml
3月14日 11:17 台媒称大陆在台有5千间谍 台陆委会:不知道数据 http://news.sina.com.cn/c/2017-03-14/doc-ifychavf2718466.shtml
3月14日 10:42 多条来往港澳航线因大雾延误 乘客需留意航班 http://news.sina.com.cn/o/2017-03-14/doc-ifychihc6498659.shtml
3月14日 10:34 马英九被控教唆泄密案侦结 台北地检署今起诉 http://news.sina.com.cn/c/2017-03-14/doc-ifychavf2709238.shtml
3月14日 02:01 台湾名嘴:大陆打台湾 61万个小时都打不下来 http://news.sina.com.cn/c/gat/2017-03-14/doc-ifychhus1152392.shtml
3月15日 03:18 侠客岛：一个房字 多少心酸 http://news.sina.com.cn/c/zs/2017-03-15/doc-ifychhus1377249.shtml
3月14日 21:06 媒体：三四线楼市火爆 北漂还买得起家乡房吗 http://news.sina.com.cn/c/zs/2017-03-14/doc-ifychhus1360755.shtml
3月14日 11:02 欧洲媒体评中国两会:增长更“结实”向雾霾宣战 http://news.sina.com.cn/o/2017-03-14/doc-ifychavf2714137.shtml
3月14日 09:17 环球时报批女网红搞怪骂“乐天狗”:给爱国抹黑 http://news.sina.com.cn/c/zs/2017-03-14/doc-ifychhuq4424563.shtml
3月14日 05:00 媒体:“包子雷”式伪英雄主义 寒了英雄的心 http://news.sina.com.cn/o/2017-03-14/doc-ifychihc6452752.shtml
3月13日 03:37 学者:TPP没有中国无法实现利益最大化 http://news.sina.com.cn/c/zs/2017-03-13/doc-ifychihc6312215.shtml
3月12日 02:07 女权主义者：一提“女权”怎么就这么多人骂？ http://news.sina.com.cn/c/zs/2017-03-12/doc-ifychihc6242594.shtml
3月10日 12:20 三大运营商取消漫游费 谁最受益 http://news.sina.com.cn/c/nd/2017-03-10/doc-ifychhuq3659348.shtml
3月9日 09:37 美媒称中国推动制造强国战略:欧美担忧被挤走 http://news.sina.com.cn/c/zs/2017-03-09/doc-ifychhuq3368940.shtml
3月9日 04:43 丽江大量原住民外迁 旅游移民能否守住丽江古城 http://news.sina.com.cn/o/2017-03-09/doc-ifychihc5897833.shtml
3月8日 22:32 媒体:年收入12万以下不交个税 这事儿靠谱吗？ http://news.sina.com.cn/c/zs/2017-03-08/doc-ifychihc5886349.shtml
3月8日 08:37 媒体:财政部长这番话会让我们少交多少税 http://news.sina.com.cn/c/zs/2017-03-08/doc-ifycaasy7952439.shtml
3月8日 01:07 媒体:个税万元起征是让个税回归富人税本位 http://news.sina.com.cn/c/zs/2017-03-08/doc-ifyazwha4181974.shtml
3月6日 08:48 媒体:降低婚龄有利无害 赞同法定婚龄改为18岁 http://news.sina.com.cn/c/2017-03-06/doc-ifyazwha3912889.shtml
3月3日 09:02 美媒:更多留学生回国 分析称被中国经济所吸引 http://news.sina.com.cn/o/2017-03-03/doc-ifycaasy7397099.shtml
3月3日 02:44 环球时报:砸现代汽车是对制裁韩国的“高级黑” http://news.sina.com.cn/c/zs/2017-03-03/doc-ifyazwha3625633.shtml
3月3日 01:53 两会发布会背后:发言人团队内部模拟 随时演练 http://news.sina.com.cn/c/nd/2017-03-03/doc-ifyazwha3622206.shtml
3月2日 15:13 最高检谈惩治村霸:打击为其当保护伞的职务犯罪 http://news.sina.com.cn/o/2017-03-02/doc-ifyazwha3561182.shtml
3月2日 10:58 学者：中国要不要接替美国重启TPP？ http://news.sina.com.cn/c/zs/2017-03-02/doc-ifycaafp1513477.shtml
3月2日 07:35 专家献反制萨德十策:必要时可定点清除萨德阵地 http://news.sina.com.cn/c/zs/2017-03-02/doc-ifycaafm4688980.shtml
1月31日 19:12 大马沉船事故确认7名苏州游客身份 1死1失联 http://news.sina.com.cn/c/sd/2017-01-31/doc-ifxzyxmu8444643.shtml
1月19日 00:01 中央时隔17年再下文加强政法队伍建设 有何用意 http://news.sina.com.cn/o/2017-01-19/doc-ifxzunxf1377803.shtml
1月17日 01:59 哈萨克斯坦人集会反对姑娘嫁中国人 怕他们分地 http://news.sina.com.cn/o/2017-01-17/doc-ifxzqnva3778799.shtml
1月12日 16:36 美没收中国红通3号人物乔建军前妻赵世兰房产 http://news.sina.com.cn/c/sd/2017-01-12/doc-ifxzqnip0848945.shtml
1月12日 13:50 中科院最美的玫瑰走了 她当得起这一声“先生” http://news.sina.com.cn/c/sd/2017-01-12/doc-ifxzqnip0817768.shtml
12月16日 21:53 落马贪官人大代表职务 为何有的请辞有的被罢免 http://news.sina.com.cn/c/sd/2016-12-16/doc-ifxytqqn8780142.shtml
12月5日 08:20 大米走私链条曝光:进行抛光搀兑后销往多地市场 http://news.sina.com.cn/c/sd/2016-12-05/doc-ifxyicnf1572611.shtml
12月1日 19:23 江苏广电总台原女台长被带走调查 疑涉经济问题 http://news.sina.com.cn/c/sd/2016-12-02/doc-ifxyhwyy0408568.shtml
11月29日 03:39 小鱼塘兽药失禁 多地水产均曾检出孔雀石绿(图) http://news.sina.com.cn/c/sd/2016-11-29/doc-ifxyawxa3005371.shtml
11月28日 23:53 国安部长任中政委委员 曾弃清华北大选这所大学 http://news.sina.com.cn/c/sd/2016-11-29/doc-ifxyasmv2125402.shtml
11月28日 11:35 雾霾中现耐药菌人类将面临无药可医？揭秘真相 http://news.sina.com.cn/c/sd/2016-11-28/doc-ifxyawmm3624224.shtml
11月28日 07:50 舰载机飞行员牺牲细节:4.4秒生死瞬间欲救战机 http://news.sina.com.cn/c/sd/2016-11-28/doc-ifxyawxa2907507.shtml
11月28日 05:41 贵州童工多因贫困外出打工 有时连吃盐都成问题 http://news.sina.com.cn/o/2016-11-28/doc-ifxyasmv2025198.shtml
11月27日 14:01 湖南从严推进县乡人大换届选举:铭记衡阳案教训 http://news.sina.com.cn/c/sd/2016-11-27/doc-ifxyawxa2866597.shtml
11月21日 15:00 北京国I国Ⅱ车辆明年2月15日起五环内限行 http://news.sina.com.cn/c/sd/2016-11-21/doc-ifxxwrwh4831425.shtml
11月21日 14:44 北京重污染应急预案为何5年4版本 http://news.sina.com.cn/c/2016-11-21/doc-ifxxwsix4256007.shtml
11月15日 11:47 中央督察组:黑龙江自然保护区违建问题严重 http://news.sina.com.cn/c/2016-11-15/doc-ifxxsmuu5714118.shtml
11月15日 07:16 这些贪官为什么被判终身监禁 http://news.sina.com.cn/c/sd/2016-11-15/doc-ifxxsmic6290399.shtml
11月6日 05:09 遭贾敬龙射杀村支书之子接任父职 被指村官世袭 http://news.sina.com.cn/c/sd/2016-11-06/doc-ifxxnety7454000.shtml
11月6日 03:36 揭秘职称评选之痛 教授称专注教学就是毁灭自己 http://news.sina.com.cn/c/sd/2016-11-06/doc-ifxxnety7452898.shtml
'''