APP?=mortimer
VERSION?=dev
LATEST=latest

DOCKER_IMAGE_NAME=roch1990/${APP}
DOCKER_IMAGE_VERSION=${DOCKER_IMAGE_NAME}:${VERSION}
DOCKER_IMAGE_LATEST=${DOCKER_IMAGE_NAME}:${LATEST}

.PHONY: compose-test
compose-test:
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: build
build:
	docker build -t ${DOCKER_IMAGE_NAME}:${VERSION} .

.PHONY: push
push:
	docker push ${DOCKER_IMAGE_NAME}:${VERSION}