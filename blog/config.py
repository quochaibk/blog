# -*- coding: utf-8 -*-
"""
    @author: Hai
    
"""
import sys
import os
import json


 
def load_config():
    try:
        configure= json.load(open(os.path.join(os.path.dirname(__file__), 'config.json'),'r'))
        return configure
    except Exception as ex:
        sys.exit(sys.exc_info())

