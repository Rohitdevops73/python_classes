#waf to convert usd to inr

def usd_inr(dollar, exchange_rate):
    inr_val = dollar * exchange_rate

    return inr_val

print(usd_inr(2,95))