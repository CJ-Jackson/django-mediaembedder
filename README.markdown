# django-mediaembedder

Automatically produce embed code from media sharing site such as YouTube.  Currently under development.

## Usage

	{% load mediaembedder %}
    {% mediaembedder "http://www.youtube.com/watch?v=sOVLhnOCLMM&feature=g-u-u" width=640 height=368 %}

Width and Height are optional!

## Usage [with Shortcode Application](https://github.com/CJ-Jackson/django-shortcode)

	\[embed url="http://www.youtube.com/watch?v=sOVLhnOCLMM&feature=g-u-u" width="640" height="368" /\]

Width and Height are optional!
