import argparse

def main():
    parser = argparse.ArgumentParser(description="Sandbox CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    from friday_package.command import concentric_hex

    concentric_hex.add_subparser(subparsers)
    args = parser.parse_args()
    args.func(args)

if __name__=="__main__":
    main()