 #
 # QTop
 #
 # Copyright (c) 2016 Jacob Marks (jacob.marks@yale.edu)
 #
 # This file is part of QTop.
 #
 # QTop is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

from common import *
from surface_codes import *
from color_codes import *
from error_models import *
from decoders import mwpm
from visualization import *
from threshold import *
from simulation import *

################## Surface Code Simulation ##################


# model = CodeCapacity()
model = Depolarizing()
decoder = mwpm.MWPM_decoder()
sim = simulation(2, 'Surface Code', [model, 'Depolarizing Channel'], [decoder, 'MWPM'], './')
L_vals = [7,9]
p_vals = np.linspace(.13,.18,10)
num_trials = 3000
run(sim, L_vals, p_vals, num_trials)

