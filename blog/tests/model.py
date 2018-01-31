# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your tests here.
from django.test import TestCase
from blog.models import Post,Tag,Location,PostLocation,PostTag,Comment

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="this is a title", type=Post.FEATURE, content="some random content")

    def test_getting_content(self):
        """title match content"""
        example = Post.objects.get(title="this is a title")

        self.assertEqual(example.content, 'some random content')
        self.assertEqual(example.type, Post.FEATURE)
