#!/usr/bin/env python

# Copyright 2019 OffWorld Inc.
# Doing business as Off-World AI, Inc. in California.
# All rights reserved.
#
# Licensed under GNU General Public License v3.0 (the "License")
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Unless required by applicable law, any source code or other materials
# distributed under the License is distributed on an "AS IS" basis,
# without warranties or conditions of any kind, express or implied.

import gym
import logging

from offworld_gym.envs.common.channels import Channels
import time


# create the environment
env = gym.make("OffWorldDockerMonolithDiscreteSim-v0", channel_type=Channels.RGBD)
env.seed(42)

print(f"action space: {env.action_space} observation_space: {env.observation_space}")
step = 0
start = time.time()
while True and step < 100:
    env.reset()
    done = False
    while not done:
        sampled_action = env.action_space.sample()
        env.render()
        obs, rew, done, info = env.step(sampled_action)
        print(obs.shape)
        step += 1
end = time.time()

print(end - start)