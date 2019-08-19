# -*- coding: utf-8 -*-
"""Main module.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import cli

shtech = cli.execute("show tech-support")

fp = open('/bootflash/reload_shtech.txt','w')

fp.write("sh tech upon reload command from "+timestamp+"\n\n")

fp.write(shtech+"\n\n")

fp.close()

cli.execute("reload command detected. Check /bootflash/reload_shtech.txt for show tech output")