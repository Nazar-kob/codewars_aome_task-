# Help Suzuki purchase his Tofu!
# Suzuki has sent a lay steward to market who will
# purchase some items not produced in the monastary
# gardens for the monks. The stewart has with him a
# large box full of change from donations earlier in
# the day mixed in with some personal items. You will
# be given a string of items representing the box.
# Sort through the items in the box finding the coins
# and putting aside anything else.
# You will be given a data structure similar to the one below.



def buy_tofu(cost, box):
    mon = box.count('mon')
    monme = box.count('monme')
    if mon + monme < cost:
        return 'leaving the market'
    return [mon, monme, mon + monme, cost]

