
def add_subparser(subparsers):
    parser = subparsers.add_parser("print_hello")
    parser.add_argument(
        "-s",
        "--size",
        required=False,
        help="Size of your concentrix hexagon"
    )
    parser.add_argument(
        "-n",
        "--name",
        required=False,
        help="A name"
    )
    parser.set_defaults(func=run)
def run(args):
    print(f"Hello, {args.name}")