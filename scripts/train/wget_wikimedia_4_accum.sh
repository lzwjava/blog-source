#!/bin/bash
# Quick test: download multiple Wikipedia dump chunks (~5+ GB total)
# Enough for 20–30 GB clean text — perfect for pipeline testing

mkdir -p wikipedia_test_dump
cd wikipedia_test_dump

echo "Downloading 2 Wikipedia dumps for testing..."

wget -c https://mirror.accum.se/mirror/wikimedia.org/dumps/enwiki/20251101/enwiki-20251101-pages-articles2.xml-p41243p151573.bz2
wget -c https://mirror.accum.se/mirror/wikimedia.org/dumps/enwiki/20251101/enwiki-20251101-pages-articles3.xml-p151574p311329.bz2

echo "Done! You now have 2 data files"
echo "Total download size: ~5+ GB"
echo "To extract clean text, you can now run wikiextractor:"
echo "   wikiextractor --processes 8 -o extracted/ enwiki-20251101-pages-articles2.xml-p41243p151573.bz2"
echo "   wikiextractor --processes 8 -o extracted/ enwiki-20251101-pages-articles3.xml-p151574p311329.bz2"