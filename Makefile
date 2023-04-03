IMAGENAME=localchat

it: serve

build:
	docker build -t $(IMAGENAME) docker

data/index.json:
	. $$HOME/.openai.rc; docker run --rm -e OPENAI_API_KEY=$$OPENAI_API_KEY -v `pwd`/data:/root/data -v `pwd`/docs:/root/docs $(IMAGENAME) python3 genmodel.py

serve: build data/index.json
	. $$HOME/.openai.rc; docker run -it --rm -e OPENAI_API_KEY=$$OPENAI_API_KEY -v `pwd`/data:/root/data $(IMAGENAME) python3 serve.py

