---
annotations_creators:
  - other
configs:
  - config_name: absabank-imm
    data_files:
      - path: data/absabank-imm/absabank-imm_train.tsv
        split: train
      - path: data/absabank-imm/absabank-imm_test.tsv
        split: test
      - path: data/absabank-imm/absabank-imm_dev.tsv
        split: dev
    names:
      - id
      - text
      - label
      - a0
      - a1
      - a3
      - a4
      - a6
      - a7
      - a8
      - a9
      - a10
      - a11
  - config_name: argumentation-sentences
    data_files:
      - path: data/argumentation-sentences/argumentation-sentences_test.tsv
        split: test
      - path: data/argumentation-sentences/argumentation-sentences_dev.tsv
        split: dev
      - path: data/argumentation-sentences/argumentation-sentences_train.tsv
        split: train
    names:
      - sentence_id
      - topic
      - label
      - sentence
  - config_name: dalaj-ged-superlim
    data_files:
      - path: data/dalaj-ged-superlim/dalaj-ged-superlim_test.jsonl
        split: test
      - path: data/dalaj-ged-superlim/dalaj-ged-superlim_train.jsonl
        split: train
      - path: data/dalaj-ged-superlim/dalaj-ged-superlim_dev.jsonl
        split: dev
    names:
      - sentence
      - label
      - meta
  - config_name: supersim-superlim-relatedness
    data_files:
      - path: data/supersim-superlim/supersim-superlim-relatedness_test.tsv
        split: test
      - path: data/supersim-superlim/supersim-superlim-relatedness_train.tsv
        split: train
    names:
      - word_1
      - word_2
      - a1
      - a2
      - a3
      - a4
      - a5
      - label
  - config_name: supersim-superlim-similarity
    data_files:
      - path: data/supersim-superlim/supersim-superlim-similarity_test.tsv
        split: test
      - path: data/supersim-superlim/supersim-superlim-similarity_train.tsv
        split: train
    names:
      - word_1
      - word_2
      - a1
      - a2
      - a3
      - a4
      - a5
      - label
  - config_name: sweanalogy
    data_files:
      - path: data/sweanalogy/sweanalogy_train.tsv
        split: train
      - path: data/sweanalogy/sweanalogy_test.tsv
        split: test
    names:
      - pair1_element1
      - pair1_element2
      - pair2_element1
      - label
      - category
  - config_name: swediagnostics
    data_files:
      - path: data/swediagnostics/swediagnostics_test.tsv
        split: test
    names:
      - id
      - label
      - premise
      - hypothesis
      - meta
  - config_name: swedn
    data_files:
      - path: data/swedn/swedn_add_info.tsv
        split: stats
  - config_name: swefaq
    data_files:
      - path: data/swefaq/swefaq_test.jsonl
        split: test
      - path: data/swefaq/swefaq_dev.jsonl
        split: dev
      - path: data/swefaq/swefaq_train.jsonl
        split: train
    names:
      - category_id
      - question
      - candidate_answers
      - label
      - meta
  - config_name: swenli
    data_files:
      - path: data/swenli/swenli_dev.tsv
        split: dev
      - path: data/swenli/swenli_train.tsv
        split: train
      - path: data/swenli/swenli_test.tsv
        split: test
    names:
      - id
      - premise
      - hypothesis
      - label
  - config_name: swenli_match_swefracas
    data_files:
      - path: data/swenli/swenli_test_match_swefracas.tsv
        split: test
    names:
      - id
      - premise
      - hypothesis
      - label
      - original_id
  - config_name: sweparaphrase
    data_files:
      - path: data/sweparaphrase/sweparaphrase_dev.tsv
        split: dev
      - path: data/sweparaphrase/sweparaphrase_train.tsv
        split: train
      - path: data/sweparaphrase/sweparaphrase_test.tsv
        split: test
    names:
      - genre
      - file
      - sentence_1
      - sentence_2
      - label
  - config_name: swesat-synonyms
    data_files:
      - path: data/swesat-synonyms/swesat-synonyms_test.jsonl
        split: test
      - path: data/swesat-synonyms/swesat-synonyms_train.jsonl
        split: train
    names:
      - id
      - item
      - candidate_answers
      - label
      - meta
  - config_name: swewic
    data_files:
      - path: data/swewic/swewic_train.jsonl
        split: train
      - path: data/swewic/swewic_test.jsonl
        split: test
      - path: data/swewic/swewic_dev.jsonl
        split: dev
    names:
      - idx
      - first
      - second
      - label
      - meta
  - config_name: swewinogender
    data_files:
      - path: data/swewinogender/swewinogender.jsonl
        split: train
      - path: data/swewinogender/swewinogender_test.jsonl
        split: test
    names:
      - idx
      - premise
      - hypothesis
      - label
      - meta
  - config_name: swewinograd
    data_files:
      - path: data/swewinograd/swewinograd_test.jsonl
        split: test
      - path: data/swewinograd/swewinograd_train.jsonl
        split: train
      - path: data/swewinograd/swewinograd_dev.jsonl
        split: dev
    names:
      - idx
      - text
      - pronoun
      - candidate_antecedent
      - label
      - meta
language:
  - sv
language_creators:
  - other
multilinguality:
  - monolingual
pretty_name: A standardized suite for evaluation and analysis of Swedish natural language
  understanding systems.
size_categories:
  - unknown
source_datasets: []
task_categories:
  - multiple-choice
  - text-classification
  - question-answering
  - sentence-similarity
  - token-classification
  - summarization
task_ids:
  - sentiment-analysis
  - acceptability-classification
  - closed-domain-qa
  - word-sense-disambiguation
  - coreference-resolution
---

# Dataset Card for Superlim-2

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [The official homepage of Språkbanken](https://spraakbanken.gu.se/resurser/superlim/)
- **Repository:**
- **Paper:**[SwedishGLUE – Towards a Swedish Test Set for Evaluating Natural Language Understanding Models](https://gup.ub.gu.se/publication/299130?lang=sv)
- **Leaderboard:** https://lab.kb.se/leaderboard/
- **Point of Contact:**[sb-info@svenska.gu.se](sb-info@svenska.gu.se)

### Dataset Summary

SuperLim 2.0 is a continuation of SuperLim 1.0, which aims for a standardized suite for evaluation and analysis of Swedish natural language understanding systems. The projects is inspired by the GLUE/SuperGLUE projects from which the name is derived: "lim" is the Swedish translation of "glue".

Since Superlim 2.0 is a collection of datasets, we refer for information about dataset structure, creation, social impact etc. to the specific data cards or documentation sheets in the official GitHub repository: https://github.com/spraakbanken/SuperLim-2/

### Supported Tasks and Leaderboards

See our leaderboard: https://lab.kb.se/leaderboard/

### Languages

Swedish

## Dataset Structure

### Data Instances

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Data Fields

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Data Splits

Most datasets have a train, dev and test split. However, there are a few (`supersim`, `sweanalogy` and `swesat-synonyms`) who only have a train and test split. The diagnostic tasks `swediagnostics` and `swewinogender` only have a test split, but they could be evaluated on models trained on `swenli` since they are also NLI-based.

## Dataset Creation

### Curation Rationale

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Source Data

#### Initial Data Collection and Normalization

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

#### Who are the source language producers?

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Annotations

#### Annotation process

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

#### Who are the annotators?

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Personal and Sensitive Information

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

## Considerations for Using the Data

### Social Impact of Dataset

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Discussion of Biases

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Other Known Limitations

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Dataset Curators

See individual datasets: https://github.com/spraakbanken/SuperLim-2/

### Licensing Information

All datasets constituting Superlim are available under Creative Commons licenses (CC BY 4.0, 8144 CC BY-SA 4.0, respectively).

### Citation Information

To cite as a whole, use the standard reference. If you use or reference individual resources, cite the references specific for these resources:

Standard reference:

Superlim: A Swedish Language Understanding Evaluation Benchmark (Berdicevskis et al., EMNLP 2023)

```

@inproceedings{berdicevskis-etal-2023-superlim,
    title = "Superlim: A {S}wedish Language Understanding Evaluation Benchmark",
    author = {Berdicevskis, Aleksandrs  and
      Bouma, Gerlof  and
      Kurtz, Robin  and
      Morger, Felix  and
      {\"O}hman, Joey  and
      Adesam, Yvonne  and
      Borin, Lars  and
      Dann{\'e}lls, Dana  and
      Forsberg, Markus  and
      Isbister, Tim  and
      Lindahl, Anna  and
      Malmsten, Martin  and
      Rekathati, Faton  and
      Sahlgren, Magnus  and
      Volodina, Elena  and
      B{\"o}rjeson, Love  and
      Hengchen, Simon  and
      Tahmasebi, Nina},
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.506",
    doi = "10.18653/v1/2023.emnlp-main.506",
    pages = "8137--8153",
    abstract = "We present Superlim, a multi-task NLP benchmark and analysis platform for evaluating Swedish language models, a counterpart to the English-language (Super)GLUE suite. We describe the dataset, the tasks, the leaderboard and report the baseline results yielded by a reference implementation. The tested models do not approach ceiling performance on any of the tasks, which suggests that Superlim is truly difficult, a desirable quality for a benchmark. We address methodological challenges, such as mitigating the Anglocentric bias when creating datasets for a less-resourced language; choosing the most appropriate measures; documenting the datasets and making the leaderboard convenient and transparent. We also highlight other potential usages of the dataset, such as, for instance, the evaluation of cross-lingual transfer learning.",
}


```

Thanks to [Felix Morger](https://github.com/felixhultin) for adding this dataset.
