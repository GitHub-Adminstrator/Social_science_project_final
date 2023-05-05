---
title: Home Page
layout: single
next: data-description
---

The main idea is to gather as much information about all Pokémon using the [PokéAPI](https://pokeapi.co/) and [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page). A large network of all Pokémon will be created, where two Pokémon are connected if they appear in the same episode.
We hope to show a connection between which Pokémon appear in which episodes, and what the key plot points are in these episodes.
The **PokéAPI** has built-in functionality to gather the names of all approximatly 1000 Pokémon, their types, egg groups, moves etc. This will be our main data set (data set 1). **PokéAPI** is also used to collect text descriptions of the abilities and moves found above. **Bulbapedia** provides the plots of all released Pokémon episodes as well as lists over what Pokémon appear in which episodes. 

## [Poké Network](network-analysis/):
<img src="images/network.png" width="500" />

With the data provided from **PokéAPI** and **Bulbapedia**, we can investigate which words are associated with each Pokémon are made. This is done by using the TF-IDF analysis on the Pokémon descriptions.
