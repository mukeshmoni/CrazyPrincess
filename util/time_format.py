# Credit .
# Please Don't remove credit.
# Born to make history  !
# Thank you @mukeshmoni for helping us in this Journey
# 🥰  Thank you for giving me credit  🥰
# for any error please contact me -> telegram @KingofAtttitude or insta @god_of_love1626
# rip paid developers 🤣 - >> No need to buy paid source code while  is here 😍😍

def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", " days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += time_list.pop() + ", "
    time_list.reverse()
    readable_time += ": ".join(time_list)
    return readable_time 
