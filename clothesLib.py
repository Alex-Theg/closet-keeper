#!/usr/bin/env python3

import json

class ClothingItem:
    image = ""
    name = ""
    size = ""
    isFavorite = False
    
    def __init__(self  = "", image  = "", name  = "", size  = "", isFavorite = False):
        self.image = image
        self.name = name
        self.size = size
        self.isFavorite = isFavorite

    def exportToJson(self):
        return json.dumps(self.__dict__)