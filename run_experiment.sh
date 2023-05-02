
#!/bin/bash


rm reports/*
for itr_num in {6..8}
do
    for policy_len in {1..4}
    do
    for clause_len in {1..4}
        do
            rm -rf build; brownie run scripts/main.py main $itr_num $policy_len $clause_len --network glocal
        done
    done
done
python3 aggregate_data.py
