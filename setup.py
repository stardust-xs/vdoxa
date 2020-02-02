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
"""
vdoXA is an open-source python package for trimming the videos.

It is built as a subsystem for < XXXXX Not to be named XXXXX > project.

Originally inspired by my colleague's work, I thought of improving the
concept and build a tool to simplify the process. I hope it comes with
strong support for continuous updates, reliable functions and overall
ease of use.

Read complete documentation at: <https://github.com/xames3/vdoxa>.
"""
from setuptools import find_packages, setup

from vdoxa.vars import dev

doclines = __doc__.split('\n')


def use_readme() -> str:
  """Use `README.md` for parsing long description."""
  with open('README.md') as file:
    return file.read()


with open('requirements.txt', 'r') as requirements:
  required_packages = [package.rstrip() for package in requirements]

setup(
  name=dev.PROJECT_NAME,
  version=dev.PROJECT_VERSION,
  url=dev.PROJECT_LINK,
  download_url=dev.PROJECT_LINK,
  author=dev.AUTHOR,
  author_email=dev.AUTHOR_EMAIL,
  maintainer=dev.AUTHOR,
  maintainer_email=dev.AUTHOR_EMAIL,
  classifiers=[
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    ],
  license=dev.PROJECT_LICENSE,
  description=f'{doclines[1]}',
  long_description=use_readme(),
  long_description_content_type='text/markdown',
  keywords='opencv2 cv2 moviepy',
  zip_safe=False,
  install_requires=required_packages,
  python_requires='~=3.6',
  include_package_data=True,
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'vdoxa = vdoxa.parser:main',
      ],
  }
)
