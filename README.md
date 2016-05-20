## ms_TestFibonacciService

**Test a Fibonacci Service**

ms_TestFibonacciService ([ms_TestFibonacciService](http://github.com/msmith303/ms_TestFibonacciService)) is an
[ECMAScript](http://www.ecma-international.org/publications/standards/Ecma-262.htm)
code generator from.


### Install

py.test can be found in tagged revisions on GitHub.

Or in a Docker application via npm:

    npm install escodegen

### Usage

A simple example: the program

    py.test({
        left: { type: 'Literal', value: 40 },
        right: { type: 'Literal', value: 2 }
    });

produces the string `'40 + 2'`.

To run the tests, execute `py.test` in the root directory.

Revision 2 May 2016
