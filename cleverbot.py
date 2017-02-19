# -*- coding: utf-8 -*-
import urllib
import json

class Cleverbot:

    def __init__(self, apikey):

        self.URL = 'https://www.cleverbot.com/getreply'
        self.apiUrl = "{}?key={}&wrapper=python-wrapper".format(self.URL, apikey)
        self.ERRORS = {401: 'Cleverbot API key not valid',
                       404: 'Cleverbot API not found',
                       413: 'Cleverbot API request too large. Please limit requests to 8KB',
                       502: 'Unable to get reply from API server, please contact Cleverbot Support',
                       503: 'Cleverbot API: Too many requests from client',
                       504: 'Unable to get reply from API server, please contact Cleverbot Support'}

        try:
                self.request = urllib.urlopen(self.apiUrl)


        except urllib.HTTPError as err:
                if err.code in self.ERRORS:
                        print self.ERRORS[err.code]
                else:
                        raise

        self.response = json.loads(self.request.read())
        self.cs = self.response['cs']

    def ask(self, question):
        question = urllib.quote_plus(question.encode('utf8'))
        qUrl = "{}&input={}&cs={}".format(self.apiUrl, question, self.cs)
        response = json.loads(urllib.urlopen(qUrl).read())
        self.cs = response['cs']
        print response['output']
        return response['output']
