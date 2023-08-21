build:
	cd streamlit_chemical_flow/frontend && npm run build && cd ../..
	python setup.py sdist
run:
	DEVELOP_MODE=True streamlit run streamlit_chemical_flow/__init__.py
run-frontend:
    cd streamlit_chemical_flow/frontend && npm run start

