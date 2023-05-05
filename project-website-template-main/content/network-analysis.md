---
title: Network analysis
prev: data-description
next: text-analysis
---

## Seasons: [1](#season-1-indigo) [2](#season-2-orange) [3](#season-3-johto) [4](#season-4-hoenn) [5](#season-5-sinnoh) [6](#season-6-unova) [7](#season-7-kalos) [8](#season-8-alola) [9](#season-9-journeys) [All](#all-seasons)

In this section we will discuss and describe the network analysis of the Pokémon seasons. We will look at the network of all Pokémon in all seasons, and see how the pokémon are connected based on their appearance in each episode. We will also look at the degree distribution of the networks, and compare them to a random network. It is worth noticing that the networks size increase from season to season, since more and more pokémon are introduced. This means that the networks are not directly comparable, but we can still compare the degree distribution of the networks.

# **All seasons**

<img src="/images/network.png" width="400" />

In the graph explaining the network of all seasons, we can see that there are a few Pokémon that are very connected, and a lot of Pokémon that are not connected at all. This is expected, as there are a few Pokémon that are in almost every episode, and a lot of Pokémon that are only in a few episodes. Furthermore, we can clearly interpret what pokémon are the "main" characters for the 10 seasons. For example, we see a lot of connections to Pikachu, Ash's main Pokémon, and we also see a lot of connections to Team Rocket's Pokémon, Meowth, Wobbuffet and Mime Jr. The network for all seasons contains 869 nodes and 119010 edges.

By looking at the degree distribution of the network, we can see that it somehow resembles a power law distribution. This means that there are a few nodes with a very high degree, and a lot of nodes with a very low degree. This is also expected, as there are a few Pokémon that appear in almost every episode, and a lot of Pokémon that appear in only a few episodes. By looking at the degree rank plot for all seasons, we can see that the degree rank plot has a steep start and then tends to be linear, which means that the degree distribution is a power law distribution as expected:

<img src="/images/degree_all.png" width="600" />

If we compare the degree distribution of the network to a random network to the actual means, we can clearly see that our network does not tend to be randomized. This indicates that there is a connection between the pokémons' attributes in each episode. We hypothesize that if a pokémon appears in an episode, their families (pokémon with same type or egg-group) and they evolved state would also appear - resulting in the connection we see:

<img src="/images/random_distributions_all.png" width="700" />

#
#
# **Season 1 (Indigo)**
First season of pokémon is Indigo, and here we see the most known pokémons such as Pikachu, Meowth, Bulbasaur, Squirtle and more. The network for season 1 contains 153 nodes and 5250 edges.

<img src="/images/network_3.png" width="400" />
<img src="/images/season1/degree_plots.png" width="600" />
<img src="/images/season1/random_distributions.png" width="700" />

#
#
# **Season 2 (Orange)**

<img src="/images/network_7.png" width="400" />
<img src="/images/season2/degree_plots.png" width="600" />
<img src="/images/season2/random_distributions.png" width="700" />

#
#
# **Season 3 (Johto)**

<img src="/images/network_4.png" width="400" />
<img src="/images/season3/degree_plots.png" width="600" />
<img src="/images/season3/random_distributions.png" width="700" />

#
#
# **Season 4 (Hoenn)**

<img src="/images/network_2.png" width="400" />
<img src="/images/season4/degree_plots.png" width="600" />
<img src="/images/season4/random_distributions.png" width="700" />

#
#
# **Season 5 (Sinnoh)**

<img src="/images/network_8.png" width="400" />
<img src="/images/season5/degree_plots.png" width="600" />
<img src="/images/season5/random_distributions.png" width="700" />

#
#
# **Season 6 (Unova)**

<img src="/images/network_9.png" width="400" />
<img src="/images/season6/degree_plots.png" width="600" />
<img src="/images/season6/random_distributions.png" width="700" />

#
#
# **Season 7 (Kalos)**

<img src="/images/network_6.png" width="400" />
<img src="/images/season7/degree_plots.png" width="600" />
<img src="/images/season7/random_distributions.png" width="700" />

#
#
# **Season 8 (Alola)**

<img src="/images/network_1.png" width="400" />
<img src="/images/season8/degree_plots.png" width="600" />
<img src="/images/season8/random_distributions.png" width="700" />

#
#
# **Season 9 (Journeys)**

<img src="/images/network_5.png" width="400" />
<img src="/images/season9/degree_plots.png" width="600" />
<img src="/images/season9/random_distributions.png" width="700" />
