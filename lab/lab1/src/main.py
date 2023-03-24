import sys
import numpy as np
import math


epsilon = 10**(-15)


class Solution():

    def __init__(self, x_p, x_q, y_q) -> None:
        self.p = np.array([x_p, 0])
        self.q = np.array([x_q, y_q])

    def Angle(self, theta):
        t = np.array([math.cos(theta), math.sin(theta)])
        tp = np.array([self.p[0] - t[0], self.p[1] - t[1]])
        tq = np.array([self.q[0] - t[0], self.q[1] - t[1]])
        ptv = math.acos(
            np.dot(tp, t) / (np.linalg.norm(tp) * np.linalg.norm(t)))
        qtv = math.acos(
            np.dot(tq, t) / (np.linalg.norm(tq) * np.linalg.norm(t)))

        return ptv, qtv

    def binary_search(self):
        theta1 = np.arccos(0)
        theta2 = np.arccos(-1)
        theta3 = 0

        while True:
            theta3 = (theta1 + theta2)/2
            angle1, angle2 = self.Angle(theta3)

            if abs(theta1 - theta2) < epsilon:
                break
            if angle1 < angle2:
                theta2 = theta3
            else:
                theta1 = theta3

        t = np.array([math.cos(theta1), math.sin(theta1)])
        r = np.array([self.q[0] - 2 * t[0] * (np.dot(t, self.q) - 1),
                      self.q[1] - 2 * t[1] * (np.dot(t, self.q) - 1)])
        return t, r


if __name__ == '__main__':
    x_p, x_q, y_q = sys.argv[1], sys.argv[2], sys.argv[3]
    # x_p, x_q, y_q = -10, -2, 1

    solution = Solution(x_p, x_q, y_q)
    print(solution.binary_search())

    # p = "6e"

    # P = np.array([-2, -10, -1.000001, -2, -2.33, -3, -3, -3, -10, -1024])
    # Q = np.array([[-1, 1], [-2, 1], [-2, 2], [-1, 0.000001],
    #              [-3, 1], [-1, 0.5], [-2, 10], [-3, 1], [-2, 1], [-8, 4]])

    # for i in range(P.shape[0]):

    #     solution = Solution(P[i], Q[i][0], Q[i][1])
    #     T, R = solution.binary_search()

    #     print(
    #         f"$({P[i]}, {0})$ & $({Q[i][0]}, {Q[i][1]})$ & $({T[0]: .{p}}, {T[1]: .{p}})$ & $({R[0]: .{p}}, {R[1]: .{p}})$\\\\")
