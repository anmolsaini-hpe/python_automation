list = ["V1_abcd","V2_cejn","V300_dnmewx","V300_cenjc","V301_ceiknce"]

append_list = []

def get_prefix():
    for item in list:
        new_item = item.split("_")
        append_list.append(new_item[0])
    return append_list
#new_list = ["V1","V2","V300","V300","V301"]
newList = get_prefix()


def compare():
    for item in range(len(newList)):
        for item2 in range(item + 1, len(newList)):
            if newList[item] == newList[item2]:
                print("SAME")

compare()