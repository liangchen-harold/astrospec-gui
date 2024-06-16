.PHONY: build env run

all: run

env:
	pip install -U astrospec async-tkinter-loop pyinstaller

build:
	# pyinstaller --onefile --noconsole main.py -n astrospec -i astrospec-256.png
	pyinstaller astrospec.spec

run:
	python main.py

clean:
	pip freeze | xargs pip uninstall -y
