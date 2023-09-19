build:
	cd frontend && npm run build && cd ../..
	python setup.py sdist
run:
	DEVELOP_MODE=True streamlit run --theme.base light __init__.py
run-frontend:
	cd frontend && npm run start

