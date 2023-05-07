---
title: Data description
prev: "/"
next: network-analysis
---

This project uses 2 main data sets. [Base Pokémon data](#base-pokémon-data-set) set (978 KB, 905 rows, 6 variables) which we create from PokéAPI. [Episode Plot data](#episode-plot-data-set) set (9018 KB, 1231 rows, 3 variables) which we create from Bulbapedia. The episode plot data contains 9 "sub-data-sets" (one for each season) which we will use to create the network analysis.

The two data sets can be downloaded here:

> # <a href="/pokemon_clean.pickle" download>Base Pokémon data set</a> (978 KB)

> # <a href="/all_seasons_df.pkl" download>Episode Plot data set</a> (9018 KB)

The data sets are described in more detail below.

# **Base Pokémon data set**

The Base pokémon data set contains information about all pokémon in the first 9 seasons of the Pokémon series. The data set contains the following variables:

- **`pokemon`**: The name of the pokémon
- **`abilities`**: The abilities of the pokémon
- **`types`**: The type of the pokémon
- **`egg-groups`**: The egg-group of the pokémon
- **`moves`**: The moves of the pokémon
- **`pokedex_entry`**: The desciption of the pokémon

#
#

# **Episode Plot data set**

The Episode Plot data set contains information about all episodes in the first 9 seasons of the Pokémon series. The data set contains the following variables:

- **`pokemon`**: List of pokémon in the episode
- **`plot`**: The plot of the episode
- **`season`**: Which season the episode is from

The key take way from this data set is that we get a text analysis of each episode aswell as the pokémon in it, which can be used to see which words are associated with each pokémon.
