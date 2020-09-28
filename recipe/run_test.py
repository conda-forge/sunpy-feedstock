import os
import sys

# Force OpenBLAS to use a single thread to prevent image-rotation
# test failures on macOS. See https://github.com/sunpy/sunpy/issues/4290
# for more information.
os.environ['OMP_NUM_THREADS'] = '1'

import sunpy
import numpy as np

print(os.environ['OMP_NUM_THREADS'])

sys.exit(sunpy.self_test())