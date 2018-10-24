import itchat
import requests

#机器人自动回复api
apiUrl = 'http://www.tuling123.com/openapi/api'
def reply(msg):
    data = {
        'key'    : 'a91dad1d4a234e2c9827811d99f00ae2',
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    r = requests.post(apiUrl, data=data).json()
    print(r['text'])
    return r['text']

    #定义开关
class look(object):
    def __init__(self):
        self.status='open'
    def open(self):
        self.status='open'
    def off(self):
        self.status='off'
lock=look()
print(lock.status)
print('重复*')

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):

    #声明全局变量。
    global reply
    global lock
    global status
    global look
    

    print('----------------------\n\n','收到:',msg['Text'])

    if str(msg['Text'])=='openpassword':
        lock.open()
        print(lock)
        print('','机器人锁状态','***',lock.status,'***')
    elif str(msg['Text'])=='offpassword':
        lk=lock.off()
        print(lock)
        print('','机器人锁状态','###',lock.status,'###')
    elif str(msg['Text'])=='lock':
        print(lock)
        print('','机器人锁状态','@@@',lock.status,'@@@')
    else :
        print('','消息没有检测到任何指令')
        pass

    #检查开关的状态
    if lock.status=='open':
        msg['status']='1'
    if lock.status=='off':
        msg['status']='0'

    #检查lock.status
    if msg['status']=='1':

        if msg['FromUserName']== UN:#通过识别个性签名，保证没有自己回复自己的bug。
            print('','发送给自己','\n\n----------------------')
            pass
        else:
            #print(msg.User.UserName)

            #自动回复机器人模块
            msgcon=msg['Text']
            re=reply(msgcon)
            itchat.send(str(re),msg.User.UserName)

            #另一种回复接口
            #msg.user.send('%s: %s' % (msg.User.UserName, msg['Text']))

            #回复其他内容的格式，必须在同一文件夹。
            # itchat.send('@img@%s' % 'image1.jpg', 'filehelper')
            # itchat.send('@fil@%s' % 'xlsx.xlsx','filehelper')
            # itchat.send('@vid@%s' % 'demo.mp4','filehelper')

            print('\n----------------------')

    else :
        print('拒收消息',msg.User['UserName'],':',msg['Text'])
        print('\n----------------------')

itchat.auto_login(hotReload=True)
UN=itchat.search_friends().UserName
itchat.run()
