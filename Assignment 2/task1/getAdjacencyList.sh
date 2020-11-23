#!/bin/sh


echo `cat web-Google.txt | python3 Assignment_2_task1_mapper.py | python3 Assignment_2_task1_reducer.py > adj_list`