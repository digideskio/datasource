#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import sys


def is_python_test(filename):
    return os.path.splitext(filename)[1] == '.py' and filename.lower().startswith('test')

current_directory = os.path.dirname(os.path.abspath(__file__))
failed = False

for (dirpath, dirname, filenames) in os.walk(current_directory):
    for filename in filenames:
        if is_python_test(filename):
            relpath = os.path.relpath(os.path.join(dirpath, filename), current_directory)
            test = __import__(os.path.splitext(relpath)[0].replace('/', '.').replace('\\', '.'), fromlist='main')
            print '\nRunning tests in %s' % relpath
            test_passed = test.main()
            if not test_passed:
                failed = True

if failed:
    print '\nTests failed!'
    sys.exit(1)
