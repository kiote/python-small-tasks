## How to setup the environment

Read the [contributing manual](http://scikit-learn.org/dev/developers/contributing.html).
It have to be enough, but if you are such a lazy thing as I am:

1. Clone scikit-learn repo onto your local machine with `git clone https://github.com/scikit-learn/scikit-learn.git`.
2. Use virtualenv: `virtualenv venv`
3. Make sure `make` runs sucessfully in scikit-learn/ directory
    * `pip install scipy`
    * `pip install cython`
    * `pip install -U scikit-learn`
4. Make sure you can run tests:
   * `pip install nose`
   * `pip install numpy`
   * `python setup.py install --user`
   * `nosetests -v sklearn`

## How to run particular test

For example, [test-common](https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tests/test_common.py): `nosetests sklearn.tests.test_common`

## How to add git remote

To be able to fetch changes from base repo.

What remotes do we have already:

    git remote -v

Add remote:

    git remote add new-remote-name https://github.com/user/repo.git
