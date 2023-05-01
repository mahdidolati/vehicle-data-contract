from statistic_collector import StatCollector, Stat
import os

CryptographyTime = "CryptographyTime"
stats = {
    CryptographyTime: Stat.MEAN_MODE
}
algs = ["Case 1", "Case 2"]
stat_collector = StatCollector(algs, stats)
policy_lens = []
clause_lens = []

for filename in os.listdir("./reports/"):
    run_name = filename[2:]
    filename = filename.split("-")
    policy_len = filename[1]
    clause_len = filename[2]
    data_file = open("./reports/" + filename, "r")
    policy_lens.append(policy_len)
    clause_lens.append(clause_len)
    for line in data_file:
        line = line.split(" ")
        alg_name = line[0]
        stat_name = line[1]
        run_name = "{}-{}".format(policy_len, clause_len) 
        stat_collector.add_stat(alg_name, stat_name, run_name, line[2])

policy_lens.sort()
stat_collector.write_to_file('a.txt', policy_lens, 0, CryptographyTime, algs, CryptographyTime, CryptographyTime)

clause_lens.sort()
stat_collector.write_to_file('a.txt', clause_lens, 1, CryptographyTime, algs, CryptographyTime, CryptographyTime)