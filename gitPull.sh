#!/bin/bash

GIT=`which git`
echo $GIT
echo "Enter the commit message: "
read commit_msg
${GIT} status
${GIT} add --all
${GIT} commit -m $commit_msg
${GIT} push