#!/usr/bin/env bash
git config --global user.name 'Ander Fernández'
git config --global user.email 'afernandez@decidata.es'
git add data/raw.csv
git commit -m "Automatically updated raw data"
git push origin main
