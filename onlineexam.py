from pandas.core.internals import blocks
def apartmentHunting(blocks, reqs):
    blocks = [
        {
            "gym": False,
            "school": True,
            "store": False
        }, {
            "gym": True,
            "school": False,
            "store": False
        }, {
            "gym": True,
            "school": True,
            "store": False
        }, {
            "gym": False,
            "school": True,
            "store": False
        }, {
            "gym": False,
            "school": True,
            "store": True
        }
    ]

    reqs = ["gym", "school", "store"]

    def main():
        for index, b in enumerate(blocks):
            tmp_reqs = reqs.copy()
            for key in b.keys():
                if b[key] == True and key in tmp_reqs:
                    tmp_reqs.remove(key)

            if index - 1 >= 0:
                for key_1 in blocks[index - 1].keys():
                    if blocks[index - 1][key_1] == True and key_1 in tmp_reqs:
                        tmp_reqs.remove(key_1)

            if index + 1 < len(blocks):
                for key_2 in blocks[index + 1].keys():
                    if blocks[index + 1][key_2] == True and key_2 in tmp_reqs:
                        tmp_reqs.remove(key_2)

            if len(tmp_reqs) == 0:
                print("The ideal block is {} : {}".format(index, blocks[index]))
                break

    if __name__ == "__main__":
       main()
       pass