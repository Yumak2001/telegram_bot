

# PROJECT CONFIG
PATCH = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PROJECT:=telegram_bot
LOCALES_DOMAIN := bot
LOCALES_DIR := locales
VERSION:=0.1


# =================================================================================================
# Base
# =================================================================================================

default:help

help:
	@echo PATCH=$(PATCH)
	@echo $(PROJECT_NAME) V$(VERSION)

# Install virtualenv to .ven and install package from requirements.txt
install:
	@echo Start install VirtialEnv to evn/
	@pip install pipenv
	@pipenv --python 3.9
	@pipenv install --dev
	@mkdir log
	@mkdir files

texts-update:
	@pipenv run pybabel extract . \
    	-o ${LOCALES_DIR}/${LOCALES_DOMAIN}.pot \
    	--project=${PROJECT} \
    	--version=${VERSION} \
    	--copyright-holder=Illemius \
    	-k __:1,2 \
    	--sort-by-file -w 99
	@pipenv run pybabel update \
		-d ${LOCALES_DIR} \
		-D ${LOCALES_DOMAIN} \
		--update-header-comment \
		-i ${LOCALES_DIR}/${LOCALES_DOMAIN}.pot

texts-compile:
	@pipenv run pybabel compile -d locales -D bot

clear:
	@pipenv --rm
	@rmdir /s env log files
