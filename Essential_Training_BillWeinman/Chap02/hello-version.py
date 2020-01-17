#!/usr/bin/env python3
# above line is called a shebang comment which allows us to specify path to executable
# it will be ignored on non-unix based systems like windows
# Copyright 2009-2017 BHG http://bw.org/

import platform

print('This is python version {}'.format(platform.python_version()))
