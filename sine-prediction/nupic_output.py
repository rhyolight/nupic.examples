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
from collections import deque
from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt
from nupic.data.inference_shifter import InferenceShifter


WINDOW = 360


class NuPICOutput(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def write(self, index, value, prediction_result):
    pass

  @abstractmethod
  def close(self):
    pass



class NuPICFileOutput(NuPICOutput):


  def __init__(self, name):
    self.file = open("%s.csv" % (name,), 'w')


  def write(self, index, value, prediction_result):
    prediction = prediction_result.inferences['multiStepBestPredictions'][1]
    self.file.write("%i,%f,%f\n" % (index, value, prediction))


  def close(self):
    self.file.close()



class NuPICPlotOutput(NuPICOutput):


  def __init__(self, name):
    # turn matplotlib interactive mode on (ion)
    plt.ion()
    self.fig = plt.figure()
    # plot title, legend, etc
    plt.title('Sine prediction example')
    plt.xlabel('angle (deg)')
    plt.ylabel('Sine (rad)')
    # The shifter will align prediction and actual values.
    self.shifter = InferenceShifter()
    # Keep the last WINDOW predicted and actual values for plotting.
    self.actual_history = deque([0.0] * WINDOW, maxlen=360)
    self.predicted_history = deque([0.0] * WINDOW, maxlen=360)
    # Initialize the plot lines that we will update with each new record.
    self.actual_line, = plt.plot(range(WINDOW), self.actual_history)
    self.predicted_line, = plt.plot(range(WINDOW), self.predicted_history)
    # Set the y-axis range.
    self.actual_line.axes.set_ylim(-1, 1)
    self.predicted_line.axes.set_ylim(-1, 1)


  def write(self, index, value, prediction_result):
    shifted_result = self.shifter.shift(prediction_result)
    # Update the trailing predicted and actual value deques.
    inference = shifted_result.inferences['multiStepBestPredictions'][1]
    if inference is not None:
      self.actual_history.append(shifted_result.rawInput['sine'])
      self.predicted_history.append(inference)

    # Redraw the chart with the new data.
    self.actual_line.set_ydata(self.actual_history)  # update the data
    self.predicted_line.set_ydata(self.predicted_history)  # update the data
    plt.draw()
    plt.legend( ('actual','predicted') )    



  def close(self):
    pass



NuPICOutput.register(NuPICFileOutput)
NuPICOutput.register(NuPICPlotOutput)