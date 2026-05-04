#!/bin/bash
PS=/home/roaguila/push_swap/push_swap
CK=/home/roaguila/push_swap/checker
CKL=/home/roaguila/push_swap/checker_linux

echo "Testing random 100 numbers..."
ARGS=$(shuf -i -500-500 -n 100 | tr '\n' ' ')
RESULT=$($PS $ARGS | $CK $ARGS)
echo "Our checker: $RESULT"
RESULT2=$($PS $ARGS | $CKL $ARGS)
echo "Official checker: $RESULT2"

echo ""
echo "Testing random 500 numbers (just our checker)..."
ARGS2=$(shuf -i -5000-5000 -n 500 | tr '\n' ' ')
RESULT3=$($PS $ARGS2 | $CK $ARGS2)
echo "Our checker: $RESULT3"
