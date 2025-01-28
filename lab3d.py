#!/usr/bin/env python3

# Author ID: [sjdujua] 

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    output = p.communicate()
    free_space = output[0].decode('utf-8').strip()
    return free_space

if __name__ == '__main__':
    print(free_space())
