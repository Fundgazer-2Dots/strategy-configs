import os
import json

directory = "pattern_backtest/config"
output_dir = "pattern_backtest/converted"

with open("coversion_configs/condition_name.json") as file:
    condition_name = json.load(file)

# condition_name_clone = condition_name.copy()
# for key,val in condition_name_clone.items():
#     condition_name[key.lower()] = val

# with open("coversion_configs/condition_name.json", "w") as file:
#         json.dump(condition_name, file, indent=2)

with open("coversion_configs/condition_params.json") as file:
    condition_params = json.load(file)

# condition_params_clone = condition_params.copy()
# for key,val in condition_params_clone.items():
#     condition_params[key.lower()] = val

# with open("coversion_configs/condition_params.json", "w") as file:
#         json.dump(condition_params, file, indent=2)

# exit(0)


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if not os.path.isfile(f):
        continue

    with open(f) as file:
        configs = json.load(file)

    reverse_configs = []
    for idx, conf in enumerate(configs):
        rever_configs = None
        conditions = conf["conditions"]
        for cond in conditions:

            name = cond["name"]
            new_param = condition_params[name]
            new_name = condition_name[name]
            cond["name"] = new_name.strip()
            cond["params"] = new_param

        conf["config_id"] = idx
        conf["bar_count"] = -1
        conf_clone = conf.copy()
        for key, val in conf_clone.items():

            if key not in [
                "config_id",
                "strategy",
                "symbol",
                "timeframe",
                "bar_count",
                "conditions",
                "divergence",
                "bullish",
                "bearish",
                "exit1",
                "exit2",
            ]:
                del conf[key]

        conf_clone = conf.copy()
        conf_clone["exit1"] = not conf_clone["exit1"]
        conf_clone["exit2"] = not conf_clone["exit2"]
        reverse_configs.append(conf_clone)

    with open(f"{output_dir}/{filename}", "w") as file:
        json.dump(configs, file, indent=2)

    filename_token = os.path.splitext(filename)

    with open(f"{output_dir}/{filename_token[0]}_reverse.json", "w") as file:
        json.dump(reverse_configs, file, indent=2)

    
