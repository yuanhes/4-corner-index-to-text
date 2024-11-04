# 4CornerIndex-to-Text
Translate the 4-corner indexes to Chinese text.

## Motivation: 
A few days ago, my friend [SUN ZHIZHENG](https://kpee.art/81), who is a writer, shared a post on social media, where he mentioned the concept of creating a book titled 《 $\pi$ 》: use the 4-corner index method to encode the digits of $\pi$ into an endless sequence of Chinese characters, forming a book without a final page. The idea fascinated me and sparked my imagination. Inspired by this, I decided to try bringing it to life using Python here.

## And app for translating input number as 4-corner indexes to Chinese.
http://yuanhes.com/translate_4CI


## My Steps:

1. Extract the 4CornerIndex mapping file from the `html` file converted from the original source `.chm` file.
   - Text version with count: https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/results/extracted_map.txt
   - Json version: https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/results/4CornerIndex_mapping.json

2. Generate large number of digits of the constant $\pi$.
   - $\pi$ of 1 million digits: https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/pi_calculation/pi50m/pi1m.txt
   - $\pi$ of 50 million digits: not uploaded due to large file size
 
3. Generate text with translating the digits of $\pi$ as 4-corner indexes to Chinese.
   - Text from $\pi$ of 1 million digits: https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/text_from_pi_1M_digits.txt
   - Text from $\pi$ of 50 million digits: https://github.com/yuanhes/4CornerIndex-to-Text/blob/main/text_from_pi_50M_digits.txt



***

**References:**

- 四角号码检字表（勘误版）.zip 来源：http://bbs.unispim.com/forum.php?mod=viewthread&tid=31674
- Pi digits source: https://www.angio.net/pi/digits.html
  > "50 million digits (compressed, special): You can download 50 million from the Pi searcher [here](https://www.angio.net/pi/pi50.4.bin). These digits are packed together two per byte, so you'll have to download, compile, and use [this program](https://www.angio.net/pi/printpi.c) to print them. Geeks only, sorry."
- Found a program [y-cruncher](http://www.numberworld.org/y-cruncher) for computing large number of digits of irrational constants, under studying how to use it.
