# Helper Scripts

A simple project with various tools, scripts, samples, gists for quick refrence.

## Setup
For Python projects use virtualenv.

Here is how you install virtualenv in debian based linux (ubuntu)
>     $ sudo apt install pipx
>     $ pipx install virutalenv

To Create a virutal environment for this project goto python folder and run
>     $ cd python
>     $ virtualenv --python="/usr/bin/python3" venv
>     $ . venv/bin/activate

Make sure your pip is upto date by running
>     pip install pip --upgrade

## Usage
To use a script/tool go to the folder and install python requirments.
>     pip install -r requirements.txt

To List local packages installed by pip in your envronment run
>     pip list

If folder has only one script run the script, if not consult the Readme inside the folder for more description about the usage of that script.

## License
[MIT License](https://github.com/vkkotha/helper_scripts/blob/master/LICENSE).