#!/bin/bash
# Quick test: download only 5 Wikipedia multistream chunks (~2.3 GB total)
# Enough for 10–15 GB clean text — perfect for pipeline testing

mkdir -p wikipedia_test_dump
cd wikipedia_test_dump

echo "Downloading 5 Wikipedia chunks for testing..."

wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p1p41242.bz2
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles2.xml-p41243p65958.bz2
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles3.xml-p65959p111399.bz2
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles4.xml-p111400p151573.bz2
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles5.xml-p151574p201573.bz2

echo "Done! You now have 5 data + 5 index files."
echo "Total download size: ~2.3 GB"
echo "To extract clean text, you can now run wikiextractor on the whole folder:"
echo "   wikiextractor --processes 8 -o extracted/ *.bz2"