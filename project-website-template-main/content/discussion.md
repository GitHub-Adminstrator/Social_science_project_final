---
title: Discussion and conclusion
prev: discussion
---

To first conclude on this project, generally, many aspects went well. Through numerous analyses, this project was able to explore and answer the research questions that laid the foundation for the entire work. These were:

1. What characterizes the network for each season of the Pokémon Anime.

2. Are there any similarities or differences between the various seasons and if so, what are these?

3. How do the seasons themselves separate each other w.r.t. their plots, and are there any similarities or differences between seasons?

Of course, this is does not mean that there are not aspects that could be improved upon. First of all, there is are some obvious descrepancies in something as simple as the Pokémon names when making the networks in section 3. As was pointed out in that section, some of the Pokémon names from PokéAPI had some "extra" information such as the Pokémon "Pumpkaboo" having the name "Pumpkaboo-average". This stems from the Pokémon video game in which Pumpkaboo indeed has different sizes with each having a distinct name corresponding to its size. However, in the anime, this is not the case, and therefore, Pumpkaboo will not appear in any graph. This was the case for a total of 36 Pokémon, and in future work it might be possible to handle these edge cases better such that all Pokémon would be included in the final.

Another interesting aspect would be to include the movies made within each season also. There is a possibility that some of the Pokémon not found in graph would have been there if the movies were included, and this is also something that would be possible in future work.

Furthermore, an interesting thing to research more would be the collocations. We could for example have found all the collocations, where we only use collocation with the name of a Pokémon. Here we would be able to find the significant collocations and thus find which words a Pokémon would be associated with. This would probably result in some attack names or elements connected to the Pokémon, but it would be interesting nonetheless.

Finally, an idea for future work would be to create a network in the "episode" space instead of the "Pokémon" space. In this project, we operate with networks that are made up of Pokémon nodes but an entirely different approach would be to have episode nodes. This would work in such a way that two episodes would be connected iff a Pokémon appears in both or perhaps operate with a threshold such that a number of Pokémon must appear in both episodes such that not every episode is guaranteed to have a connection. Going down this path, it would open up the opportunity for a more interesting community analysis, and would likely tie in better with the text analysis. This would also perhaps make for an interesting text analysis for the different communities, since episodes that end up in the same communities might then share important plot points. This could then be expanded into one big graph of all Pokémon episodes, which ideally would show nice separation between different seasons but hopefully also small conections between these showing how the entire Pokémon Anime is still one big show with good continuance from season to season.