#!/usr/bin/env bash
if [[ "$(git status --porcelain)" != "" ]]; then
    git config --global user.name 'Ander Fernández'
    git config --global user.email 'afernandez@decidata.es'
    git add data/raw.csv
    git commit -am "Automatically updated raw data"
    git push origin main
else
echo "Nothing to commit..."
fi