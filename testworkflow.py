name: Python Testing

 

on:

  push:

    branches:

      - branch2

  pull_request:

    branches:

      - branch2

 

jobs:

  test:

    runs-on: ubuntu-latest

 

    steps:

    - name: Checkout code

      uses: actions/checkout@v3

   

    - name: Set up Python

      uses: actions/setup-python@v3

      with:

        python-version: '3.x'

   

    - name: Install dependencies

      run: |

        python -m pip install --upgrade pip

        pip install -r requirements.txt

   

    - name: Run tests

      run: |

        python -m unittest discover -s tests

