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
"""Allows use of arguments for command.

These arguments often begin with '-' or '--'.

All the arguments added in this module should begin with the keyword
'pass' and end with the keyword 'arg' seperated with underscores
between them.

Examples:
  * vdoxa trim --path <these come here> --parts <and here>
  * vdoxa trim auto --parts <these come here>
  * vdoxa trim custom --by <these come here>
"""

import argparse
import logging
from typing import Optional, Union

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def pass_video_path_arg(parser: Union[argparse.ArgumentParser,
                                      argparse._ActionsContainer],
                        help: str,
                        default: Optional[str] = 'current directory') -> None:
  """Pass argument for the video path."""
  parser.add_argument('--path', default=default,
                      help=help, type=str, metavar='<path>')


def pass_video_parts_arg(parser: Union[argparse.ArgumentParser,
                                         argparse._ActionsContainer],
                           help: str,
                           default: Optional[int] = 24) -> None:
  """Pass argument for number of videos to split into."""
  parser.add_argument('--parts', default=default,
                      help=help, type=str, metavar='<number>')


def pass_video_by_arg(parser: Union[argparse.ArgumentParser,
                                         argparse._ActionsContainer],
                      help: str,
                      default: Optional[str] = 'mins') -> None:
  """Pass argument to trim video by deciding factor."""
  parser.add_argument('--by', default=default,
                      help=help, type=str, metavar='<trim by>')


def add_logging_options(parser: Union[argparse.ArgumentParser,
                                      argparse._ActionsContainer]) -> None:
  """Adds logging options to the parser object."""
  parser = parser.add_argument_group('Logging Options')
  parser.add_argument('-v',
                      '--verbose',
                      action='store_const',
                      dest='loglevel',
                      help='Give more output. Increase output verbosity.',
                      const=logging.INFO)
  parser.add_argument('-d',
                      '--debug',
                      action='store_const',
                      dest='loglevel',
                      help='Print all debugging statements.',
                      const=logging.DEBUG)
  parser.add_argument('-q',
                      '--quiet',
                      action='store_const',
                      dest='loglevel',
                      help=('Give less output. Decrease output verbosity '
                            '(respond only to WARNING, ERROR, and '
                            'CRITICAL logging levels).'),
                      const=logging.WARNING)
