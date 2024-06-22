import numpy as np
from dataclasses import dataclass

@dataclass
class Cubie():
    tag: str
    type: str
    home_cubicle: str
    current_cubicle: str
    current_face1_points: dict | None
    current_face2_points: dict | None
    current_face3_points: dict | None
    ideal_face1_points: dict | None
    ideal_face2_points: dict | None
    ideal_face3_points: dict | None



def get_corner_cubies_8(off):
    ## UBL Cubie
    ubl = Cubie("UBL", "corner", "ubl", "ubl", None, None, None, None, None, None)
    ubl.current_face1_points = {"points": np.array([[0, 2, 2], [1-off, 2, 2], [0, 1+off, 2], [1-off, 1+off, 2]]), "color": "white"}
    ubl.current_face2_points = {"points": np.array([[0, 2, 2], [1-off, 2, 2], [0, 2, 1+off], [1-off, 2, 1+off]]), "color": "orange"}
    ubl.current_face3_points = {"points": np.array([[0, 2, 2], [0, 1+off, 2], [0, 2, 1+off], [0, 1+off, 1+off]]), "color": "green"}
    ubl.ideal_face1_points = {"points": np.array([[0, 2, 2], [1-off, 2, 2], [0, 1+off, 2], [1-off, 1+off, 2]]), "color": "white"}
    ubl.ideal_face2_points = {"points": np.array([[0, 2, 2], [1-off, 2, 2], [0, 2, 1+off], [1-off, 2, 1+off]]), "color": "orange"}
    ubl.ideal_face3_points = {"points": np.array([[0, 2, 2], [0, 1+off, 2], [0, 2, 1+off], [0, 1+off, 1+off]]), "color": "green"}

    ## UFL Cubie
    ufl = Cubie("UFL", "corner", "ufl", "ufl",
                {"points": np.array([[0, 0, 2], [1-off, 0, 2], [0, 1-off, 2], [1-off, 1-off, 2]]), "color": "white"},
                {"points": np.array([[0, 0, 2], [1-off, 0, 2], [0, 0, 1+off], [1-off, 0, 1+off]]), "color": "red"},
                {"points": np.array([[0, 0, 2], [0, 1-off, 2], [0, 0, 1+off], [0, 1-off, 1+off]]), "color": "green"},
                {"points": np.array([[0, 0, 2], [1 - off, 0, 2], [0, 1 - off, 2], [1 - off, 1 - off, 2]]),
                 "color": "white"},
                {"points": np.array([[0, 0, 2], [1 - off, 0, 2], [0, 0, 2 + off], [1-off, 0, 2 + off]]), "color": "red"},
                {"points": np.array([[0, 0, 2], [0, 1 - off, 2], [0, 0, 2 + off], [0, 1 - off, 2 + off]]),
                 "color": "green"})

    ## UFR Cubie
    ufr = Cubie("UFR", "corner", "ufr", "ufr",
                {"points": np.array([[2, 0, 2], [1+off, 0, 2], [2, 1-off, 2], [1+off, 1-off, 2]]), "color": "white"},
                {"points": np.array([[2, 0, 2], [1+off, 0, 2], [2, 0, 1+off], [1+off, 0, 1+off]]), "color": "red"},
                {"points": np.array([[2, 0, 2], [2, 0, 1+off], [2, 1-off, 2], [2, 1-off, 1+off]]), "color": "blue"},
                {"points": np.array([[2, 0, 2], [2 + off, 0, 2], [2, 1 - off, 2], [1+off, 1 - off, 2]]), "color": "white"},
                {"points": np.array([[2, 0, 2], [2 + off, 0, 2], [2, 0, 2 + off], [1+off, 0, 2 + off]]), "color": "red"},
                {"points": np.array([[2, 0, 2], [2, 0, 2 + off], [2, 1 - off, 2], [2, 1 - off, 2 + off]]),
                 "color": "blue"})

    ## URB Cubie
    urb = Cubie("URB", "corner", "urb", "urb",
                {"points": np.array([[2, 2, 2], [2, 1+off, 2], [1+off, 2, 2], [1+off, 1+off, 2]]), "color": "white"},
                {"points": np.array([[2, 2, 2], [2, 1+off, 2], [2, 2, 1+off], [2, 1+off, 1+off]]), "color": "blue"},
                {"points": np.array([[2, 2, 2], [2, 2, 1+off], [1+off, 2, 2], [1+off, 2, 1+off]]), "color": "orange"},
                {"points": np.array([[2, 2, 2], [2, 2 + off, 2], [2 + off, 2, 2], [2 + off, 2 + off, 2]]),
                 "color": "white"},
                {"points": np.array([[2, 2, 2], [2, 2 + off, 2], [2, 2, 2 + off], [2, 2 + off, 2 + off]]),
                 "color": "blue"},
                {"points": np.array([[2, 2, 2], [2, 2, 2 + off], [2 + off, 2, 2], [2 + off, 2, 2 + off]]),
                 "color": "orange"})

    ## DBL Cubie
    dbl = Cubie("DBL", "corner", "dbl", "dbl",
                {"points": np.array([[0, 2, 0], [1-off, 2, 0], [0, 1+off, 0], [1-off, 1+off, 0]]), "color": "yellow"},
                {"points": np.array([[0, 2, 0], [1-off, 2, 0], [0, 2, 1-off], [1-off, 2, 1-off]]), "color": "orange"},
                {"points": np.array([[0, 2, 0], [0, 2, 1-off], [0, 1+off, 0], [0, 1+off, 1-off]]), "color": "green"},
                {"points": np.array([[0, 2, 0], [1 - off, 2, 0], [0, 2 + off, 0], [1 - off, 2 + off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[0, 2, 0], [1 - off, 2, 0], [0, 2, 1 - off], [1 - off, 2, 1 - off]]),
                 "color": "orange"},
                {"points": np.array([[0, 2, 0], [0, 2, 1 - off], [0, 2 + off, 0], [0, 2 + off, 1 - off]]),
                 "color": "green"})

    ## DFL Cubie
    dfl = Cubie("DFL", "corner", "dfl", "dfl",
                {"points": np.array([[0, 0, 0], [1-off, 0, 0], [0, 1-off, 0], [1-off, 1-off, 0]]), "color": "yellow"},
                {"points": np.array([[0, 0, 0], [1-off, 0, 0], [0, 0, 1-off], [1-off, 0, 1-off]]), "color": "red"},
                {"points": np.array([[0, 0, 0], [0, 1-off, 0], [0, 0, 1-off], [0, 1-off, 1-off]]), "color": "green"},
                {"points": np.array([[0, 0, 0], [1 - off, 0, 0], [0, 1 - off, 0], [1 - off, 1 - off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[0, 0, 0], [1 - off, 0, 0], [0, 0, 1 - off], [1 - off, 0, 1 - off]]),
                 "color": "red"},
                {"points": np.array([[0, 0, 0], [0, 1 - off, 0], [0, 0, 1 - off], [0, 1 - off, 1 - off]]),
                 "color": "green"})

    ## DFR Cubie
    dfr = Cubie("DFR", "corner", "dfr", "dfr",
                {"points": np.array([[2, 0, 0], [1+off, 0, 0], [2, 1-off, 0], [1+off, 1-off, 0]]), "color": "yellow"},
                {"points": np.array([[2, 0, 0], [1+off, 0, 0], [2, 0, 1-off], [1+off, 0, 1-off]]), "color": "red"},
                {"points": np.array([[2, 0, 0], [2, 0, 1-off], [2, 1-off, 0], [2, 1-off, 1-off]]), "color": "blue"},
                {"points": np.array([[2, 0, 0], [2 + off, 0, 0], [2, 1 - off, 0], [2 + off, 1 - off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[2, 0, 0], [2 + off, 0, 0], [2, 0, 1 - off], [2 + off, 0, 1 - off]]),
                 "color": "red"},
                {"points": np.array([[2, 0, 0], [2, 0, 1 - off], [2, 1 - off, 0], [2, 1 - off, 1 - off]]),
                 "color": "blue"})

    ## DRB Cubie
    drb = Cubie("DRB", "corner", "drb", "drb",
                {"points": np.array([[2, 2, 0], [2, 1+off, 0], [1+off, 2, 0], [1+off, 1+off, 0]]), "color": "yellow"},
                {"points": np.array([[2, 2, 0], [2, 1+off, 0], [2, 2, 1-off], [2, 1+off, 1-off]]), "color": "blue"},
                {"points": np.array([[2, 2, 0], [2, 2, 1-off], [1+off, 2, 0], [1+off, 2, 1-off]]), "color": "orange"},
                {"points": np.array([[2, 2, 0], [2, 2 + off, 0], [2 + off, 2, 0], [2 + off, 2 + off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[2, 2, 0], [2, 2 + off, 0], [2, 2, 1 - off], [2, 2 + off, 1-off]]), "color": "blue"},
                {"points": np.array([[2, 2, 0], [2, 2, 1 - off], [2 + off, 2, 0], [2 + off, 2, 1-off]]), "color": "orange"})
    corner_cubies = [ubl, ufl, ufr, urb, dbl, dfl, dfr, drb]
    return corner_cubies

