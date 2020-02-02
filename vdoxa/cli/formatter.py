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
"""Provides custom formatter.

These custom formatter inherits RawTextHelpFormatter and uses it's
methods to override them. It provides custom ``Usage`` and ``MetaVar``
sections.
"""

import argparse
import os
import textwrap


class VdoXAHelpFormatter(argparse.RawTextHelpFormatter):
  """Overrides RawTextHelpFormatter class."""
  # You can find the reference code here:
  # https://stackoverflow.com/questions/35847084/customize-argparse-help-message
  def add_usage(self, usage, actions, groups, prefix=None):
    """Captilizes the usage text."""
    if prefix is None:
      prefix = 'Usage: ' + '\n' + '  '
    return super(VdoXAHelpFormatter, self).add_usage(usage, actions,
                                                     groups, prefix)

  # You can find the reference code here:
  # https://stackoverflow.com/questions/35917547/python-argparse-rawtexthelpformatter-with-line-wrap
  def _split_lines(self, text, width):
    """Unwraps the lines to width of the terminal."""
    text = self._whitespace_matcher.sub(' ', text).strip()
    return textwrap.wrap(text, round(os.get_terminal_size().columns / 1.3))

  # You can find the reference code here:
  # https://stackoverflow.com/questions/13423540/argparse-subparser-hide-metavar-in-command-listing
  def _format_action(self, action):
    """Hides MetaVar in command listing."""
    parts = super()._format_action(action)
    if action.nargs == argparse.PARSER:
        parts = '\n'.join(parts.split('\n')[1:])
    return parts
