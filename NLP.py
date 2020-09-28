#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:41:15 2020

@author: medasahithi
"""


from Selenium_bot import Bot
import argparse

def generate_txt(My_List):
    Link_txt = open("Links.txt", 'w+')
    for Link in My_List:
        Link_txt.write(Link + "\n")

def NLP(config):
    username = config.username
    password = config.password
    b = Bot()
    b.setUp()
    b.go_to_page("https://www.instagram.com/accounts/login/")
    b.login(username, password)
    wordlist=["food"]
    count=1000
    Links = b.get_image_URL(wordlist,count)
    generate_txt(Links)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # input parameters
    parser.add_argument('--username', type=str)
    parser.add_argument('--password', type=str)

    config = parser.parse_args()

    NLP(config)
