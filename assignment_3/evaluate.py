import argparse

import yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    print(
        f"Evaluating assignment 3 using checkpoints from "
        f"{config['checkpoint_dir']}"
    )


if __name__ == "__main__":
    main()
