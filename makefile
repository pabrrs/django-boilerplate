up: # start app
	@if [ ! -f .env ]; then \
		cp .env.template .env; \
	fi
	docker-compose up --build --remove-orphans --renew-anon-volumes
