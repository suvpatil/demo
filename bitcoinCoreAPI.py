from bitcoinrpc.authproxy import AuthServiceProxy


'''#create wallet 
#access = AuthServiceProxy("http://admin:adminpw@ec2-13-228-250-145.ap-southeast-1.compute.amazonaws.com:18332")
#cr = access.createwallet("DigitalVault")
#print(cr)'''


'''#Generate new address
access = AuthServiceProxy("http://admin:adminpw@ec2-13-228-250-145.ap-southeast-1.compute.amazonaws.com:18332/wallet/DigitalVault")
address = access.getnewaddress()
print(address)
dumpPri = access.dumpprivkey(address)
print(dumpPri)
impoPri = access.importprivkey(dumpPri)
print(impoPri)'''
 
#access = AuthServiceProxy("http://admin:adminpw@ec2-13-228-250-145.ap-southeast-1.compute.amazonaws.com:18332/wallet/HSBCVault")

'''#load wallet in case multiple wallet
#ld = access.loadwallet("/home/ubuntu/.bitcoin/testnet3/wallets/testWallet/")
#print(ld)'''


'''get the walletinfo
#info = access.getwalletinfo()
#print(info)'''

'''#List the unspent transaction outputs. This will required in to checked the confirmation and after getting min confirmation i.e. 6,
#will show on history page.
#unspent = access.listunspent(1,9999999,["2Mt3RPZrTVmYT2yYWcRfgixQQ7q7DuSf63A"])
#print (unspent)'''

'''#check balance
print ('%.08f' % access.getbalance())'''

'''#send bitcoin to other
#spends = access.sendtoaddress("2MvgpD1LbbFhS54p281g7cwDBtQaED5Up8y",0.00010101)
#print(spends)'''

'''#get the transaction information
#print(access.gettransaction("0b425e7ae326760725c16e2405ad59f8254e39d3632b00866181e21174ae13ef"))
'''

'''#we have enable notification like if block is created it gives notification of createtion
#its zero mq messaging
#print(access.getzmqnotifications()) '''


#print('%.08f' % access.getunconfirmedbalance())
#access.loadwallet('DigitalVault')

