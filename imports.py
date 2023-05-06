# imports
import os
import pickle
import random
import re
import warnings
from collections import Counter, defaultdict

import community as community_louvain
import matplotlib.pyplot as plt
import networkx as nx
import netwulf as nw
import nltk
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from scipy.stats import chi2_contingency, ttest_1samp
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm.auto import tqdm
from wordcloud import WordCloud

warnings.filterwarnings("ignore")
