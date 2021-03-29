local-bash:
	docker exec -it django-bp /bin/bash

logs:
	docker logs --follow django-bp

start-local:
	docker-compose up -d

stop:
	docker stop django-bp
	docker stop django-db
