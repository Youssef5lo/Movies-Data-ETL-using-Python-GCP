@echo off
mkdir ml-100k
curl -o ml-100k.zip http://files.grouplens.org/datasets/movielens/ml-100k.zip
tar -xf ml-100k.zip -C ml-100k
