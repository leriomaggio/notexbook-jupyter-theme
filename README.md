# <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/main/docs/logo/notexbook.png" width="34%" />

## The Jupyter notebook theme for ![LaTeX](https://render.githubusercontent.com/render/math?math=\LaTeX) lovers ![heart](https://render.githubusercontent.com/render/math?math=\heartsuit)

The <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/main/docs/logo/notexbook.png" width="10%" /> theme aims at combining the flexibility and interactivity of Jupyter notebooks with the unique elegance and sobriety of a `LaTeX` article.  

### `noTeXbook` in a Nutshell

- *Computer Modern* fonts for Markdown typesetting;
- `Fira Code` (_open source_) font for **Code** editor (with ligatures support);
- `Hack` (_open source_) font for **Markdown** editor (slightly better for text writing, _ed._);
- Multiple Colour Syntax highlighting themes;
- Extra `CSS` classes for additional LaTeX-ish formatting use cases (e.g. _footnotes_, _dropcap_);
- **Full** support for Jupyter Notebooks and JupyterLab (version `2.0x`).

### Sneak Peek?

Here is a [**Preview**](https://leriomaggio.github.io/notexbook-jupyter-theme/) of how \[a\] `noTeXbook` looks like!

### Setup `noTeXbook` Theme

The  `noTeXbook` theme is available on [PyPi](https://pypi.org/project/notexbook-theme/) as a Jupyter Notebook 
(Python) extension:

```shell
$ pip install notexbook-theme
```

Once installed, just `load` the `notexbook` extension into a Jupyter notebook cell:

```jupyterpython
%load_ext notexbook
```

The theme can be activated via the `%texify` IPython magic 🔮:

```jupyterpython
%texify  # default theme settings will be used
```

#### `%texify` IPython magic

The `%texify` IPython magic embeds the `noTeXbook` theme directly into the current notebook.
This results into the following three unique features: 

1.  **on-demand activation**: the theme is enabled **only** for selected notebooks, without having to 
	[change](https://jupyter-notebook.readthedocs.io/en/stable/security.html?highlight=custom.css#javascript-and-css-in-markdown-cells) 
	the (global) default Jupyter notebook theme.

2.  **portable**: the theme is embedded directly into the notebook (as the output of a single cell). 
	Therefore, whenever the notebook will be *shared* and/or *exported* (e.g. in HTML or PDF via `webpdf`), 
	the theme will continue to be available, with no extra installation required. 
	Similarly, *disabling the theme* becomes as easy as *clearing* the output of the `%texify` cell.

3.  **customisable**: the theme allows for an easy customisation (e.g. enabling multiple **editor themes**) 
	via `IPython magic` line arguments.

#### Magic Line Arguments and Theme settings 🪄

The `%texify` IPython magic 🔮 supports the following arguments:

```shell
-cdth <{material,github,github2,crisp}>, --code-theme <{material,github,github2,crisp}>
	Colour Theme for Code Editor

-mdth <{material,typora}>, --md-theme <{material,typora}>
	Colour Theme for Markdown Editor

-cdfs CODE_MONO_FONT_SIZE, --code-fontsize CODE_MONO_FONT_SIZE
	Font size used in Code and Markdown Editor. Default: 16px

-mdfs MD_MONO_FONT_SIZE, --md-fontsize MD_MONO_FONT_SIZE
	Font size of Rendered Markdown monospace. Default: 17px
	
-nbfs NB_FONT_SIZE, --notebook-font-size NB_FONT_SIZE
	Font size of Rendered Content in Notebook. Default: 17px

-lh NB_LINE_HEIGHT, --linespread NB_LINE_HEIGHT
	Line height of Notebook Content. Default: 1.4

-v, --verbose         
	Verbose mode: Display the list of enabled Theme settings.
```

**Examples**: 

```jupyterpython
%texify --code-font Monaco --linespread 1.3 -fs 18
```

In these settings: (1) the `Monaco` font will be used for code editor; (2) notebook font size will be set to `18px`, 
and the line height will be `1.3`. 
**Note**: To actually use the `Monaco` font for code editor, the font must be available and installed on your local machine.
If that is not be the case, the default code mono font (i.e. `Fira Code`) will be used as a fallback.

```jupyterpython
%texify --code-theme github
```

In these settings, the **new** `github` Code Editor theme will be used for code syntax highlighting, substituting the 
default _Material Design_ theme. This theme is inspired by the current code theme on GitHub.

To see the **full** list of configuration options :

```jupyterpython
%texify?
```

### There's more...

The `noTeXbook` theme is **also** available as a **full-fledged** _custom_ Jupyter notebook theme (HTML/CSS).
This is useful in case you would prefer to enable the theme as **the** global custom default Jupyter theme.

The `noTeXbook` theme package is available for [download](https://github.com/leriomaggio/notexbook-jupyter-theme/releases), 
along with its corresponding [documentation](https://github.com/leriomaggio/notexbook-jupyter-theme/blob/custom-css/README.md). 
The documentation also contains details on the original CSS design, and instructions on how to define 
your own CSS Editor Colour theme.

**Last but not least**, **Experimental** theme integration for Google Colaboratory Notebooks (via the 
    [Stylus](https://en.wikipedia.org/wiki/Stylus_(browser_extension)) browser extension)
is also available. See [here](https://github.com/leriomaggio/notexbook-jupyter-theme/blob/texbook-colab/README.md) 
for more information.

### `noTeXbook` shall by *thy* name

When I had to think to a name for this project, I aimed almost immediately at finding a single word that would 
convey the idea of integration between `LaTeX` and notebooks I had in mind. 
So <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> 
seemed quite an obvious choice. 
Moreover, this name itself is also a unique [portmanteau](https://www.merriam-webster.com/dictionary/portmanteau) 
(`port·man·teau | \ pȯrt-ˈman-(ˌ)tō`) that blends together the words **noTe**<del>X</del>**book**, and 
<del>no</del>**TeXbook**, that is the name of [Donald E. Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)'s 
[book](http://www.ctex.org/documents/shredder/src/texbook.pdf) on `TeX`.

That was the omen... 🤩.

> One!... Two!... Five! 

(_from_:  [The Holy Hand Grenade](https://www.youtube.com/watch?v=xOrgLj9lOwk) - Monty Python and the Holy Grail)

The <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> 
project wishes to pay a tribute of gratitude (in the name, and in the content) to two of the technologies I do use 
(and love) the most as a researcher and as a data scientist.

### Project Links

- 📦 [PyPi package](https://pypi.org/project/notexbook-theme/)
- 🖌 [Official GitHub Repo](https://github.com/leriomaggio/notexbook-jupyter-theme/)
- 🚀 [Documentation and GitHub Page](https://leriomaggio.github.io/notexbook-jupyter-theme/)

#### Credits

* The [`spinzero`](https://github.com/neilpanchal/spinzero-jupyter-theme) jupyter theme has been inspirational in the design of the early version of this theme;
* The idea of overlay of selected cells has been inspired from [this](https://gist.github.com/formigone/dbabdd4ae38ded54b6f028713ac78c8a) custom theme.
* Inspiration on the choice of Monospace fonts for code and markdown has come from this [article](https://fontsarena.com/blog/best-programming-fonts/) 
* Original versions of colour themes for code and markdown editors:
	- [Material Design Light](https://github.com/JonaDuran/Material-Light-Theme/)
	- [GitHub Light](https://github.com/primer/github-syntax-light)
	- [Crisp Rainglow Collection](https://github.com/rainglow/vscode/)
	
#### References

(Some links I found useful along the way):

- [Computer Modern on the Web](https://www.checkmyworking.com/cm-web-fonts/)
- [`setuptools`: Specify Dependencies](https://python-packaging.readthedocs.io/en/latest/dependencies.html)
- [How to Add Custom `setup.py` commands](https://jichu4n.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy/)
- [`pyproject.toml`](https://martin-thoma.com/pyproject-toml/)
- [What the heck is `pyproject.toml`](https://snarky.ca/what-the-heck-is-pyproject-toml/)
- [Jupyter Server Extension](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html) (Particularly useful in earlier version of this project in which fonts where handled as local resources)

#### Acknowledgments

Special thanks to [cdesio](https://github.com/cdesio), [ninadicara](https://github.com/ninadicara), and [alanderex](https://github.com/alanderex) for testing earlier versions of the theme!














