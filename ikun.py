#导入模块
import random
import time

#初始化百分比
init = 0

#初始化
print('您已进入米哈游验证码窃取程序')
time.sleep(2)
print('目标IP：139.224.19.81')
time.sleep(1)
print('正在连接至米哈游服务器')
time.sleep(1)
while True :
    if init < 101 :
        init = str(init)
        print('连接中：'+init+'%')
        time.sleep(0.1)
        init = int(init)
        init = init + 1
    else:
        time.sleep(5)
        print('成功连接服务器，正在加载！')
        print('Loading, please wait...')
        time.sleep(5)
        break


#提示语列表
list = ['您正在登录米哈游通行证，请勿将验证码告诉他人哦。',
        '您正在查看自助登录限制状态，如您的限制时长已超过6小时，将可解除登录限制。请勿将验证码告诉他人哦。',
        '您正在注销米哈游通行证，请勿将验证码告诉他人哦。',
        '您正在修改米哈游通行证个人信息，请勿将验证码告诉他人哦。'
        ]

#循环
while True:
    #电话号码随机
    pa = str(random.randint(0, 9))
    pb = str(random.randint(0, 9))
    pc = str(random.randint(0, 9))
    pd = str(random.randint(0, 9))
    pe = str(random.randint(0, 9))
    pf = str(random.randint(0, 9))
    pg = str(random.randint(0, 9))
    ph = str(random.randint(0, 9))
    pi = str(random.randint(0, 9))
    pj = str(random.randint(0, 9))

    #验证码随机
    a = str(random.randint(1,9))
    b = str(random.randint(1,9))
    c = str(random.randint(1,9))
    d = str(random.randint(1,9))
    e = str(random.randint(1,9))
    f = str(random.randint(1,9))

    #随机提示语
    txt = random.choice(list)

    #输出电话号码
    print('该验证码发送至：'+'1'+pa+pb+pc+pd+pe+pf+pg+ph+pi+pj)

    #正文
    print('【米哈游】')
    print('验证码:'+a+b+c+d+e+f+'（十分钟内有效）。')
    print(txt)
    print('______________________________')

    #延迟
    time.sleep(1)
