cd example
doxygen Doxyfile
cd ..
python -m doxybook -t gitbook -i example/temp/xml -o example/gitbook/api -s example/gitbook/SUMMARY.md
python -m doxybook -t vuepress -i example/temp/xml -o example/vuepress/api
