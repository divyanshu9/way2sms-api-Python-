import requests as req

token = None
way2session = req.Session()

def login(mob,password):
    global token
    try:
        if(len(str(mob))!=10):
            raise Exception("Invalid Mobile no. ")
        log = way2session.post('http://site21.way2sms.com/Login1.action?username=%s&password=%s'%(mob,password))
        if (log.status_code != 200):
            raise Exception('Error in login')
        else:
            if('Token' not in log.url):
                raise Exception(" Invalid Username or Password")
            token = way2session.cookies.get_dict()['JSESSIONID'][4:]
    except Exception as e:
        print (e)

def sendsms(mobile,message):
    global token
    try:
        if (len(str(mobile))!=10):
            raise Exception("Invalid Mobile no.")
        if (token != None):
            print (" SENDING SMS... ")
            send = way2session.post('http://site21.way2sms.com/smstoss.action?ssaction=ss&Token=%s&mobile=%s&message=%s'%(token,mobile,message))
            if (send.status_code !=200):
                raise Exception("Error occurred in sending sms")
            print (" SMS SENT")
        else:
            print (" Login Token error ")
        
    except Exception as e:
        print (e)

