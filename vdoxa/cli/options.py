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
"""Enables optional arguments for commands.

These optional arguments are generally passed after a subparser.

All the arguments added in this module should begin with the command
name and end with the keyword `arg` seperated with underscores between
them.

Examples:
  * vdoxa trim <these come here>
  * vdoxa trim auto <these come here>
  * vdoxa trim custom <these come here>
"""

import argparse

from vdoxa.cli.arguments import (pass_video_by_arg, pass_video_parts_arg,
                                 pass_video_path_arg)


def trim_args(parser: argparse.ArgumentParser):
  """Parses arguments for `trim` command."""
  pass_video_path_arg(parser, help='Path of the video file.')
  pass_video_parts_arg(parser, help='Number of parts to split the video in.')


def trim_auto_args(parser: argparse.ArgumentParser):
  """Parses arguments for `trim auto` command."""
  pass_video_path_arg(parser, help='Path of the video file.')
  pass_video_parts_arg(parser, help='Number of parts to split the video in.')


def trim_custom_args(parser: argparse.ArgumentParser):
  """Parses arguments for `trim custom` command."""
  pass_video_path_arg(parser, help='Path of the video file.')
  pass_video_by_arg(parser, help='Trim video by a deciding factor.')
