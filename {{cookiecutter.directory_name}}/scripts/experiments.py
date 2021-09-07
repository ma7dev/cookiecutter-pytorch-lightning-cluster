from typing import List
import yaml
import fire
from train import train


def main(config_path: str, selected: List = [], all: bool = False):
    experiments = yaml.load(open(config_path), Loader=yaml.FullLoader)
    root_path = experiments["ROOT_PATH"]
    print(root_path)

    print(config_path)
    print(selected)
    print(all)
    if all:
        for experiment, _ in experiments.items():
            print(experiment)
            train(config_path, experiment)
    elif selected:
        if type(selected) == str:
            print(selected)
            train(config_path, selected)
        else:
            for experiment in selected:
                print(experiment)
                train(config_path, experiment)
    else:
        print("nothing selected")


if __name__ == "__main__":
    fire.Fire(main)