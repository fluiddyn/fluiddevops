image := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
tag := $(shell date -I'date'| tr -d "[:punct:]")

start:
	systemctl start docker

dockermako:
	python make_files_with_mako.py
	
cleanmako:
	python -c 'from make_files_with_mako import clean; clean()'

build: dockermako
	docker build -f $(image).Dockerfile -t fluiddyn/$(image) .
	docker tag fluiddyn/$(image) fluiddyn/$(image):$(tag)

build_nocache: dockermako
	docker build -f $(image).Dockerfile -t fluiddyn/$(image) . --no-cache
	docker tag fluiddyn/$(image) fluiddyn/$(image):$(tag)

onbuild: dockermako
	docker build -f $(image).onbuild.Dockerfile -t fluiddyn/$(image):onbuild .

push:
	docker push fluiddyn/$(image)

run:
	docker run -it fluiddyn/$(image) bash

run_travis:
	docker run -it travisci/ci-python bash -c "su - travis"

run_travis_old:
	docker run -it quay.io/travisci/travis-python bash -c "su - travis"

cleancontainers:
	for cont in $$(docker ps -a | awk 'NR>1{print $$1}'); do docker rm $$cont; done

cleanimages:
	docker rmi -f $$(docker images -qf "dangling=true")

cleanall: cleanmako cleancontainers cleanimages
