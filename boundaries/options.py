"""Geometry integration settings shared by generation and asset validation."""

import math
from numbers import Integral


VOLUME_MAP_ALGORITHM_VERSION = 1


def check_volume_options(support_radius, quadrature_points):
    if not math.isfinite(support_radius) or support_radius <= 0:
        raise ValueError("support_radius must be finite and positive")
    if isinstance(quadrature_points, bool) or not isinstance(quadrature_points, Integral) or quadrature_points < 1:
        raise ValueError("quadrature_points must be a positive integer")
