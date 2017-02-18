dir := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
tag := $(shell date -I'date'| tr -d "[:punct:]")

build:
	cd $(dir) && docker build -t fluiddyn/$(dir):$(tag) .
	docker tag fluiddyn/$(dir):$(tag) fluiddyn/$(dir):latest

push:
	cd $(dir) && docker push fluiddyn/$(dir)

run:
	docker run -it fluiddyn/$(dir):$(tag) bash
