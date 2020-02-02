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
"""Holds usage, help and descriptions strings for the parsers."""

# Parent parser object.
epilog = ('For specific information about a particular command, run "vdoxa '
          '<command> -h".\nRead complete documentation at: '
          '<https://github.com/xames3/vdoxa>\n\nCopyright 2020 XAMES3. '
          'All Rights Reserved.')

# Trim subparser object.
trim_usage = ('vdoxa trim [options] --path <local video path> --num_parts '
              '<num> ...\n  '
              'vdoxa trim [options] auto --path <local video path> ...\n  '
              'vdoxa trim [options] custom --by <trim by> ...\n  '
              'vdoxa trim [options] <no arguments> ...\n  ')
trim_help = ('Trims the video for further processing into small chunks. '
             'These videos can be trimmed either by selecting portions of it '
             'by minutes or by seconds or can be trimmed automatically in "n" '
             'number of equal parts. These trimmed videos will be unpacked in '
             '"~/.<video file>/" directory (same directory with file name)')
trim_description = ('Description:\n  Getting started for vdoXA:\n\n  '
                    '- Trims video automatically in equal parts.\n  '
                    '- Trims video for a selected portion by minutes or by '
                    'seconds.\n\n')

# Trim auto subparser object.
auto_usage = ('vdoxa trim auto --path <local video path> --parts '
              '<num of parts> ...\n  '
              'vdoxa trim auto --path <local video path> ...\n')
auto_help = ('Trims the video for further processing into small chunks. '
             'These videos can be trimmed automatically in "n" number of '
             'equal parts. These trimmed videos will be unpacked in '
             '"~/.<video file>/" directory (same directory with file name)')
auto_description = ('Description:\n  Similar to "vdoxa trim":\n\n  '
                    '- Trims video automatically in equal parts.\n\n')

# Trim custom subparser object.
custom_usage = ('vdoxa trim custom --by <trim by> ...\n  ')
custom_help = ('Trims the video for further processing into small chunks. '
               'These videos can be trimmed either by selecting portions of it '
               'by minutes or by seconds. These trimmed videos will be '
               'unpacked in "~/.<video file>/" directory (same directory '
               'with file name)')
custom_description = ('Description:\n  Trims video according to needs:\n\n  '
                      '- Trims video for a selected portion by minutes or by '
                      'seconds.\n\n')
