## `TexBook` theme for Google Colaboratory

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
