
def add_subparser(subparsers):
    parser = subparsers.add_parser("print_hello")
    parser.add_argument(
        "-s",
        "--size",
        required=True,
        help="Size of your concentrix hexagon"
    )
    parser.set_defaults(func=run)
def run(args):
    print(f"Hello, {args.name}")