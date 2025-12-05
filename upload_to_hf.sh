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

main() {
    data_folders=( absabank-imm swediagnostics swesat-synonyms argumentation-sentences swedn swewic dalaj-ged-superlim swefaq swewinogender supersim-superlim swenli swewinograd sweanalogy sweparaphrase )
    for data_folder in "${data_folders[@]}"
    do
        :
        echo "Uploading '${data_folder}' to HuggingFace '${DATASET_ID}'"
        hf upload ${DATASET_ID} --repo-type dataset ${data_folder} data/${data_folder}
    done
    echo do awesome stuff
}

main "$@"
