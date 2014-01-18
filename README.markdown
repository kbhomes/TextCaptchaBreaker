
What is textCAPTCHA?
--------------------

[TextCAPTCHA](http://textcaptcha.com/demo) is a service that provides human readable logic questions designed to create a distinction between humans and computers. For example:

> Fourteen minus 6 = ?

> The colour of a black dog is?

> What is twenty five thousand two hundred and eight as digits?

While created to block automated programs from answering these questions, most, if not all, follow identifiable patterns.

How does TextCaptchaBreaker work?
---------------------------------

TextCaptchaBreaker is a Python application that exploits the predictability of these patterns **with a staggering 99% success rate** (in one run, 9952 of 10000 questions were answered correctly). Some example patterns used by the textCAPTCHA service include the 'words to number' pattern and the 'colour' pattern.

How do the patterns work?
-------------------------

TextCaptchaBreaker hands the question off to each Pattern until one such Pattern is able to return an answer. ColorPattern works as such:

* ColorPattern approaches each question by first tokenizing it (split it into words). 

* The keyword 'colour' is searched for in the tokens. This appears in a question such as *The colour of a black dog is?*. 

* The singular form 'colour' indicates that there is one color in the question itself which is the answer; in this case, ColorPattern iterates over the tokens and returns the first color it sees. If no such color is found, ColorPattern returns None to indicate that it was unable to answer the question.

* If the keyword 'colour' was not found in the tokens, the plural 'colours' is searched for, appearing in questions such as *The list blue, brown, T-shirt, white and purple contains how many colours?*.

* The plural 'colours' lets ColorPattern know to return all the colors that are in the questions. Thus, ColorPattern iterates over the tokens and returns the total count of colors it found.

Similar algorithms exist for other patterns that are employed, such as the BodyPartsPattern, used for questions such as *Cat, apple, finger, elephant or hospital: the body part is?* (singular) and *The list chin, cat, head, toe, T-shirt and hair contains how many body parts?* (plural).

What does this mean for textCAPTCHA?
------------------------------------

The relative ease with which I created TextCaptchaBreaker as well as the impressive 99% success rate shows that text based CAPTCHAs are insufficient protections for any site, high-profile or not. TextCAPTCHA could write and implement new patterns for their questions, but with time (not much) those patterns can be identified.

Text based CAPTCHAs, I believe, are not the correct way to move forward in terms of distinguishing between humans and computers.

How do the other patterns work?
-------------------------------

The patterns identified by TextCaptchaBreaker work similarly to the ColorPattern and BodyPartsPattern described above. The patterns are:

* AddSubtractPattern
* BodyPartsPattern (explained above)
* ColorPattern (explained above)
* DayPattern
* DigitPattern
* NamePattern
* WhichNumberPattern
* WordsToNumberPattern

### AddSubtractPattern

> What is 10 plus 1?

> What is ten - 3?

AddSubtractPattern behaves initially like any other pattern by tokenizing the question. A hardcoded mapping of words to numbers (e.g.: *eight* is 8, *seventeen* is 17) exists. The two operations that are used in this pattern is addition ('plus', '+', or 'add') and subtraction ('minus', '-', or 'subtract').

AddSubtractPattern searches for the location of a token that represents either operator. From there, it looks at the token before it and the token after it, which are the operands of the operation. The operands can be numerals (e.g.: 'eight', 'seventeen'), in which case the mapping is used to obtain integers, or digits (e.g.: '13', '2'), in which case the number is just parsed. The sum of the operation is returned as the answer.

### DayPattern

> Which day from Sunday, Thursday, Tuesday or Monday is part of the weekend?

> What day is today, if yesterday was Wednesday?

If the token 'weekend' is found, DayPattern iterates through all the tokens and returns the first day that is either 'Saturday' or 'Sunday'.

If the token 'today' is found, the question is asking what day today is given either yesterday or today. If the token 'yesterday' is found, the tokens are searched until a day is recognized; that day was 'yesterday', and the next day is returned. If the token 'tomorrow' is found, the tokens are seached until a day is recognized; that day is 'tomorrow', and so the previous day is returned.

### DigitPattern

> What is the 6th digit in 7911863?

If the token 'digit' is found, the question is assumed to be in the above or similar format. A hardcoded mapping of ordinals (e.g.: *1st* and *first* are 1, *2nd* and *second* are 2) is used to identify which digit is to be chosen. The tokens are searched for an ordinal and a number. The specified digit of the specified number is then returned.

### NamePattern

> What is Susan's name?

> If a person is called George, what is their name?

If the token 'name' is found, the question is assumed to be in one of the above or similar formats. Since names are proper nouns, the only candidates for the answer are the words beginning in a capital letter, which are the first word of the sentence and/or the actual name. Words such as 'What', 'If', and 'The' are omitted such that the actual name is the only title-cased token. That token is then returned.

### WhichNumberPattern

> What is the 2nd number in the list nineteen, 23 and twenty nine?

> Forty five, 24, 11, eighty three or 81: which of these is the smallest?

> Sixty two, 14, 75, fifty three, fifty seven or seventy: the largest is?

The question is assumed to be in a format similar any of the above. In this pattern, there are two types of numbers: those that are standalone (e.g.: *two*, *nine*) and those that can be compounded (e.g.: *twenty*, *ninety*); mappings exist to separate these two types.

The tokens are iterated to find the numbers. It first checks if the token is a number, as in *38*; if it is, the number is saved. If it was not a number, it is then checked to see if it is in the standalone number mapping; if it exists in the mapping, the number is saved. If it is not a standalone number either, it is checked to see if it is a compoundable number. If it is, the next token is checked to see if it is standalone; if that is, then the compound number is added to the standalone number, which is then saved. The standalone number that was 'peeked' at is skipped. If there was no standalone number after the compound number, the compound number is simply saved. After this step, there is an ordered list of the numbers that appear in the question.

Next, and ordinal number is searched for in the token. If one is found, then the question is asking for a number at the specific location, and that number is returned. If no ordinal number is found, the question is asking for the smallest or the largest number of the list. As such, the keywords 'largest', 'biggest', 'highest', 'smallest' and 'lowest' are searched for to find whether to return the min() or max() of the list.

### WordsToNumberPattern

> Enter the number fifteen thousand six hundred and eighty six in digits:

> What is sixty four thousand six hundred and sixty one as digits?

WordsToNumberPattern works by filtering out all tokens except for numbers and the word 'and'. What remains is a representation of the desired number in words. This representation is fed into [WolframAlpha](http://wolframalpha.com/), whose result is parsed for the actual number.