# How to Predict Sine Waves with NuPIC

## Script for Screencast

1. Show nupic imported in repl
1. Generate a CSV file with sine data records
1. Run a *swarm* over the input data
  - Follow the [Running Swarms](https://github.com/numenta/nupic/wiki/Running-Swarms) wiki page
  - Test database
  - Create a search definition for the swarm based on [`examples/swarm/simple/search_def.json`](https://github.com/numenta/nupic/blob/master/examples/swarm/simple/search_def.json)
  - Run the swarm from command line
1. Run NuPIC
  - Run OpfRunExperiment manually
  - Inspect output data in spreadsheet
1. Automate swarm
1. Automate NuPIC run after swarm
