Now that you have your ignore list, here is the "Golden Rule" for Python projects:

Work in your venv: source venv/bin/activate

Install stuff: pip install flask

Save the list: pip freeze > requirements.txt

Git Dance: * git add . (This will now ignore the venv folder automatically!)

git commit -m "Add requirements and flask code"

git push