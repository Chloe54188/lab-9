#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:02:57 2024

@author: chennuo
"""

import random

class Agent:
    def __init__(self, world, x=None, y=None):
        self.world = world
        self.x = x if x is not None else random.randint(0, world.width - 1)
        self.y = y if y is not None else random.randint(0, world.height - 1)

    def find_empty_patch(self):
        empty_patches = [(i, j) for i in range(self.world.width) for j in range(self.world.height) if self.world.grid[i][j] is None]
        if empty_patches:
            return random.choice(empty_patches)
        return None

    def move(self):
        new_position = self.find_empty_patch()
        if new_position:
            self.world.grid[self.x][self.y] = None
            self.x, self.y = new_position
            self.world.grid[self.x][self.y] = self

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(height)] for _ in range(width)]
        self.agents = [Agent(self) for _ in range(num_agents)]

        for agent in self.agents:
            self.grid[agent.x][agent.y] = agent

    def step(self):
        for agent in self.agents:
            agent.move()

    def display(self):
        for row in self.grid:
            print(' '.join(['A' if cell else '.' for cell in row]))
        print()

def main():
    width, height, num_agents, num_steps = 5, 5, 3, 10
    world = World(width, height, num_agents)

    for step in range(num_steps):
        print(f"Step {step + 1}")
        world.display()
        world.step()

if __name__ == "__main__":
    main()

