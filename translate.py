import re

from googletrans import Translator

translator = Translator()


class Blurb(object):
  def __init__(self, x, y, w, h, text, confidence=100.0):
    self.x=x
    self.y=y
    self.w=w
    self.h=h
    self.text = text
    self.confidence = confidence

  def clean_text(self):
    text = self.text
    text = re.sub(r"\n", "", text)
    return text

  def __unicode__(self):
    return str(self.x)+','+str(self.y)+' '+str(self.w)+'x'+str(self.h)+' '+ str(self.confidence)+'% :'+ self.text


class TranslatedBlurb(Blurb):
  def __init__(self, x, y, w, h, text, confidence, translation):
    Blurb.__init__(self, x, y, w, h, text, confidence)
    self.translation = translation

  @classmethod
  def as_translated(cls, parent, translation):
    return cls(parent.x,
               parent.y,
               parent.w,
               parent.h,
               parent.text,
               parent.confidence,
               translation)


def translate_text(text):
    translatedText  = translator.translate(text, dest='en')
    return translatedText.text.encode('utf-8')


def translate_blurb(blurb):
    translation = translate_text(blurb.clean_text())
    return TranslatedBlurb.as_translated(blurb, translation)
