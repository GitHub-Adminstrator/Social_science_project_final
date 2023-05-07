---
title: Text analysis
prev: network-analysis
next: "discussion"
---

## Seasons: [1](#season-1) [2](#season-2) [3](#season-3) [4](#season-4) [5](#season-5) [6](#season-6) [7](#season-7) [8](#season-8) [9](#season-9) [All](#all-seasons)

In this section we will be analyzing the text of the Pokémon episodes for each season. We will be looking at the most
common words for each season using word clouds.

# **Concepts used**
The concepts used in the analysis will be described in the sections below.

## **Tokenization**
Tokenization is the process of splitting text into smaller pieces, called tokens. This is done to make the text easier
to analyze. In this project we will be using the `nltk` library to tokenize the text.

The steps we are going to do are as follows:
1. Split into word tokens with NLTK
2. Convert all tokens to lowercase
3. Remove all punctuation and other special characters
4. Remove all numbers/digits
5. Remove spaces
6. Convert all characters to ascii characters to remove all japanese and otherwise special characters
7. Remove all stopwords

This tokenizer makes sure, that we have all the words in same format. Moreover, it seems that in the text that there is
quite a lot of Japanese spread throughout, and to combat that (since we cannot analyse Japanese text), we convert all
the text to ASCII, which only has A-Z. This makes sure, that we get understandable collocations, wordclouds etc.

## **Zipf's law**
Zipf's law describes the frequency of words in a text. It states that the frequency of a word is inversely proportional
to its rank in the frequency table. This means that the most frequent word will occur approximately twice as often as
the second most frequent word, three times as often as the third most frequent word, etc.

This means that we use a log-log plot to visualize the frequency of words. This is done by taking the log of the rank
and the log of the frequency. This is done to make the plot more linear, since the frequency of words is not linear.

## **Bigrams/Collocation and chi-squared test**
Bigrams are pairs of words that occur together in a text. Collocations are bigrams that occur more often than expected.
We're simply creating these collocations by using the tokens and their neighbour, thus, a bigram is itself and its
previous and next neighbour.

We will be using the chi-squared test to find the collocations. This means that we need to create contingency tables
for each bigram first, and then use that to calculate the p-value. The threshold of significant that we're going to use
will be 0.001. This means that we will only be looking at collocations that are significant at the 0.1% level.

## **Discriminative word analysis**
Discriminative word analysis is a self invented term, which we use to describe the process of removing words from a set
of words, if they are present in another set of words. This is done to make sure that we only analyze words that are
discriminative or different for a season.

Here we will define the process. We will do this by calculating counts for each season for each word, which we will have
in dicts (already calculated in the previous cell), and then we will perform the analysis, which is these steps:
1. Define a set of words $W_{current}$ that we want to analyze  for a season
2. Loop through all other seasons and for each season, take top $K = 100$ words with the highest score , defined as $W_{topK}$
3. For each word $W_{topK}$ remove it from $W_{current}$ if it is present in $W_{current}$

This makes sure, that the top words we analyze for a season, are not present in the other seasons. This is done to make
sure that we only analyze words that are discriminative or different for a season.

## **Wordclouds**
Finally, we will create wordclouds from the tokens. This is done by taking the tokens and their frequency and then
creating a wordcloud from that. We will be using the `wordcloud` library to create the wordclouds.

# **Analysis**
After we have introduced the concepts, we will now perform the analysis. It will be split into each season, and then
finally a combined analysis of all seasons.

## **Zipf's law**
We will start by examining if our text corpus follows Zipf's law. We will do this by plotting the frequency of words:

![Zipf's law per season](/zipf/per_season.png)

We can see that the data follows Zipf's law, since the plot is pretty linear.

Now we will plot the frequency of words for all seasons combined:

![Zipf's law all seasons](/zipf/all.png)

Finally, we can see for all seasons combined, that the data also follows Zipf's law.

## **Bigrams/Collocation and chi-squared test**
Now we will look at the collocations for each season. First we will look at a summary of the number of bigrams:

| Season           | Number of bigrams with p-value < 0.001 | Number of bigrams | Ratio  |
|------------------|----------------------------------------|-------------------|--------|
| Indigo League    | 23829                                  | 35769             | 66.62% |
| Orange Islands   | 10134                                  | 14518             | 69.80% |
| Johto League     | 47145                                  | 76464             | 61.66% |
| Pokémon Journeys | 44493                                  | 68654             | 64.81% |
| Hoenn League     | 44370                                  | 74468             | 59.58% |
| Kalos League     | 41087                                  | 70175             | 58.55% |
| Unova League     | 49131                                  | 84288             | 58.29% |
| Alola League     | 42532                                  | 70513             | 60.32% |
| Sinnoh League    | 58263                                  | 105090            | 55.44% |

As one can see in the table, the ratio of bigrams with p-value < 0.001 is pretty high for all seasons. This means that
there are a lot of collocations in the text. This is probably due to the fact that the text is a plot from a TV show,
which means that there are a lot of repeated words and phrases.

### **Indigo League**
(proof, victory),
(etiquette, spying),
(capacity, extra),
(rail, cart),
(cares, nine),
(rescued, rapids),
(fifth, round),
(reeling, amidst),
(shoots, suction),
(pin, missile)

Some of these collocations are quite interesting. For example, "proof, victory" is a collocation, which is probably
because the characters are trying to prove themselves to be the best. Even though some collocations are quite obvious,
such as "rail, cart", there are also some nonsensical collocations, such as "cares, nine". They do not seem to
mean anything.

### **Orange Islands**
(port, located),
(targets, equal),
(words, reminisces),
(angered, revelation),
(checks, pokedex),
(balance, scratching),
(size, lighter),
(team, rocket),
(food, shipment),
(th, episode)

Once again some of these collocations seem to make sense. Fx "checks, pokedex" is an obvious collocation, since
the characters are checking their pokedex (A pokedex is a small computer on which, you are able to look up
pokemons), or "team, rocket", which is the name of the team of the antagonists. However, there are also some
nonsensical collocations, such as

### **Johto League**
(host, guest)
(tension, teams),
(smiles, encouragingly),
(questioned, established),
(canteens, request),
(defense, curl),
(bask, success),
(overloads, pikapower),
(intent, tipping),
(pretending, tv)

In _Johto League_ we can see some of the victory and battling themes are quite obvious in the collocations.
For example "tension, teams" is a collocation, which is probably due to the fact that the characters are battling
and have tense interactions and "bask, success" is also another collocation showing the victory theme.

### **Pokémon Journeys**
(contains, transparent),
(extremely, tasty),
(awaken, slumbering),
(eight, tournament),
(emerged, victorious),
(number, incomplete),
(natural, habitat),
(swell, eaters),
(calculations, pointed),
(bringing, copious)

We can once again see the victory theme in the "emergered, victorious" collocation. However, there are also some
nonsensical collocations, such as "contains, transparent" and "swell, eaters".

But for this season, it seems that there is also a theme of food, since there are some collocations related to
food such as "extremely, tasty" and "swell, eaters".

### **Hoenn League**
(arrive, scene),
(crooked, salesman),
(results, announced),
(milk, drake),
(puffy, cheeks),
(young, girl),
(regarding, tomorrow),
(waving, goodbye),
(albert, einstein),
(hijacks, cable)

Most of the collocations for Hoenn are quite nonsensical, such as "albert, einstein" and "hijacks, cable", and
do not seem to have anything to do with Pokémon or its themes. However, we can see a theme of competition in the
collocation "results, announced".

### **Kalos League**
(sign, respect),
(excites, hugely),
(destructive, destruction),
(accustomed, aid),
(lower, body),
(volunteers, provide),
(unfamiliar, chesto),
(observation, chamber),
(commemorating, tenth),
(jay, candy)

For this season we cannot really extract many themes, besides maybe destruction from "destructive, destruction",
since the rest of the do not make any sense without context.

### **Unova League**
(recoiling, presence),
(brushes, hind),
(mamoswine, overcame),
(abyssal, ruins),
(tumbling, steep),
(meanwhile, team),
(researchers, monumental),
(matchups, announced),
(abandon, costumes),
(realized, whereabouts)

In _Unova League_ we see the theme of victory and competition in the collocation "matchups, announced". However,
there are also the collocations "recoiling, presence" and "abyssal, ruins", which seem to be quite "dark" words.

### **Alola League**
(impressive, offense),
(predicts, chances),
(splits, merges),
(produce, largest),
(dust, clears),
(maniacal, mood),
(uncharacteristic, behaviour),
(swatting, vengeful),
(ornate, cabinet),
(tape, recorders)

The first collocation which is interesting is "impressive, offense", which is probably from the theme of battling
with Pokémon, where one trainer is complementing the other trainer's Pokémon.

### **Sinnoh League**
(awkward, interview),
(obvious, disdain),
(blank, range),
(discuss, beliefs),
(cease, rivalry),
(older, classmate),
(sting, bombardment),
(lighting, repeatedly),
(ordinary, dream),
(manipulative, spike)

In _Sinnoh League_ we can see the theme of rivalry in the collocation "cease, rivalry", which is quite obvious in
this season.

### **Collocation analysis conclusion**
From the collocation analysis we can see that there are some themes which are quite obvious in the collocations,
such as victory, battling, rivalry and competition. However, throughout the seasons there are quite a lot of 
collocations that does not make sense.

Overall, we can say that the collocation analysis provided some confirmation in the themes of the seasons, but
it is definitely not a perfect method for extracting themes from the text.

## **Wordclouds**
Now we are going to plot all the wordclouds for each season, and finally one plot for all the seasons combined.
We are plotting both the plain counts and the discriminatory counts wordclouds.

We are not going to describe every wordcloud but rather just show them, and then describe the overall important in a
conclusion.

### **Indigo League**
![Indigo League - wordcloud](/wordclouds/Indigo_League_mask_coloring_discriminatory.png)

### **Orange Islands**
![Orange Islands - wordcloud](/wordclouds/Orange_Islands_mask_coloring_discriminatory.png)

### **Johto League**
![Johto League - wordcloud](/wordclouds/Johto_League_mask_coloring_discriminatory.png)

### **Pokémon Journeys**
![Pokémon Journeys - wordcloud](/wordclouds/Pokémon_Journeys_mask_coloring_discriminatory.png)

### **Hoenn League**
![Hoenn League - wordcloud](/wordclouds/Hoenn_League_mask_coloring_discriminatory.png)

### **Kalos League**
![Kalos League - wordcloud](/wordclouds/Kalos_League_mask_coloring_discriminatory.png)

### **Unova League**
![Unova League - wordcloud](/wordclouds/Unova_League_mask_coloring_discriminatory.png)

### **Alola League**
![Alola League - wordcloud](/wordclouds/Alola_League_mask_coloring_discriminatory.png)

### **Sinnoh League**
![Sinnoh League - wordcloud](/wordclouds/Sinnoh_League_mask_coloring_discriminatory.png)

### **All seasons**
![All seasons - wordcloud](/wordclouds/All_seasons_mask_coloring.png)

### **Wordclouds conclusion**
From the counts wordclouds we can see that there are some themes which are quite obvious in the wordclouds, such as the names
of the most prominent characters and Pokémon, such as Ash, Pikachu, Misty, Brock, Team Rocket, etc. This shows that the
wordclouds are quite good at extracting the most prominent words from the text. But we can also see that those words do
not really tell us anything about the themes of the seasons. Furthermore, this is probably also caused by the fact that
Pokémon series is quite simplistic in its language and the show is quite repetitive in its language and structure.

From the discriminative counts wordclouds, we mostly see the characters and Pokémon names, that are mostly only
mentioned in that specific season. In every season Ash (the protagonist) have some sort of new companion or rival
and a new Pokémon. This is clearly defined in the wordclouds, since we can see that the names of the characters and
Pokémon are the most prominent words in the discriminative counts wordclouds. For example in _Pokémon Journeys_ we
can clearly see the character Goh and his Pokémon Raboot, which are not mentioned in any other season.

Overall, we can say that the wordclouds are quite good at extracting the most prominent words from the text, but they
are not good at extracting the themes of the seasons. We can mostly see the difference in the characters and Pokémon
that are used every season.