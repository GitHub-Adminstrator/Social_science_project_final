---
title: Home Page
layout: single
next: data-description
---

The main idea is to gather as much information about all Pokémon using the [PokéAPI](https://pokeapi.co/) and [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page). A large network of all Pokémon will be created, where two Pokémon are connected if they appear in the same episode.
We hope to show a connection between which Pokémon appear in which episodes, and what the key plot points are in these episodes.
The **PokéAPI** has built-in functionality to gather the names of all approximatly 1000 Pokémon, their types, egg groups, moves etc. This will be our main data set (data set 1). **PokéAPI** is also used to collect text descriptions of the abilities and moves found above. **Bulbapedia** provides the plots of all released Pokémon episodes as well as lists over what Pokémon appear in which episodes (data set 2). More on the data can be seen in [Data description](data-description/).

An analysis of the different seasons of Pokémon, including a network of all seasons combined, can be seen in [Network analysis](network-analysis/).

## Network of all seasons:
<img src="images/network.png" width="500" />

With the data provided from **PokéAPI** and **Bulbapedia**, an investigation of which words are associated with each Pokémon are made. This is done by using the TF-IDF analysis on the Pokémon descriptions and are visualized with wordclouds. Can be seen in [Text analysis](text-analysis/).

## Wordcloud of all seasons:

<img src="wordclouds/All_seasons_mask_coloring.png" width="500" />

## Research questions:

Essentially, this project can be boiled down to the following **research questions**:

1. What characterizes the network for each season of the Pokémon Anime.

2. Are there any similarities or differences between the various seasons and if so, what are these?

3. How do the seasons themselves separate each other w.r.t. their plots, and are there any similarities or differences between seasons?