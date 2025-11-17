#!/bin/bash
# wget_fineweb_1.sh (updated for speed)
mkdir -p fineweb_test_dump
cd fineweb_test_dump
echo "Downloading FineWeb shard via HF Mirror (faster for Asia)..."

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00001.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00002.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00003.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00004.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00005.parquet?download=true"
