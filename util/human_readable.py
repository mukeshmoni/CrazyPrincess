# Credit .
# Please Don't remove credit.
# Born to make history  !
# Thank you @mukeshmoni for helping us in this Journey
# 🥰  Thank you for giving me credit  🥰
# for any error please contact me -> telegram @KingofAtttitude or insta @god_of_love1626
# rip paid developers 🤣 - >> No need to buy paid source code while  is here 😍😍
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
