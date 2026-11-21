# Solver4Newton

Particle solvers and reusable volume-map boundaries for Newton 1.7 and Warp
1.18. The current implementation includes a position-based fluids (PBF)
solver and coupled stepping with Newton's MuJoCo rigid-body solver.

## Use in Robot Lab

The [RoboLab](https://github.com/Ekubooo/Robot_Lab) integration repository checks out this submodule
at `Robot_Lab/Solver` and installs it as the `Solver` package. Follow the parent
README to set up the environment and launch a coupled scene. The parent owns
the scene configuration and the files used to assemble it.

## Volume-map boundaries

`Solver.boundaries.volume_map.precompute_volume_map` takes a prepared float32
CUDA SDF and a support radius in meters. It returns a Warp Volume containing
effective boundary volumes in cubic meters. The radius determines the map's
coverage and must match the solver's requested support. Geometry integration
produces the map without baking in an SPH kernel.

`Solver.boundaries.runtime` provides grid queries and `BoundarySystem` for
sharing grids among static and rigid instances. Each prepared asset supplies
`sdf`, `volume_map`, `bounds_center`, `bounds_half`, and `bounds_radius`.
Applications resolve and load resources and assemble scenes. Each SPH solver
chooses how to use the boundary result in its equations, including the kernel,
effective pressure distance, and reaction force. The PBF implementation uses
compile-time constants for a single solver configuration per process.

## Source and license

The initial snapshot came from [Robot Lab commit `b439ffa`](https://github.com/Ekubooo/Robot_Lab/tree/b439ffa7d50157476301152bc8e54d815a032f70),
including its PBF, coupling, and volume-map implementations. Volume-map
quadrature follows [Bender et al. (2019)](https://animation.rwth-aachen.de/publication/0565/).
The [implementation](boundaries/volume_map.py) documents the SPlisHSPlasH
reference. The parent repository's [Apache License 2.0](LICENSE) and original
copyright notice are included.
