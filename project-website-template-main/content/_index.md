---
title: Home Page
layout: single
next: data-description
---

The main idea is to gather as much information about all Pokémon using the **PokéAPI** and **Bulbapedia** (Links: https://pokeapi.co/ and https://bulbapedia.bulbagarden.net/wiki/Main_Page). A large network of all Pokémon will be created, where two Pokémon are connected if they appear in the same episode.
We hope to show a connection between which Pokémon appear in which episodes, and what the key plot points are in these episodes.
The **PokéAPI** has built-in functionality to gather the names of all approximatly 1000 Pokémon, their types, egg groups, moves etc. This will be our main data set (data set 1). **PokéAPI** is also used to collect text descriptions of the abilities and moves found above. **Bulbapedia** provides the plots of all released Pokémon episodes as well as lists over what Pokémon appear in which episodes. 

## [Poké Network](network-analysis/):
<img src="images/network.png" width="500" />

With the data provided from **PokéAPI** and **Bulbapedia**, we can investigate which words are associated with each Pokémon are made. This is done by using the TF-IDF analysis on the Pokémon descriptions.

# Degree distribution:
<img src="images/degree_distribution_all.png" width="500" />

# Degree rank plot:
<img src="images/degree_rank_plot_all.png" width="500" />

# Random distribution:
<img src="images/random_distributions_all.png" width="600" />

## Math formula


$$ x^n + y^n = z^n $$
$$ hej \space jord $$

## Code chunk

```
import pandas as pd

df = pd.DataFrame()
```

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam nec mauris aliquet, convallis ligula vel, mollis est. Fusce accumsan massa vel lectus dapibus, at vehicula elit auctor.

| Column 1  | Column 2  |  Column 3 |
|---|---|---|
| 1 | 4 | 7 |
| 2 | 5 | 8 |
| 3 | 6 | 9 |

## [Explainer Notebook](explainer-notebook.html)

Aenean non augue vulputate, bibendum ligula ac, euismod arcu. Proin consequat, urna at lobortis sodales, ligula nulla molestie dolor, et interdum nulla arcu eu lacus. Aenean maximus mi vel augue blandit, quis vehicula libero egestas. In mollis nibh in turpis sodales, eget luctus sem pretium. Integer lobortis diam vel nisi laoreet, ut condimentum risus ultrices. Praesent diam risus, imperdiet at lorem in, hendrerit auctor ex.