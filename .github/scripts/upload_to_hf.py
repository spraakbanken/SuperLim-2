# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "datasets>=4.8.4",
#     "json-arrays>=0.15.0",
# ]
# ///

import csv
import typing as t
from pathlib import Path

import json_arrays
from datasets import ClassLabel, Dataset, Features, List, Value


def main() -> None:

    upload_datasets()


ABSABANK_IMM_FEATURES = Features(
    {
        "id": Value("string"),
        "text": Value("string"),
        "label": Value("float64"),
        "a0": Value("float64"),
        "a1": Value("float64"),
        "a3": Value("float64"),
        "a4": Value("float64"),
        "a6": Value("float64"),
        "a7": Value("float64"),
        "a8": Value("float64"),
        "a9": Value("float64"),
        "a10": Value("float64"),
        "a11": Value("float64"),
    }
)
ARGUMENTATION_SENTENCES_FEATURES = Features(
    {
        "sentence_id": Value("string"),
        "topic": Value("string"),
        "label": ClassLabel(num_classes=3, names=["pro", "con", "non"]),
        "sentence": Value("string"),
    }
)
DALAJ_GED_SUPERLIM = Features(
    {
        "sentence": Value("string"),
        "label": ClassLabel(num_classes=2, names=["correct", "incorrect"]),
        "meta": {
            "confusion_pair": {
                "correction": Value("string"),
                "incorrect_span": Value("string"),
            },
            "data_source": Value("string"),
            "education_level": Value("string"),
            "error_label": Value("string"),
            "error_span": {"start": Value("int64"), "stop": Value("int64")},
            "l1": Value("string"),
        },
    }
)
SWEFAQ_FEATURES = Features(
    {
        "category_id": Value("int64"),
        "question": Value("string"),
        "candidate_answers": List(Value("string")),
        "label": Value("int64"),
        "meta": {
            "category": Value("string"),
            "link": Value("string"),
            "source": Value("string"),
        },
    }
)
SWENLI_FEATURES = Features(
    {
        "id": Value("int64"),
        "premise": Value("string"),
        "hypothesis": Value("string"),
        "label": ClassLabel(names=["entailment", "neutral", "contradiction"]),
    }
)
SWENLI_MATCH_SWEFRACAS_FEATURES = Features(
    **SWENLI_FEATURES.copy(), original_id=Value("int64")
)
SWEWINOGRAD_FEATURES = Features(
    {
        "idx": Value("int64"),
        "text": Value("string"),
        "pronoun": {
            "location": {"start": Value("int64"), "stop": Value("int64")},
            "text": Value("string"),
        },
        "candidate_antecedent": {
            "location": {"start": Value("int64"), "stop": Value("int64")},
            "text": Value("string"),
        },
        "label": ClassLabel(names=["not_coreferring", "coreferring"]),
        "meta": {"snippet_id": Value("string")},
    }
)
SWEWINOGENDER_FEATURES = Features(
    {
        "idx": Value("int64"),
        "premise": Value("string"),
        "hypothesis": Value("string"),
        "label": ClassLabel(names=["neutral", "entailment"]),
        "meta": {
            "occupation_participant": Value("string"),
            "other_participant": Value("string"),
            "pronoun": Value("string"),
            "template_id": Value("string"),
            "tuple_id": Value("string"),
        },
    }
)
SWEWIC_FEATURES = Features(
    {
        "idx": Value("int64"),
        "first": {
            "context": Value("string"),
            "word": {
                "location": {"start": Value("int64"), "stop": Value("int64")},
                "text": Value("string"),
            },
        },
        "second": {
            "context": Value("string"),
            "word": {
                "location": {"start": Value("int64"), "stop": Value("int64")},
                "text": Value("string"),
            },
        },
        "label": ClassLabel(names=["different_sense", "same_sense"]),
        "meta": {
            "first_sense_id": Value("string"),
            "first_source": Value("string"),
            "pos": Value("string"),
            "second_sense_id": Value("string"),
            "second_source": Value("string"),
        },
    }
)


DATASET_CONFIG = {
    "absabank-imm": {
        "dev": {
            "data_file": "absabank-imm/absabank-imm_dev.jsonl",
            "features": ABSABANK_IMM_FEATURES,
        },
        "test": {
            "data_file": "absabank-imm/absabank-imm_test.jsonl",
            "features": ABSABANK_IMM_FEATURES,
        },
        "train": {
            "data_file": "absabank-imm/absabank-imm_train.jsonl",
            "features": ABSABANK_IMM_FEATURES,
        },
    },
    "argumentation-sentences": {
        "dev": {
            "data_file": "argumentation-sentences/argumentation-sentences_dev.jsonl",
            "features": ARGUMENTATION_SENTENCES_FEATURES,
        },
        "test": {
            "data_file": "argumentation-sentences/argumentation-sentences_test.jsonl",
            "features": ARGUMENTATION_SENTENCES_FEATURES,
        },
        "train": {
            "data_file": "argumentation-sentences/argumentation-sentences_train.jsonl",
            "features": ARGUMENTATION_SENTENCES_FEATURES,
        },
    },
    "dalaj-ged-superlim": {
        "dev": {
            "data_file": "dalaj-ged-superlim/dalaj-ged-superlim_dev.jsonl",
            "features": DALAJ_GED_SUPERLIM,
        },
        "test": {
            "data_file": "dalaj-ged-superlim/dalaj-ged-superlim_test.jsonl",
            "features": DALAJ_GED_SUPERLIM,
        },
        "train": {
            "data_file": "dalaj-ged-superlim/dalaj-ged-superlim_train.jsonl",
            "features": DALAJ_GED_SUPERLIM,
        },
    },
    "supersim-superlim-relatedness": {
        "test": {
            "data_file": "supersim-superlim/supersim-superlim-relatedness_test.jsonl",
            "features": None,
        },
        "train": {
            "data_file": "supersim-superlim/supersim-superlim-relatedness_train.jsonl",
            "features": None,
        },
    },
    "supersim-superlim-similarity": {
        "test": {
            "data_file": "supersim-superlim/supersim-superlim-similarity_test.jsonl",
            "features": None,
        },
        "train": {
            "data_file": "supersim-superlim/supersim-superlim-similarity_train.jsonl",
            "features": None,
        },
    },
    "sweanalogy": {
        "test": {
            "data_file": "sweanalogy/sweanalogy_test.jsonl",
            "features": None,
        },
        "train": {
            "data_file": "sweanalogy/sweanalogy_train.jsonl",
            "features": None,
        },
    },
    "swediagnostics": {
        "test": {
            "data_file": "swediagnostics/swediagnostics_test.jsonl",
            "features": Features(
                {
                    "id": Value("int64"),
                    "label": ClassLabel(
                        names=["entailment", "neutral", "contradiction"]
                    ),
                    "premise": Value("string"),
                    "hypothesis": Value("string"),
                    "meta": {
                        "domain": Value("string"),
                        "knowledge": Value("string"),
                        "lexical_semantics": Value("string"),
                        "logic": Value("string"),
                        "predicate_argument_structure": Value("string"),
                    },
                }
            ),
        },
    },
    "swefaq": {
        "dev": {
            "data_file": "swefaq/swefaq_dev.jsonl",
            "features": SWEFAQ_FEATURES,
        },
        "test": {
            "data_file": "swefaq/swefaq_test.jsonl",
            "features": SWEFAQ_FEATURES,
        },
        "train": {
            "data_file": "swefaq/swefaq_train.jsonl",
            "features": SWEFAQ_FEATURES,
        },
    },
    "swenli": {
        "dev": {
            "data_file": "swenli/swenli_dev.jsonl",
            "features": SWENLI_FEATURES,
        },
        "test": {
            "data_file": "swenli/swenli_test.jsonl",
            "features": SWENLI_FEATURES,
        },
        "train": {
            "data_file": "swenli/swenli_train.jsonl",
            "features": SWENLI_FEATURES,
        },
    },
    "swenli-match-swefracas": {
        "test": {
            "data_file": "swenli/swenli_test_match_swefracas.tsv",
            "features": SWENLI_MATCH_SWEFRACAS_FEATURES,
        }
    },
    "sweparaphrase": {
        "dev": {
            "data_file": "sweparaphrase/sweparaphrase_dev.jsonl",
            "features": None,
        },
        "test": {
            "data_file": "sweparaphrase/sweparaphrase_test.jsonl",
            "features": None,
        },
        "train": {
            "data_file": "sweparaphrase/sweparaphrase_train.jsonl",
            "features": None,
        },
    },
    "swesat-synonyms": {
        "test": {
            "data_file": "swesat-synonyms/swesat-synonyms_test.jsonl",
            "features": None,
        },
        "train": {
            "data_file": "swesat-synonyms/swesat-synonyms_train.jsonl",
            "features": None,
        },
    },
    "swewic": {
        "dev": {"data_file": "swewic/swewic_dev.jsonl", "features": SWEWIC_FEATURES},
        "test": {"data_file": "swewic/swewic_test.jsonl", "features": SWEWIC_FEATURES},
        "train": {
            "data_file": "swewic/swewic_train.jsonl",
            "features": SWEWIC_FEATURES,
        },
    },
    "swewinogender": {
        "test": {
            "data_file": "swewinogender/swewinogender_test.jsonl",
            "features": SWEWINOGENDER_FEATURES,
        },
    },
    "swewinograd": {
        "dev": {
            "data_file": "swewinograd/swewinograd_dev.jsonl",
            "features": SWEWINOGRAD_FEATURES,
        },
        "test": {
            "data_file": "swewinograd/swewinograd_test.jsonl",
            "features": SWEWINOGRAD_FEATURES,
        },
        "train": {
            "data_file": "swewinograd/swewinograd_train.jsonl",
            "features": SWEWINOGRAD_FEATURES,
        },
    },
}


def upload_datasets() -> None:
    for name, subset in DATASET_CONFIG.items():
        print(f" === subset: {name} ===")
        for split, split_info in subset.items():
            print(f" === subset: {name} === split: {split} =====")
            data = load_data(Path(split_info["data_file"]))
            ds = Dataset.from_list(
                data, split=split, features=split_info.get("features")
            )
            print(f"{ds=}")
            print(f"{ds.features=}")
            print(f"{ds['label']=}")
            ds.push_to_hub("sbx/superlim-2", config_name=name, split=split)
            print(f" >>> Successfully upload {name} (split={split}) to sbx/superlim-2")


def load_data(path: Path) -> list[dict[str, t.Any]]:
    if path.suffix == ".jsonl":
        return list(json_arrays.load_from_file(path))
    if path.suffix == ".tsv":
        with path.open(newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            return list(reader)
    raise RuntimeError("unknown file type")


if __name__ == "__main__":
    main()
