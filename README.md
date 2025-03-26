# VAT: Visual Assessment of (Cluster) Tendency

This repository contains our implementation of the VAT algorithm as described in the paper ["VAT: A Tool for Visual Assessment of (Cluster) Tendency"](https://www.researchgate.net/publication/3950332_VAT_A_tool_for_visual_assessment_of_cluster_tendency) by J.C. Bezdek and R.J. Hathaway.

## Algorithm Overview

VAT is a tool for visually assessing whether clusters exist in a dataset before applying clustering algorithms. It works by:
1. Creating a dissimilarity (distance) matrix between all data points
2. Reordering this matrix to group similar objects together
3. Displaying the reordered matrix as a grayscale image where darker pixels indicate closer objects

## Installation

```bash
pip install -r requirements.txt