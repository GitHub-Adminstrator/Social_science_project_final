---
title: Network analysis
prev: data-description
next: text-analysis
---

## Seasons: [1](#season-1-indigo) [2](#season-2-orange) [3](#season-3-johto) [4](#season-4-hoenn) [5](#season-5-sinnoh) [6](#season-6-unova) [7](#season-7-kalos) [8](#season-8-alola) [9](#season-9-journeys) [All](#all-seasons)

In this section we will discuss and describe the network analysis of the Pokémon seasons. We will look at the network of all Pokémon in all seasons, and see how the pokémon are connected based on their appearance in each episode. We will also look at the degree distribution of the networks, compare the the pokémon attributes to a random network, and lastly look at the modularities. It is worth noticing that the networks size increase from season to season, since more and more pokémon are introduced. This means that the networks are not directly comparable, but we can still compare the degree distribution of the networks.

# Graph size:

What is shown from something as simple as the graph sizes is that obviously the graphs grow from season to season especially in the first couple of seasons. This aligns very well with the fact that the Pokémon anime is based off of the Pokémon video game. In this game series, new Pokémon are added to each iteration of the game, and hence, one would expect the number of Pokémon to increase with each released season. However, at one point, decisions were made to not include all previous Pokémon in the next iteration of the game, and this happened some point between [Unova](#season-6-unova) Leage and the [Kalos](#season-7-kalos) League. This might explain why the number of nodes stopped stopped increasing around this point. 

Also, it is interesting to note that although there were 905 Pokémon left in the dataframe containing all Pokémon, the network of [All seasons](#all-seasons) only has 869 nodes. This should mean that 36 Pokémon do not appear in the show at all. However, the more obvious reason as to why this has happened is due to discrepancies between the names from PokéAPI and Bulbapedia. In the code cell above, the names of these mysterious Pokémon have been printed, and a clear pattern emerges. Some Pokémon have some sort of description after their names such as "Pumpkaboo-average" which will not match the "Pumpkaboo" name found from Bulbapedia. Whilst this is a shame, it has only happened in a small amount of cases, and therefore the impact is assumed to be minimal. Some of these Pokémon are also known as legendary Pokémon, and these are quite rare to appear in the anime episodes as well.

# Degree distribution:

Interesting development from season to season w.r.t top Pokémon, degree distributions and degree assortativity coefficients. First of all, the Pokémon animes favourite character is obviously Pikachu that appears together in an episode with almost every other Pokémon in existence. This makes good sense since Pikachu is the companion of Ash, the shows protagonist, who appears in every season of the show. It is then important to note the other top Pokémon such as Meowth, Wobbuffet, and several others. The Pokémon anime has two main anagonists being the two Team Rocket members Jesse and James. These two has a number of companions being exactly the Pokémon Meowth, Wobbuffet, and Arbok/Seviper with Seviper being the evolution of Arbok. The other top Pokémon often belong to either Ash acting as his team throughout his journey or they belong to the sidekicks of each season. A good example of this is Axew from Season 6 ([Unova](#season-6-unova) League) who is the main Pokémon of the sidekick Iris. 

W.r.t. the degree distributions of each season, the first couple of seasons do not exactly show signs of being heavy-tailed. The hypothesis for this is that there are simply not enough Pokémon yet, and since the show was kind of new, the showrunners would prefer to give a decent amount of airtime to each Pokémon in the show. However, as the number of Pokémon grew, and fan-favourites developed amongst fans, the degree distribution changed accordingly. Also, since the number of Pokémon grew, it was perhaps not possible to include as many Pokémon as possible in each episode without either heavily increasing the amount of episodes or increasing the runtime of each episodes both of which seam infeasible. As such, it makes sense to prioritize more airtime for more popular Pokémon, and this is the hypothesis as to why the degree distributions have evolved as shown in the analyses above.

Looking at the degree assortativity coefficient across seasons, there is a pattern of all seasons having negative values for this measure with the largest being -0.26 ([Orange](#season-2-ornage) Islands, [Kalos](#season-7-kalos) League, and [Alola](#season-8-alola) League) and the smallest being -0.10 (All Seasons). As such, there exists a pattern across all seasons for Pokémon with large degrees being more likely to be connected to Pokémon of smaller degrees, and vice-versa. The hypothesis for this is that the main Pokémon will obviously appear in many episodes, and thus appear in the same episodes as many other Pokémon. On the contrary, more niche Pokémon will not have as much airtime, and not appear in as many episodes. As such, it is more rare for niche Pokémon to appear in the same episode than it is for popular Pokémon. Hence, the reason for the degree assortativity coefficient being negative is an effect of all the niche Pokémon with little airtime having many connections to the popular Pokémon that appear in every episodes.  

# Attribute Analysis:

What is the result of this analysis is that there exist evidence of correlation between which Pokémon have an edge between them, and their attributes. This is true in all seasons of the Pokémon show, albeit with some variations in the p-values (whilst all are still far, far lower than the **significance level of 0.05**). The question is then, if this makes sense. The reason for this being true might be something as simple as the concept of Pokémon families and evolution lines. It is true that Pokémon from the same evolution line will more often than not share the same types, abilities and egg groups. Hence, the reason behind the results shown from the analysis is that when one Pokémon from an evolution line appears in an episodes it evolutions will also appear. This also makes some intuitive sense just as in real life such that Pokémon are likely to stick together in groups or packs with some being further older/more evolved than others. However, whether this is true or not would require further testing, and is currently outside the scope of this project.

# Modularity Analysis:

The final part of the graph analyses covers the community and modularity aspect of the networks. In all the networks, the modularity of these networks are found to be above 0 indicating some slight community structure in the graphs. However, in all cases the partitionings appear to be sub-optimal, and perhaps it does not make sense to separate the nodes into different communities based off of this analysis. From the double edge swap test, trying to determine whether the modularity is random or not, it is shown that the modularity is indeed not random in any of the cases. The question is then, what is the cause of this modularity, and can it be explained? To answer this question, it might make sense to draw on the point raised before about Pokémon families and evolution lines. Hence, some of these communities might exist due to some Pokémon species living in different habitats than others such as in water, forests, caves, etc. Since episodes in the Pokémon anime are rather short, the characters are likely to spend the entire time in one habitat with certain types of Pokémon living there. However, there will certainly exist overlaps in these habitats, as is true for animals in the real world. Whether or not this is the reason for the partitionings is not entirely certain, though, and would require more analysis beyond the scope of this project.

Also note that the network with the largest value of modularity is the network covering all seasons, and this intuitively makes perfect sense. Just as different Pokémon live in different habitats, different Pokémon also live in different regions, and since almost every Pokémon season takes place in a different region, this would explain why the community structure is stronger when looking at all seasons at once. The hypothesis is therefore, that the communities themselves represent regional differences, however, further analysis would be required to determine whether this is true or not. 


# **All seasons**

<img src="/images/network.png" width="400" />

In the graph explaining the network of all seasons, we can see that there are a few Pokémon that are very connected, and a lot of Pokémon that are not connected at all. This is expected, as there are a few Pokémon that are in almost every episode, and a lot of Pokémon that are only in a few episodes. Furthermore, we can clearly interpret what pokémon are the "main" characters for the 10 seasons. For example, we see a lot of connections to Pikachu, Ash's main Pokémon, and we also see a lot of connections to Team Rocket's Pokémon, Meowth, Wobbuffet and Mime Jr. The network for all seasons contains 869 nodes and 119010 edges.

By looking at the degree distribution of the network, we can see that it somehow resembles a power law distribution. This means that there are a few nodes with a very high degree, and a lot of nodes with a very low degree. This is also expected, as there are a few Pokémon that appear in almost every episode, and a lot of Pokémon that appear in only a few episodes. The top 5 Pokémon are Pikachu: 844, Meowth: 821, Wobbuffet: 786, Rotom: 763, Eevee: 716, and a Degree assortativity coefficient of -0.10. By looking at the degree rank plot for all seasons, we can see that the degree rank plot has a steep start and then tends to be linear, which means that the degree distribution is a power law distribution as expected:

<img src="/images/degree_all.png" width="600" />

If we compare the degree distribution of the network to a random network to the actual means, we can clearly see that our network does not tend to be randomized. This indicates that there is a connection between the pokémons' attributes in each episode. We hypothesize that if a pokémon appears in an episode, their families (pokémon with same type or egg-group) and they evolved state would also appear - resulting in the connection we see:

<img src="/images/random_distributions_all.png" width="700" />

The All seasons network had 5 communities with sizes [208, 132, 249, 138, 118]. Modularity of 0.21, however, double edge swap was infeasible to perform due to the number of edges in this graph. This is unfortunate.

#
#
# **Season 1 (Indigo)**
First season of pokémon is Indigo, and here we see the most known pokémons such as Pikachu, Meowth, Bulbasaur, Squirtle and more. The network for season 1 contains 153 nodes and 5250 edges. The network is shown below: 

<img src="/images/network_3.png" width="400" />

If we look at the degree analysis for Indigo League we see that the top 5 Pokémon w.r.t. degree are Pikachu: 150, Meowth: 150, Pidgeotto: 138, Bulbasaur: 137, Squirtle: 136. The distribution of degrees appear pretty uniform, and the degree rank plot shows linear tendenies. The degree assortativity coefficient is at -0.20.

<img src="/images/season1/degree_plots.png" width="600" />

By looking at the random distribution plot for the Indigo season it is obvious that for all three attributes, there is some correlation between the Pokémon that has an edge between them and their attributes. This is both seen in the plots as well as in the statistical test with p-values which os below the chosen significance level of 0.05:

<img src="/images/season1/random_distributions.png" width="700" />

Indigo League has 4 communities with sizes [32, 36, 53, 30]. The modularity for this partitioning is 0.1, and this is found to be significantly different than the average modularity of 0.07 when links between nodes are shuffled.

<img src="/images/season1/modularity_distribution.png" width="400" />

#
#
# **Season 2 (Orange)**
The network for season 2 has 134 nodes and 3399 edges. Here is seems like the network is more connected than the Indigo network, and we can see that there are a lot of pokémon that are connected to each other. The network is shown below:

<img src="/images/network_7.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 131, Meowth: 131, Togepi: 131, Lapras: 120, Squirtle: 114. This is not as uniform as for Indigo League, and does almost appears normally distributed with some nodes having large degrees, but with most lying between ~10 and ~90. The degree assortativity coefficient is -0.26:

<img src="/images/season2/degree_plots.png" width="600" />

By looking at the random distribution plot for the Orange season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season2/random_distributions.png" width="700" />

Orange League has 4 communites with sizes [29, 43, 39, 21] with a modularity of 0.11. Double edge swap yields average modularity of 0.07. This shows a significant difference.

<img src="/images/season2/modularity_distribution.png" width="400" />

#
#
# **Season 3 (Johto)**
The network for season 3 has 258 nodes and 10781 edges. Here it seems like the strenght of the connections are less than for the seasons before. The network is shown below:

<img src="/images/network_4.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 253, Meowth: 253, Togepi: 251, Wobbuffet: 251, Arbok: 235. The graph appears normally distributed, however there is some tendency of heavy-tailed with few nodes having very high degrees. Degree assortativity coefficient of -0.23. It is clear that the amount of the degree in the top pokémon has increased compared to the previous seasons. The degree distribution is shown below:

<img src="/images/season3/degree_plots.png" width="600" />

By looking at the random distribution plot for the Orange season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season3/random_distributions.png" width="700" />

Orange League has 4 communites with sizes [87, 81, 43, 43] with a modularity of 0.11. Double edge swap yields average modularity of 0.08. This shows a significant difference.

<img src="/images/season3/modularity_distribution.png" width="400" />

#
#
# **Season 4 (Hoenn)**

The network for season 4 has 366 nodes and 15134 edges. It is clear that the networks are beginning to have more and more nodes, as more pokémons are introduced. The network is shown below:

<img src="/images/network_2.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 362, Meowth: 362, Wobbuffet: 361, Seviper: 301, Beautifly: 290. The graph mostly resembles a heavy-tailed distribution with very few nodes having large degrees and most nodes clumped. Degree assortativity coefficient of -0.24. The degree distribution is shown below:

<img src="/images/season4/degree_plots.png" width="600" />

By looking at the random distribution plot for the Hoenn season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season4/random_distributions.png" width="700" />

Hoenn League has 5 communities with sizes [122, 22, 54, 91, 74] with a Modularity of 0.16, and double edge swap yields average modularity of 0.09. This shows a significant difference.

<img src="/images/season4/modularity_distribution.png" width="400" />

#
#
# **Season 5 (Sinnoh)**
The network for season 5 has 453 nodes and 20779 edges. The network is shown below:

<img src="/images/network_8.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 447, Meowth: 447, Piplup: 443, Wobbuffet: 428, Croagunk: 386. The degree histogram also shows a heavy-tailed distribution with many nodes having small degrees compared to the few nodes having large degree values. Degree assortativity coefficient of -0.23. The degree distribution is shown below:

<img src="/images/season5/degree_plots.png" width="600" />

By looking at the random distribution plot for the Sinnoh season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season5/random_distributions.png" width="700" />

Sinnoh League has 5 communities with sizes [152, 111, 49, 73, 63] with a Modularity of 0.14, and double edge swap yields average modularity of 0.09. This shows a significant difference.

<img src="/images/season5/modularity_distribution.png" width="400" />

#
#
# **Season 6 (Unova)**
The network for season 6 has 324 nodes and 12658 edges. Here the number of nodes has deacresed compared to the seasons before. The network is shown below:

<img src="/images/network_9.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 320, Axew: 320, Meowth: 296, Oshawott: 288, Pignite: 250. Histogram shows trend of many nodes having smaller degree and very few nodes with large degree. Heavy-tailed distribution. Degree assortativity coefficient of -0.25. The degree distribution is shown below:

<img src="/images/season6/degree_plots.png" width="600" />

By looking at the random distribution plot for the Unova season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season6/random_distributions.png" width="700" />

Unova League has 4 communities with sizes [88, 112, 19, 102] with a Modularity of 0.16, and double edge swap yields average modularity of 0.08. This shows a significant difference.

<img src="/images/season6/modularity_distribution.png" width="400" />

#
#
# **Season 7 (Kalos)**
The network for season 7 has 439 nodes and 21311 edges. The network is shown below:

<img src="/images/network_6.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 433, Dedenne: 433, Meowth: 420, Wobbuffet: 396, Chespin: 357. The degree histogram also shows a heavy-tailed distribution with many nodes having small degrees compared to the few nodes having large degree values. Degree assortativity coefficient of -0.26. The degree distribution is shown below:

<img src="/images/season7/degree_plots.png" width="600" />

By looking at the random distribution plot for the Kalos season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season7/random_distributions.png" width="700" />

Kalos League has 4 communities with sizes [88, 112, 19, 102]. Modularity of 0.16, and double edge swap yields average modularity of 0.08. Significant difference.

<img src="/images/season7/modularity_distribution.png" width="400" />

#
#
# **Season 8 (Alola)**
The network for season 8 has 458 nodes and 28784 edges. The network is shown below:

<img src="/images/network_1.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 451, Rotom: 448, Togedemaru: 446, Vulpix: 429, Turtonator: 403. The degree histogram also shows a heavy-tailed distribution with many nodes having small degrees compared to the few nodes having large degree values. Degree assortativity coefficient of -0.26. The degree distribution is shown below:

<img src="/images/season8/degree_plots.png" width="600" />

By looking at the random distribution plot for the Alola season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season8/random_distributions.png" width="700" />

Alola League has 5 communities with sizes [164, 86, 94, 43, 65] with a Modularity of 0.13, and double edge swap yields average modularity of 0.12. This shows a significant difference.

<img src="/images/season8/modularity_distribution.png" width="400" />

#
#
# **Season 9 (Journeys)**
The network for season 9 has 698 nodes and 53260 edges. We can see that a lot pokémon has been introduced to the show, compared to the first season. However, the "main" pokémon are still the same (Pikachu and Meowth). The network is shown below:

<img src="/images/network_5.png" width="400" />

The top 5 Pokémon w.r.t. degree are Pikachu: 688, Rotom: 663, Meowth: 576, Grookey: 568, Wobbuffet: 560. There the distribution plot in histogram are interesting. It has a lot of nodes with small degree, then a decently sized group with degrees around ~160 to ~350, and finally very few nodes with larger degrees. Degree assortativity coefficient of -0.16. The degree distribution is shown below:

<img src="/images/season9/degree_plots.png" width="600" />

By looking at the random distribution plot for the Journeys season it is obvious that for all three attributes, there are some correlation between the Pokémon that has an edge between them and their attributes:

<img src="/images/season9/random_distributions.png" width="700" />

Pokémon Journeys has 4 communities with sizes [208, 303, 156, 22] with a Modularity of 0.19, and double edge swap yields average modularity of 0.07. This shows a significant difference.

<img src="/images/season9/modularity_distribution.png" width="400" />
