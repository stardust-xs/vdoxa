# Copyright 2020 XAMES3. All Rights Reserved.
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
"""Trim video subparser command."""

import argparse
import os
from typing import List

from vdoxa.cli import strings
from vdoxa.cli.formatter import VdoXAHelpFormatter as HelpFormatter
from vdoxa.cli.options import trim_args, trim_auto_args, trim_custom_args
from vdoxa.core.trim import trim_by, trim_num_parts
from vdoxa.utils.options import select_file
from vdoxa.vars.dev import PROJECT_NAME

prog = PROJECT_NAME.lower()


def subparser(subparsers: argparse._SubParsersAction,
              parents: List[argparse.ArgumentParser]) -> None:
  """Creates subparser object."""
  title = os.path.basename(__file__).split('.')[0].capitalize()
  parser = subparsers.add_parser('trim',
                                 usage=strings.trim_usage,
                                 help=strings.trim_help,
                                 formatter_class=HelpFormatter,
                                 parents=parents,
                                 description=strings.trim_description)
  trim_args(parser)
  parser._positionals.title = f'{title} Options'
  parser._optionals.title = f'{title} Arguments'
  trim = parser.add_subparsers()

  trim_auto_parser = trim.add_parser('auto',
                                     usage=strings.auto_usage,
                                     help=strings.auto_help,
                                     formatter_class=HelpFormatter,
                                     parents=parents,
                                     description=(strings.auto_description))
  trim_auto_parser.set_defaults(function=trim_auto)
  trim_auto_parser._positionals.title = f'{title} Auto Options'
  trim_auto_parser._optionals.title = f'{title} Auto Arguments'

  trim_custom_parser = trim.add_parser('custom',
                                       usage=strings.custom_usage,
                                       help=strings.custom_help,
                                       formatter_class=HelpFormatter,
                                       parents=parents,
                                       description=(strings.custom_description))
  trim_custom_parser.set_defaults(function=trim_custom)
  trim_custom_parser._positionals.title = f'{title} Custom Options'
  trim_custom_parser._optionals.title = f'{title} Custom Arguments'
  parser.set_defaults(function=trim_auto_24)
  trim_auto_args(trim_auto_parser)
  trim_custom_args(trim_custom_parser)


def trim_auto_24(args: argparse.Namespace,
                 path: str = None) -> None:
  """Trim videos in 24 equal parts by default.

  Args:
    args: Arguments for storing attributes.
    path: Path (default: current directory) of the video file to be
          trimmed.
  """
  path = path or args.path
  trim_num_parts(path, 24)


def trim_auto(args: argparse.Namespace,
              path: str = None,
              parts: int = None) -> None:
  """Trim videos in "n" equal parts by default.

  Args:
    args: Arguments for storing attributes.
    parts: Number of parts the video needs to be trimmed into.
    path: Path (default: current directory) of the video file to be
          trimmed.
  """
  path = path or args.path
  parts = parts or args.parts
  trim_num_parts(path, int(parts))


def trim_custom(args: argparse.Namespace,
                path: str = None,
                by: str = None) -> None:
  """Trim videos by minutes or seconds.

  Args:
    args: Arguments for storing attributes.
    path: Path (default: current directory) of the video file to be
          trimmed.
    by: Trimming by (default: mins); secs available.
  """
  path = path or args.path
  by = by or args.by
  trim_by(path, by)
