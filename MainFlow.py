import numpy as np
import segyio

with segyio.open('F:/SeismicData/U121_01.SGY') as f:
    for trace in f.trace:
        filtered = trace[np.where(trace < 1e-2)]