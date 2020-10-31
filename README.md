# <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="34%" />

⚠️ **Note**: ⚠️ 
You just hit the `custom-css `branch where the **full-fledged** Jupyter Custom theme is available and maintained.
Jump [here](#custom) for instructions!

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

Here is a [**Preview**](https://leriomaggio.github.io/texbook-jupyter-theme/) of what [a]   `noTeXbook` looks like!

## Install <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> Theme

The <img src="https://github.com/leriomaggio/notexbook-jupyter-theme/raw/master/docs/logo/notexbook.png" width="10%" /> theme is available in three different flavours: 

1. **Full-fledged** _custom_ Jupyter notebook theme (HTML/CSS): ([here  ![arrow](https://render.githubusercontent.com/render/math?math=\Downarrow)](#custom))

1. `pip`-_installable_ package to embed the theme into notebooks via custom **IPython magic** (`%texify`) ([Link ![arrow](https://render.githubusercontent.com/render/math?math=\Rightarrow)](https://github.com/leriomaggio/notexbook-jupyter-theme/blob/notebook-magic/README.md#magic));

3. (**Experimental**) theme integration for Google Colaboratory Notebooks (via the 
    [Stylus](https://en.wikipedia.org/wiki/Stylus_(browser_extension)) browser extension) ([Link ![arrow](https://render.githubusercontent.com/render/math?math=\Rightarrow)](https://github.com/leriomaggio/notexbook-jupyter-theme/blob/texbook-colab/README.md#colab)).

⚠️ Jupyter **Lab** is <ins>supported</ins>, but *still in progress* ! ⚠️

<a name="custom"></a>
### Setup `noTeXbook` as the default Jupyter Notebook theme

To install and enable `noTeXbook` as the **default** Jupyter Notebook theme, it is just necessart to copy the `custom` folder  contained in this repository **as-is** in the `JUPYTER_CONFIG_DIR` folder (see [here](https://jupyter.readthedocs.io/en/latest/use/jupyter-directories.html#configuration-files)) - default `$HOME/.jupyter`:

```shell
cp -R custom $HOME/.jupyter
```
This will automatically enable the `noTeXbook` theme as the **default** theme for all Jupyter notebook. 

See [here](https://stackoverflow.com/questions/32156248/how-do-i-set-custom-css-for-my-ipython-ihaskell-jupyter-notebook/34742362#34742362) for more information on Customising Notebook style.



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
`[(1)]` : `port·man·teau | \ pȯrt-ˈman-(ˌ)tō` <br />
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







