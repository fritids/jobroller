#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_bootstrap.settings")

    # sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
