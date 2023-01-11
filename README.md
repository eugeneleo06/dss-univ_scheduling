# Decision Support System University Scheduling
Decision Support System that is [Minizinc](https://www.minizinc.org/) based. Developed with **Constraint Programming** method, integrated with python library [PyMzn](http://paolodragone.com/pymzn/index.html) and [Python Minizinc](https://minizinc-python.readthedocs.io/en/latest/index.html). Implemented to web application with [Flask](https://flask.palletsprojects.com/en/2.2.x/) framework.

## Dependencies
Minizinc

    brew install minizinc

PyMzn

    pip install pymzn

Minizinc Python

    pip install minizinc

Flask

    pip install Flask

*require Python 3.6 (or higher)*

## High Level Illustration
![Illustration Diagram](https://raw.githubusercontent.com/eugeneleo06/dss-univ_scheduling/main/Diagram.png)

## How to Run
Run this command to run the local server with port :5000

    flask -app main run

## Paper Source
https://www.researchgate.net/publication/319122545_PENJADWALAN_KULIAH_OTOMATIS_DENGAN_CONSTRAINT_PROGRAMMING