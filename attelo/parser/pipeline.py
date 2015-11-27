"""
Parser made by sequencing other parsers
"""

# FIXME: look into using sklearn.pipeline.Pipeline
# I wasn't too successful last time

from .interface import Parser


class Pipeline(Parser):
    """
    Apply a sequence of parsers.

    NB. For now we assume that these parsers can be
    fitted independently of each other

    Steps should be a tuple of names and parsers, just like
    in scikit
    """
    def __init__(self, steps):
        self._parsers = [p for _, p in steps]

    def fit(self, dpacks, targets, cache=None):
        for parser in self._parsers:
            parser.fit(dpacks, targets, cache=cache)

    def transform(self, dpack):
        for parser in self._parsers:
            dpack = parser.transform(dpack)
        return dpack
