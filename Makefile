build:
	docker-compose build django

local-bash:
	docker-compose exec django /bin/bash
logs:
	docker-compose logs --follow django

unit:
	docker-compose exec django coverage run -m pytest tests/unit -v -x
	docker-compose exec django coverage xml --ignore-errors
	@echo "Total Python coverage:" `docker-compose exec django coverage report --precision=2 | tail -n 1 | awk '{ print $4 }'`

test:
	docker-compose exec django coverage run -m pytest tests/ -v -x
	docker-compose exec django coverage xml --ignore-errors
	@echo "Total Python coverage:" `docker-compose exec django coverage report --precision=2 | tail -n 1 | awk '{ print $4 }'`

pre-commit-install:
	docker-compose exec django pre-commit install

start-local:
	docker-compose up -d

stop:
	docker-compose down
