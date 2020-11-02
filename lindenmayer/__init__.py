# -*- coding: utf-8 -*-
import math


class LindenmayerSystem(object):
    """Lindenmayer System

    A simple class for generating Lindenmayer Systems.

    See `operations` for list of available operations.

    Reference:
       https://en.wikipedia.org/wiki/L-system

    """

    operations = {
        "draw": {
            "keywords": "ABFG",
            "description": "Move forward by line length drawing a line",
        },
        "move": {
            "keywords": "abfg",
            "description": "Move forward by line length without drawing a line",
        },
        "turnleft": {"keywords": "-", "description": "Turn left by turning angle"},
        "turnright": {"keywords": "+", "description": "Turn right by turning angle"},
        "push": {
            "keywords": "[",
            "description": "Push current drawing state onto stack",
        },
        "pop": {
            "keywords": "]",
            "description": "Pop current drawing state from the stack",
        },
    }

    def __init__(self, config):
        """Example usage:

        config = {
            'start': 'X',
            'rules': {
                'X': 'F+[[X]-X]-F[-FX]+X',
                'F': 'FF'
            }
        }

        ls = LindenmayerSystem(config)
        """
        self.__start = config["start"]
        self.__rules = config["rules"]
        self.__iterations = 0
        self.__string = self.__start

    def __repr__(self):
        rules = []
        for k, v in sorted(self.__rules.items()):
            rules.append("%s=>%s" % (k, v))
        return "LindenmayerSystem(start=%s rules={%s} iterations=%d)" % (
            self.__start,
            ", ".join(rules),
            self.__iterations,
        )

    @property
    def string(self):
        """Return the current string""" 
        return self.__string

    def reset(self):
        """Restore the system to the initial state"""
        self.__string = self.__start
        self.__iterations = 0

    def iterate(self, iterations=1):
        """Iterate the Lindenmayer System ``iteration`` times"""
        for _ in range(iterations):
            self.__string = self.__one_pass(self.__string)
            self.__iterations += 1
        return self.__string

    def get_points(self, startpos=(0, 0), startangle=0, angle=90, step=10):
        """Get an list of lists with points from the Lindenmayer System"""
        points = []
        stack = []
        x, y = startpos
        alpha = startangle
        currpoints = [(startpos)]

        for c in self.__string:
            op = self.__get_op(c)
            if op == "draw":
                x += step * math.cos(math.radians(alpha))
                y += step * math.sin(math.radians(alpha))
                currpoints.append((round(x, 5), round(y, 5)))
            elif op == "move":
                if len(currpoints) > 1:
                    points.append(currpoints)
                x += step * math.cos(math.radians(alpha))
                y += step * math.sin(math.radians(alpha))
                currpoints = [(round(x, 5), round(y, 5))]
            elif op == "turnleft":
                alpha += angle
            elif op == "turnright":
                alpha -= angle
            elif op == "push":
                stack.append((x, y, alpha))
            elif op == "pop":
                if len(currpoints) > 1:
                    points.append(currpoints)
                (x, y, alpha) = stack.pop()
                currpoints = [(round(x, 5), round(y, 5))]
            elif op == "":
                pass
            else:
                print("unknown op: %s" % op)

        if len(currpoints) > 1:
            points.append(currpoints)
        return points

    def __one_pass(self, string):
        result = ""
        for c in string:
            if c in self.__rules:
                result += self.__rules[c]
            else:
                result += c
        return result

    def __get_op(self, c):
        for op in self.operations:
            if c in self.operations[op]["keywords"]:
                return op
        return ""
