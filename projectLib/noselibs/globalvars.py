# Anthony Ho, ahho@stanford.edu, 10/11/2015
# Last update 3/13/2016
"""Global variables for chemical nose sensors and ligand/mixture information"""


import pandas as pd
import seaborn as sns


# ---- Ligands ---- #

# List of abbreviations of ligands
ligand_names = ['CA', 'GCA', 'TCA',
                'DCA', 'GDCA', 'TDCA',
                'CDCA', 'GCDCA',
                'E1S', 'E2S', 'E3S',
                'P5S', 'DHEAS',
                'DHEAG', 'E2G'
                ]

# Number of ligands
num_ligands = len(ligand_names)

# Dictionary of directory number corresponding to each ligand
ligand_dir_num = {'CA': 6,
                  'GCA': 7,
                  'TCA': 8,
                  'DCA': 9,
                  'GDCA': 14,
                  'TDCA': 15,
                  'CDCA': 10,
                  'GCDCA': 12,
                  'E1S': 2,
                  'E2S': 4,
                  'E3S': 3,
                  'P5S': 1,
                  'DHEAS': 13,
                  'DHEAG': 11,
                  'E2G': 5
                  }

# Dictionary of markers to be used for plotting for each ligand
ligand_markers = {'CA': '^',
                  'GCA': '^',
                  'TCA': '^',
                  'DCA': '^',
                  'GDCA': '^',
                  'TDCA': '^',
                  'CDCA': '^',
                  'GCDCA': '^',
                  'E1S': 'o',
                  'E2S': 'o',
                  'E3S': 'o',
                  'P5S': 's',
                  'DHEAS': 's',
                  'DHEAG': 's',
                  'E2G': 'o'
                  }

# Dictionary of colors to be used for plotting for each ligand
ligand_colors = {'CA': sns.light_palette("purple", 5)[0],
                 'GCA': sns.light_palette("purple", 5)[1],
                 'TCA': sns.light_palette("purple", 5)[2],
                 'DCA': sns.light_palette("lightblue", 3)[0],
                 'GDCA': sns.light_palette("lightblue", 3)[1],
                 'TDCA': sns.light_palette("lightblue", 3)[2],
                 'CDCA': sns.dark_palette("blue", 5)[4],
                 'GCDCA': sns.dark_palette("blue", 5)[2],
                 'E1S': sns.light_palette("darkgreen", 6)[0],
                 'E2S': sns.light_palette("darkgreen", 6)[1],
                 'E3S': sns.light_palette("darkgreen", 6)[2],
                 'P5S': sns.light_palette("darkgreen", 6)[3],
                 'DHEAS': sns.light_palette("darkgreen", 6)[4],
                 'DHEAG': sns.light_palette("red", 4)[1],
                 'E2G': sns.light_palette("red", 4)[3]
                 }

# Dictionary of category colors to be used for plotting for each ligand
ligand_catcolors = {'CA': sns.light_palette("purple", 5)[2],
                    'GCA': sns.light_palette("purple", 5)[2],
                    'TCA': sns.light_palette("purple", 5)[2],
                    'DCA': sns.light_palette("lightblue", 3)[2],
                    'GDCA': sns.light_palette("lightblue", 3)[2],
                    'TDCA': sns.light_palette("lightblue", 3)[2],
                    'CDCA': sns.dark_palette("blue", 5)[4],
                    'GCDCA': sns.dark_palette("blue", 5)[4],
                    'E1S': sns.light_palette("darkgreen", 6)[3],
                    'E2S': sns.light_palette("darkgreen", 6)[3],
                    'E3S': sns.light_palette("darkgreen", 6)[3],
                    'P5S': sns.light_palette("darkgreen", 6)[3],
                    'DHEAS': sns.light_palette("darkgreen", 6)[3],
                    'DHEAG': sns.light_palette("red", 4)[3],
                    'E2G': sns.light_palette("red", 4)[3]
                    }

# List of colors to be used for plotting for each ligand
ligand_catcolors_list = [ligand_catcolors[ligand] for ligand in ligand_names]

# Define class labels and categories
ligand_cat1 = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 3]
ligand_cat_labels1 = ['-cholic acids', '-deoxycholic acids',
                      '-chenodeoxycholic acids', 'Estrogens', 'Androgens']
ligand_cat2 = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4]
ligand_cat_labels2 = ['-cholic acids', '-deoxycholic acids',
                      '-chenodeoxycholic acids', '3-sulfates',
                      '3-glucuronides']
ligand_cat3 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 1]
ligand_cat_labels3 = ['Cholic acids', 'Estrogens', 'Androgens']
ligand_cat4 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
ligand_cat_labels4 = ['Cholic acids', '3-sulfates', '3-glucuronides']

# Define the highest concentration used (uM) in the titration series of ligands
ligand_highest_conc = {'CA': 4096,
                       'GCA': 4096,
                       'TCA': 4096,
                       'DCA': 4096,
                       'GDCA': 4096,
                       'TDCA': 4096,
                       'CDCA': 2048,
                       'GCDCA': 4096,
                       'E1S': 1024,
                       'E2S': 1024,
                       'E3S': 1024,
                       'P5S': 256,
                       'DHEAS': 1024,
                       'DHEAG': 512,
                       'E2G': 1024
                       }


# ---- Mixtures ---- #

# Define complex mixture ID's
cm_id = ['cm_'+str(cm) for cm in range(1, 19)]

# Define true concentrations (uM) in complex mixtures
cm_true_conc = pd.DataFrame({'cm_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 44, 0, 235],
                             'cm_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 228, 175, 105, 0, 0, 0],
                             'cm_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 201, 301],
                             'cm_4': [0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 0, 141, 0, 43],
                             'cm_9':  [0, 0, 50, 0, 500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             'cm_10': [15, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0],
                             'cm_11': [0, 50, 0, 150, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0],
                             'cm_12': [1500, 0, 0, 0, 1200, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0],
                             'cm_17': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 0, 0],
                             'cm_18': [0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 100]
                             },
                            index=ligand_names)