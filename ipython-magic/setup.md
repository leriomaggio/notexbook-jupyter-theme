## Using `%texify` custom IPython magic

The `texify` custom IPython magic has been created to allow using the `TexBook` theme is notebooks without having to change the default custom theme, and so using it in *every* single notebook. In addition, the custom magic allows for extra flexibility to customise the theme, and to share it. 

The `notebook-texbook-theme` package available on [PyPi](https://pypi.org/project/notebook-texbook-theme/) allows to install and setup the custom IPython magic  via pip:

```shell script
    pip install notebook-texbook-theme
```
Once installed, it will just necessary to `load` the `texbook_theme` extension as in:

```jupyter
%load_ext texbook_theme
```
This will make the `texify` magic available in your notebook. 

Therefore, just type: 
```jupyter
%texify
```
into a new notebook cell, and the `TeXbook` theme will be automatically enabled. 

#### Customising the `TeXbook` theme

Current version of the theme allows to customise the following settings:

- `--code-mono-font`: the font-family used for Code Editor (default: `Fira Code`)
- `--md-mono-font`: the font-family used for Markdown Editor (default `Hack`)
- `--code-mono-font-size`: the font-size used in Code Editor (default `16px`)
- `--md-mono-font-size`: the font-size used for *rendered* Markdown mono (default `16px`)
- `--notebook-font-size`:  the font-size of the *rendered* Markdown text (default: `19px`)
- `--notebook-line-height`: the line height used in *rendered* Markdown text (default `1.4`)
- `--code-theme`: The Code Editor Highlight theme to use (default: `Material Design`)
	- Other available themes are: `github`, `crisp` 	
- `--md-theme`: The Markdown Editor Highlight theme to use (default `Material Design`)
	- Other available themes are: `typora`

**Example**: `%texify --code-mono-font Monaco` will enable the `TeXbook` theme using the `Monaco` font instead of the default `Fira Code` for code editor.
