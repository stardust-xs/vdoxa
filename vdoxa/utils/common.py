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
"""Utility for performing common functions."""

from datetime import datetime
import logging
import os
import subprocess
import sys
from typing import Union

logger = logging.getLogger(__name__)


def now() -> datetime:
  """Return current time without microseconds."""
  return datetime.now().replace(microsecond=0)


def check_version(package_name: str) -> None:
  """Compare current and latest version of the package.

  Check and compares= the installed version versus the latest version of
  package available on `PyPI` and returns a favorable response. If a
  newer version is available for download it will recommend upgrading to
  it.

  Arg:
    package_name: Package name whose version needs to be checked.

  Example:
    >>> from vdoxa.utils.common import check_version
    >>> check_version()

    You are using the latest version of vdoxa, 0.1
  """
  current = str(subprocess.run([sys.executable, '-m', 'pip',
                                'show', package_name],
                                capture_output=True, text=True))
  name = current[current.find('Name:') + 5:]
  name = name[:name.find('\\n')].replace(' ', '')

  version = current[current.find('Version:') + 8:]
  version = version[:version.find('\\n')].replace(' ', '')

  latest = str(subprocess.run([sys.executable, '-m', 'pip', 'install',
                               f'{package_name}==random'], capture_output=True, text=True))
  latest = latest[latest.find('(from versions:') + 15:]
  latest = latest[:latest.find(')')]
  latest = latest.replace(' ', '').split(',')[-1]

  if latest == 'none':
    print(f'Installed {name} version is {version}')
  elif version == latest:
    print(f'You are using the latest version of {name}, {version}')
  else:
    print(f'You are using an older version of {name}, {version}. However '
          f'version, {latest} is available for download. You should '
          f'consider upgrading via "pip install --upgrade {name}" '
          'command.')


def set_log_level(log_level: Union[int, str] = None) -> None:
  """Set logging level.

  Set a logging level for the operation if it is not set. The default
  logging level is INFO.

  Arg:
      log_level: Logging level to be set.
  """
  if not log_level:
    log_level = os.environ.get('VDOXA_LOG_LEVEL', 'INFO')
    log_level = logging.getLevelName(log_level)

  logging.getLogger('vdoxa').setLevel(log_level)
