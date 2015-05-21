#!/usr/bin/env python
# coding: utf-8
from pyltp import Segmentor


segmentor = Segmentor()
segmentor.load('/downloads/cws.model')


def segment(text):
    if isinstance(text, unicode):
        text = text.encode('utf-8')
    words = segmentor.segment(text)
    return map(lambda x: x.decode('utf-8'), words)

