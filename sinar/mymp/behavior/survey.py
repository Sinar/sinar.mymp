from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.textfield import RichText
from sinar.mymp import MessageFactory as _

class ISurvey(form.Schema):
    """
       Marker/Form interface for Survey
    """
    
    # -*- Your Zope schema definitions here ... -*-
    mymp_plan = RichText(
                    title=_(u'Pelan'),
                    description=_(u'Apakah yang Yang Berhormat ingin '
                    'mencapai di kawasan Yang Berhormat dalam '
                    'penggal ini?'),
                    required=False,
                    )

    mymp_role = RichText(
                title=_(u'Peranan Wakil Rakyat'),
                description=_(u'Bagaimanakah atau apakah yang boleh '
                    'dilakukan supaya peranan Ahli Parlimen lebih '
                    'efektif?'),
                required=False,
                )

    mymp_book = RichText(
                title=_(u'Cadangan'),
                description=_(u'Cadangkan satu buku yang Yang Berhomat '
                          'rasa patut dibaca oleh rakyat Malaysia dan '
                          'jelaskan mengapa Yang Berhormat '
                          'mencadangkan buku tersebut.'),
                required=False,
                )

alsoProvides(ISurvey,IFormFieldProvider)
