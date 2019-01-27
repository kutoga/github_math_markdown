# Github: Math-Markdown

Ever wanted to use formulas in your markdown-files on GitHub? Unfortunately, this feature is not enabled by GitHub.
Therefore, one might generate images with the formulas and insert them to the markdown-file. This is a relatively
"painful" process. Another solution is this repsitory:

Just execute `cat MY_MARKDOWN_FILE.md | ./md_replace_math.py --imgdir ./img > MY_MARKDOW_FILE_WITH_MATH.py`

The parameter `--imgdir` forces to store the generated math SVG-images to the given directory. If this parameter
is not present, the generated markdown document will have links to an external service. In this case, the document
cannot be viewed without an internet connection.

As many other implementations do, text between dollar-signs (=`$`) is interpreted as math. The start and the end
dollar sign must be on the same line.

## Examples
Given the following formula:

$
x^2+\exp\left(\int\limits_{-\infty}^{a} \sin(x)\exp(x)\mathrm{d}x\right)x^{x}$

This will result in:

![mathematical expression](doc/img/6e8f7f662a7bde1542dcb3884bc997a3.svg)

Some more formulas:

$
f(x)=g(x)h(x)\Rightarrow f^{*}(x)=g^{*}(x)h^{*}(x)$

![mathematical expression](doc/img/b85f1f515bef42274c3bb29b593a866c.svg)

![mathematical expression](doc/img/01381ac9312352f2700cd1467d14cd6b.svg)



$
f(x)=c g(x), c\neq 0 \Rightarrow f^{*}(x)=g^{*}(x)$

![mathematical expression](doc/img/b85f1f515bef42274c3bb29b593a866c.svg)

![mathematical expression](doc/img/2760bc166732e71b4716c97e0ce25447.svg)

etc.

## Notes

This repsoitory itself uses the described script to insert the math formulas. There is a super-simple `Makefile`
which is used to generate the final `README.md`.

