python setup.py sdist
python setup.py bdist_wheel
python -m twine upload dist/*
