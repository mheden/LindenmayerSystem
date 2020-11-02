import math
import svgwrite
from lindenmayer import LindenmayerSystem


def output(filename, points):
    curves = []

    xmin, ymin = (math.inf, math.inf)
    xmax, ymax = (-math.inf, -math.inf)

    dwg = svgwrite.Drawing(filename, debug=False)
    for line in points:
        for x, y in line:
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)
        curves.append(
            dwg.polyline(points=line, stroke="black", fill="none", stroke_width=0.2)
        )

    dwg.viewbox(xmin, ymin, xmax - xmin, ymax - ymin)
    for curve in curves:
        dwg.add(curve)
    dwg.save()


def generate(filename, start, rules, iterations=10, step=5, startangle=0, angle=90):
    print("Creating %s..." % filename)
    config = {"start": start, "rules": rules}
    ls = LindenmayerSystem(config)
    ls.iterate(iterations)
    points = ls.get_points(step=step, startangle=startangle, angle=angle)
    output(filename, points)


if __name__ == "__main__":
    # sources:
    #
    # - https://en.wikipedia.org/wiki/L-system
    # - http://mathforum.org/advanced/robertd/lsys2d.html
    # - ...

    generate(
        "koch_curve.svg", start="F", rules={"F": "F+F--F+F"}, iterations=5, angle=60
    )

    generate(
        "koch_curve_variant.svg", start="F", rules={"F": "F+F-F-F+F"}, iterations=5
    )

    generate(
        "koch_snowflake.svg",
        start="F--F--F",
        rules={"F": "F+F--F+F"},
        iterations=5,
        angle=60,
    )

    generate(
        "sierpinski_triangle.svg",
        start="F-G-G",
        rules={"F": "F-G+F+G-F", "G": "GG"},
        iterations=8,
        startangle=180,
        angle=120,
    )

    generate(
        "sierpinski_triangle_arrowhead.svg",
        start="A",
        rules={"A": "B-A-B", "B": "A+B+A"},
        iterations=8,
        angle=60,
    )

    generate(
        "dragon_curve.svg",
        start="FX",
        rules={"X": "X+YF+", "Y": "-FX-Y"},
        iterations=12,
    )

    generate(
        "plant.svg",
        start="X",
        rules={"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"},
        iterations=8,
        startangle=-65,
        angle=25,
    )

    generate(
        "hilbert_curve.svg",
        start="X",
        rules={"X": "-YF+XFX+FY-", "Y": "+XF-YFY-FX+"},
        iterations=8,
    )

    generate(
        "peano_curve.svg",
        start="F",
        rules={"F": "F+F-F-F-F+F+F+F-F"},
        iterations=4,
        startangle=45,
    )

    generate(
        "quadratic_koch_island.svg",
        start="F+F+F+F",
        rules={"F": "F-F+F+FFF-F-F+F"},
        iterations=3,
    )

    generate(
        "32_segment_curve.svg",
        start="F+F+F+F",
        rules={"F": "-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"},
        iterations=2,
    )

    generate(
        "peano_gosper_curve.svg",
        start="FX",
        rules={"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"},
        iterations=4,
        angle=60,
    )

    generate(
        "square_curve.svg",
        start="F+XF+F+XF",
        rules={"X": "XF-F+F-XF+F+XF-F+F-X"},
        iterations=4,
    )

    generate(
        "hilbert_curve_2.svg",
        start="X",
        rules={"X": "XFYFX+F+YFXFY-F-XFYFX", "Y": "YFXFY-F-XFYFX+F+YFXFY"},
        iterations=3,
    )
