## ms_TestFibonacciService

**Test a Fibonacci Service**

ms_TestFibonacciService ([ms_TestFibonacciService](http://github.com/msmith303/ms_TestFibonacciService)) repository
holds the py.test files used to test the python project dg_FibonacciService.


### Install

py.test can be found in tagged revisions on GitHub.

Or in a Docker application:

    docker run ms_FibonacciService

### Usage

  $ py.test
  ======= test session starts =======

  =======  1 failed in 0.14 seconds =========

  With py.test's detailed assertion intropection, only plain assert statements are used.

### Issues

1. Unable to run either back-end or front-end docker containers on AWS EC2 even though 'docker build' worked.

[ec2-user@ip-172-31-33-214 GitHub]$ sudo docker run -p 5000:5000 -d --name dg-fibonacci-be dg-fibonacci-be
Unable to find image 'dg-fibonacci-be:latest' locally
Pulling repository docker.io/library/dg-fibonacci-be
Error: image library/dg-fibonacci-be:latest not found


Revision 2 May 2016
