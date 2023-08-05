import json
import os
import re

import torch
from torchtext.data import get_tokenizer

from datasets import FEATURE_MAPS_KEYS, TOKENS_KEY

SOS = 'startofsentence'
EOS = 'endofsentence'


class GPRConceptsDataset:
    def __init__(self):
        if os.getenv("GPR_DATASET_CONCEPT_DETECTION") is None:
            raise RuntimeError('Dataset path must be set up.')
        root = os.environ['GPR_DATASET_CONCEPT_DETECTION']
        feature_maps_dir = os.path.join(root, FEATURE_MAPS_KEYS)
        self.descriptions_path = os.path.join(root, 'categories.json')
        self.feature_maps_list = [os.path.join(feature_maps_dir, file_name) for file_name in sorted(os.listdir(feature_maps_dir))]

        # load descriptions
        with open(self.descriptions_path, 'r') as json_file:
            self._descriptions = json.load(json_file)

        for key, value in self._descriptions.items():
            self._descriptions[key] = re.sub(r"[^a-zA-Z0-9]+", ' ', value.lower())

        # get text corpus
        text_corpus = list(self._descriptions.values())

        # init tokenizer
        self._tokenizer = get_tokenizer('spacy', language='en_core_web_sm')

        # tokenize text corpus
        self._tokenized_corpus = [self._tokenizer(text) for text in text_corpus]

        # init vocab
        self._vocab = [SOS, EOS]

        # create sos and eos indices
        self.sos_idx = self._vocab.index(SOS)
        self.eos_idx = self._vocab.index(EOS)

        # form vocab
        for sentence in self._tokenized_corpus:
            for token in sentence:
                if token not in self._vocab:
                    self._vocab.append(token)

    def __len__(self):
        return len(self.feature_maps_list)

    def __getitem__(self, idx):
        feature_map = torch.load(self.feature_maps_list[idx], map_location=torch.device('cpu'))
        feature_map_class = int(os.path.basename(self.feature_maps_list[idx]).split('_')[0])
        description = self._descriptions[str(feature_map_class)]
        tokenized = self._tokenizer(f'{SOS} {description} {EOS}')
        tokenized_tensor = torch.tensor([self._vocab.index(token) for token in tokenized], dtype=torch.int64)
        d, h, w = feature_map.shape
        return {FEATURE_MAPS_KEYS: feature_map.reshape(h * w, d), TOKENS_KEY: tokenized_tensor}
