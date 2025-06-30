import os
import sys
import warnings
import platform

# Force OpenBLAS to use a single thread to prevent image-rotation
# test failures on macOS. See https://github.com/sunpy/sunpy/issues/4290
# for more information.
os.environ['OMP_NUM_THREADS'] = '1'

import sunpy

if platform.machine() in ('aarch64', 'ppc64le'):
    print('WARNING: Skipping most tests on aarch64/ppc64le because they take too long')
    sys.exit(sunpy.self_test(package="io"))

with warnings.catch_warnings() as cw:
    warnings.simplefilter("ignore", message="interpolating from IERS_Auto using predictive values that are more")
    sys.exit(sunpy.self_test())
