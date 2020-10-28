## Using `TeXbook` as default Jupyter Notebook theme

To install and enable `TeXbook` as the **default** Jupyter Notebook theme, it is just necessart to copy the `custom` folder 
contained in this repository **as-is** in the `JUPYTER_CONFIG_DIR` folder (default `$HOME/.jupyter`):

```shell script
cp -R custom $HOME/.jupyter
```

This will create a `custom` folder within your `JUPYTER_CONFIG_DIR` 
(see [here](https://jupyter.readthedocs.io/en/latest/use/jupyter-directories.html#configuration-files))
for more details about Jupyter Notebook Directories), that will automatically enable `TeXbook` theme 
**by default** for all Jupyter notebook. 

See [here](https://stackoverflow.com/questions/32156248/how-do-i-set-custom-css-for-my-ipython-ihaskell-jupyter-notebook/34742362#34742362) for more information on Customising Notebook style.
