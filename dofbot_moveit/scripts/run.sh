#!/bin/bash
./detection_bin.sh
sleep 15
# to run garbage classification twice, can add more or do a for loop to run multiple times
./detection_garbage.sh
sleep 15
./detection_garbage.sh
