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

import math
import csv
import shutil

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic_output import NuPICFileOutput, NuPICPlotOutput
from nupic.swarming import permutations_runner

import generate_data



def swarm_over_data():
  permutations_runner.runPermutations(['search_def.json', '--maxWorkers=8', '--overwrite'])
  shutil.copyfile('model_0/model_params.py', 'model_params.py')



def run_sine_experiment():
  generate_data.run()
  swarm_over_data()
  import model_params
  output = NuPICPlotOutput('sine_output', show_anomaly_score=False)
  model = ModelFactory.create(model_params.MODEL_PARAMS)
  model.enableInference({'predictedField': 'sine'})
  
  with open('sine.csv', 'rb') as sine_input:
    csv_reader = csv.reader(sine_input)

    # skip header rows
    csv_reader.next()
    csv_reader.next()
    csv_reader.next()

    # the real data
    for row in csv_reader:
      angle = float(row[0])
      sine_value = float(row[1])
      result = model.run({'sine': sine_value})
      output.write(angle, sine_value, result, prediction_step=1)

  output.close()



if __name__ == "__main__":
  run_sine_experiment()
