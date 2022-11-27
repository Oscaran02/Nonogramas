# Nonogramas
## Development

### Run it

There's two ways of running this project:

#### Running it from Pycharm setting a run environment

* First you have to set a interpreter for python, Pycharm suggest you to use the pipenv interpreter if you have this library installed, if not, just use your normal python interpreter.
* In the top right part, you will click "Edit configurations"
![image](https://user-images.githubusercontent.com/38623131/204152985-dbbb824f-77d8-42a6-8c3d-a73c7b814282.png)
* Add new run configuration
![image](https://user-images.githubusercontent.com/38623131/204153037-8f9400b5-567f-4ffc-80ef-d6abc87f6cef.png)
* We are going to search Python
![image](https://user-images.githubusercontent.com/38623131/204153068-41272095-cc4f-47e6-b6cb-2708d32f28d7.png)
* In script path we are going to look for nonogramas.py and on parameters we are going to write our board to solve .txt
* In this order the result should be this
![image](https://user-images.githubusercontent.com/38623131/204153173-228abbf7-fef1-4989-a4e5-00398ccc8c00.png)
* Finally, we are going to run the script
![image](https://user-images.githubusercontent.com/38623131/204153217-96a77b7a-0dd8-463b-bb3a-1b92dd453515.png)


#### Running directly from cmd/console

or as an alternative, you can try this:
Going to project directory
```shell
cd <project_dir>
```

Run it directly with Python
```shell
python3 nonogramas.py <any board.txt>
```
An example for this command will be:
```shell
python3 nonogramas.py Tablero7x6.txt
```

## Author

* Oscar Pacheco
