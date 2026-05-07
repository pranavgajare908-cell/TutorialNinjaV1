python -m pip install pytest
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -s -v testCases -m "regression"