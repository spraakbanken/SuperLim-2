#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Enable Debug mode with TRACE=1 ./upload_to_hf.sh
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./upload_to_hf.sh

Upload all data folders in thsi repo to Huggingface sbx/superlim-2.
You need to call `hf auth login` first.

'
    exit
fi

cd "$(dirname "$0")"

DATASET_ID=sbx/superlim-2

function upload_file {
    local folder="$1"
    local hf_folder="$2"
    local path="$3"

    hf upload "${DATASET_ID}" --repo-type dataset "${folder}/${path}" "data/${hf_folder}/${path}"
}

function upload_folder {
    local folder="$1"
    local hf_folder="$2"
    local paths=("${@:3}")

    echo "Uploading '${folder}' ..."
    for path in "${paths[@]}"; do
        upload_file "${folder}" "${hf_folder}" "${path}"
    done
}

main() {
    folder=absabank-imm
    paths=( absabank-imm_dev.tsv absabank-imm_test.tsv absabank-imm_train.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=argumentation-sentences
    paths=( argumentation-sentences_dev.tsv argumentation-sentences_test.tsv argumentation-sentences_train.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=dalaj-ged-superlim
    paths=( dalaj-ged-superlim_dev.jsonl dalaj-ged-superlim_test.jsonl dalaj-ged-superlim_train.jsonl )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=supersim-superlim
    hf_folder=supersim-superlim-relatedness
    paths=( supersim-superlim-relatedness_test.tsv supersim-superlim-relatedness_train.tsv )
    upload_folder "${folder}" "${hf_folder}" "${paths[@]}"

    folder=supersim-superlim
    hf_folder=supersim-superlim-similarity
    paths=( supersim-superlim-similarity_test.tsv supersim-superlim-similarity_train.tsv )
    upload_folder "${folder}" "${hf_folder}" "${paths[@]}"

    folder=sweanalogy
    paths=( sweanalogy_test.tsv sweanalogy_train.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swediagnostics
    paths=( swediagnostics_test.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swedn
    paths=( swedn_add_info.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swefaq
    paths=( swefaq_dev.jsonl swefaq_test.jsonl swefaq_train.jsonl )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swenli
    paths=( swenli_dev.tsv swenli_test.tsv swenli_train.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swenli
    hf_folder=swenli-match-swefracas
    paths=( swenli_test_match_swefracas.tsv )
    upload_folder "${folder}" "${hf_folder}" "${paths[@]}"

    folder=sweparaphrase
    paths=( sweparaphrase_dev.tsv sweparaphrase_test.tsv sweparaphrase_train.tsv )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swesat-synonyms
    paths=( swesat-synonyms_test.jsonl swesat-synonyms_train.jsonl )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swewic
    paths=( swewic_dev.jsonl swewic_test.jsonl swewic_train.jsonl )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swewinogender
    paths=( swewinogender_test.jsonl swewinogender.jsonl )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    folder=swewinograd
    paths=( swewinograd_dev.jsonl swewinograd_test.jsonl swewinograd_train.jsonl )
    upload_folder "${folder}" "${folder}" "${paths[@]}"

    echo "Uploading README.md ..."
    hf upload "${DATASET_ID}" --repo-type dataset huggingface.readme.md README.md
}

main "$@"
