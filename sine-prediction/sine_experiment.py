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
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic_output import NuPICFileOutput, NuPICPlotOutput
import sine_model_params

def run_sine_experiment():
  output = NuPICFileOutput('sine_output', show_anomaly_score=True)
  model = ModelFactory.create(sine_model_params.MODEL_PARAMS)
  model.enableInference({'predictedField': 'sine'})
  
  iteration = 0
  for i in range(100):
    angle = iteration
    sine_value = math.sin(math.radians(angle))
    modelInput = {'sine': sine_value}
    result = model.run(modelInput)
    if angle is 180:
      angle = 0

    output.write(angle, sine_value, result, prediction_step=1)
    iteration = iteration + 1


  output.close()

if __name__ == "__main__":
  run_sine_experiment()
