#!/bin/bash

GIT=`which git`
echo $GIT
echo "Enter the commit message (DO NOT use space, insted use "_"): "
read -r commit_msg
${GIT} status
echo "-------------------------------------"
${GIT} add --all
echo "-------------------------------------"
${GIT} status
echo "-------------------------------------"
${GIT} commit -m $commit_msg
echo "-------------------------------------"
${GIT} push
echo "-------------------------------------"
