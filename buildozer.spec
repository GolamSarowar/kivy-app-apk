name: Build APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        pip install buildozer
        pip install kivy

    - name: Build APK
      run: |
        # buildozer init  # Comment out this line
        buildozer android debug
