import os
import sys
import platform

# Force OpenBLAS to use a single thread to prevent image-rotation
# test failures on macOS. See https://github.com/sunpy/sunpy/issues/4290
# for more information.
os.environ['OMP_NUM_THREADS'] = '1'

import sunpy

# Bypass any issues with the older IERS data
from astropy.utils.iers import conf
conf.auto_max_age = None

if platform.machine() in ('aarch64', 'ppc64le'):
    print('WARNING: Skipping tests on aarch64/ppc64le because they take too long')
    sys.exit()

sys.exit(sunpy.self_test())
