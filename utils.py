import numpy as np
from dataclasses import dataclass


@dataclass
class RotationAxis():
    tag: str
    a: float
    b: float
    c: float
    px: float
    py: float
    pz: float


def trans_mat_rotation_axis_angle(RotAxis, theta_deg):
    a = RotAxis.a
    b = RotAxis.b
    c = RotAxis.c
    px = RotAxis.px
    py = RotAxis.py
    pz = RotAxis.pz
    phi = np.radians(theta_deg)
    r11 = (a*a) + (((b*b) + (c*c))*np.cos(phi))
    r12 = a * b * (1 - np.cos(phi)) - (c * np.sin(phi))
    r13 = a * c * (1 - np.cos(phi)) + (b * np.sin(phi))
    r21 = a * b * (1 - np.cos(phi)) + (c * np.sin(phi))
    r22 = (b*b) + (((a*a) + (c*c))*np.cos(phi))
    r23 = b * c * (1 - np.cos(phi)) - (a * np.sin(phi))
    r31 = a * c * (1 - np.cos(phi)) - (b * np.sin(phi))
    r32 = b * c * (1 - np.cos(phi)) + (a * np.sin(phi))
    r33 = (c*c) + (((a*a) + (b*b))*np.cos(phi))
    tx1 = ((px * ((b*b) + (c*c))) - (a * ((py*b) + (pz*c)))) * (1 - np.cos(phi))
    tx2 = ((py*c) - (pz*b)) * np.sin(phi)
    ty1 = ((py * ((a*a) + (c*c))) - (b * ((pz*c) + (px*a)))) * (1 - np.cos(phi))
    ty2 = ((pz*a) - (px*c)) * np.sin(phi)
    tz1 = ((pz * ((a*a) + (b*b))) - (c * ((px*a) + (py*b)))) * (1 - np.cos(phi))
    tz2 = ((px*b) - (py*a)) * np.sin(phi)
    tx = tx1 + tx2
    ty = ty1 + ty2
    tz = tz1 + tz2
    trans_mat = np.asarray([[r11, r12, r13, tx],
                            [r21, r22, r23, ty],
                            [r31, r32, r33, tz],
                            [0, 0, 0, 1]])
    return trans_mat


def rotationAxisAngle_mat_m2(RotAxis, theta_deg):
    a = RotAxis.a
    b = RotAxis.b
    c = RotAxis.c
    px = RotAxis.px
    py = RotAxis.py
    pz = RotAxis.pz
    phi = np.radians(theta_deg)
    t1_mat = np.asarray([[1, 0, 0, -px], [0, 1, 0, -py], [0, 0, 1, -pz], [0, 0, 0, 1]])
    t2_mat = np.asarray([[1, 0, 0, px], [0, 1, 0, py], [0, 0, 1, pz], [0, 0, 0, 1]])
    rm_r11 = (a * a) + ((1 - (a * a)) * np.cos(phi))
    rm_r12 = (a * b * (1 - np.cos(phi))) - (c * np.sin(phi))
    rm_r13 = (a * c * (1 - np.cos(phi))) + (b * np.sin(phi))

    rm_r21 = (a * b * (1 - np.cos(phi))) + (c * np.sin(phi))
    rm_r22 = (b * b) + ((1 - (b * b)) * np.cos(phi))
    rm_r23 = (b * c * (1 - np.cos(phi))) - (a * np.sin(phi))

    rm_r31 = (a * c * (1 - np.cos(phi))) - (b * np.sin(phi))
    rm_r32 = (b * c * (1 - np.cos(phi))) + (a * np.sin(phi))
    rm_r33 = (c * c) + ((1 - (c * c)) * np.cos(phi))
    rot_mat = np.asarray([[rm_r11, rm_r12, rm_r13, 0],
                          [rm_r21, rm_r22, rm_r23, 0],
                          [rm_r31, rm_r32, rm_r33, 0],
                          [0, 0, 0, 1]])
    trans_mat1 = np.matmul(rot_mat, t1_mat)
    trans_mat = np.matmul(t2_mat, trans_mat1)
    return trans_mat

