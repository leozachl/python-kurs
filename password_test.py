import mk_passwd

min_words = 5

while True:
    satz = input("Bitte einen Satz eingeben")
    passwd = mk_passwd.mk_passwd(satz, min_words=min_words)
    if passwd == False:
        print ("mindestens %d Wörter" % min_words)
    else:
        print (passwd)
        break