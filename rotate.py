#!/usr/bin/env python

import numpy as np
from obspy.core import Trace, Stream


def rotateZaxis(e, n, z, rot_angle_n, rot_angle_e):
    '''
    Python function to rotate data about vertical component about horizontal
    axes. First rotate about east, followed by north.
    '''

    # Get traces
    e_data = np.array(e[0].data, dtype='float64')
    n_data = np.array(n[0].data, dtype='float64')
    z_data = np.array(z[0].data, dtype='float64')

    # Rotate about east
    z_rot_1 = ((np.cos(np.arctan2(n_data, z_data) + np.deg2rad(rot_angle_n))) *
               np.sqrt(z_data**2 + n_data**2))

    # Rotate about north
    z_rot_2 = ((np.cos(np.arctan2(e_data, z_rot_1) + np.deg2rad(rot_angle_e))) *
               np.sqrt(z_rot_1**2 + e_data**2))

    # Get rotated vertical component back into obspy stream object
    Tr = Trace(data=z_rot_2, header=z[0].stats)
    Z_rot = Stream(traces=[Tr])

    return Z_rot
