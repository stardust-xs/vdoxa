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
"""Core utility for trimming the video."""

import os
import random
from datetime import timedelta
from typing import Any, Optional, Union

from moviepy.editor import VideoFileClip as vfc

from vdoxa.utils.common import now
from vdoxa.utils.file_ops import filename
from vdoxa.utils.options import ask_numbers, confirm
from vdoxa.vars.cmd import TRIM_END, TRIM_START


def trim_video(source: Any,
               file: str,
               start: Optional[Union[float, int]] = 0,
               end: Optional[Union[float, int]] = 30) -> None:
  """Trim video."""
  trimmed_video = vfc(source, verbose=True).subclip(start, end)
  trimmed_video.write_videofile(file, codec='libx264')


def delta(value: Union[float, int], factor: str) -> timedelta:
  """Returns value in timedelta format."""
  if factor == 'mins':
    return timedelta(minutes=value, )
  else:
    return timedelta(seconds=value)


def trim_by(source: Any, factor: str = 'mins') -> None:
  """Trim the video by deciding factor."""
  _factor = 1 if factor == 'secs' else 60
  total_limit = float(vfc(source).duration) / _factor
  start = ask_numbers(TRIM_START)
  end = ask_numbers(TRIM_END)
  _start = delta(start, factor)
  _end = delta(end, factor)
  if factor == 'percentage':
    start = round((start / 100) * total_limit, 2)
    end = round((end / 100) * total_limit, 2)
    factor = 'mins'
    total_limit = 100.0
  # If end time is less than start time, terminate the program.
  if end < start:
    print('? The ending time is less than starting time. Please choose '
          f'value greater than {start} {factor}.')
    exit(0)
  else:
    if end >= total_limit:
      if factor == 'percentage':
        print(f'? Video doesn\'t have additional frames to process. '
              f'It\'ll max out at {total_limit}%.')
      else:
        print(f'? Video doesn\'t have additional {end - total_limit} '
              f'frames to process. It\'ll max out at {total_limit} {factor}.')
      end = total_limit
    elif start < 0:
      print('? Start time should be equal or greater than 0. Choosing '
            f'default start time 0 {factor}.')
      start = 0
    print(f'? Video clip of {_end - _start} {factor} '
          f'will be created from {start} {factor} to {end} {factor}.')
    file = filename(source, 0)
    if os.path.isfile(file):
      overwrite = confirm('File with same name exists already. '
                          'Would you like to overwrite that one?')
      if not overwrite:
        file = filename(source, random.randint(00000, 99999))
    trim_video(source, file, start * _factor, end * _factor)


def trim_num_parts(source: Any, num_parts: int) -> None:
  """Trim video in number of equal parts."""
  total_limit = float(vfc(source).duration)
  split_part = total_limit / num_parts
  start = 0
  for idx in range(num_parts):
    file = filename(source, idx)
    start, end = start, start + split_part
    trim_video(source, file, start, end)
    start += split_part
  print(f'Completed trimming {file}.', end='\r')
