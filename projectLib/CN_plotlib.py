# Anthony Ho, ahho@stanford.edu, 9/1/2015
# Last update 9/1/2016
"""Python module containing plot functions for chemical nose project"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotlib
import liblib
from fittinglibs import plotting, processresults


# Plot fitted binding curve of a single variant
# Borrowed from Sarah's pipeline with modifications to show Kd instead of dG, 
# and allow for using current axis
def plotBindingCurve(affinityData, variant, annotate=True, ax=None):
    '''Plot a binding curve of a particular variant'''
    # Load data
    subSeries = affinityData.getVariantBindingSeries(variant)
    if len(subSeries)==0:
        print 'No fluorescence data associated with variant %s'%str(variant)
        return
    concentrations = affinityData.x
    variant_table = affinityData.variant_table
    
    # Plot
    if ax is None:
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
    plotting.plotFitCurve(concentrations, subSeries, variant_table.loc[variant], ax=ax)

    plotlib.setproperties(xlabel='Concentration (nM)', ylabel='Fluorescence', 
                          labelfontsize=16, tickfontsize=16)

    # Annonate
    if annotate:
        names = ['dG', 'dG_lb', 'dG_ub', 'fmax', 'fmax_lb', 'fmax_ub', 'numTests', 'pvalue', 'rsq', 'flag']
        vec = pd.Series([processresults.getValueInTable(variant_table.loc[variant], name) for name in names], index=names)
            #vec.fillna('', inplace=True)
        annotationText = ['Kd = {:4.2f} uM ({:4.2f}, {:4.2f})'.format(liblib.dGtoKd(vec.dG, 'uM'),
                                                                   liblib.dGtoKd(vec.dG_lb, 'uM'),
                                                                   liblib.dGtoKd(vec.dG_ub, 'uM')),
                          'fmax = {:4.2f} ({:4.2f}, {:4.2f})'.format(vec.fmax,
                                                                     vec.fmax_lb,
                                                                     vec.fmax_ub),
                          'Nclusters = {:4.0f}'.format(vec.numTests),
                          'pvalue = {:.1e}'.format(vec.pvalue),
                          'average Rsq = {:4.2f}'.format(vec.rsq),
                          'fmax enforced = {}'.format(vec.flag)
                          ]
        ax.annotate('\n'.join(annotationText), xy=(0.05, .95), xycoords='axes fraction',
                    horizontalalignment='left', verticalalignment='top', fontsize=11)

    return ax


# Plot fitted binding curves of a single variant across different targets
# Borrowed from Sarah's pipeline with modifications to show Kd instead of dG, 
# and allow for using current axis
def plotBindingCurvesAcrossTargets(affinityDataList, variant, 
                                  colors=None, names=None, norm=False, ax=None):
    '''Plot a binding curve of a particular variant'''

    if colors is None:
        colors = sns.color_palette("Paired", 12)

    if ax is None:
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)

    for i, affinityData in enumerate(affinityDataList):
        
        # Load data
        subSeries = affinityData.getVariantBindingSeries(variant)
        if len(subSeries)==0:
            print 'No fluorescence data associated with variant %s'%str(variant)
            return
        concentrations = affinityData.x
        variant_table = affinityData.variant_table
        variant_data = variant_table.loc[variant]

        if norm:
            fmax = variant_data['fmax']
            subSeries = subSeries.copy() / fmax
            variant_data = variant_data.copy()
            for field in ['fmax_init', 'fmin_init', 
                          'fmax_lb', 'fmax', 'fmax_ub', 
                          'fmin_lb', 'fmin', 'fmin_ub']:
                variant_data[field] = variant_data[field] / fmax
        
        # Plot
        plotting.plotFitCurve(concentrations, subSeries, variant_data, ax=ax)
        
        ax.lines[i*4+3].set_color(colors[i])
        ax.lines[i*4+3].set_linewidth(2)
        if names is not None:
            ax.lines[i*4+3].set_label(names[i])
    
    if norm:
        ylabel = 'Normalized fluorescence'
    else:
        ylabel = 'Fluorescence'
    plotlib.setproperties(xlabel='Concentration (nM)', ylabel=ylabel, 
                          labelfontsize=16, tickfontsize=16, 
                          legend=names, legendloc=2, legendfontsize=12)

    return ax


# Plot fitted binding curves of different variant on the same target
# Borrowed from Sarah's pipeline with modifications to show Kd instead of dG, 
# and allow for using current axis
def plotBindingCurvesAcrossVariants(affinityData, variantList, 
                                    colors=None, norm=False, ax=None):
    '''Plot a binding curve of a particular variant'''

    if colors is None:
        colors = sns.color_palette("Paired", 12)

    if ax is None:
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)

    for i, variant in enumerate(variantList):
        
        # Load data
        subSeries = affinityData.getVariantBindingSeries(variant)
        if len(subSeries)==0:
            print 'No fluorescence data associated with variant %s'%str(variant)
            return
        concentrations = affinityData.x
        variant_table = affinityData.variant_table
        variant_data = variant_table.loc[variant]
        
        if norm:
            fmax = variant_data['fmax']
            subSeries = subSeries.copy() / fmax
            variant_data = variant_data.copy()
            for field in ['fmax_init', 'fmin_init', 
                          'fmax_lb', 'fmax', 'fmax_ub', 
                          'fmin_lb', 'fmin', 'fmin_ub']:
                variant_data[field] = variant_data[field] / fmax
        
        # Plot
        plotting.plotFitCurve(concentrations, subSeries, variant_data, ax=ax)
        
        ax.lines[i*4+3].set_color(colors[i])
        ax.lines[i*4+3].set_linewidth(2)

    if norm:
        ylabel = 'Normalized fluorescence'
    else:
        ylabel = 'Fluorescence'    
    plotlib.setproperties(xlabel='Concentration (nM)', ylabel=ylabel, 
                          labelfontsize=16, tickfontsize=16)

    return ax