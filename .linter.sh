#!/bin/bash
cd /home/kavia/workspace/code-generation/easyeventmanager-45866-fcc2f9f2/easyeventmanager_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

