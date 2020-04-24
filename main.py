import sys
import random


if(len(sys.argv) == 2):
    if(sys.argv[1] == "list"):
        d_list = open(".domain_list", 'r')
        print(d_list.read())
        d_list.close()

if(len(sys.argv) == 3):
    url = sys.argv[1]
    key = sys.argv[2]
    if(len(url.split('.')) == 2 and len(url.split('.')[1]) == 3):
        d_list = open(".domain_list", 'a')
        d_list.write(url + "\n")
        d_list.close()

        pass_len = 20
        seed_str = ""

        for i in range(len(url) - 1):
            if(i < len(key)):
                seed_str += str(ord(key[i]))
            seed_str += str(ord(url[i]))

        if(len(key) > len(url)):
            for i in range(len(key) - len(url)):
                seed_str += str(ord(key[i + len(url) - 1]))

        seed = int(seed_str)
        random.seed(seed)

        pass_str = ""
        for i in range(pass_len):
            pass_str += chr(random.randint(32, 127))

        print(pass_str)