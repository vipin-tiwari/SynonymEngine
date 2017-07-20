#!/bin/bash

echo "Running the Application..."
sudo nohup python /vagrant/code/api/names.py >/dev/null 2>&1 &

echo "Application started"