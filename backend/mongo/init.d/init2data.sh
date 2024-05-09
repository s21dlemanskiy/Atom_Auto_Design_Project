#!/bin/bash

mongoimport -d db1 -c texts --file '/home/texts.json'

mongoimport -d db1 -c adjectives --file '/home/adjectives.json'