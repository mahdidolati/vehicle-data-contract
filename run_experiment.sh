
#!/bin/bash

rm reports/*
for itr_num in {1..1}
do
    for policy_len in {1..2}
    do
    for clause_len in {1..2}
        do
            rm -rf build; brownie run scripts/main.py main $itr_num $policy_len $clause_len --network glocal
        done
    done
done
