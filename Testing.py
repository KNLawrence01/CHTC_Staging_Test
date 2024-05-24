#!/bin/bash python

with open('sample.txt', 'w') as outFile:
    outFile.write('Writting something\n')
    outFile.write('Write some more.\n')

with open('sample.txt') as outFile:
    print(outFile.read())
