#!/bin/bash
#GET request to the URL, and displays the body of the response
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
