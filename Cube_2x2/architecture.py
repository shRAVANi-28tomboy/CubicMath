import numpy as np
from develop2x2 import get_corner_cubies_8
from utils import RotationAxis, trans_mat_rotation_axis_angle
import plotly.graph_objects as go


class RubiksCube2x2():
    def __init__(self):
        self.cube = get_corner_cubies_8(0.01)
        self.front_axis = RotationAxis("front", 0, -1, 0, 1, 1, 1)  # neg y axis
        self.back_axis = RotationAxis("back", 0, 1, 0, 1, 1, 1)  # pos y axis
        self.left_axis = RotationAxis("left",  -1, 0, 0, 1, 1, 1)  # neg x axis
        self.right_axis = RotationAxis("right",  1, 0, 0, 1, 1, 1)  # pos x axis
        self.down_axis = RotationAxis("down",  0, 0, -1, 1, 1, 1)  # neg z axis
        self.up_axis = RotationAxis("up",  0, 0, 1, 1, 1, 1)  # pos z axis

    @staticmethod
    def transform_face_points(trans_mat_4x4, face_points_4x3):
        points_t = np.transpose(face_points_4x3)
        homo_pts = np.vstack((points_t, [1, 1, 1, 1]))
        trans_homo_pts = np.matmul(trans_mat_4x4, homo_pts)
        trans_homo_pts = trans_homo_pts[0:3, :]
        trans_pts_4x3 = np.transpose(trans_homo_pts)
        return trans_pts_4x3
        pass

    def perform_axis_move(self, angle1, rot_axis):
        angle = -1 * angle1
        abs_d = ((rot_axis.a * rot_axis.px) +
                 (rot_axis.b * rot_axis.py) +
                 (rot_axis.c * rot_axis.pz))
        trans_mat_f = trans_mat_rotation_axis_angle(rot_axis, angle)
        cubies_of_interest = []
        for cubie in self.cube:
            # taking any one point of cubicle
            p_o_i = cubie.current_face1_points["points"][0]
            value = ((rot_axis.a * p_o_i[0]) +
                     (rot_axis.b * p_o_i[1]) +
                     (rot_axis.c * p_o_i[2]) - abs_d)
            if value > 0:
                cubies_of_interest.append(cubie)
                # break

        for cubie_oi in cubies_of_interest:
            cubie_oi.current_face1_points["points"] = (
                self.transform_face_points(trans_mat_f, cubie_oi.current_face1_points["points"]))
            cubie_oi.current_face2_points["points"] = (
                self.transform_face_points(trans_mat_f, cubie_oi.current_face2_points["points"]))
            cubie_oi.current_face3_points["points"] = (
                self.transform_face_points(trans_mat_f, cubie_oi.current_face3_points["points"]))

        pass

    def perform_front_move(self, angle1):
        self.perform_axis_move(angle1, self.front_axis)

    def perform_back_move(self, angle1):
        self.perform_axis_move(angle1, self.back_axis)

    def perform_left_move(self, angle1):
        self.perform_axis_move(angle1, self.left_axis)

    def perform_right_move(self, angle1):
        self.perform_axis_move(angle1, self.right_axis)

    def perform_down_move(self, angle1):
        self.perform_axis_move(angle1, self.down_axis)

    def perform_up_move(self, angle1):
        self.perform_axis_move(angle1, self.up_axis)

    @staticmethod
    def bias_plotly_transformation(points):
        ## this process is solely for display purpose because Mesh3d doesn't
        # display planes that are perpendicular to XY plane
        transformed_points = []
        deg = 10
        T1_mat = np.asarray([[1, 0, 0, 0],
                             [0, np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0],
                             [0, -np.sin(np.radians(deg)), np.cos(np.radians(deg)), 0],
                             [0, 0, 0, 1]])
        T2_mat = np.asarray([[np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0, 0],
                             [-np.sin(np.radians(deg)), np.cos(np.radians(deg)), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        T_mat = np.matmul(T1_mat, T2_mat)
        for point in points:
            point1 = np.asarray([[point[0]], [point[1]], [point[2]], [1]])
            trans_point1 = np.matmul(T_mat, point1)
            trans_point = np.transpose(trans_point1)
            transformed_points.append(trans_point[0])
        return np.asarray(transformed_points)

    def get_cubie_trace(self, cubie):
        size1 = 10
        mode1 = 'lines+markers'
        tag = cubie.tag
        traces = []
        points_traces = []
        if cubie.current_face1_points is not None:
            color1 = cubie.current_face1_points["color"]
            points1 = cubie.current_face1_points["points"]
            points = self.bias_plotly_transformation(points1)
            x = points[:, 0]
            y = points[:, 1]
            z = points[:, 2]
            trace1 = go.Mesh3d(x=x, y=y, z=z, color=color1, name=tag)
            traces.append(trace1)

            pts_trace1 = go.Scatter3d(x=x, y=y, z=z, mode=mode1,
                                   marker=dict(size=size1, color=color1), name=tag)
            points_traces.append(pts_trace1)
        if cubie.current_face2_points is not None:
            color1 = cubie.current_face2_points["color"]
            points1 = cubie.current_face2_points["points"]
            points = self.bias_plotly_transformation(points1)
            x = points[:, 0]
            y = points[:, 1]
            z = points[:, 2]
            trace2 = go.Mesh3d(x=x, y=y, z=z, color=color1, name=tag)
            traces.append(trace2)
            pts_trace2 = go.Scatter3d(x=x, y=y, z=z, mode=mode1,
                                      marker=dict(size=size1, color=color1), name=tag)
            points_traces.append(pts_trace2)
        if cubie.current_face3_points is not None:
            color1 = cubie.current_face3_points["color"]
            points1 = cubie.current_face3_points["points"]
            points = self.bias_plotly_transformation(points1)
            x = points[:, 0]
            y = points[:, 1]
            z = points[:, 2]
            trace3 = go.Mesh3d(x=x, y=y, z=z, color=color1, name=tag)
            traces.append(trace3)
            pts_trace3 = go.Scatter3d(x=x, y=y, z=z, mode=mode1,
                                      marker=dict(size=size1, color=color1), name=tag)
            points_traces.append(pts_trace3)
        return traces, points_traces

    def display_cube(self):
        fig = go.Figure(layout={"height": 960/2, "margin": dict(l=2, r=2, b=2, t=2, pad=0),
                                        "paper_bgcolor": "LightslateGray", "width": 1280/2})

        for cubie_x in self.cube:
            mesh_trace_list, points_trace_list = self.get_cubie_trace(cubie_x)
            # for trace_x in points_trace_list:
            #     fig.add_trace(trace_x)
            for trace_y in mesh_trace_list:
                fig.add_trace(trace_y)
        fig.update_yaxes(
            scaleanchor="x",
            scaleratio=1,
        )
        camera = dict(
            eye=dict(x=-2, y=-2, z=2)
        )
        fig.update_layout(scene_camera=camera, title='cube 3x3')
        fig.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            )
        )
        # fig.show()
        return fig


test_cube = RubiksCube2x2()
ideal_cube = test_cube.cube
# test_cube.perform_front_move(30)
# test_cube.perform_back_move(30)
# test_cube.perform_left_move(30)
# test_cube.perform_right_move(30)
# test_cube.perform_down_move(30)
test_cube.perform_up_move(30)
fig = test_cube.display_cube()
fig.show()