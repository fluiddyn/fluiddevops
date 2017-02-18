dir := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
tag := $(shell date -I'date'| tr -d "[:punct:]")

build:
	cd $(dir) && docker build -t fluiddyn/$(dir):$(tag) .

push:
	cd $(dir) && docker push fluiddyn/$(dir)

run:
	docker run -it fluiddyn/$(dir):$(tag) bash
