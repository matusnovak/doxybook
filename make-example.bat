cd example
doxygen Doxyfile
cd ..
python -m doxybook -i example/temp/xml -o example/docs/api -s example/SUMMARY.md
