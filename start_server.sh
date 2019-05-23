#!/bin/bash

/usr/local/spark/bin/spark-submit --master local --total-executor-cores 4 --executor-memory 6g server.py 