#!/usr/bin/env python3

import re
import unicodedata

from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol


class ConteoPalabras(MRJob):

    OUTPUT_PROTOCOL = RawValueProtocol

    def mapper(self, _, linea):
        # Corrige caracteres Unicode extraídos del PDF, por ejemplo: ﬁ -> fi
        linea = unicodedata.normalize("NFKC", linea).casefold()

        # Obtiene palabras conservando tildes, diéresis y ñ
        palabras = re.findall(r"[a-záéíóúüñ]+", linea)

        for palabra in palabras:
            yield palabra, 1

    def combiner(self, palabra, cantidades):
        yield palabra, sum(cantidades)

    def reducer(self, palabra, cantidades):
        total = sum(cantidades)
        yield None, f"{palabra}, {total}"


if __name__ == "__main__":
    ConteoPalabras.run()
