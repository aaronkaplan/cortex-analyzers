#!/usr/bin/env python3
"""
Hello world analyzer example.

Author: aaron@lo-res.org.
License: AGPL 3.0 or higher.

"""
from cortexutils.analyzer import Analyzer


class HelloWorldAnalyzer(Analyzer):
    """A very simple hello world example. Will say 'hello <input>' where
    <input> is the data you call it with.

    If input == "errortest" then return
    an error message.
    If input == "many" then return an array of answers
    Everything else gets copied back with a "hello <input>!"
    """

    def __init__(self):
        Analyzer.__init__(self)
        self.limit = self.get_param('config.limit', '100')

    def run(self):
        """Run the analyzer. Gets called for every invocation. See cortexutils."""
        data = self.get_data()
        if data == "errortest":
            self.error('Hello World error message\n')
        if data == "many":
            self.report({'results': ["Hello %s!" % data, "Here is another result for %s" % data]})
        else:
            self.report({'results': ["Hello %s!" % data]})

    def summary(self, raw):
        """Produce the summary field in the result. See cortexutils."""
        taxonomies = []
        level = "info"
        namespace = "HelloWorld"
        predicate = "World"

        results = raw.get('results')
        rlen = len(results)
        if rlen == 0 or rlen == 1:
            value = "{} hit".format(rlen)
        else:
            value = "{} hits".format(rlen)

        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {"taxonomies": taxonomies}


if __name__ == '__main__':
    HelloWorldAnalyzer().run()
