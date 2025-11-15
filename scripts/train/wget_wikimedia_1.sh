#!/bin/bash
# Quick test: download only 1 Wikipedia multistream chunk (~460 MB)
# Perfect for pipeline testing

mkdir -p wikipedia_test_dump
cd wikipedia_test_dump

echo "Downloading 1 Wikipedia chunk for testing..."

wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p1p41242.bz2

# Also grab the matching index file (needed by wikiextractor and most tools)
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index1.xml-p1p41242.bz2

echo "Done! You now have 1 data + 1 index file."
echo "Total download size: ~460 MB"
echo "To extract clean text, you can now run wikiextractor on the whole folder:"
echo "   wikiextractor --processes 8 -o extracted/ *.bz2"