from  eosfactory import *
import argparse

parser = argparse.ArgumentParser(description='''
Given a workspace name and a template name (optional),
create a new workspace, compatible with Visual Studio Code.

Example:
    python3 create_workspace.py contract.name 01_hello_world
''')

parser.add_argument("name")
parser.add_argument("template", nargs="?", default="01_hello_world")
parser.add_argument("--vsc", help="open Visual Studio Code", action="store_true")

args = parser.parse_args()
contract_workspace_from_template(args.name, template=args.template, visual_studio_code=args.vsc)
