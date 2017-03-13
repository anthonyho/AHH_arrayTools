# Anthony Ho, ahho@stanford.edu, 2/7/2017
# Last update 3/13/2017
"""Library containing the auxiliary functions"""


import numpy as np
import pandas as pd
import globalvars


T = 19.72386556666862
RT = 0.0019872036 * (T + 273.15)


# Convert delta G in kcal/mol to Kd. Default Kd unit is uM.
def dG_to_Kd(data, unit='uM'):
    """Converts delta G in kcal/mol to Kd """
    # Set unit multiplier
    if unit == 'pM':
        multiplier = 1e12
    elif unit == 'nM':
        multiplier = 1e9
    elif unit == 'uM':
        multiplier = 1e6
    elif unit == 'mM':
        multiplier = 1e3
    elif unit == 'M':
        multiplier = 1
    else:
        raise ValueError('Unit \"'+unit+'\" not supported!')

    try:
        return np.exp(data.astype(float) / RT) * multiplier
    except AttributeError:
        return np.exp(data / RT) * multiplier


# Convert Kd to delta G in kcal/mol. Default Kd unit is uM.
def Kd_to_dG(data, unit='uM'):
    """Converts Kd to delta G in kcal/mol"""
    # Set unit multiplier
    if unit == 'pM':
        multiplier = 1e12
    elif unit == 'nM':
        multiplier = 1e9
    elif unit == 'uM':
        multiplier = 1e6
    elif unit == 'mM':
        multiplier = 1e3
    elif unit == 'M':
        multiplier = 1
    else:
        raise ValueError('Unit \"'+unit+'\" not supported!')

    try:
        return np.log(data.astype(float) / multiplier) * RT
    except AttributeError:
        return np.log(data / multiplier) * RT


# Function to return a confusion matrix of the true concentrations of ligands
def generate_true_conc_df(conc,
                          list_ligands=globalvars.ligand_names,
                          list_samples=globalvars.ligand_names):
    true_conc_df = pd.DataFrame(0, index=list_ligands,
                                columns=list_samples)
    for ligand in list(set(list_ligands) & set(list_samples)):
        true_conc_df.loc[ligand, ligand] = conc
    return true_conc_df