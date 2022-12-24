#!/usr/bin/env python3

import json
import clothesLib as CL

def getCommand():
    result = input("> ")
    return result

def main():
    shirt = CL.ClothingItem()
    strjson = shirt.exportToJson()
    print(strjson)

if __name__ == "__main__":
    main()


