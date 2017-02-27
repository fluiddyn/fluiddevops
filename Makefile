dir := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
tag := $(shell date -I'date'| tr -d "[:punct:]")

build:
	cd $(dir) && docker build -t fluiddyn/$(dir) .
	docker tag fluiddyn/$(dir) fluiddyn/$(dir):$(tag)

push:
	docker push fluiddyn/$(dir)

run:
	docker run -it fluiddyn/$(dir) bash
