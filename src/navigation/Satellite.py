#! usr/bin/env python
# Import native modules
import numpy as np

# Satellite class


class Satellite:
    def __init__(self, width, length, r0_target_center, r0_target_radius):
        # Initialize satellite
        self._width = width                                     # Width of satellite
        self._length = length                                   # Length of satellite
        self._r0_target_center = np.array(r0_target_center)     # Vector from centroid to center of target (in satellite body frame)
        self._r0_target_radius = np.array(r0_target_radius)     # Vector from centroid to outer edge of target circle (in satellite body frame)
        self.r_l = np.array([1,0,0])                            # Radial vector pointing from centroid to target center
        self.r_t = np.array([0,1,0])                            # Transverse vector normal to radial vector


    @property
    def psi(self):
        # Calculate angle between target radius vector and radial unit vector
        self._r0_target_radius_hat = self._r0_target_radius / np.linalg.norm(r0_target_radius)
        self._psi = np.arccos(np.dot(self._r0_target_radius_hat, self.r_l)) * 180/np.pi
        return self._psi

    def check_alignment(self, tol = 1e-5):
        # Check to see if r_l = r0_target_radius_hat
        return self.psi < tol
