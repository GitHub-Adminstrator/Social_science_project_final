---
title: Data description
prev: "/"
next: network-analysis
---

This project uses 2 main data sets. [Base Pokémon data](#base-pokémon-data-set) set (X MB, X rows, X variables) which we create from PokéAPI. [Episode Plot data](#episode-plot-data-set) set (X MB, X rows, X variables) which we create from Bulbapedia. The episode plot data contains 9 "sub-data-sets" (one for each season) which we will use to create the network analysis.

The two data sets can be downloaded here:

> [Base Pokémon data set](/data/pokemon.csv) (X MB)

> [Episode Plot data set](/data/episode_plot.csv) (X MB)

The data sets are described in more detail below.

# **Base Pokémon data set**

The Base pokémon data set contains information about all pokémon in the first 9 seasons of the Pokémon series. The data set contains the following variables:

- **`typing`**: The type of the pokémon
- **`name`**: The name of the pokémon
- **`abilities`**: The abilities of the pokémon
- **`egg-groups`**: The egg-group of the pokémon
- Tilføj flere variable!!

#
#

# **Episode Plot data set**

The Episode Plot data set contains information about all episodes in the first 9 seasons of the Pokémon series, herunder key-plots, characters, pokémon and more. The data set contains the following variables:

- **`season`**: The season of the episode
- **`episode`**: The episode number
- **`title`**: The title of the episode
- **`plot`**: The plot of the episode
- **`characters`**: The characters in the episode
- **`pokémon`**: The pokémon in the episode
- **`locations`**: The locations in the episode
- **`key-plot`**: The key-plot of the episode


