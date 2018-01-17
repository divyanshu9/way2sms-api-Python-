import way2

way2.login(YourMobileNo,'Loginpassword')    #ex way2.login(1111111111,'password')
if (way2.token !=None):
    way2.sendsms(RecieverMobileNo.,'message from python')   #way2.sendsms(22222222222,'HI')
