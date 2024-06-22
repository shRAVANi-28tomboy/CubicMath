import numpy as np
from cubies_26_offset import get_corner_cubies_8, get_edge_cubies_12, get_center_cubies_6
import random
import plotly.graph_objects as go


class RubiksCube3x3():

    def __init__(self):
        self.cube = self.construct_ideal_cube()  ## list of 26 cubie class objects
        #next version make it a dict of cubies
        self.face_centers_dict = self.compute_n_set_face_centers()
        self.initial_state = 0 # for ideal cube
        self.track_moves = False
        self.move_sequences = []
        self.cubies_moves = {'UBL': [], 'UFL': [], 'UFR': [], 'URB': [],
                             'DBL': [], 'DFL': [], 'DFR': [], 'DRB': [],
                             'UL': [], 'UF': [], 'UR': [], 'UB': [],
                             'BL': [], 'LF': [], 'FR': [], 'RB': [],
                             'DL': [], 'DF': [], 'DR': [], 'DB': [],
                             'U': [], 'D': [], 'F': [], 'B': [], 'L': [], 'R': []}
        # self.initial_state = -1 #for scrambled/unrestored cube

    def scramble_ideal_cube(self):
        operations_count_list = list(np.linspace(31, 50, 20, endpoint=True))
        operations_list = list(np.linspace(1, 12, 12, endpoint=True))
        op_count = int(random.choice(operations_count_list))
        operations_sequence = ''
        for i in range(0, op_count):
            operation_number = int(random.choice(operations_list))
            if operation_number == 1:
                self.rotate_layer('u', -90)
                operations_sequence = operations_sequence + 'u '
            elif operation_number == 2:
                self.rotate_layer('d', -90)
                operations_sequence = operations_sequence + 'd '
            elif operation_number == 3:
                self.rotate_layer('f', -90)
                operations_sequence = operations_sequence + 'f '
            elif operation_number == 4:
                self.rotate_layer('b', -90)
                operations_sequence = operations_sequence + 'b '
            elif operation_number == 5:
                self.rotate_layer('l', -90)
                operations_sequence = operations_sequence + 'l '
            elif operation_number == 6:
                self.rotate_layer('r', -90)
                operations_sequence = operations_sequence + 'r '
            elif operation_number == 7:
                self.rotate_layer('u', 90)
                operations_sequence = operations_sequence + 'u1 '
            elif operation_number == 8:
                self.rotate_layer('d', 90)
                operations_sequence = operations_sequence + 'd1 '
            elif operation_number == 9:
                self.rotate_layer('f', 90)
                operations_sequence = operations_sequence + 'f1 '
            elif operation_number == 10:
                self.rotate_layer('b', 90)
                operations_sequence = operations_sequence + 'b1 '
            elif operation_number == 11:
                self.rotate_layer('l', 90)
                operations_sequence = operations_sequence + 'l1 '
            elif operation_number == 12:
                self.rotate_layer('r', 90)
                operations_sequence = operations_sequence + 'r1 '
        return operations_sequence

    def compute_n_set_face_centers(self):
        face_centers_dict = {}
        for cubie in self.cube:
            if cubie.type == "center":
                points_plane = cubie.current_face1_points["points"]
                axis_normal, axis_point = self.get_axis_of_rotation(points_plane)
                face_centers_dict.update({cubie.home_cubicle: {"face_normal": axis_normal, "face_center": axis_point}})
        return face_centers_dict

    @staticmethod
    def construct_ideal_cube():
        # corners = get_corner_cubies_8()
        # edges = get_edge_cubies_12()
        corners = get_corner_cubies_8(0.02)
        edges = get_edge_cubies_12(0.02)
        centers = get_center_cubies_6()
        cube = corners + edges + centers
        return cube

    @staticmethod
    def compute_face_center(face_points):
        sum_x, sum_y, sum_z = 0, 0, 0
        for point in face_points:
            sum_x = sum_x + point[0]
            sum_y = sum_y + point[1]
            sum_z = sum_z + point[2]
        x = sum_x/len(face_points)
        y = sum_y/len(face_points)
        z = sum_z/len(face_points)
        return np.asarray([x, y, z])

    def get_axis_of_rotation(self, face_points):
        face_center = self.compute_face_center(face_points)
        # (p2-p1)x(p3-p1)
        p1 = face_points[0]
        p2 = face_points[1]
        p3 = face_points[2]
        p21 = p2-p1
        p31 = p3-p1
        face_normal = np.cross(p21, p31)
        norm = np.linalg.norm(face_normal)
        unit_normal = face_normal/norm
        return unit_normal, face_center

    @staticmethod
    def get_rotation_mat(unit_vec, theta):
        ux = unit_vec[0]
        uy = unit_vec[1]
        uz = unit_vec[2]
        r11 = np.cos(theta) + (ux * ux * (1 - np.cos(theta)))
        r12 = (ux * uy * (1 - np.cos(theta))) - (uz * np.sin(theta))
        r13 = (ux * uz * (1 - np.cos(theta))) + (uy * np.sin(theta))
        r21 = (ux * uy * (1 - np.cos(theta))) + (uz * np.sin(theta))
        r22 = np.cos(theta) + (uy * uy * (1 - np.cos(theta)))
        r23 = (uy * uz * (1 - np.cos(theta))) - (ux * np.sin(theta))
        r31 = (ux * uz * (1 - np.cos(theta))) - (uy * np.sin(theta))
        r32 = (uy * uz * (1 - np.cos(theta))) + (ux * np.sin(theta))
        r33 = np.cos(theta) + (uz * uz * (1 - np.cos(theta)))
        rot_mat_4x4 = np.asarray([[r11, r12, r13, 0], [r21, r22, r23, 0], [r31, r32, r33, 0], [0, 0, 0, 1]])
        return rot_mat_4x4

    def get_transformation_matrix(self, line_normal, line_point, thetha_deg):
        theta = np.radians(thetha_deg)
        T1 = np.asarray([[1, 0, 0, line_point[0]], [0, 1, 0, line_point[1]],
                         [0, 0, 1, line_point[2]], [0, 0, 0, 1]])
        T1_inv = np.linalg.inv(T1)
        T2 = self.get_rotation_mat(line_normal, theta)
        trans_mat = np.linalg.multi_dot((T1, T2, T1_inv))
        return trans_mat

    @staticmethod
    def transform_face(face_points, trans_matrix):
        trans_face_points = []
        for point in face_points:
            point_transpose = np.asarray([[point[0]], [point[1]], [point[2]], [1]])
            trnsfm_pt_transpose = np.matmul(trans_matrix, point_transpose)
            trans_face_points.append([trnsfm_pt_transpose[0][0], trnsfm_pt_transpose[1][0], trnsfm_pt_transpose[2][0]])
        return np.asarray(trans_face_points)

    def get_nearest_center_piece(self, face_center):
        min_dist = 100
        min_tag = ''
        for key, item in self.face_centers_dict.items():
            # print(key, item["face_center"])
            distance_square = ((item["face_center"][0] - face_center[0])**2) + \
                              ((item["face_center"][1] - face_center[1])**2) + \
                              ((item["face_center"][2] - face_center[2])**2)
            dist = np.sqrt(distance_square)
            if dist < min_dist:
                min_dist = dist
                min_tag = key
        return min_tag

    def get_current_location(self, cubie):
        loc = ""
        if cubie.current_face1_points is not None:
            cubie_center1 = self.compute_face_center(cubie.current_face1_points["points"])
            tag1 = self.get_nearest_center_piece(cubie_center1)
            loc = loc + tag1
        if cubie.current_face2_points is not None:
            cubie_center2 = self.compute_face_center(cubie.current_face2_points["points"])
            tag2 = self.get_nearest_center_piece(cubie_center2)
            loc = loc + tag2
        if cubie.current_face3_points is not None:
            cubie_center3 = self.compute_face_center(cubie.current_face3_points["points"])
            tag3 = self.get_nearest_center_piece(cubie_center3)
            loc = loc + tag3
        return loc

    def transform_n_update(self, cubies_of_interest, angle_deg, center_tag):
        if (angle_deg % 90) == 0:
            axis_normal = self.face_centers_dict[center_tag]["face_normal"]
            axis_point = self.face_centers_dict[center_tag]["face_center"]
            trans_mat = self.get_transformation_matrix(axis_normal, axis_point, angle_deg)
            for cubie in cubies_of_interest:
                if cubie.current_face1_points is not None:
                    cubie.current_face1_points["points"] = self.transform_face(cubie.current_face1_points["points"], trans_mat)
                if cubie.current_face2_points is not None:
                    cubie.current_face2_points["points"] = self.transform_face(cubie.current_face2_points["points"], trans_mat)
                if cubie.current_face3_points is not None:
                    cubie.current_face3_points["points"] = self.transform_face(cubie.current_face3_points["points"], trans_mat)

            # update the current cubicle tag

            for cubie in cubies_of_interest:
                new_loc = self.get_current_location(cubie)
                cubie.current_cubicle = new_loc
        else:
            print('invalid rotation angle, should be multiples of 90 deg')

    def rotate_layer(self, centre_piece_tag, angle_deg):
        cubies_of_interest = []
        for cubie in self.cube:
            if centre_piece_tag in cubie.current_cubicle and cubie.type != "center":
                cubies_of_interest.append(cubie)
        if len(cubies_of_interest) < 8:
            print('something fishy while extracting cubies of interest!')
            print('tag should be either u/l/f/d/r/b (small case)')
        else:
            self.transform_n_update(cubies_of_interest, angle_deg, centre_piece_tag)

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

    def get_tag_current_cubicle_dict(self):
        dict_cubes = {}
        for cubie in self.cube:
            dict_cubes.update({cubie.tag: cubie.current_cubicle})
        return dict_cubes

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

    def appending_move(self):
        new_list = self.get_tag_current_cubicle_dict()
        for key, value in new_list.items():
            self.cubies_moves[key].append(value)
        print('')





