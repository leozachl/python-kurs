import mk_passwd

min_words = 5

while True:
    satz = input("Bitte einen Satz eingeben")
    try:
        passwd = mk_passwd.mk_passwd(satz, min_words=min_words)
        print(passwd)
        break
    except:
        print ("mindestens %d Wörter" % min_words)
