#!/bin/bash
# Quick test: download only 5 Wikipedia multistream chunks (~2.3 GB total)
# Enough for 10–15 GB clean text — perfect for pipeline testing

mkdir -p wikipedia_test_dump
cd wikipedia_test_dump

echo "Downloading 4 Wikipedia chunks for testing..."

wget -c https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2
wget -c https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/enwiki-20251101-pages-articles-multistream2.xml-p41243p65958.bz2
wget -c https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/enwiki-20251101-pages-articles-multistream3.xml-p65959p111399.bz2
wget -c https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/enwiki-20251101-pages-articles-multistream4.xml-p111400p151573.bz2

echo "Done! You now have 4 data files"
echo "Total download size: ~2.3 GB"
echo "To extract clean text, you can now run wikiextractor on the whole folder:"
echo "   wikiextractor --processes 8 -o extracted/ *.bz2"