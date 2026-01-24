# Examples

In order to find:

- words with a meaning similar to _examples_
```python
from datamuse import Datamuse

muse = Datamuse()
muse.synonyms("examples")
```
```py
>>>
>>> ['representative', 'exemplar', 'lesson']
>>>
```
!!! info "Cache"
    All underlying api calls to the official datamuse api are always cached via the [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache).

    The cache is separate for the [words](https://api.datamuse.com/words?) and [suggestions](https://api.datamuse.com/sug?) api.

- suggestions for the user if they have typed in the word _program_ so far
```python
from datamuse import Datamuse

muse = Datamuse()
muse.suggestions("programm")
```
```py
>>>
>>> ['programme', 'programming language', 'programmed']
>>>
```