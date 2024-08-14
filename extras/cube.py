#!/usr/bin/env python3

from parent_folder import svg3d
import pyrr
import numpy as np
import svgwrite.utils

from math import *

sign = np.sign
create_ortho = pyrr.matrix44.create_orthogonal_projection
create_perspective = pyrr.matrix44.create_perspective_projection
create_lookat = pyrr.matrix44.create_look_at

def cube():
    return np.float32(
        [
            [(-10, +10, -10), (+10, +10, -10), (+10, -10, -10), (-10, -10, -10)],
            [(-10, +10, +10), (+10, +10, +10), (+10, -10, +10), (-10, -10, +10)],
            [(-10, -10, +10), (+10, -10, +10), (+10, -10, -10), (-10, -10, -10)],
            [(-10, +10, +10), (+10, +10, +10), (+10, +10, -10), (-10, +10, -10)],
            [(-10, -10, +10), (-10, +10, +10), (-10, +10, -10), (-10, -10, -10)],
            [(+10, -10, +10), (+10, +10, +10), (+10, +10, -10), (+10, -10, -10)],
        ]
    )

def create_complex_shapes():
    # Filmstrip

    def shader(face_index, winding):
        return dict(
            fill="white",
            fill_opacity="0.75",
            stroke="green",
            stroke_linejoin="round",
            stroke_width="0.05",
        )

    
    view = create_lookat(eye=[50, 40, 120], target=[0, 0, 0], up=[0, 1, 0])
    projection = create_perspective(fovy=15, aspect=1, near=10, far=200)
    camera = svg3d.Camera(view, projection)

    viewport0 = svg3d.Viewport.from_string("-2.5 -0.5 1.0 1.0")

    # cube
    view0 = svg3d.View(camera, svg3d.Scene([svg3d.Mesh(cube(), shader)]), viewport0)

    drawing = svgwrite.Drawing(
        "cube.svg", (256, 256), viewBox="-2.5 -0.5 1.0 1.0"
    )
    svg3d.Engine([view0]).render_to_drawing(drawing)
    print("saved")
    drawing.save()

def main():
    create_complex_shapes()
main()

