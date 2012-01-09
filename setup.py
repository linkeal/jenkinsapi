from setuptools import setup, find_packages
import sys, os
from setup_config import DESCRIPTION, VERSION, PROJECT_NAME, PROJECT_AUTHORS, GLOBAL_ENTRY_POINTS, PROJECT_EMAILS, PROJECT_URL, SHORT_DESCRIPTION

setup(name=PROJECT_NAME.lower(),
      version=VERSION,
      author=PROJECT_AUTHORS,
      author_email=PROJECT_EMAILS,
      packages=find_packages('.'),
      zip_safe=True,
      include_package_data = False,
      entry_points = GLOBAL_ENTRY_POINTS,
      url=PROJECT_URL,
      description=SHORT_DESCRIPTION,
      long_description=DESCRIPTION,
      )
