dir := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
tag := $(shell date -I'date'| tr -d "[:punct:]")

start:
	systemctl start docker

build:
	cd $(dir) && docker build -t fluiddyn/$(dir) .
	docker tag fluiddyn/$(dir) fluiddyn/$(dir):$(tag)

onbuild:
	cd $(dir) && docker build -t fluiddyn/$(dir):onbuild -f Dockerfile.onbuild .

push:
	docker push fluiddyn/$(dir)

run:
	docker run -it fluiddyn/$(dir) bash

run_travis:
	docker run -it travisci/ci-python bash -c "su - travis"

run_travis_old:
	docker run -it quay.io/travisci/travis-python bash -c "su - travis"
