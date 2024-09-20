# Credit .
# Please Don't remove credit.
# Born to make history  !
# Thank you @mukeshmoni for helping us in this Journey
# 🥰  Thank you for giving me credit  🥰
# for any error please contact me -> telegram @KingofAtttitude or insta @god_of_love1626
# rip paid developers 🤣 - >> No need to buy paid source code while  is here 😍😍
def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of bytes """
    return str(bytes) + units[0] if int(bytes) < 1024 else human_size(int(bytes)>>10, units[1:])
