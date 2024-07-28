#!/bin/bash

nvidia-smi --query-compute-apps=pid --format=csv,noheader | xargs -n 1 -I {} kill -9 {}
