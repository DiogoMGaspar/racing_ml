import pygame
import numpy as np
from point import Point
from math import sin, cos, pi, sqrt
from constants import DARK_GREY

class TrackSpline:
    def __init__(self, track_data, show_labels=False):
        # Data
        self.waypoints = track_data["waypoints"]
        self.track_width = track_data["track_width"]
        self.points = []
        self.length = 0

        # Display
        self.resolution = 40
        self.track_colour = DARK_GREY
        self.show_labels = show_labels

    def create_track(self):
        self.points = []

        for i, waypoint in enumerate(self.waypoints):
            x = waypoint[0]
            y = waypoint[1]
            point = Point((x, y))
            
            # Optionally add labels
            if self.show_labels:
                point.label = f"P{i}"
            
            self.points.append(point)

    def get_track_point(self, t):
        t = t / self.resolution
        num_points = len(self.points)

        # Four control points
        p1 = (int(t) + 1) % num_points
        p2 = (p1 + 1) % num_points
        p3 = (p2 + 1) % num_points
        p0 = (p1 - 1) % num_points
        
        t -= int(t)
        
        T = np.array([t**3, t**2, t, 1])

        # Catmull-Rom basis matrix
        M = np.array([
            [-1,  3, -3,  1],
            [ 2, -5,  4, -1],
            [-1,  0,  1,  0],
            [ 0,  2,  0,  0]
        ]) / 2

        # Get control points' coordinates as a vector
        Px = np.array([self.points[p0].x, self.points[p1].x, self.points[p2].x, self.points[p3].x])
        Py = np.array([self.points[p0].y, self.points[p1].y, self.points[p2].y, self.points[p3].y])

        # Compute interpolated x and y
        x = np.dot(T, np.dot(M, Px))
        y = np.dot(T, np.dot(M, Py))

        return x, y

    def draw(self, display):
        total_points = self.resolution * len(self.points)

        for i in range(total_points):
            x, y = self.get_track_point(i)
            pygame.draw.circle(display, self.track_colour, (int(x), int(y)), self.track_width)

        if self.show_labels:
            for point in self.points:
                point.draw(display)

    def calculate_track_length(self):
        length = 0
        total_points = self.resolution * len(self.points)

        for i in range(total_points):
            start_point = self.get_track_point(i)
            end_point = self.get_track_point(i + 1 if i + 1 < total_points else 0)  # This makes sure we close the loop
            length += self.get_distance(start_point, end_point)
            length += Point(*start_point).distance_to(Point(*end_point))

        self.length = length
        return length