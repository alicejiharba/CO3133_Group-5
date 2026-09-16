import argparse
import random

import yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    random.seed(config["seed"])
    if args.prepare_only:
        print(f"Preparing dataset at {config['dataset_path']} for assignment 3")
    else:
        print(
            f"Training assignment 3 with seed {config['seed']} "
            f"and checkpoints in {config['checkpoint_dir']}"
        )


if __name__ == "__main__":
    main()
