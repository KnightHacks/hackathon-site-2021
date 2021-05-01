#  Just a quick little makefile so I don't have to type so much every time
COMPOSE_YML := docker-compose-dev.yml

.PHONY: composeup
composeup:
	docker-compose -f $(COMPOSE_YML) up --build -d

.PHONY: composedown
composedown:
	docker-compose -f $(COMPOSE_YML) down
