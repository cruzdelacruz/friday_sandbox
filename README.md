## Python Project Tempalte With CLI

### Description:

A simple tempalte for a python project with a cli.

**/src**          contains the main cli.py entry point<br>
**/src/command**    contains one command script to start but you can add more, all you need to do is register each command in the cli entrypoint<br>

**to register a commad**:
```
# in the cli.py main()
from friday_package.command import concentric_hex

concentric_hex.add_subparser(subparsers)
args = parser.parse_args()
args.func(args)
```

```
# in your command python file:

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
    # your command logic can start here
    print(f"Hello, {args.name}")
```

### Recommended Installation:

1. Create python venv
```
    python -m venv .venv
```
2. Activate it
```
    # linux:
    source .venv/bin/activate

    #windows:
    .\venv\Scripts\Activate
```
3. Install
```
    pip install -e .
```