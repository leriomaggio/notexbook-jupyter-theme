# <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="34%" />

⚠️ **Note**: ⚠️ 
You just hit the `notebook-magic `branch where the **notexbook** Jupyter extension, and IPython magic are developed and maintained.
Jump [here](#magic) for instructions!

## The Jupyter notebook theme for ![LaTeX](https://render.githubusercontent.com/render/math?math=\LaTeX) lovers ![heart](https://render.githubusercontent.com/render/math?math=\heartsuit)

The <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> theme aims at combining the flexibility and interactivity of Jupyter notebooks with the unique elegance and sobriety of a `LaTeX`-generated article.  The <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> project wishes to pay a tribute of gratitude (in the name, and in the content) to two of the technologies I do use and love the most as a researcher and a data scientist.

### <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> theme in a Nutshell

- *Computer Modern* fonts for Markdown typesetting;
	- *Computer Modern Typesetting* for Markdown Mono	
- `Fira Code` (_open source_) font as the default `monospace` for the **Code** editor (with ligatures support);
- `Hack` (_open source_) font as the default `monospace` font for **Markdown** editor (slightly better for text writing, _ed._);
- Colour Syntax highlight themes for Code and Markdown editors based on Material Design colour scheme.
    - Multiple Editor Themes supported: easy to change and customise (just a few CSS variables to do the trick!)
- Special Output formatting for `stderr` and `pandas.DataFrame`
- Extra `ad-hoc` CSS classes for extra formatting use cases (e.g. _footnotes_, _dropcap_)
  

### Sneak Peek?

Here is a [**Preview**](https://leriomaggio.github.io/notexbook-jupyter-theme/) of what [a]   `noTeXbook` looks like!

## Install <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> Theme

<a name="magic"></a>

### `notexbook-theme`  and `%texify` 🔮

The `notexbook-theme` package (on [PyPi](https://pypi.org/project/notexbook-theme/)) provides the `noTeXbook` theme as an easy-to-integrate IPython magic (i.e. `%texify`), activated via Jupyter notebook (Python) extension, `notexbook`. So, to use the `noTeXbook` theme in a notebook it will be just a matter of (1) loading the extension; (2) calling the `%texify` IPython magic.

The  `%texify` custom IPython magic injects the `noTeXbook` style directly into notebooks, which results the following three unique feature: 

1.  **easy-to-use**: the theme is enabled only _on demand_ in each selected notebook, without having to change the default style;

2.  **portable**: the theme is injected directly into the notebook as the output of a single cell. Therefore, when *shared*, the notebook will continue to keep the `noTeXbook` style, without having to download nor install anything: just *trust* the notebook! Similarly, *disabling the theme* becomes as easy as *deleting a cell*.
3.  **customisable** (via `magic` line arguments). All supported customisations are listed in the next [section ![arrow](https://render.githubusercontent.com/render/math?math=\Downarrow)](#magicargs) 

To install the `notexbook-theme` from PyPi:

```shell script
pip install notexbook-theme
```

Once installed, just `load` the `notexbook` extension into a notebook cell:

```python
%load_ext notexbook
```

and activate the custom IPython magic:

```python
%texify  # default theme settings will be used
```

<a name="magicargs"></a>

#### Customising theme settings

Current version of the theme allows to customise the following settings:

- `--code-font` (`-cdf`): the font family used in Code editor (default: `Fira Code`)
- `--md-font` (`-mdf`): the font family used in Markdown editor (default `Hack`)
- `--code-fontsize` (`-cdfs`): the font size used in Code and Markdown editor (default `16px`)
- `--md-fontsize` (`-mdfs`): the font size of *rendered* Markdown monospace (default `16px`)
- `--fontsize` (`-nbfs`):  (`LaTeX` legacy) font size of *rendered* Markdown text (default: `19px`)
- `--linespread` (`-lh`): (`LaTeX` legacy) line height of *rendered* Markdown text (default `1.4`)
- `--code-theme` (`-cdth`):  colour theme for Code editor (default: `Material Design`)
	- Other available theme choices: `github`, `crisp` 	
- `--md-theme` (`-mdth`): colour theme for Markdown editor (default `Material Design`)
	- Other available theme choices: `typora`

**Example**: 

Let's say you do like `noTeXbook` theme, and you want to use it in your notebooks. However, you would prefer using the favourite monospace font you are normally using in your code editor (e.g. `Monaco`). In addition, you also want to slightly reduce the notebook default `font-size` (`18px`) as well as the `line height` (`1.3`):

```shell
%texify --code-font Monaco --linespread 1.3 -nbfs 18
```

To see the **full** list of configuration options :

```shell
%texify?
```



### Project Links

- [PyPi package](https://pypi.org/project/notexbook-theme/)
- [Official GitHub Repo](https://github.com/leriomaggio/notexbook-jupyter-theme/)
- [Documentation and GitHub Page](https://leriomaggio.github.io/notexbook-jupyter-theme/)
- [Project Board and Issue Tracker](https://github.com/leriomaggio/notexbook-jupyter-theme/projects/1)



### <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="15%" /> shall by *thy* name

When I had to think of a name for this project, I aimed almost immediately at finding a single word that could convey the idea of integration of the`LaTeX`-__inspired_  theme for notebooks I had in mind. And so, <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" />, a unique [portmanteau](https://www.merriam-webster.com/dictionary/portmanteau)[(1)]( "Pronunciation") that blends together the words **noTe**<del>X</del>**book** (_no further explanation needed, ed._), and <del>no</del>**TeXbook**, the name of [Donald E. Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)'s [book](http://www.ctex.org/documents/shredder/src/texbook.pdf) on `TeX`.

That was the omen... 🤩.

> One!... Two!... Five! [(2)]("Monty Python and the Holy Grail")

---
`[(1)]` : `port·​man·​teau | \ pȯrt-ˈman-(ˌ)tō` <br />
`[(2)]`: [The Holy Hand Grenade](https://www.youtube.com/watch?v=xOrgLj9lOwk) - Monty Python and the Holy Grail



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
















