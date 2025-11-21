#!/bin/bash
# wget_fineweb_11_20.sh (updated for speed)
mkdir -p fineweb_test_dump
cd fineweb_test_dump
echo "Downloading FineWeb shard via HF Mirror (faster for Asia)..."

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00011.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00012.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00013.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00014.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00015.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00016.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00017.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00018.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00019.parquet?download=true"

wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00020.parquet?download=true"
