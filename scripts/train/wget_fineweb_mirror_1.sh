#!/bin/bash
# wget_fineweb_1.sh (updated for speed)
mkdir -p fineweb_test_dump
cd fineweb_test_dump
echo "Downloading FineWeb shard via HF Mirror (faster for Asia)..."

# Replace huggingface.co with hf-mirror.com
wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

echo "Done! Shard size: ~500MB–1GB"
echo "For more shards, loop over e.g., 000_00001.parquet, etc."
echo "To load in Python: from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"