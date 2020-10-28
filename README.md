# TeXbook  Jupyter Notebook Theme

## Prologue:  <img src="https://render.githubusercontent.com/render/math?math=%5Ctextbf%7B%5CTeX%5Ctext%7Bbook%7D%7D">  shall be _thy_ name

When I designed this theme, I was aiming towards a notebook experience which had the elegance and sobriety of a `LaTeX`-generated article, perfectly combined with the flexibility and interactivity of Jupyter notebooks.
And so <img src="https://render.githubusercontent.com/render/math?math=%5CTeX%5Ctext%7Bbook%7D"> seemed to be the most obvious solution for a name, a unique [portmanteau](https://www.merriam-webster.com/dictionary/portmanteau)
[(1)]( "Pronunciation"),
blending together the words <img src="https://render.githubusercontent.com/render/math?math=%5CLaTeX"> and *note**book** *. 
*Incidentally*, this is also the name of the 
[Donald E. Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)'s [book](http://www.ctex.org/documents/shredder/src/texbook.pdf) on `TeX`.

That was the omen.. 🤩

> Right!, One!... Two!... Five! [(2)]("Monty Python and the Holy Grail")

The <img src="https://render.githubusercontent.com/render/math?math=%5CTeX%5Ctext%7Bbook%7D"> Jupyter notebook theme wishes to pay a tribute of gratitude (in the name, and in the content) to two of the technologies I do use the most as researcher and data scientist.

---
`[(1)]` : `port·​man·​teau | \ pȯrt-ˈman-(ˌ)tō` <br />
`[(2)]`: [The Holy Hand Grenade](https://www.youtube.com/watch?v=xOrgLj9lOwk) - Monty Python and the Holy Grail
    

#### `TeXbook` Jupyter theme in a Nutshell

- *Computer Modern* fonts for Markdown typesetting;
	- *Computer Modern Typesetting* for Markdown Mono	
- `Fira Code` (_open source_) font as the default `monospace` for the **Code** editor (with ligatures support);
- `Hack` (_open source_) font as the default `monospace` font for **Markdown** editor (slightly better for text writing, _ed._);
- `md` and `code` colour highlight editor themes based on Material Design colour scheme.
    - other themes also provided;
    - very easy to create your own custom theme (just a series of CSS variables should do the trick)
- Special formatting for `pandas.DataFrame`
- Extra `ad-hoc` CSS classes for Markdown and Code (*output*) formatting

**Last but not least**: to make things even more interesting, the `TeXbook` theme has been made available in three different flavours: 

1. **Full-fledged** _custom_ Jupyter notebook theme;
2. `pip-installable` Custom **IPython magic** (`%texify`);
3. Custom theme integration for Google Colaboratory Notebooks (via the [Stylus](https://en.wikipedia.org/wiki/Stylus_(browser_extension)) browser extension) (**still experimental**).

### Sneak Peek?

Here is a [**Preview**](https://leriomaggio.github.io/texbook-jupyter-theme/) of how the theme looks like!

---

## How to 

Installing and Enabling the `TeXbook` theme for your Jupyter notebooks varies depending on which of the three theme settings you decided to use. 

1. [Jupyter Notebook Custom Theme](#custom)
2. [Custom IPython Magic](#magic)
3. [Google Colaboratory Theme](#colab)

<a name="custom"></a>
### Using `TeXbook` as default Jupyter Notebook theme

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

<a name="magic"></a>
### Using `%texify` custom IPython magic

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

**Example**: `%texify --code-mono-font Monaco` will enable the `TeXbook` theme using 
the `Monaco` font instead of the default `Fira Code` for code editor.

<a name="colab"></a>
### `TexBook` theme for Google Colaboratory

An experimental porting of `TeXbook` to **Google Colaboratory** Notebooks is available as a 
[Stylus](https://en.wikipedia.org/wiki/Stylus_(browser_extension)) importable style. 

#### Why Stylus?

The HTML of a Colaboratory notebook is nothing similar to the standard Jupyter notebook HTML structure
(so the `custom-css` cannot work). In addition, every single Colaboratory Notebook Cell executes and generates
a new `HTML iframe`, which also makes the `texify` IPython magic pretty much useless.

Therefore, the *only* solution I could resort to was using **Stylus**.
Unfortunately it is not as customisable and portable as the IPython magic is, but hey?! Better than nothing :)

#### Install TeXbook Colaboratory Theme 

1. Install Stylus Browser Extension (**only available for Mozilla Firefox** and **Google Chrome**)
    - [Mozilla Firefox Stylus](https://addons.mozilla.org/en-GB/firefox/addon/styl-us/)
    - [Google Chrome Stylus](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne?hl=en)

2. Import `google_colab_stylus_theme.json` into stylus

    2.1 Alternatively, it is also possible to Copy&Paste the CSS as it is in the Stylus CSS Editor
        - [Google Chrome Stylus](./google_colab_stylus_chrome.css)
        - [Mozilla Stylus](./google_colab_stylus_mozilla.css)

3. Enjoy!

As the general TeXbook theme, customising the Colaboratory Theme is as easy as tweaking 
a bunch of CSS variables:

* `--txbk-content-font-size` : Set the font size of the main notebook content;
* `--txbk-content-line-height` : Set Line height of the main notebook content;
* `--txbk-code-font-family` : Set the font family for code editor;
* `--txbk-md-font-family`: Set the font family for markdown editor;
* `--txbk-code-font-size`: Set the font size for the code editor;
* `--txbk-content-mono-font-size`: Set the font-size of rendered mono Markdown.
