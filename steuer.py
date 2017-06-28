# die erste 11000 sind steuerfrei
# die nächsten 7000€ werden mit 25% versteuert
# die nächsten 13000 mit 35%
# usw...
tax_hash = {
    11000:  25, # am 11000 25%
    18000:  35, # ab 18000 35%
    31000:  42, # ab 31000 42%
    60000:  48, # ab 60000 48%
    90000:  50, # ab 90000 50%
    1000000:55  # ab 1000000 55%
}

def einkommenssteuer(einkommen):
    steuer = 0
    steuersatz = 0
    untergrenze = 0
    for steuerstufe in tax_hash:
        if einkommen < (steuerstufe - untergrenze):
            break
        else:
            steuer += (steuerstufe - untergrenze ) * steuersatz
            steuersatz = tax_hash[steuerstufe] / 100
            einkommen -= steuerstufe - untergrenze
            untergrenze = steuerstufe

    steuer += einkommen * steuersatz
    return steuer