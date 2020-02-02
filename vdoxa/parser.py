# Copyright 2019 XAMES3. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ======================================================================
"""The `vdoxa.parser` module helps exposing the main parser.

The functions in this module allow the usage of the vdoXA module over
the CLI. The function, 'global_parser' allows the use of 'vdoxa' keyword
on the CLI whereas the 'main' function parses the arguments to the
parser object.

The 'global_parser' functions also allows to share visual similarities
with the 'pip' module.

Todo:
    * Add support for handling 'help' as an argument.
"""

import argparse

from vdoxa.cli import strings
from vdoxa.cli.arguments import add_logging_options
from vdoxa import trim_parser
from vdoxa.cli.formatter import VdoXAHelpFormatter as HelpFormatter
from vdoxa.utils.common import check_version, set_log_level
from vdoxa.vars.dev import PROJECT_NAME


def global_parser() -> argparse.ArgumentParser:
  """Creates and returns the main parser for vdoxa's CLI.

  It powers the main argument parser for the pyXA module and enables
  sharing a lot of visual similarities with the 'pip' module.

  Returns:
    ArgumentParser object, which stores all the properties of the
    main argument parser.

  Example:
    >>> from vdoxa.parser import global_parser
    >>> global_parser()

    ArgumentParser(prog='vdoxa', usage='vdoxa <command> [options] ...
  """
  print()
  prog = PROJECT_NAME.lower()
  usage = f'{prog} <command> [options]'
  parser = argparse.ArgumentParser(prog=prog, usage=usage,
                                   formatter_class=HelpFormatter,
                                   conflict_handler='resolve',
                                   epilog=strings.epilog,
                                   add_help=False)
  parser._positionals.title = 'Commands'
  parser._optionals.title = 'Extra Options'
  parser.add_argument('-h', '--help', action='store_true',
                      default=argparse.SUPPRESS, help='Show help.')
  parser.add_argument('-V', '--version', action='store_true',
                      default=argparse.SUPPRESS,
                      help='Show installed vdoXA version and exit.')

  parent_parser = argparse.ArgumentParser(add_help=False)
  add_logging_options(parent_parser)
  parent_parsers = [parent_parser]
  subparsers = parser.add_subparsers(prog=prog)
  trim_parser.subparser(subparsers, parents=parent_parsers)
  return parser


def main() -> None:
  """Primary application entrypoint.

  This function is called at the entrypoint. It means that when the
  user runs this function it will display CLI for the vdoXA module.

  Example:
    >>> from vdoxa.parser import main
    >>> main()

    Usage:
      vdoxa <command> [options]

    Commands:
      trim       Trims the video for further processing ...

    Extra Options:
    -h, --help     Show help.
    -V, --version  Show installed vdoXA version and exit.

    For specific information about a particular command, run ...
    Read complete documentation at: <https://github.com/xames3/vdoxa>

    Copyright 2020 XAMES3. All Rights Reserved.
  """
  parser = global_parser()
  cmd_args = parser.parse_args()
  log_level = cmd_args.loglevel if hasattr(cmd_args, 'loglevel') else None
  set_log_level(log_level)
  if hasattr(cmd_args, 'function'):
    cmd_args.function(cmd_args)
  elif hasattr(cmd_args, 'version'):
    check_version(PROJECT_NAME.lower())
  else:
    parser.print_help()
    exit(1)
