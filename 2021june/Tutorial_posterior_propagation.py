#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Propagating Posteriors
# 
# In this tutorial we'll cover how to propagate posteriors through the forward model and to constrained parameters.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Advanced: Distribution Propagation](http://phoebe-project.org/docs/2.3/tutorials/distribution_propagation.ipynb)
# 

# In[ ]:


import phoebe

b = phoebe.load('./data/synthetic/after_final_round.bundle')


# In[ ]:


_ = b.plot_distribution_collection(solution='final_round', show=True)


# As we saw in the [distributions tutorial](./Tutorial_07_distributions.ipynb), we can pass `parameters` to propagate this set of distributions through the constraint to any other parameter(s).  For example, to see how eccentricity and argument of periastron look in `esinw` and `ecosw` instead.

# In[ ]:


_ = b.plot_distribution_collection(solution='final_round', parameters=['ecc', 'per0'], show=True)


# In[ ]:


_ = b.plot_distribution_collection(solution='final_round', parameters=['esinw', 'ecosw'], show=True)


# And we can also do the same thing as an argument to [uncertainties_from_distribution_collection](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection):

# In[ ]:


b.uncertainties_from_distribution_collection(solution='final_round', parameters=['ecc', 'per0'], tex=True)


# In[ ]:


b.uncertainties_from_distribution_collection(solution='final_round', parameters=['esinw', 'ecosw'], tex=True)


# As we've already seen several times, we can also sample from the posteriors to propagate through the forward model.

# In[ ]:


b.run_compute(compute='nm_fit', solution='final_round', sample_num=20, model='post_prop')


# In[ ]:


_ = b.plot(model='post_prop', kind='rv', x='phases', show=True)


# In[ ]:


_ = b.plot(model='post_prop', kind='rv', x='phases', y='residuals', show=True)

