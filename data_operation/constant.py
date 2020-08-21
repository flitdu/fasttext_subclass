# -*- coding: utf-8 -*-
"""
Created by Dufy on 2020/2/27  14:40
IDE used: PyCharm 
Description :
1)
2)  
Remark:      
"""

label_name_forbid = ['nan', '(含税RMB)', '晶振贴片', '晶振直插', '圆柱体电感',
                     '磁环电感', '共模电感/滤波器', '通用电感',
                     '耦合电感', '多层陶瓷电容', '特种陶瓷电容器',
                     '电解电容', '硅电容器', '馈通电容器',
                     '氧化膜电阻', 'LED灯条电阻', '平面电阻器',
                     '专用电阻', '分流器', '3', '6', '160', '1.', '2.', '3.',
                     '电话：0755-83551135', '其他说明Other', '产品型号Model',
                     '镀金;-40°C', '1206', '序号NO.', 'DATE:', 'Management',
                     '购买类型', 'PIN',
                     'RF', 'RT7291','EMIRFI', 'IRLR8259TRPBF','保险丝','存储器连接器',
                     '继电器', '铝电解电容']

# 规则类目词典
rule_dict = {
             # '耦合 电感':'共模扼流圈滤波器',
             # '耦合电感':'共模扼流圈滤波器',
             # '共模电感':'共模扼流圈滤波器',
             # 'fast recovery rectifier': '超快快恢复二极管',
             # 'aluminum electrolytic capacitor smd':'贴片电解电容',
             # '安规':'安规电容',
             # '安规 电容': '安规电容',
             # '固态 电解电容': '固态电解电容',
             # '贴片 电容 排': '电容器阵列与网络',
             # 'power inductor':'功率电感',
             # 'high frequency inductor':'高频电感',
             # '贴片 电阻 排':'排阻',
             # 'varistor':'压敏电阻',
             # 'smd0204':'MELF晶圆电阻',
             # 'cfs 碳膜 晶圆 电阻':'MELF晶圆电阻',
             # 'led 间隔 柱': 'LED灯柱导光管配件',
             # 'mf52e':'NTC热敏电阻',
             # 'frte':'磁珠',
             # '压敏':'压敏电阻',
             # '光耦':'光耦',
             # '谐振器':'谐振器',
             # '网络 变压器': '网口变压器',
             }

# 正则匹配
re_match = {r'\bbase\b (\bt\b|\bt\b)':'网口变压器', # BASE-T：网口变压器  严格匹配

            r'\baluminum electrolytic capacitor\b.*(\bsmd\b|\bsmd\b)':'贴片电解电容',  # 中间可以插入别的内容
            r'\b轻触\b.*(开关)':'轻触开关',

            r'(耦合电感|耦合 电感|共模电感)': '共模扼流圈滤波器',
            r'(\bfast recovery rectifier\b)': '超快快恢复二极管',
            r'(\bfrte\b|磁珠)': '磁珠',  # 英文严格匹配
            r'(安规|安规 电容)': '安规电容',
            r'(固态 电解电容)': '固态电解电容',
            r'(贴片 电容 排)': '电容器阵列与网络',
            r'(\bpower inductor\b)': '功率电感',
            r'(\bhigh frequency inductor\b)': '高频电感',
            r'(贴片 电阻 排)': '排阻',
            r'(\bvaristor\b|压敏)': '压敏电阻',
            r'(\bsmd0204\b|cfs 碳膜 晶圆 电阻)': 'MELF晶圆电阻',
            r'(led 间隔 柱)': 'LED灯柱导光管配件',
            r'(\bmf52e\b)': 'NTC热敏电阻',
            r'(光耦)': '光耦',
            r'(谐振器)': '谐振器',
            r'(网络 变压器)': '网口变压器',
            r'(n mos|p mos)': 'MOSFET',

            }


label_subclass_database = ['32位微控制器-MCU',
                           '16位微控制器-MCU',
                           'ARM微控制器-MCU',
                           '微处理器-MPU',
                           '其他处理器',
                           '数字信号处理器和控制器',
                           '8位微控制器-MCU',
                           'CPLD-FPGA芯片',
                           '安全(加密)IC',
                           'MCU监控芯片',
                           '时钟计时芯片',
                           '实时时钟芯片',
                           '字库芯片',
                           '时钟缓冲器驱动器',
                           '时钟发生器频率合成器',
                           'FLASH存储器',
                           'SRAM存储器',
                           'EPROM存储器',
                           'SDRAM存储器',
                           'SDMicro-SDT-Flash卡',
                           'PROM存储器',
                           'EEPROM存储器',
                           'DDRSSD存储器',
                           'FPGA-配置存储器',
                           '时基芯片',
                           '信号开关多路复用解码器',
                           '锁存器',
                           '编解码芯片',
                           '4000系列逻辑芯片',
                           '74系列逻辑芯片',
                           '缓冲器驱动器接收器收发器',
                           '移位寄存器',
                           '专用逻辑芯片',
                           '触发器',
                           '多频振荡器',
                           '门极反相器',
                           '计数器除法器',
                           '电平转换移位器',
                           '隔离芯片',
                           '以太网芯片',
                           'USB芯片',
                           'RS485RS422芯片',
                           '直接数字合成器(DDS)',
                           'RS232芯片',
                           'LVDS芯片',
                           '传感器接口芯片',
                           'LIN收发器',
                           '信号缓冲器中继器分配器',
                           'IO扩展器',
                           '控制器',
                           '音频视频接口芯片',
                           '电信',
                           '接口专用芯片',
                           '串行接口芯片',
                           '触摸屏控制器',
                           'CAN芯片',
                           '磁珠',
                           '有源滤波器',
                           'RF滤波器',
                           '共模扼流圈滤波器',
                           '馈通式电容器',
                           'EMIRFI滤波器',
                           '铁氧体磁芯与配件',
                           '信号调节器',
                           '线对板线对线连接器',
                           '排针排母',
                           '板对板连接器',
                           '背板连接器',
                           'USB连接器',
                           '插拔式连接器',
                           '螺丝钉接线端子',
                           '弹簧式接线端子',
                           '轨道式接线端子',
                           '压接端子',
                           'IO连接器',
                           'D-Sub连接器附件',
                           '音频视频链接器',
                           'IEEE1394连接器',
                           '连接器附件套件',
                           '照明连接器',
                           'RF同轴连接器',
                           '栅栏式接线端子',
                           'FFCFPC连接器',
                           '圆形连接器',
                           'IDC连接器(牛角)',
                           '汽车连接器',
                           '电源连接器',
                           '军工连接器',
                           '以太网连接器',
                           'IC与器件插座',
                           '内存连接器',
                           '卡缘连接器',
                           '鳄鱼夹测试夹',
                           '贴片电感',
                           '高频电感',
                           '工字电感',
                           '功率电感',
                           '色环电感',
                           '固定电感',
                           '可变电感器套件配件',
                           '贴片电容',
                           '贴片电解电容',
                           '直插电解电容',
                           '直插瓷片电容',
                           '云母电容',
                           '安装型大容量电容',
                           '固态电解电容',
                           '钽电容',
                           '安规电容',
                           '薄膜电容',
                           '可调电容',
                           'CBB电容',
                           '超级电容器',
                           '氧化铌电容',
                           '电容器阵列与网络',
                           '电容套件及附件',
                           '直插独石电容',
                           '校正电容',
                           '铝电解电容',
                           'NTC热敏电阻',
                           '贴片电阻',
                           '贴片超低阻值电阻',
                           '采样电阻',
                           '光敏电阻',
                           '压敏电阻',
                           'MELF晶圆电阻',
                           '金属膜电阻',
                           'PTC热敏电阻',
                           '金属氧化膜电阻',
                           '碳膜电阻',
                           '薄膜电阻-透孔',
                           '厚膜电阻-透孔',
                           '铝壳大功率电阻',
                           '射频高频电阻',
                           '陶瓷复合电阻器',
                           '可调电阻电位器',
                           '精密可调电阻',
                           '绕线电阻',
                           '保险电阻',
                           '水泥电阻',
                           '金属箔电阻',
                           '高压电阻',
                           '排阻',
                           '直插通孔电阻',
                           '电阻套件及附件',
                           '贴片高精密-低温漂电阻',
                           '无源晶体振荡器',
                           '有源晶体振荡器',
                           '圆柱体晶振',
                           '谐振器',
                           '可编程振荡器',
                           '标准时钟振荡器',
                           '稳压二极管',
                           '通用二极管',
                           '功率二极管',
                           '开关二极管',
                           '超快快恢复二极管',
                           '肖特基二极管',
                           '双向触发二极管DIAC',
                           'TVS二极管(瞬态电压抑制二极管)',
                           'ESD二极管',
                           '变容二极管VaractorDiode',
                           '稳流二极管CRD',
                           'PIN二极管',
                           '整流器',
                           '整流桥',
                           '放电管',
                           '特殊功能放大器',
                           '视频放大器',
                           '放大器',
                           '高速宽带运放',
                           '仪表运放',
                           '精密运放',
                           'FET输入运放',
                           '低噪声运放',
                           '低功耗比较器运放',
                           '差分运放',
                           '电压比较器',
                           '采样保持放大器',
                           'LCDGamma缓冲器',
                           'LED驱动',
                           'LCD驱动',
                           '电机马达点火驱动器IC',
                           'MOS驱动',
                           '激光驱动器',
                           '达林顿晶体管阵列驱动',
                           '驱动芯片',
                           '门驱动器',
                           '全桥半桥驱动',
                           '电子辅料',
                           '风扇散热片热管理产品',
                           '焊接脱焊',
                           '罩类盒类及壳类产品',
                           '胶带标签',
                           '容器类',
                           '螺丝刀镊子扳手工具',
                           '化学物质',
                           'PCB等原型产品',
                           '配件',
                           '螺丝紧固件硬件',
                           '机架机柜',
                           '线性稳压芯片LDO',
                           '开关电源芯片',
                           'DC-DC芯片',
                           '电池电源管理芯片PMIC',
                           '电池保护芯片',
                           '电压基准芯片',
                           '电源监控芯片',
                           '功率开关芯片',
                           'DC-DC电源模块',
                           'AC-DC电源模块',
                           '无线充电IC',
                           'LEDUPS等其他类型电源模块',
                           '开发板套件',
                           'WiFi物联网模块',
                           '无线模块',
                           '传感器模块',
                           '电力线滤波器模块',
                           '其他模块',
                           '蜂鸣器',
                           '扬声器喇叭',
                           '咪头麦克风',
                           '音视频IC',
                           '电源变压器',
                           '电流变压器',
                           '网口变压器',
                           '工业控制变压器',
                           '脉冲变压器',
                           '音频及信号变压器',
                           '自耦变压器',
                           '信号继电器',
                           '继电器插座配件',
                           '车用继电器',
                           '固态继电器',
                           '安全继电器',
                           '簧片继电器',
                           '高频射频继电器',
                           '延时计时继电器',
                           '工业继电器',
                           '按键开关',
                           '船型开关',
                           '行程开关',
                           '拨码开关',
                           '拨动开关',
                           '五向开关',
                           '多功能开关',
                           '锅仔片',
                           '旋转编码开关',
                           '开关插座',
                           '带灯开关',
                           '旋转波段开关',
                           '交流接触器',
                           '压接接触器',
                           '专用开关',
                           '开关配件-盖帽',
                           '轻触开关',
                           '发光二极管',
                           '光耦',
                           '红外发射管',
                           '红外接收管',
                           'LED显示模组',
                           'LED数码管',
                           'LCD显示模组',
                           '光可控硅',
                           'OLED显示模组',
                           'LED灯柱导光管配件',
                           '真空荧-VFD光显示器',
                           '等离子体显示器',
                           '红外收发器',
                           '光纤收发器',
                           '光电开关',
                           '激光器件配件',
                           '温度传感器',
                           '超声波传感器',
                           '气体传感器',
                           '光学传感器',
                           '压力传感器',
                           '颜色传感器',
                           '图像传感器',
                           '环境光传感器',
                           '红外传感器',
                           '角速度传感器',
                           '加速度传感器',
                           '角度传感器',
                           '位置传感器',
                           '姿态传感器',
                           '磁性传感器',
                           '电流传感器',
                           '湿度传感器',
                           '专用传感器',
                           '模数转换芯片',
                           '数模转换芯片',
                           '模拟开关芯片',
                           '电流监控芯片',
                           '电量计芯片',
                           '数字电位器芯片',
                           '电池',
                           '电源充电器',
                           '电池座夹附件',
                           '线材配件附件',
                           '数据线信号线',
                           '电源线',
                           '多芯电缆',
                           '同轴电缆',
                           '电子线材连接线',
                           '贴片式一次性保险丝',
                           'PTC自恢复保险',
                           '通孔型保险丝',
                           '保险丝管',
                           '工业与电气保险丝',
                           '汽车保险丝',
                           '特种保险丝',
                           '温度保险丝',
                           '保险丝座夹',
                           '断路器',
                           'MOSFET',
                           '结型场效应晶体管(JFET)',
                           '可控硅SCR',
                           '达林顿管',
                           '数字三极管',
                           'IGBT管',
                           '双极晶体管(三极管)',
                           'LAN电信电缆测试',
                           '万用表与电压表',
                           '测试与测量',
                           '仪器设备与配件',
                           '无线收发芯片',
                           '射频卡芯片',
                           '天线',
                           '射频开关',
                           'RF放大器',
                           'RF混频器',
                           'RF检测器',
                           'RF衰减器',
                           'RF耦合器',
                           'RFFETMOSFET',
                           '机电电气',
                           '高频继电器',
                           '通信卫星定位模块',
                           'RF双工器',
                           'IGBT驱动',
                           'FRAM存储器',
                           '温控开关',
                           '温湿度传感器',
                           '电路保护套件']

# label_marked = ['__label__CBB电容', '__label__MELF晶圆电阻', '__label__NTC', '__label__PTC', '__label__云母电容', '__label__保险电阻', '__label__光敏电阻', '__label__功率电感', '__label__压敏电阻', '__label__可变电感器套件配件', '__label__可调电容', '__label__可调电阻电位器', '__label__固定电感', '__label__圆柱体晶振', '__label__安装型大容量电容', '__label__安规电容', '__label__射频高频电阻', '__label__工字电感', '__label__排阻', '__label__无源晶体振荡器', '__label__有源晶体振荡器', '__label__标准时钟振荡器', '__label__校正电容', '__label__氧化铌电容', '__label__水泥电阻', '__label__电位计', '__label__电容器阵列与网络', '__label__直插独石电容', '__label__直插瓷片电容', '__label__直插电解电容', '__label__直插通孔电阻', '__label__碳膜电阻', '__label__碳质电阻器', '__label__精密可调电阻', '__label__绕线电阻', '__label__色环电感', '__label__薄膜电容', '__label__谐振器', '__label__贴片电容', '__label__贴片电感', '__label__贴片电解电容', '__label__贴片电阻', '__label__贴片超低阻值电阻', '__label__贴片高精密-低温漂电阻', '__label__超级电容器', '__label__采样电阻', '__label__金属氧化膜电阻', '__label__金属膜电阻', '__label__钽电容', '__label__铝壳大功率电阻', '__label__高压电阻', '__label__高频电感']

jieba_dict = []


class SubclassLabelList():
    label_list = []

    @classmethod
    def setLabel(cls, label_new):
        cls.label_list = label_new

    @classmethod
    def getLabel(cls):
        return cls.label_list

if __name__ == "__main__":
    pass
