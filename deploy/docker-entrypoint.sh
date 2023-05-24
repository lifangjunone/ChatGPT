#!/usr/bin/env sh
set -e
if [ "$ENVIRONMENT" = "testing" ]; then
	echo "Running Testing Application"
	uwsgi --ini conf/uwsgi.ini

elif [ "$ENVIRONMENT" = "development" ]; then
	echo "Running Development Tests"
	uwsgi --ini conf/uwsgi.ini

elif [ "$ENVIRONMENT" = "production" ]; then
	echo "Running Production Application"
	uwsgi --ini conf/uwsgi.ini

else
	echo "Please provide an environment"
	echo "Stopping"
fi
