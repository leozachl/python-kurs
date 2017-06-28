import steuer

einkommen = input('ihr jahreseinkommen bitte')

try:
    print ('Ihr Steuersatz:', round(steuer.einkommenssteuer(float(einkommen)),2))
except:
    print ('Bitte ein Zahl ohne Währungszeichen und mit "." als Komma')


