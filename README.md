# Solver4Newton

Particle solvers for Newton 1.7 and Warp 1.18. This repository provides the
existing PBF solver, its MuJoCo coupling, and reusable volume-map boundaries.
The parent checkout installs the `Solver` package alongside its applications.

`Solver.boundaries.volume_map.precompute_volume_map` takes a prepared
float32 CUDA SDF and a support radius in meters, and returns a Warp Volume
whose values are effective boundary volumes in cubic meters. The radius
defines the map's coverage and must match the solver's requested support.
The map uses geometry integration without baking in the SPH kernel.

`Solver.boundaries.runtime` provides grid queries and `BoundarySystem` for
sharing grids across static and rigid instances. Each prepared asset supplies
`sdf`, `volume_map`, `bounds_center`, `bounds_half` and `bounds_radius`.
Applications own resource resolution, files and scene assembly. Each SPH
solver owns how the boundary result enters its equations, including the
kernel, effective pressure distance and reaction forces. The PBF implementation
uses compile-time constants for a single solver configuration per process.

The initial snapshot came from `RoboSwimingPool` commit `b439ffa`, including
its existing PBF, coupling and volume-map implementations. The volume-map
quadrature follows [Bender et al. (2019)](https://animation.rwth-aachen.de/publication/0565/);
the existing SPlisHSPlasH reference is retained in the implementation.
The parent source's Apache-2.0 license is included in `LICENSE`.
