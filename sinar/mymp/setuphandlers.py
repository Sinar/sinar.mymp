from collective.grok import gs
from sinar.mymp import MessageFactory as _

@gs.importstep(
    name=u'sinar.mymp', 
    title=_('sinar.mymp import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.mymp.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
