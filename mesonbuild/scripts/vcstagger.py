#!/usr/bin/env python3

# Copyright 2015-2016 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys, os, subprocess, re

def config_vcs_tag(infile, outfile, fallback, source_dir, replace_string, regex_selector, cmd):
    try:
        output = subprocess.check_output(cmd, cwd=source_dir)
        new_string = re.search(regex_selector, output.decode()).group(1).strip()
    except Exception:
        new_string = fallback

    new_data = open(infile).read().replace(replace_string, new_string)
    if (not os.path.exists(outfile)) or (open(outfile).read() != new_data):
        open(outfile, 'w').write(new_data)

def run(args):
    infile, outfile, fallback, source_dir, replace_string, regex_selector = args[0:6]
    command = args[6:]
    config_vcs_tag(infile, outfile, fallback, source_dir, replace_string, regex_selector, command)

if __name__ == '__main__':
    sys.exit(run(sys.argv[1:]))
