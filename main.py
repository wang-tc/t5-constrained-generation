import torch
import argparse
import glob
import os
import json
import time
import logging
import random
import re
import nltk
import pytorch_lightning as pl
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
from nltk.tokenize import sent_tokenize
from itertools import chain
from string import punctuation
from transformers import (
        AdamW,
        T5ForConditionalGeneration,
        T5Tokenizer,
        get_linear_schedule_with_warmup
        )

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(42)



