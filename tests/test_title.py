"""
This is a python port of "Goose" orignialy licensed to Gravity.com
under one or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.

Python port was written by Xavier Grangier for Recrutae

Gravity.com licenses this file
to you under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from .test_base import TestExtractionBase


class TestTitle(TestExtractionBase):
    def test_title_opengraph(self):
        article = self.getArticle()
        fields = ["title"]
        self.runArticleAssertions(article=article, fields=fields)

    def test_title_empty(self):
        article = self.getArticle()
        fields = ["title"]
        self.runArticleAssertions(article=article, fields=fields)

    def test_title_splitter(self):
        article = self.getArticle()
        fields = ["title"]
        self.runArticleAssertions(article=article, fields=fields)

    def test_title_sitename(self):
        article = self.getArticle()
        fields = ["title"]
        self.runArticleAssertions(article=article, fields=fields)

    def test_title_issue172(self):
        article = self.getArticle()
        fields = ["title"]
        self.runArticleAssertions(article=article, fields=fields)
