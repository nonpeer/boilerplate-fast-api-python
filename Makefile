SHELL=/bin/bash

.PHONY: help
help:  ## Show the help
	@echo "██████╗ ███████╗ ██████╗ ██╗   ██╗██╗     ██╗   ██╗███████╗"
	@echo "██╔══██╗██╔════╝██╔════╝ ██║   ██║██║     ██║   ██║██╔════╝"
	@echo "██████╔╝█████╗  ██║  ███╗██║   ██║██║     ██║   ██║███████╗"
	@echo "██╔══██╗██╔══╝  ██║   ██║██║   ██║██║     ██║   ██║╚════██║"
	@echo "██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗╚██████╔╝███████║"
	@echo "╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

.PHONY: shell
shell: ## Shell developer
	@docker exec -ti api-dev bash

.PHONY: lint
lint: ## lint
	@docker exec -ti api-dev black --check .


.PHONY: test-cov
test-cov: ## test-cov
	@docker exec -ti api-dev pytest --cov=boilerplate_fastapi  --cov-report=html  boilerplate_fastapi/tests

.PHONY: test
test: ## test
	@docker exec -ti api-dev pytest

.PHONY: prod
prod: ## Start environment production
	@docker-compose -f docker/production/docker-compose.yaml up --build

.PHONY: dev
dev: ## Start environment developer
	@docker-compose -f docker/developer/docker-compose.yaml up --build
