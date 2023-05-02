from statistic_collector import StatCollector, Stat
from mahdi_plotter.plotter import Plotter
import os

EncTime = "EncTime"
DecTime = "DecTime"
stats = {
    EncTime: Stat.MEAN_MODE,
    DecTime: Stat.MEAN_MODE
}
algs = ["Case1", "Case2"]
stat_collector = StatCollector(algs, stats)
policy_lens = []
clause_lens = []

for filename in os.listdir("./reports/"):
    data_file = open("./reports/" + filename, "r")
    run_name = filename[2:]
    filename = filename.split("-")
    policy_len = int(filename[1])
    clause_len = int(filename[2])
    if policy_len not in policy_lens:
        policy_lens.append(policy_len)
    if clause_len not in clause_lens:
        clause_lens.append(clause_len)
    for line in data_file:
        line = line.split(" ")
        alg_name = line[0]
        stat_name = line[1]
        run_name = "{}-{}".format(policy_len, clause_len) 
        if stat_name in [EncTime, DecTime]:
            # print(line[2])
            stat_collector.add_stat(alg_name, stat_name, run_name, float(line[2]))

policy_lens.sort()
print(policy_len)
stat_collector.write_to_file('a1.txt', policy_lens, 0, EncTime, algs, EncTime, EncTime)
plotter = Plotter()
plotter.grouped_bar_err_plot('a1', 'a1.pdf')

clause_lens.sort()
print(clause_len)
stat_collector.write_to_file('a2.txt', clause_lens, 1, EncTime, algs, EncTime, EncTime)
plotter = Plotter()
plotter.grouped_bar_err_plot('a2', 'a2.pdf')