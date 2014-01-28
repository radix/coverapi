from twisted.web.server import Site
from twisted.application import service, internet
from twisted.python.filepath import FilePath

from coverapi import httpapi

router = httpapi.Router(FilePath("coverapi-storage"))

application = service.Application("CoverAPI")

service = internet.TCPServer(8080, Site(router.app.resource()))
service.setServiceParent(application)
