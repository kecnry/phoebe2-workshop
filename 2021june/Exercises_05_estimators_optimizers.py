#!/usr/bin/env python
# coding: utf-8

# # Exercises #5: Estimators & Optimizers
# 
# These exercises are designed to be done anytime after Tutorial #8b (optimizers).
# 
# Download the following files, and run estimators and optimizers to try to find a decent fit to the observations.  
# * [lc.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/testcase/lc.data) (times, fluxes, sigmas)
# * [rv1.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/testcase/rv1.data) (times, rvs, sigmas for primary star)
# * [rv2.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/testcase/rv2.data) (times, rvs, sigmas for secondary star - same times `rv1.data`, so feel free to merge into a single PHOEBE dataset)
# 
# 
# The test case is more complicated than the one demonstrated and would require more parameter tweaking and back and forth to get a good estimate!.
# 
# Refer to the docs in http://phoebe-project.org/docs/2.3/api/phoebe.parameters.solver if you need to tweak additional parameters that haven't been covered in the tutorials. For example, if you're using your own data and have a lot of data points, you can bin the data by passing `phase_bin=True` and `phase_nbins` in the geometry estimators.
# 
# For optimization runs, feel free to submit the jobs remotely and make use of `progress_every_niters` and `b.load_job_progress`.