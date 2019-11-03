# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/10/10
Email: hanscalcai@163.com
'''

eng_nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~￥…（）：，。—！·【】%‰'
riyu = 'あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわをんアイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤユヨラリルレロワヲンヴ'
cn_words = ' \'疗绚诚娇溜题贿者廖更纳加奉公一就汴计与路房原妇208-—7其>:：],，·…～（）骑刈全消昏傈安久钟嗅不影处驽蜿资关椤地瘸专问忖票嫉炎韵要月田节陂鄙捌备拳伺眼网盎大傍心东愉汇蹿科每业里航晏字平录先13彤鲶产稍督腴有象岳注绍在泺文定核名水过理让偷率等这发”为含肥酉相鄱七编猥锛日镀蒂掰倒辆栾栗综涩州雌滑馀了机块司宰甙兴矽抚保用沧秩如收息滥页疑埠!！姥异橹钇向下跄的椴沫国绥獠报开民蜇何分凇长讥藏掏施羽中讲派嘟人提浼间世而古多倪唇饯控庚首赛蜓味断制觉技替艰溢潮夕钺外摘枋动双单啮户枇确锦曜杜或能效霜盒然侗电晁放步鹃新杖蜂吒濂瞬评总隍对独合也是府青天诲墙组滴级邀帘示已时骸仄泅和遨店雇疫持巍踮境只亨目鉴崤闲体泄杂作般轰化解迂诿蛭璀腾告版服省师小规程线海办引二桧牌砺洄裴修图痫胡许犊事郛基柴呼食研奶律蛋因葆察戏褒戒再李骁工貂油鹅章啄休场给睡纷豆器捎说敏学会浒设诊格廓查来霓室溆￠诡寥焕舜柒狐回戟砾厄实翩尿五入径惭喹股宇篝|;美期云九祺扮靠锝槌系企酰阊暂蚕忻豁本羹执条钦H獒限进季楦于芘玖铋茯未答粘括样精欠矢甥帷嵩扣令仔风皈行支部蓉刮站蜡救钊汗松嫌成可.鹤院从交政怕活调球局验髌第韫谗串到圆年米/*友忿检区看自敢刃个兹弄流留同没齿星聆轼湖什三建蛔儿椋汕震颧鲤跟力情璺铨陪务指族训滦鄣濮扒商箱十召慷辗所莞管护臭横硒嗓接侦六露党馋驾剖高侬妪幂猗绺骐央酐孝筝课徇缰门男西项句谙瞒秃篇教碲罚声呐景前富嘴鳌稀免朋啬睐去赈鱼住肩愕速旁波厅健茼厥鲟谅投攸炔数方击呋谈绩别愫僚躬鹧胪炳招喇膨泵蹦毛结54谱识陕粽婚拟构且搜任潘比郢妨醪陀桔碘扎选哈骷楷亿明缆脯监睫逻婵共赴淝凡惦及达揖谩澹减焰蛹番祁柏员禄怡峤龙白叽生闯起细装谕竟聚钙上导渊按艾辘挡耒盹饪臀记邮蕙受各医搂普滇朗茸带翻酚(光堤墟蔷万幻〓瑙辈昧盏亘蛀吉铰请子假闻税井诩哨嫂好面琐校馊鬣缂营访炖占农缀否经钚棵趟张亟吏茶谨捻论迸堂玉信吧瞠乡姬寺咬溏苄皿意赉宝尔钰艺特唳踉都荣倚登荐丧奇涵批炭近符傩感道着菊虹仲众懈濯颞眺南释北缝标既茗整撼迤贲挎耱拒某妍卫哇英矶藩治他元领膜遮穗蛾飞荒棺劫么市火温拈棚洼转果奕卸迪伸泳斗邡侄涨屯萋胭氡崮枞惧冒彩斜手豚随旭淑妞形菌吲沱争驯歹挟兆柱传至包内响临红功弩衡寂禁老棍耆渍织害氵渑布载靥嗬虽苹咨娄库雉榜帜嘲套瑚亲簸欧边6腿旮抛吹瞳得镓梗厨继漾愣憨士策窑抑躯襟脏参贸言干绸鳄穷藜音折详)举悍甸癌黎谴死罩迁寒驷袖媒蒋掘模纠恣观祖蛆碍位稿主澧跌筏京锏帝贴证糠才黄鲸略炯饱四出园犀牧容汉杆浈汰瑷造虫瘩怪驴济应花沣谔夙旅价矿以考su呦晒巡茅准肟瓴詹仟褂译桌混宁怦郑抿些余鄂饴攒珑群阖岔琨藓预环洮岌宀杲瀵最常囡周踊女鼓袭喉简范薯遐疏粱黜禧法箔斤遥汝奥直贞撑置绱集她馅逗钧橱魉[恙躁唤9旺膘待脾惫购吗依盲度瘿蠖俾之镗拇鲵厝簧续款展啃表剔品钻腭损清锶统涌寸滨贪链吠冈伎迥咏吁览防迅失汾阔逵绀蔑列川凭努熨揪利俱绉抢鸨我即责膦易毓鹊刹玷岿空嘞绊排术估锷违们苟铜播肘件烫审鲂广像铌惰铟巳胍鲍康憧色恢想拷尤疳知SYFDA峄裕帮握搔氐氘难墒沮雨叁缥悴藐湫娟苑稠颛簇后阕闭蕤缚怎佞码嘤蔡痊舱螯帕赫昵升烬岫、疵蜻髁蕨隶烛械丑盂梁强鲛由拘揉劭龟撤钩呕孛费妻漂求阑崖秤甘通深补赃坎床啪承吼量暇钼烨阂擎脱逮称P神属矗华届狍葑汹育患窒蛰佼静槎运鳗庆逝曼疱克代官此麸耧蚌晟例础榛副测唰缢迹灬霁身岁赭扛又菡乜雾板读陷徉贯郁虑变钓菜圾现琢式乐维渔浜左吾脑钡警T啵拴偌漱湿硕止骼魄积燥联踢玛|则窿见振畿送班钽您赵刨印讨踝籍谡舌崧汽蔽沪酥绒怖财帖肱私莎勋羔霸励哼帐将帅渠纪婴娩岭厘滕吻伤坝冠戊隆瘁介涧物黍并姗奢蹑掣垸锴命箍捉病辖琰眭迩艘绌繁寅若毋思诉类诈燮轲酮狂重反职筱县委磕绣奖晋濉志徽肠呈獐坻口片碰几村柿劳料获亩惕晕厌号罢池正鏖煨家棕复尝懋蜥锅岛扰队坠瘾钬@卧疣镇譬冰彷频黯据垄采八缪瘫型熹砰楠襁箐但嘶绳啤拍盥穆傲洗盯塘怔筛丿台恒喂葛永￥烟酒桦书砂蚝缉态瀚袄圳轻蛛超榧遛姒奘铮右荽望偻卡丶氰附做革索戚坨桷唁垅榻岐偎坛莨山殊微骇陈爨推嗝驹澡藁呤卤嘻糅逛侵郓酌德摇※鬃被慨殡羸昌泡戛鞋河宪沿玲鲨翅哽源铅语照邯址荃佬顺鸳町霭睾瓢夸椁晓酿痈咔侏券噎湍签嚷离午尚社锤背孟使浪缦潍鞅军姹驶笑鳟鲁》孽钜绿洱礴焯椰颖囔乌孔巴互性椽哞聘昨早暮胶炀隧低彗昝铁呓氽藉喔癖瑗姨权胱韦堑蜜酋楝砝毁靓歙锲究屋喳骨辨碑武鸠宫辜烊适坡殃培佩供走蜈迟翼况姣凛浔吃飘债犟金促苛崇坂莳畔绂兵蠕斋根砍亢欢恬崔剁餐榫快扶‖濒缠鳜当彭驭浦篮昀锆秸钳弋娣瞑夷龛苫拱致%嵊障隐弑初娓抉汩累蓖"唬助苓昙押毙破城郧逢嚏獭瞻溱婿赊跨恼璧萃姻貉灵炉密氛陶砸谬衔点琛沛枳层岱诺脍榈埂征冷裁打蹴素瘘逞蛐聊激腱萘踵飒蓟吆取咙簋涓矩曝挺揣座你史舵焱尘苏笈脚溉榨诵樊邓焊义庶儋蟋蒲赦呷杞诠豪还试颓茉太除紫逃痴草充鳕珉祗墨渭烩蘸慕璇镶穴嵘恶骂险绋幕碉肺戳刘潞秣纾潜銮洛须罘销瘪汞兮屉r林厕质探划狸殚善煊烹〒锈逯宸辍泱柚袍远蹋嶙绝峥娥缍雀徵认镱谷=贩勉撩鄯斐洋非祚泾诒饿撬威晷搭芍锥笺蓦候琊档礁沼卵荠忑朝凹瑞头仪弧孵畏铆突衲车浩气茂悖厢枕酝戴湾邹飚攘锂写宵翁岷无喜丈挑嗟绛殉议槽具醇淞笃郴阅饼底壕砚弈询缕庹翟零筷暨舟闺甯撞麂茌蔼很珲捕棠角阉媛娲诽剿尉爵睬韩诰匣危糍镯立浏阳少盆舔擘匪申尬铣旯抖赘瓯居ˇ哮游锭茏歌坏甚秒舞沙仗劲潺阿燧郭嗖霏忠材奂耐跺砀输岖媳氟极摆灿今扔腻枝奎药熄吨话q额慑嘌协喀壳埭视著於愧陲翌峁颅佛腹聋侯咎叟秀颇存较罪哄岗扫栏钾羌己璨枭霉煌涸衿键镝益岢奏连夯睿冥均糖狞蹊稻爸刿胥煜丽肿璃掸跚灾垂樾濑乎莲窄犹撮战馄软络显鸢胸宾妲恕埔蝌份遇巧瞟粒恰剥桡博讯凯堇阶滤卖斌骚彬兑磺樱舷两娱福仃差找桁÷净把阴污戬雷碓蕲楚罡焖抽妫咒仑闱尽邑菁爱贷沥鞑牡嗉崴骤塌嗦订拮滓捡锻次坪杩臃箬融珂鹗宗枚降鸬妯阄堰盐毅必杨崃俺甬状莘货耸菱腼铸唏痤孚澳懒溅翘疙杷淼缙骰喊悉砻坷艇赁界谤纣宴晃茹归饭梢铡街抄肼鬟苯颂撷戈炒咆茭瘙负仰客琉铢封卑珥椿镧窨鬲寿御袤铃萎砖餮脒裳肪孕嫣馗嵇恳氯江石褶冢祸阻狈羞银靳透咳叼敷芷啥它瓤兰痘懊逑肌往捺坊甩呻〃沦忘膻祟菅剧崆智坯臧霍墅攻眯倘拢骠铐庭岙瓠′缺泥迢捶?？郏喙掷沌纯秘种听绘固螨团香盗妒埚蓝拖旱荞铀血遏汲辰叩拽幅硬惶桀漠措泼唑齐肾念酱虚屁耶旗砦闵婉馆拭绅韧忏窝醋葺顾辞倜堆辋逆玟贱疾董惘倌锕淘嘀莽俭笏绑鲷杈择蟀粥嗯驰逾案谪褓胫哩昕颚鲢绠躺鹄崂儒俨丝尕泌啊萸彰幺吟骄苣弦脊瑰〈诛镁析闪剪侧哟框螃守嬗燕狭铈缮概迳痧鲲俯售笼痣扉挖满咋援邱扇歪便玑绦峡蛇叨〖泽胃斓喋怂坟猪该蚬炕弥赞棣晔娠挲狡创疖铕镭稷挫弭啾翔粉履苘哦楼秕铂土锣瘟挣栉习享桢袅磨桂谦延坚蔚噗署谟猬钎恐嬉雒倦衅亏璩睹刻殿王算雕麻丘柯骆丸塍谚添鲈垓桎蚯芥予飕镦谌窗醚菀亮搪莺蒿羁足J真轶悬衷靛翊掩哒炅掐冼妮l谐稚荆擒犯陵虏浓崽刍陌傻孜千靖演矜钕煽杰酗渗伞栋俗泫戍罕沾疽灏煦芬磴叱阱榉湃蜀叉醒彪租郡篷屎良垢隗弱陨峪砷掴颁胎雯绵贬沐撵隘篙暖曹陡栓填臼彦瓶琪潼哪鸡摩啦俟锋域耻蔫疯纹撇毒绶痛酯忍爪赳歆嘹辕烈册朴钱吮毯癜娃谀邵厮炽璞邃丐追词瓒忆轧芫谯喷弟半冕裙掖墉绮寝苔势顷褥切衮君佳嫒蚩霞佚洙逊镖暹唛&殒顶碗獗轭铺蛊废恹汨崩珍那杵曲纺夏薰傀闳淬姘舀拧卷楂恍讪厩寮篪赓乘灭盅鞣沟慎挂饺鼾杳树缨丛絮娌臻嗳篡侩述衰矛圈蚜匕筹匿濞晨叶骋郝挚蚴滞增侍描瓣吖嫦蟒匾圣赌毡癞恺百曳需篓肮庖帏卿驿遗蹬鬓骡歉芎胳屐禽烦晌寄媾狄翡苒船廉终痞殇々畦饶改拆悻萄￡瓿乃訾桅匮溧拥纱铍骗蕃龋缬父佐疚栎醍掳蓄x惆颜鲆榆〔猎敌暴谥鲫贾罗玻缄扦芪癣落徒臾恿猩托邴肄牵春陛耀刊拓蓓邳堕寇枉淌啡湄兽酷萼碚濠萤夹旬戮梭琥椭昔勺蜊绐晚孺僵宣摄冽旨萌忙蚤眉噼蟑付契瓜悼颡壁曾窕颢澎仿俑浑嵌浣乍碌褪乱蔟隙玩剐葫箫纲围伐决伙漩瑟刑肓镳缓蹭氨皓典畲坍铑檐塑洞倬储胴淳戾吐灼惺妙毕珐缈虱盖羰鸿磅谓髅娴苴唷蚣霹抨贤唠犬誓逍庠逼麓籼釉呜碧秧氩摔霄穸纨辟妈映完牛缴嗷炊恩荔茆掉紊慌莓羟阙萁磐另蕹辱鳐湮吡吩唐睦垠舒圜冗瞿溺芾囱匠僳汐菩饬漓黑霰浸濡窥毂蒡兢驻鹉芮诙迫雳厂忐臆猴鸣蚪栈箕羡渐莆捍眈哓趴蹼埕嚣骛宏淄斑噜严瑛垃椎诱压庾绞焘廿抡迄棘夫纬锹眨瞌侠脐竞瀑孳骧遁姜颦荪滚萦伪逸粳爬锁矣役趣洒颔诏逐奸甭惠攀蹄泛尼拼阮鹰亚颈惑勒〉际肛爷刚钨丰养冶鲽辉蔻画覆皴妊麦返醉皂擀〗酶凑粹悟诀硖港卜z杀涕±舍铠抵弛段敝镐奠拂轴跛袱et沉菇俎薪峦秭蟹历盟菠寡液肢喻染裱悱抱氙赤捅猛跑氮谣仁尺辊窍烙衍架擦倏璐瑁币楞胖夔趸邛惴饕虔蝎§哉贝宽辫炮扩饲籽魏菟锰伍猝末琳哚蛎邂呀姿鄞却歧仙恸椐森牒寤袒婆虢雅钉朵贼欲苞寰故龚坭嘘咫礼硷兀睢汶’铲烧绕诃浃钿哺柜讼颊璁腔洽咐脲簌筠镣玮鞠谁兼姆挥梯蝴谘漕刷躏宦弼b垌劈麟莉揭笙渎仕嗤仓配怏抬错泯镊孰猿邪仍秋鼬壹歇吵炼<尧射柬廷胧霾凳隋肚浮梦祥株堵退L鹫跎凶毽荟炫栩玳甜沂鹿顽伯爹赔蛴徐匡欣狰缸雹蟆疤默沤啜痂衣禅wih辽葳黝钗停沽棒馨颌肉吴硫悯劾娈马啧吊悌镑峭帆瀣涉咸疸滋泣翦拙癸钥蜒+尾庄凝泉婢渴谊乞陆锉糊鸦淮IBN晦弗乔庥葡尻席橡傣渣拿惩麋斛缃矮蛏岘鸽姐膏催奔镒喱蠡摧钯胤柠拐璋鸥卢荡倾^_珀逄萧塾掇贮笆聂圃冲嵬M滔笕值炙偶蜱搐梆汪蔬腑鸯蹇敞绯仨祯谆梧糗鑫啸豺囹猾巢柄瀛筑踌沭暗苁鱿蹉脂蘖牢热木吸溃宠序泞偿拜檩厚朐毗螳吞媚朽担蝗橘畴祈糟盱隼郜惜珠裨铵焙琚唯咚噪骊丫滢勤棉呸咣淀隔蕾窈饨挨煅短匙粕镜赣撕墩酬馁豌颐抗酣氓佑搁哭递耷涡桃贻碣截瘦昭镌蔓氚甲猕蕴蓬散拾纛狼猷铎埋旖矾讳囊糜迈粟蚂紧鲳瘢栽稼羊锄斟睁桥瓮蹙祉醺鼻昱剃跳篱跷蒜翎宅晖嗑壑峻癫屏狠陋袜途憎祀莹滟佶溥臣约盛峰磁慵婪拦莅朕鹦粲裤哎疡嫖琵窟堪谛嘉儡鳝斩郾驸酊妄胜贺徙傅噌钢栅庇恋匝巯邈尸锚粗佟蛟薹纵蚊郅绢锐苗俞篆淆膀鲜煎诶秽寻涮刺怀噶巨褰魅灶灌桉藕谜舸薄搀恽借牯痉渥愿亓耘杠柩锔蚶钣珈喘蹒幽赐稗晤莱泔扯肯菪裆腩豉疆骜腐倭珏唔粮亡润慰伽橄玄誉醐胆龊粼塬陇彼削嗣绾芽妗垭瘴爽薏寨龈泠弹赢漪猫嘧涂恤圭茧烽屑痕巾赖荸凰腮畈亵蹲偃苇澜艮换骺烘苕梓颉肇哗悄氤涠葬屠鹭植竺佯诣鲇瘀鲅邦移滁冯耕癔戌茬沁巩悠湘洪痹锟循谋腕鳃钠捞焉迎碱伫急榷奈邝卯辄皲卟醛畹忧稳雄昼缩阈睑扌耗曦涅捏瞧邕淖漉铝耦禹湛喽莼琅诸苎纂硅始嗨傥燃臂赅嘈呆贵屹壮肋亍蚀卅豹腆邬迭浊}童螂捐圩勐触寞汊壤荫膺渌芳懿遴螈泰蓼蛤茜舅枫朔膝眙避梅判鹜璜牍缅垫藻黔侥惚懂踩腰腈札丞唾慈顿摹荻琬~斧沈滂胁胀幄莜Z匀鄄掌绰茎焚赋萱谑汁铒瞎夺蜗野娆冀弯篁懵灞隽芡脘俐辩芯掺喏膈蝈觐悚踹蔗熠鼠呵抓橼峨畜缔禾崭弃熊摒凸拗穹蒙抒祛劝闫扳阵醌踪喵侣搬仅荧赎蝾琦买婧瞄寓皎冻赝箩莫瞰郊笫姝筒枪遣煸袋舆痱涛母〇启践耙绲盘遂昊搞槿诬纰泓惨檬亻越Co憩熵祷钒暧塔阗胰咄娶魔琶钞邻扬杉殴咽弓〆髻】吭揽霆拄殖脆彻岩芝勃辣剌钝嘎甄佘皖伦授徕憔挪皇庞稔芜踏溴兖卒擢饥鳞煲‰账颗叻斯捧鳍琮讹蛙纽谭酸兔莒睇伟觑羲嗜宜褐旎辛卦诘筋鎏溪挛熔阜晰鳅丢奚灸呱献陉黛鸪甾萨疮拯洲疹辑叙恻谒允柔烂氏逅漆拎惋扈湟纭啕掬擞哥忽涤鸵靡郗瓷扁廊怨雏钮敦E懦憋汀拚啉腌岸f痼瞅尊咀眩飙忌仝迦熬毫胯篑茄腺凄舛碴锵诧羯後漏汤宓仞蚁壶谰皑铄棰罔辅晶苦牟闽\\烃饮聿丙蛳朱煤涔鳖犁罐荼砒淦妤黏戎孑婕瑾戢钵枣捋砥衩狙桠稣阎肃梏诫孪昶婊衫嗔侃塞蜃樵峒貌屿欺缫阐栖诟珞荭吝萍嗽恂啻蜴磬峋俸豫谎徊镍韬魇晴U囟猜蛮坐囿伴亭肝佗蝠妃胞滩榴氖垩苋砣扪馏姓轩厉夥侈禀垒岑赏钛辐痔披纸碳“坞蠓挤荥沅悔铧帼蒌蝇apyng哀浆瑶凿桶馈皮奴苜佤伶晗铱炬优弊氢恃甫攥端锌灰稹炝曙邋亥眶碾拉萝绔捷浍腋姑菖凌涞麽锢桨潢绎镰殆锑渝铬困绽觎匈糙暑裹鸟盔肽迷綦『亳佝俘钴觇骥仆疝跪婶郯瀹唉脖踞针晾忒扼瞩叛椒疟嗡邗肆跆玫忡捣咧唆艄蘑潦笛阚沸泻掊菽贫斥髂孢镂赂麝鸾屡衬苷恪叠希粤爻喝茫惬郸绻庸撅碟宄妹膛叮饵崛嗲椅冤搅咕敛尹垦闷蝉霎勰败蓑泸肤鹌幌焦浠鞍刁舰乙竿裔。茵函伊兄丨娜匍謇莪宥似蝽翳酪翠粑薇祢骏赠叫Q噤噻竖芗莠潭俊羿耜O郫趁嗪囚蹶芒洁笋鹑敲硝啶堡渲揩』携宿遒颍扭棱割萜蔸葵琴捂饰衙耿掠募岂窖涟蔺瘤柞瞪怜匹距楔炜哆秦缎幼茁绪痨恨楸娅瓦桩雪嬴伏榔妥铿拌眠雍缇‘卓搓哌觞噩屈哧髓咦巅娑侑淫膳祝勾姊莴胄疃薛蜷胛巷芙芋熙闰勿窃狱剩钏幢陟铛慧靴耍k浙浇飨惟绗祜澈啼咪磷摞诅郦抹跃壬吕肖琏颤尴剡抠凋赚泊津宕殷倔氲漫邺涎怠$垮荬遵俏叹噢饽蜘孙筵疼鞭羧牦箭潴c眸祭髯啖坳愁芩驮倡巽穰沃胚怒凤槛剂趵嫁v邢灯鄢桐睽檗锯槟婷嵋圻诗蕈颠遭痢芸怯馥竭锗徜恭遍籁剑嘱苡龄僧桑潸弘澶楹悲讫愤腥悸谍椹呢桓葭攫阀翰躲敖柑郎笨橇呃魁燎脓葩磋垛玺狮沓砜蕊锺罹蕉翱虐闾巫旦茱嬷枯鹏贡芹汛矫绁拣禺佃讣舫惯乳趋疲挽岚虾衾蠹蹂飓氦铖孩稞瑜壅掀勘妓畅髋W庐牲蓿榕练垣唱邸菲昆婺穿绡麒蚱掂愚泷涪漳妩娉榄讷觅旧藤煮呛柳腓叭庵烷阡罂蜕擂猖咿媲脉【沏貅黠熏哲烁坦酵兜×潇撒剽珩圹乾摸樟帽嗒襄魂轿憬锡〕喃皆咖隅脸残泮袂鹂珊囤捆咤误徨闹淙芊淋怆囗拨梳渤RG绨蚓婀幡狩麾谢唢裸旌伉纶裂驳砼咛澄樨蹈宙澍倍貔操勇蟠摈砧虬够缁悦藿撸艹摁淹豇虎榭ˉ吱d°喧荀踱侮奋偕饷犍惮坑璎徘宛妆袈倩窦昂荏乖K怅撰鳙牙袁酞X痿琼闸雁趾荚虻涝《杏韭偈烤绫鞘卉症遢蓥诋杭荨匆竣簪辙敕虞丹缭咩黟m淤瑕咂铉硼茨嶂痒畸敬涿粪窘熟叔嫔盾忱裘憾梵赡珙咯娘庙溯胺葱痪摊荷卞乒髦寐铭坩胗枷爆溟嚼羚砬轨惊挠罄竽菏氧浅楣盼枢炸阆杯谏噬淇渺俪秆墓泪跻砌痰垡渡耽釜讶鳎煞呗韶舶绷鹳缜旷铊皱龌檀霖奄槐艳蝶旋哝赶骞蚧腊盈丁`蜚矸蝙睨嚓僻鬼醴夜彝磊笔拔栀糕厦邰纫逭纤眦膊馍躇烯蘼冬诤暄骶哑瘠」臊丕愈咱螺擅跋搏硪谄笠淡嘿骅谧鼎皋姚歼蠢驼耳胬挝涯狗蒽孓犷凉芦箴铤孤嘛坤V茴朦挞尖橙诞搴碇洵浚帚蜍漯柘嚎讽芭荤咻祠秉跖埃吓糯眷馒惹娼鲑嫩讴轮瞥靶褚乏缤宋帧删驱碎扑俩俄偏涣竹噱皙佰渚唧斡#镉刀崎筐佣夭贰肴峙哔艿匐牺镛缘仡嫡劣枸堀梨簿鸭蒸亦稽浴{衢束槲j阁揍疥棋潋聪窜乓睛插冉阪苍搽「蟾螟幸仇樽撂慢跤幔俚淅覃觊溶妖帛侨曰妾泗犇'
cn_words_first = '一乙二十丁厂七卜八人入儿匕几九刁了刀力乃又三干于亏工土士才下寸大丈与万上小口山巾千乞川亿个夕久么勺凡丸及广亡门丫义之尸己已巳弓子卫也女刃飞习叉马乡丰王开井天夫元无云专丐扎艺木五支厅不犬太区历歹友尤匹车巨牙屯戈比互切瓦止少曰日中贝冈内水见午牛手气毛壬升夭长仁什片仆化仇币仍仅斤爪反介父从仑今凶分乏公仓月氏勿欠风丹匀乌勾凤六文亢方火为斗忆计订户认冗讥心尺引丑巴孔队办以允予邓劝双书幻玉刊未末示击打巧正扑卉扒功扔去甘世艾古节本术可丙左厉石右布夯戊龙平灭轧东卡北占凸卢业旧帅归旦目且叶甲申叮电号田由只叭史央兄叽叼叫叩叨另叹冉皿凹囚四生矢失乍禾丘付仗代仙们仪白仔他斥瓜乎丛令用甩印尔乐句匆册卯犯外处冬鸟务包饥主市立冯玄闪兰半汁汇头汉宁穴它讨写让礼训议必讯记永司尼民弗弘出辽奶奴召加皮边孕发圣对台矛纠母幼丝邦式迂刑戎动扛寺吉扣考托老巩圾执扩扫地场扬耳芋共芒亚芝朽朴机权过臣吏再协西压厌戌在百有存而页匠夸夺灰达列死成夹夷轨邪尧划迈毕至此贞师尘尖劣光当早吁吐吓虫曲团吕同吊吃因吸吗吆屿屹岁帆回岂则刚网肉年朱先丢廷舌竹迁乔迄伟传乒乓休伍伏优臼伐延仲件任伤价伦份华仰仿伙伪自伊血向似后行舟全会杀合兆企众爷伞创肌肋朵杂危旬旨旭负匈名各多争色壮冲妆冰庄庆亦刘齐交衣次产决亥充妄闭问闯羊并关米灯州汗污江汛池汝汤忙兴宇守宅字安讲讳军讶许讹论讼农讽设访诀寻那迅尽导异弛孙阵阳收阶阴防奸如妇妃好她妈戏羽观欢买红驮纤驯约级纪驰纫巡寿弄麦玖玛形进戒吞远违韧运扶抚坛技坏抠扰扼拒找批址扯走抄贡汞坝攻赤折抓扳抡扮抢孝坎均抑抛投坟坑抗坊抖护壳志块扭声把报拟却抒劫芙芜苇芽花芹芥芬苍芳严芦芯劳克芭苏杆杠杜材村杖杏杉巫极李杨求甫匣更束吾豆两酉丽医辰励否还尬歼来连轩步卤坚肖旱盯呈时吴助县里呆吱吠呕园旷围呀吨足邮男困吵串员呐听吟吩呛吻吹呜吭吧邑吼囤别吮岖岗帐财针钉牡告我乱利秃秀私每兵估体何佐佑但伸佃作伯伶佣低你住位伴身皂伺佛囱近彻役返余希坐谷妥含邻岔肝肛肚肘肠龟甸免狂犹狈角删条彤卵灸岛刨迎饭饮系言冻状亩况床库庇疗吝应这冷庐序辛弃冶忘闰闲间闷判兑灶灿灼弟汪沐沛汰沥沙汽沃沦汹泛沧没沟沪沈沉沁怀忧忱快完宋宏牢究穷灾良证启评补初社祀识诈诉罕诊词译君灵即层屁尿尾迟局改张忌际陆阿陈阻附坠妓妙妖姊妨妒努忍劲矣鸡纬驱纯纱纲纳驳纵纷纸纹纺驴纽奉玩环武青责现玫表规抹卦坷坯拓拢拔坪拣坦担坤押抽拐拖者拍顶拆拎拥抵拘势抱拄垃拉拦幸拌拧拂拙招坡披拨择抬拇拗其取茉苦昔苛若茂苹苗英苟苑苞范直茁茄茎苔茅枉林枝杯枢柜枚析板松枪枫构杭杰述枕丧或画卧事刺枣雨卖郁矾矿码厕奈奔奇奋态欧殴垄妻轰顷转斩轮软到非叔歧肯齿些卓虎虏肾贤尚旺具味果昆国哎咕昌呵畅明易咙昂迪典固忠呻咒咋咐呼鸣咏呢咄咖岸岩帖罗帜帕岭凯败账贩贬购贮图钓制知迭氛垂牧物乖刮秆和季委秉佳侍岳供使例侠侥版侄侦侣侧凭侨佩货侈依卑的迫质欣征往爬彼径所舍金刹命肴斧爸采觅受乳贪念贫忿肤肺肢肿胀朋股肮肪肥服胁周昏鱼兔狐忽狗狞备饰饱饲变京享庞店夜庙府底疟疙疚剂卒郊庚废净盲放刻育氓闸闹郑券卷单炬炒炊炕炎炉沫浅法泄沽河沾泪沮油泊沿泡注泣泞泻泌泳泥沸沼波泼泽治怔怯怖性怕怜怪怡学宝宗定宠宜审宙官空帘宛实试郎诗肩房诚衬衫视祈话诞诡询该详建肃录隶帚屉居届刷屈弧弥弦承孟陋陌孤陕降函限妹姑姐姓妮始姆迢驾叁参艰线练组绅细驶织驹终驻绊驼绍绎经贯契贰奏春帮玷珍玲珊玻毒型拭挂封持拷拱项垮挎城挟挠政赴赵挡拽哉挺括垢拴拾挑垛指垫挣挤拼挖按挥挪拯某甚荆茸革茬荐巷带草茧茵茶荒茫荡荣荤荧故胡荫荔南药标栈柑枯柄栋相查柏栅柳柱柿栏柠树勃要柬咸威歪研砖厘厚砌砂泵砚砍面耐耍牵鸥残殃轴轻鸦皆韭背战点虐临览竖省削尝昧盹是盼眨哇哄哑显冒映星昨咧昭畏趴胃贵界虹虾蚁思蚂虽品咽骂勋哗咱响哈哆咬咳咪哪哟炭峡罚贱贴贻骨幽钙钝钞钟钢钠钥钦钧钩钮卸缸拜看矩毡氢怎牲选适秒香种秋科重复竿段便俩贷顺修俏保促俄俐侮俭俗俘信皇泉鬼侵禹侯追俊盾待徊衍律很须叙剑逃食盆胚胧胆胜胞胖脉胎勉狭狮独狰狡狱狠贸怨急饵饶蚀饺饼峦弯将奖哀亭亮度迹庭疮疯疫疤咨姿亲音帝施闺闻闽阀阁差养美姜叛送类迷籽娄前首逆兹总炼炸烁炮炫烂剃洼洁洪洒柒浇浊洞测洗活派洽染洛浏济洋洲浑浓津恃恒恢恍恬恤恰恼恨举觉宣宦室宫宪突穿窃客诫冠诬语扁袄祖神祝祠误诱诲说诵垦退既屋昼屏屎费陡逊眉孩陨除险院娃姥姨姻娇姚娜怒架贺盈勇怠癸蚤柔垒绑绒结绕骄绘给绚骆络绝绞骇统耕耘耗耙艳泰秦珠班素匿蚕顽盏匪捞栽捕埂捂振载赶起盐捎捍捏埋捉捆捐损袁捌都哲逝捡挫换挽挚热恐捣壶捅埃挨耻耿耽聂恭莽莱莲莫莉荷获晋恶莹莺真框梆桂桔栖档桐株桥桦栓桃格桩校核样根索哥速逗栗贾酌配翅辱唇夏砸砰砾础破原套逐烈殊殉顾轿较顿毙致柴桌虑监紧党逞晒眠晓哮唠鸭晃哺晌剔晕蚌畔蚣蚊蚪蚓哨哩圃哭哦恩鸯唤唁哼唧啊唉唆罢峭峨峰圆峻贼贿赂赃钱钳钻钾铁铃铅缺氧氨特牺造乘敌秤租积秧秩称秘透笔笑笋债借值倚俺倾倒倘俱倡候赁俯倍倦健臭射躬息倔徒徐殷舰舱般航途拿耸爹舀爱豺豹颁颂翁胰脆脂胸胳脏脐胶脑脓逛狸狼卿逢鸵留鸳皱饿馁凌凄恋桨浆衰衷高郭席准座症病疾斋疹疼疲脊效离紊唐瓷资凉站剖竞部旁旅畜阅羞羔瓶拳粉料益兼烤烘烦烧烛烟烙递涛浙涝浦酒涉消涡浩海涂浴浮涣涤流润涧涕浪浸涨烫涩涌悖悟悄悍悔悯悦害宽家宵宴宾窍窄容宰案请朗诸诺读扇诽袜袖袍被祥课冥谁调冤谅谆谈谊剥恳展剧屑弱陵祟陶陷陪娱娟恕娥娘通能难预桑绢绣验继骏球琐理琉琅捧堵措描域捺掩捷排焉掉捶赦堆推埠掀授捻教掏掐掠掂培接掷控探据掘掺职基聆勘聊娶著菱勒黄菲萌萝菌萎菜萄菊菩萍菠萤营乾萧萨菇械彬梦婪梗梧梢梅检梳梯桶梭救曹副票酝酗厢戚硅硕奢盔爽聋袭盛匾雪辅辆颅虚彪雀堂常眶匙晨睁眯眼悬野啪啦曼晦晚啄啡距趾啃跃略蚯蛀蛇唬累鄂唱患啰唾唯啤啥啸崖崎崭逻崔帷崩崇崛婴圈铐铛铝铜铭铲银矫甜秸梨犁秽移笨笼笛笙符第敏做袋悠偿偶偎偷您售停偏躯兜假衅徘徙得衔盘舶船舵斜盒鸽敛悉欲彩领脚脖脯豚脸脱象够逸猜猪猎猫凰猖猛祭馅馆凑减毫烹庶麻庵痊痒痕廊康庸鹿盗章竟商族旋望率阎阐着羚盖眷粘粗粒断剪兽焊焕清添鸿淋涯淹渠渐淑淌混淮淆渊淫渔淘淳液淤淡淀深涮涵婆梁渗情惜惭悼惧惕惟惊惦悴惋惨惯寇寅寄寂宿窒窑密谋谍谎谐袱祷祸谓谚谜逮敢尉屠弹隋堕随蛋隅隆隐婚婶婉颇颈绩绪续骑绰绳维绵绷绸综绽绿缀巢琴琳琢琼斑替揍款堪塔搭堰揩越趁趋超揽堤提博揭喜彭揣插揪搜煮援搀裁搁搓搂搅壹握搔揉斯期欺联葫散惹葬募葛董葡敬葱蒋蒂落韩朝辜葵棒棱棋椰植森焚椅椒棵棍椎棉棚棕棺榔椭惠惑逼粟棘酣酥厨厦硬硝确硫雁殖裂雄颊雳暂雅翘辈悲紫凿辉敞棠赏掌晴睐暑最晰量鼎喷喳晶喇遇喊遏晾景畴践跋跌跑跛遗蛙蛛蜓蜒蛤喝鹃喂喘喉喻啼喧嵌幅帽赋赌赎赐赔黑铸铺链销锁锄锅锈锋锌锐甥掰短智氮毯氯鹅剩稍程稀税筐等筑策筛筒筏答筋筝傲傅牌堡集焦傍储皓皖粤奥街惩御循艇舒逾番释禽腊脾腋腔腕鲁猩猬猾猴惫然馈馋装蛮就敦斌痘痢痪痛童竣阔善翔羡普粪尊奠道遂曾焰港滞湖湘渣渤渺湿温渴溃溅滑湃渝湾渡游滋渲溉愤慌惰愕愣惶愧愉慨割寒富寓窜窝窖窗窘遍雇裕裤裙禅禄谢谣谤谦犀属屡强粥疏隔隙隘媒絮嫂媚婿登缅缆缉缎缓缔缕骗编骚缘瑟鹉瑞瑰瑙魂肆摄摸填搏塌鼓摆携搬摇搞塘摊聘斟蒜勤靴靶鹊蓝墓幕蓬蓄蒲蓉蒙蒸献椿禁楚楷榄想槐榆楼概赖酪酬感碍碘碑碎碰碗碌尴雷零雾雹辐辑输督频龄鉴睛睹睦瞄睫睡睬嗜鄙嗦愚暖盟歇暗暇照畸跨跷跳跺跪路跤跟遣蜈蜗蛾蜂蜕嗅嗡嗓署置罪罩蜀幌错锚锡锣锤锥锦键锯锰矮辞稚稠颓愁筹签简筷毁舅鼠催傻像躲魁衙微愈遥腻腰腥腮腹腺鹏腾腿鲍猿颖触解煞雏馍馏酱禀痹廓痴痰廉靖新韵意誊粮数煎塑慈煤煌满漠滇源滤滥滔溪溜漓滚溢溯滨溶溺粱滩慎誉塞寞窥窟寝谨褂裸福谬群殿辟障媳嫉嫌嫁叠缚缝缠缤剿静碧璃赘熬墙墟嘉摧赫截誓境摘摔撇聚慕暮摹蔓蔑蔡蔗蔽蔼熙蔚兢模槛榴榜榨榕歌遭酵酷酿酸碟碱碳磁愿需辖辗雌裳颗瞅墅嗽踊蜻蜡蝇蜘蝉嘛嘀赚锹锻镀舞舔稳熏箕算箩管箫舆僚僧鼻魄魅貌膜膊膀鲜疑孵馒裹敲豪膏遮腐瘩瘟瘦辣彰竭端旗精粹歉弊熄熔煽潇漆漱漂漫滴漾演漏慢慷寨赛寡察蜜寥谭肇褐褪谱隧嫩翠熊凳骡缩慧撵撕撒撩趣趟撑撮撬播擒墩撞撤增撰聪鞋鞍蕉蕊蔬蕴横槽樱橡樟橄敷豌飘醋醇醉磕磊磅碾震霄霉瞒题暴瞎嘻嘶嘲嘹影踢踏踩踪蝶蝴蝠蝎蝌蝗蝙嘿嘱幢墨镇镐镑靠稽稻黎稿稼箱篓箭篇僵躺僻德艘膝膛鲤鲫熟摩褒瘪瘤瘫凛颜毅糊遵憋潜澎潮潭鲨澳潘澈澜澄懂憔懊憎额翩褥谴鹤憨慰劈履豫缭撼擂操擅燕蕾薯薛薇擎薪薄颠翰噩橱橙橘整融瓢醒霍霎辙冀餐嘴踱蹄蹂蟆螃器噪鹦赠默黔镜赞穆篮篡篷篱儒邀衡膨雕鲸磨瘾瘸凝辨辩糙糖糕燃濒澡激懒憾懈窿壁避缰缴戴擦藉鞠藏藐檬檐檀礁磷霜霞瞭瞧瞬瞳瞩瞪曙蹋蹈螺蟋蟀嚎赡穗魏簧簇繁徽爵朦臊鳄癌辫赢糟糠燥懦豁臀臂翼骤藕鞭藤覆瞻蹦嚣镰翻鳍鹰瀑襟璧戳孽警蘑藻攀曝蹲蹭蹬巅簸簿蟹颤靡癣瓣羹鳖爆疆鬓壤馨耀躁蠕嚼嚷巍籍鳞魔糯灌譬蠢霸露霹躏黯髓赣囊镶瓤罐矗'
cn_words_second = '乂乜兀弋孑孓幺亓韦廿丏卅仄厄仃仉仂兮刈爻卞闩讣尹夬爿毋邗邛艽艿札叵匝丕匜劢卟叱叻仨仕仟仡仫仞卮氐犰刍邝邙汀讦讧讪讫尻阡尕弁驭匡耒玎玑邢圩圬圭扦圪圳圹扪圮圯芊芍芄芨芑芎芗亘厍夼戍尥乩旯曳岌屺凼囡钇缶氘氖牝伎伛伢佤仵伥伧伉伫囟汆刖夙旮刎犷犸舛凫邬饧汕汔汐汲汜汊忖忏讴讵祁讷聿艮厾阱阮阪丞妁牟纡纣纥纨玕玙抟抔圻坂坍坞抃抉㧐芫邯芸芾苈苣芷芮苋芼苌苁芩芪芡芟苄苎苡杌杓杞杈忑孛邴邳矶奁豕忒欤轫迓邶忐卣邺旰呋呒呓呔呖呃旸吡町虬呗吽吣吲帏岐岈岘岑岚兕囵囫钊钋钌迕氙氚牤佞邱攸佚佝佟佗伽彷佘佥孚豸坌肟邸奂劬狄狁鸠邹饨饩饪饫饬亨庑庋疔疖肓闱闳闵羌炀沣沅沔沤沌沏沚汩汨沂汾沨汴汶沆沩泐怃怄忡忤忾怅忻忪怆忭忸诂诃诅诋诌诏诒孜陇陀陂陉妍妩妪妣妊妗妫妞姒妤邵劭刭甬邰纭纰纴纶纾玮玡玭玠玢玥玦盂忝匦坩抨拤坫拈垆抻劼拃拊坼坻㧟坨坭抿坳耶苷苯苤茏苫苜苴苒苘茌苻苓茚茆茑茓茔茕茀苕枥枇杪杳枧杵枨枞枋杻杷杼矸砀刳奄瓯殁郏轭郅鸢盱昊昙杲昃咂呸昕昀旻昉炅咔畀虮咀呷黾呱呤咚咆咛呶呣呦咝岢岿岬岫帙岣峁刿迥岷剀帔峄沓囹罔钍钎钏钒钕钗邾迮牦竺迤佶佬佰侑侉臾岱侗侃侏侩佻佾侪佼佯侬帛阜侔徂刽郄怂籴瓮戗肼䏝肽肱肫剁迩郇狙狎狍狒咎炙枭饯饴冽冼庖疠疝疡兖妾劾炜炖炘炝炔泔沭泷泸泱泅泗泠泺泖泫泮沱泯泓泾怙怵怦怛怏怍㤘怩怫怿宕穹宓诓诔诖诘戾诙戽郓衩祆祎祉祇诛诜诟诠诣诤诧诨诩戕孢亟陔妲妯姗帑弩孥驽虱迦迨绀绁绂驷驸绉绌驿骀甾珏珐珂珑玳珀顸珉珈拮垭挝垣挞垤赳贲垱垌郝垧垓挦垠茜荚荑贳荜莒茼茴茱莛荞茯荏荇荃荟荀茗荠茭茨垩荥荦荨荩剋荪茹荬荮柰栉柯柘栊柩枰栌柙枵柚枳柞柝栀柢栎枸柈柁枷柽剌酊郦甭砗砘砒斫砭砜奎耷虺殂殇殄殆轱轲轳轶轸虿毖觇尜哐眄眍𠳐郢眇眊眈禺哂咴曷昴昱昵咦哓哔畎毗呲胄畋畈虼虻盅咣哕剐郧咻囿咿哌哙哚咯咩咤哝哏哞峙峣罘帧峒峤峋峥贶钚钛钡钣钤钨钫钯氡氟牯郜秕秭竽笈笃俦俨俅俪叟垡牮俣俚皈俑俟逅徇徉舢俞郗俎郤爰郛瓴胨胪胛胂胙胍胗胝朐胫鸨匍狨狯飑狩狲訇逄昝饷饸饹胤孪娈弈奕庥疬疣疥疭庠竑彦飒闼闾闿阂羑迸籼酋炳炻炽炯烀炷烃洱洹洧洌浃洇洄洙涎洎洫浍洮洵浒浔浕洳恸恓恹恫恺恻恂恪恽宥扃衲衽衿袂祛祜祓祚诮祗祢诰诳鸩昶郡咫弭牁胥陛陟娅姮娆姝姣姘姹怼羿炱矜绔骁骅绗绛骈耖挈珥珙顼珰珩珧珣珞琤珲敖恚埔埕埘埙埚挹耆耄埒捋贽垸捃盍荸莆莳莴莪莠莓莜莅荼莩荽莸荻莘莎莞莨鸪莼栲栳郴桓桡桎桢桤梃栝桕桁桧桅栟桉栩逑逋彧鬲豇酐逦厝孬砝砹砺砧砷砟砼砥砣剞砻轼轾辂鸫趸龀鸬虔逍眬唛晟眩眙哧哽唔晁晏鸮趵趿畛蚨蚜蚍蚋蚬蚝蚧唢圄唣唏盎唑崂崃罡罟峪觊赅钰钲钴钵钹钺钽钼钿铀铂铄铆铈铉铊铋铌铍䥽铎氩氤氦毪舐秣秫盉笄笕笊笏笆俸倩俵偌俳俶倬倏恁倭倪俾倜隼隽倌倥臬皋郫倨衄颀徕舫釜奚衾胯胱胴胭脍胼朕脒胺鸱玺鸲狷猁狳猃狺逖桀袅饽凇栾挛亳疳疴疸疽痈疱痂痉衮凋颃恣旆旄旃阃阄訚阆恙粑朔郸烜烨烩烊剡郯烬涑浯涞涟娑涅涠浞涓浥涔浜浠浣浚悚悭悝悒悌悛宸窈剜诹冢诼袒袢祯诿谀谂谄谇屐屙陬勐奘牂蚩陲姬娠娌娉娲娩娴娣娓婀畚逡绠骊绡骋绥绦绨骎邕鸶彗耜焘舂琏琇麸揶埴埯捯掳掴埸埵赧埤捭逵埝堋堍掬鸷掖捽掊堉掸捩掮悫埭埽掇掼聃菁萁菘堇萘萋菽菖萜萸萑棻菔菟萏萃菏菹菪菅菀萦菰菡梵梿梏觋桴桷梓棁桫棂啬郾匮敕豉鄄酞酚戛硎硭硒硖硗硐硇硌鸸瓠匏厩龚殒殓殍赉雩辄堑眭眦啧晡晤眺眵眸圊喏喵啉勖晞唵晗冕啭畦趺啮跄蚶蛄蛎蛆蚰蛊圉蚱蛉蛏蚴啁啕唿啐唼唷啖啵啶啷唳唰啜帻崚崦帼崮崤崆赇赈赊铑铒铗铙铟铠铡铢铣铤铧铨铩铪铫铬铮铯铰铱铳铵铷氪牾鸹秾逶笺筇笸笪笮笠笥笤笳笾笞偾偃偕偈傀偬偻皑皎鸻徜舸舻舴舷龛翎脬脘脲匐猗猡猞猝斛猕馗馃馄鸾孰庹庾痔痍疵翊旌旎袤阇阈阉阊阋阍阏羟粝粕敝焐烯焓烽焖烷焗渍渚淇淅淞渎涿淖挲淠涸渑淦淝淬涪淙涫渌淄惬悻悱惝惘悸惆惚惇惮窕谌谏扈皲谑裆袷裉谒谔谕谖谗谙谛谝逯郿隈粜隍隗婧婊婕娼婢婵胬袈翌恿欸绫骐绮绯绱骒绲骓绶绺绻绾骖缁耠琫琵琶琪瑛琦琥琨靓琰琮琯琬琛琚辇鼋揳堞搽揸揠堙趄揖颉塄揿耋揄蛩蛰塆摒揆掾聒葑葚靰靸葳葺葸萼葆葩葶蒌萱戟葭楮棼椟棹椤棰赍椋椁椪棣椐鹁覃酤酢酡鹂厥殚殛雯雱辊辋椠辍辎斐睄睑睇睃戢喋嗒喃喱喹晷喈跖跗跞跚跎跏跆蛱蛲蛭蛳蛐蛔蛞蛴蛟蛘喁喟啾嗖喑嗟喽嗞喀喔喙嵘嵖崴遄詈嵎崽嵬嵛嵯嵝嵫幄嵋赕铻铼铿锃锂锆锇锉锏锑锒锔锕掣矬氰毳毽犊犄犋鹄犍嵇黍稃稂筚筵筌傣傈舄牍傥傧遑傩遁徨媭畲弑颌翕釉鹆舜貂腈腌腓腆腴腑腚腱鱿鲀鲂颍猢猹猥飓觞觚猱颎飧馇馊亵脔裒痣痨痦痞痤痫痧赓竦瓿啻颏鹇阑阒阕粞遒孳焯焜焙焱鹈湛渫湮湎湜渭湍湫溲湟溆湲湔湉渥湄滁愠惺愦惴愀愎愔喾寐谟扉裢裎裥祾祺谠幂谡谥谧遐孱弼巽骘媪媛婷巯翚皴婺骛缂缃缄彘缇缈缌缑缒缗飨耢瑚瑁瑜瑗瑄瑕遨骜韫髡塬鄢趔趑摅摁蜇搋搪搐搛搠摈彀毂搦搡蓁戡蓍鄞靳蓐蓦鹋蒽蓓蓖蓊蒯蓟蓑蒿蒺蓠蒟蒡蒹蒴蒗蓥颐楔楠楂楝楫楸椴槌楯皙榈槎榉楦楣楹椽裘剽甄酮酰酯酩蜃碛碓硼碉碚碇碜鹌辏龃龅訾粲虞睚嗪韪嗷嗉睨睢雎睥嘟嗑嗫嗬嗔嗝戥嗄煦暄遢暌跬跶跸跐跣跹跻蛸蜊蜍蜉蜣畹蛹嗣嗯嗥嗲嗳嗌嗍嗨嗐嗤嗵罨嵊嵩嵴骰锗锛锜锝锞锟锢锨锩锭锱雉氲犏歃稞稗稔筠筢筮筲筱牒煲敫徭愆艄觎毹貊貅貉颔腠腩腼腭腧塍媵詹鲅鲆鲇鲈稣鲋鲐肄鹐飕觥遛馐鹑亶瘃痱痼痿瘐瘁瘆麂裔歆旒雍阖阗阙羧豢粳猷煳煜煨煅煊煸煺滟溱溘漭滢溥溧溽裟溻溷滗滫溴滏滃滦溏滂滓溟滪愫慑慊鲎骞窦窠窣裱褚裨裾裰禊谩谪媾嫫媲嫒嫔媸缙缜缛辔骝缟缡缢缣骟耥璈瑶瑭獒觏慝嫠韬叆髦摽墁撂摞撄翥踅摭墉墒榖綦蔫蔷靺靼鞅靿甍蔸蔟蔺戬蕖蔻蓿斡鹕蓼榛榧榻榫榭槔榱槁槟槠榷僰酽酶酹厮碡碴碣碲磋臧豨殡霆霁辕蜚裴翡龇龈睿䁖睽嘞嘈嘌嘁嘎暧暝踌踉蜞蜥蜮蝈蜴蜱蜩蜷蜿螂蜢嘘嘡鹗嘣嘤嘚嗾嘧罴罱幔嶂幛赙罂骷骶鹘锲锴锶锷锸锵镁镂犒箐箦箧箍箸箬箅箪箔箜箢箓毓僖儆僳僭劁僮魃魆睾艋鄱膈膑鲑鲔鲚鲛鲟獐觫雒夤馑銮塾麽瘌瘊瘘瘙廖韶旖膂阚鄯鲞粿粼粽糁槊鹚熘熥潢漕滹漯漶潋潴漪漉漳漩澉潍慵搴窨寤綮谮褡褙褓褛褊谯谰谲暨屣鹛嫣嫱嫖嫦嫚嫘嫡鼐翟瞀鹜骠缥缦缧缨骢缪缫耦耧瑾璜璀璎璁璋璇奭髯髫撷撅赭撸鋆撙撺墀聩觐鞑蕙鞒蕈蕨蕤蕞蕺瞢蕃蕲赜槿樯槭樗樘樊槲醌醅靥魇餍磔磙霈辘龉龊觑瞌瞋瞑嘭噎噶颙暹噘踔踝踟踒踬踮踯踺踞蝽蝾蝻蝰蝮螋蝓蝣蝼噗嘬颚噍噢噙噜噌噔颛幞幡嶙嶝骺骼骸镊镉镌镍镏镒镓镔稷箴篑篁篌篆牖儋徵磐虢鹞膘滕鲠鲡鲢鲣鲥鲧鲩獗獠觯馓馔麾廛瘛瘼瘢瘠齑羯羰𥻗遴糌糍糅熜熵熠澍澌潸潦潲鋈潟潼潺憬憧寮窳谳褴褟褫谵熨屦嬉勰戮蝥缬缮缯骣畿耩耨耪璞璟靛璠璘聱螯髻髭髹擀熹甏擞縠磬颞蕻鞘颟薤薨檠薏薮薜薅樾橛橇樵檎橹樽樨橼墼橐翮醛醐醍醚磲赝飙殪霖霏霓錾辚臻遽氅瞟瞠瞰嚄嚆噤暾蹀踹踵踽蹉蹁螨蟒螈螅螭螠螟噱噬噫噻噼罹圜䦃镖镗镘镚镛镝镞镠氇氆憩穑篝篥篦篪篙盥劓翱魉魈徼歙膳膦膙鲮鲱鲲鲳鲴鲵鲷鲻獴獭獬邂鹧廨赟瘰廪瘿瘵瘴癃瘳斓麇麈嬴壅羲糗瞥甑燎燠燔燧濑濉潞澧澹澥澶濂褰寰窸褶禧嬖犟隰嬗颡缱缲缳璨璩璐璪螫擤壕觳罄擢薹鞡鞬薷薰藓藁檄檩懋醢翳礅磴鹩龋龌豳壑黻嚏嚅蹑蹒蹊蟥螬螵疃螳蟑嚓羁罽罾嶷黜黝髁髀镡镢镣镦镧镩镪镫罅黏簌篾篼簖簋鼢黛儡鹪鼾皤魍龠繇貘邈貔臌膻臆臃鲼鲽鳀鳃鳅鳇鳊螽燮鹫襄糜縻膺癍麋懑濡濮濞濠濯蹇謇邃襁檗擘孺隳嬷蟊鹬鍪鏊鳌鬈鬃瞽鞯鞨鞫鞧鞣藜藠藩醪蹙礓燹餮瞿曛颢曜躇蹚鹭蟛蟪蟠蟮鹮黠黟髅髂镬镭镯馥簟簪鼬雠艟鳎鳏鳐癞癔癜癖糨蹩鎏懵彝邋鬏攉攒鞲鞴藿蘧蘅麓醮醯酃霪霭霨黼嚯蹰蹶蹽蹼蹴蹾蹿蠖蠓蟾蠊黢髋髌镲籀籁齁魑艨鳓鳔鳕鳗鳙麒鏖羸㸆瀚瀣瀛襦谶襞骥缵瓒攘蘩蘖醴霰酆矍曦躅鼍巉黩黥黪镳镴黧纂璺鼯臜鳜鳝鳟獾孀骧瓘鼙醺礴颦曩鳢癫麝夔爝灏禳鐾羼蠡耱懿蘸鹳霾氍饕躐髑镵穰饔鬻鬟趱攫攥颧躜鼹癯麟蠲蠹躞衢鑫灞襻纛鬣攮囔馕戆爨齉'
cn_words_third = '亍尢彳卬殳𠙶毌邘戋圢氕伋仝冮氿汈氾忉宄讱扞圲圫芏芃朳朸𨙸邨吒吖屼屾辿钆仳伣伈癿甪邠犴冱邡闫汋䜣讻孖纩玒玓玘玚刬坜坉扽坋扺㧑毐芰芣苊苉芘芴芠芤杕杙杄杧杩尪尨轪坒芈旴旵呙㕮岍岠岜呇冏觃岙伾㑇伭佖伲佁飏狃闶汧汫𣲘𣲗沄沘汭㳇沇忮忳忺祃诇邲诎诐屃岊阽䢺阼妧妘𨚕纮驲纻纼玤玞玱玟邽邿坥坰坬坽弆耵䢼𦭜茋苧苾苠枅㭎枘枍矼矻匼旿昇昄昒昈咉咇咍岵岽岨岞峂㟃囷钐钔钖牥佴垈侁侹佸佺隹㑊侂佽侘郈舠郐郃攽肭肸肷狉狝饳忞於炌炆泙沺泂泜泃泇怊峃穸祋祊鸤弢弨陑陎卺乸妭姈迳叕驵䌹驺绋绐砉耔㛃玶珇珅珋玹珌玿韨垚垯垙垲埏垍耇垎垴垟垞挓垵垏拶荖荁荙荛茈茽荄茺荓茳𦰡茛荭㭕柷柃柊枹栐柖郚剅䴓迺厖砆砑砄耏奓䶮轵轷轹轺昺昽盷咡咺昳昣哒昤昫昡咥昪虷虸哃峘耑峛峗峧帡钘钜钪钬钭矧秬俫舁俜俙俍垕衎舣弇侴鸧䏡胠𦙶胈胩胣朏飐訄饻庤疢炣炟㶲洭洘洓洿㳚泚浈浉洸洑洢洈洚洺洨浐㳘洴洣恔宬窀扂袆祏祐祕叚陧陞娀姞姱姤姶姽枲绖骃彖骉恝珪珛珹琊玼珖珽珦珫珒珢珕珝埗垾垺埆垿埌埇莰茝鄀莶莝䓖莙栻桠桄梠栴梴栒酎酏砵砠砫砬硁恧翃郪𨐈辀辁剕赀哢晅晊唝哳哱冔晔晐晖畖蚄蚆帱崁峿崄帨崀赆钷眚甡笫倻倴脩倮倕倞倓倧衃虒舭舯舥瓞鬯鸰脎朓胲虓鱽狴峱狻眢勍痄疰痃竘羖羓桊敉烠烔烶烻涍浡浭浬涄涢涐浰浟浛浼浲涘悈悃悢宧窅窊窎扅扆袪袗袯祧隺堲疍𨺙陴烝砮㛚哿翀翂剟绤骍䂮琎珸珵琄琈琀珺掭堎堐埼掎埫堌晢掞埪壸㙍聍菝萚菥莿䓫勚䓬萆菂菍菼萣䓨菉䓛梼梽桲梾桯梣梌桹敔厣硔硙硚硊硍勔䴕龁逴唪啫翈㫰晙畤趼跂蛃蚲蚺啴䎃崧崟崞崒崌崡铏铕铖铘铚铞铥铴牻牿稆笱笯偰偡鸺偭偲偁㿠鄅偓徛衒舳舲鸼悆鄃瓻䝙脶脞脟䏲鱾猇猊猄觖𠅤庱庼庳痓䴔竫堃阌羝羕焆烺焌淏淟淜淴淯湴涴㥄惛惔悰惙寁逭袼裈祲谞艴弸弶隃婞娵婼媖婳婍婌婫婤婘婠绹骕絜珷琲琡琟琔琭堾堼揕㙘堧喆堨塅堠絷𡎚葜惎萳葙靬葴蒇蒈鄚蒉蓇萩蒐葰葎鄑蒎葖蒄萹棤棽棫椓椑鹀椆棓棬棪椀楗甦酦觌奡皕硪欹詟辌棐龂黹牚睎晫晪晱𧿹蛑畯斝喤崶嵁崾嵅崿嵚翙圌圐赑淼赒铹铽𨱇锊锍锎锓犇颋稌筀筘筜筥筅傃傉翛傒傕舾畬脿腘䐃腙腒鲃猰猯㺄馉鄗廋廆鄌粢遆旐焞欻𣸣溚溁湝渰湓㴔渟溠渼溇湣湑溞愐愃敩甯棨扊裣祼婻媆媞㛹媓媂媄毵矞缊缐骙瑃瑓瑅瑆䴖瑖瑝瑔瑀𤧛瑳瑂嶅瑑遘髢塥堽赪摛塝搒搌蒱蒨蓏蔀蓢蓂蒻蓣椹楪榃榅楒楞楩榇椸楙歅碃碏碈䃅硿鄠辒龆觜䣘暕鹍㬊暅跱蜐蜎嵲赗骱锖锘锳锧锪锫锬稑稙䅟筻筼筶筦筤傺鹎僇艅艉谼貆腽腨腯鲉鲊鲌䲟鲏雊猺飔觟𦝼馌裛廒瘀瘅鄘鹒鄜麀鄣阘煁煃煴煋煟煓滠溍溹滆滉溦溵漷滧滘滍愭慥慆塱裼禋禔禘禒谫鹔愍嫄媱戤勠戣缞耤瑧瑨瑱瑷瑢斠摏墕墈墐墘摴銎𡐓墚撖靽鞁蔌蔈蓰蔹蔊嘏榰榑槚𣗋槜榍疐酺酾酲酴碶䃎碨𥔲碹碥劂䴗夥瞍鹖㬎跽蜾幖嶍圙𨱏锺锼锽锾锿镃镄镅馝鹙箨箖劄僬僦僔僎槃㙦鲒鲕鲖鲗鲘鲙𩽾夐獍飗凘廑廙瘗瘥瘕鲝鄫熇漹漖潆漤潩漼漴㽏漈漋漻慬窬窭㮾褕禛禚隩嫕嫭嫜嫪㻬麹璆漦叇墣墦墡劐薁蕰蔃鼒槱鹝磏磉殣慭霅暵暲暶踦踣䗖蝘蝲蝤噇噂噀罶嶲嶓㠇嶟嶒镆镈镋镎镕稹儇皞皛䴘艎艏鹟𩾃鲦鲪鲬橥觭鹠鹡糇糈翦鹢鹣熛潖潵㵐澂澛瑬潽潾潏憭憕戭褯禤嫽遹璥璲璒憙擐鄹薳鞔黇蕗薢蕹橞橑橦醑觱磡𥕢磜豮鹾虤暿曌曈㬚蹅踶䗛螗疁㠓幪嶦𨱑馞穄篚篯簉鼽衠盦螣縢鲭鲯鲰鲺鲹亸癀瘭羱糒燋熻燊燚燏濩濋澪澽澴澭澼憷憺懔黉嬛鹨翯璱𤩽璬璮髽擿薿薸檑櫆檞醨繄磹磻瞫瞵蹐蟏㘎镤镥镨𨱔矰穙穜穟簕簃簏儦魋斶艚谿䲠鲾鲿鳁鳂鳈鳉獯䗪馘襕襚螱甓嬬嬥𦈡瓀釐鬶爇鞳鞮藟藦藨鹲檫黡礞礌𥖨蹢蹜蟫䗴嚚髃镮镱酂馧簠簝簰鼫鼩皦臑䲢鳑鳒鹱鹯癗𦒍旞翷冁䎖瀔瀍瀌襜䴙嚭㰀鬷醭蹯蠋翾鳘儳儴鼗𩾌鳚鳛麑麖蠃彟嬿鬒蘘欂醵颥甗𨟠巇酅髎犨𨭉㸌爔瀱瀹瀼瀵襫孅骦耰𤫉瓖鬘趯罍鼱鳠鳡鳣爟爚灈韂糵蘼礵鹴躔皭龢鳤亹籥鼷玃醾齇觿蠼'