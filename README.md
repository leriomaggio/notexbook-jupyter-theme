# <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="34%" />

⚠️ **Note**: ⚠️ 
The `custom-css `branch is specifically dedicated to develop and maintain the **full-fledged** 
Jupyter Custom theme version of the `noTeXbook` theme.

## Setup `noTeXbook` as the default Jupyter Notebook theme

To install and enable `noTeXbook` as the **default** Jupyter Notebook theme (for **all your notebooks**), it is just 
necessary to copy the `custom` folder  contained in this repository **as-is** in your `JUPYTER_CONFIG_DIR` folder 
(`$HOME/.jupyter`by default)
See [here](https://jupyter.readthedocs.io/en/latest/use/jupyter-directories.html#configuration-files)) for more about 
Jupyter configuration dirs.

```shell
cp -R custom $HOME/.jupyter
```

See [here](https://stackoverflow.com/questions/32156248/how-do-i-set-custom-css-for-my-ipython-ihaskell-jupyter-notebook/34742362#34742362) for 
more information on Customising Notebook style.

#### Customising the CSS theme

To personalise the default settings of the `noTeXbook` theme it is just necessary to tweak a few CSS variables. 
These variables have a common prefix that identifies their purpose, and what they are used for:

- `--txbk-ui-`: VARS related to the look&feel of the notebook, not related to content;
- `--txbk-content-`: VARS controlling the rendered Markdown and cells' output;
- `--txbk-code-`: VARS controlling cells editors (code and markdown)

##### Customising Editor Colour themes

In order to change the **colour theme** used by code and markdown editors, it is necessary to edit 
the `editors.css` file and substitute the corresponding file to import on the very top (`lines 28;31`). 

It is also very simple to create your own theme: in each theme CSS file there is just the reference  _colour palette_, 
and how this palette maps to specific CSS VARS (e.g. `keywords`, `numbers`, etc.).

**No CSS class nor rule is defined into a Theme file**. 
Each rule is defined into the main `editors.css` file, and overloaded by specific themes VARS definitions.

### Project Links

- 📦 [PyPi package](https://pypi.org/project/notexbook-theme/)
- 🖌 [Official GitHub Repo](https://github.com/leriomaggio/notexbook-jupyter-theme/)
- 🚀 [Documentation and GitHub Page](https://leriomaggio.github.io/notexbook-jupyter-theme/)
