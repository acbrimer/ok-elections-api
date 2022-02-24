#!/bin/bash
APP_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd );
gcloud run deploy ok-election-api --source ${APP_DIR} --allow-unauthenticated;