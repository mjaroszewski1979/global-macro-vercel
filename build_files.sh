#!/bin/bash

echo "BUILD START"

# Zainstaluj zależności
python3.9 -m pip install -r requirements.txt

# Zbierz statyczne pliki do katalogu 'static'
python3.9 manage.py collectstatic --noinput

# Utwórz katalog wynikowy dla Vercel
mkdir -p staticfiles_build

# Skopiuj zawartość katalogu static do katalogu wynikowego
cp -r static/* staticfiles_build/

echo "BUILD END"

