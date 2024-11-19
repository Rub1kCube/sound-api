TAIL=1000

define set-default-container
	ifndef c
	c = django
	else ifeq (${c},all)
	override c=
	endif
endef

set-container:
	$(eval $(call set-default-container))

build:
	docker compose -f docker-compose.dev.yml build
up:
	docker compose -f docker-compose.dev.yml up --remove-orphans  -d $(c)
down:
	docker compose -f docker-compose.dev.yml down
logs: set-container
	docker compose -f docker-compose.dev.yml logs --tail=$(TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.dev.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/bash
remove: set-container
	docker compose -f docker-compose.dev.yml rm -fs $(c)


migrate: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c './manage.py migrate'
migrations: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c './manage.py makemigrations'
shell: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/bash -c './manage.py shell'

compile-reqs: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pip install pip-tools && uv pip compile --all-extras pyproject.toml -o requirements.txt'

test: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pytest -n 4'
pre-commit: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'git config --global --add safe.directory /src && PRE_COMMIT_HOME=.precomcache pre-commit run --all-files'
