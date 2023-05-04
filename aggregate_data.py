from statistic_collector import StatCollector, Stat
from mahdi_plotter.plotter import Plotter
import os

Time = "Time"
policy_stats = {
    Time: Stat.MEAN_MODE
}
policy_algs = ["Enc", "Dec"]
policy_collector = StatCollector(policy_algs, policy_stats)
policy_lens = []

clause_stats = {
    Time: Stat.MEAN_MODE
}
clause_algs = ["Enc", "Dec"]
clause_collector = StatCollector(clause_algs, clause_stats)
clause_lens = []

crypto_stats = {
    Time: Stat.MEAN_MODE
}
crypto_algs = ["Case1", "Case2"]
crypto_collector = StatCollector(crypto_algs, crypto_stats)

ipfs_stats = {
    Time: Stat.MEAN_MODE
}
ipfs_algs = ["Case1", "Case2"]
ipfs_collector = StatCollector(ipfs_algs, ipfs_stats)

size_stats = {
    Time: Stat.MEAN_MODE
}
size_algs = ["alg_name"]
size_collector = StatCollector(size_algs, size_stats)

gas_algs = ["DeployGas", "SetAddrGas", "GetReqGas", "GetAddrGas", "GetFeeGas", "RequestGas"]
Group = "Group"
gas_stats = {
    Group: Stat.MEAN_MODE
}
gas_collector = StatCollector(gas_algs, gas_stats)

contract_algs = ["DeployTime", "SetAddrTime", "GetAddrTime", "RequestTime", "GetReqTime", "GetFeeTime"]
Group = "Group"
contract_stats = {
    Group: Stat.MEAN_MODE
}
contract_collector = StatCollector(contract_algs, contract_stats)

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
        if alg_name in ["Case1"] and clause_len == 6:
            if stat_name == "EncTime":
                policy_collector.add_stat("Enc", Time, "{}".format(policy_len), float(line[2]))
            if stat_name == "DecTime":
                policy_collector.add_stat("Dec", Time, "{}".format(policy_len), float(line[2]))
        if alg_name in ["Case1"] and policy_len == 6:
            if stat_name == "EncTime":
                clause_collector.add_stat("Enc", Time, "{}".format(clause_len), float(line[2]))
            if stat_name == "DecTime":
                clause_collector.add_stat("Dec", Time, "{}".format(clause_len), float(line[2]))
        if clause_len == 6 and policy_len == 6:
            if stat_name == "EncTime":
                crypto_collector.add_stat(alg_name, Time, "0", float(line[2]))
            if stat_name == "DecTime":
                crypto_collector.add_stat(alg_name, Time, "1", float(line[2]))
        if clause_len == 6 and policy_len == 6:
            if "Size" in stat_name and alg_name == "Case1":
                size_collector.add_stat("alg_name", Time, "0", float(line[2]))
            if "Size" in stat_name and alg_name == "Case2":
                size_collector.add_stat("alg_name", Time, "1", float(line[2]))
        if clause_len == 6 and policy_len == 6:
            if stat_name == "IpfsSaveTime":
                ipfs_collector.add_stat(alg_name, Time, "0", float(line[2]))
            if stat_name == "IpfsReadTime":
                ipfs_collector.add_stat(alg_name, Time, "1", float(line[2]))
        if clause_len == 6 and policy_len == 6:
            if stat_name in gas_algs:
                if alg_name == "Case1" or stat_name == "DeployGas":
                    gas_collector.add_stat(stat_name, Group, "0", float(line[2]))
                if alg_name == "Case2" or stat_name == "DeployGas":
                    gas_collector.add_stat(stat_name, Group, "1", float(line[2]))
        if clause_len == 6 and policy_len == 6:
            if stat_name in contract_algs:
                if alg_name == "Case1" or stat_name == "DeployTime":
                    contract_collector.add_stat(stat_name, Group, "0", float(line[2]))
                if alg_name == "Case2" or stat_name == "DeployTime":
                    contract_collector.add_stat(stat_name, Group, "1", float(line[2]))

policy_lens.sort()
print(policy_lens)
policy_collector.write_to_file('./f/policy_collector.txt', policy_lens, 0, Time, policy_algs, "Number of Entities", "Time (sec)")
plotter = Plotter()
plotter.grouped_bar_err_plot('./f/policy_collector', './f/policy_collector.pdf')

clause_lens.sort()
print(clause_lens)
clause_collector.write_to_file('./f/clause_collector.txt', clause_lens, 0, Time, clause_algs, "Number of Attributes", "Time (sec)")
plotter = Plotter()
plotter.grouped_bar_err_plot('./f/clause_collector', './f/clause_collector.pdf')

crypto_collector.write_to_file('./f/crypto_collector.txt', [0, 1], 0, Time, crypto_algs, "Cryptography Operation", "Time (sec)")
plotter = Plotter()
plotter.grouped_bar_err_plot('./f/crypto_collector', './f/crypto_collector.pdf')

ipfs_collector.write_to_file('./f/ipfs_collector.txt', [0, 1], 0, Time, ipfs_algs, "IPFS Operation", "Time (sec)")
plotter = Plotter()
plotter.grouped_bar_err_plot('./f/ipfs_collector', './f/ipfs_collector.pdf')

for ss in ["GetReqGas", "GetFeeGas", "RequestGas"]:
    gas_collector.add_stat(ss, Group, "0", 0.0)
gas_collector.write_to_file('./f/gas_collector.txt', [0, 1], 0, Group, gas_algs, "IPFS Operation", "Time (sec)")
plotter = Plotter()
plotter.stacked_bar_err_plot('./f/gas_collector', './f/gas_collector.pdf')

size_collector.write_to_file('./f/size_collector.txt', [0, 1], 0, Time, size_algs, "Encryption Method", "Size (byte)")
plotter = Plotter()
plotter.grouped_bar_err_plot('./f/size_collector', './f/size_collector.pdf')

for ss in ["GetReqTime", "GetFeeTime", "RequestTime"]:
    contract_collector.add_stat(ss, Group, "0", 0.0)
contract_collector.write_to_file('./f/contract_collector.txt', [0, 1], 0, Group, contract_algs, "IPFS Operation", "Time (sec)")
plotter = Plotter()
plotter.stacked_bar_err_plot('./f/contract_collector', './f/contract_collector.pdf')