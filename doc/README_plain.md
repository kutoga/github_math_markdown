# Github: Math-Markdown

Ever wanted to use formulas in your markdown-files on GitHub? Unfortunately, this feature is not enabled by GitHub.
Therefore, one might generate images with the formulas and insert them to the markdown-file. This is a relatively
"painful" process. Another solution is the standalone script `md_replace_math.py` in repository:

Just execute `cat MY_MARKDOWN_FILE.md | python3 ./md_replace_math.py --imgdir ./img > MY_MARKDOW_FILE_WITH_MATH.md`

The parameter `--imgdir` forces to store the generated (vector) math SVG-images to the given directory. If this parameter
is not present, the generated markdown document will have links to an external service. In this case, the document
cannot be viewed without an internet connection.

As many other implementations do, text between dollar-signs (=`$`) is interpreted as math. The start and the end
dollar sign must be on the same line.

## Examples
Given the following formula:

$
x^2+\exp\left(\int\limits_{-\infty}^{a} \sin(x)\exp(x)\mathrm{d}x\right)x^{x}$

This will result in:

$x^2+\exp\left(\int\limits_{-\infty}^{a} \sin(x)\exp(x)\mathrm{d}x\right)x^{x}$

Some more formulas:

$
f(x)=g(x)h(x)\Rightarrow f^{*}(x)=g^{*}(x)h^{*}(x)$

$\Rightarrow$

$f(x)=g(x)h(x)\Rightarrow f^{*}(x)=g^{*}(x)h^{*}(x)$



$
f(x)=c g(x), c\neq 0 \Rightarrow f^{*}(x)=g^{*}(x)$

$\Rightarrow$

$f(x)=c g(x), c\neq 0 \Rightarrow f^{*}(x)=g^{*}(x)$

etc.

## Notes

This repsoitory itself uses the described script to insert the math formulas. There is a super-simple `Makefile`
which is used to generate the final `README.md`.

