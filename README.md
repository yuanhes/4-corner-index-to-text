# 4CornerIndex-to-Text
Translate the 4-corner indexes to Chinese text.

## Motivation: 
A few days ago, my friend [SUN ZHIZHENG](https://kpee.art/81), who is a writer, shared a [post](https://mp.weixin.qq.com/s/LyUCRKytMIxOkjeeRd1OYg) on social media, where he mentioned the concept of creating a book titled 《 $\pi$ 》: use the 4-corner index method to encode the digits of $\pi$ into an endless sequence of Chinese characters, forming a book without a final page. The idea fascinated me and sparked my imagination. Inspired by this, I decided to try bringing it to life using Python here. (of course only to a certain extent :) ).


## My Steps:

1. Extract the 4CornerIndex mapping file from the `html` file converted from the original source `.chm` file.
   - Text version with count: [extracted_map.txt](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/results/extracted_map.txt)
   - Json version: [4CornerIndex_mapping.json](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/results/4CornerIndex_mapping.json)

2. Generate large number of digits of the constant $\pi$.
   - $\pi$ of 1 million digits: [pi1m.txt](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/pi_calculation/pi50m/pi1m.txt)
   - $\pi$ of 50 million digits: [pi50m.txt](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/pi_calculation/pi50m/pi50m.txt)
 
3. Generate text with translating the digits of $\pi$ as 4-corner indexes to Chinese.
   - Text from $\pi$ of 1 million digits: [text_from_pi_1M_digits.txt](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/text_from_pi_1M_digits.txt)
   - Text from $\pi$ of 50 million digits: [text_from_pi_50M_digits.txt](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/text_from_pi_50M_digits.txt)

4. Render the text to pdf by using Tex. (IDE: TeXstudio ; Compiler: XeLaTex )
   - Pi Book of text from $\pi$ of 1 million digits: [tex](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/PiBook/PiBook_1M.tex) , [pdf](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/PiBook/PiBook_1M.pdf)
   - Pi Book of text from $\pi$ of 50 million digits: [tex](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/PiBook/PiBook_50M.tex) , [pdf](https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/PiBook/PiBook_50M.pdf)


#### - PS: Naturally this can be extended to other irrational numbers like $e$, $\sqrt2$, golden ratio ($1+\sqrt5/2$) .


## App:
I turned it into an app for translating input number as 4-corner indexes to Chinese:
- http://yuanhes.com/translate_4CI

(As I tried, the phone browsers cannot display most of the characters due to encoding issue, while the computer browsers perform much better.)

***

**References:**

- 四角号码检字表（勘误版）.zip 来源：http://bbs.unispim.com/forum.php?mod=viewthread&tid=31674
- Pi digits source: https://www.angio.net/pi/digits.html
  > "50 million digits (compressed, special): You can download 50 million from the Pi searcher [here](https://www.angio.net/pi/pi50.4.bin). These digits are packed together two per byte, so you'll have to download, compile, and use [this program](https://www.angio.net/pi/printpi.c) to print them. Geeks only, sorry."
- Found a program [y-cruncher](http://www.numberworld.org/y-cruncher) for computing large number of digits of irrational constants, under studying how to use it.
- Wikipedia page for 4-corner method:  [Four-corner method - Wikipedia](https://en.wikipedia.org/wiki/Four-corner_method)
- Method for handling the rendering issue of Chinese charactes of different fonts (character sets): [xetex - Vertical Chinese text that contains characters in a "CJK fallback family font" - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/110588/vertical-chinese-text-that-contains-characters-in-a-cjk-fallback-family-font)
