#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""A simple script to generate a CSV with sine data."""

import csv
import math


def run():
  fileHandle = open("sine.csv","w")
  writer = csv.writer(fileHandle)
  writer.writerow(["angle","sine"])
  writer.writerow(["float","float"])
  writer.writerow(["",""])
  
  for angle in range(1500):
    angle_rad = math.radians(angle)
    sine_value = math.sin(angle_rad)
    writer.writerow([angle_rad, sine_value])
    
  fileHandle.close()
  

if __name__ == "__main__":
  run()
