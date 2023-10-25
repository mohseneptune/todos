virtualenv = .venv
source_dir = src

run:
	@echo "Running FastAPI app..."
	@cd ${source_dir} && uvicorn main:app --reload

pre-commit:
	@echo "Running pre-commit..."
	@git add .
	@pre-commit run -a

test:
	@echo "Running tests..."
	@pytest tests/

clean:
	@echo "Cleaning up..."
	@find . -type d -name "*cache*" -not -path "./.venv/*" -exec rm -rf {} \;
	@find . -name "*.pyc" -not -delete

compose-up:
	@echo "Running docker-compose up..."
	@docker compose up -d

tree:
	@make clean
	@echo "Generating project tree..."
	@tree -L 4 -a -I ${virtualenv}/ -I .git/

help:
	@echo "Available targets:"
	@echo "  run - Run the FastAPI app using Uvicorn"
	@echo "  clean - Remove generated files"
	@echo "  pre-commit - Add all files to staging and run pre-commit"
	@echo "  git-commit - Commit changes to git with message"
	@echo "  tree - Generate project tree"
	@echo "  help - Show this help message and exit"
	@echo "  docker-compose-up - Run docker-compose up"
