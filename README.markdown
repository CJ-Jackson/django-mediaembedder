# django-mediaembedder

Automatically produce embed code from media sharing site such as YouTube.

## Requirement

*	Django 1.4 or greater (Due to use of '**kwargs' in Simple Tag )
*	Python 2.7 or (Python 3.2 or greater)
*	[html5lib](http://code.google.com/p/html5lib/)

## Usage

	{% load mediaembedder %}
    {% mediaembedder "http://www.youtube.com/watch?v=sOVLhnOCLMM&feature=g-u-u" width=640 height=368 %}

Width and Height are optional!

## Usage [with Shortcode Application](https://github.com/CJ-Jackson/django-shortcode)

	[embed url="http://www.youtube.com/watch?v=sOVLhnOCLMM&feature=g-u-u" width="640" height="368" /]

Width and Height are optional!
