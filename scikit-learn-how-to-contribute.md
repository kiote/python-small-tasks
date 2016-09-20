Read the [contributing manual](http://scikit-learn.org/dev/developers/contributing.html).
Have to be enough, but if you are such a lazy thing as me:

1. Clone scikit-learn repo onto your local machine with `git clone https://github.com/scikit-learn/scikit-learn.git`.
2. Use virtualenv: `virtualenv venv`
3. Make sure `make` runs sucessfully in scikit-learn/ directory
    * `pip install scipy`
    * `pip install cython`
    * `make`
4. Make sure you can run tests:
   * `pip install nose`
   * `pip install scipy`
   * `pip install numpy`
   * `python setup.py install --user`
   * `nosetests -v sklearn`
