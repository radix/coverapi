import json
import cPickle
from StringIO import StringIO
from coverage import coverage
from klein import Klein


class Router(object):
    app = Klein()

    def __init__(self, storage):
        self.storage = storage

    @app.route('/<revision>/<build>', methods=['POST'])
    def upload_coverage(self, request, revision, build):
        data = json.loads(request.content.getvalue())
        for disallowed in '/.':
            for thing in (revision, build):
                assert disallowed not in thing
        f = self.storage.child("coverage-data.%s.%s" % (revision, build))
        f.setContent(cPickle.dumps(data))
        return "Thanks!"


    @app.route('/<revision>.html', methods=['GET'])
    def get_html_coverage(self, request, revision):
        cov = coverage(data_file=self.storage.child("coverage-data").path)
        cov.combine() # lol this deletes the input files, wtf
        io = StringIO()
        cov.report(file=io)
        return io.getvalue()


__all__ = ['Router']
