# Homework

Name:Brian Brooks

## Question 1)

Unit Test: A unit test is the test of a single function, class, or component to assure it works by itself. You use it if you want to verify that a small, individual part of your code works correctly independently.

Integration Test: An integration tests multiple functions/components of a program working together. You would use this when you want to make sure that different components interact with eachother correctly

Regression Test: A regression test tests already exisiting pieces of the progrma after changes, to assure everything that worked previously still does. You would use this when you have made changes to your code and need to make sure that everything still works properly

## Question 2)

Pytest is a testing framework in Python that automatically finds and executes test cases in your project. It looks for files, classes and functions that follow certain naming patterns.

A fixture in pytest is a reusable piece of setup/teardown code that provides data, objects, or state to test functions. It is a function that can set up Test data, temporary file, etc

## Pytest Feature Used

@pytest.mark.parametrize

## Regression test-Q5

I created a regression test file name test_apply_discount_bug.py, this test calls apply_discount(20.0,10) and anticipates a result of 18.0, When first running it the bug in apply_discount causes it to fail. The bug in apply discount was that it was not dividing the percentage by 100. I fixed the bug and the test passed, confirming it works correctly now
